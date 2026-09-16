#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

LOCKS = {
    "compressed_family": (
        "stages/stage32/residual-32-01-production/compressed_terminal_family.py",
        "90ff82ed312dcc0cb32cf207935945f550e29170",
    ),
    "prefix_checkpoint": (
        "stages/stage32/residual-32-01-production/full178-prefix-indexed-compression-main-checkpoint.json",
        "eb823cc2f99d74456d5701b4673f848f18ba3151",
    ),
    "corrected_adjunction": (
        "stages/stage32/management/hpadj-07/proof-chain/GENERAL-TYPE-ADJUNCTION-CORRECTION.json",
        "c90b41dcfbd5bd081629a6fa62d9447d43cb3d5e",
    ),
    "full178_contract": (
        "stages/stage32/32-01-178/topdown-01/FULL178-SCALEOUT-CONTRACT.json",
        "ca1b195a3ee8e786707e1ef50b404ee8c19f1429",
    ),
}

MAX_D = 32
H = 16
EXPECTED_HPADJ08_REJECTED = 25_770_706_503_487
EXPECTED_HPADJ08_SURVIVORS = 11_531_305_094_786
EXPECTED_PANEL_TOTAL = EXPECTED_HPADJ08_REJECTED + EXPECTED_HPADJ08_SURVIVORS


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def component_a(d: int, a: int) -> int:
    h = d // 2
    return min(13, d - a, d - 2 * a + 4, h + 5)


def component3(d: int, b: int, c: int) -> int:
    return min(9, d - b - c, d - 2 * b, d - 2 * c + 1)


def even_es(lower: int, upper: int, excluded: set[int]) -> list[int]:
    lo = lower if lower % 2 == 0 else lower + 1
    hi = upper if upper % 2 == 0 else upper - 1
    if lo > hi:
        return []
    return [e for e in range(lo, hi + 1, 2) if e not in excluded]


def build_a_q():
    # x2,x3,x7: keyed by exceptional square sum.
    out = [[defaultdict(int) for _ in range(4)] for __ in range(H + 1)]
    for a in range(H + 1):
        for x2 in range(a + 1):
            for x3 in range(a - x2 + 1):
                x7 = a - x2 - x3
                support = sum(v > 0 for v in (x2, x3, x7))
                out[a][support][x2*x2 + x3*x3 + x7*x7] += 1
    return out


def build_bc_qt():
    # Remaining exceptional variables x0,x1,x5,x6,x8,x9,x10.
    # Besides q=sum squares, retain t=x0+x1+x6+x9 because the GRF04
    # correction is (d/2 - t - 2*x4)^2.
    B = [[[defaultdict(int) for _ in range(2)] for __ in range(3)] for ___ in range(H + 1)]
    C = [[[defaultdict(int) for _ in range(2)] for __ in range(4)] for ___ in range(H + 1)]
    for m in range(H + 1):
        for x9 in range(m + 1):
            x5 = m - x9
            B[m][int(x5 > 0) + int(x9 > 0)][x9 & 1][(x5*x5 + x9*x9, x9)] += 1
        for x8 in range(m + 1):
            for x10 in range(m - x8 + 1):
                x6 = m - x8 - x10
                C[m][int(x6 > 0) + int(x8 > 0) + int(x10 > 0)][(x8 + x10) & 1][(x6*x6 + x8*x8 + x10*x10, x6)] += 1

    out = [[[defaultdict(int) for _ in range(8)] for __ in range(H + 1)] for ___ in range(H + 1)]

    # x0 < x1: no lex restriction on (x5,x6),(x8,x9).
    for x0 in range(H + 1):
        extra = int(x0 > 0) + 1
        for x1 in range(x0 + 1, H + 1):
            parity = x1 & 1
            q01 = x0*x0 + x1*x1
            for g2 in range(H - x1 + 1):
                b = x1 + g2
                for g3 in range(H - x0 + 1):
                    c = x0 + g3
                    for sb in range(3):
                        for pb in (0, 1):
                            left = B[g2][sb][pb]
                            if not left:
                                continue
                            for sc in range(4):
                                right = C[g3][sc][pb ^ parity]
                                if not right:
                                    continue
                                dst = out[b][c][sb + sc + extra]
                                for (ql, x9), vl in left.items():
                                    for (qr, x6), vr in right.items():
                                        dst[(q01 + ql + qr, x0 + x1 + x6 + x9)] += vl * vr

    # x0 == x1 and x5 < x8.
    for x0 in range(H + 1):
        cap = H - x0
        for x5 in range(cap + 1):
            for x8 in range(x5 + 1, cap + 1):
                for x9 in range(cap - x5 + 1):
                    b = x0 + x5 + x9
                    for x6 in range(cap - x8 + 1):
                        for x10 in range(cap - x8 - x6 + 1):
                            c = x0 + x8 + x6 + x10
                            if (x0 + x8 + x9 + x10) & 1:
                                continue
                            vals = (x0, x0, x5, x6, x8, x9, x10)
                            support = sum(v > 0 for v in vals)
                            q = sum(v*v for v in vals)
                            t = 2*x0 + x6 + x9
                            out[b][c][support][(q, t)] += 1

    # x0 == x1, x5 == x8, and x6 <= x9.
    for x0 in range(H + 1):
        cap = H - x0
        for x5 in range(cap + 1):
            x8 = x5
            for x6 in range(cap - x8 + 1):
                for x9 in range(x6, cap - x5 + 1):
                    b = x0 + x5 + x9
                    for x10 in range(cap - x8 - x6 + 1):
                        c = x0 + x8 + x6 + x10
                        if (x0 + x8 + x9 + x10) & 1:
                            continue
                        vals = (x0, x0, x5, x6, x8, x9, x10)
                        support = sum(v > 0 for v in vals)
                        q = sum(v*v for v in vals)
                        t = 2*x0 + x6 + x9
                        out[b][c][support][(q, t)] += 1
    return out


