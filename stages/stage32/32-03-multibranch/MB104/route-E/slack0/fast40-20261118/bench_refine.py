"""Compare hp.refine (mpmath) and hp_fast.refine (flint) on the covers of a cov_n_*.pkl (speedup mono.py output).
usage: python3 bench_refine.py cov_7_111333.pkl [max covers] [skip_old]"""
import os, sys, time, pickle, numpy as np, mpmath as mp
here = os.path.dirname(os.path.abspath(__file__))
fn = sys.argv[1]; NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 10**9; SKIP = len(sys.argv) > 3
sys.path.insert(0, here); sys.path.insert(0, os.path.join(here, '../speedup-20261118')); sys.path.insert(0, os.path.join(here, '../numeric-upto5-20261118'))
_a = sys.argv; sys.argv = [_a[0], '0', '0', '1']
import mono, hp, allcovers, hp_fast
sys.argv = _a
_strict = allcovers.analyse
allcovers.analyse = lambda *a, **k: _strict(*a, **k) or mono.analyse_loose(*a, **k)
d = pickle.load(open(fn, 'rb')); n = d['n']; prof = d['prof']
def get_an(x):
    p, q = x[:n + 1], x[n + 1:]
    W = np.polysub(np.polymul(np.polyder(p[::-1]), q[::-1]), np.polymul(p[::-1], np.polyder(q[::-1])))
    W = np.trim_zeros(np.where(np.abs(W) < 1e-10 * np.abs(W).max(), 0, W), 'f'); cr = np.roots(W)
    crit = []; ysl = []
    for c in cr:
        v = (np.polyval(p[::-1], c), np.polyval(q[::-1], c))
        k = min(range(6), key=lambda y: abs(v[0] * mono.BP[y][1] - v[1] * mono.BP[y][0]) / (abs(v[0]) + abs(v[1])))
        crit.append(c); ysl.append(k)
    an = allcovers.analyse(p, q, n, prof, crit, ysl)
    if an is None: an = allcovers.rough(p, q, n, prof, crit, ysl)
    return p, q, an
rows = []; tO = tF = 0.0
for idx, (x, aut) in enumerate(d['covers'][:NMAX]):
    try: p, q, an = get_an(x)
    except AssertionError: continue
    t = time.time(); F = hp_fast.refine_full(p, q, an, n, iters=12); tF += time.time() - t
    _, resF, coF, hpF, critF, _, nit = F
    if SKIP: rows.append((idx, resF, None, nit)); continue
    mp.mp.dps = 40
    t = time.time()
    try: _, resO, coO, hpO = hp.refine(p, q, an, n, iters=12)
    except Exception as e: resO = None
    tO += time.time() - t
    if resO is None: rows.append((idx, resF, None, nit)); continue
    # compare odd points at 40 digits (old code: co as complex, so compare hp odd points)
    dmax = 0
    for y in range(6):
        for a, b in zip(hpF.get(y, []), hpO.get(y, [])):
            if (a is None) != (b is None): dmax = 1.0
            elif a is not None: dmax = max(dmax, float(abs(a - b) / (1 + abs(b))))
    rows.append((idx, resF, resO, nit, dmax))
k = len(rows)
print(f'{fn}: {k} covers; fast {tF:.2f}s ({tF / k * 1e3:.1f} ms/cover)' + ('' if SKIP else f'; mpmath {tO:.2f}s ({tO / k * 1e3:.1f} ms/cover); speed-up x{tO / max(tF,1e-9):.0f}'))
rF = np.array([r[1] for r in rows]); print('  fast: residual max', f'{rF.max():.1e}', ' newton steps', np.bincount([r[3] for r in rows]).tolist())
if not SKIP:
    good = [r for r in rows if r[2] is not None]
    print('  mpmath: residual max', f'{max(r[2] for r in good):.1e}', ' max relative difference of the 40-digit odd points', f'{max(r[4] for r in good):.1e}')
    print('  covers with residual < 1e-28: fast', int((rF < 1e-28).sum()), ' mpmath', sum(1 for r in good if r[2] < 1e-28))
