#!/usr/bin/env python3
"""Deterministic audit for Stage14-4bv.

Checks:
- exact inert-prime projective zero trace for G_ab=b^2 y^4-a^2 x^4;
- exact additive Fourier identity T=p*chi(b^2 h^4-a^2 k^4);
- the dual coefficient identity for H_xy=y^4 b^2-x^4 a^2;
- exact threshold/exponent ledger for the thick/thin switch.
"""
from cmath import exp, pi
from fractions import Fraction
from math import gcd


def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def G(a, b, x, y, p):
    return (b * b * pow(y, 4, p) - a * a * pow(x, 4, p)) % p


def H(x, y, a, b, p):
    return (pow(y, 4, p) * b * b - pow(x, 4, p) * a * a) % p


def projective_trace_G(p, a, b):
    # affine slopes [t:1] plus infinity [1:0]
    s = sum(chi(G(a, b, t, 1, p), p) for t in range(p))
    s += chi(G(a, b, 1, 0, p), p)
    return s


def projective_trace_H(p, x, y):
    s = sum(chi(H(x, y, t, 1, p), p) for t in range(p))
    s += chi(H(x, y, 1, 0, p), p)
    return s


def fourier_G(p, a, b, h, k):
    total = 0j
    for x in range(p):
        for y in range(p):
            c = chi(G(a, b, x, y, p), p)
            if c:
                total += c * exp(2j * pi * (h * x + k * y) / p)
    return total


def fourier_H(p, x, y, h, k):
    total = 0j
    for a in range(p):
        for b in range(p):
            c = chi(H(x, y, a, b, p), p)
            if c:
                total += c * exp(2j * pi * (h * a + k * b) / p)
    return total


def audit_fourier():
    primes = [3, 7, 11, 19]
    samples = [(1, 1), (1, 2), (2, 1), (2, 3)]
    checked = 0
    for p in primes:
        assert p % 4 == 3
        for a, b in samples:
            if a % p == 0 or b % p == 0:
                continue
            assert projective_trace_G(p, a, b) == 0
            for h in range(p):
                for k in range(p):
                    got = fourier_G(p, a, b, h, k)
                    want = 0 if (h == 0 and k == 0) else p * chi(b*b*pow(h, 4, p) - a*a*pow(k, 4, p), p)
                    assert abs(got.real - want) < 1e-7
                    assert abs(got.imag) < 1e-7
                    checked += 1

        for x, y in samples:
            if x % p == 0 or y % p == 0:
                continue
            assert projective_trace_H(p, x, y) == 0
            for h in range(p):
                for k in range(p):
                    got = fourier_H(p, x, y, h, k)
                    want = 0 if (h == 0 and k == 0) else p * chi(pow(y,4,p)*h*h - pow(x,4,p)*k*k, p)
                    assert abs(got.real - want) < 1e-7
                    assert abs(got.imag) < 1e-7
                    checked += 1
    return checked


def audit_ledger():
    current = Fraction(20, 21)
    tau = Fraction(2, 21)
    assert Fraction(1, 1) - tau / 2 == current

    eta = Fraction(1, 210)
    assert Fraction(1, 1) - (tau + eta) / 2 == current - eta / 2

    small_num = Fraction(3, 7)
    denom_upper = Fraction(11, 21)
    assert small_num + denom_upper == current

    numerator_coeff = small_num - 2 * tau
    denominator_coeff = Fraction(10, 21) - 2 * tau
    assert numerator_coeff == Fraction(5, 21)
    assert denominator_coeff == Fraction(2, 7)

    sqrt_gap = current - Fraction(1, 2)
    assert sqrt_gap == Fraction(19, 42)
    return {
        "current": current,
        "tau": tau,
        "small_num": small_num,
        "num_coeff": numerator_coeff,
        "den_coeff": denominator_coeff,
        "sqrt_gap": sqrt_gap,
    }


def main():
    checked = audit_fourier()
    ledger = audit_ledger()
    print(f"FOURIER_MODES_CHECKED={checked}")
    print("INERT_PROJECTIVE_TRACE_ZERO=true")
    print("INERT_ADDITIVE_FOURIER_TRANSFORM_EXACT=true")
    print("DUAL_COEFFICIENT_FOURIER_TRANSFORM_EXACT=true")
    print(f"CURRENT_WHOLE_FAMILY_EXPONENT={ledger['current']}")
    print(f"CRITICAL_SQUAREPART_THICKNESS={ledger['tau']}")
    print(f"SMALL_NUMERATOR_THRESHOLD={ledger['small_num']}")
    print(f"THIN_NUMERATOR_COEFFICIENT_LOWER={ledger['num_coeff']}")
    print(f"THIN_DENOMINATOR_COEFFICIENT_LOWER={ledger['den_coeff']}")
    print(f"CURRENT_GAP_TO_SQRT={ledger['sqrt_gap']}")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
