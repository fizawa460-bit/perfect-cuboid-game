#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s5t.

The proof is in stages/stage14/14-s5t/result.md.  This script checks the exact
threshold ledger, the 1/41 optimizer, compatibility with the previously closed
s5n/s5r sectors, and the B-scale exponent conversion.
"""

from fractions import Fraction
import json


def saving_terms(sigma: Fraction, lam: Fraction):
    return {
        "A_long_long": sigma / 2,
        "B_very_long": lam / 2 - 3 * sigma / 4,
        "C_periodic_perimeter": 1 - 8 * lam,
        "C_periodic_quadratic": 2 - 12 * lam,
    }


def exact_optimizer():
    delta = Fraction(1, 41)
    sigma = Fraction(2, 41)
    lam = Fraction(5, 41)
    terms = saving_terms(sigma, lam)

    assert terms["A_long_long"] == delta
    assert terms["B_very_long"] == delta
    assert terms["C_periodic_perimeter"] == delta
    assert terms["C_periodic_quadratic"] == Fraction(22, 41)
    assert min(terms.values()) == delta

    # Algebraic equalities used by the proof.
    assert lam == 5 * sigma / 2
    assert delta == sigma / 2
    assert delta == 1 - 8 * lam

    return delta, sigma, lam, terms


def rational_grid_stress(delta_star: Fraction):
    """Finite stress test around the analytic optimum.

    This is regression evidence, not the proof of optimality.  We sample a fine
    rational grid and verify that no tested threshold pair exceeds 1/41.
    """
    best = Fraction(-1000, 1)
    best_pair = None
    tested = 0
    den = 820  # contains the exact optimizer: 40/820 and 100/820.
    for i in range(1, 180):
        sigma = Fraction(i, den)
        for j in range(i + 1, 260):
            lam = Fraction(j, den)
            terms = saving_terms(sigma, lam)
            d = min(terms.values())
            tested += 1
            if d > best:
                best = d
                best_pair = (sigma, lam)
    assert best == delta_star, (best, best_pair, delta_star)
    assert best_pair == (Fraction(2, 41), Fraction(5, 41)), best_pair
    return tested, best_pair


def all_short_exponent_ledger(lam: Fraction):
    # Q and tuple count are each M^(4 lambda).
    q_exp = 4 * lam
    tuple_exp = 4 * lam
    perimeter_term = 1 + q_exp + tuple_exp
    quadratic_term = 2 * q_exp + tuple_exp
    assert perimeter_term == Fraction(81, 41)
    assert quadratic_term == Fraction(60, 41)
    assert 2 - perimeter_term == Fraction(1, 41)
    assert 2 - quadratic_term == Fraction(22, 41)
    return {
        "Q_exponent": str(q_exp),
        "tuple_count_exponent": str(tuple_exp),
        "perimeter_total_exponent": str(perimeter_term),
        "quadratic_total_exponent": str(quadratic_term),
    }


def case_b_ledger(sigma: Fraction, lam: Fraction):
    q_neighbor = 3 * sigma
    completion_relative_exponent = -lam / 2 + q_neighbor / 4
    assert q_neighbor == Fraction(6, 41)
    assert completion_relative_exponent == Fraction(-1, 41)
    return {
        "neighbor_product_exponent": str(q_neighbor),
        "relative_exponent": str(completion_relative_exponent),
    }


def s5r_compatibility(sigma: Fraction, delta: Fraction):
    # Near-area mixed completion exponent from s5r:
    # 1 + 5/4 - 17/40 + 3*sigma/4 = 73/40 + 3*sigma/4.
    mixed_exp = Fraction(73, 40) + 3 * sigma / 4
    mixed_saving = 2 - mixed_exp
    assert mixed_exp == Fraction(3053, 1640)
    assert mixed_saving == Fraction(227, 1640)
    assert mixed_saving > delta

    prior_savings = {
        "s5l_linear_central": Fraction(1, 5),
        "s5n_small_medium": Fraction(1, 10),
        "s5n_switched_large": Fraction(1, 20),
        "s5n_double_switched": Fraction(1, 5),
        "s5r_root_spacing_far": Fraction(3, 20),
    }
    for name, d in prior_savings.items():
        assert d > delta, (name, d, delta)

    return {
        "mixed_exponent": str(mixed_exp),
        "mixed_saving": str(mixed_saving),
        "prior_savings": {k: str(v) for k, v in prior_savings.items()},
    }


def physical_conversion(delta: Fraction):
    euclid_count_exp = 2 - delta
    b_exp = euclid_count_exp / 2
    assert euclid_count_exp == Fraction(81, 41)
    assert b_exp == Fraction(81, 82)

    old_delta = Fraction(1, 200)
    old_b_exp = (2 - old_delta) / 2
    assert old_b_exp == Fraction(399, 400)
    assert b_exp < old_b_exp

    return {
        "euclid_count_exponent": str(euclid_count_exp),
        "new_B_exponent": str(b_exp),
        "old_B_exponent": str(old_b_exp),
        "B_exponent_improvement": str(old_b_exp - b_exp),
    }


def numerical_sanity(delta: Fraction):
    # Purely illustrative regression numbers.
    rows = []
    for M in (10**4, 10**8, 10**12):
        old_rel = M ** (-1 / 200)
        new_rel = M ** (-float(delta))
        assert new_rel < old_rel
        rows.append({"M": M, "old_relative": old_rel, "new_relative": new_rel})
    return rows


def main():
    delta, sigma, lam, terms = exact_optimizer()
    tested, best_pair = rational_grid_stress(delta)
    all_short = all_short_exponent_ledger(lam)
    case_b = case_b_ledger(sigma, lam)
    compat = s5r_compatibility(sigma, delta)
    physical = physical_conversion(delta)
    sanity = numerical_sanity(delta)

    report = {
        "metadata": {
            "stage": "14-s5t",
            "classification": "EXACT_EXPONENT_LEDGER_PLUS_REGRESSION_AUDIT",
        },
        "optimizer": {
            "delta": str(delta),
            "sigma": str(sigma),
            "lambda": str(lam),
            "terms": {k: str(v) for k, v in terms.items()},
        },
        "rational_grid": {
            "tested_pairs": tested,
            "best_pair": [str(best_pair[0]), str(best_pair[1])],
        },
        "all_short": all_short,
        "case_b": case_b,
        "s5r_compatibility": compat,
        "physical_conversion": physical,
        "numerical_sanity": sanity,
    }
    print(json.dumps(report, indent=2, sort_keys=True))

    decisions = {
        "STAGE14_S5T": "COMPLETE_SAVING_BUDGET_OPTIMIZATION_AND_ALL_SHORT_BOTTLENECK_ISOLATION",
        "OLD_GRAPH_SAVING_1_OVER_200_STRUCTURAL": False,
        "GRAPH_ESCAPE_GENERAL_THRESHOLD_LEDGER_PROVED": True,
        "GRAPH_ESCAPE_OPTIMAL_SIGMA": "2/41",
        "GRAPH_ESCAPE_OPTIMAL_LAMBDA": "5/41",
        "GRAPH_ESCAPE_OPTIMAL_SAVING": "1/41",
        "OPTIMAL_WITHIN_CURRENT_THREE_CASE_ARCHITECTURE": True,
        "S5R_E_TRANSITION_COMPATIBLE_WITH_OPTIMIZED_THRESHOLDS": True,
        "ACTUAL_LOCAL_SYSTEM_POWER_SAVING_EXPONENT": "1/41",
        "ACTIVE_PHYSICAL_BASE_UPPER_BOUND_EXPONENT": "81/82",
        "ACTIVE_PHYSICAL_BASE_POWER_SAVING_UPPER_BOUND_IMPROVED": True,
        "ALL_SHORT_ABSOLUTE_TUPLE_SUM_IS_CURRENT_BOTTLENECK": True,
        "NEW_ARITHMETIC_RESONANCE_FOUND": False,
        "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
        "GLOBAL_SOLUBILITY_AVERAGED": False,
        "SMALL_POINT_DISTRIBUTION_PROVED": False,
        "SQRT_B_ASYMPTOTIC_PROVED": False,
        "S5T_SUBSTAGE_SPLIT_REQUIRED": False,
        "NEXT": "Stage14-s5u",
    }
    for key, value in decisions.items():
        if isinstance(value, bool):
            value = str(value).lower()
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
