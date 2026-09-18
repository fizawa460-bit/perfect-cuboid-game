#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOUND = HERE / "bounded_exact_deletion_correlation.py"
BOUND_BLOB = "98d84c925af74c35b99001b08d8428f997ab63ea"
SCHEMA = "STAGE32EX5_HPADJ22_FULL_BCHUNK_CERT_V1"
QCAP = 4992
OVERFLOW = 4993


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_bound():
    req(BOUND.is_file() and git_blob(BOUND) == BOUND_BLOB, "bounded gate blob drift")
    spec = importlib.util.spec_from_file_location("hpadj22_bounded_locked_for_bchunk", BOUND)
    req(spec is not None and spec.loader is not None, "cannot load bounded gate")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def qcap(q: int) -> int:
    return q if q <= QCAP else OVERFLOW


def build_joint_bc_shard(H: int, b0: int, b1: int):
    req(0 <= b0 <= b1 <= H, "invalid BC shard")
    BC = [None] * (H + 1)
    for b in range(b0, b1 + 1):
        BC[b] = [[[defaultdict(int) for _ in range(2)] for __ in range(8)] for ___ in range(H + 1)]

    B = [[[defaultdict(int) for _ in range(2)] for __ in range(3)] for ___ in range(H + 1)]
    C = [[[defaultdict(int) for _ in range(2)] for __ in range(4)] for ___ in range(H + 1)]
    for m in range(H + 1):
        for x9 in range(m + 1):
            x5 = m - x9
            B[m][int(x5 > 0) + int(x9 > 0)][x9 & 1][qcap(x5*x5 + x9*x9)] += 1
        for x8 in range(m + 1):
            for x10 in range(m - x8 + 1):
                x6 = m - x8 - x10
                C[m][int(x6 > 0) + int(x8 > 0) + int(x10 > 0)][(x8 + x10) & 1][
                    qcap(x6*x6 + x8*x8 + x10*x10)
                ] += 1

    # Unequal x0<x1 branch.
    for x0 in range(H + 1):
        extra = int(x0 > 0) + 1
        x0par = x0 & 1
        for x1 in range(x0 + 1, H + 1):
            x1par = x1 & 1
            q01 = x0*x0 + x1*x1
            for b in range(max(b0, x1), b1 + 1):
                g2 = b - x1
                for c in range(x0, H + 1):
                    g3 = c - x0
                    dst = BC[b][c]
                    for sb in range(3):
                        for x9par in (0, 1):
                            left = B[g2][sb][x9par]
                            if not left:
                                continue
                            required_cpar = x9par ^ x1par
                            r = x0par ^ x1par ^ x9par
                            for sc in range(4):
                                right = C[g3][sc][required_cpar]
                                if not right:
                                    continue
                                out = dst[sb + sc + extra][r]
                                for ql, vl in left.items():
                                    for qr, vr in right.items():
                                        out[qcap(q01 + ql + qr)] += vl * vr

    # Equal x0=x1=t, lex-strict x5<x8. P tracks x6+x10 with x10 parity and q.
    P = [[[defaultdict(int) for _ in range(2)] for __ in range(3)] for ___ in range(H + 1)]
    for m in range(H + 1):
        for x10 in range(m + 1):
            x6 = m - x10
            P[m][int(x6 > 0) + int(x10 > 0)][x10 & 1][qcap(x6*x6 + x10*x10)] += 1

    for t in range(H + 1):
        et = 2 * int(t > 0)
        for x5 in range(H - t + 1):
            for x9 in range(H - t - x5 + 1):
                b = t + x5 + x9
                if not (b0 <= b <= b1):
                    continue
                r = x9 & 1
                for x8 in range(x5 + 1, H - t + 1):
                    qbase = 2*t*t + x5*x5 + x8*x8 + x9*x9
                    sbase = et + int(x5 > 0) + 1 + int(x9 > 0)
                    need = (t + x8 + x9) & 1
                    for m in range(H - t - x8 + 1):
                        c = t + x8 + m
                        dst = BC[b][c]
                        for sp in range(3):
                            pd = P[m][sp][need]
                            if not pd:
                                continue
                            out = dst[sbase + sp][r]
                            for qp, vp in pd.items():
                                out[qcap(qbase + qp)] += vp

    # Equal x5=x8=u branch, enforce x6<=x9.
    for t in range(H + 1):
        et = 2 * int(t > 0)
        for u in range(H - t + 1):
            eu = 2 * int(u > 0)
            for x9 in range(H - t - u + 1):
                b = t + u + x9
                if not (b0 <= b <= b1):
                    continue
                r = x9 & 1
                for x6 in range(min(x9, H - t - u) + 1):
                    max10 = H - t - u - x6
                    sbase = et + eu + int(x6 > 0) + int(x9 > 0)
                    qbase = 2*t*t + 2*u*u + x6*x6 + x9*x9
                    need = (t + u + x9) & 1
                    for x10 in range(max10 + 1):
                        if (x10 & 1) != need:
                            continue
                        c = t + u + x6 + x10
                        BC[b][c][sbase + int(x10 > 0)][r][qcap(qbase + x10*x10)] += 1
    return BC


