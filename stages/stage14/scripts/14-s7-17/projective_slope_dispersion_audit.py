#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-17."""

from __future__ import annotations

from fractions import Fraction
from math import gcd


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def jacobi_two(a: int, p: int, q: int) -> int:
    return legendre(a, p) * legendre(a, q)


def projective_trace_prime(p: int, A: int, B0: int) -> int:
    return sum(legendre(A - B0 * pow(t, 4, p), p) for t in range(p))


def projective_trace_two(p: int, q: int, A: int, B0: int) -> int:
    m = p * q
    return sum(jacobi_two(A - B0 * pow(t, 4, m), p, q) for t in range(m))


def primitive_box(R: int, S: int) -> list[tuple[int, int]]:
    return [
        (r, s)
        for r in range(1, R + 1)
        for s in range(1, S + 1)
        if gcd(r, s) == 1
    ]


def slope(r: int, s: int, m: int) -> int:
    return (-r * pow(s, -1, m)) % m


def check_slope_injectivity(points: list[tuple[int, int]], p: int) -> None:
    seen: dict[int, tuple[int, int]] = {}
    max_det = 0
    for r1, s1 in points:
        for r2, s2 in points:
            max_det = max(max_det, abs(r1 * s2 - r2 * s1))
    assert max_det < p

    for z in points:
        t = slope(*z, p)
        assert t not in seen, (p, t, seen[t], z)
        seen[t] = z


def check_character_reduction(
    points: list[tuple[int, int]], p: int, q: int, A: int, B0: int
) -> list[tuple[int, int]]:
    m = p * q
    good = []
    for r, s in points:
        F = A * s**4 - B0 * r**4
        if F % p == 0 or F % q == 0:
            continue
        assert gcd(s, m) == 1
        t = slope(r, s, m)
        lhs = jacobi_two(F, p, q)
        rhs = jacobi_two(A - B0 * pow(t, 4, m), p, q)
        assert lhs == rhs
        good.append((r, s))
    return good


def check_centered_transfer(
    points: list[tuple[int, int]], p: int, q: int, A: int, B0: int
) -> None:
    m = p * q
    slopes = [slope(r, s, m) for r, s in points]
    assert len(slopes) == len(set(slopes))
    H = len(slopes)
    assert H < m

    X = [jacobi_two(A - B0 * pow(t, 4, m), p, q) for t in range(m)]
    assert sum(X) == 1

    nu = [0] * m
    for t in slopes:
        nu[t] = 1

    mu = Fraction(H, m)
    b = [Fraction(v, 1) - mu for v in nu]
    assert sum(b) == 0

    norm = sum(v * v for v in b)
    assert norm == Fraction(H, 1) - Fraction(H * H, m)

    S = sum(nu[t] * X[t] for t in range(m))
    Y = sum(b[t] * X[t] for t in range(m))
    assert Fraction(S, 1) == Y + mu

    primal_centered = Fraction(S * S - H, 1)
    projective_centered = Y * Y - norm
    correction = 2 * mu * Y + Fraction(H * H, m * m) - Fraction(H * H, m)
    assert primal_centered == projective_centered + correction
    assert abs(correction) <= Fraction(6 * H * H, m)


def check_exponent_ledger() -> None:
    determinant = Fraction(1, 8)
    rho = Fraction(1, 7)
    assert rho > determinant
    assert rho - determinant == Fraction(1, 56)

    # Critical fixed-k mass H_k <= B^(1/8+o(1)).
    H_exp = Fraction(1, 8)
    assert H_exp == determinant

    # A single auxiliary prime at rho=1/7 is already above the alias scale.
    assert rho > H_exp


def main() -> None:
    # Fixed split: k_-=2, k_+=5, so both quartic coefficients are squares.
    k_minus = 2
    k_plus = 5
    A = k_plus**2
    B0 = k_minus**2

    # Two inert primes.  Both exceed every cross determinant in this box.
    p, q = 43, 47
    assert p % 4 == q % 4 == 3
    assert projective_trace_prime(p, A, B0) == 1
    assert projective_trace_prime(q, A, B0) == 1
    assert projective_trace_two(p, q, A, B0) == 1

    points = primitive_box(3, 4)
    check_slope_injectivity(points, p)
    check_slope_injectivity(points, q)

    good = check_character_reduction(points, p, q, A, B0)
    assert len(good) >= 5
    check_centered_transfer(good, p, q, A, B0)

    check_exponent_ledger()

    print("Stage14-s7-17 audit: OK")
    print(f"primitive points={len(points)}, good points={len(good)}")
    print("projective trace p=q-local=1 and pq-global=1")
    print("slope alias threshold exponent=1/8")
    print("rho=1/7 margin=1/56")
    print("centered transfer correction <= 6 H^2/m")


if __name__ == "__main__":
    main()
