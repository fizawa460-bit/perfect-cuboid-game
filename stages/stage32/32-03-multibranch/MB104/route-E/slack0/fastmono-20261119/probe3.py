"""learn the action of the pure braids braid.path_loop(a, b) on tuples: g_a -> e1 g_a e1^-1, g_b -> e2 g_b e2^-1
(others unchanged), words up to length 3, from covers of a finished 2,2,2,2,2,2 checkpoint"""
import sys, os, pickle, itertools, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '../speedup-20261118'))
import mono, monodromy as md, braid, fasttuples as ft, autact
from mono import System
d = pickle.load(open(sys.argv[1], 'rb')); n = 7; prof = (2,) * 6
S = System(n, prof, d['fixed'], d['L']); rng = np.random.default_rng(1)
ii = rng.choice(len(d['sols']), 60, replace=False); U = d['sols'][ii]; T0 = [d['TT'][i] for i in ii]
def words(L):
    out = [()]
    for l in range(1, L + 1):
        for w in itertools.product(range(6), repeat=l):
            if all(w[i] != w[i + 1] for i in range(l - 1)): out.append(w)
    return out
WD = words(3); found = {}
for a, b in ((0, 2), (0, 3), (0, 4), (0, 5), (3, 5)):
    for sense in (1, -1):
        U1, ok = braid.run_path(S, U, braid.path_loop(a, b, sense=sense))
        pairs = []
        for u, o, t in zip(U1, ok, T0):
            if not o: continue
            try: t1 = ft.tuples(*S.unpack(u[None])[:2], 12)[0]
            except Exception: continue
            if md.check(t1, prof): pairs.append((t, md.canon(t1)[0]))
        hit = None
        for w1 in WD:
            # filter on the first 3 pairs quickly
            for w2 in WD:
                okk = True
                for t, c1 in pairs[:40]:
                    s = list(t); s[a] = autact.conj(t, w1, t[a]); s[b] = autact.conj(t, w2, t[b])
                    if md.canon(tuple(s))[0] != c1: okk = False; break
                if okk: hit = (w1, w2); break
            if hit: break
        print((a, b, sense), len(pairs), 'hit', hit, flush=True)
        if hit: found[(a, b, sense)] = hit
pickle.dump(found, open('loop_rules.pkl', 'wb'))
