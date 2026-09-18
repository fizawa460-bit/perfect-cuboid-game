#!/usr/bin/env python3
from __future__ import annotations

import bisect
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "run_full_bband.py"
BASE_BLOB = "2c998a190baaf5f29b33a91fd9efedbb036cef46"
H21_CARRY_RUN = 35275839413
H21_CARRY_ARTIFACT_ID = 10519913594
H21_CARRY_ARTIFACT_DIGEST = "sha256:366e93ff132652d830e86ab4a46392a1e0fd90185110863a9805fa0ef97f4499"
H21_MISSING_ROWS = {20, 21, 44, 88, 171}


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_base():
    global _BASE_CACHE
    if _BASE_CACHE is not None:
        return _BASE_CACHE
    req(BASE.is_file() and git_blob(BASE) == BASE_BLOB, "base worker blob drift")
    spec = importlib.util.spec_from_file_location("hpadj22_base_locked_for_fast", BASE)
    req(spec is not None and spec.loader is not None, "cannot load base worker")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    _BASE_CACHE = mod
    return mod


def load_h21_cells(root: Path, base) -> dict[tuple[int, int], dict]:
    files = sorted(root.rglob("hpadj21-row-*.json"))
    req(len(files) == 173, f"expected 173 carried HPADJ21 rows, got {len(files)}")
    out: dict[tuple[int, int], dict] = {}
    seen_rows = set()
    for p in files:
        d = json.loads(p.read_text())
        req(d.get("schema") == "STAGE32EX5_HPADJ21_FULL_QA_ROW_CERT_V1", f"schema drift {p}")
        req(d.get("status") == "EXACT_FULL_QA_ROW_COMPLETE_HOSTILE_AUDIT_REQUIRED", f"status drift {p}")
        req(d.get("canonical_sha256_without_this_field") == base.canonical(d), f"canonical drift {p}")
        req(all(v is False for v in d["credit_firewall"].values()), f"credit firewall drift {p}")
        src = d["source_locks"]
        req(src["bounded_pilot_git_blob"] == "266c7eb92fc971df24733f651c245cd14a32e494", "bounded pilot lock")
        req(src["full178_manifest_blob_sha1"] == "0a46b34e278688240656b4977e9cb7f589e90e06", "manifest lock")
        req(src["hpadj10_counter_blob_sha1"] == "eebeb47f91df22461c33e9974d63aceca4da3b52", "counter lock")
        req(src["hpadj20_parent_git_blob"] == "837d647cfcbc96bbe384e564f449cd7042a46d48", "HPADJ20 lock")
        idx = int(d["row"]["index"])
        req(idx not in seen_rows, f"duplicate HPADJ21 row {idx}")
        seen_rows.add(idx)
        req(len(d["cell_records"]) == 8, f"HPADJ21 cell coverage row {idx}")
        for cell in d["cell_records"]:
            pos = int(cell["interval_position"])
            req(0 <= pos < 8, f"HPADJ21 interval position row {idx}")
            req(tuple(cell["b_interval"]) == base.PLANNED[pos], f"HPADJ21 interval geometry row {idx}/{pos}")
            out[(idx, pos)] = cell
    req(seen_rows == set(range(178)) - H21_MISSING_ROWS, "HPADJ21 carried row identity drift")
    req(len(out) == 173 * 8, "HPADJ21 carried cell coverage")
    return out


def build_qbc_prefix(joint, b0: int, b1: int, hmax: int):
    pref = {}
    for b in range(b0, b1 + 1):
        for c in range(hmax + 1):
            jbc = joint[b][c]
            for sbc in range(8):
                for r in (0, 1):
                    hist = jbc[sbc][r]
                    if not hist:
                        continue
                    qs = []
                    ps = []
                    total = 0
                    for q, v in sorted(hist.items()):
                        total += int(v)
                        qs.append(int(q))
                        ps.append(total)
                    pref[(b, c, sbc, r)] = (qs, ps, total)
    return pref


def qbc_count_le(rec, limit: int) -> int:
    if rec is None:
        return 0
    qs, ps, _ = rec
    i = bisect.bisect_right(qs, limit)
    return 0 if i == 0 else int(ps[i - 1])


