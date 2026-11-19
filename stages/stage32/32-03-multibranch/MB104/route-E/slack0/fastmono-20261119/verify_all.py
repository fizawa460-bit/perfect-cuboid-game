"""Independent check of a finished run: number every cover numerically (fasttuples, chunk k of K) and compare
with the class the run assigned.  Prints counts of agree / disagree / numbering failed."""
import sys, os, pickle, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '../speedup-20261118'))
import mono, monodromy as md, fasttuples as ft
from mono import System
d = pickle.load(open(sys.argv[1], 'rb')); k, K = int(sys.argv[2]), int(sys.argv[3]); m = int(sys.argv[4]) if len(sys.argv) > 4 else 12
n = len(d['sols'][0]) and 7; prof = tuple(int(x) for x in sys.argv[5].split(',')) if len(sys.argv) > 5 else (2,) * 6
S = System(n, prof, d['fixed'], d['L']); idx = np.arange(len(d['sols']))[k::K]
agree = disagree = failed = 0; bad = []; fl = []
for s0 in range(0, len(idx), 500):
    ii = idx[s0:s0 + 500]; p, q, _ = S.unpack(d['sols'][ii])
    try: T = ft.tuples(p, q, m)
    except (RuntimeError, AssertionError):
        T = []
        for j in range(len(ii)):
            try: T.append(ft.tuples(p[j:j + 1], q[j:j + 1], m)[0])
            except (RuntimeError, AssertionError): T.append(None)
    for i, t in zip(ii, T):
        if t is None: failed += 1; fl.append(int(i))
        elif md.check(t, prof) and md.canon(t)[0] == md.canon((d.get('tuples') or d['TT'])[i])[0]: agree += 1
        else: disagree += 1; bad.append(int(i))
print(f'chunk {k}/{K}: agree {agree} disagree {disagree} numbering_failed {failed}; bad {bad[:20]} failed {fl[:50]}', flush=True)
pickle.dump({'bad': bad, 'failed': fl}, open(f'verify_{k}_{K}.pkl', 'wb'))