def grf_survivor_x4_count(*, d: int, g: int, q: int, t: int, n: int) -> int:
    # Exact necessary condition, equivalent to rho <= B_g(d):
    #   24*q + 4*(d/2 - t - 2*x4)^2 <= 3*d^2+48*d+96-96*g.
    rhs = 3*d*d + 48*d + 96 - 96*g
    rem = rhs - 24*q
    if rem < 0:
        return 0
    r = math.isqrt(rem // 4)
    D = d // 2 - t
    lo = max(0, ceil_div(D - r, 2))
    hi = min(n, (D + r) // 2)
    return max(0, hi - lo + 1)


def census() -> dict:
    A = build_a_q()
    BC = build_bc_qt()
    rows = []
    panel_total = 0
    hp_rejected_total = 0
    grf_rejected_total = 0

    for g in (0, 1):
        for d in range(8, MAX_D + 1, 2):
            h = d // 2
            legacy = 8 if g == 0 else 4
            K = ceil_div(d - 16*g + 16, 4)
            hp_threshold8 = d*d + 16*d + (32 if g == 0 else 0)
            row_total = row_hp = row_grf = 0

            for b in range(h + 1):
                for c in range(h + 1):
                    if not any(BC[b][c]):
                        continue
                    c3 = component3(d, b, c)
                    if c3 < 0:
                        continue
                    for a in range(h + 1):
                        if not any(A[a]):
                            continue
                        M = a + b + c
                        ca = component_a(d, a)
                        if ca < 0:
                            continue
                        srem = min(16, d) + ca + c3
                        for sbc in range(8):
                            if not BC[b][c][sbc]:
                                continue
                            for sa in range(4):
                                if not A[a][sa]:
                                    continue
                                support = sbc + sa
                                qneed = K - support
                                if qneed > 0 and srem < qneed:
                                    continue
                                lower = max(legacy, K, d - 4*g + 4, M, M + max(0, qneed))
                                upper = min((19*d)//5, 3*d, 3*d - (b-c))
                                if lower > upper:
                                    continue
                                excluded = set()
                                e_n358 = 3*d - (b-c)
                                if b <= h - 5 and support + srem == K and e_n358 - M >= srem:
                                    excluded.add(e_n358)
                                if g == 1 and d == 8:
                                    excluded.add(8)
                                es = even_es(lower, upper, excluded)
                                if not es:
                                    continue

                                for (qb, t), vb in BC[b][c][sbc].items():
                                    for qa, va in A[a][sa].items():
                                        q = qa + qb
                                        mult = va * vb
                                        hp_all = 8*q > hp_threshold8
                                        for e in es:
                                            n = 19*d - 5*e
                                            req(n >= 0, f"negative normal budget {(g,d,e)}")
                                            total_x4 = n + 1
                                            row_total += mult * total_x4
                                            if hp_all:
                                                hp_bad = total_x4
                                            else:
                                                hp_bad = 0
                                            survive = grf_survivor_x4_count(d=d, g=g, q=q, t=t, n=n)
                                            grf_bad = total_x4 - survive
                                            req(grf_bad >= hp_bad, f"HPADJ08 subset regression {(g,d,e,q,t)}")
                                            row_hp += mult * hp_bad
                                            row_grf += mult * grf_bad

            rows.append({
                "g": g,
                "d": d,
                "panel_terminals": row_total,
                "hpadj08_rejected": row_hp,
                "grf04_rejected": row_grf,
                "incremental_over_hpadj08": row_grf - row_hp,
                "grf04_survivors": row_total - row_grf,
            })
            panel_total += row_total
            hp_rejected_total += row_hp
            grf_rejected_total += row_grf

    req(panel_total == EXPECTED_PANEL_TOTAL, f"bounded panel total drift {panel_total}")
    req(hp_rejected_total == EXPECTED_HPADJ08_REJECTED, f"HPADJ08 baseline drift {hp_rejected_total}")
    req(panel_total - hp_rejected_total == EXPECTED_HPADJ08_SURVIVORS, "HPADJ08 survivor baseline drift")
    req(grf_rejected_total >= hp_rejected_total, "GRF04 must dominate HPADJ08")
    req(grf_rejected_total > hp_rejected_total, "GRF04 bounded strict gain missing")

    stream = hashlib.sha256()
    for row in rows:
        stream.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    return {
        "schema": "STAGE32_32_01_178_TD02_GRF04_BOUNDED_V1",
        "domain": {"g": [0,1], "d_even": [8,32], "hmax": H},
        "panel_terminals": panel_total,
        "hpadj08_rejected": hp_rejected_total,
        "hpadj08_survivors": panel_total - hp_rejected_total,
        "grf04_rejected": grf_rejected_total,
        "grf04_survivors": panel_total - grf_rejected_total,
        "incremental_over_hpadj08": grf_rejected_total - hp_rejected_total,
        "retained_fraction_of_hpadj08_survivors_num": panel_total - grf_rejected_total,
        "retained_fraction_of_hpadj08_survivors_den": panel_total - hp_rejected_total,
        "row_stream_sha256": stream.hexdigest(),
        "rows": rows,
        "credit": {"main": False, "theorem": False, "effectivity": False, "endpoint": False, "merge": False},
    }


def main() -> None:
    for name, (rel, expected) in LOCKS.items():
        path = ROOT / rel
        req(path.is_file(), f"missing source {name}")
        req(git_blob(path) == expected, f"source drift {name}")

    prefix = json.loads((ROOT / LOCKS["prefix_checkpoint"][0]).read_text())
    labels = prefix["exact_terminal_family"]["assignment_order_known_labels_1based"]
    req(labels == [95,99,103,102,49,97,94,101,93,98,96], "FULL178 label-order regression")

    correction = json.loads((ROOT / LOCKS["corrected_adjunction"][0]).read_text())
    c = correction["corrected_general_type_adjunction"]
    req(c["g0_exact_exceptional_square_necessary_condition"] == "8*sum(y_i^2)<=d^2+16*d+32", "g0 adjunction regression")
    req(c["g1_exact_exceptional_square_necessary_condition"] == "8*sum(y_i^2)<=d^2+16*d", "g1 adjunction regression")

    result = census()
    out = HERE / "TD02-GRF04-BOUNDED-RESULT.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: result[k] for k in (
        "panel_terminals", "hpadj08_rejected", "hpadj08_survivors",
        "grf04_rejected", "grf04_survivors", "incremental_over_hpadj08",
        "retained_fraction_of_hpadj08_survivors_num",
        "retained_fraction_of_hpadj08_survivors_den", "row_stream_sha256"
    )}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
