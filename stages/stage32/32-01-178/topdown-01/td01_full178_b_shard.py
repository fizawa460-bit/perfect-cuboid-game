#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import hashlib
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CONTRACT = HERE / "FULL178-SCALEOUT-CONTRACT.json"
CONTRACT_BLOB = "ca1b195a3ee8e786707e1ef50b404ee8c19f1429"
CONTRACT_CANON = "02a350a4c4c9b5c999767386be499edfa4e635189ff8f0e37db0bece7a00f660"
LOCKS = {
    "compressed_family": (
        "stages/stage32/residual-32-01-production/compressed_terminal_family.py",
        "90ff82ed312dcc0cb32cf207935945f550e29170",
    ),
    "grf02_projected_kernel": (
        "stages/stage32/management/global-residual-feasibility/GRF-02-PROJECTED-KERNEL.json",
        "7c1cda07749fbfb90245995d1def2ae96fb5604b",
    ),
    "corrected_adjunction": (
        "stages/stage32/management/hpadj-07/proof-chain/GENERAL-TYPE-ADJUNCTION-CORRECTION.json",
        "c90b41dcfbd5bd081629a6fa62d9447d43cb3d5e",
    ),
    "main_state_v30": (
        "stages/stage32/MAIN-STATE.json",
        "76bf5e3d9d97297ff5fbee2bf4826a78d125e171",
    ),
}
HMAX = 96
QCAP = 4992
OVERFLOW = 4993
PLANNED = ((0, 11), (12, 23), (24, 35), (36, 47), (48, 59), (60, 71), (72, 83), (84, 96))


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def qcap(q: int) -> int:
    return q if q <= QCAP else OVERFLOW


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def component_a(d: int, a: int) -> int:
    h = d // 2
    return min(13, d - a, d - 2 * a + 4, h + 5)


def component3(d: int, b: int, c: int) -> int:
    return min(9, d - b - c, d - 2 * b, d - 2 * c + 1)


