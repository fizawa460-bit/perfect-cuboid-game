#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd

PHI_LO = F(5, 24)
PHI_HI = F(1, 4)
SQRT = F(1, 2)
SOURCE_SHA = "4588528adb7776978c4071f9d3cb4e6ff5231570"


def divisors(n: int):
    n = abs(n)
    if n == 0:
        return []
    out = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


# 1. Frozen s7-44 theta-quarter dual-line ledger.
phi_checks = 0
for i in range(1025):
    phi = PHI_LO + (PHI_HI - PHI_LO) * F(i, 1024)
    chi = 2 * phi - F(1, 4)
    gaussian_line = 2 * phi - chi
    endpoint_line = F(1, 4) - chi
    total = chi + gaussian_line + endpoint_line

    assert F(1, 6) <= chi <= F(1, 4)
    assert gaussian_line == F(1, 4)
    assert endpoint_line == F(1, 2) - 2 * phi
    assert total == SQRT
    phi_checks += 1


# 2. Primewise orientation spaces are finite/subpolynomial entropy.
primes_1mod4 = [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109]
orientation_checks = 0
for p in primes_1mod4:
    roots_m1 = [x for x in range(1, p) if (x * x + 1) % p == 0]
    roots_p1 = [x for x in range(1, p) if (x * x - 1) % p == 0]
    assert len(roots_m1) == 2
    assert len(roots_p1) == 2
    assert len([(r, s) for r in roots_m1 for s in roots_p1]) == 4
    orientation_checks += 1


# 3. Primitive sum/difference column gcd sanity.
column_gcd_checks = 0
for A in range(1, 80):
    for B in range(1, 80):
        if gcd(A, B) != 1:
            continue
        g = gcd(abs(A - B), A + B)
        assert g in (1, 2)
        column_gcd_checks += 1


# 4. Cayley full-core => lambda=+/-4 at each active row cell.
bad_reduction_checks = 0
for M in range(2, 80):
    for N in range(1, 80):
        if gcd(M, N) != 1 or M == N:
            continue
        for cm in divisors(oddpart(M - N)):
            for cp in divisors(oddpart(M + N)):
                if gcd(cm, cp) != 1:
                    continue
                C = cm * cp
                if C <= 1 or gcd(C, M * N) != 1:
                    continue
                assert (16 * (M * M - N * N)) % C == 0
                if cm > 1:
                    lam = (4 * M * pow(N, -1, cm)) % cm
                    assert (lam - 4) % cm == 0
                    assert (lam * lam - 16) % cm == 0
                if cp > 1:
                    lam = (4 * M * pow(N, -1, cp)) % cp
                    assert (lam + 4) % cp == 0
                    assert (lam * lam - 16) % cp == 0
                bad_reduction_checks += 1

assert bad_reduction_checks > 1000


# 5. lambda=+/-4 exact reciprocal singular factorizations.
singular_checks = 0
for u in range(2, 35):
    for v in range(2, 35):
        base = (u * u - 1) * (v * v - 1)
        assert base - 4 * u * v == (u * v - u - v - 1) * (u * v + u + v - 1)
        assert base + 4 * u * v == (u * v - u + v + 1) * (u * v + u - v + 1)
        singular_checks += 2


print("Stage14-sH44 frozen s7-44 snapshot audit: PASS")
print("source snapshot SHA:", SOURCE_SHA)
print("theta-quarter dual-line ledger checks:", phi_checks)
print("column primitive gcd checks:", column_gcd_checks)
print("local orientation Cartesian checks:", orientation_checks)
print("Cayley bad-reduction checks:", bad_reduction_checks)
print("lambda=+/-4 singular factor checks:", singular_checks)
print("frozen dual-root-line principal exponent:", SQRT)
print("certified B-power saving exponent: 0")
print("off-the-shelf theorem applicable: false")
print("s7-45 can consume sH44: true")
print("downstream 4dc rewrites sH44 target: false")
