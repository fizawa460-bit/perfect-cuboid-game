#!/usr/bin/env python3
"""Deterministic audit for Stage14-4by.

This audit checks the algebraic pieces surrounding the external Lei Fu
Corollary 0.3 contract:

- the six-dimensional Gauss-lift support span;
- normal-crossing transversality of the four Kummer divisors;
- exact exceptional-frequency line cancellation at inert primes;
- finite all-frequency O(p)-scale regression for the universal detector;
- exact 13/14 threshold ledger and barrier arithmetic.

The l-adic mixed-sum theorem itself is an external theorem contract and is not
reproved numerically here.
"""

from fractions import Fraction
from math import cos, gcd, pi, sin


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def detector(r: int, s: int, p: int) -> int:
    return ((1 - (r * s) ** 2) * (s * s - r * r)) % p


def matrix_rank_q(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    m = len(a)
    n = len(a[0]) if m else 0
    rank = 0
    col = 0
    while rank < m and col < n:
        pivot = next((i for i in range(rank, m) if a[i][col] != 0), None)
        if pivot is None:
            col += 1
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        q = a[rank][col]
        a[rank] = [x / q for x in a[rank]]
        for i in range(m):
            if i == rank or a[i][col] == 0:
                continue
            q = a[i][col]
            a[i] = [a[i][j] - q * a[rank][j] for j in range(n)]
        rank += 1
        col += 1
    return rank


def audit_full_dimension_support():
    # Coordinates: R,S,U,V,W,Z.
    U = (0, 0, 1, 0, 0, 0)
    URS = (1, 1, 1, 0, 0, 0)
    V = (0, 0, 0, 1, 0, 0)
    WR = (1, 0, 0, 0, 1, 0)
    WS = (0, 1, 0, 0, 1, 0)
    ZR = (1, 0, 0, 0, 0, 1)
    vectors = [U, URS, V, WR, WS, ZR]
    assert matrix_rank_q(vectors) == 6


def audit_normal_crossing():
    # f1=1-rs, f2=1+rs, f3=s-r, f4=s+r.
    # Check the four hyperbola/line intersection gradient determinants.
    primes = [3, 7, 11, 19, 23, 31]
    for p in primes:
        assert p % 4 == 3
        for r in range(1, p):
            for s in range(1, p):
                vals = [
                    (1 - r * s) % p,
                    (1 + r * s) % p,
                    (s - r) % p,
                    (s + r) % p,
                ]
                grads = [
                    ((-s) % p, (-r) % p),
                    (s % p, r % p),
                    ((-1) % p, 1),
                    (1, 1),
                ]
                for hi in (0, 1):
                    for li in (2, 3):
                        if vals[hi] == 0 and vals[li] == 0:
                            (a, b), (c, d) = grads[hi], grads[li]
                            assert (a * d - b * c) % p != 0


def line_sum_plus(p: int, x: int) -> int:
    inv2 = pow(2, -1, p)
    total = 0
    for y in range(p):
        r = ((x - y) * inv2) % p
        s = ((x + y) * inv2) % p
        total += legendre(detector(r, s, p), p)
    return total


def line_sum_minus(p: int, y: int) -> int:
    inv2 = pow(2, -1, p)
    total = 0
    for x in range(p):
        r = ((x - y) * inv2) % p
        s = ((x + y) * inv2) % p
        total += legendre(detector(r, s, p), p)
    return total


def audit_exceptional_line_cancellation():
    for p in [3, 7, 11, 19, 23, 31, 43, 47]:
        assert p % 4 == 3
        assert legendre(-1, p) == -1
        for x in range(p):
            assert line_sum_plus(p, x) == 0
        for y in range(p):
            assert line_sum_minus(p, y) == 0


def all_fourier_max_ratio(p: int) -> float:
    roots = [complex(cos(2 * pi * j / p), sin(2 * pi * j / p)) for j in range(p)]
    vals = [[legendre(detector(r, s, p), p) for s in range(p)] for r in range(p)]
    max_abs = 0.0
    for h in range(p):
        for k in range(p):
            z = 0j
            for r in range(p):
                hr = h * r
                row = vals[r]
                for s in range(p):
                    if row[s]:
                        z += row[s] * roots[(hr + k * s) % p]
            max_abs = max(max_abs, abs(z))
    return max_abs / p


def audit_finite_fourier_scale():
    # Evidence/regression only. The theorem is supplied by Fu + face audit.
    ratios = {}
    for p in [3, 7, 11, 19, 23, 31]:
        ratio = all_fourier_max_ratio(p)
        ratios[p] = ratio
        assert ratio < 5.0 + 1e-9
    return ratios


def audit_exponent_ledger():
    lam = Fraction(13, 28)
    nu = Fraction(11, 28)
    tau = Fraction(5, 56)
    target = Fraction(13, 14)

    e1 = 2 * lam
    e2 = 1 + nu - lam
    e3 = 1 - Fraction(4, 5) * tau
    e4 = 1 - (nu - 2 * tau) / 3
    e5 = 1 - (lam - 2 * tau) / 3

    assert e1 == target
    assert e2 == target
    assert e3 == target
    assert e4 == target
    assert e5 == Fraction(19, 21)
    assert e5 < target

    assert Fraction(15, 16) - target == Fraction(1, 112)
    assert Fraction(41, 42) - target == Fraction(1, 21)
    assert target - Fraction(1, 2) == Fraction(3, 7)

    # Barrier certificate:
    # lambda<=E/2, nu<=3E/2-1,
    # tau>=5/4(1-E), and nu>=2tau+3(1-E)
    # imply 11/2(1-E)<=3E/2-1, hence E>=13/14.
    E = target
    assert Fraction(11, 2) * (1 - E) == Fraction(11, 28)
    assert Fraction(3, 2) * E - 1 == Fraction(11, 28)

    return {
        "lambda": lam,
        "nu": nu,
        "tau": tau,
        "target": target,
        "denominator_thin": e5,
    }


def main():
    audit_full_dimension_support()
    audit_normal_crossing()
    audit_exceptional_line_cancellation()
    ratios = audit_finite_fourier_scale()
    led = audit_exponent_ledger()

    print("GAUSS_LIFT_SUPPORT_DIMENSION=6")
    print("NORMAL_CROSSING_TRANSVERSALITY_AUDIT=true")
    print("EXCEPTIONAL_FREQUENCY_LINE_SUMS_EXACT_ZERO=true")
    print("FINITE_FOURIER_MAX_OVER_P=" + ",".join(f"{p}:{ratios[p]:.6f}" for p in ratios))
    print(f"OPTIMAL_DENOMINATOR_CUTOFF={led['lambda']}")
    print(f"OPTIMAL_NUMERATOR_CUTOFF={led['nu']}")
    print(f"OPTIMAL_SQUAREPART_THRESHOLD={led['tau']}")
    print(f"NEW_WHOLE_FAMILY_EXPONENT={led['target']}")
    print(f"DENOMINATOR_THIN_EXPONENT={led['denominator_thin']}")
    print("EXACT_13_14_MINIMAX_LEDGER_AUDIT=true")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