def even_interval_normal_sum_split(d: int, lower: int, upper: int, excluded: set[int]):
    lo = lower if lower % 2 == 0 else lower + 1
    hi = upper if upper % 2 == 0 else upper - 1
    if lo > hi:
        return 0, 0, 0, 0
    n = (hi - lo) // 2 + 1
    total = n * (19 * d + 1) - 5 * (n * (lo + hi) // 2)
    for e in sorted(excluded):
        if lo <= e <= hi and e % 2 == 0:
            total -= 19 * d - 5 * e + 1
            n -= 1
    even = (total + n) // 2
    odd = (total - n) // 2
    req(even + odd == total, "normal parity split mismatch")
    return n, total, even, odd


def build_a():
    table = [[defaultdict(int) for _ in range(4)] for __ in range(HMAX + 1)]
    for a in range(HMAX + 1):
        for x2 in range(a + 1):
            for x3 in range(a - x2 + 1):
                x7 = a - x2 - x3
                support = sum(v > 0 for v in (x2, x3, x7))
                table[a][support][qcap(x2 * x2 + x3 * x3 + x7 * x7)] += 1
    return table


def build_bc_shard(b0: int, b1: int):
    # BC[b][c][support][r] -> histogram of Qstored contribution, where
    # r=(x0+x8+x10) mod 2 is the x4 parity required by GRF-02.
    bc = [None] * (HMAX + 1)
    for b in range(HMAX + 1):
        if b0 <= b <= b1:
            bc[b] = [
                [[defaultdict(int) for _ in range(2)] for _ in range(8)]
                for __ in range(HMAX + 1)
            ]

    btab = [[[defaultdict(int) for _ in range(2)] for __ in range(3)] for ___ in range(HMAX + 1)]
    ctab = [[[defaultdict(int) for _ in range(2)] for __ in range(4)] for ___ in range(HMAX + 1)]
    for mass in range(HMAX + 1):
        for x9 in range(mass + 1):
            x5 = mass - x9
            btab[mass][int(x5 > 0) + int(x9 > 0)][x9 & 1][qcap(x5 * x5 + x9 * x9)] += 1
        for x8 in range(mass + 1):
            for x10 in range(mass - x8 + 1):
                x6 = mass - x8 - x10
                ctab[mass][int(x6 > 0) + int(x8 > 0) + int(x10 > 0)][(x8 + x10) & 1][
                    qcap(x6 * x6 + x8 * x8 + x10 * x10)
                ] += 1

    # x0 < x1.
    for x0 in range(HMAX + 1):
        for x1 in range(x0 + 1, HMAX + 1):
            extra = int(x0 > 0) + 1
            q01 = x0 * x0 + x1 * x1
            for b in range(max(b0, x1), min(b1, HMAX) + 1):
                g2 = b - x1
                for c in range(x0, HMAX + 1):
                    g3 = c - x0
                    dst = bc[b][c]
                    for sb in range(3):
                        for px9 in (0, 1):
                            left = btab[g2][sb][px9]
                            if not left:
                                continue
                            px8x10 = px9 ^ (x1 & 1)
                            r = (x0 & 1) ^ px8x10
                            for sc in range(4):
                                right = ctab[g3][sc][px8x10]
                                if not right:
                                    continue
                                out = dst[sb + sc + extra][r]
                                for ql, vl in left.items():
                                    for qr, vr in right.items():
                                        out[qcap(q01 + ql + qr)] += vl * vr

    # x0=x1=t, lex branch x5<x8.
    ptab = [[[defaultdict(int) for _ in range(2)] for __ in range(3)] for ___ in range(HMAX + 1)]
    for mass in range(HMAX + 1):
        for x10 in range(mass + 1):
            x6 = mass - x10
            ptab[mass][int(x6 > 0) + int(x10 > 0)][x10 & 1][qcap(x6 * x6 + x10 * x10)] += 1
    for t in range(HMAX + 1):
        et = 2 * int(t > 0)
        for x5 in range(HMAX - t + 1):
            for x9 in range(HMAX - t - x5 + 1):
                b = t + x5 + x9
                if not (b0 <= b <= b1):
                    continue
                for x8 in range(x5 + 1, HMAX - t + 1):
                    qbase = 2 * t * t + x5 * x5 + x8 * x8 + x9 * x9
                    sbase = et + int(x5 > 0) + 1 + int(x9 > 0)
                    need_x10 = (t + x8 + x9) & 1
                    r = (t + x8 + need_x10) & 1
                    for mass in range(HMAX - t - x8 + 1):
                        c = t + x8 + mass
                        dst = bc[b][c]
                        for sp in range(3):
                            pd = ptab[mass][sp][need_x10]
                            if not pd:
                                continue
                            out = dst[sbase + sp][r]
                            for qp, vp in pd.items():
                                out[qcap(qbase + qp)] += vp

    # x0=x1=t, x5=x8=u and x6<=x9.
    for t in range(HMAX + 1):
        et = 2 * int(t > 0)
        for u in range(HMAX - t + 1):
            eu = 2 * int(u > 0)
            for x9 in range(HMAX - t - u + 1):
                b = t + u + x9
                if not (b0 <= b <= b1):
                    continue
                for x6 in range(min(x9, HMAX - t - u) + 1):
                    max10 = HMAX - t - u - x6
                    sbase = et + eu + int(x6 > 0) + int(x9 > 0)
                    qbase = 2 * t * t + 2 * u * u + x6 * x6 + x9 * x9
                    need_x10 = (t + u + x9) & 1
                    for x10 in range(max10 + 1):
                        if (x10 & 1) != need_x10:
                            continue
                        c = t + u + x6 + x10
                        r = (t + u + x10) & 1
                        bc[b][c][sbase + int(x10 > 0)][r][qcap(qbase + x10 * x10)] += 1
    return bc


def hist(dct):
    if not dct:
        return (), (), 0
    keys = sorted(dct)
    pref = []
    total = 0
    for key in keys:
        total += dct[key]
        pref.append(total)
    return tuple(keys), tuple(pref), total


def pairs_gt(ha, hb, cutoff: int) -> int:
    ka, pa, _ = ha
    kb, pb, tb = hb
    if not ka or not kb:
        return 0
    total = 0
    prev = 0
    for i, qa in enumerate(ka):
        ca = pa[i] - prev
        prev = pa[i]
        j = bisect.bisect_right(kb, cutoff - qa)
        le = pb[j - 1] if j else 0
        total += ca * (tb - le)
    return total


def census(b0: int, b1: int):
    atab = build_a()
    bc = build_bc_shard(b0, b1)
    ah = [[hist(atab[a][s]) for s in range(4)] for a in range(HMAX + 1)]
    keys = (
        "population",
        "old_group_cauchy_rejected",
        "hpadj08_exact_square_rejected",
        "hpadj08_exact_square_survivors",
        "grf02_plus_hpadj08_survivors",
        "grf02_additional_rejected_among_hpadj08_survivors",
    )
    totals = {key: 0 for key in keys}
    records = []

    for g, dmax in ((0, 176), (1, 192)):
        for d in range(8, dmax + 1, 2):
            h = d // 2
            legacy = 8 if g == 0 else 4
            k_req = ceil_div(d - 16 * g + 16, 4)
            cutoff = (d * d + 16 * d + (32 if g == 0 else 0)) // 8
            row = {key: 0 for key in keys}
            for b in range(max(b0, 0), min(b1, h) + 1):
                for c in range(h + 1):
                    c3 = component3(d, b, c)
                    if c3 < 0:
                        continue
                    for a in range(h + 1):
                        ca = component_a(d, a)
                        if ca < 0:
                            continue
                        mass = a + b + c
                        srem = min(16, d) + ca + c3
                        old_reject = 8 * a * a + 8 * b * b + 6 * c * c > 3 * d * d + 48 * d + (96 if g == 0 else 0)
                        for sbc in range(8):
                            for required_x4_parity in (0, 1):
                                bd = bc[b][c][sbc][required_x4_parity]
                                if not bd:
                                    continue
                                hb = hist(bd)
                                btot = hb[2]
                                for sa in range(4):
                                    ha = ah[a][sa]
                                    atot = ha[2]
                                    if not atot:
                                        continue
                                    support = sbc + sa
                                    qneed = k_req - support
                                    if qneed > 0 and srem < qneed:
                                        continue
                                    lower = max(legacy, k_req, d - 4 * g + 4, mass, mass + max(0, qneed))
                                    upper = min((19 * d) // 5, 3 * d, 3 * d - (b - c))
                                    if lower > upper:
                                        continue
                                    excluded = set()
                                    en = 3 * d - (b - c)
                                    if b <= h - 5 and support + srem == k_req and en - mass >= srem:
                                        excluded.add(en)
                                    if g == 1 and d == 8:
                                        excluded.add(8)
                                    ne, normal_total, normal_even, normal_odd = even_interval_normal_sum_split(d, lower, upper, excluded)
                                    if ne <= 0:
                                        continue
                                    local_population = atot * btot * normal_total
                                    exact_rejected_pairs = pairs_gt(ha, hb, cutoff)
                                    if old_reject:
                                        req(exact_rejected_pairs == atot * btot, f"Cauchy subset regression {(g,d,a,b,c,sa,sbc,required_x4_parity)}")
                                        row["old_group_cauchy_rejected"] += local_population
                                    row["population"] += local_population
                                    row["hpadj08_exact_square_rejected"] += exact_rejected_pairs * normal_total
                                    survivor_pairs = atot * btot - exact_rejected_pairs
                                    row["hpadj08_exact_square_survivors"] += survivor_pairs * normal_total
                                    normal_required = normal_even if required_x4_parity == 0 else normal_odd
                                    kept = survivor_pairs * normal_required
                                    row["grf02_plus_hpadj08_survivors"] += kept
                                    row["grf02_additional_rejected_among_hpadj08_survivors"] += survivor_pairs * (normal_total - normal_required)
            req(row["population"] == row["hpadj08_exact_square_rejected"] + row["hpadj08_exact_square_survivors"], f"HPADJ08 partition mismatch g={g} d={d}")
            req(row["hpadj08_exact_square_survivors"] == row["grf02_plus_hpadj08_survivors"] + row["grf02_additional_rejected_among_hpadj08_survivors"], f"GRF02 partition mismatch g={g} d={d}")
            records.append({"g": g, "d": d, **row})
            for key in keys:
                totals[key] += row[key]

    stream = hashlib.sha256()
    for row in records:
        stream.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    return records, totals, stream.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--b-start", type=int, required=True)
    ap.add_argument("--b-end", type=int, required=True)
    ap.add_argument("--output", required=True)
    ns = ap.parse_args()
    b0, b1 = ns.b_start, ns.b_end
    req((b0, b1) in PLANNED, "b interval is not a planned exact shard")
    req(git_blob(CONTRACT) == CONTRACT_BLOB, "scaleout contract blob drift")
    contract = json.loads(CONTRACT.read_text())
    req(contract.get("canonical_sha256_without_this_field") == CONTRACT_CANON and canon(contract) == CONTRACT_CANON, "scaleout contract canonical drift")
    req(contract["execution"]["heavy_authorized"] is True, "heavy execution is not authorized by retained contract")
    req(contract["execution"]["execution_armed"] is True, "FULL178 execution is not armed")
    req(contract["execution"]["runkey_present"] is True, "FULL178 runkey is absent")
    for name, (rel, sha) in LOCKS.items():
        req(git_blob(ROOT / rel) == sha, f"source drift: {name}")

    records, totals, stream = census(b0, b1)
    out = {
        "schema": "STAGE32_32_01_178_TD01_FULL178_B_SHARD_RESULT_V1",
        "stage": 32,
        "route_id": "TD01_GRF02_HPADJ08_TOPDOWN_COMPOSITION",
        "b_interval": [b0, b1],
        "row_count": len(records),
        "q_cap": QCAP,
        "totals": totals,
        "row_stream_sha256": stream,
        "records": records,
        "credit_firewall": {
            "partial_shard_only": True,
            "main_pruning_credit": False,
            "main_authority_changed": False,
            "full178_complete": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canon(out)
    Path(ns.output).write_text(json.dumps(out, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"b_interval": [b0, b1], "row_count": len(records), "totals": totals, "row_stream_sha256": stream, "canonical_sha256_without_this_field": out["canonical_sha256_without_this_field"]}, sort_keys=True))


if __name__ == "__main__":
    main()
