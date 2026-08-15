#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt


def sub(pair_a, pair_b):
    return (pair_a[0] - pair_b[0], pair_a[1] - pair_b[1])


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def main():
    # Encode asymptotic scales as (power of B, power of log B),
    # ignoring positive constants and carrying epsilon symbolically only in text.
    n1 = (Fraction(1), Fraction(3))
    n2_lower = (Fraction(0), Fraction(1, 2))
    n2_upper_no_eps = (Fraction(1, 2), Fraction(0))
    m2_over_m1 = (Fraction(-1), Fraction(4))

    ratio_lower = sub(n2_lower, n1)
    ratio_upper_no_eps = sub(n2_upper_no_eps, n1)
    assert ratio_lower == (Fraction(-1), Fraction(-5, 2))
    assert ratio_upper_no_eps == (Fraction(-1, 2), Fraction(-3))

    cross_lower = sub(ratio_lower, m2_over_m1)
    cross_upper_no_eps = sub(ratio_upper_no_eps, m2_over_m1)
    assert cross_lower == (Fraction(0), Fraction(-13, 2))
    assert cross_upper_no_eps == (Fraction(1, 2), Fraction(-7))

    # Exact C17 witness from the audited Stage24-50 family.
    p, q, z = 38, 43, 569
    assert gcd(p, q) == 1
    assert p**4 + q**4 == 17 * z**2

    e = 4 * p * q
    x = 4 * p * p - q * q
    y = 4 * q * q - p * p
    d = 17 * z

    assert (x, y, e, d) == (3927, 5952, 6536, 9673)
    assert 0 < x < y < e
    assert gcd(gcd(x, y), e) == 1

    # Canonical map (a,b,c)=(x,y,e) gives guaranteed ac and bc faces.
    a, b, c = x, y, e
    ac2 = a * a + c * c
    bc2 = b * b + c * c
    ab2 = a * a + b * b
    assert is_square(ac2)
    assert is_square(bc2)
    assert not is_square(ab2)
    assert a * a + b * b + c * c == d * d

    print("STAGE23_POST24_REINVESTIGATION_AUDIT=PASS")
    print("RATIO_LOWER_EXPONENTS=B^-1 LOG^-5/2")
    print("RATIO_UPPER_EXPONENTS=B^-1/2+epsilon LOG^-3")
    print("CROSS_RATIO_LOWER=LOG^-13/2")
    print("CROSS_RATIO_UPPER=B^1/2+epsilon LOG^-7")
    print("C17_CANONICAL_CHANNEL=ac,bc")
    print(f"C17_WITNESS={(a,b,c,d)}")


if __name__ == "__main__":
    main()
