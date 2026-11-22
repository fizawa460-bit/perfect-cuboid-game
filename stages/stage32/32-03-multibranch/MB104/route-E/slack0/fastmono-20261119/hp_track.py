"""Path tracking of mono.System at 40 digits (python-flint acb), for the few moves whose double-precision track
fails because critical points almost collide on the way.  Same equations as mono.System.FJ."""
import numpy as np, flint
from flint import acb, acb_mat
DEBUG = False
import os
POLISH = [int(os.environ.get('HPPOLISH', '30'))]      # Newton steps at the start of track_path (0: off, the old behaviour)
def setup(dps=40): flint.ctx.dps = dps
def _poly(co, z):            # value, first and second derivative of sum co[j] z^j
    v = acb(0); d1 = acb(0); d2 = acb(0)
    for c in reversed(co): d2 = d2 * z + 2 * d1; d1 = d1 * z + v; v = v * z + c
    return v, d1, d2
class HP:
    def __init__(s, S):
        s.n = S.n; s.K = S.K; s.ys = list(S.ys); s.m = S.m
        s.fixed = [acb(complex(z).real, complex(z).imag) for z in S.fixed]
        s.L = [acb(complex(z).real, complex(z).imag) for z in S.L]
    def FJ(s, u, W, dW=None):
        n, K, m = s.n, s.K, s.m; p = u[:n + 1]; q = u[n + 1:2 * n + 2]; c = s.fixed + u[2 * n + 2:]
        F = [acb(0)] * m; J = acb_mat(m, m); Fd = [acb(0)] * m if dW is not None else None
        for k in range(K):
            y0, y1 = W[s.ys[k]]; z = c[k]
            Pv, Pd, Pdd = _poly(p, z); Qv, Qd, Qdd = _poly(q, z)
            F[k] = y1 * Pv - y0 * Qv; F[K + k] = y1 * Pd - y0 * Qd
            zj = acb(1); zj1 = acb(0)
            for j in range(n + 1):
                J[k, j] = y1 * zj; J[k, n + 1 + j] = -y0 * zj
                J[K + k, j] = y1 * j * zj1; J[K + k, n + 1 + j] = -y0 * j * zj1
                zj1 = zj; zj = zj * z
            if k >= 3:
                J[k, 2 * n + 2 + k - 3] = y1 * Pd - y0 * Qd; J[K + k, 2 * n + 2 + k - 3] = y1 * Pdd - y0 * Qdd
            if dW is not None:
                d0, d1 = dW[s.ys[k]]; Fd[k] = d1 * Pv - d0 * Qv; Fd[K + k] = d1 * Pd - d0 * Qd
        F[2 * K] = sum((a * b for a, b in zip(u[:2 * n + 2], s.L)), acb(0)) - 1
        for j in range(2 * n + 2): J[2 * K, j] = s.L[j]
        return F, J, Fd
def to_acb(x): return [acb(complex(z).real, complex(z).imag) for z in x]
def to_np(x): return np.array([complex(z.real.mid()) + 1j * float(z.imag.mid()) for z in x])
def _W(Wa, Wb, t): return [(Wa[y][0] + t * (Wb[y][0] - Wa[y][0]), Wa[y][1] + t * (Wb[y][1] - Wa[y][1])) for y in range(6)]
def norm(v): return max(abs(complex(z.real.mid()) + 1j * float(z.imag.mid())) for z in v)
def solve(J, F):
    x = J.solve(acb_mat([[f] for f in F]), nonstop=True, algorithm='approx')
    return [x[i, 0].mid() for i in range(x.nrows())]
def track_segment(H, u, Wa, Wb, h=0.05, hmin=1e-9, tol=None, maxsteps=20000):
    if tol is None: tol = 10.0 ** (-0.6 * flint.ctx.dps)
    """u: list of acb; Wa, Wb: (6,2) complex arrays. returns (u_end, ok)"""
    Wa = [tuple(to_acb(r)) for r in Wa]; Wb = [tuple(to_acb(r)) for r in Wb]
    dW = [(Wb[y][0] - Wa[y][0], Wb[y][1] - Wa[y][1]) for y in range(6)]
    t = 0.0; steps = 0
    while t < 1 - 1e-15 and steps < maxsteps:
        steps += 1; hh = min(h, 1 - t)
        _, J, Fd = H.FJ(u, _W(Wa, Wb, acb(t)), dW)
        v = solve(J, Fd); up = [(a - hh * b).mid() for a, b in zip(u, v)]          # Euler predictor
        W1 = _W(Wa, Wb, acb(t + hh)); good = False; first = None
        for it in range(6):
            F, J, _ = H.FJ(up, W1); dx = solve(J, F); nd = norm(dx) / (1 + norm(up))
            if first is None: first = nd
            up = [(a - b).mid() for a, b in zip(up, dx)]
            if nd < tol: good = True; break
            if it >= 1 and nd > 0.5 * prev: break
            prev = nd
        if good and first < 1e-3:
            u = up; t += hh; h = min(hh * 1.6, 0.2)
        else:
            h = hh / 2
            if h < hmin:
                if DEBUG: print('  stuck at t', t, 'first', first, 'nd', nd)
                return u, False
    return u, t >= 1 - 1e-15
def track_path(S, u_np, Ws, dps=40):
    setup(dps); H = HP(S); u = to_acb(u_np)
    if POLISH[0]:    # Newton at the start point first: for condition 1e10-1e13 the double start is off by up to 1e-3
        W0 = [tuple(to_acb(r)) for r in Ws[0]]          # relative, which fails the predictor's 'first < 1e-3' test at t = 0
        for _ in range(POLISH[0]):
            F, J, _ = H.FJ(u, W0); dx = solve(J, F); u = [(a - b).mid() for a, b in zip(u, dx)]
            if norm(dx) / (1 + norm(u)) < 10.0 ** (-0.8 * flint.ctx.dps): break
    for Wa, Wb in zip(Ws[:-1], Ws[1:]):
        u, ok = track_segment(H, u, Wa, Wb)
        if not ok: return None
    return u
