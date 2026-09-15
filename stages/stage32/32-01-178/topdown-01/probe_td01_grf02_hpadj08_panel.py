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

# Fresh 178 top-down route, source-locked to Stage32 MAIN PR #1808 exact head.
SOURCE_HEAD = "4f7889e79d9d967d410bfcf781ade8e215703a5d"
HPADJ08_AUDITED_HEAD = "36eab50192cf80ec5ed48aba40f4a56076759fea"
LOCKS = {
    "compressed_family": (
        "stages/stage32/residual-32-01-production/compressed_terminal_family.py",
        "90ff82ed312dcc0cb32cf207935945f550e29170",
    ),
    "grf02_projected_kernel": (
        "stages/stage32/management/global-residual-feasibility/GRF-02-PROJECTED-KERNEL.json",
        "7c1cda07749fbfb90245995d1def2ae96fb5604b",
    ),
    "main_state_v30": (
        "stages/stage32/MAIN-STATE.json",
        "76bf5e3d9d97297ff5fbee2bf4826a78d125e171",
    ),
}

# Low-degree panel used by the retained HPADJ08 preflight: g in {0,1}, d=8..32 even.
HMAX = 16
QCAP = 4992
OVERFLOW = 4993
EXPECTED_OLD_GROUP_CAUCHY_REJECT = 3_257_761_571_005
EXPECTED_HPADJ08_EXACT_SQUARE_REJECT = 25_770_706_503_487


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


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
    """Return (#e, all x4 choices, even-x4 choices, odd-x4 choices).

    Every retained d and e is even, hence N=19*d-5*e is even.  For x4 in 0..N,
    even choices are N/2+1 and odd choices are N/2.  This is the only extra
    statistic needed to compose the GRF-02 parity condition with HPADJ08.
    """
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
    a_table = [[defaultdict(int) for _ in range(4)] for __ in range(HMAX + 1)]
    for a in range(HMAX + 1):
        for x2 in range(a + 1):
            for x3 in range(a - x2 + 1):
                x7 = a - x2 - x3
                support = sum(v > 0 for v in (x2, x3, x7))
                a_table[a][support][qcap(x2 * x2 + x3 * x3 + x7 * x7)] += 1
    return a_table


