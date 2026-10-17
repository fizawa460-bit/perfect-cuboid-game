#!/usr/bin/env python3
"""Stage32 BOUNDARY-FIXED-POINT-HECKE (research cycle 32R-18): computational checks for the fixed-point Hecke lemma.
Checks only arithmetic and finite-group facts; the geometric proof is in CONTRACT.md and needs hostile audit.

Lemma (proved in CONTRACT.md; the general-omega case uses the monotone bound 6*2^w*n/h <= 6n(1/4)^w):
#Fix(iota) = 48 but #Fix(iota) <= 6 * 2^omega(g) * n / h(g), with n = d/2 = deg f_i and h(g) = prod N(P)^(k-1)(N(P)+1).
What this script ACTUALLY checks (finite illustrations only; not a substitute for the proofs in CONTRACT.md):
  1. the numerical inequality 6*2^w*n/8^w < 48 for n in {22, 24} and w = 1..11;
  2. involutions of PGL2(F_p) fix 0 or 2 points of P^1(F_p), for p = 7, 23;
  3. a pair (x, y) in PGL2(F_p) with x^2 = y^3 = 1 and xy of order 8 EXISTS (p = 7, 23).
NOT checked here: that such a pair generates PGL2(F_p), the perfectness of SL2 over finite local rings, or any
geometric statement.  These are argued in CONTRACT.md.
"""
from itertools import product
from sympy import primerange


def hecke_min_per_prime():
    # smallest N(P)+1 over unramified primes of Z[sqrt2]: p = ±1 mod 8 split (N = p), ±3 mod 8 inert (N = p^2)
    best = None
    for p in primerange(3, 200):
        N = p if p % 8 in (1, 7) else p * p
        best = N + 1 if best is None else min(best, N + 1)
    return best


hmin = hecke_min_per_prime()
assert hmin == 8
for n in (22, 24):
    for w in range(1, 12):
        bound = 6 * 2 ** w * n / (hmin ** w)       # h >= 8^w
        assert bound < 48, (n, w, bound)
    print(f"n={n}: max over omega of 6*2^w*n/8^w = {6*2*n/8:.1f} < 48 (omega=1); decreasing in omega")


def pgl2(p):
    mats = []
    for a, b, c, d in product(range(p), repeat=4):
        if (a * d - b * c) % p:
            mats.append((a, b, c, d))
    return mats


def mul(x, y, p):
    a, b, c, d = x; e, f, g, h = y
    return ((a*e+b*g) % p, (a*f+b*h) % p, (c*e+d*g) % p, (c*f+d*h) % p)


def proj_key(m, p):
    # normalise up to scalar
    for v in m:
        if v:
            inv = pow(v, p - 2, p)
            return tuple(x * inv % p for x in m)


def order(m, p):
    k, x, I = 1, m, proj_key((1, 0, 0, 1), p)
    while proj_key(x, p) != I:
        x = mul(x, m, p); k += 1
        if k > 1000:
            return None
    return k


def fixed_points(m, p):
    a, b, c, d = m
    cnt = 0
    for x in range(p):                       # points (x:1)
        if ((a*x+b) - x*(c*x+d)) % p == 0:
            cnt += 1
    if c % p == 0:                           # point (1:0) fixed iff c = 0
        cnt += 1
    return cnt


for p in (7, 23):
    G = {proj_key(m, p): m for m in pgl2(p)}
    elems = list(G.values())
    invol = [m for m in elems if order(m, p) == 2]
    fps = sorted({fixed_points(m, p) for m in invol})
    assert set(fps) <= {0, 2}, fps
    # find a (2,3,8)-pair generating something containing order-8 elements
    found = False
    ord3 = [m for m in elems if order(m, p) == 3]
    for x in invol[:200]:
        for y in ord3[:200]:
            if order(mul(x, y, p), p) == 8:
                found = True; break
        if found:
            break
    assert found
    print(f"p={p}: |PGL2|={len(elems)}, involution fixed-point counts {fps}, (2,3,8)-pair with xy of order 8 exists")
print("PASS: fixed-point Hecke lemma inequality and local facts")
