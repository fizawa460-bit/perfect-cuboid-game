#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt


def q(z):
    return z**4 - 20*z**2 + 256*z - 412


def qh(a, b):
    return a**4 - 20*a*a*b*b + 256*a*b**3 - 412*b**4


def short_from_minimal(a2, a4, a6):
    # y^2=x^3+a2*x^2+a4*x+a6; set u=x+a2/3, then X=9u, W=27y.
    A = Fraction(a4) - Fraction(a2*a2, 3)
    B = Fraction(a6) - Fraction(a2*a4, 3) + Fraction(2*a2**3, 27)
    return A * 81, B * 729


def divisors(n):
    n = abs(n)
    out = set()
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.add(d)
            out.add(n // d)
    return sorted(out)


def main():
    assert q(2) == 36
    assert q(-2) == -988
    assert 988 == 4 * 13 * 19

    # Shift identities controlling the resultants.
    for b in range(-7, 8):
        for t in range(-7, 8):
            if b == 0:
                continue
            assert qh(2*b + t, b) == (
                36*b**4 + 208*b**3*t + 4*b*b*t*t + 8*b*t**3 + t**4
            )
            assert qh(-2*b + t, b) == (
                -988*b**4 + 304*b**3*t + 4*b*b*t*t - 8*b*t**3 + t**4
            )

    # Q has no rational root: monic means any rational root is an integer divisor of 412.
    for d in divisors(412):
        assert q(d) != 0
        assert q(-d) != 0

    # Exact minimal-model adapters for the elliptic twists used in A1-9.
    adapters = {
        1: (1, 95, 703),
        -1: (-1, 95, -703),
        3: (0, 852, 18128),
        -3: (0, 852, -18128),
        19: (1, 34175, 4616575),
        -19: (-1, 34175, -4616575),
    }
    for delta, model in adapters.items():
        A, B = short_from_minimal(*model)
        assert A == delta**2 * 7668
        assert B == delta**3 * 489456

    # Sanity-check the square-denominator and squareclass claims on a large exact box:
    # whenever the cleared odd-degree equation is a square, the predicted restrictions hold.
    # This is not the proof; the proof is the gcd argument in result.md.
    for sign, allowed in [(-1, {1, -1, 3, -3}), (1, {1, -1, 13, -13, 19, -19, 247, -247})]:
        for b in range(1, 80):
            for a in range(-120, 121):
                from math import gcd
                if gcd(abs(a), b) != 1:
                    continue
                n = b * (a + sign*2*b) * qh(a, b)
                if n < 0:
                    continue
                r = isqrt(n)
                if r*r != n:
                    continue
                assert isqrt(b)**2 == b
                t = a + sign*2*b
                h = qh(a, b)
                # Signed squareclass of a nonzero integer.
                if t == 0 or h == 0:
                    continue
                def sqclass(x):
                    s = -1 if x < 0 else 1
                    x = abs(x)
                    p = 2
                    d = 1
                    while p*p <= x:
                        e = 0
                        while x % p == 0:
                            x //= p
                            e ^= 1
                        if e:
                            d *= p
                        p += 1
                    if x > 1:
                        d *= x
                    return s*d
                assert sqclass(t) == sqclass(h)
                assert sqclass(t) in allowed

    print("Q_endpoint_values=PASS")
    print("shift_resultant_identities=PASS")
    print("Q_rational_root_test=PASS")
    print("elliptic_twist_model_adapters=PASS")
    print("bounded_squareclass_sanity=PASS")
    print("A1-9 exact verification: PASS")


if __name__ == "__main__":
    main()
