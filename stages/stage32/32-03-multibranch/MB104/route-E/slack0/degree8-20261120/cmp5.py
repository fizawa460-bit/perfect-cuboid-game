"""Compare the |Omega|<=4 hits of search4 (res4_*.pkl, on all_n.pkl from to_search4.py) and search5 (res5 .pkl, same
covers): a hit is keyed by (query index, the map q∘M evaluated at 3 fixed points, rounded), so that the same pair
(f, q∘M) found through different table covers / self-part relabellings compares equal.
usage: python3 cmp5.py n dir res4_a,res4_b,... res5.pkl"""
import sys, os, pickle, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../numeric-upto5-20261118'))
import mpmath as mp; mp.mp.dps = 60
from common import AUT
n = int(sys.argv[1]); D = sys.argv[2]
A = pickle.load(open(f'{D}/all_{n}.pkl', 'rb')); reps = A['reps']; src = A['src']
TP = np.array([[0.3 + 0.1j, 1], [-0.7 + 0.45j, 1], [0.15 - 1.3j, 1]])
def val(p, q, M):
    out = []
    for t in TP:
        w = M @ t; P = sum(p[m] * w[0] ** m * w[1] ** (n - m) for m in range(n + 1)); Q = sum(q[m] * w[0] ** m * w[1] ** (n - m) for m in range(n + 1))
        z = P / Q if abs(Q) > abs(P) else None; out.append(('a', round(z.real, 5), round(z.imag, 5)) if z is not None else ('b', round((Q / P).real, 5), round((Q / P).imag, 5)))
    return tuple(out)
def cov(r, ui):
    p, q = reps[r][0], reps[r][1]; Mu = AUT[ui][0]; return Mu[0, 0] * p + Mu[0, 1] * q, Mu[1, 0] * p + Mu[1, 1] * q
K4 = {}
for fn in sys.argv[3].split(','):
    for fi, qi, M, om, j, h in pickle.load(open(fn, 'rb'))['hits']:
        r, ui = src[qi]; K4[(fi,) + val(*cov(r, ui), M)] = om
R5 = pickle.load(open(sys.argv[4], 'rb')); K5 = {}
for fi, kind, r, ui, M, om in R5['hits_q']: K5[(fi,) + val(*cov(r, ui), M)] = om
print('search4 distinct hits', len(K4), ' search5 distinct hits', len(K5), ' common', len(set(K4) & set(K5)))
o4 = set(K4) - set(K5); o5 = set(K5) - set(K4)
print('only search4', len(o4), ' only search5', len(o5))
for k in list(o4)[:5]: print('  4 only', k[0], K4[k])
for k in list(o5)[:5]: print('  5 only', k[0], K5[k])
fs = set(k[0] for k in K4); print('queries with hits: search4', len(fs), 'search5', len(set(k[0] for k in K5)))
