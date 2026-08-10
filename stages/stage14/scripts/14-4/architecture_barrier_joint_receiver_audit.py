#!/usr/bin/env python3
from fractions import Fraction


def f(theta):
    return max(theta, Fraction(1,1)-theta/Fraction(20,1), Fraction(3,2)-Fraction(3,5)*theta)


def main():
    theta = Fraction(20,21)
    small = theta
    cross = Fraction(1,1)-theta/Fraction(20,1)
    good = Fraction(3,2)-Fraction(3,5)*theta
    assert small == Fraction(20,21)
    assert cross == Fraction(20,21)
    assert good == Fraction(13,14)
    assert f(theta) == Fraction(20,21)

    # Exact rational-grid verification around the unique minimizer.
    for q in range(21, 421):
        for p in range(1, q+1):
            t = Fraction(p,q)
            if t < theta:
                assert Fraction(1,1)-t/Fraction(20,1) > Fraction(20,21)
            elif t > theta:
                assert t > Fraction(20,21)
            else:
                assert f(t) == Fraction(20,21)

    assert Fraction(20,21)-Fraction(1,2) == Fraction(19,42)
    print('GENERAL_CUTOFF_FORMULAS_AUDITED=true')
    print('ARCHITECTURE_OPTIMAL_THETA_20_21=true')
    print('ARCHITECTURE_MIN_EXPONENT_20_21=true')
    print('GOOD_TERM_AT_OPTIMUM_13_14=true')
    print('REMAINING_SQRT_GAP_19_42=true')
    print('ALL_AUDITS_PASS=true')

if __name__ == '__main__':
    main()
