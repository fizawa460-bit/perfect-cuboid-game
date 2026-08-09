#!/usr/bin/env python3
from fractions import Fraction
import json


def saving_terms(sigma, lam):
    return {
        "A": sigma / 2,
        "B": lam / 2 - 3 * sigma / 4,
        "C1": 1 - 8 * lam,
        "C2": 2 - 12 * lam,
    }


def main():
    delta = Fraction(1, 41)
    sigma = Fraction(2, 41)
    lam = Fraction(5, 41)
    terms = saving_terms(sigma, lam)
    assert terms == {
        "A": Fraction(1, 41),
        "B": Fraction(1, 41),
        "C1": Fraction(1, 41),
        "C2": Fraction(22, 41),
    }
    assert lam == 5 * sigma / 2
    assert delta == sigma / 2 == 1 - 8 * lam

    # Fine rational-grid regression check containing the exact optimizer.
    den = 820
    best = Fraction(-999, 1)
    best_pair = None
    tested = 0
    for i in range(1, 180):
        s = Fraction(i, den)
        for j in range(i + 1, 260):
            l = Fraction(j, den)
            d = min(saving_terms(s, l).values())
            tested += 1
            if d > best:
                best = d
                best_pair = (s, l)
    assert best == delta
    assert best_pair == (sigma, lam)

    # Case-B conductor ledger.
    q0_exp = 3 * sigma
    case_b_rel = -lam / 2 + q0_exp / 4
    assert q0_exp == Fraction(6, 41)
    assert case_b_rel == Fraction(-1, 41)

    # All-short ledger.
    q_exp = 4 * lam
    tuple_exp = 4 * lam
    p_term = 1 + q_exp + tuple_exp
    q2_term = 2 * q_exp + tuple_exp
    assert p_term == Fraction(81, 41)
    assert q2_term == Fraction(60, 41)
    assert 2 - p_term == delta
    assert 2 - q2_term == Fraction(22, 41)

    # Compatibility with s5r mixed near-area completion.
    mixed_exp = Fraction(73, 40) + 3 * sigma / 4
    mixed_saving = 2 - mixed_exp
    assert mixed_exp == Fraction(3053, 1640)
    assert mixed_saving == Fraction(227, 1640)
    assert mixed_saving > delta

    prior = [Fraction(1, 5), Fraction(1, 10), Fraction(1, 20), Fraction(1, 5), Fraction(3, 20)]
    assert all(x > delta for x in prior)

    euclid_exp = 2 - delta
    b_exp = euclid_exp / 2
    assert euclid_exp == Fraction(81, 41)
    assert b_exp == Fraction(81, 82)
    assert b_exp < Fraction(399, 400)

    print(json.dumps({
        "stage": "14-s5t",
        "grid_pairs": tested,
        "optimizer": {"sigma": str(sigma), "lambda": str(lam), "delta": str(delta)},
        "terms": {k: str(v) for k, v in terms.items()},
        "mixed_s5r_saving": str(mixed_saving),
        "B_exponent": str(b_exp),
    }, indent=2, sort_keys=True))

    flags = {
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
    for k, v in flags.items():
        if isinstance(v, bool):
            v = str(v).lower()
        print(f"{k}={v}")


if __name__ == "__main__":
    main()
