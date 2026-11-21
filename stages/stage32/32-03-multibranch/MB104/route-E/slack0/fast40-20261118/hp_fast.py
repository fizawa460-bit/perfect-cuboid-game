"""Fast 40-digit refinement: same square system and same outputs as hp.refine (numeric-upto5 / degree6), computed
with python-flint (arb/acb) instead of mpmath.

System (as hp.refine): unknowns P, Q coefficients (2n+2, low -> high) and the critical points c_k (the first three in
ys order are fixed); equations y1 P(c_k) - y0 Q(c_k) = 0, y1 P'(c_k) - y0 Q'(c_k) = 0 for every critical point and the
normalisation co[k0] = 1 (k0 = the largest coefficient).  Newton with the square Jacobian, solved by acb_mat
(approximate midpoint LU), at `dps` decimal digits (default 40, mpmath's prec = 136 bits).

Differences from hp.refine, all on the safe side:
  * stops when the Newton step is below 10^-(0.75 dps) (at least `miniters` steps; Newton converges quadratically,
    so the error after such a step is at the working precision), instead of a fixed number of steps;
  * the returned residual is the residual AFTER the last step (hp.refine returns the one before the last step);
  * the odd points are polished by Newton until the relative step is below 10^-(dps-5) (at most 30 steps; hp.refine: 12).
Return value: (out, res, co, hpodd) exactly as hp.refine, with co as python complex and hpodd as mpmath mpc
(so existing callers, e.g. hp_pre.py / search2.py / birhp.py, work unchanged).  refine_full also returns the
high-precision coefficients and critical points (mpmath mpc) like the patched refine of birhp.py."""
import mpmath as mp
from flint import acb, acb_mat, arb, ctx
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '../degree6-20261118'))
from common import BP

def _bits(dps): return int(round(dps * 3.3219280948873626)) + 3 if dps != 40 else 136

def to_mp(z):
    """acb (midpoint) -> mpmath mpc, exact transfer of the binary midpoint."""
    def f(x):
        m, e = x.mid().man_exp(); m = int(m); e = int(e)
        return mp.mpf((m, e)) if m else mp.mpf(0)
    return mp.mpc(f(z.real), f(z.imag))

def _acb(z): return z if isinstance(z, acb) else acb(complex(z).real, complex(z).imag)   # acb passes (80-digit starts)

def _newton(co, crit, Y, n, K, k0, prec_eps, iters, miniters):
    ncol = 2 * n + 2 + K - 3
    res = None
    for it in range(iters + 1):
        rows = []; R = []
        for k in range(K):
            c = crit[k]; y0, y1 = Y[k]
            pw = [acb(1)] * (n + 1)
            for m in range(1, n + 1): pw[m] = pw[m - 1] * c
            dpw = [acb(0)] + [m * pw[m - 1] for m in range(1, n + 1)]
            ddpw = [acb(0), acb(0)] + [m * (m - 1) * pw[m - 2] for m in range(2, n + 1)]
            Pc = sum((co[m] * pw[m] for m in range(n + 1)), acb(0)); Qc = sum((co[n + 1 + m] * pw[m] for m in range(n + 1)), acb(0))
            dP = sum((co[m] * dpw[m] for m in range(n + 1)), acb(0)); dQ = sum((co[n + 1 + m] * dpw[m] for m in range(n + 1)), acb(0))
            R.append(y1 * Pc - y0 * Qc); R.append(y1 * dP - y0 * dQ)
            if it == iters: continue
            ddP = sum((co[m] * ddpw[m] for m in range(n + 1)), acb(0)); ddQ = sum((co[n + 1 + m] * ddpw[m] for m in range(n + 1)), acb(0))
            r1 = [y1 * pw[m] for m in range(n + 1)] + [-y0 * pw[m] for m in range(n + 1)] + [acb(0)] * (K - 3)
            r2 = [y1 * dpw[m] for m in range(n + 1)] + [-y0 * dpw[m] for m in range(n + 1)] + [acb(0)] * (K - 3)
            if k >= 3:
                r1[2 * n + 2 + k - 3] = y1 * dP - y0 * dQ; r2[2 * n + 2 + k - 3] = y1 * ddP - y0 * ddQ
            rows.append(r1); rows.append(r2)
        R.append(co[k0] - 1)
        res = float(sum((abs(r).mid() ** 2 for r in R), arb(0)).sqrt())
        if it == iters: break
        r = [acb(0)] * ncol; r[k0] = acb(1); rows.append(r)
        J = acb_mat(rows); dx = J.solve(acb_mat([[v] for v in R]), algorithm='approx')
        step = 0.0
        for i in range(2 * n + 2):
            co[i] = (co[i] - dx[i, 0]).mid(); step = max(step, float(abs(dx[i, 0]).mid()))
        for k in range(3, K):
            crit[k] = (crit[k] - dx[2 * n + 2 + k - 3, 0]).mid(); step = max(step, float(abs(dx[2 * n + 2 + k - 3, 0]).mid()))
        if it + 1 >= miniters and step < prec_eps:
            iters = it + 1  # one more pass computes the final residual only
    return co, crit, res, it

def refine_full(p, q, an, n, iters=12, dps=40, miniters=2):
    old = ctx.prec; ctx.prec = _bits(dps)
    try:
        ys = [y for y in range(6) for _ in an[y][1]]
        crit = [_acb(z) for y in range(6) for z in an[y][1]]
        s = max(abs(v) for v in list(p) + list(q))
        co = [_acb(v / s) for v in list(p) + list(q)]
        k0 = max(range(2 * n + 2), key=lambda i: abs(complex(p[i] if i <= n else q[i - n - 1])))
        Y = [(_acb(BP[y][0]), _acb(BP[y][1])) for y in ys]
        K = len(ys); eps = 10.0 ** (-0.75 * dps); eps_pt = 10.0 ** (-(dps - 5))
        co, crit, res, nit = _newton(co, crit, Y, n, K, k0, eps, iters, miniters)
        critby = {y: [] for y in range(6)}
        for k in range(K): critby[ys[k]].append(crit[k])
        out = {}; hpodd = {}
        for y in range(6):
            y0, y1 = _acb(BP[y][0]), _acb(BP[y][1])
            f = [y1 * co[m] - y0 * co[n + 1 + m] for m in range(n + 1)]
            df = [m * f[m] for m in range(1, n + 1)]
            odd = []
            for z in an[y][0]:
                if z is None:
                    odd.append(None); hpodd.setdefault(y, []).append(None); continue
                z = _acb(z)
                for _ in range(30):
                    fz = f[n]; dfz = df[n - 1]
                    for m in range(n - 1, -1, -1): fz = fz * z + f[m]
                    for m in range(n - 2, -1, -1): dfz = dfz * z + df[m]
                    st = fz / dfz; z = (z - st).mid()
                    if float(abs(st).mid()) < eps_pt * (1 + float(abs(z).mid())): break
                zm = to_mp(z)
                odd.append(complex(zm)); hpodd.setdefault(y, []).append(zm)
            out[y] = (odd, [complex(to_mp(c)) for c in critby[y]])
        com = [to_mp(c) for c in co]; critm = [to_mp(c) for c in crit]
        return out, res, com, hpodd, critm, ys, nit
    finally:
        ctx.prec = old

def refine(p, q, an, n, iters=12, dps=40):
    """Drop-in replacement of hp.refine."""
    with mp.workdps(dps):
        out, res, com, hpodd, critm, ys, nit = refine_full(p, q, an, n, iters=iters, dps=dps)
        return out, res, [complex(c) for c in com], hpodd
