#!/usr/bin/env python3
"""Stage14-4ax: audit sparse-linear L2 transfer into the main retainer chain."""

import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
AW = ROOT / "stages/stage14/14-4aw/result.md"
S5I = ROOT / "stages/stage14/14-s5i/result.md"
S5J = ROOT / "stages/stage14/14-s5j/result.md"
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


def det(p, q):
    m, n = p
    mp, np = q
    return m * np - mp * n


def anti(p, q):
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
    s5j = S5J.read_text()

    assert "DISCREPANCY_SECOND_MOMENT_PROVED=false" in aw
    assert "PURE_EUCLID_DIVISIBILITY_BULK_SEPARABLE=true" in s5i
    assert "STAGE14_S5J=COMPLETE_PROJECTIVE_COLLISION_REDUCTION_AND_SPARSE_LINEAR_L2_BOUND" in s5j
    assert "SPARSE_LINEAR_L2_DISPERSION=O_epsilon(N*B^epsilon)" in s5j
    assert "N_SCALE_DIAGONAL_UNAVOIDABLE=true" in s5j
    assert "MEDIUM_LINEAR_OFFDIAGONAL_REDUCED_TO_DETERMINANT_DIVISORS=true" in s5j
    assert "STATE_SPLIT_E_MIXED_SIGN_OBSTRUCTION_PERSISTS=true" in s5j

    # Recheck the four projective linear roots directly.
    projective_checks = 0
    for p in PRIMES:
        for col in LINEAR:
            roots = 0
            for m in range(p):
                for n in range(p):
                    if m == 0 and n == 0:
                        continue
                    if value(col, m, n) % p == 0:
                        roots += 1
            assert roots == p - 1
            projective_checks += 1

    # Recheck the norm sign collision law over all split test primes.
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
                    assert det(same_p, same_q) % p == 0
                    assert anti(same_p, opp_q) % p == 0
                    norm_checks += 2
        else:
            assert r is None

    # Primitive positive collinear integer vectors are identical.
    primitive = []
    for m in range(2, 25):
        for n in range(1, m):
            if gcd(m, n) == 1 and (m - n) % 2 == 1:
                primitive.append((m, n))
    for i, p in enumerate(primitive):
        for q in primitive[i + 1 :]:
            assert det(p, q) != 0

    report = {
        "stage": "14-4ax",
        "classification": "SPARSE_LINEAR_L2_IMPORTED_AND_MAIN_TRACK_FRONTIER_SHARPENED",
        "imports": {
            "stage14_4aw_endpoint_ledger": True,
            "stage14_s5i_rank_one_bulk": True,
            "stage14_s5j_sparse_linear_l2": True,
        },
        "sparse_linear": {
            "edge_count": 6,
            "collision_determinant": "D(P,P')=m*n'-m'*n",
            "threshold": "Q=UV>2XY",
            "cell_occupancy": "W(u,v) in {0,1}",
            "discrepancy_second_moment": "sum |Delta(u,v)|^2 <<_epsilon N*B^epsilon",
            "natural_diagonal": "N*B^epsilon",
            "naive_cauchy_transfer": "sqrt(Q*N)*B^epsilon",
            "direct_sparse_absolute_bound": "N*B^epsilon",
            "fixed_power_retainer_saving_from_sparse_l2_alone": False,
        },
        "medium_linear": {
            "range": "Q<=2XY",
            "off_diagonal_support": "uv divides D(P,P')",
            "arbitrary_matrix_obstruction": False,
            "determinant_dispersion_required": True,
            "power_saving_proved": False,
        },
        "microscopic": {
            "unit_modulus_character": "(1/v)=1",
            "unit_edge_reclassified_as_lower_dimensional": True,
            "full_small_side_range_closed": False,
            "next_method": "induction on active reciprocal edges and/or divisor switching",
        },
        "norm_split": {
            "same_sign": "p divides D(P,P')",
            "opposite_sign": "p divides S(P,P')=m*n'+m'*n",
            "state_split_factorization": "q_E=q_same*q_opp with q_same|D and q_opp|S",
            "mixed_sign_sparse_closed": False,
        },
        "updated_frontier": "MEDIUM_DETERMINANT_DISPERSION_PLUS_MICROSCOPIC_SMALL_SIDE_INDUCTION_PLUS_NORM_MIXED_SIGN_D_TIMES_S_DISPERSION",
        "decision": {
            "STAGE14_4AX": "SPARSE_LINEAR_L2_IMPORTED_AND_MAIN_TRACK_FRONTIER_SHARPENED",
            "S5J_SPARSE_LINEAR_L2_IMPORTED": True,
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

    assert json.loads(SUMMARY.read_text()) == report
    print(f"projective_root_checks={projective_checks}")
    print(f"norm_sign_checks={norm_checks}")
    print(f"primitive_points={len(primitive)}")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
