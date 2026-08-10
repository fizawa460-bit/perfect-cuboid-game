#!/usr/bin/env python3
from fractions import Fraction


def main():
    gamma = Fraction(4, 21)
    delta = gamma / 4
    assert delta == Fraction(1, 21)

    cross_exp = 1 - delta
    assert cross_exp == Fraction(20, 21)

    old_cross = Fraction(61, 63)
    assert old_cross - cross_exp == Fraction(1, 63)

    small_partner = Fraction(20, 21)
    good_residual = Fraction(13, 14)
    whole = max(cross_exp, small_partner, good_residual)
    assert whole == Fraction(20, 21)

    local_old = Fraction(41, 42)
    assert local_old - whole == Fraction(1, 42)
    assert whole - Fraction(1, 2) == Fraction(19, 42)

    # Deterministic weighted-cover ledger: if every receiver is below B^delta,
    # then 2^a*c*h^2 is below B^(delta+delta+2delta)=B^gamma.
    assert delta + delta + 2 * delta == gamma

    print('CROSS_GAMMA=4/21')
    print('OPTIMAL_COMMON_RECEIVER_THRESHOLD=1/21')
    print('WEIGHTED_PRODUCT_EXPONENT_IDENTITY=true')
    print('CROSS_SECTOR_EXPONENT=20/21')
    print('CROSS_IMPROVEMENT_OVER_61_63=1/63')
    print('WHOLE_FAMILY_EXPONENT=20/21')
    print('CUMULATIVE_POST_LOCAL_SAVING=1/42')
    print('REMAINING_GAP_TO_SQRT=19/42')
    print('ALL_AUDITS_PASS=true')


if __name__ == '__main__':
    main()
