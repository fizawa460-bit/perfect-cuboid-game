"""Full cover list of degree n with 40-digit points, = speedup-20261118/allcovers2.py (allcovers.full with the relaxed
analyse) but with the flint refinement (hp_fast) and one process per input file.
usage (from a data folder holding cov_n_*.pkl):  python3 build_all.py n [procs] [mpmath]
output all_n.pkl = {'reps': [(p,q,an,aut)], 'all': [(p,q,an,aut)], 'src': [(rep index, Aut(B) index) of each 'all' entry]}
an['hp'] holds the 40-digit odd points (mpmath mpc), as in allcovers.  'mpmath' as 3rd argument uses the old hp.refine
(for comparison)."""
import os, sys, glob, time, pickle, numpy as np
here = os.path.dirname(os.path.abspath(__file__))
for d in ('../numeric-upto5-20261118', '../speedup-20261118', '.'): sys.path.insert(0, os.path.join(here, d))
n = int(sys.argv[1]); NP = int(sys.argv[2]) if len(sys.argv) > 2 else 4; OLD = len(sys.argv) > 3 and sys.argv[3] == 'mpmath'
_a = sys.argv; sys.argv = [_a[0], '0', '0', '1']
import mono, allcovers, hp, hp_fast
from covers import BP, AUT, polish
sys.argv = _a
_strict = allcovers.analyse
allcovers.analyse = lambda *a, **k: _strict(*a, **k) or mono.analyse_loose(*a, **k)
REF = hp.refine if OLD else hp_fast.refine
analyse = allcovers.analyse

