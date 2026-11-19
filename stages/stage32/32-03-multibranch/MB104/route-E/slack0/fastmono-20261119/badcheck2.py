"""classify verify_all 'disagree' entries: invalid tuple (double precision cannot number) vs another valid class"""
import sys, os, pickle, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '../speedup-20261118'))
import mono, monodromy as md, fasttuples as ft
from mono import System, analyse, analyse_loose
from collections import Counter
d = pickle.load(open(sys.argv[1], 'rb')); n = 7; prof = (2,) * 6; S = System(n, prof, d['fixed'], d['L'])
bad = []
for k in range(3): bad += pickle.load(open(f'ver/verify_{k}_3.pkl', 'rb'))['bad']
c = Counter(); dm = []
for i in bad:
    u = d['sols'][i]; p, q, cc = S.unpack(u[None])
    t = ft.tuples(p, q, 12)[0]; cs = cc[0]; dm.append(min(abs(cs[a] - cs[b]) for a in range(12) for b in range(a)))
    an = analyse(p[0], q[0], n, prof, cs, list(S.ys)) or analyse_loose(p[0], q[0], n, prof, cs, list(S.ys))
    c[('valid' if md.check(t, prof) else 'invalid', 'analyse_ok' if an else 'analyse_fail', 'img' if not d['ISREP'][i] else 'rep')] += 1
print(len(bad), dict(c), 'dmin max %.1e median %.1e' % (max(dm), np.median(dm)))