def build_bc_with_required_x4_parity():
    """Build the HPADJ08 BC table refined by the GRF-02-required x4 parity.

    Stage32 fixed assignment order is
      x0..x10 = [95,99,103,102,49,97,94,101,93,98,96].

    The retained compressed family already enforces
      x1+x8+x9+x10 = 0 (mod 2).
    GRF-02 adds the independent completion condition
      x0+x4+x8+x10 = 0 (mod 2),
    so a fixed exceptional state requires
      x4 = x0+x8+x10 (mod 2).
    """
    bc = [
        [
            [[defaultdict(int) for _ in range(2)] for _ in range(8)]
            for __ in range(HMAX + 1)
        ]
        for ___ in range(HMAX + 1)
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

    # x0 < x1.  Existing parity fixes parity(x8+x10)=parity(x9+x1).
    for x0 in range(HMAX + 1):
        for x1 in range(x0 + 1, HMAX + 1):
            extra_support = int(x0 > 0) + 1
            q01 = x0 * x0 + x1 * x1
            for b in range(x1, HMAX + 1):
                g2 = b - x1
                for c in range(x0, HMAX + 1):
                    g3 = c - x0
                    dst = bc[b][c]
                    for sb in range(3):
                        for parity_x9 in (0, 1):
                            left = btab[g2][sb][parity_x9]
                            if not left:
                                continue
                            parity_x8_x10 = parity_x9 ^ (x1 & 1)
                            required_x4_parity = (x0 & 1) ^ parity_x8_x10
                            for sc in range(4):
                                right = ctab[g3][sc][parity_x8_x10]
                                if not right:
                                    continue
                                out = dst[sb + sc + extra_support][required_x4_parity]
                                for ql, vl in left.items():
                                    for qr, vr in right.items():
                                        out[qcap(q01 + ql + qr)] += vl * vr

    # x0=x1=t and lex branch x5<x8.
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
                for x8 in range(x5 + 1, HMAX - t + 1):
                    qbase = 2 * t * t + x5 * x5 + x8 * x8 + x9 * x9
                    sbase = et + int(x5 > 0) + 1 + int(x9 > 0)
                    need_x10 = (t + x8 + x9) & 1
                    required_x4_parity = (t + x8 + need_x10) & 1
                    for mass in range(HMAX - t - x8 + 1):
                        c = t + x8 + mass
                        dst = bc[b][c]
                        for sp in range(3):
                            pd = ptab[mass][sp][need_x10]
                            if not pd:
                                continue
                            out = dst[sbase + sp][required_x4_parity]
                            for qp, vp in pd.items():
                                out[qcap(qbase + qp)] += vp

    # x0=x1=t and lex diagonal x5=x8=u with x6<=x9.
    for t in range(HMAX + 1):
        et = 2 * int(t > 0)
        for u in range(HMAX - t + 1):
            eu = 2 * int(u > 0)
            for x9 in range(HMAX - t - u + 1):
                b = t + u + x9
                for x6 in range(min(x9, HMAX - t - u) + 1):
                    max10 = HMAX - t - u - x6
                    sbase = et + eu + int(x6 > 0) + int(x9 > 0)
                    qbase = 2 * t * t + 2 * u * u + x6 * x6 + x9 * x9
                    need_x10 = (t + u + x9) & 1
                    for x10 in range(max10 + 1):
                        if (x10 & 1) != need_x10:
                            continue
                        c = t + u + x6 + x10
                        required_x4_parity = (t + u + x10) & 1
                        bc[b][c][sbase + int(x10 > 0)][required_x4_parity][qcap(qbase + x10 * x10)] += 1
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


def census():
    atab = build_a()
    bc = build_bc_with_required_x4_parity()
    ah = [[hist(atab[a][s]) for s in range(4)] for a in range(HMAX + 1)]
    keys = (
        "population",
        "old_group_cauchy_rejected",
        "hpadj08_exact_square_rejected",
        "hpadj08_exact_square_survivors",
        "grf02_plus_hpadj08_survivors",
        "grf02_additional_rejected_among_hpadj08_survivors",
    )
    totals = {k: 0 for k in keys}
    rows = []

    for g in (0, 1):
        for d in range(8, 33, 2):
            h = d // 2
            legacy = 8 if g == 0 else 4
            k_req = ceil_div(d - 16 * g + 16, 4)
            cutoff = (d * d + 16 * d + (32 if g == 0 else 0)) // 8
            row = {k: 0 for k in keys}
            for b in range(h + 1):
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
                                        req(exact_rejected_pairs == atot * btot, f"Cauchy subset regression {(g,d,a,b,c,sa,sbc)}")
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
            rows.append({"g": g, "d": d, **row})
            for key in keys:
                totals[key] += row[key]

    req(totals["old_group_cauchy_rejected"] == EXPECTED_OLD_GROUP_CAUCHY_REJECT, "retained HPADJ08 bounded Cauchy baseline mismatch")
    req(totals["hpadj08_exact_square_rejected"] == EXPECTED_HPADJ08_EXACT_SQUARE_REJECT, "retained HPADJ08 bounded exact-square baseline mismatch")
    return rows, totals


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output")
    ns = ap.parse_args()
    for name, (rel, sha) in LOCKS.items():
        req(git_blob(ROOT / rel) == sha, f"source drift: {name}")

    rows, totals = census()
    out = {
        "schema": "STAGE32_32_01_178_TD01_GRF02_HPADJ08_BOUNDED_RESULT_V1",
        "stage": 32,
        "route_id": "TD01_GRF02_HPADJ08_TOPDOWN_COMPOSITION",
        "source_main_pr": 1808,
        "source_main_exact_head": SOURCE_HEAD,
        "hpadj08_audited_exact_head": HPADJ08_AUDITED_HEAD,
        "scope": {"g": [0, 1], "d_even": [8, 32], "row_count": 26, "hmax": HMAX},
        "mathematical_composition": {
            "retained_terminal_parity": "x1+x8+x9+x10 == 0 (mod 2)",
            "grf02_completion_parity": "x0+x4+x8+x10 == 0 (mod 2)",
            "hpadj08_condition": "8*Qstored <= d^2+16*d+(32 if g=0 else 0)",
            "direction": "actual target carrier -> HPADJ08 exact-square condition AND GRF02 completion parity",
        },
        "totals": totals,
        "strict_gain": totals["grf02_additional_rejected_among_hpadj08_survivors"] > 0,
        "rows": rows,
        "credit_firewall": {
            "bounded_diagnostic_only": True,
            "main_pruning_credit": False,
            "main_authority_changed": False,
            "full178_complete": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canonical(out)
    text = json.dumps(out, sort_keys=True, indent=2) + "\n"
    if ns.output:
        Path(ns.output).write_text(text)
    print(json.dumps({"totals": totals, "canonical_sha256_without_this_field": out["canonical_sha256_without_this_field"]}, sort_keys=True))


if __name__ == "__main__":
    main()
