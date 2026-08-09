#!/usr/bin/env python3
"""Stage14-4ay: deterministic structural audit for six-linear slicing dispersion."""

import json
from fractions import Fraction
from itertools import combinations
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
AX = ROOT / "stages/stage14/14-4ax/result.md"
S5J = ROOT / "stages/stage14/14-s5j/result.md"
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
    s5j = S5J.read_text()
    assert "SPARSE_LINEAR_DISCREPANCY_L2_DIAGONAL_SCALE_PROVED=true" in ax
    assert "MEDIUM_LINEAR_L2_POWER_SAVING_PROVED=false" in ax
    assert "LINEAR_COLLISION_DIVIDES_DETERMINANT=true" in s5j
    assert "STATE_SPLIT_E_MIXED_SIGN_OBSTRUCTION_PERSISTS=true" in s5j

    edges = list(combinations(FORMS, 2))
    determinants = []
    for i, j in edges:
        d = abs(det(FORMS[i], FORMS[j]))
        assert d in (1, 2)
        determinants.append(d)
    assert sorted(determinants) == [1, 1, 1, 1, 1, 2]

    # In every opposite-parity class, each edge coordinate pair has exactly
    # the same gcd as (m,n). This is the visible-lattice coordinate lock.
    primitive_equivalence_checks = 0
    for m in range(1, 80):
        for n in range(1, m):
            if (m - n) % 2 == 0:
                continue
            g = gcd(m, n)
            for i, j in edges:
                gij = gcd(abs(value(i, m, n)), abs(value(j, m, n)))
                assert gij == g, (m, n, i, j, g, gij)
                primitive_equivalence_checks += 1

    # Any third linear root is distinct from the two endpoint roots, hence
    # both endpoint coordinates are nonzero there modulo every odd prime.
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

    # At split norm primes, both +/-sqrt(-1) roots are distinct from all four
    # linear roots, so they become unit projective congruences in any edge
    # coordinate system.
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

    # Exact exponent ledger for the Cauchy transfer
    # L(U+V)+UV+L*sqrt(UV), with U,V <= L^(1-kappa).
    exponent_rows = []
    for kappa in (Fraction(1, 10), Fraction(1, 8), Fraction(1, 6), Fraction(1, 4)):
        top = 1 - kappa
        u_exp = top
        v_exp = top
        terms = {
            "L*U": 1 + u_exp,
            "L*V": 1 + v_exp,
            "U*V": u_exp + v_exp,
            "L*sqrt(UV)": 1 + (u_exp + v_exp) / 2,
        }
        maximum = max(terms.values())
        assert maximum == 2 - kappa
        exponent_rows.append(
            {
                "kappa": fstr(kappa),
                "max_side_exponent": fstr(top),
                "transfer_term_exponents": {k: fstr(v) for k, v in terms.items()},
                "maximum": fstr(maximum),
                "saving": fstr(kappa),
            }
        )

    report = {
        "stage": "14-4ay",
        "classification": "SIX_LINEAR_FROZEN_STATE_DISCREPANCY_L2_POWER_SAVING_PROVED",
        "linear_edge_coordinates": {
            "forms": ["m", "n", "m-n", "m+n"],
            "edge_count": 6,
            "transform_determinants_abs": [1, 1, 1, 1, 1, 2],
            "primitive_opposite_parity_equivalence": "gcd(L_i,L_j)=1 iff gcd(m,n)=1 in the corresponding parity class",
        },
        "frozen_state_normal_form": {
            "endpoint_coordinates": "x=a0*u*r; y=b0*v*s",
            "endpoint_moduli_coprime": True,
            "norm_root_sign_refinement_cost": "2^omega(q_E)=B^o(1)",
            "auxiliary_congruence": "r=c*s mod R",
            "c_unit_mod_R": True,
            "R_coprime_to_endpoint_moduli": True,
            "q2_branch_count": "O(1)",
        },
        "slicing_mobius_bound": {
            "effective_scales": "A_*=L/(a0*u), B_*=L/(b0*v)",
            "congruence_count": "area/R + O(A_*+B_*+1)",
            "uniform_in_auxiliary_R": True,
            "pointwise_discrepancy": "Delta_state(u,v) <<_epsilon B^epsilon*(L/(a0*u)+L/(b0*v)+1)",
            "weakened_uniform_bound": "|Delta_state(u,v)| <<_epsilon B^epsilon*(L/u+L/v+1)",
        },
        "dyadic_l2": {
            "definition": "D_lin(U,V)=sum_{u~U,v~V}|Delta_state(u,v)|^2",
            "bound": "D_lin(U,V) <<_epsilon B^epsilon*(L^2*(V/U+U/V)+UV+L^2)",
            "character_transfer": "E_Delta <<_epsilon B^epsilon*(L*(U+V)+UV+L*sqrt(UV))",
            "power_range": "max(U,V)<=L^(1-kappa)",
            "power_saving": "E_Delta << L^(2-kappa+epsilon)",
            "lower_bound_on_min_UV_required": False,
        },
        "endpoint_ledger": {
            "microscopic_discrepancy_closed": True,
            "unit_modulus_bulk_mode": "(1/v)=1; delete reciprocal edge and reclassify as lower-dimensional mode",
            "full_lower_dimensional_bulk_induction_closed": False,
            "upper_endpoint": "max(U,V)~L",
            "upper_switch_target": "rewrite large state piece using complementary kernel piece together with Fourier/Jacobi coefficient",
            "upper_complementary_state_switch_closed": False,
        },
        "norm_boundary": {
            "linear_edge_auxiliary_norm_signs_absorbed_by_projective_congruence": True,
            "remaining_norm_problem": "reciprocal modes involving state-split E=m^2+n^2 pieces",
            "mixed_sign_two_copy_kernel": "q_same|D(P,P'), q_opp|S(P,P')",
            "state_split_E_reciprocal_dispersion_closed": False,
        },
        "updated_frontier": "LOWER_DIMENSIONAL_BULK_MODE_INDUCTION_PLUS_UPPER_COMPLEMENTARY_STATE_SWITCH_PLUS_STATE_SPLIT_E_RECIPROCAL_DISPERSION",
        "decision": {
            "STAGE14_4AY": "SIX_LINEAR_FROZEN_STATE_DISCREPANCY_L2_POWER_SAVING_PROVED",
            "SIX_LINEAR_EDGE_PRIMITIVE_COORDINATES": True,
            "AUXILIARY_NORM_ROOT_SIGN_REFINEMENT_SUBPOWER": True,
            "FROZEN_AUXILIARY_STATE_SINGLE_PROJECTIVE_CONGRUENCE": True,
            "SLICING_ERROR_UNIFORM_IN_AUXILIARY_MODULUS": True,
            "SIX_LINEAR_POINTWISE_DISCREPANCY_BOUND_PROVED": True,
            "SIX_LINEAR_DYADIC_L2_DISPERSION_PROVED": True,
            "SIX_LINEAR_MEDIUM_DISCREPANCY_POWER_SAVING_PROVED": True,
            "MICROSCOPIC_DISCREPANCY_CLOSED": True,
            "FULL_MICROSCOPIC_BULK_INDUCTION_CLOSED": False,
            "UPPER_COMPLEMENTARY_STATE_SWITCH_CLOSED": False,
            "STATE_SPLIT_E_RECIPROCAL_DISPERSION_CLOSED": False,
            "EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED": False,
            "EXPLICIT_E_LOC_PROVED": False,
            "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED": False,
            "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4az close the finite lower-dimensional bulk-mode induction and formulate/prove the upper complementary-state switch for linear columns; in parallel isolate the state-split E reciprocal modes for the s5 norm-dispersion track",
        },
    }

    committed = json.loads(SUMMARY.read_text())
    assert committed == report
    print(f"edge_count={len(edges)}")
    print(f"primitive_equivalence_checks={primitive_equivalence_checks}")
    print(f"linear_root_checks={linear_root_checks}")
    print(f"norm_root_checks={norm_root_checks}")
    print(json.dumps(exponent_rows, indent=2))
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
