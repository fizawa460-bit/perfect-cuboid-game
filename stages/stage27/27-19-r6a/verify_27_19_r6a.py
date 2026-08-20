#!/usr/bin/env python3
from math import isqrt


def squarefree_kernel(n: int) -> int:
    assert n > 0
    k = 1
    p = 2
    while p * p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            k *= p
        p += 1 if p == 2 else 2
    if n > 1:
        k *= n
    return k


# Known primitive Stage19 exactly-two + space survivor.
R, e, x, y, A, B = 1073, 840, 448, 495, 952, 975
assert e * e + x * x == A * A
assert e * e + y * y == B * B
assert e * e + x * x + y * y == R * R
assert A * A + y * y == R * R
assert B * B + x * x == R * R
assert isqrt(x * x + y * y) ** 2 != x * x + y * y

P = A * B - x * y
Q = A * B + x * y
assert P > 0 and Q > 0
assert P == 706440
assert Q == 1149960
assert P * Q == (e * R) ** 2

dP = squarefree_kernel(P)
dQ = squarefree_kernel(Q)
assert dP == dQ == 210
u = isqrt(P // dP)
v = isqrt(Q // dQ)
assert dP * u * u == P
assert dP * v * v == Q
assert (u, v) == (58, 74)
assert 2 * A * B == dP * (u * u + v * v)
assert 2 * x * y == dP * (v * v - u * u)
assert e * R == dP * u * v

# Converse algebra on the same exact data: square collision recovers e.
w = isqrt(P * Q)
assert w * w == P * Q
assert w % R == 0
recovered_e = w // R
assert recovered_e == e
assert A * A - x * x == recovered_e * recovered_e
assert B * B - y * y == recovered_e * recovered_e

# Representation-multiplicity no-go: every multiple of 25 has two
# positive representations of R^2, so that weak condition has positive density.
for m in (1, 2, 7, 31, 101):
    R0 = 25 * m
    assert (24 * m) ** 2 + (7 * m) ** 2 == R0 * R0
    assert (20 * m) ** 2 + (15 * m) ** 2 == R0 * R0

# The two fixed base representations do not themselves satisfy the collision;
# this illustrates that the squareclass condition is strictly stronger than
# representation multiplicity alone.
A0, y0, B0, x0 = 24, 7, 20, 15
P0 = A0 * B0 - x0 * y0
Q0 = A0 * B0 + x0 * y0
assert squarefree_kernel(P0) == 15
assert squarefree_kernel(Q0) == 65
assert squarefree_kernel(P0) != squarefree_kernel(Q0)

print("Stage27-19-r6a norm receiver: PASS")
print("Stage27-19-r6a PQ=(eR)^2 identity: PASS")
print("Stage27-19-r6a squarefree-kernel collision: PASS")
print("Stage27-19-r6a exact witness reconstruction: PASS")
print("Stage27-19-r6a two-representation positive-density no-go: PASS")