def eligible_stats(d: int, g: int, h: int, a: int, b: int, c: int,
                   support: int, srem: int, K: int):
    legacy = 8 if g == 0 else 4
    qneed = K - support
    if qneed > 0 and srem < qneed:
        return None
    M = a + b + c
    lower = max(legacy, K, d - 4*g + 4, M, M + max(0, qneed))
    upper = min((19*d)//5, 3*d, 3*d - (b-c))
    if lower > upper:
        return None
    lo = lower if lower % 2 == 0 else lower + 1
    hi = upper if upper % 2 == 0 else upper - 1
    if lo > hi:
        return None
    n = (hi - lo)//2 + 1
    sum_e = n * (lo + hi) // 2
    normal_sum = n * (19*d + 1) - 5 * sum_e
    excluded = set()
    e_n358 = 3*d - (b-c)
    if b <= h - 5 and support + srem == K and e_n358 - M >= srem:
        excluded.add(e_n358)
    if g == 1 and d == 8:
        excluded.add(8)
    for ex in excluded:
        if lo <= ex <= hi and ex % 2 == 0:
            n -= 1
            normal_sum -= 19*d - 5*ex + 1
    if n <= 0:
        return None
    return normal_sum, n


def compute_row_cell_fast(ctx, qbc_pref, band_position: int, row_index: int, h21_cells: dict) -> dict:
    base = load_base()
    req(row_index not in H21_MISSING_ROWS, f"row {row_index} lacks carried HPADJ21 cell certificate")
    bc, bnd, h21, _, h16, p15, p14, counter, rows, rejected, profiles, classes_gt2, tuples_above_second = ctx
    row_id, g0, d0 = rows[row_index]
    g, d = int(g0), int(d0)
    h = d // 2
    interval = base.PLANNED[band_position]
    b0, b1 = interval
    K = counter.ceil_div(d - 16*g + 16, 4)
    threshold_q = (d*d + 16*d + (32 if g == 0 else 0)) // 8
    pre = reject = h22 = 0

    ca_cache = [counter.component_a(d, a) for a in range(h + 1)]
    a_meta = []
    for a in range(h + 1):
        row = []
        for sa in range(4):
            tiers = profiles[a][sa]
            row.append((tiers, sum(int(mult) for _, mult in tiers)))
        a_meta.append(row)

    for b in range(b0, min(b1, h) + 1):
        for c in range(h + 1):
            c3 = counter.component3(d, b, c)
            if c3 < 0:
                continue
            active = False
            for sbc in range(8):
                for r in (0, 1):
                    if (b, c, sbc, r) in qbc_pref:
                        active = True
                        break
                if active:
                    break
            if not active:
                continue

            x4caps = bnd.x4_caps(h16, h, g, b, c)

            # Cache Picard survivor counts by (a,sa,r) once per (b,c).
            qa_surv = {}
            for a in range(h + 1):
                if ca_cache[a] < 0:
                    continue
                for sa in range(4):
                    tiers, _ = a_meta[a][sa]
                    if not tiers:
                        continue
                    for r in (0, 1):
                        qa_surv[(a, sa, r)] = [
                            (int(qa), int(va), bnd.survivor_count(x4caps, r, int(qa)))
                            for qa, va in tiers
                        ]

            for a in range(h + 1):
                ca = ca_cache[a]
                if ca < 0:
                    continue
                srem = min(16, d) + ca + c3
                # eligible_e is independent of Picard parity r and depends on sbc+sa only.
                support_stats = {}
                for support in range(11):
                    stats = eligible_stats(d, g, h, a, b, c, support, srem, K)
                    if stats is not None:
                        support_stats[support] = stats

                for sbc in range(8):
                    for sa in range(4):
                        tiers, a_total = a_meta[a][sa]
                        if not tiers or not a_total:
                            continue
                        stats = support_stats.get(sbc + sa)
                        if stats is None:
                            continue
                        normal_sum, ne = stats
                        for r in (0, 1):
                            qrec = qbc_pref.get((b, c, sbc, r))
                            if qrec is None:
                                continue
                            left_total = int(qrec[2])
                            pre += left_total * a_total * normal_sum
                            for qa, va, s in qa_surv[(a, sa, r)]:
                                survive_bc = qbc_count_le(qrec, threshold_q - qa)
                                reject_bc = left_total - survive_bc
                                reject += reject_bc * va * normal_sum
                                h22 += survive_bc * va * s * ne

    retained_reject = int(rejected[(interval, g, d)])
    req(reject == retained_reject,
        f"HPADJ08 retained rejected-mass mismatch {(interval,g,d)}: {reject} != {retained_reject}")

    cell = h21_cells[(row_index, band_position)]
    req(pre == int(cell["pre_mass"]), f"HPADJ21 carried pre-mass mismatch {(row_index,band_position)}")
    post = pre - reject
    req(post == int(cell["post_mass"]), f"HPADJ21 carried post-mass mismatch {(row_index,band_position)}")
    h21_num = int(cell["hpadj21_num"])
    h21_den = int(cell["hpadj21_den"])
    h21_floor = int(cell["hpadj21_floor"])
    req(h21_num // h21_den == h21_floor, "HPADJ21 carried floor arithmetic drift")
    req(h22 <= h21_floor, f"HPADJ22 weakened HPADJ21 {(interval,g,d)}")

    out = {
        "schema": base.SCHEMA_ROW,
        "route_id": "HPADJ-22_ex5",
        "band_position": band_position,
        "b_interval": list(interval),
        "row": {"index": row_index, "row_id": row_id, "g": g, "d": d},
        "source_locks": base.row_source_locks(bc, bnd, h21, p14),
        "totals": {
            "pre_mass": pre,
            "rejected_mass": reject,
            "post_mass": post,
            "hpadj21_num": h21_num,
            "hpadj21_den": h21_den,
            "hpadj21_floor": h21_floor,
            "hpadj22_exact_survivors": h22,
            "strict": h22 < h21_floor,
            "improvement": h21_floor - h22,
        },
        "profile": {
            "classes_with_more_than_two_qA_bins": classes_gt2,
            "tuples_above_second_qA_level": tuples_above_second,
        },
        "semantics": {
            "one_exact_hpadj15_b_shard_cell": True,
            "joint_qA_qBC_picard_parity_used": True,
            "retained_hpadj08_rejected_mass_replayed_exactly": True,
            "same_population_as_hpadj21": True,
            "same_picard_qA_rule_as_hpadj21": True,
            "additive_subtraction_used": False,
        },
        "credit_firewall": {
            "partial_output_credit": False,
            "stage32_main_credit": False,
            "full178_completion_credit": False,
            "theorem_credit": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_credit": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = base.canonical(out)
    return out
