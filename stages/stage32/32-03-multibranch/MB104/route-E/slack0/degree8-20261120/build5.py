"""Degree-n cover list for search5 from mono_dir output (one profile per call; research code).

Input (folder D): cov_<n>_<tag>.pkl, rej_<n>_<tag>.pkl, full_<n>_<tag>.pkl, extra_<n>_<tag>.pkl of fastmono/mono_dir.py
(every class of the profile, exact by monodromy tuple).  Steps:
  1. covers in the cov file: refined at DPS digits by hp_fast.refine_full from mono's own critical points
     (= fast40/build_all.one_file); covers of the extra file (fail analyse in double precision): 60-digit refinement
     and odd points by mpmath.polyroots of the fibre polynomials (= degree7-20261119/extras40.entry, n generic).
  2. symmetry images: for every cover i and every s in Stab(prof) of Aut(B) x <conj> (fastmono autact.sym_list), the
     image class is named by the learned rule and looked up; EVERY named image is then confirmed numerically: the
     labelled point set f^-1(B) (odd and double points, 2 + 3n - 2 ... points) of s(cover i) is Moebius-aligned
     with cover j (align_nb.align, tolerance ALTOL).  Unconfirmed images are stored as -1 (never merged).
Output L5_<n>_<tag>.pkl: dict with numpy arrays (no mpmath objects):
  prof, pq (N, 2n+2) double coefficients (P low->high, Q), odd (N, nodd, 2) unit homogeneous odd points (from the
  DPS-digit points), oddy (nodd,) branch index of each odd position, crit (N, 2n-2), crity, aut (N,),
  (file L5hp_<n>_<tag>.npy) hp (N, nodd, 2) bytes: the DPS-digit odd points as decimal strings (b'inf' for infinity),
  syms [(conj, perm)], img (N, nsym) int32 image index or -1, aldist (N, nsym) alignment distance, cls (canonical tuples),
  log (residuals, smallest point distances).
usage: DPS=60 python3 build5.py n tag D [procs]"""
import os, sys, pickle, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
SL = os.path.join(HERE, '..')
for d in ('numeric-upto5-20261118', 'speedup-20261118', 'fast40-20261118', 'fastmono-20261119'): sys.path.insert(0, os.path.join(SL, d))
sys.path.insert(0, HERE)
_a = sys.argv; sys.argv = [_a[0], '0', '0', '1']
import mono, hp_fast, monodromy as md, autact
from covers import BP, AUT
sys.argv = _a
import mpmath as mp
DPS = int(os.environ.get('DPS', '60')); mp.mp.dps = DPS
ALTOL = float(os.environ.get('ALTOL', '1e-7'))
analyse = lambda *a, **k: mono.analyse(*a, **k) or mono.analyse_loose(*a, **k)

def refine_cov(p, q, n, prof, crit, ysl):
    an = analyse(p, q, n, prof, crit, ysl)
    if an is None: return None
    out, res, com, hpodd, critm, ys, nit = hp_fast.refine_full(p, q, an, n, iters=12, dps=DPS)
    if not res < 1e-25: return None
    return com, hpodd, critm, ys, float(res)

def refine_extra(p, q, n, prof, crit, ysl):
    """extras40.entry (degree7-20261119) for general n: 60-digit Newton, odd points from polyroots, fibre check."""
    an = {y: ([], [c for c, yy in zip(crit, ysl) if yy == y]) for y in range(6)}
    for y in range(6):
        g = (BP[y][1] * p - BP[y][0] * q)[::-1].copy()
        for c in an[y][1]:
            for _ in range(2): g, _r = np.polydiv(g, np.array([1, -c]))
        an[y] = (list(np.roots(g)) + [None] * (n - 2 * prof[y] - (len(g) - 1)), an[y][1])
    out, res, com, hpodd, critm, ys, nit = hp_fast.refine_full(p, q, an, n, iters=40, dps=DPS)
    assert res < 1e-25, res
    P = com[:n + 1]; Q = com[n + 1:]; hpo = {}
    for y in range(6):
        y0, y1 = mp.mpc(BP[y][0]), mp.mpc(BP[y][1])
        f = [y1 * P[m] - y0 * Q[m] for m in range(n + 1)]
        cr = [c for c, yy in zip(critm, ys) if yy == y]
        top = max(abs(v) for v in f)
        deg0 = max(m for m in range(n + 1) if abs(f[m]) > mp.mpf(10) ** -30 * top)
        h = list(f[:deg0 + 1])
        for c in cr:
            for _ in (0, 1):
                hi = h[::-1]; qd = [hi[0]]
                for a_ in hi[1:]: qd.append(a_ + c * qd[-1])
                h = qd[:-1][::-1]
        rts = mp.polyroots(h[::-1], maxsteps=3000, extraprec=400) if len(h) > 1 else []
        odd = list(rts) + [None] * (n - deg0)
        assert len(odd) == n - 2 * prof[y], (y, len(odd), prof)
        fin = [z for z in odd if z is not None] + [c for c in cr for _ in (0, 1)]
        g = [mp.mpc(1)]
        for r in fin: g = [mp.mpc(0)] + g; g = [g[k] - r * (g[k + 1] if k + 1 < len(g) else 0) for k in range(len(g))]
        deg = len(fin); lead = f[deg]
        rec = max(abs(f[m] - lead * g[m]) for m in range(deg + 1)) / top
        assert rec < mp.mpf(10) ** -35, rec
        hpo[y] = odd
    return com, hpo, critm, ys, float(res)

