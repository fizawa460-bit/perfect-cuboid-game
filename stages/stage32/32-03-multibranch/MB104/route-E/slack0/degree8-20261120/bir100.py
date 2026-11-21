"""Recheck at 100 digits of search5's pairs that stay 'BIRATIONAL or unclear' after bircheck40 (as degree7/birhi.py:
bircheck40 with dps 100, 60 refinement iterations, coincidence threshold 1e-25 -> 1e-60, separation 1e-12 unchanged).

usage: python3 bir100.py result.pkl a b dirA [dirB]       (result.pkl = search5 output, its 'bir' list)
Covers that are ill-conditioned in double precision (the 40-digit refinement from the double data stops near
1e-24, just above bircheck40's 1e-25 line) are the expected case."""
import sys, os, glob, pickle, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); SL = os.path.join(HERE, '..'); F = os.path.join(SL, 'fast40-20261118')
for d in ('numeric-upto5-20261118', 'speedup-20261118', 'fast40-20261118'): sys.path.insert(0, os.path.join(SL, d))
_a = sys.argv; sys.argv = [_a[0], '0', '0', '1']
import mpmath as mp; mp.mp.dps = 100
src = open(F + '/bircheck40.py').read().replace('workdps(40)', 'workdps(100)').replace('iters=15)', 'iters=60, dps=100)') \
    .replace('1e-25', '1e-60').replace('extraprec=120', 'extraprec=300')
ns = {'__name__': 'bir100'}; exec(compile(src, 'bir100', 'exec'), ns)
sys.argv = _a
R = pickle.load(open(sys.argv[1], 'rb')); a, b = int(sys.argv[2]), int(sys.argv[3]); DA = sys.argv[4]; DB = sys.argv[5] if len(sys.argv) > 5 else DA


def load(D, n):
    L = {'pq': [], 'odd': [], 'oddy': [], 'crit': [], 'crity': [], 'off': [0]}
    for fn in sorted(glob.glob(f'{D}/L5_{n}_*.pkl')):
        d = pickle.load(open(fn, 'rb')); N = len(d['aut'])
        L['pq'].append(d['pq']); L['odd'].append(d['odd']); L['oddy'].append(np.broadcast_to(d['oddy'], (N, len(d['oddy']))))
        L['crit'].append(d['crit']); L['crity'].append(d['crity']); L['off'].append(L['off'][-1] + N)
    return {'n': n, 'pq': np.concatenate(L['pq']), 'odd': np.concatenate(L['odd']), 'oddy': np.concatenate(L['oddy']),
            'crit': L['crit'], 'crity': L['crity'], 'off': np.array(L['off'])}


def rep_tuple(L, r):          # as search5
    n = L['n']; pi = int(np.searchsorted(L['off'], r, 'right') - 1); k = r - L['off'][pi]
    oy = L['oddy'][r]; cy = L['crity'][pi]; cr = L['crit'][pi][k]; an = {}
    for y in range(6):
        od = [None if abs(L['odd'][r][j][1]) < 1e-300 else complex(L['odd'][r][j][0] / L['odd'][r][j][1]) for j in range(len(oy)) if oy[j] == y]
        an[y] = (od, [complex(c) for c, yy in zip(cr, cy) if yy == y])
    return (L['pq'][r][:n + 1], L['pq'][r][n + 1:], an)


LA = load(DA, a); LB = LA if DB == DA and a == b else load(DB, b)
HQ = {(h[0], h[1]): h for h in R['hits_q']}
todo = R['bir']; out = []
hq = {}
for h in R['hits_q']: hq.setdefault((h[0], h[1]), []).append(h)
for fi, kind, qx, om, j, h, v in todo:
    # the hit's (rep, U, M) from hits_q (same order as hits)
    cand = [x for x, y in zip(R['hits_q'], R['hits']) if y[0] == fi and y[1] == kind and y[2] == qx]
    _, _, r, ui, M, _ = cand[0]
    Lq = LB if kind == 'T' else LA
    res = ns['check'](('A', fi), rep_tuple(LA, fi), ('B' if kind == 'T' else 'A', r), rep_tuple(Lq, r), ui, M)
    out.append((fi, kind, qx, r, ui, res['verdict']))
    print(fi, kind, qx, 'rep', r, 'U', ui, '->', res['verdict'], ['%.1e' % f[1] for f in res.get('fibres', [])],
          'pts', res.get('pts_matched'), '/', res.get('npts'), flush=True)
from collections import Counter
print('verdicts at 100 digits:', dict(Counter(o[5] for o in out)))
pickle.dump(out, open(sys.argv[1].replace('.pkl', '_bir100.pkl'), 'wb'))
