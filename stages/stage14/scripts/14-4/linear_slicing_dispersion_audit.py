#!/usr/bin/env python3
"""Stage14-4ay: audit frozen-state stability and six-linear interior summation."""

import json
from fractions import Fraction
from itertools import combinations
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
AX = ROOT / "stages/stage14/14-4ax/result.md"
S5K = ROOT / "stages/stage14/14-s5k/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/linear_slicing_dispersion_summary.json"

FORMS = {
    "m": (1, 0),
    "n": (0, 1),
    "m-n": (1, -1),
    "m+n": (1, 1),
}
PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)


def value(name: str, m: int, n: int) -> int:
    a, b = FORMS[name]
    return a * m + b * n


def det(v, w):
    return v[0] * w[1] - v[1] * w[0]


def root_rep(name: str, p: int):
    if name == "m":
        return (0, 1)
    if name == "n":
        return (1, 0)
    if name == "m-n":
        return (1, 1)
    if name == "m+n":
        return (-1 % p, 1)
    raise ValueError(name)


def sqrt_minus_one(p: int):
    for r in range(1, p):
        if (r * r + 1) % p == 0:
            return r
    return None


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> None:
    ax = AX.read_text()
    s5k = S5K.read_text()
    assert "SPARSE_LINEAR_DISCREPANCY_L2_DIAGONAL_SCALE_PROVED=true" in ax
    assert "LINEAR_SIX_POINTWISE_DISCREPANCY_PROVED=true" in s5k
    assert "MEDIUM_LINEAR_L2_DISPERSION_PROVED=true" in s5k
    assert "LINEAR_RECIPROCAL_DISCREPANCY_BOUND_PROVED=true" in s5k
    assert "FULL_LINEAR_SIX_DYADIC_SUMMATION_PROVED=false" in s5k
    assert "STATE_SPLIT_E_MIXED_SIGN_OBSTRUCTION_PERSISTS=true" in s5k

    edges = list(combinations(FORMS, 2))
    determinants = [abs(det(FORMS[i], FORMS[j])) for i, j in edges]
    assert sorted(determinants) == [1, 1, 1, 1, 1, 2]

    primitive_checks = 0
    for m in range(1, 80):
        for n in range(1, m):
            if (m - n) % 2 == 0:
                continue
            g = gcd(m, n)
            for i, j in edges:
                gij = gcd(abs(value(i, m, n)), abs(value(j, m, n)))
                assert gij == g
                primitive_checks += 1

    linear_root_checks = 0
    for p in PRIMES:
        for i, j in edges:
            for k in FORMS:
                if k in (i, j):
                    continue
                m, n = root_rep(k, p)
                assert value(k, m, n) % p == 0
                assert value(i, m, n) % p != 0
                assert value(j, m, n) % p != 0
                linear_root_checks += 1

    norm_root_checks = 0
    for p in PRIMES:
        r = sqrt_minus_one(p)
        if p % 4 == 3:
            assert r is None
            continue
        assert r is not None
        for sign in (1, -1):
            m, n = (sign * r) % p, 1
            assert (m * m + n * n) % p == 0
            for i, j in edges:
                assert value(i, m, n) % p != 0
                assert value(j, m, n) % p != 0
                norm_root_checks += 1

    exponent_rows = []
    for kappa in (Fraction(1, 10), Fraction(1, 8), Fraction(1, 6), Fraction(1, 4)):
        discrepancy = 2 - kappa
        bulk = 2 - kappa / 2
        full_mode = max(discrepancy, bulk)
        assert full_mode == bulk
        exponent_rows.append(
            {
                "kappa": fstr(kappa),
                "discrepancy_exponent": fstr(discrepancy),
                "bulk_exponent": fstr(bulk),
                "full_mode_exponent": fstr(full_mode),
                "full_mode_saving": fstr(kappa / 2),
            }
        )

    report = {
        "stage": "14-4ay",
        "classification": "FROZEN_STATE_LINEAR_DISPERSION_STABLE_AND_INTERIOR_FULL_MODE_SUMMED",
        "imported_s5k": {
            "six_linear_pointwise_discrepancy": True,
            "medium_linear_l2": True,
            "linear_reciprocal_discrepancy_bound": True,
            "bare_full_dyadic_summation_was_open": True,
        },
        "frozen_state_extension": {
            "endpoint_coordinates": "x=a0*u*r; y=b0*v*s",
            "endpoint_moduli_coprime": True,
            "norm_root_sign_refinement_cost": "2^omega(q_E)=B^o(1)",
            "auxiliary_congruence": "r=c*s mod R",
            "c_unit_mod_R": True,
            "R_coprime_to_endpoint_moduli": True,
            "q2_branch_count": "O(1)",
            "slicing_error_uniform_in_R": True,
            "pointwise_bound": "Delta_state << B^epsilon*(1+H_i/(a0*u)+H_j/(b0*v))",
        },
        "frozen_state_l2": {
            "bound": "sum|Delta_state|^2 << B^epsilon*(UV+H_i^2*V/U+H_j^2*U/V)",
            "reciprocal_transfer": "sum Delta_state*(u/v) << B^epsilon*(UV+H_i*V+H_j*U)",
            "balanced_medium_consequence": "max(U,V)<=L^(1-kappa) => discrepancy << L^(2-kappa+epsilon)",
            "lower_bound_on_min_UV_required_for_discrepancy": False,
        },
        "full_linear_interior": {
            "bulk_input": "E_bulk << L^(2+epsilon)*sqrt(1/U+1/V)",
            "interior_range": "L^kappa<=U,V<=L^(1-kappa)",
            "bulk_bound": "L^(2-kappa/2+epsilon)",
            "discrepancy_bound": "L^(2-kappa+epsilon)",
            "full_mode_bound": "L^(2-kappa/2+epsilon)",
            "dyadic_state_sum": "L^(2-kappa/2+o(1))",
            "interior_full_mode_power_saving": True,
        },
        "endpoint_ledger": {
            "microscopic_discrepancy_closed": True,
            "bounded_side_bulk_reclassification": "delete reciprocal edge; lower-dimensional character mode",
            "lower_dimensional_induction_formulated": True,
            "lower_dimensional_induction_closed": False,
            "upper_endpoint": "max(U,V)~L",
            "upper_switch_target": "complementary state piece + Jacobi/Fourier coefficient rewrite",
            "upper_complementary_state_fourier_switch_closed": False,
        },
        "norm_boundary": {
            "linear_edge_auxiliary_norm_signs_absorbed": True,
            "remaining_norm_problem": "reciprocal modes involving state-split E=m^2+n^2 pieces",
            "mixed_sign_kernel": "q_same|D(P,P'), q_opp|S(P,P')",
            "state_split_E_reciprocal_dispersion_closed": False,
        },
        "updated_frontier": "LOWER_DIMENSIONAL_BULK_MODE_INDUCTION_PLUS_UPPER_COMPLEMENTARY_STATE_FOURIER_SWITCH_PLUS_STATE_SPLIT_E_RECIPROCAL_DISPERSION",
        "decision": {
            "STAGE14_4AY": "FROZEN_STATE_LINEAR_DISPERSION_STABLE_AND_INTERIOR_FULL_MODE_SUMMED",
            "S5K_SIX_LINEAR_MEDIUM_DISPERSION_IMPORTED": True,
            "FROZEN_AUXILIARY_STATE_SINGLE_PROJECTIVE_CONGRUENCE": True,
            "FROZEN_AUXILIARY_MODULUS_DOES_NOT_WORSEN_SLICING_ERROR": True,
            "FROZEN_STATE_POINTWISE_DISCREPANCY_BOUND_PROVED": True,
            "FROZEN_STATE_L2_DISPERSION_PROVED": True,
            "SIX_LINEAR_MEDIUM_DISCREPANCY_POWER_SAVING_PROVED": True,
            "SIX_LINEAR_INTERIOR_FULL_MODE_POWER_SAVING_PROVED": True,
            "SIX_LINEAR_INTERIOR_DYADIC_STATE_SUMMATION_PROVED": True,
            "MICROSCOPIC_DISCREPANCY_CLOSED": True,
            "LOWER_DIMENSIONAL_BULK_MODE_INDUCTION_FORMULATED": True,
            "LOWER_DIMENSIONAL_BULK_MODE_INDUCTION_CLOSED": False,
            "UPPER_COMPLEMENTARY_STATE_FOURIER_SWITCH_CLOSED": False,
            "STATE_SPLIT_E_RECIPROCAL_DISPERSION_CLOSED": False,
            "EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED": False,
            "EXPLICIT_E_LOC_PROVED": False,
            "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED": False,
            "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4az close the finite lower-dimensional bulk-mode induction and prove the upper complementary-state Fourier switch for the linear columns, while the s-track attacks the state-split E mixed-sign reciprocal sector",
        },
    }

    committed = json.loads(SUMMARY.read_text())
    assert committed == report
    print(f"edge_count={len(edges)}")
    print(f"primitive_checks={primitive_checks}")
    print(f"linear_root_checks={linear_root_checks}")
    print(f"norm_root_checks={norm_root_checks}")
    print(json.dumps(exponent_rows, indent=2))
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