def hom(z):
    w = np.array((1, 0) if z is None else (complex(z), 1), complex); return w / np.linalg.norm(w)
def sstr(z): return b'inf' if z is None else (mp.nstr(z.real, DPS + 5).encode(), mp.nstr(z.imag, DPS + 5).encode())

def work(args):
    """refine covers idx of one profile (a worker)"""
    n, prof, F, covmap, idx = args
    mp.mp.dps = DPS
    out = []
    for i in idx:
        u = F['sols'][i]; p, q = u[:n + 1], u[n + 1:2 * n + 2]
        crit = list(F['fixed'][:3]) + list(u[2 * n + 2:]); ysl = list(F['ys'])
        r = refine_cov(p, q, n, prof, crit, ysl) if i in covmap else None
        kind = 'cov'
        if r is None:
            kind = 'extra'
            try: r = refine_extra(p, q, n, prof, crit, ysl)
            except AssertionError as e:      # drifts away under refinement (cf. E24 §2: 112323 #21): rebuilt below as an exact image
                out.append((i, None, None, None, None, None, None, None, 'failed')); continue
        com, hpo, critm, ys, res = r
        odd = [z for y in range(6) for z in hpo.get(y, [])]
        allp = [z for z in odd if z is not None] + list(critm)
        mind = min(float(abs(a - b)) for k, a in enumerate(allp) for b in allp[:k])
        out.append((i, np.array([complex(c) for c in com]), [hom(z) for z in odd], [sstr(z) for z in odd],
                    np.array([complex(c) for c in critm]), list(ys), res, mind, kind))
    return out

