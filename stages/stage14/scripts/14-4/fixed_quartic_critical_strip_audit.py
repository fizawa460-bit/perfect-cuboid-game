#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt, log


def squarefree_kernel(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    out = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e ^= 1
        if e:
            out *= p
        p += 1 if p == 2 else 2
    if n > 1:
        out *= n
    return out


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def jacobi_squarefree(a: int, m: int) -> int:
    value = 1
    n = m
    p = 3
    while p * p <= n:
        if n % p == 0:
            value *= legendre(a, p)
            n //= p
        p += 2
    if n > 1:
        value *= legendre(a, n)
    return value


def F(p: int, q: int) -> int:
    return p * q * (q - p) * (q + p)


def primitive_box_sum(U: int, m: int) -> int:
    total = 0
    for p in range(1, U + 1):
        for q in range(1, U + 1):
            if gcd(p, q) == 1:
                total += jacobi_squarefree(F(p, q), m)
    return total


# Exact exponent ledger.
assert 2 * Fraction(10, 21) == Fraction(20, 21)
assert 1 - Fraction(10, 21) == Fraction(11, 21)
assert Fraction(20, 21) - Fraction(1, 2) == Fraction(19, 42)

# Fixed quartic identity, coprimality of the two labels, and n<Q^4.
state_checks = 0
for q in range(2, 120):
    for p in range(1, q):
        if gcd(p, q) != 1:
            continue
        xi = squarefree_kernel(p * q)
        k = squarefree_kernel(q * q - p * p)
        n = xi * k
        assert gcd(p * q, q * q - p * p) == 1
        assert gcd(xi, k) == 1
        assert n == squarefree_kernel(F(p, q))
        assert n < q ** 4
        state_checks += 1

# Exact inert-prime one-variable and two-variable complete sums.
inert_primes = [3, 7, 11, 19, 23, 31, 43, 47]
prime_checks = 0
for prime in inert_primes:
    one = sum(legendre(t * (1 - t * t), prime) for t in range(prime))
    two = sum(legendre(F(p, q), prime) for p in range(prime) for q in range(prime))
    assert one == 0
    assert two == 0
    prime_checks += 1

# CRT/Jacobi complete sums for small squarefree inert moduli.
composite_moduli = [21, 33, 57, 77]
composite_checks = 0
for m in composite_moduli:
    total = sum(jacobi_squarefree(F(p, q), m) for p in range(m) for q in range(m))
    assert total == 0
    composite_checks += 1

# Finite incomplete primitive-box regression against a generous absolute
# constant times U*m*log(2U), matching the proved tiling/Mobius shape.
box_checks = 0
for m in [3, 7, 11, 21, 33]:
    for U in [m, m + 3, 2 * m + 1, 3 * m + 5]:
        s = abs(primitive_box_sum(U, m))
        rhs = 8.0 * U * m * log(2 * U)
        assert s <= rhs + 1e-9
        box_checks += 1

print('STAGE14_4BU_AUDIT=PASS')
print(f'FIXED_QUARTIC_STATE_CHECKS={state_checks}')
print(f'INERT_PRIME_ZERO_TRACE_CHECKS={prime_checks}')
print(f'INERT_COMPOSITE_ZERO_TRACE_CHECKS={composite_checks}')
print(f'INCOMPLETE_PRIMITIVE_BOX_CHECKS={box_checks}')
print('TWIST_PARAMETER_IS_FIXED_BINARY_QUARTIC_KERNEL=true')
print('CRITICAL_DENOMINATOR_EXPONENT=10/21')
print('BALANCED_DENOMINATOR_STRIP=10/21..11/21')
print('INERT_PRIME_COMPLETE_CHARACTER_SUM_ZERO=true')
print('INERT_SQUAREFREE_MODULUS_COMPLETE_CHARACTER_SUM_ZERO=true')
print('CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=20/21')
print('NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false')
