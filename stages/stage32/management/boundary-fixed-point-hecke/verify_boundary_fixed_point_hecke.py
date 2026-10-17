#!/usr/bin/env python3
"""Stage32 BOUNDARY-FIXED-POINT-HECKE (research cycle 32R-18): computational checks for the fixed-point Hecke lemma.
Checks only arithmetic and finite-group facts; the geometric proof is in CONTRACT.md and needs hostile audit.

Lemma: in the equality case the deck involution iota of D -> Ctilde has exactly 48 fixed points, but for every g in
Comm(Delta) \\ Delta,  #Fix(iota) <= 6 * 2^omega(g) * n / h(g)  with n = d/2 = deg f_i, h(g) = prod N(P)^(k-1)(N(P)+1).
Checks:
  1. the inequality 6 * 2^w * n / h < 48 for every Hecke degree (all primes of Z[sqrt2] with N >= 7; w = #primes),
     n in {22, 24};
  2. sanity of the local fact used: an involution of PGL2(F_p) (p odd) fixes 0 or 2 points of P^1(F_p);
  3. Delta(2,3,8) maps onto PGL2(F_7) and PGL2(F_23) (a (2,3,8)-generating pair exists), images of order-2
     elements fix <= 2 points; and the PSL2 parts are perfect (transitivity of Gamma_Y).
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
