#!/usr/bin/env python3
"""Exact Stage29-02f odd-primary Frobenius witness.

Inputs are the audited Stage29-02e weight-3 newform coefficients recovered
from the exact K3 trace checkpoint.  No floating point or external package is
used.

For a weight-3 two-dimensional H^2 piece with Frobenius polynomial
    X^2 - a_p X + p^2,
a fixed vector after Tate twist (1) modulo an odd ell != p forces
    ell | (2*p - a_p).

For the full endpoint transcendental package
    3*h16 + h32 + 3*h8,
we form the determinant numerator
    D_p=(2p-a16)^3*(2p-a32)*(2p-a8)^3.
"""

from math import gcd

PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

A = {
    "h16": [0, -6, 0, 0, 10, -30, 0, 0, 42, 0, -70, 18, 0, 0],
    "h32": [2, 0, 0, -14, 0, 2, 34, 0, 0, 0, 0, -46, -14, 0],
    "h8":  [-2, 0, 0, 14, 0, 2, -34, 0, 0, 0, 0, -46, 14, 0],
}


def gcd_all(values):
    g = 0
    for value in values:
        g = gcd(g, abs(value))
    return g


def is_power_of_two(n):
    return n > 0 and n & (n - 1) == 0


rows = []
for i, p in enumerate(PRIMES):
    n16 = 2 * p - A["h16"][i]
    n32 = 2 * p - A["h32"][i]
    n8 = 2 * p - A["h8"][i]
    det_num = n16**3 * n32 * n8**3
    rows.append((p, n16, n32, n8, det_num))

# Individual two-dimensional pieces already have no common odd divisor.
assert gcd_all([r[1] for r in rows]) == 2
assert gcd_all([r[2] for r in rows]) == 2
assert gcd_all([r[3] for r in rows]) == 2

# Full rank-14 determinant witness.
full_gcd = gcd_all([r[4] for r in rows])
assert full_gcd == 128

# For ell equal to one of the test primes, p=ell cannot be used.  Removing
# that row must still leave no common odd divisor.
for ell in PRIMES:
    g = gcd_all([r[4] for r in rows if r[0] != ell])
    assert is_power_of_two(g), (ell, g)

print("p  2p-a16  2p-a32  2p-a8")
for p, n16, n32, n8, _ in rows:
    print(f"{p:2d} {n16:8d} {n32:8d} {n8:7d}")
print(f"gcd full determinant numerators = {full_gcd}")
print("all p=ell excluded-row gcds are powers of two")
print("PASS")
