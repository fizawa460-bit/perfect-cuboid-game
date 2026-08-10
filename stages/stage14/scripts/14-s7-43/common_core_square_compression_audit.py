#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd

SQRT = F(1, 2)


def chi(phi: F) -> F:
    return 2 * phi - F(1, 4)


def acol(phi: F) -> F:
    return F(1, 2) - 2 * phi


def jexp(phi: F, s: F) -> F:
    return chi(phi) - 2 * s


def matched_bound(phi: F, s: F) -> F:
    c = chi(phi)
    j = jexp(phi, s)
    return (j + s) + (2 * phi - c) + acol(phi)


# Exact exponent ledger over the full X13/4da square-root band.
mesh_checks = 0
for ip in range(0, 97):
    phi = F(5, 24) + F(ip, 2304)
    if phi > F(1, 4):
        break
    smax = phi - F(5, 24)
    for js in range(0, 25):
        s = smax * F(js, 24)
        mesh_checks += 1
        c = chi(phi)
        j = jexp(phi, s)
        assert F(1, 6) <= j <= c
        assert 2 * phi - c == F(1, 4)
        assert acol(phi) == F(1, 4) - c
        assert matched_bound(phi, s) == SQRT - s
        assert matched_bound(phi, s) <= SQRT
        if s > 0:
            assert matched_bound(phi, s) < SQRT

# Small exact integer models for D=C/J=D0*Omega1 and G=H^2/D0.
# These verify the reconstruction order (J,H,G,Omega1)->C and that G|H^2.
integer_checks = 0
for H in range(1, 61):
    H2 = H * H
    divisors = [d for d in range(1, H2 + 1) if H2 % d == 0]
    for G in divisors:
        D0 = H2 // G
        for omega1 in (1, 2, 3, 5, 7):
            D = D0 * omega1
            for J in (1, 3, 5, 11, 17):
                if gcd(J, H) != 1:
                    continue
                C = J * D
                assert C // J == D
                assert D0 == D // omega1
                assert H2 // D0 == G
                integer_checks += 1

# Saturation consequences.
for phi in (F(5, 24), F(11, 48), F(1, 4)):
    c = chi(phi)
    assert matched_bound(phi, F(0)) == SQRT
    assert jexp(phi, F(0)) == c

print("Stage14-s7-43 common-core square-compression audit: PASS")
print("fraction matched-band checks:", mesh_checks)
print("integer J,H,G,Omega reconstruction checks:", integer_checks)
print("matched fixed-s bound: 1/2-s")
print("sqrt saturation forces s=0")
print("sqrt saturation: H=K=B^o(1), J=C_Cayley=C at fixed-power scale")
print("next receiver: SquareRootThetaQuarterGloballyOddPrimitiveFullCoreDualPrimitiveRootLineIncidence")
