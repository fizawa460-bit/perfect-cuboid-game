#!/usr/bin/env python3
from fractions import Fraction


def main():
    # Stage21 ambient-relative constant:
    # (kappa*pi/18) / (9*zeta(3)/(8*pi*G))
    assert Fraction(1, 18) * Fraction(8, 9) == Fraction(4, 81)

    # Equivalent first-face-in-space comparison:
    # N1/NS coefficient = (kappa/(24*pi))*32G = 4*kappa*G/(3*pi)
    assert Fraction(32, 24) == Fraction(4, 3)
    # M1/U coefficient = (3/(4*pi^2))*(36*zeta(3)/pi) = 27*zeta(3)/pi^3
    assert Fraction(3 * 36, 4) == 27
    # Quotient again gives 4/81 times kappa*pi^2*G/zeta(3)
    assert Fraction(4, 3) / 27 == Fraction(4, 81)

    # Encode powers as (B exponent, log exponent).
    U = (3, 0)
    NS = (2, 0)
    M1 = (2, 1)
    N1 = (1, 3)
    M2 = (1, 5)
    N2_lower = (0, Fraction(1, 2))
    # epsilon is carried separately for the upper bound.
    N2_upper_noeps = (Fraction(1, 2), 0)

    def ratio(a, b):
        return (a[0] - b[0], a[1] - b[1])

    assert ratio(NS, U) == (-1, 0)
    assert ratio(N1, M1) == (-1, 2)
    assert ratio(M2, M1) == (-1, 4)
    assert ratio(N2_lower, M2) == (-1, Fraction(-9, 2))
    assert ratio(N2_lower, N1) == (-1, Fraction(-5, 2))
    assert ratio(N2_upper_noeps, M2) == (Fraction(-1, 2), -5)
    assert ratio(N2_upper_noeps, N1) == (Fraction(-1, 2), -3)

    # Ambient-relative J2 bounds.
    J2_lower = ratio(ratio(N2_lower, M2), ratio(NS, U))
    J2_upper = ratio(ratio(N2_upper_noeps, M2), ratio(NS, U))
    assert J2_lower == (0, Fraction(-9, 2))
    assert J2_upper == (Fraction(1, 2), -5)

    # Second-order I bounds, either vertical-ratio or horizontal-ratio form.
    I_lower_v = ratio(ratio(N2_lower, M2), ratio(N1, M1))
    I_upper_v = ratio(ratio(N2_upper_noeps, M2), ratio(N1, M1))
    I_lower_h = ratio(ratio(N2_lower, N1), ratio(M2, M1))
    I_upper_h = ratio(ratio(N2_upper_noeps, N1), ratio(M2, M1))
    assert I_lower_v == I_lower_h == (0, Fraction(-13, 2))
    assert I_upper_v == I_upper_h == (Fraction(1, 2), -7)

    print('STAGE24_60_INTERACTION_FORMULA_AUDIT=PASS')
    print('J2_LOWER=log^(-9/2)')
    print('J2_UPPER=B^(1/2+epsilon) log^(-5)')
    print('I_LOWER=log^(-13/2)')
    print('I_UPPER=B^(1/2+epsilon) log^(-7)')


if __name__ == '__main__':
    main()