from covers import _OM
import itertools
_SUBS = {}
def invariants_images(an):
    """covers.invariant of the 24 Aut(B) images {perm[y]: an[y]} at once (identical formula; the j-function part
    does not depend on the labels, so it is computed once; only the label characters are permuted).
    Index 0 is the identity of AUT (checked below)."""
    pts = []; ys = []
    for y in range(6):
        for t in (0, 1):
            for z in an[y][t]:
                w = np.array((1, 0) if z is None else (z, 1), complex); pts.append(w / np.linalg.norm(w)); ys.append((y, t))
    pts = np.array(pts); N = len(pts)
    if N not in _SUBS: _SUBS[N] = np.array(list(itertools.combinations(range(N), 4)))
    S = _SUBS[N]; P = pts[S]
    def wd(u, v): return u[..., 0] * v[..., 1] - u[..., 1] * v[..., 0]
    num = wd(P[:, 0], P[:, 2]) * wd(P[:, 1], P[:, 3]); den = wd(P[:, 0], P[:, 3]) * wd(P[:, 1], P[:, 2])
    Aq = (num ** 2 - num * den + den ** 2) ** 3; Bq = (num * den * (num - den)) ** 2
    jj = Aq / Bq; h = jj / np.sqrt(1 + np.abs(jj) ** 2)
    base = np.array([y + 6 * t for y, t in ys]); L = np.sort(base[S], 1)
    code = ((L[:, 0] * 12 + L[:, 1]) * 12 + L[:, 2]) * 12 + L[:, 3]
    uc, ix = np.unique(code, return_inverse=True)
    H = np.bincount(ix, h.real, len(uc)) + 1j * np.bincount(ix, h.imag, len(uc))   # sum of h per label class
    CL = np.stack([uc // 1728, uc // 144 % 12, uc // 12 % 12, uc % 12], 1)            # the 4 labels of each class
    out = []
    for M, perm in AUT:
        pl = np.array([perm[l % 6] + 6 * (l // 6) for l in range(12)])
        out.append(np.array([(np.prod(np.concatenate([om, om ** 2])[pl[CL]], 1) * H).sum() for om in _OM]))
    return out
assert all(tuple(AUT[0][1]) == tuple(range(6)) for _ in [0])
def dedupe_inv(lst, inv):
    """allcovers.dedupe with precomputed invariants (same sort, same tolerance 1e-7, keeps the same entries)."""
    inv = np.array(inv); o = np.argsort(inv[:, 0].real)
    used = np.zeros(len(lst), bool); out = []; r0 = inv[o, 0].real
    for a_ in range(len(o)):
        i = o[a_]
        if used[i]: continue
        used[i] = True; out.append(lst[i])
        b_ = a_ + 1
        while b_ < len(o) and r0[b_] - r0[a_] < 1e-7 * (1 + abs(r0[a_])):
            j = o[b_]
            if not used[j] and np.abs(inv[j] - inv[i]).max() < 1e-7 * (1 + np.abs(inv[i]).max()): used[j] = True
            b_ += 1
    return out

def one_file(fn):
    """allcovers.load_reps for one file (same steps; only the refinement routine differs)."""
    import mpmath as mp; mp.mp.dps = 40
    d = pickle.load(open(fn, 'rb')); prof = d['prof']; out = []; worst = 0.0; t0 = time.time()
    # speedup mono.py also writes rej_n_prof.pkl with the full solutions (P, Q and the critical points in ys order):
    # use those critical points (the Wronskian route can mis-assign critical points of nearly colliding covers)
    rj = fn.replace('cov_', 'rej_'); SOL = None
    if os.path.exists(rj):
        R = pickle.load(open(rj, 'rb'))
        if len(R['sols']) == len(d['covers']): SOL = R
    for ci, (x, aut) in enumerate(d['covers']):
        p, q = x[:n + 1], x[n + 1:]
        if SOL is not None:
            u = SOL['sols'][ci]; crit = list(SOL['fixed'][:3]) + list(u[2 * n + 2:]); ysl = list(SOL['ys'])
            assert np.allclose(u[:2 * n + 2], x)
            an = analyse(p, q, n, prof, crit, ysl)
            if an is None: raise AssertionError((fn, ci, 'analyse failed on the solver critical points'))
            an2, res, co, hpo = REF(p, q, an, n, iters=12); an2['hp'] = hpo
            assert res < 1e-25, (fn, res)
            worst = max(worst, res); co = np.array(co); out.append((co[:n + 1], co[n + 1:], an2, aut)); continue
        W = np.polysub(np.polymul(np.polyder(p[::-1]), q[::-1]), np.polymul(p[::-1], np.polyder(q[::-1])))
        W = np.trim_zeros(np.where(np.abs(W) < 1e-10 * np.abs(W).max(), 0, W), 'f'); cr = np.roots(W)
        assert len(cr) == 2 * n - 2
        crit = []; ysl = []
        for c in cr:
            v = (np.polyval(p[::-1], c), np.polyval(q[::-1], c))
            k = min(range(6), key=lambda y: abs(v[0] * BP[y][1] - v[1] * BP[y][0]) / (abs(v[0]) + abs(v[1])))
            crit.append(c); ysl.append(k)
        crit = [complex(polish(W, c)) for c in crit]
        an = analyse(p, q, n, prof, crit, ysl)
        if an is None:
            an = allcovers.rough(p, q, n, prof, crit, ysl)
            an2, res, co, hpo = REF(p, q, an, n, iters=15)
            co = np.array(co)
            an = analyse(co[:n + 1], co[n + 1:], n, prof, [z for y in range(6) for z in an2[y][1]], [y for y in range(6) for z in an2[y][1]])
            assert an is not None, fn
            p, q = co[:n + 1], co[n + 1:]
        an2, res, co, hpo = REF(p, q, an, n, iters=12)
        an2['hp'] = hpo
        assert res < 1e-25, (fn, res)
        worst = max(worst, res)
        for y in range(6):
            for z1, z2 in zip(an[y][0], an2[y][0]):
                assert (z1 is None) == (z2 is None) and (z1 is None or abs(z1 - z2) < 1e-3 * (1 + abs(z1))), (fn, z1, z2)
        co = np.array(co); out.append((co[:n + 1], co[n + 1:], an2, aut))
    return fn, out, worst, time.time() - t0

if __name__ == '__main__':
    from multiprocessing import Pool
    t0 = time.time()
    files = sorted(glob.glob(f'cov_{n}_*.pkl'))
    with Pool(NP) as P: res = P.map(one_file, files, chunksize=1)
    reps = [c for _, out, _, _ in res for c in out]
    print(f'n={n}: {len(files)} files, {len(reps)} covers refined, worst residual {max(r[2] for r in res):.1e}, '
          f'refinement {sum(r[3] for r in res):.1f} core-s ({"mpmath" if OLD else "flint"})', flush=True)
    t1 = time.time()
    reps = dedupe_inv(reps, [invariants_images(c[2])[0] for c in reps]) if n > 2 else reps
    allc = []; inv = []
    for ri, (p, q, an, aut) in enumerate(reps):
        IV = invariants_images(an)
        for ui, (M, perm) in enumerate(AUT):
            an2 = {perm[y]: an[y] for y in range(6)}; an2['hp'] = {perm[y]: v for y, v in an['hp'].items()}
            allc.append((M[0, 0] * p + M[0, 1] * q, M[1, 0] * p + M[1, 1] * q, an2, aut, ri, ui)); inv.append(IV[ui])
    allc = dedupe_inv(allc, inv)
    print(f'dedupe {time.time() - t1:.1f}s', flush=True)
    src = [(c[4], c[5]) for c in allc]; allc = [c[:4] for c in allc]
    print(f'reps {len(reps)}  all {len(allc)}  weighted {sum(1 / c[3] for c in allc):.4f}  total {time.time() - t0:.1f}s', flush=True)
    pickle.dump({'reps': reps, 'all': allc, 'src': src}, open(f'all_{n}.pkl' if not OLD else f'all_{n}_mpmath.pkl', 'wb'))
