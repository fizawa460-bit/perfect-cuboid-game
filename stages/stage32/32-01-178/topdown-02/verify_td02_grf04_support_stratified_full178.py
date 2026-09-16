#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import sys
import types
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

LOCKS = {
    "predecessor_verifier": (
        "stages/stage32/32-01-178/topdown-02/verify_td02_grf04_full178_aggregate.py",
        "bf742845626fb3a0c9bc0f2e563885b98d646f7c",
    ),
    "predecessor_checkpoint": (
        "stages/stage32/32-01-178/topdown-02/TD02-GRF04-FULL178-AGGREGATE-CHECKPOINT.json",
        "4e2ccf5f9f8d25f117e4e9792d3b54ec31a0799b",
    ),
    "bounded_exact_verifier": (
        "stages/stage32/32-01-178/topdown-02/verify_td02_grf04_bc_envelope_bounded.py",
        "3ce709a2afe9d1acb573cb7c4c1b2e7bff4b53ae",
    ),
}

HMAX = 96
INF = 10**30
NEG = -1
EXPECTED_ROWS = 178
EXPECTED_HPADJ08_PANEL = 47_589_703_313_957_134_958_895
PREDECESSOR_RELAXED_PANEL = 71_384_787_021_929_133_241_956
PREDECESSOR_SURVIVOR_UPPER = 1_666_897_772_020_475_143_768
REFERENCE_HPADJ08_UPPER = 6_703_403_803_993_210_101_494


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked_raw(rel: str, expected: str) -> bytes:
    path = ROOT / rel
    req(path.is_file(), f"missing source {rel}")
    raw = path.read_bytes()
    req(git_blob(raw) == expected, f"source drift {rel}")
    return raw


def load_module(name: str, path: Path, raw: bytes):
    old = sys.modules.get(name)
    try:
        mod = types.ModuleType(name)
        mod.__file__ = str(path)
        sys.modules[name] = mod
        exec(compile(raw, str(path), "exec"), mod.__dict__)
        return mod
    finally:
        if old is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = old


def new_stat() -> list[int]:
    return [0, INF, NEG]


def add_stat(dst: list[int], count: int, qmin: int, qmax: int) -> None:
    if count == 0:
        return
    req(qmin <= qmax, "invalid q range")
    dst[0] += count
    dst[1] = min(dst[1], qmin)
    dst[2] = max(dst[2], qmax)


def positive_qmin(total: int, support: int) -> int:
    req(1 <= support <= total, f"positive_qmin domain {(total, support)}")
    q, r = divmod(total, support)
    return r * (q + 1) ** 2 + (support - r) * q * q


def positive_qmax(total: int, support: int) -> int:
    req(1 <= support <= total, f"positive_qmax domain {(total, support)}")
    return (total - support + 1) ** 2 + support - 1


def build_a_support_stats(H: int):
    out = [[new_stat() for _ in range(4)] for __ in range(H + 1)]
    out[0][0] = [1, 0, 0]
    for a in range(1, H + 1):
        for s in range(1, min(3, a) + 1):
            count = math.comb(3, s) * math.comb(a - 1, s - 1)
            out[a][s] = [count, positive_qmin(a, s), positive_qmax(a, s)]
    return out