def enc_caps(caps):
    return [[int(s), int(B), int(m)] for (s, B), m in sorted(caps.items()) if int(m)]


def compute_chunk(row_index: int, b_start: int, b_stop: int) -> dict:
    req((192*192 + 16*192)//8 == QCAP, "qBC cap no longer covers maximum FULL178 cutoff")
    bnd = load_bound()
    h21 = bnd.load_module(bnd.H21, bnd.H21_BLOB, "hpadj21_bounded_locked_for_hpadj22_bchunk")
    h20 = h21.load_parent()
    h19 = h20.load_parent()
    h18 = h19.load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "hpadj15_locked_for_hpadj22_bchunk")
    p14 = p15.load_parent()
    counter = p14.load_counter()
    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    req(len(rows) == 178 and 0 <= row_index < 178, "row index/coverage drift")
    row_id, g0, d0 = rows[row_index]
    g, d = int(g0), int(d0)
    h = d // 2
    req(0 <= b_start <= b_stop <= h, "invalid b chunk")

    profiles, classes_gt2, tuples_above_second = h21.full_profiles(h, counter, h19)
    joint = build_joint_bc_shard(h, b_start, b_stop)
    K = counter.ceil_div(d - 16*g + 16, 4)
    threshold8 = d*d + 16*d + (32 if g == 0 else 0)
    pos = {interval: i for i, interval in enumerate(p15.PLANNED)}
    acc = {
        i: {"pre": 0, "reject": 0, "h22": 0, "h21_caps": defaultdict(int)}
        for i in range(len(p15.PLANNED))
    }

    for b in range(b_start, b_stop + 1):
        interval = p15.shard_for_b(b)
        dst = acc[pos[interval]]
        for c in range(h + 1):
            jbc = joint[b][c]
            if not any(any(bool(jbc[s][r]) for r in (0, 1)) for s in range(8)):
                continue
            c3 = counter.component3(d, b, c)
            if c3 < 0:
                continue
            caps = bnd.x4_caps(h16, h, g, b, c)
            for a in range(h + 1):
                ca = counter.component_a(d, a)
                if ca < 0:
                    continue
                srem = min(16, d) + ca + c3
                for sbc in range(8):
                    for r in (0, 1):
                        qbc_hist = jbc[sbc][r]
                        left_total = sum(qbc_hist.values())
                        if not left_total:
                            continue
                        for sa in range(4):
                            tiers = profiles[a][sa]
                            if not tiers:
                                continue
                            support = sbc + sa
                            es = bnd.eligible_e(counter, d, g, h, a, b, c, support, srem, K)
                            if not es:
                                continue
                            normal_sum = sum(19*d - 5*e + 1 for e in es)
                            ne = len(es)
                            a_total = sum(mult for _, mult in tiers)
                            dst["pre"] += left_total * a_total * normal_sum
                            for qa, va in tiers:
                                s = bnd.survivor_count(caps, r, qa)
                                for e in es:
                                    B = 19*d - 5*e + 1
                                    req(B > 0 and B % 2 == 1, f"normal block drift {(g,d,e,B)}")
                                    dst["h21_caps"][(s, B)] += left_total * int(va) * B
                                survive_bc = sum(vb for qb, vb in qbc_hist.items()
                                                 if 8 * (qa + qb) <= threshold8)
                                reject_bc = left_total - survive_bc
                                dst["reject"] += reject_bc * int(va) * normal_sum
                                dst["h22"] += survive_bc * int(va) * s * ne

    interval_records = []
    for i, interval in enumerate(p15.PLANNED):
        x = acc[i]
        if x["pre"] or x["reject"] or x["h22"] or x["h21_caps"]:
            interval_records.append({
                "interval_position": i,
                "b_interval": list(interval),
                "pre_mass": int(x["pre"]),
                "rejected_mass": int(x["reject"]),
                "hpadj22_exact_survivors": int(x["h22"]),
                "hpadj21_caps": enc_caps(x["h21_caps"]),
            })

    out = {
        "schema": SCHEMA,
        "route_id": "HPADJ-22_ex5",
        "status": "EXACT_BCHUNK_COMPLETE_NO_MATHEMATICAL_CREDIT",
        "row": {"index": row_index, "row_id": row_id, "g": g, "d": d, "h": h},
        "b_range": {"start": b_start, "stop": b_stop},
        "qbc_cap": {"max_exact_cutoff": QCAP, "overflow": OVERFLOW},
        "source_locks": {
            "bounded_gate_git_blob": BOUND_BLOB,
            "hpadj21_bounded_git_blob": bnd.H21_BLOB,
            "hpadj20_parent_git_blob": h21.PARENT_BLOB,
            "full178_manifest_blob_sha1": p14.LOCKS["manifest_blob"],
            "hpadj10_counter_blob_sha1": p14.LOCKS["hpadj10_counter_blob"],
        },
        "profile": {
            "classes_with_more_than_two_qA_bins": classes_gt2,
            "tuples_above_second_qA_level": tuples_above_second,
        },
        "interval_records": interval_records,
        "semantics": {
            "b_partition_is_execution_only": True,
            "qbc_overflow_cap_is_exact_for_hpadj08_survival_test": True,
            "same_pre_domain_population_as_hpadj21": True,
            "same_picard_qA_rule_as_hpadj21": True,
            "exact_hpadj08_deletion_location_retained": True,
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
    out["canonical_sha256_without_this_field"] = canonical(out)
    return out


def validate_obj(d: dict, row_index: int, b_start: int, b_stop: int) -> dict:
    req(d.get("schema") == SCHEMA, "chunk schema drift")
    req(int(d["row"]["index"]) == row_index, "chunk row index drift")
    req(int(d["b_range"]["start"]) == b_start and int(d["b_range"]["stop"]) == b_stop,
        "chunk b range drift")
    req(d["source_locks"]["bounded_gate_git_blob"] == BOUND_BLOB, "bounded gate source drift")
    req(d["qbc_cap"] == {"max_exact_cutoff": QCAP, "overflow": OVERFLOW}, "qBC cap drift")
    req(d.get("canonical_sha256_without_this_field") == canonical(d), "chunk canonical drift")
    req(all(v is False for v in d["credit_firewall"].values()), "chunk credit firewall")
    return d


def validate(path: Path, row_index: int, b_start: int, b_stop: int) -> dict:
    req(path.is_file(), "missing chunk certificate")
    return validate_obj(json.loads(path.read_text()), row_index, b_start, b_stop)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--row-index", type=int, required=True)
    ap.add_argument("--b-start", type=int, required=True)
    ap.add_argument("--b-stop", type=int, required=True)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--verify-existing", type=Path)
    args = ap.parse_args()
    if args.verify_existing is not None:
        d = validate(args.verify_existing, args.row_index, args.b_start, args.b_stop)
        print("VALID_HPADJ22_BCHUNK=" + d["canonical_sha256_without_this_field"])
        return
    req(args.output is not None, "--output required")
    d = compute_chunk(args.row_index, args.b_start, args.b_stop)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(d, sort_keys=True, separators=(",", ":")) + "\n")
    print(json.dumps({
        "row_index": args.row_index,
        "row_id": d["row"]["row_id"],
        "b_start": args.b_start,
        "b_stop": args.b_stop,
        "bytes": args.output.stat().st_size,
        "canonical": d["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
