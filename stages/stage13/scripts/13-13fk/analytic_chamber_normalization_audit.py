#!/usr/bin/env python3
"""Deterministic consistency audit for Stage13-13fk.

This script does not replace the analytic proof. It verifies the exact algebraic
normalization recorded by the proof-facing lemma.
"""
from fractions import Fraction


def main() -> None:
    # Work in units of pi^2. One pair-weight octant integral is pi^2/4.
    pair_octant = Fraction(1, 4)
    three_pairs_octant = 3 * pair_octant
    ordered_chamber_sum = three_pairs_octant / 6

    assert pair_octant == Fraction(1, 4)
    assert three_pairs_octant == Fraction(3, 4)
    assert ordered_chamber_sum == Fraction(1, 8)

    # J_q = 2 I_q / pi, so sum J_q is pi times this rational coefficient.
    sum_j_over_pi = 2 * ordered_chamber_sum
    assert sum_j_over_pi == Fraction(1, 4)

    # P_q = 8 I_q / pi^2.
    sum_p = 8 * ordered_chamber_sum
    assert sum_p == 1

    print("STAGE13_13FK_AUDIT=PASS")
    print("PAIR_WEIGHT_OCTANT_INTEGRAL_OVER_PI2=1/4")
    print("THREE_PAIR_OCTANT_INTEGRAL_OVER_PI2=3/4")
    print("SUM_IQ_OVER_PI2=1/8")
    print("SUM_JQ_OVER_PI=1/4")
    print("SUM_PQ=1")


if __name__ == "__main__":
    main()