def main():
    n = int(sys.argv[1]); tag = sys.argv[2]; D = sys.argv[3]; NP = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    prof = tuple(int(c) for c in tag); t0 = time.time()
    F = pickle.load(open(f'{D}/full_{n}_{tag}.pkl', 'rb')); N = len(F['sols'])
    covmap = set(F['in_cov_file'])
    oddy = np.array([y for y in range(6) for _ in range(n - 2 * prof[y])]); nodd = len(oddy)
    chunks = [list(range(k, N, max(1, NP * 4))) for k in range(max(1, NP * 4))]
    NCH = max(1, N // 2000)                   # chunks of ~2000 covers, each saved (resume after a restart)
    chunks = [list(range(k, N, NCH)) for k in range(NCH)]
    os.makedirs(f'b5tmp_{n}_{tag}', exist_ok=True)
    def one(k):
        fn = f'b5tmp_{n}_{tag}/c{k}of{NCH}.pkl'
        if os.path.exists(fn): return pickle.load(open(fn, 'rb'))
        r = work((n, prof, F, covmap, chunks[k])); pickle.dump(r, open(fn + '.tmp', 'wb')); os.replace(fn + '.tmp', fn); return r
    if NP > 1:
        from multiprocessing import Pool
        with Pool(NP) as P: res = P.map(one, range(NCH))
    else: res = [one(k) for k in range(NCH)]
    R = sorted([r for rr in res for r in rr], key=lambda r: r[0]); assert [r[0] for r in R] == list(range(N))
    # covers whose own refinement failed: exact symmetry image of a refined cover of the same profile (rule-named;
    # the alignment check below then confirms the image relation numerically like every other)
    RR = pickle.load(open(os.path.join(SL, 'fastmono-20261119', 'aut_rules_7_222222.pkl'), 'rb'))
    rkey = {(cj, pi): w for (cj, M, pi), (pi2, w) in zip(autact.sym_list(tuple(RR['prof'])), RR['rules'])}
    syms = autact.sym_list(prof); cls = [md.canon(t)[0] for t in F['tuples']]
    bad = [i for i in range(N) if R[i][8] == 'failed']
    oddy0 = np.array([y for y in range(6) for _ in range(n - 2 * prof[y])])
    for i in bad:
        done_ = False
        for j in range(N):
            if R[j][8] == 'failed': continue
            for (cj, M, pi) in syms:
                if md.canon(autact.apply(F['tuples'][j], (pi, rkey[(cj, pi)])))[0] != cls[i]: continue
                _, pqj, oddj, sj, critj, ysj, resj, mindj, _k = R[j]
                pp, qq = (pqj[:n + 1].conj(), pqj[n + 1:].conj()) if cj else (pqj[:n + 1], pqj[n + 1:])
                pq2 = np.concatenate([M[0, 0] * pp + M[0, 1] * qq, M[1, 0] * pp + M[1, 1] * qq])
                om = np.array([k for yq in range(6) for k in range(len(oddy0)) if pi[oddy0[k]] == yq])
                ysa = np.array(ysj); cm = np.array([k for yq in range(6) for k in range(len(ysa)) if pi[ysa[k]] == yq])
                cv = lambda w: w.conj() if cj else w
                odd2 = [cv(oddj[k]) for k in om]
                def cs(x): return x if (x == b'inf' or not cj) else (x[0], x[1][1:] if x[1].startswith(b'-') else b'-' + x[1])
                s2 = [cs(sj[k]) for k in om]
                crit2 = np.array([critj[k] for k in cm]); crit2 = crit2.conj() if cj else crit2
                R[i] = (i, pq2, odd2, s2, crit2, [pi[ysa[k]] for k in cm], resj, mindj, f'image of {j}')
                done_ = True; break
            if done_: break
        assert done_, ('no refined cover maps to', i)
        print(f'cover {i}: refinement failed, replaced by the exact image ({R[i][8]})', flush=True)
    pq = np.array([r[1] for r in R]); odd = np.array([r[2] for r in R]); hp = np.array([[s if s == b'inf' else s for s in r[3]] for r in R], dtype=object)
    crit = np.array([r[4] for r in R]); crity = np.array(R[0][5])
    assert all(list(r[5]) == list(crity) for r in R)
    # string array (N, nodd, 2)
    H = np.empty((N, nodd, 2), dtype='S%d' % (DPS + 12))
    for i, r in enumerate(R):
        for k, s in enumerate(r[3]):
            H[i, k] = (b'inf', b'inf') if s == b'inf' else s
    aut = np.array([md.canon(t)[1] for t in F['tuples']]); cls = [md.canon(t)[0] for t in F['tuples']]
    log = [(r[6], r[7], r[8]) for r in R]
    t1 = time.time()
    # ---- symmetry images, named by rule, confirmed by alignment
    RR = pickle.load(open(os.path.join(SL, 'fastmono-20261119', 'aut_rules_7_222222.pkl'), 'rb'))
    rkey = {(cj, pi): w for (cj, M, pi), (pi2, w) in zip(autact.sym_list(tuple(RR['prof'])), RR['rules'])}
    syms = autact.sym_list(prof); idx = {c: i for i, c in enumerate(cls)}
    assert len(idx) == N
    import align_nb
    # labelled point sets: odd (label y) and double points (label 6 + y)
    PTS = np.concatenate([odd, np.array([[hom(z) for z in row] for row in crit])], 1)
    LAB = np.concatenate([oddy, 6 + crity])
    img = np.full((N, len(syms)), -1, np.int32); ald = np.ones((N, len(syms)))
    nbad = 0
    for k, (cj, M, pi) in enumerate(syms):
        rule = (pi, rkey[(cj, pi)])
        LX = np.array([pi[l] if l < 6 else 6 + pi[l - 6] for l in LAB])
        for i in range(N):
            c = md.canon(autact.apply(F['tuples'][i], rule))[0]
            j = idx.get(c)
            if j is None: nbad += 1; continue
            X = PTS[i].conj() if cj else PTS[i]
            # anchors: three odd points of different labels if possible
            anc = np.array(_anchors(LX, X), np.int64)
            d = align_nb.align(X[:, 0].copy(), X[:, 1].copy(), LX, PTS[j][:, 0].copy(), PTS[j][:, 1].copy(), LAB, anc, ALTOL)
            ald[i, k] = d
            if d <= ALTOL: img[i, k] = j
    t2 = time.time()
    unconf = int((img < 0).sum())
    print(f'n={n} prof={tag}: {N} covers (extra {sum(l[2] == "extra" for l in log)}), weighted {sum(1 / a for a in aut):.4f}, '
          f'worst residual {max(l[0] for l in log):.1e}, smallest point distance {min(l[1] for l in log):.1e}, '
          f'refine {t1 - t0:.0f}s; {len(syms)} symmetries, images unnamed {nbad}, unconfirmed {unconf}, '
          f'largest alignment distance {ald[img >= 0].max() if (img >= 0).any() else 0:.1e}, {t2 - t1:.0f}s', flush=True)
    np.save(f'L5hp_{n}_{tag}.npy', H)          # separate file (memory-mapped by search5)
    pickle.dump({'n': n, 'prof': prof, 'pq': pq, 'odd': odd, 'oddy': oddy, 'crit': crit, 'crity': crity, 'aut': aut,
                 'syms': [(cj, pi) for cj, M, pi in syms], 'img': img, 'aldist': ald, 'cls': cls, 'log': log},
                open(f'L5_{n}_{tag}.pkl', 'wb'))

def _anchors(L, X):
    """three points with the rarest labels, well separated"""
    order = sorted(range(len(L)), key=lambda i: (np.sum(L == L[i]), i))
    sel = []
    for i in order:
        if all(abs(X[i][0] * X[j][1] - X[i][1] * X[j][0]) > 1e-3 for j in sel): sel.append(i)
        if len(sel) == 3: break
    return sel

if __name__ == '__main__': main()