def build_bc_support_stats(H: int):
    # Each stat is [exact_count, exact_q_min, exact_q_max].
    B = [[[new_stat() for _ in range(2)] for __ in range(3)] for ___ in range(H + 1)]
    C = [[[new_stat() for _ in range(2)] for __ in range(4)] for ___ in range(H + 1)]
    D = [[[new_stat() for _ in range(2)] for __ in range(3)] for ___ in range(H + 1)]

    for m in range(H + 1):
        for x9 in range(m + 1):
            x5 = m - x9
            s = int(x5 > 0) + int(x9 > 0)
            p = x9 & 1
            q = x5*x5 + x9*x9
            add_stat(B[m][s][p], 1, q, q)
        for x8 in range(m + 1):
            for x10 in range(m - x8 + 1):
                x6 = m - x8 - x10
                s = int(x6 > 0) + int(x8 > 0) + int(x10 > 0)
                p = (x8 + x10) & 1
                q = x6*x6 + x8*x8 + x10*x10
                add_stat(C[m][s][p], 1, q, q)
        for x10 in range(m + 1):
            x6 = m - x10
            s = int(x6 > 0) + int(x10 > 0)
            p = x10 & 1
            q = x6*x6 + x10*x10
            add_stat(D[m][s][p], 1, q, q)

    # Unequal branch x0<x1. R stores exact residual support/q ranges.
    R = [[[[new_stat() for _ in range(6)] for __ in range(H + 1)] for ___ in range(H + 1)] for ____ in range(2)]
    for gb in range(H + 1):
        for gc in range(H + 1):
            for sb in range(3):
                for pb in (0, 1):
                    lb = B[gb][sb][pb]
                    if not lb[0]:
                        continue
                    for sc in range(4):
                        for pc in (0, 1):
                            rc = C[gc][sc][pc]
                            if not rc[0]:
                                continue
                            add_stat(R[pb ^ pc][gb][gc][sb + sc], lb[0] * rc[0], lb[1] + rc[1], lb[2] + rc[2])

    BC = [[[new_stat() for _ in range(8)] for __ in range(H + 1)] for ___ in range(H + 1)]
    for b in range(H + 1):
        for c in range(H + 1):
            for x1 in range(1, b + 1):
                gb = b - x1
                for x0 in range(min(c, x1 - 1) + 1):
                    fixed_s = 1 + int(x0 > 0)
                    fixed_q = x0*x0 + x1*x1
                    for sr in range(6):
                        st = R[x1 & 1][gb][c - x0][sr]
                        if st[0]:
                            add_stat(BC[b][c][fixed_s + sr], st[0], fixed_q + st[1], fixed_q + st[2])

    # Equal branch x0=x1=t. Dcap retains x6<=cap exactly.
    Dcap = [[[[new_stat() for _ in range(2)] for __ in range(3)] for ___ in range(H + 1)] for ____ in range(H + 1)]
    for r in range(H + 1):
        acc = [[new_stat() for _ in range(2)] for __ in range(3)]
        for cap in range(H + 1):
            if cap <= r:
                x6 = cap
                x10 = r - cap
                s = int(x6 > 0) + int(x10 > 0)
                p = x10 & 1
                q = x6*x6 + x10*x10
                add_stat(acc[s][p], 1, q, q)
            for s in range(3):
                for p in (0, 1):
                    Dcap[r][cap][s][p] = list(acc[s][p])

    # E covers x5,x6,x8,x9,x10 subject to (x5,x6)<=lex(x8,x9).
    E = [[[[new_stat() for _ in range(6)] for __ in range(H + 1)] for ___ in range(H + 1)] for ____ in range(2)]
    for x5 in range(H + 1):
        for x8 in range(x5 + 1, H + 1):
            fixed_s_58 = int(x5 > 0) + int(x8 > 0)
            fixed_q_58 = x5*x5 + x8*x8
            for x9 in range(H - x5 + 1):
                bs = x5 + x9
                fixed_s = fixed_s_58 + int(x9 > 0)
                fixed_q = fixed_q_58 + x9*x9
                for r in range(H - x8 + 1):
                    cs = x8 + r
                    for sd in range(3):
                        for p10 in (0, 1):
                            st = D[r][sd][p10]
                            if not st[0]:
                                continue
                            p = (x8 + x9 + p10) & 1
                            add_stat(E[p][bs][cs][fixed_s + sd], st[0], fixed_q + st[1], fixed_q + st[2])

    for u in range(H + 1):
        fixed_u_s = 2 * int(u > 0)
        fixed_u_q = 2*u*u
        for x9 in range(H - u + 1):
            bs = u + x9
            fixed_s = fixed_u_s + int(x9 > 0)
            fixed_q = fixed_u_q + x9*x9
            for r in range(H - u + 1):
                cs = u + r
                for sd in range(3):
                    for p10 in (0, 1):
                        st = Dcap[r][x9][sd][p10]
                        if not st[0]:
                            continue
                        p = (u + x9 + p10) & 1
                        add_stat(E[p][bs][cs][fixed_s + sd], st[0], fixed_q + st[1], fixed_q + st[2])

    for b in range(H + 1):
        for c in range(H + 1):
            for t in range(min(b, c) + 1):
                fixed_s = 2 * int(t > 0)
                fixed_q = 2*t*t
                for sr in range(6):
                    st = E[t & 1][b - t][c - t][sr]
                    if st[0]:
                        add_stat(BC[b][c][fixed_s + sr], st[0], fixed_q + st[1], fixed_q + st[2])
    return BC


