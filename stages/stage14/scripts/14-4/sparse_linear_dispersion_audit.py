#!/usr/bin/env python3
"""Stage14-4ax: deterministic audit of sparse linear projective dispersion."""

import json
from itertools import combinations
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
AW = ROOT / "stages/stage14/14-4aw/result.md"
S5I = ROOT / "stages/stage14/14-s5i/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/sparse_linear_dispersion_summary.json"

LINEAR = ("m", "n", "m-n", "m+n")
PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)


def value(col: str, m: int, n: int) -> int:
    if col == "m":
        return m
    if col == "n":
        return n
    if col == "m-n":
        return m - n
    if col == "m+n":
        return m + n
    raise ValueError(col)


def odd_squarefree_rad(x: int) -> int:
    x = abs(x)
    while x and x % 2 == 0:
        x //= 2
    out = 1
    p = 3
    while p * p <= x:
        if x % p == 0:
            out *= p
            while x % p == 0:
                x //= p
        p += 2
    if x > 1:
        out *= x
    return out


def primitive_points(xmax: int, ymax: int):
    pts = []
    for m in range(2, xmax + 1):
        for n in range(1, min(ymax, m - 1) + 1):
            if gcd(m, n) != 1:
                continue
            if (m - n) % 2 == 0:
                continue
            pts.append((m, n))
    return pts


def determinant(p, q):
    m, n = p
    mp, np = q
    return m * np - mp * n


def antideterminant(p, q):
    m, n = p
    mp, np = q
    return m * np + mp * n


def sqrt_minus_one(p: int):
    for r in range(1, p):
        if (r * r + 1) % p == 0:
            return r
    return None


