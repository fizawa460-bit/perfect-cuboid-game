"""40-digit recheck of a pair that the double-precision fibre test calls BIRATIONAL (the E22 §3 procedure of
degree6-20261118/birhp.py, as a function that search3.py calls automatically on every such flag).

For a hit (f, q, M) with q = U∘r (r a profile representative, U in Aut(B)):
  1. f and r are refined at 40 digits (hp_fast.refine_full: coefficients, critical points and odd points).
  2. M40 is rebuilt from three well separated odd points of f that the double M matches (chordal < 1e-4) with odd
     points of q, and every labelled point of f^{-1}(B) (odd and double) is mapped by M40 and compared with
     q^{-1}(B) at 40 digits  ->  'points' (largest distance of the best-matched points, number matched < 1e-25).
  3. Fibre test at 40 digits: for three random t, the whole fibre f^{-1}(f(t)) is computed (mpmath polyroots, 40
     digits) and r∘M40 is evaluated on it (q∘M = U∘r∘M, and U is a bijection, so the fibres of q∘M and r∘M agree).
     If in every fibre at least one other point has the same value as t (distance < 1e-25) then r∘M40 = V∘f on
     three fibres, i.e. q∘M = V∘f: a composite, NOT birational.  If some fibre has only t itself and the next
     distance is > 1e-12, it is birational at 40 digits.  Anything else is 'unclear' (needs more digits).
Returns dict(verdict=..., fibres=[sorted distances per fibre], pts_max=..., pts_matched=..., nf=...)."""
import itertools, numpy as np, mpmath as mp
import hp_fast
from common import BP, AUT, BLAB

def _pts(co, crit, ys, hpo):
    P = []
    for y in range(6):
        for z in hpo.get(y, []): P.append((y, 0, (mp.mpc(1), mp.mpc(0)) if z is None else (z, mp.mpc(1))))
    for c, y in zip(crit, ys): P.append((y, 1, (c, mp.mpc(1))))
    return P
def _cd(u, v):
    w = u[0] * v[1] - u[1] * v[0]
    return abs(w) / (mp.sqrt(abs(u[0]) ** 2 + abs(u[1]) ** 2) * mp.sqrt(abs(v[0]) ** 2 + abs(v[1]) ** 2))
def _app(M, u): return (M[0][0] * u[0] + M[0][1] * u[1], M[1][0] * u[0] + M[1][1] * u[1])
def _mob3(a, b):
    def frame(z):
        Mt = mp.matrix([[z[0][0], z[1][0]], [z[0][1], z[1][1]]]); lm = mp.lu_solve(Mt, mp.matrix([z[2][0], z[2][1]]))
        return mp.matrix([[Mt[0, 0] * lm[0], Mt[0, 1] * lm[1]], [Mt[1, 0] * lm[0], Mt[1, 1] * lm[1]]])
    T = frame(b) * mp.inverse(frame(a)); return [[T[0, 0], T[0, 1]], [T[1, 0], T[1, 1]]]
_cache = {}
def _ref(key, p, q, an):
    if key not in _cache:
        n = len(p) - 1
        out, res, co, hpo, crit, ys, nit = hp_fast.refine_full(p, q, an, n, iters=15)
        _cache[key] = (co, _pts(co, crit, ys, hpo), res, n)
    return _cache[key]

def fibre_test(cf, n, cr, m, M40, seed=3, ntrial=3):
    """40-digit fibre test: for ntrial random t, sorted chordal distances of r∘M40 on the fibre f^{-1}(f(t)) to r∘M40(t)."""
    def r_after_M(z):
        w = _app(M40, (z, mp.mpc(1)))
        return (sum(cr[k] * w[0] ** k * w[1] ** (m - k) for k in range(m + 1)),
                sum(cr[m + 1 + k] * w[0] ** k * w[1] ** (m - k) for k in range(m + 1)))
    rng = np.random.default_rng(seed); fibres = []
    for _ in range(ntrial):
        t = mp.mpc(*map(float, rng.normal(size=2)))
        v = (sum(cf[k] * t ** k for k in range(n + 1)), sum(cf[n + 1 + k] * t ** k for k in range(n + 1)))
        poly = [v[1] * cf[k] - v[0] * cf[n + 1 + k] for k in range(n + 1)][::-1]
        rts = mp.polyroots(poly, maxsteps=400, extraprec=120)
        g0 = r_after_M(t); fibres.append(sorted(float(_cd(r_after_M(z), g0)) for z in rts))
    return fibres

def check(fkey, frep, rkey, rrep, ui, M, seed=3, ntrial=3):
    """frep, rrep = (p, q, an, ...) of the query cover f and of the representative r of q (q = AUT[ui] ∘ r)."""
    with mp.workdps(40):
        cf, Pf, resf, n = _ref(fkey, *frep[:3]); cr, Pr, resr, m = _ref(rkey, *rrep[:3])
        perm = AUT[ui][1]; Pq = [(perm[y], t, z) for y, t, z in Pr]
        Md = [[mp.mpc(complex(M[i, j])) for j in range(2)] for i in range(2)]
        match = []
        for y, t, z in Pf:
            w = _app(Md, z)
            cands = [(_cd(w, zz), k) for k, (yy, tt, zz) in enumerate(Pq) if BLAB[yy] == BLAB[y] and tt == t]
            match.append(min(cands, key=lambda a: a[0]) if cands else (mp.mpf(1), -1))
        oddg = [i for i, (d, k) in enumerate(match) if d < 1e-4 and Pf[i][1] == 0]
        if len(oddg) < 3: return dict(verdict='unclear', why='fewer than 3 matched odd points')
        best = max(((min(_cd(Pf[a][2], Pf[b][2]), _cd(Pf[a][2], Pf[c][2]), _cd(Pf[b][2], Pf[c][2])), (a, b, c))
                    for a, b, c in itertools.combinations(oddg[:10], 3)), key=lambda x: x[0])
        tri = best[1]; M40 = _mob3([Pf[i][2] for i in tri], [Pq[match[i][1]][2] for i in tri])
        dpts = sorted(float(min([_cd(_app(M40, z), zz) for yy, tt, zz in Pq if tt == t and BLAB[yy] == BLAB[y]] or [1]))
                      for y, t, z in Pf)
        fibres = fibre_test(cf, n, cr, m, M40, seed, ntrial)
        comp = all(f[1] < 1e-25 for f in fibres)
        bir = any(f[1] > 1e-12 for f in fibres)
        verdict = 'composite' if comp else ('BIRATIONAL' if bir else 'unclear')
        return dict(verdict=verdict, fibres=fibres, pts_max_matched=max([d for d in dpts if d < 1e-25] or [0.0]),
                    pts_matched=sum(d < 1e-25 for d in dpts), npts=len(Pf), res=(resf, resr))