def crosscheck_h16_exact(pred, bounded, A, BC) -> None:
    exact_a = bounded.build_a_q()
    exact_bc = bounded.build_bc_q()
    for a in range(17):
        for s in range(4):
            hist = exact_a[a][s]
            expected = [sum(hist.values()), min(hist) if hist else INF, max(hist) if hist else NEG]
            req(A[a][s] == expected, f"H16 A support/q mismatch {(a,s)}")
    for b in range(17):
        for c in range(17):
            for s in range(8):
                hist = exact_bc[b][c][s]
                expected = [sum(hist.values()), min(hist) if hist else INF, max(hist) if hist else NEG]
                req(BC[b][c][s] == expected, f"H16 BC support/q mismatch {(b,c,s)}")

    pcount, pminq = pred.build_bc_count_minq(HMAX)
    for b in range(HMAX + 1):
        for c in range(HMAX + 1):
            count = sum(BC[b][c][s][0] for s in range(8))
            mins = [BC[b][c][s][1] for s in range(8) if BC[b][c][s][0]]
            qmin = min(mins) if mins else INF
            req(count == pcount[b][c], f"BC collapsed count mismatch {(b,c)}")
            req(qmin == pminq[b][c], f"BC collapsed qmin mismatch {(b,c)}")


def allowed_even_stats(pred, lower: int, upper: int, excluded: set[int]) -> tuple[int, int, int, int]:
    ne, se, lo, hi = pred.even_interval_count_sum(lower, upper)
    if ne == 0:
        return 0, 0, lo, hi
    for e in excluded:
        if lo <= e <= hi and (e & 1) == 0:
            ne -= 1
            se -= e
    return ne, se, lo, hi