def main() -> None:
    aw = AW.read_text()
    s5i = S5I.read_text()
    assert "DISCREPANCY_SECOND_MOMENT_PROVED=false" in aw
    assert "SPARSE_LARGE_MODULUS_BLOCKS_CLOSED=false" in aw
    assert "PURE_EUCLID_DIVISIBILITY_BULK_SEPARABLE=true" in s5i
    assert "MOBIUS_TRUNCATION_DISCREPANCY_DECOMPOSITION_PROVED=true" in s5i

    # Each linear column is one primitive projective root mod p.
    for p in PRIMES:
        for col in LINEAR:
            roots = 0
            for m in range(p):
                for n in range(p):
                    if m == 0 and n == 0:
                        continue
                    if value(col, m, n) % p == 0:
                        roots += 1
            assert roots == p - 1, (p, col, roots)

    # For every distinct primitive point pair and every linear edge, the
    # common squarefree state modulus divides the determinant.
    X, Y = 30, 15
    pts = primitive_points(X, Y)
    edge_checks = 0
    for p, q in combinations(pts, 2):
        d = determinant(p, q)
        assert d != 0
        assert abs(d) < 2 * X * Y
        for ci, cj in combinations(LINEAR, 2):
            ui = odd_squarefree_rad(gcd(value(ci, *p), value(ci, *q)))
            vj = odd_squarefree_rad(gcd(value(cj, *p), value(cj, *q)))
            assert gcd(ui, vj) == 1
            mod = ui * vj
            if mod > 1:
                assert d % mod == 0, (p, q, ci, cj, mod, d)
                assert mod < 2 * X * Y
            edge_checks += 1

    # Split norm roots: same sign -> D; opposite sign -> S.
    norm_checks = 0
    for p in PRIMES:
        r = sqrt_minus_one(p)
        if p % 4 == 1:
            assert r is not None
            for n in range(1, p):
                for np in range(1, p):
                    same_p = ((r * n) % p, n)
                    same_q = ((r * np) % p, np)
                    opp_q = ((-r * np) % p, np)
                    assert determinant(same_p, same_q) % p == 0
                    assert antideterminant(same_p, opp_q) % p == 0
                    norm_checks += 2
        else:
            assert r is None

    # The unit Jacobi edge (1/v) is identically +1 for odd v.
    for v in range(3, 100, 2):
        assert pow(1, (v - 1) // 2, v) == 1

    report = {
        "stage": "14-4ax",
        "classification": "SPARSE_LINEAR_L2_CLOSED_AND_DETERMINANT_NORM_OBSTRUCTIONS_ISOLATED",
        "linear_projective_core": {
            "columns": ["m", "n", "m-n", "m+n"],
            "projective_roots": {
                "m": "[0:1]",
                "n": "[1:0]",
                "m-n": "[1:1]",
                "m+n": "[-1:1]",
            },
            "reciprocal_edge_count": 6,
            "collision_determinant": "D(P,P')=m*n'-m'*n",
            "same_cell_implication": "q=uv divides D(P,P')",
            "primitive_positive_D_zero_implies_same_point": True,
        },
        "sparse_linear_dispersion": {
            "rectangle": "0<m<=X, 0<n<=Y",
            "determinant_bound": "|D(P,P')|<2XY",
            "threshold": "Q=UV>2XY",
            "cell_occupancy": "W(u,v) in {0,1}",
            "raw_second_moment": "sum W(u,v)^2 <<_epsilon N*B^epsilon",
            "rank_one_bulk_second_moment": "sum M(u,v)^2 <<_epsilon N^2*B^epsilon/Q << N*B^epsilon",
            "discrepancy_second_moment": "sum |Delta(u,v)|^2 <<_epsilon N*B^epsilon",
            "natural_diagonal_scale": "N*B^epsilon",
            "fixed_power_retainer_saving_from_this_alone": False,
        },
        "medium_linear_boundary": {
            "range": "Q<=2XY",
            "off_diagonal_support": "uv divides D(P,P')",
            "arbitrary_matrix_obstruction": False,
            "determinant_dispersion_required": True,
            "power_saving_proved": False,
        },
        "microscopic_boundary": {
            "unit_modulus_character": "(1/v)=1",
            "unit_edge_reclassified_as_lower_dimensional": True,
            "full_small_side_range_closed": False,
        },
        "norm_split_boundary": {
            "split_prime_roots": "[+r:1],[-r:1] with r^2=-1 mod p",
            "same_sign": "p divides D(P,P')",
            "opposite_sign": "p divides S(P,P')=m*n'+m'*n",
            "state_split_factorization": "q_E=q_same*q_opp with q_same|D and q_opp|S",
            "mixed_sign_sparse_closed_by_q_gt_2XY": False,
        },
        "updated_frontier": "MEDIUM_DETERMINANT_DISPERSION_PLUS_MICROSCOPIC_SMALL_SIDE_INDUCTION_PLUS_NORM_MIXED_SIGN_D_TIMES_S_DISPERSION",
        "decision": {
            "STAGE14_4AX": "SPARSE_LINEAR_L2_CLOSED_AND_DETERMINANT_NORM_OBSTRUCTIONS_ISOLATED",
            "SIX_LINEAR_RECIPROCAL_EDGES_PROJECTIVE": True,
            "LINEAR_COLLISION_DIVIDES_DETERMINANT": True,
            "SPARSE_LINEAR_THRESHOLD_Q_GT_2XY": True,
            "SPARSE_LINEAR_DISCREPANCY_L2_DIAGONAL_SCALE_PROVED": True,
            "N_SCALE_DIAGONAL_GENUINE": True,
            "SPARSE_LINEAR_FIXED_POWER_RETAINER_SAVING_PROVED": False,
            "MEDIUM_LINEAR_OFFDIAGONAL_REDUCED_TO_DETERMINANT": True,
            "MEDIUM_LINEAR_L2_POWER_SAVING_PROVED": False,
            "UNIT_MODULUS_RECIPROCAL_EDGE_RECLASSIFIED": True,
            "FULL_MICROSCOPIC_SMALL_SIDE_CLOSED": False,
            "NORM_SAME_SIGN_COLLISION_DIVIDES_DETERMINANT": True,
            "NORM_OPPOSITE_SIGN_COLLISION_DIVIDES_ANTIDETERMINANT": True,
            "FULL_STATE_SPLIT_E_SPARSE_REGIME_CLOSED": False,
            "EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED": False,
            "EXPLICIT_E_LOC_PROVED": False,
            "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED": False,
            "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4ay prove a medium-range determinant-dispersion estimate for the six linear reciprocal edges and organize the remaining microscopic small-side modes inductively, then isolate the state-split E mixed-sign D*S kernel as a separate norm problem",
        },
    }

    committed = json.loads(SUMMARY.read_text())
    assert committed == report
    print(f"primitive_points={len(pts)}")
    print(f"linear_edge_collision_checks={edge_checks}")
    print(f"norm_sign_checks={norm_checks}")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
