"""Recheck at more digits the hits that search7's birationality stage left 'BIRATIONAL' or 'unclear' after 40 digits.

usage: python3 recheck_bir.py res.pkl LOCDIR [DPS=80] [ITERS=60]
res.pkl is search7's OUT.pkl (non-QMODE), LOCDIR the L7 directory it ran on (A side; for kind 'U' the pair is
(f, U∘f∘M) on the same side, for kind 'T' the table side must be the same LOCDIR, as in SELFONLY / SAME runs).
Same procedure as bircheck40.check (refine f and r, rebuild M from three matched odd points, compare all labelled
points, fibre test), with DPS digits, ITERS Newton steps, composite threshold 10^-(DPS/2), birational > 1e-12."""
import sys, os, glob, pickle, itertools, numpy as np, mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, f'{HERE}/../degree8-20261120', f'{HERE}/../fast40-20261118', f'{HERE}/../speedup-20261118', f'{HERE}/../numeric-upto5-20261118']
import hp_fast, bircheck40
from common import AUT, BLAB

res_f, D = sys.argv[1], sys.argv[2]
DPS = int(os.environ.get('DPS', '80')); ITERS = int(os.environ.get('ITERS', '60')); CT = 10.0 ** (-DPS / 2)
files = sorted(glob.glob(f'{D}/L7_9_*[0-9].pkl')); n = 9
meta = []; off = 0
for fn in files:
    d = pickle.load(open(fn, 'rb')); meta.append((fn[:-4], off, d['N'], d['oddy'], d['crity'])); off += d['N']
offs = np.array([m[1] for m in meta])
_arr = {}
def arr(pre, s):
    if (pre, s) not in _arr: _arr[(pre, s)] = np.load(f'{pre}_{s}.npy', mmap_mode='r')
    return _arr[(pre, s)]
def rep_tuple(r):
    pi = int(np.searchsorted(offs, r, 'right') - 1); pre, o, N, oy, cy = meta[pi]; k = r - o
    pq = np.asarray(arr(pre, 'pq')[k]); Z = np.asarray(arr(pre, 'z')[k]); INF = np.asarray(arr(pre, 'inf')[k])
    cr = np.asarray(arr(pre, 'crit')[k]); an = {}
    for y in range(6):
        an[y] = ([None if INF[j] else complex(Z[j]) for j in range(len(oy)) if oy[j] == y],
                 [complex(c) for c, yy in zip(cr, cy) if yy == y])
    return pq[:n + 1], pq[n + 1:], an
_cache = {}
def ref(r):
    if r not in _cache:
        p, q, an = rep_tuple(r)
        out, res, co, hpo, crit, ys, nit = hp_fast.refine_full(p, q, an, n, iters=ITERS, dps=DPS, miniters=4)
        _cache[r] = (co, bircheck40._pts(co, crit, ys, hpo), res, nit)
    return _cache[r]
def check(fi, r, ui, M):
    with mp.workdps(DPS):
        cf, Pf, resf, nf = ref(fi); cr, Pr, resr, nr = ref(r)
        perm = AUT[ui][1]; Pq = [(perm[y], t, z) for y, t, z in Pr]; _cd, _app = bircheck40._cd, bircheck40._app
        Md = [[mp.mpc(complex(M[i, j])) for j in range(2)] for i in range(2)]
        match = []
        for y, t, z in Pf:
            w = _app(Md, z); cands = [(_cd(w, zz), k) for k, (yy, tt, zz) in enumerate(Pq) if BLAB[yy] == BLAB[y] and tt == t]
            match.append(min(cands, key=lambda a: a[0]) if cands else (mp.mpf(1), -1))
        oddg = [i for i, (d_, k) in enumerate(match) if d_ < 1e-4 and Pf[i][1] == 0]
        if len(oddg) < 3: return dict(verdict='unclear', why='fewer than 3 matched odd points', res=(resf, resr))
        best = max(((min(_cd(Pf[a_][2], Pf[b_][2]), _cd(Pf[a_][2], Pf[c_][2]), _cd(Pf[b_][2], Pf[c_][2])), (a_, b_, c_))
                    for a_, b_, c_ in itertools.combinations(oddg[:10], 3)), key=lambda x: x[0])
        tri = best[1]; M40 = bircheck40._mob3([Pf[i][2] for i in tri], [Pq[match[i][1]][2] for i in tri])
        dpts = sorted(float(min([_cd(_app(M40, z), zz) for yy, tt, zz in Pq if tt == t and BLAB[yy] == BLAB[y]] or [1])) for y, t, z in Pf)
        fib = bircheck40.fibre_test(cf, n, cr, n, M40, 3, 3)
        comp = all(f[1] < CT for f in fib); bir = any(f[1] > 1e-12 for f in fib)
        return dict(verdict='composite' if comp else ('BIRATIONAL' if bir else 'unclear'), fibres=fib,
                    pts_matched=sum(d_ < CT for d_ in dpts), npts=len(Pf), res=(resf, resr), nit=(nf, nr))

R = pickle.load(open(res_f, 'rb'))
Mof = {(h[0], h[1], h[2]): h for h in R['hits_q']}      # (fi, kind, r, ui, M, om)
out = []; cnt = {}
for x in R['bir']:
    fi, kind, qx = x[0], x[1], x[2]
    h = next(h for h in R['hits_q'] if h[0] == fi and h[1] == kind and (h[3] == qx if kind == 'U' else True))
    _, _, r, ui, M, om = h
    v = check(int(fi), int(r), int(ui), np.asarray(M))
    cnt[v['verdict']] = cnt.get(v['verdict'], 0) + 1; out.append((x, v))
    print(f'f={fi} {kind}{qx} r={r} U={ui} |Omega|={om}: {v["verdict"]}  fibres(2nd) {[f"{f[1]:.1e}" for f in v.get("fibres", [])]}'
          f'  points {v.get("pts_matched")}/{v.get("npts")}  res {[f"{float(e):.1e}" for e in v["res"]]}', flush=True)
print(f'{DPS} digits: {cnt} of {len(R["bir"])}', flush=True)
pickle.dump(out, open(res_f.replace('.pkl', f'_re{DPS}.pkl'), 'wb'))