def row_census(pred, *, g: int, d: int, A, BC) -> tuple[int, int, int]:
    h = d // 2
    legacy = 8 if g == 0 else 4
    K = pred.ceil_div(d - 16*g + 16, 4)
    panel = survivor = support_cells = 0
    for b in range(h + 1):
        for c in range(h + 1):
            c3 = pred.component3(d, b, c)
            if c3 < 0:
                continue
            for sbc in range(8):
                bc = BC[b][c][sbc]
                if not bc[0]:
                    continue
                for a in range(h + 1):
                    ca = pred.component_a(d, a)
                    if ca < 0:
                        continue
                    M = a + b + c
                    srem = min(16, d) + ca + c3
                    for sa in range(4):
                        aa = A[a][sa]
                        if not aa[0]:
                            continue
                        support = sa + sbc
                        qneed = K - support
                        if qneed > 0 and srem < qneed:
                            continue
                        lower = max(legacy, K, d - 4*g + 4, M, M + max(0, qneed))
                        upper = min((19*d)//5, 3*d, 3*d - (b-c))
                        if lower > upper:
                            continue
                        excluded: set[int] = set()
                        en = 3*d - (b-c)
                        if b <= h - 5 and support + srem == K and en - M >= srem:
                            excluded.add(en)
                        if g == 1 and d == 8:
                            excluded.add(8)
                        ne, se, _elo, ehi = allowed_even_stats(pred, lower, upper, excluded)
                        if ne == 0:
                            continue
                        configs = aa[0] * bc[0]
                        panel += configs * (ne * (19*d + 1) - 5*se)
                        qmin = aa[1] + bc[1]
                        sx4, raw_hi = pred.td02_x4_survivors(d=d, g=g, b=b, c=c, qmin=qmin)
                        if raw_hi >= 0:
                            req(ehi <= 3*d, f"e upper regression {(g,d,a,sa,b,c,sbc,ehi)}")
                            min_n = 19*d - 5*ehi
                            req(min_n >= 4*d, f"normal lower regression {(g,d,a,sa,b,c,sbc,min_n)}")
                            req(raw_hi <= min_n, f"x4 clipping regression {(g,d,a,sa,b,c,sbc,raw_hi,min_n)}")
                        survivor += configs * ne * sx4
                        support_cells += 1
    return panel, survivor, support_cells


def run_domain(pred, rows: list[tuple[int, int]], A, BC):
    out = []
    panel = survivor = support_cells = 0
    for g, d in rows:
        rp, rs, rcells = row_census(pred, g=g, d=d, A=A, BC=BC)
        row = {"row_id": f"g{g}-d{d:03d}", "g": g, "d": d, "exact_hpadj08_panel_terminals": rp, "td02_support_stratified_survivor_upper_bound": rs, "support_cells": rcells}
        out.append(row)
        panel += rp
        survivor += rs
        support_cells += rcells
    stream = hashlib.sha256()
    for row in out:
        stream.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    return out, panel, survivor, support_cells, stream.hexdigest()


def support_table_sha(A, BC) -> str:
    h = hashlib.sha256()
    for a in range(HMAX + 1):
        for s in range(4):
            h.update(json.dumps(["A", a, s, A[a][s]], separators=(",", ":")).encode() + b"\n")
    for b in range(HMAX + 1):
        for c in range(HMAX + 1):
            for s in range(8):
                h.update(json.dumps(["BC", b, c, s, BC[b][c][s]], separators=(",", ":")).encode() + b"\n")
    return h.hexdigest()


def main() -> None:
    raws = {name: checked_raw(rel, sha) for name, (rel, sha) in LOCKS.items()}
    pred = load_module("td02_support_predecessor", ROOT / LOCKS["predecessor_verifier"][0], raws["predecessor_verifier"])
    bounded = load_module("td02_support_bounded_exact", ROOT / LOCKS["bounded_exact_verifier"][0], raws["bounded_exact_verifier"])
    pred_sources = pred.verified_sources()
    checkpoint = json.loads(raws["predecessor_checkpoint"])
    req(checkpoint["result"]["relaxed_panel_terminals"] == PREDECESSOR_RELAXED_PANEL, "predecessor panel")
    req(checkpoint["result"]["td02_independent_survivor_upper_bound"] == PREDECESSOR_SURVIVOR_UPPER, "predecessor survivor")
    req(checkpoint["next_route"]["id"] == "TD02-FULL178-SUPPORT-STRATIFIED-AGGREGATE", "route handoff")

    A = build_a_support_stats(HMAX)
    BC = build_bc_support_stats(HMAX)
    crosscheck_h16_exact(pred, bounded, A, BC)

    fam = pred.load_module("td02_support_compressed_family", ROOT / pred.LOCKS["compressed_family"][0], pred_sources["compressed_family"])
    table = fam.build_exceptional_count_table(HMAX)
    mass = [0] * (HMAX + 1)
    for a in range(HMAX + 1):
        ac = sum(A[a][s][0] for s in range(4))
        req(ac == math.comb(a + 2, 2), f"A count collapse {a}")
        for b in range(HMAX - a + 1):
            for c in range(HMAX - a - b + 1):
                bcc = sum(BC[b][c][s][0] for s in range(8))
                mass[a+b+c] += ac * bcc
    cumulative = 0
    for e in range(HMAX + 1):
        cumulative += mass[e]
        req(cumulative == table.count(e), f"compressed-family count mismatch e={e}")

    expected_rows = [(0, d) for d in range(8, 177, 2)] + [(1, d) for d in range(8, 193, 2)]
    rows, panel, survivor, support_cells, row_sha = run_domain(pred, expected_rows, A, BC)
    req(len(rows) == EXPECTED_ROWS, "row count")
    req(panel == EXPECTED_HPADJ08_PANEL, f"exact HPADJ08 panel drift {panel}")
    req(panel < PREDECESSOR_RELAXED_PANEL, "support stratification did not recover tighter panel")
    req(survivor < PREDECESSOR_SURVIVOR_UPPER, "support stratification did not tighten TD02 upper bound")
    req(survivor < REFERENCE_HPADJ08_UPPER, "support-stratified TD02 does not tighten HPADJ08 reference")

    stats_sha = support_table_sha(A, BC)
    result = {
        "schema": "STAGE32_32_01_178_TD02_GRF04_SUPPORT_STRATIFIED_FULL178_UPPER_V1",
        "route": "TD02-FULL178-SUPPORT-STRATIFIED-AGGREGATE",
        "domain": {"rows": EXPECTED_ROWS, "g0_d_even": [8, 176], "g1_d_even": [8, 192], "hmax": HMAX, "per_terminal_enumeration": False},
        "semantics": {
            "aggregation": "EXACT_(A_SUPPORT,BC_SUPPORT)_COUNTS_WITH_EXACT_QMIN_QMAX_RANGES",
            "support": "EXACT_SUPPORT_CLASS_RESTORES_QNEED_SREM_FEASIBILITY_AND_SINGLETON_E_EXCLUSIONS",
            "q_usage": "GRF04 survivor upper bound uses exact support-class qmin; retained qmax is diagnostic/range evidence only",
            "t": "SOURCE_LOCKED_CANONICAL_PARITY_INTERVAL_ENVELOPE_FROM_PREDECESSOR",
            "composition": "MIN_ONLY__NO_ADDITIVE_STACKING__NO_EXACT_RESIDUAL_SET_CLAIM",
        },
        "exact_hpadj08_panel_terminals": panel,
        "predecessor_relaxed_panel_terminals": PREDECESSOR_RELAXED_PANEL,
        "predecessor_td02_survivor_upper_bound": PREDECESSOR_SURVIVOR_UPPER,
        "td02_support_stratified_survivor_upper_bound": survivor,
        "tightening_vs_predecessor_td02_upper": PREDECESSOR_SURVIVOR_UPPER - survivor,
        "reference_hpadj08_v29_upper_bound": REFERENCE_HPADJ08_UPPER,
        "tightening_vs_hpadj08_reference": REFERENCE_HPADJ08_UPPER - survivor,
        "support_cells_evaluated": support_cells,
        "support_table_sha256": stats_sha,
        "row_stream_sha256": row_sha,
        "crosschecks": {
            "h16_exact_a_support_count_qmin_qmax_all_cells": True,
            "h16_exact_bc_support_count_qmin_qmax_all_cells": True,
            "h96_bc_support_collapse_matches_predecessor_count_qmin_all_cells": True,
            "production_compressed_exceptional_counts_e_0_through_96": True,
            "wolfram_positive_support_balanced_qmin_small_domain": True,
            "wolfram_positive_support_extreme_qmax_small_domain": True,
        },
        "rows": rows,
        "source_blobs": {name: sha for name, (_rel, sha) in LOCKS.items()},
        "predecessor_source_blobs": {name: sha for name, (_rel, sha) in pred.LOCKS.items()},
        "credit": {"main": False, "theorem": False, "effectivity": False, "receiver": False, "endpoint": False, "stage32_closed": False, "perfect_cuboid_existence": False, "perfect_cuboid_nonexistence": False, "merge": False},
        "next_route": {"id": "TD02-SUPPORT-STRATIFIED-T-REFINEMENT", "goal": "only after audit boundary: determine whether canonical t can be safely tightened within support/q strata without terminal expansion"},
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    (HERE / "TD02-GRF04-SUPPORT-STRATIFIED-FULL178-RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "exact_hpadj08_panel_terminals": panel,
        "predecessor_td02_survivor_upper_bound": PREDECESSOR_SURVIVOR_UPPER,
        "td02_support_stratified_survivor_upper_bound": survivor,
        "tightening_vs_predecessor_td02_upper": PREDECESSOR_SURVIVOR_UPPER - survivor,
        "tightening_vs_hpadj08_reference": REFERENCE_HPADJ08_UPPER - survivor,
        "support_cells_evaluated": support_cells,
        "support_table_sha256": stats_sha,
        "row_stream_sha256": row_sha,
        "canonical_sha256_without_this_field": result["canonical_sha256_without_this_field"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
