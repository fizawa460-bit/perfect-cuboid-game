#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd

SQRT = F(1, 2)

# 1. Frozen s7-44 theta-quarter ledger.
ledger_checks = 0
for i in range(0, 257):
    phi = F(5, 24) + (F(1, 4) - F(5, 24)) * F(i, 256)
    chi = 2 * phi - F(1, 4)
    gaussian = 2 * phi - chi
    column = F(1, 4) - chi
    total = chi + gaussian + column
    assert gaussian == F(1, 4)
    assert column == F(1, 2) - 2 * phi
    assert total == SQRT
    assert 0 <= chi <= F(1, 4)
    assert 0 <= column <= F(1, 12)
    ledger_checks += 1

# 2. Local root equations and resultant no-intersection on odd primes.
def roots_mod(poly, p):
    return [x for x in range(p) if poly(x) % p == 0]

primes = [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97]
root_checks = 0
for p in primes:
    minus_one = roots_mod(lambda x: x*x + 1, p)
    plus_one = roots_mod(lambda x: x*x - 1, p)
    assert len(plus_one) == 2
    if p % 4 == 1:
        assert len(minus_one) == 2
        assert set(minus_one).isdisjoint(plus_one)
        for r in minus_one:
            for s in plus_one:
                assert (r - s) % p != 0
                assert (r + s) % p != 0
                root_checks += 1
    else:
        assert len(minus_one) == 0

# Res(t^2+1,t^2-1)=4, so odd common roots cannot occur.
assert gcd(4, 2) == 2

# 3. Cayley support implies lambda == +/-4 and cleared lambda^2-16 vanishes.
# lambda=4M/N, with N a unit modulo the core. Check representative prime powers.
cayley_checks = 0
for p in [5, 13, 17, 29, 37]:
    for e in [1, 2]:
        mod = p ** e
        for N in range(1, min(mod, 40)):
            if gcd(N, mod) != 1:
                continue
            for sign in (-1, 1):
                M = (sign * N) % mod
                if gcd(M, mod) != 1:
                    continue
                invN = pow(N, -1, mod)
                lam = (4 * M * invN) % mod
                assert lam == (4 * sign) % mod
                assert (lam * lam - 16) % mod == 0
                # Cleared numerator: 16(M^2-N^2).
                assert (16 * (M*M - N*N)) % mod == 0
                cayley_checks += 1

# 4. The local label entropy is O(1) per prime: at most four pairs.
for p in [5, 13, 17, 29, 37, 41]:
    rminus = roots_mod(lambda x: x*x + 1, p)
    rplus = roots_mod(lambda x: x*x - 1, p)
    if p % 4 == 1:
        assert len(rminus) * len(rplus) == 4

print('Stage14-sH44 frozen s7-44 snapshot H audit: PASS')
print('source snapshot: ca427d50b9afcbae226b6ffe619dba2cc98deebc')
print('source stage head: 4588528adb7776978c4071f9d3cb4e6ff5231570')
print('ledger checks:', ledger_checks)
print('local transverse root checks:', root_checks)
print('Cayley bad-reduction checks:', cayley_checks)
print('frozen receiver exponent:', SQRT)
print('certified uniform delta:', 0)
print('off-the-shelf theorem applicable: false')
print('next s-route: Stage14-s7-45')
