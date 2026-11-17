#!/usr/bin/env python3
"""E19 s13: shortest closed geodesic of the octahedral orbifold group Gamma_oct (sphere, 6 cone points of order 2,
equilateral pi/4 triangles) and of the triangle group Delta(2,3,8) that contains it with index 24.
Gamma_oct = kernel of Delta(2,3,8) -> S4 (A -> order 2, B -> order 3, AB -> order 4).  Every slack-0 map p has
orbifold group inside Gamma_oct, so its hyperbolic translation lengths are >= the value printed here."""
import math, itertools
import numpy as np
from mpmath import mp, mpf, matrix, cos, sin, acosh, cosh, exp, pi
mp.dps = 30
d = acosh(cos(pi/8)/sin(pi/3))                     # distance between the order-2 and order-3 centres
def rot(theta):                                    # rotation about i by 2*theta
    return matrix([[cos(theta), sin(theta)], [-sin(theta), cos(theta)]])
T = matrix([[exp(d/2), 0], [0, exp(-d/2)]]); Ti = matrix([[exp(-d/2), 0], [0, exp(d/2)]])
A = rot(pi/2); B = T*rot(pi/3)*Ti; Bi = T*rot(-pi/3)*Ti
AB = A*B
assert abs(abs(AB[0,0]+AB[1,1]) - 2*cos(pi/8)) < mpf(10)**-20
# S4 images: find a = transposition-type order 2, b order 3 with ab of order 4
S = list(itertools.permutations(range(4)))
def mul(p, q): return tuple(p[q[i]] for i in range(4))      # (p*q)(i) = p(q(i))
def order(p):
    e = tuple(range(4)); k, x = 1, p
    while x != e: x = mul(x, p); k += 1
    return k
ok = None
for a in S:
    if order(a) != 2: continue
    for b in S:
        if order(b) == 3 and order(mul(a, b)) == 4: ok = (a, b); break
    if ok: break
a, b = ok; bi = tuple(sorted(range(4), key=lambda i: b[i]))
e = tuple(range(4))
gens = [(A, a), (B, b), (Bi, bi)]
# BFS over words, dedupe by rounded matrix up to sign
def key(M):
    v = [float(M[0,0]), float(M[0,1]), float(M[1,0]), float(M[1,1])]
    if v[0] < 0 or (abs(v[0]) < 1e-9 and v[1] < 0): v = [-x for x in v]
    return tuple(round(x, 7) for x in v)
I = matrix([[1, 0], [0, 1]])
seen = {key(I): (I, e)}; frontier = [(I, e)]
best_all = best_oct = None
for L in range(1, 19):
    nf = []
    for M, s in frontier:
        for G, g in gens:
            N = M*G; t = mul(s, g); k = key(N)
            if k in seen: continue
            seen[k] = (N, t); nf.append((N, t))
            tr = abs(N[0,0] + N[1,1])
            if tr > 2 + mpf(10)**-12:
                ell = 2*acosh(tr/2)
                if best_all is None or ell < best_all: best_all = ell
                if t == e and (best_oct is None or ell < best_oct): best_oct = ell
    frontier = nf
    print(L, len(seen), "Delta(2,3,8) min", mp.nstr(best_all, 12) if best_all else None,
          "Gamma_oct min", mp.nstr(best_oct, 12) if best_oct else None, flush=True)
lmin = acosh(1 + mp.sqrt(2))
print("l_min =", mp.nstr(lmin, 12), " 2*l_min =", mp.nstr(2*lmin, 12))
