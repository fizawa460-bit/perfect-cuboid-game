"""Exact de-duplication of fast40/build_all.py output for a mono_dir run.
build_all regenerates the 24 Aut(B) images of every representative and merges them by Moebius invariants (tolerance
1e-7), which can fail for covers with almost-coincident points.  Here every 'all' entry gets its exact class from the
representative's monodromy tuple and the learned symmetry rule, and one entry per class is kept.
usage: python3 exact_dedupe.py all_7.pkl full_7_222222.pkl aut_rules_7_222222.pkl  -> all_7_exact.pkl"""
import sys, os, pickle, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '../speedup-20261118'))
import mono, monodromy as md, autact
A = pickle.load(open(sys.argv[1], 'rb')); F = pickle.load(open(sys.argv[2], 'rb')); R = pickle.load(open(sys.argv[3], 'rb'))
prof = tuple(R['prof']); syms = autact.sym_list(prof)
from common import AUT
# rule index for each AUT element (conj = 0)
k_of = {}
for ui, (M, perm) in enumerate(AUT):
    ks = [k for k, (cj, M2, pi) in enumerate(syms) if cj == 0 and np.allclose(M2, M)]
    k_of[ui] = ks[0] if ks else None
keep = F['in_cov_file']; T = F['tuples']
# build_all re-orders its representatives (sorted by invariant): match them back to the run's covers by coefficients
def nv(x):
    x = np.asarray(x, complex); x = x / x[np.argmax(np.abs(x))]; return np.r_[x.real, x.imag]
n = (len(F['sols'][0]) and None) or (len(A['reps'][0][0]) - 1)
base = np.array([nv(F['sols'][i][:2 * n + 2]) for i in keep])
rq = np.array([nv(np.r_[np.array(p, complex), np.array(q, complex)]) for p, q, _, _ in A['reps']])
proj = np.random.default_rng(0).normal(size=base.shape[1]); kb = base @ proj; o = np.argsort(kb); ks = kb[o]
dist = np.empty(len(rq)); pos = np.empty(len(rq), int)
for r, v in enumerate(rq):
    c = np.searchsorted(ks, v @ proj); lo, hi = max(0, c - 50), min(len(ks), c + 50)
    dd = np.abs(base[o[lo:hi]] - v).max(1); j = dd.argmin(); dist[r] = dd[j]; pos[r] = o[lo + j]
print(f'rep matching: max distance {dist.max():.1e}, one-to-one {len(set(pos)) == len(pos)}')
rep_full = [keep[j] for j in pos]
cls = []
for ri, ui in A['src']:
    t = T[rep_full[ri]]; cls.append(md.canon(autact.apply(t, R['rules'][k_of[ui]]))[0])
allcls = set(md.canon(t)[0] for t in T)
first = {}
for j, c in enumerate(cls): first.setdefault(c, j)
extra = len(cls) - len(first)
print(f"build_all entries {len(cls)}, distinct exact classes {len(first)}, duplicates {extra}, "
      f"classes equal to the run's list: {set(first) == allcls}")
sel = sorted(first.values())
pickle.dump({'reps': A['reps'], 'all': [A['all'][j] for j in sel], 'src': [A['src'][j] for j in sel],
             'class': [cls[j] for j in sel]}, open(sys.argv[1].replace('.pkl', '_exact.pkl'), 'wb'))
