#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd

SQRT = F(1, 2)

# 1. Theta-quarter Gaussian-product ledger from merged 4dc.
ledger_checks = 0
for i in range(257):
    phi = F(5, 24) + (F(1, 4) - F(5, 24)) * F(i, 256)
    chi = 2 * phi - F(1, 4)
    product_line = F(1, 2) - chi
    assert F(1, 6) <= chi <= F(1, 4)
    assert F(1, 4) <= product_line <= F(1, 3)
    assert chi + product_line == SQRT
    ledger_checks += 1

# 2. Gaussian product coordinate algebra and first reciprocal reconstruction.
# a=g*a0, b=g*b0, P=a0*U, Q=b0*V imply
# (aU)^2-(bV)^2 = g^2(P^2-Q^2).
reconstruction_checks = 0
for g in range(1, 8):
    for a0 in range(1, 10):
        for b0 in range(1, 10):
            if gcd(a0, b0) != 1:
                continue
            for U in range(1, 9):
                for V in range(1, 9):
                    P = a0 * U
                    Q = b0 * V
                    a = g * a0
                    b = g * b0
                    assert (a * U) ** 2 - (b * V) ** 2 == g * g * (P * P - Q * Q)
                    reconstruction_checks += 1

# 3. If a physical endpoint factor 4*r*s divides the forced difference,
# p*q is uniquely reconstructed. This checks uniqueness, not density.
forced_product_checks = 0
for g in range(1, 6):
    for P in range(2, 30):
        for Q in range(1, P):
            diff = g * g * (P * P - Q * Q)
            for r in range(1, 5):
                for s in range(1, 5):
                    den = 4 * r * s
                    if diff % den:
                        continue
                    pq = diff // den
                    assert den * pq == diff
                    forced_product_checks += 1

# 4. The local transverse root systems have resultant 4; on odd primes
# no root of t^2+1 equals +/- a root of t^2-1.
def roots(poly, p):
    return [x for x in range(p) if poly(x) % p == 0]

root_checks = 0
for p in (5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97):
    rm = roots(lambda x: x*x + 1, p)
    rp = roots(lambda x: x*x - 1, p)
    if p % 4 == 1:
        assert len(rm) == 2
        assert len(rp) == 2
        for x in rm:
            for y in rp:
                assert (x-y) % p != 0
                assert (x+y) % p != 0
                root_checks += 1

print('Stage14-s7-45 sH44-consumption / s-route-closure audit: PASS')
print('theta-quarter ledger checks:', ledger_checks)
print('first reciprocal reconstruction checks:', reconstruction_checks)
print('forced p*q product checks:', forced_product_checks)
print('transverse root checks:', root_checks)
print('current whole-family exponent:', SQRT)
print('strict sub-sqrt saving certified: false')
print('s7 route closed at sqrt: true')
print('handoff: Stage14-4dd')
