"""E07: modular Hecke correspondences on X(8) (cusped uniformization Gamma(8) < PSL2(Z)).
For a = diag(N,1) and a twist sigma in PSL2(Z/8): Z_sigma = {(Gamma(8) z, sigma Gamma(8) a z)}.  The group of lifts of
the diagonal G-elements preserving Z_sigma is
   L = { l in Gamma_0(N) : l mod 8 in G (projectively), phi(l) mod 8 = sigma^-1 (l mod 8) sigma (projectively) },
   phi([[al,be],[ga,de]]) = [[al, N be],[ga/N, de]] = a l a^-1.
L contains Gamma(8N), so everything is computed in SL2(Z/8N), exactly.  S(sigma) = image of L in G, k = |S|;
the underlying genus of H/L (cusps filled) is computed by Riemann-Hurwitz from the cycles of S=[[0,-1],[1,0]],
U=S*T (order 3) and T=[[1,1],[0,1]] on the cosets of L.  usage: python modhecke.py N"""
import sys, itertools
import numpy as np
N = int(sys.argv[1]); m = 8 * N
def mul(A, B):
    a, b, c, d = A; e, f, g, h = B
    return ((a*e + b*g) % m, (a*f + b*h) % m, (c*e + d*g) % m, (c*f + d*h) % m)
Sg, Tg = (0, m-1, 1, 0), (1, 1, 0, 1)
# all of SL2(Z/m) by BFS
I = (1, 0, 0, 1); seen = {I}; fr = [I]
while fr:
    nf = []
    for x in fr:
        for g in (Sg, Tg):
            y = mul(g, x)
            if y not in seen: seen.add(y); nf.append(y)
    fr = nf
SL = list(seen)
def red8(A): return tuple(x % 8 for x in A)
def proj8(A):   # canonical rep of +-A in SL2(Z/8)
    B = tuple((-x) % 8 for x in A); return min(A, B)
def mul8(A, B):
    a, b, c, d = A; e, f, g, h = B
    return ((a*e + b*g) % 8, (a*f + b*h) % 8, (c*e + d*g) % 8, (c*f + d*h) % 8)
def inv8(A): a, b, c, d = A; return (d % 8, (-b) % 8, (-c) % 8, a % 8)
# PSL2(Z/8) and G = {+-(I mod 4)}
SL8 = {red8(x) for x in SL} if N == 1 else None
if SL8 is None:
    s8 = {(1, 0, 0, 1)}; fr = [(1, 0, 0, 1)]
    while fr:
        nf = []
        for x in fr:
            for g in ((0, 7, 1, 0), (1, 1, 0, 1)):
                y = mul8(g, x)
                if y not in s8: s8.add(y); nf.append(y)
        fr = nf
    SL8 = s8
PSL8 = sorted({proj8(x) for x in SL8})
G = sorted({proj8(x) for x in SL8 if (x[0] % 4, x[1] % 4, x[2] % 4, x[3] % 4) in ((1, 0, 0, 1), (3, 0, 0, 3))})
Gset = set(G)
if len(PSL8) != 192 or len(G) != 8: raise SystemExit("FAIL: PSL2(Z/8) or G")
# elements of Gamma_0(N) mod m with l mod 8 in G: precompute (proj l8, proj phi(l)8)
cand = []
for x in SL:
    al, be, ga, de = x
    if ga % N: continue
    l8 = proj8(red8(x))
    if l8 not in Gset: continue
    ph = proj8(((al) % 8, (N*be) % 8, (ga // N) % 8 if True else 0, de % 8))
    cand.append((x, l8, ph))
# encode SL elements as integers for fast coset keys
def enc(A): return ((A[0]*m + A[1])*m + A[2])*m + A[3]
def genus_and_k(Lset):
    Larr = np.array(sorted(Lset), dtype=np.int64)
    La, Lb, Lc, Ld = Larr[:, 0], Larr[:, 1], Larr[:, 2], Larr[:, 3]
    def key(h):
        a, b, c, d = h
        A = (a*La + b*Lc) % m; B = (a*Lb + b*Ld) % m; C = (c*La + d*Lc) % m; D = (c*Lb + d*Ld) % m
        return int((((A*m + B)*m + C)*m + D).min())
    U = mul(Sg, Tg)
    start = I; keys = {key(start): 0}; reps = [start]; perm = {"S": {}, "U": {}, "T": {}}; i = 0
    while i < len(reps):
        r = reps[i]
        for nm, g in (("S", Sg), ("U", U), ("T", Tg)):
            h = mul(g, r); kk = key(h)
            if kk not in keys: keys[kk] = len(reps); reps.append(h)
            perm[nm][i] = keys[kk]
        i += 1
    mu = len(reps)
    def ncyc(p):
        seen = [False]*mu; c = 0
        for t in range(mu):
            if not seen[t]:
                c += 1; u = t
                while not seen[u]: seen[u] = True; u = p[u]
        return c
    tg = -2*mu + sum(mu - ncyc(perm[nm]) for nm in ("S", "U", "T"))
    if tg % 2: raise SystemExit("FAIL: odd Euler characteristic")
    return tg // 2 + 1, mu
res = []
cache = {}
for sigma in PSL8:
    sinv = proj8(inv8(sigma))
    Lset = set(); Simg = set()
    for x, l8, ph in cand:
        target = proj8(mul8(mul8(sinv, l8), sigma))
        if ph == target: Lset.add(x); Simg.add(l8)
    Lkey = frozenset(Lset)
    if Lkey not in cache: cache[Lkey] = genus_and_k(Lset)
    g, mu = cache[Lkey]
    res.append((sigma, len(Simg), g, mu))
from collections import Counter
n_leg = None
print(f"N={N}  m={m}  |SL2(Z/m)|={len(SL)}  distinct L: {len(cache)}")
print("  (k, genus) distribution:", sorted(Counter((k, g) for _, k, g, _ in res).items()))
low = [r for r in res if r[2] <= 1]
print("  twists with genus <= 1:", len(low), sorted(Counter((k, g) for _, k, g, _ in low).items()))
print("  min genus:", min(r[2] for r in res))
import json
import tempfile, os
json.dump({"N": N, "res": [[list(s), k, g, mu] for s, k, g, mu in res]}, open(sys.argv[2] if len(sys.argv) > 2 else os.path.join(tempfile.gettempdir(), f"modhecke_N{N}.json"), "w"))
