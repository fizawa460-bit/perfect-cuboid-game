"""40-digit check of a cov_n_*.pkl list: Gauss-Newton refinement, residual, point separation, 40-digit dedupe."""
import os, sys, pickle, numpy as np
here = os.path.dirname(os.path.abspath(__file__)); fn = sys.argv[1]
sys.path.insert(0, here); sys.path.insert(0, os.path.join(here, '../numeric-upto5-20261118'))
sys.argv = [sys.argv[0], '0', '0', '1']
import mono, hp, allcovers
from covers import invariant
d = pickle.load(open(fn, 'rb')); n = d['n']; prof = d['prof']
_strict = allcovers.analyse
allcovers.analyse = lambda *a, **k: _strict(*a, **k) or mono.analyse_loose(*a, **k)
rows = []
for idx, (x, aut) in enumerate(d['covers']):
    p, q = x[:n + 1], x[n + 1:]
    W = np.polysub(np.polymul(np.polyder(p[::-1]), q[::-1]), np.polymul(p[::-1], np.polyder(q[::-1])))
    W = np.trim_zeros(np.where(np.abs(W) < 1e-10 * np.abs(W).max(), 0, W), 'f'); cr = np.roots(W)
    crit = []; ysl = []
    for c in cr:
        v = (np.polyval(p[::-1], c), np.polyval(q[::-1], c))
        k = min(range(6), key=lambda y: abs(v[0] * mono.BP[y][1] - v[1] * mono.BP[y][0]) / (abs(v[0]) + abs(v[1])))
        crit.append(c); ysl.append(k)
    an = allcovers.analyse(p, q, n, prof, crit, ysl)
    if an is None:
        try: an = allcovers.rough(p, q, n, prof, crit, ysl)
        except AssertionError: rows.append((idx, 2.0, 0.0, None)); continue
    try:
        an2, res, co, hpo = hp.refine(p, q, an, n, iters=15)
    except Exception as e:
        rows.append((idx, 1.0, 0.0, None)); continue
    pts = [complex(z) for y in range(6) for t in (0, 1) for z in an2[y][t] if z is not None]
    pts = np.array(pts); dd = np.abs(pts[:, None] - pts[None]) / (1 + np.abs(pts[:, None])) / (1 + np.abs(pts[None]))
    np.fill_diagonal(dd, 9)
    rows.append((idx, float(res), float(dd.min()), invariant(an2)))
res = np.array([r[1] for r in rows]); sep = np.array([r[2] for r in rows])
good = res < 1e-25
print(f'{fn}: {len(rows)} covers; 40-digit residual < 1e-25: {good.sum()}; min separation of good ones {sep[good].min():.2e}')
print('  residuals of bad ones:', sorted(res[~good])[:10], ' their separations:', sorted(sep[~good])[:10])
INV = np.array([r[3] for r in rows if r[3] is not None and r[1] < 1e-25])
D = np.abs(INV[:, None] - INV[None]).max(2); np.fill_diagonal(D, 9)
print(f'  smallest invariant distance among good ones: {D.min():.2e}; pairs closer than 1e-6: {(D < 1e-6).sum() // 2}')
pickle.dump(rows, open(fn.replace('.pkl', '_hp.pkl'), 'wb'))
