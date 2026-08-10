#!/usr/bin/env python3
"""Stage14-s7-16 deterministic audit.

Checks:
- inert one-variable quartic trace sum chi(t^4-c)=-1;
- exact 2D Fourier self-duality for F=A*s^4-B*r^4 at small inert primes;
- exact algebraic ratio derivation for a larger prime range;
- centered absolute-completion barrier algebra;
- locked Stage14-s7-16 theorem boundary.
"""

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
    """Integer-only derivation using the r!=0 ratio decomposition."""
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
            assert quartic_trace(p, c) == -1, (p, c, quartic_trace(p, c))
            checks += 1
    return checks


def check_direct_dft() -> int:
    checks = 0
    # Direct complex DFT is only used at small primes; the tolerance is far below
    # the integer gap between possible predicted values {-p,0,p}.
    for p in (3, 7, 11, 19):
        reps = [1]
        if p > 3:
            reps += [2, 3]
        for A in reps:
            if A % p == 0:
                continue
            for B in reps:
                if B % p == 0:
                    continue
                for h in range(p):
                    for j in range(p):
                        got = direct_fourier(p, A, B, h, j)
                        want = predicted_fourier(p, A, B, h, j)
                        assert abs(got.real - want) < 1e-8, (p, A, B, h, j, got, want)
                        assert abs(got.imag) < 1e-8, (p, A, B, h, j, got, want)
                        checks += 1
    return checks


def check_ratio_derivation() -> int:
    checks = 0
    for p in inert_primes(127):
        for A in range(1, min(p, 8)):
            for B in range(1, min(p, 8)):
                for h in range(p):
                    for j in range(p):
                        got = ratio_derived_fourier(p, A, B, h, j)
                        want = predicted_fourier(p, A, B, h, j)
                        assert got == want, (p, A, B, h, j, got, want)
                        checks += 1
    return checks


def check_completion_barrier() -> int:
    """Exact exponent audit for C <= H^2/L + min(H,L^2)^2."""
    # Write L=H^lambda.  For lambda<=1/2, first exponent is 2-lambda,
    # which is >=3/2.  For lambda>=1/2, the second exponent is 2.
    grid = [Fraction(i, 100) for i in range(0, 201)]
    for lam in grid:
        first = Fraction(2) - lam
        second = min(Fraction(1), 2 * lam) * 2
        envelope = max(first, second)
        assert envelope >= 1
    # The best absolute-completion exponent is still >1; the known pointwise
    # genus-one collision bound has exponent 1 in H.
    candidates = []
    for lam in grid:
        first = Fraction(2) - lam
        second = 4 * lam if lam <= Fraction(1, 2) else Fraction(2)
        candidates.append(max(first, second))
    assert min(candidates) >= Fraction(8, 5) - Fraction(1, 100)

    # Conditional global ledger from s7-15 remains 7/8 -> 6/7, gain 1/56.
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
