#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import hashlib
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
REF = ROOT / "stages/stage32/management/btva-compressed-lift/BTVA-D8-V43-HPADJ21-ROW-REFERENCE.json"
REF_BLOB = "c7c01eb27c4e80598d32261cb498fdccc7264ba9"
REF_CANON = "53e9dd57501b4ed10cd1a60e172c7ac1e255eba46a7b4d592847ba5387a2341d"
INDEXER = ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_indexer.py"
INDEXER_BLOB = "4fb0a8dd34909494bd62646373e42877ed7a3c9e"

HPADJ21_HEAD = "33f63a4c0bb3dde9d56efd895f4e8eb19d9217e2"
ROW_WORKER_REL = Path("stages/stage32-ex5/hpadj-21_ex5/run_full_hist_row.py")
ROW_WORKER_BLOB = "68a3edcf5be71bb75ed97959fcc5f56a2fcecbd7"
COUNTER_BLOB = "eebeb47f91df22461c33e9974d63aceca4da3b52"

ROW_INDEX = 23
ROW_ID = "g0-d008"
G = 0
D = 8
E = 12
H = 4
B = 93

TOP16 = {
    (4,4,4,4),(4,5,3,5),(5,3,4,4),(5,4,3,5),
    (3,5,4,6),(3,4,5,5),(6,3,3,3),(6,4,2,4),
    (4,4,4,6),(4,3,5,3),(3,6,3,7),(3,3,6,4),
    (4,3,5,5),(4,6,2,6),(2,6,4,6),(2,5,5,5),
}
TOP16_SHA256 = "9df7cc14ed5eecf755ce7a6f9d30e7b392f19c2f2393054131b02a5a550e8f27"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, "cannot load " + str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def exact_s_for_block(h16, x: tuple[int, ...]) -> tuple[int, int, int, int, int, int, int]:
    a = x[2] + x[3] + x[7]
    b = x[1] + x[5] + x[9]
    c = x[0] + x[6] + x[8] + x[10]
    t = x[0] + x[1] + x[6] + x[9]
    r = (x[0] + x[8] + x[10]) & 1
    sa = int(x[2] > 0) + int(x[3] > 0) + int(x[7] > 0)
    qA = x[2] * x[2] + x[3] * x[3] + x[7] * x[7]
    xr = h16.a0_interval(H, G, b, c)
    req(xr is not None, f"missing a0 interval {(a,b,c,t)}")
    caps = [[], []]
    left, right = xr
    for xx4 in range(left, right + 1):
        room = -h16.f0(H, G, b, c, xx4)
        req(room >= 0, "q interval construction regression")
        caps[xx4 & 1].append(room // 138)
    caps[0].sort()
    caps[1].sort()
    s = len(caps[r]) - bisect.bisect_left(caps[r], qA)
    return a, b, c, t, r, sa, qA, s


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hpadj21-root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    req(blob(REF) == REF_BLOB, "e12 reference blob drift")
    ref = json.loads(REF.read_text(encoding="utf-8"))
    stored = ref.get("canonical_sha256_without_this_field")
    body = dict(ref); body.pop("canonical_sha256_without_this_field", None)
    req(stored == REF_CANON and csha(body) == REF_CANON, "e12 reference canonical drift")
    pilot = ref["e12_top16_retained_basis_pilot"]
    req(pilot["unsat_base4_count"] == 16 and pilot["unknown_base4_count"] == 0, "top16 pilot drift")
    req(pilot["unsat_terminal_mass"] == 1248525, "top16 unsat mass drift")
    req(csha(sorted([list(x) for x in TOP16])) == TOP16_SHA256, "top16 key digest drift")

    req(blob(INDEXER) == INDEXER_BLOB, "compressed indexer drift")
    sys.path.insert(0, str(INDEXER.parent))
    idxmod = load_module(INDEXER, "stage32_e12_exact_qbin_indexer")
    indexer = idxmod.CompressedTerminalIndexer(E, D)
    req(indexer.normal_budget == 92, "e12 normal budget drift")
    req(int(indexer.exceptional_count) == 164282, "e12 exceptional count drift")
    req(int(indexer.terminal_count) == 15278226, "e12 terminal count drift")

    hp_root = args.hpadj21_root.resolve()
    row_worker = hp_root / ROW_WORKER_REL
    req(row_worker.is_file() and blob(row_worker) == ROW_WORKER_BLOB, "HPADJ21 row worker drift")
    rw = load_module(row_worker, "stage32_e12_exact_qbin_hpadj21_row")
    p = rw.load_pilot()
    h20 = p.load_parent()
    h19 = h20.load_parent()
    h18 = h19.load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "stage32_e12_exact_qbin_hpadj15")
    p14 = p15.load_parent()
    counter = p14.load_counter()
    req(p14.LOCKS["hpadj10_counter_blob"] == COUNTER_BLOB, "HPADJ10 counter identity drift")
    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    row_id, g, d = rows[ROW_INDEX]
    req((row_id, int(g), int(d)) == (ROW_ID, G, D), "HPADJ21 row identity drift")

    cells, BC = p.exact_pilot_cells(p15, p14, counter, [(ROW_ID, G, D)])
    full_profiles, _, _ = p.full_profiles(H, counter, h19)
    A = [[sum(mult for _, mult in full_profiles[a][sa]) for sa in range(4)] for a in range(H + 1)]

    full_caps = {interval: defaultdict(int) for interval in p15.PLANNED}
    K = counter.ceil_div(D - 16 * G + 16, 4)
    exact_block_count_by_interval_e = defaultdict(int)

    for b in range(H + 1):
        interval = p15.shard_for_b(b)
        for c in range(H + 1):
            bcv = BC[b][c]
            if not any(any(pair) for pair in bcv):
                continue
            c3 = counter.component3(D, b, c)
            if c3 < 0:
                continue
            exact_surv = p.full_survivors(h16, full_profiles, H, G, b, c)
            for a in range(H + 1):
                if not any(A[a]):
                    continue
                M = a + b + c
                ca = counter.component_a(D, a)
                if ca < 0:
                    continue
                srem = min(16, D) + ca + c3
                for sbc, pair in enumerate(bcv):
                    for r in (0, 1):
                        left = int(pair[r])
                        if not left:
                            continue
                        for sa, right in enumerate(A[a]):
                            if not right:
                                continue
                            fi = exact_surv[a][sa]
                            req(fi is not None, "missing full q profile")
                            support = sbc + sa
                            qneed = K - support
                            if qneed > 0 and srem < qneed:
                                continue
                            lower = max(8, K, D - 4 * G + 4, M, M + max(0, qneed))
                            upper = min((19 * D) // 5, 3 * D, 3 * D - (b - c))
                            if lower > upper:
                                continue
                            excluded = set()
                            e_n358 = 3 * D - (b - c)
                            if b <= H - 5 and support + srem == K and e_n358 - M >= srem:
                                excluded.add(e_n358)
                            lo = lower if lower % 2 == 0 else lower + 1
                            hi = upper if upper % 2 == 0 else upper - 1
                            for e in range(lo, hi + 1, 2):
                                if e in excluded:
                                    continue
                                normal_block = 19 * D - 5 * e + 1
                                exact_block_count_by_interval_e[(interval, e)] += left * int(right)
                                for s0, s1, mult in fi["tiers"]:
                                    ss = s0 if r == 0 else s1
                                    full_caps[interval][(int(ss), normal_block)] += left * int(mult) * normal_block

    for interval in p15.PLANNED:
        info = cells[(interval, G, D)]
        req(sum(full_caps[interval].values()) == int(info["pre_mass"]), "full-cap/pre-mass replay")
        for e, term_cap in info["pre_e_term_caps"].items():
            normal_block = 19 * D - 5 * int(e) + 1
            req(
                exact_block_count_by_interval_e[(interval, int(e))] * normal_block == int(term_cap),
                "e-cap replay",
            )

    exact_removed_caps = {interval: Counter() for interval in p15.PLANNED}
    overlap_by_key = Counter()
    support_hist = Counter()
    ratio_hist = Counter()
    overlap_blocks = 0

    for erank in range(int(indexer.exceptional_count)):
        x = tuple(int(v) for v in indexer.unrank(erank * B))
        req(x[4] == 0, "x4 stride regression")
        a, b, c, t, r, sa, qA, s = exact_s_for_block(h16, x)
        key = (a, b, c, t)
        if key not in TOP16:
            continue
        if not (0 <= a <= H and 0 <= b <= H and 0 <= c <= H):
            continue
        c3 = counter.component3(D, b, c)
        ca = counter.component_a(D, a)
        if c3 < 0 or ca < 0:
            continue
        support = sum(1 for j, v in enumerate(x) if j != 4 and v > 0)
        req(sa == int(x[2] > 0) + int(x[3] > 0) + int(x[7] > 0), "A support drift")
        srem = min(16, D) + ca + c3
        qneed = K - support
        if qneed > 0 and srem < qneed:
            continue
        M = a + b + c
        lower = max(8, K, D - 4 * G + 4, M, M + max(0, qneed))
        upper = min((19 * D) // 5, 3 * D, 3 * D - (b - c))
        if not (lower <= E <= upper):
            continue
        e_n358 = 3 * D - (b - c)
        if b <= H - 5 and support + srem == K and e_n358 - M >= srem and E == e_n358:
            continue

        # Cross-check the concrete qA/parity survivor against the aggregated full-profile tier.
        fi = p.full_survivors(h16, full_profiles, H, G, b, c)[a][sa]
        req(fi is not None, "missing concrete full-profile tier")
        matched = False
        for s0, s1, mult in fi["tiers"]:
            if (s0 if r == 0 else s1) == s:
                matched = True
                break
        req(matched, f"concrete q survivor absent from aggregate tier {(key,r,qA,s)}")

        interval = p15.shard_for_b(b)
        exact_removed_caps[interval][(s, B)] += B
        overlap_blocks += 1
        overlap_by_key[key] += 1
        support_hist[support] += 1
        ratio_hist[s] += 1

    req(overlap_blocks == 1389, f"exact overlap block count drift {overlap_blocks}")
    overlap_terms = overlap_blocks * B
    req(overlap_terms == 129177, "exact overlap terminal mass drift")
    req(set(k[0] for k in [(interval, E) for interval in p15.PLANNED if sum(exact_removed_caps[interval].values())]) == {(0, 11)},
        "e12 top16 overlap escaped first b shard")

    baseline_floor = 0
    joint_floor = 0
    per_interval = []
    for interval in p15.PLANNED:
        info = cells[(interval, G, D)]
        P = int(info["pre_mass"])
        Mpost = int(info["post_mass"])
        caps = dict(full_caps[interval])
        bobj, _, _, _ = h18.optimize_cell_exact_predomain(caps, Mpost)
        bf = bobj.numerator // bobj.denominator
        baseline_floor += bf

        removals = exact_removed_caps[interval]
        removal_mass = sum(removals.values())
        for k, v in removals.items():
            req(k in caps and int(caps[k]) >= int(v), f"exact removal exceeds cap {(interval,k,v,caps.get(k))}")
            caps[k] = int(caps[k]) - int(v)
            if caps[k] == 0:
                del caps[k]
        newP = P - removal_mass
        newM = min(Mpost, newP)  # prior HPADJ08 identities remain adversarial/unknown
        req(sum(caps.values()) == newP, "joint exact-q pre capacity conservation")
        jobj, _, _, _ = h18.optimize_cell_exact_predomain(caps, newM)
        jf = jobj.numerator // jobj.denominator
        joint_floor += jf
        per_interval.append({
            "b_interval": list(interval),
            "pre_mass": P,
            "post_mass": Mpost,
            "btva_exact_qbin_removed_terminal_mass": removal_mass,
            "adversarial_joint_post_mass": newM,
            "baseline_hpadj21_floor": bf,
            "joint_exact_qbin_conservative_floor": jf,
            "floor_improvement": bf - jf,
            "removed_ratio_bins": [
                {"s": int(k[0]), "B": int(k[1]), "removed_terminal_capacity": int(v)}
                for k, v in sorted(removals.items(), key=lambda kv: Fraction(kv[0][0], kv[0][1]))
            ],
        })

    req(baseline_floor == 448431, "baseline HPADJ21 row floor drift")
    req(joint_floor <= baseline_floor, "exact-q joint floor weakened baseline")

    out = {
        "schema": "STAGE32_MAIN_BTVA_D8_E12_HPADJ21_EXACT_QBIN_JOINT_LP_V1",
        "stage": 32,
        "status": "EXACT_QBIN_OVERLAP_AND_CONSERVATIVE_POSTIDENTITY_LP_ZERO_CREDIT",
        "target": {"row_id": ROW_ID, "row_index": ROW_INDEX, "g": G, "d": D, "e": E},
        "overlap": {
            "exact_overlap_block_count": overlap_blocks,
            "exact_overlap_terminal_mass": overlap_terms,
            "overlap_by_base4": [
                {"base4": list(k), "blocks": int(v), "terminals": int(v) * B}
                for k, v in sorted(overlap_by_key.items())
            ],
            "support_histogram": [
                {"support": int(k), "blocks": int(v)} for k, v in sorted(support_hist.items())
            ],
            "exact_q_survivor_histogram": [
                {"s": int(k), "B": B, "blocks": int(v), "terminals": int(v) * B, "ratio": f"{k}/{B}"}
                for k, v in sorted(ratio_hist.items())
            ],
        },
        "joint_lp": {
            "baseline_hpadj21_row_floor": baseline_floor,
            "joint_exact_qbin_conservative_row_floor": joint_floor,
            "certified_floor_improvement_candidate": baseline_floor - joint_floor,
            "btva_removal_ratio_bins_reconstructed_exactly": True,
            "unknown_hpadj08_removed_identity_handled_adversarially": True,
            "post_mass_after_overlap_rule": "min(original_post_mass, exact_remaining_pre_mass)",
            "per_interval": per_interval,
        },
        "semantics": {
            "btva_top16_unsat_source_exact": True,
            "hpadj21_predomain_overlap_exact": True,
            "hpadj21_full_qA_ratio_bin_for_each_removed_block_exact": True,
            "prior_hpadj08_removed_identity_still_unknown": True,
            "joint_lp_is_certified_upper_bound_candidate_not_exact_survivor_identity": True,
            "no_statistical_independence_assumed": True,
            "no_additive_subtraction_used": True,
            "direct_raw_e12_mass_subtraction_from_448431_forbidden": True,
        },
        "source_locks": {
            "main_e12_reference_blob_sha1": REF_BLOB,
            "main_e12_reference_canonical_sha256": REF_CANON,
            "compressed_terminal_indexer_blob_sha1": INDEXER_BLOB,
            "hpadj21_head": HPADJ21_HEAD,
            "hpadj21_row_worker_blob_sha1": ROW_WORKER_BLOB,
            "hpadj10_counter_blob_sha1": COUNTER_BLOB,
            "top16_key_stream_sha256": TOP16_SHA256,
        },
        "firewalls": {
            "main_pruning_credit": False,
            "receiver_credit": False,
            "effectivity_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "full178_complete": False,
            "stage32_closed": False,
            "merge_authorized": False,
            "hostile_audit_required_before_promotion": True,
        },
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("BTVA_E12_EXACT_QBIN_JOINT_SUMMARY=" + json.dumps({
        "overlap_blocks": overlap_blocks,
        "overlap_terminals": overlap_terms,
        "baseline_floor": baseline_floor,
        "joint_floor": joint_floor,
        "candidate_improvement": baseline_floor - joint_floor,
        "qbin_hist": {str(k): int(v) for k, v in sorted(ratio_hist.items())},
        "canonical": out["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
