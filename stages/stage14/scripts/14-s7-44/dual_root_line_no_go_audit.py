#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd

SQRT = F(1, 2)

# Exponent ledger on theta=1/4.
for n in range(0, 257):
    phi = F(5, 24) + (F(1, 4) - F(5, 24)) * F(n, 256)
    chi = 2 * phi - F(1, 4)
    gauss = 2 * phi - chi
    col = F(1, 4) - chi
    assert gauss == F(1, 4)
    assert col == F(1, 2) - 2 * phi
    assert chi + gauss + col == SQRT
    assert F(0) <= col <= F(1, 12)

# Primitive endpoint sum/difference gcd identity.
primitive_checks = 0
for a in range(1, 80):
    for b in range(1, 80):
        g = gcd(a, b)
        gm = gcd(a - b, a + b)
        # odd part of gcd(a-b,a+b) divides gcd(a,b)
        odd = gm
        while odd % 2 == 0 and odd:
            odd //= 2
        assert g % odd == 0
        primitive_checks += 1

# Local orientation system: for primes 1 mod 4, roots of -1 and signs ±1
# form a full Cartesian label set at the level of the imported congruences.
def roots_minus_one(p):
    return [x for x in range(1, p) if (x * x + 1) % p == 0]

orientation_checks = 0
for p in (5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97):
    roots = roots_minus_one(p)
    assert len(roots) == 2
    signs = [1, p - 1]
    pairs = {(r, s) for r in roots for s in signs}
    assert len(pairs) == 4
    for r, s in pairs:
        assert (r * r + 1) % p == 0
        assert (s * s - 1) % p == 0
        orientation_checks += 1

# Synthetic primitive root-line determinant divisibility checks.
det_checks = 0
for q, rho in ((5, 2), (13, 5), (17, 4), (29, 12), (37, 6)):
    gauss_pts = []
    col_plus = []
    col_minus = []
    for u in range(1, 4 * q + 1):
        for v in range(1, 4 * q + 1):
            if gcd(u, v) != 1:
                continue
            if (u - rho * v) % q == 0:
                gauss_pts.append((u, v))
            if (u - v) % q == 0:
                col_plus.append((u, v))
            if (u + v) % q == 0:
                col_minus.append((u, v))
    for pts in (gauss_pts, col_plus, col_minus):
        for i in range(min(len(pts), 20)):
            for j in range(i + 1, min(len(pts), 20)):
                u1, v1 = pts[i]
                u2, v2 = pts[j]
                assert (u1 * v2 - u2 * v1) % q == 0
                det_checks += 1

print('Stage14-s7-44 dual primitive root-line audit: PASS')
print('theta-quarter exponent blocks:', 257)
print('primitive sum/difference gcd checks:', primitive_checks)
print('local orientation Cartesian checks:', orientation_checks)
print('root-line determinant checks:', det_checks)
print('dual root-line trivial exponent:', SQRT)
print('orientation-only fixed-power saving: false')
print('second full-core determinant spacing proved: false')
print('auxiliary H needed: true')
print('next receiver: SquareRootThetaQuarterGloballyOddPrimitiveFullCoreDualRootLineCompatibilityEnergy')
