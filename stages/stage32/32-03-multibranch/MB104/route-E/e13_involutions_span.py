#!/usr/bin/env python3
"""
Exhaustive spanning check for products of involutions in the Bolza order.

Enumerates ALL subsets of size >= 8 of the 12 involutions and checks
the numerical rank of their pairwise products over R.

WARNING: This is a finite computational verification on the model of
the 12 involutions of the Bolza unit group. It is NOT a general proof
that every arithmetic configuration of remaining involutions spans D_B.
Random tests are not proofs.

Environment:
- Python 3.10+
- numpy
- No external data files.

Usage:
    python e13_involutions_span.py

All randomness (if any) uses seed 42.
"""

from fractions import Fraction as Fr
import itertools
import numpy as np

np.random.seed(42)

Z0 = (Fr(0), Fr(0)); ONE = (Fr(1), Fr(0))
def ka(p, q): return (p[0] + q[0], p[1] + q[1])
def km(p, q): return (p[0]*q[0] + 2*p[1]*q[1], p[0]*q[1] + p[1]*q[0])
def kc(c): return (Fr(c), Fr(0))
A = kc(-3); B = (Fr(0), Fr(1)); AB = km(A, B)
mAB = (-AB[0], -AB[1]); mB = (-B[0], -B[1]); mA = (-A[0], -A[1])

def qm(x, y):
    a0, a1, a2, a3 = x; b0, b1, b2, b3 = y; m = km
    r0 = ka(ka(m(a0,b0), m(A, m(a1,b1))), ka(m(B, m(a2,b2)), m(mAB, m(a3,b3))))
    r1 = ka(ka(m(a0,b1), m(a1,b0)), ka(m(mB, m(a2,b3)), m(B, m(a3,b2))))
    r2 = ka(ka(m(a0,b2), m(a2,b0)), ka(m(A, m(a1,b3)), m(mA, m(a3,b1))))
    r3 = ka(ka(m(a0,b3), m(a3,b0)), ka(m(a1,b2), (-m(a2,b1)[0], -m(a2,b1)[1])))
    return (r0, r1, r2, r3)

def qs(c, x): return tuple(km(c, x[t]) for t in range(4))
def qa(*xs):
    o = (Z0,)*4
    for x in xs: o = tuple(ka(o[t], x[t]) for t in range(4))
    return o
def nrd(x):
    a0, a1, a2, a3 = x
    return ka(ka(km(a0,a0), km(mA, km(a1,a1))), ka(km(mB, km(a2,a2)), km(AB, km(a3,a3))))

Q1 = (ONE, Z0, Z0, Z0)
m1 = qs(kc(-1), Q1)
I = (Z0, ONE, Z0, Z0)
J = (Z0, Z0, ONE, Z0)
alpha = qs((Fr(1,2), Fr(0)), qa(Q1, I))
gamma = qm(qs((Fr(1,6), Fr(0)), qa(qs(kc(3), Q1), I)), qa(Q1, qs((Fr(-1), Fr(-1)), J)))
beta = qm(alpha, qa(Q1, qs((Fr(-1), Fr(1)), gamma)))

group = {str(Q1): Q1}
frontier = [Q1]
while frontier and len(group) < 500:
    nxt = []
    for g in frontier:
        for h in [alpha, beta]:
            p = qm(g, h)
            key = str(p)
            if key not in group and nrd(p) == ONE:
                group[key] = p
                nxt.append(p)
    frontier = nxt

invols = [g for g in group.values() if qm(g, g) in (Q1, m1) and g not in (Q1, m1)]
print(f"Total involutions found: {len(invols)}")

def to_vec(x):
    return [float(c[0]) for c in x] + [float(c[1]) for c in x]

def product_rank(subset):
    prods = [qm(i1, i2) for i1, i2 in itertools.combinations(subset, 2)]
    if len(prods) < 4:
        return 0
    M = np.array([to_vec(p) for p in prods])
    return np.linalg.matrix_rank(M, tol=1e-8)

def main():
    print("Exhaustive check for subsets of size >= 8")
    print("WARNING: This is finite enumeration on the model of 12 involutions.")
    print("Random tests are not proofs. This does not constitute a general proof.")
    sizes = [8, 9, 10, 11, 12]
    for size in sizes:
        count = 0
        full = 0
        for subset in itertools.combinations(invols, size):
            count += 1
            r = product_rank(subset)
            if r == 8:
                full += 1
        print(f"Size {size}: {full}/{count} full rank")
    print("Done.")

if __name__ == "__main__":
    main()
