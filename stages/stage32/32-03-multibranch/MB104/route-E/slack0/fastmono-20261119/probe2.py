import sys, os, pickle, itertools, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../speedup-20261118'))
import mono, monodromy as md, braid
from mono import System
from braid import comp
d = pickle.load(open(sys.argv[1], 'rb')); n = 7; prof = (2,) * 6
S = System(n, prof, d['fixed'], d['L']); U = d['sols'][:40]
p, q, _ = S.unpack(U); T0 = md.tuples(p, q)
def words(L):
    out = [()]
    for l in range(1, L + 1):
        for w in itertools.product(range(6), repeat=l):
            if all(w[i] != w[i + 1] for i in range(l - 1)): out.append(w)
    return out
WD = words(2)
def ev(t, w):
    g = tuple(range(n))
    for i in w: g = comp(g, t[i])
    return g
def conj(t, w, x):
    e = ev(t, w); ei = [0] * n
    for i in range(n): ei[e[i]] = i
    return comp(e, comp(x, tuple(ei)))
for a, b in ((2, 4), (3, 5)):
    for side in (1, -1):
        U1, ok = braid.run(S, U, a, b, side)
        p, q, _ = S.unpack(U1[ok]); T1 = [md.canon(t)[0] for t in md.tuples(p, q)]; T0k = [t for t, o in zip(T0, ok) if o]
        hits = []
        for w1, w2, w3 in itertools.product(WD, WD, WD):
            good = True
            for t0, c1 in zip(T0k, T1):
                t = list(t0); ga, gb, g0 = t[a], t[b], t[0]
                t[a] = conj(t0, w1, gb); t[b] = conj(t0, w2, ga); t[0] = conj(t0, w3, g0)
                # recompute g_inf from product relation is implicit: keep as is
                if md.canon(tuple(t))[0] != c1: good = False; break
            if good: hits.append((w1, w2, w3))
        print(a, b, side, len(T1), 'hits', hits[:6], len(hits), flush=True)
