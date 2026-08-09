#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s5u.

The analytic argument is in stages/stage14/14-s5u/result.md. This audit checks
projective-lattice indices, the quantifier distinction for Hilbert energy, the
exact 1/21 threshold optimizer, compatibility ledgers, and B-scale conversion.
"""

from fractions import Fraction
from math import gcd
import json


def forms(m: int, n: int):
    return (m, n, m - n, m + n)


def tuple_condition(m: int, n: int, qs):
    return all(f % q == 0 for f, q in zip(forms(m, n), qs))


def projective_index_checks():
    # Pairwise-coprime odd state moduli. q=1 means inactive column.
    tuples = [
        (3, 5, 1, 1),
        (3, 1, 5, 1),
        (1, 3, 5, 7),
        (3, 5, 7, 1),
    ]
    records = []
    for qs in tuples:
        active = [q for q in qs if q > 1]
        for i in range(len(active)):
            for j in range(i):
                assert gcd(active[i], active[j]) == 1
        Q = 1
        for q in qs:
            Q *= q
        count = 0
        for m in range(Q):
            for n in range(Q):
                if tuple_condition(m, n, qs):
                    count += 1
        # One index-Q lattice has exactly Q residue points modulo Q.
        assert count == Q, (qs, Q, count)
        records.append({"q": qs, "Q": Q, "residue_count": count})
    return records


def finite_lattice_boundary_checks():
    # Regression only: compare rectangle lattice count with area/Q and verify an
    # O(M) envelope with a deliberately generous absolute constant.
    tuples = [(3, 5, 1, 1), (3, 1, 5, 1), (1, 3, 5, 7)]
    rows = []
    worst = 0.0
    for qs in tuples:
        Q = 1
        for q in qs:
            Q *= q
        for M in (25, 50, 100):
            actual = 0
            # Positive M x M square; exact area is M^2.
            for m in range(1, M + 1):
                for n in range(1, M + 1):
                    if tuple_condition(m, n, qs):
                        actual += 1
            main = Fraction(M * M, Q)
            err = abs(Fraction(actual, 1) - main)
            ratio = float(err / M)
            worst = max(worst, ratio)
            assert ratio < 8.0, (qs, M, actual, main, ratio)
            rows.append({
                "q": qs,
                "M": M,
                "actual": actual,
                "main": str(main),
                "error_over_M": ratio,
            })
    return rows, worst


def hilbert_quantifier_counterexample(N=64):
    # c_{P_j}=e_j. Each physical point has pointwise ell2 norm 1, while the
    # union/support vector sum_j e_j has squared norm N.
    pointwise_norm_sq = [1 for _ in range(N)]
    union_norm_sq = N
    assert max(pointwise_norm_sq) == 1
    assert union_norm_sq > 1
    return {
        "points": N,
        "max_pointwise_norm_sq": 1,
        "union_norm_sq": union_norm_sq,
        "union_norm": N ** 0.5,
    }


def saving_terms(sigma: Fraction, lam: Fraction):
    return {
        "A_long_long": sigma / 2,
        "B_very_long": lam / 2 - 3 * sigma / 4,
        "C_projective_all_short": 1 - 4 * lam,
    }


def optimizer():
    delta = Fraction(1, 21)
    sigma = Fraction(2, 21)
    lam = Fraction(5, 21)
    terms = saving_terms(sigma, lam)
    assert terms["A_long_long"] == delta
    assert terms["B_very_long"] == delta
    assert terms["C_projective_all_short"] == delta
    assert lam == 5 * sigma / 2
    assert delta == sigma / 2
    assert delta == 1 - 4 * lam
    return delta, sigma, lam, terms


def grid_stress(delta_star):
    den = 840  # contains sigma=80/840 and lambda=200/840.
    best = Fraction(-100, 1)
    best_pair = None
    tested = 0
    for i in range(1, 260):
        sigma = Fraction(i, den)
        for j in range(i + 1, 330):
            lam = Fraction(j, den)
            d = min(saving_terms(sigma, lam).values())
            tested += 1
            if d > best:
                best = d
                best_pair = (sigma, lam)
    assert best == delta_star, (best, best_pair, delta_star)
    assert best_pair == (Fraction(2, 21), Fraction(5, 21)), best_pair
    return tested, best_pair


def compatibility(delta, sigma):
    single_edge = Fraction(1, 20)
    assert single_edge > delta

    mixed_exp = Fraction(73, 40) + 3 * sigma / 4
    mixed_saving = 2 - mixed_exp
    assert mixed_exp == Fraction(531, 280)
    assert mixed_saving == Fraction(29, 280)
    assert mixed_saving > delta

    prior = {
        "single_edge_switched_large": Fraction(1, 20),
        "linear_small_medium": Fraction(1, 10),
        "linear_central": Fraction(1, 5),
        "root_spacing_far": Fraction(3, 20),
    }
    assert all(v > delta for v in prior.values())
    return {
        "mixed_exponent": str(mixed_exp),
        "mixed_saving": str(mixed_saving),
        "prior": {k: str(v) for k, v in prior.items()},
    }


def physical_conversion(delta):
    euclid_exp = 2 - delta
    b_exp = euclid_exp / 2
    assert euclid_exp == Fraction(41, 21)
    assert b_exp == Fraction(41, 42)

    prior_b = Fraction(81, 82)
    current_module_cap_b = Fraction(39, 40)
    assert b_exp < prior_b
    assert current_module_cap_b < b_exp
    return {
        "euclid_exponent": str(euclid_exp),
        "B_exponent": str(b_exp),
        "previous_s5t_B_exponent": str(prior_b),
        "preexisting_single_edge_module_cap_B_exponent": str(current_module_cap_b),
        "remaining_gap_to_module_cap": str(b_exp - current_module_cap_b),
    }


def main():
    lattice = projective_index_checks()
    boundary, worst_boundary = finite_lattice_boundary_checks()
    quantifier = hilbert_quantifier_counterexample()
    delta, sigma, lam, terms = optimizer()
    tested, best_pair = grid_stress(delta)
    compat = compatibility(delta, sigma)
    physical = physical_conversion(delta)

    report = {
        "metadata": {
            "stage": "14-s5u",
            "classification": "PROJECTIVE_LATTICE_REFINEMENT_PLUS_METHOD_CLOSURE_AUDIT",
        },
        "projective_index_checks": lattice,
        "finite_boundary_checks": boundary,
        "finite_boundary_worst_error_over_M": worst_boundary,
        "hilbert_quantifier_counterexample": quantifier,
        "optimizer": {
            "delta": str(delta),
            "sigma": str(sigma),
            "lambda": str(lam),
            "terms": {k: str(v) for k, v in terms.items()},
        },
        "grid": {
            "tested_pairs": tested,
            "best_pair": [str(best_pair[0]), str(best_pair[1])],
        },
        "compatibility": compat,
        "physical_conversion": physical,
    }
    print(json.dumps(report, indent=2, sort_keys=True))

    decisions = {
        "STAGE14_S5U": "COMPLETE_PROJECTIVE_ALL_SHORT_REFINEMENT_AND_S5_METHOD_CLOSURE",
        "FULL_SHORT_STATE_TUPLE_IS_PROJECTIVE_LATTICE": True,
        "FIXED_TUPLE_PROJECTIVE_LATTICE_INDEX_PRODUCT": True,
        "FIXED_TUPLE_CENTERED_DISCREPANCY_O_M": True,
        "ALL_SHORT_GENERIC_PERIODIC_Q_LOSS_REMOVED": True,
        "ALL_SHORT_TUPLEWISE_BOUND": "M^(1+4lambda+epsilon)",
        "HILBERT_POINTWISE_COEFFICIENT_ENERGY_RETAINED": True,
        "HILBERT_GLOBAL_TUPLE_CARDINALITY_ELIMINATION_JUSTIFIED": False,
        "HILBERT_QUANTIFIER_MISMATCH_ISOLATED": True,
        "GRAPH_ESCAPE_OPTIMAL_SIGMA": "2/21",
        "GRAPH_ESCAPE_OPTIMAL_LAMBDA": "5/21",
        "ACTUAL_LOCAL_SYSTEM_POWER_SAVING_EXPONENT": "1/21",
        "ACTIVE_PHYSICAL_BASE_UPPER_BOUND_EXPONENT": "41/42",
        "S5R_E_TRANSITION_COMPATIBLE_WITH_S5U_THRESHOLDS": True,
        "CURRENT_PROVED_SINGLE_EDGE_CEILING": "1/20",
        "NEW_ARITHMETIC_RESONANCE_FOUND": False,
        "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
        "GLOBAL_SOLUBILITY_AVERAGED": False,
        "SMALL_POINT_DISTRIBUTION_PROVED": False,
        "SQRT_B_ASYMPTOTIC_PROVED": False,
        "S5_METHOD_CLOSED": True,
        "S5_SUBSTAGE_SPLIT_REQUIRED": False,
        "NEXT": "Stage14-s6",
    }
    for key, value in decisions.items():
        if isinstance(value, bool):
            value = str(value).lower()
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
