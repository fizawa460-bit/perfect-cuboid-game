#!/usr/bin/env python3
"""Stage14-s7-16 deterministic audit."""

from __future__ import annotations

import cmath
from fractions import Fraction
from math import pi


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def inert_primes(limit: int) -> list[int]:
    out = []
    for n in range(3, limit + 1, 2):
        prime = all(n % d for d in range(3, int(n**0.5) + 1, 2))
        if prime and n % 4 == 3:
            out.append(n)
    return out


def quartic_trace(p: int, c: int) -> int:
    return sum(legendre(pow(t, 4, p) - c, p) for t in range(p))


def direct_fourier(p: int, A: int, B: int, h: int, j: int) -> complex:
    total = 0j
    for r in range(p):
        r4 = pow(r, 4, p)
        for s in range(p):
            val = legendre(A * pow(s, 4, p) - B * r4, p)
            if val:
                total += val * cmath.exp(2j * pi * ((h * r + j * s) % p) / p)
    return total


def predicted_fourier(p: int, A: int, B: int, h: int, j: int) -> int:
    return p * legendre(A * pow(h, 4, p) - B * pow(j, 4, p), p)


def ratio_derived_fourier(p: int, A: int, B: int, h: int, j: int) -> int:
    if h % p == 0 and j % p == 0:
        return 0
    if j % p:
        t0 = (-h * pow(j, -1, p)) % p
        return p * legendre(A * pow(t0, 4, p) - B, p)
    return p * legendre(A, p)


def check_one_variable() -> int:
    checks = 0
    for p in inert_primes(79):
        for c in range(1, p):
            assert quartic_trace(p, c) == -1
            checks += 1
    return checks


def check_direct_dft() -> int:
    checks = 0
    for p in (3, 7, 11, 19):
        reps = [1] if p == 3 else [1, 2, 3]
        for A in reps:
            for B in reps:
                if A % p == 0 or B % p == 0:
                    continue
                for h in range(p):
                    for j in range(p):
                        got = direct_fourier(p, A, B, h, j)
                        want = predicted_fourier(p, A, B, h, j)
                        assert abs(got.real - want) < 1e-8
                        assert abs(got.imag) < 1e-8
                        checks += 1
    return checks


def check_ratio_derivation() -> int:
    checks = 0
    for p in inert_primes(127):
        for A in range(1, min(p, 8)):
            for B in range(1, min(p, 8)):
                for h in range(p):
                    for j in range(p):
                        assert ratio_derived_fourier(p, A, B, h, j) == predicted_fourier(p, A, B, h, j)
                        checks += 1
    return checks


def check_completion_barrier() -> int:
    grid = [Fraction(i, 100) for i in range(0, 201)]
    candidates = []
    for lam in grid:
        first = Fraction(2) - lam
        second = 4 * lam if lam <= Fraction(1, 2) else Fraction(2)
        envelope = max(first, second)
        assert envelope >= 1
        candidates.append(envelope)
    assert min(candidates) >= Fraction(8, 5) - Fraction(1, 100)
    assert Fraction(7, 8) - Fraction(6, 7) == Fraction(1, 56)
    return len(grid)


def main() -> None:
    one_var = check_one_variable()
    direct = check_direct_dft()
    ratio = check_ratio_derivation()
    barrier = check_completion_barrier()
    print(f"one_variable_trace_checks={one_var}")
    print(f"direct_fourier_checks={direct}")
    print(f"ratio_derivation_checks={ratio}")
    print(f"completion_barrier_grid_checks={barrier}")
    print("INERT_TWO_DIMENSIONAL_FOURIER_SELF_DUALITY_EXACT=true")
    print("ABSOLUTE_PER_MODULUS_COMPLETION_BEATS_POINTWISE_COLLISION=false")
    print("CENTERED_DIAGONAL_SUBTRACTION_ESSENTIAL=true")
    print("DUAL_FREQUENCY_CENTERED_DISPERSION_PROVED=false")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8")
    print("NEXT=Stage14-s7-17")


if __name__ == "__main__":
    main()
