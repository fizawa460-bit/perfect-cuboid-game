"""Rigorous (ball-arithmetic) tools for slack-0 covers of (P^1; B), B = {0, inf, 1, -1, i, -i}.

A normalized map is a vector u = (p_0..p_n, q_0..q_n, c_3..c_{K-1}), K = 2n-2, with
  f = P/Q, crit points c_0, c_1, c_2 = PHI (exact dyadic constants), c_3.. free,
  equations  F_{y_k}(c_k) = 0,  F'_{y_k}(c_k) = 0  (k = 0..K-1),  L.x = 1,
  F_y = y1*P - y0*Q for y = y0/y1 in B.
Everything that is claimed is checked with arb balls (python-flint); doubles are only used as starting points.
"""
import itertools
import numpy as np
from flint import acb, arb, acb_mat, ctx

ctx.prec = 320
BH = [(0, 1), (1, 0), (1, 1), (-1, 1), (1j, 1), (-1j, 1)]          # (y0, y1), value y0/y1
BLAB = [0, 0, 1, 1, 2, 2]                                           # label class e, b, a
Y0 = [acb(complex(a).real, complex(a).imag) for a, b in BH]
Y1 = [acb(b) for a, b in BH]
PHI = [acb(0.3125, 0.1875), acb(-0.5, 0.4375), acb(0.125, -0.625)]  # exact dyadic constants
PHIc = [complex(0.3125, 0.1875), complex(-0.5, 0.4375), complex(0.125, -0.625)]


def Lvec(n):
    r = np.random.default_rng(12345 + n)
    return [complex(round(a * 16) / 16 or 0.0625, round(b * 16) / 16) for a, b in r.normal(size=(2 * n + 2, 2))]


def A(z):
    """exact acb from a python complex / float / str pair"""
    if isinstance(z, acb): return z
    z = complex(z); return acb(z.real, z.imag)


def ball(m, r):
    """rectangle m + [-r, r] + i[-r, r]"""
    return acb(arb(m.real.mid(), r), arb(m.imag.mid(), r))


def cpx(z):
    m = z.mid(); return complex(float(m.real), float(m.imag))


def radup(z):
    """upper bound of max(rad re, rad im) as float"""
    return float(max(z.real.rad(), z.imag.rad())) * (1 + 1e-12) + 1e-300


def peval(co, z):
    s = acb(0)
    for c in reversed(co): s = s * z + c
    return s


def pder(co): return [co[k] * k for k in range(1, len(co))]


def pmul(a, b):
    out = [acb(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i + j] = out[i + j] + x * y
    return out


def mob_subst(co, n, T):
    """coefficients (low->high, degree n form) of co((a z + b)/(c z + d)) * (c z + d)^n"""
    a, b, c, d = T
    num = [b, a]; den = [d, c]
    pw_num = [[acb(1)]]; pw_den = [[acb(1)]]
    for _ in range(n): pw_num.append(pmul(pw_num[-1], num)); pw_den.append(pmul(pw_den[-1], den))
    out = [acb(0)] * (n + 1)
    for k in range(n + 1):
        t = pmul(pw_num[k], pw_den[n - k])
        for i in range(n + 1): out[i] = out[i] + co[k] * t[i]
    return out


def mob_apply(T, z):
    a, b, c, d = T; return (a * z + b) / (c * z + d)


def mob_inv(T):
    a, b, c, d = T; return (d, -b, -c, a)


def mob_mul(S, T):
    a, b, c, d = S; e, f, g, h = T
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)


def frame(p0, p1, p2):
    """Mobius sending inf->p0, 0->p1, 1->p2 (finite p's): z -> (p0*l0*z + p1*l1)/(l0*z + l1), l0 + l1 = 1 scaled"""
    # columns (p0,1)*l0 and (p1,1)*l1 with l0*(p0,1)+l1*(p1,1) ~ (p2,1)
    # l0 p0 + l1 p1 = p2 ; l0 + l1 = 1
    l0 = (p2 - p1) / (p0 - p1); l1 = 1 - l0
    return (p0 * l0, p1 * l1, l0, l1)


def mob3(x, y):
    """Mobius T with T(x_k) = y_k, k = 0, 1, 2"""
    return mob_mul(frame(*y), mob_inv(frame(*x)))


class Sys:
    def __init__(s, n, ys):
        s.n = n; s.ys = list(ys); s.K = 2 * n - 2
        s.L = [A(z) for z in Lvec(n)]
        s.D = 2 * n + 2 + s.K - 3

    def unpack(s, u):
        n = s.n
        return u[:n + 1], u[n + 1:2 * n + 2], PHI + list(u[2 * n + 2:])

    def G(s, u):
        p, q, c = s.unpack(u); n = s.n
        dp, dq = pder(p), pder(q)
        F = []; Fd = []
        for k in range(s.K):
            y = s.ys[k]
            F.append(Y1[y] * peval(p, c[k]) - Y0[y] * peval(q, c[k]))
            Fd.append(Y1[y] * peval(dp, c[k]) - Y0[y] * peval(dq, c[k]))
        lx = acb(0)
        for j in range(2 * n + 2): lx = lx + s.L[j] * u[j]
        return F + Fd + [lx - 1]

    def J(s, u):
        p, q, c = s.unpack(u); n = s.n; K = s.K; D = s.D
        dp, dq = pder(p), pder(q); ddp, ddq = pder(dp), pder(dq)
        M = [[acb(0)] * D for _ in range(2 * K + 1)]
        for k in range(K):
            y = s.ys[k]; ck = c[k]
            pw = [acb(1)]
            for _ in range(n): pw.append(pw[-1] * ck)
            for j in range(n + 1):
                M[k][j] = Y1[y] * pw[j]; M[k][n + 1 + j] = -Y0[y] * pw[j]
                if j >= 1:
                    M[K + k][j] = Y1[y] * j * pw[j - 1]; M[K + k][n + 1 + j] = -Y0[y] * j * pw[j - 1]
            if k >= 3:
                col = 2 * n + 2 + k - 3
                M[k][col] = Y1[y] * peval(dp, ck) - Y0[y] * peval(dq, ck)
                M[K + k][col] = Y1[y] * peval(ddp, ck) - Y0[y] * peval(ddq, ck)
        for j in range(2 * n + 2): M[2 * K][j] = s.L[j]
        return M

    def newton(s, u, iters=40, tol=1e-85):
        u = [A(x) if not isinstance(x, acb) else x.mid() for x in u]
        for it in range(iters):
            G = acb_mat([[g.mid()] for g in s.G(u)])
            J = acb_mat([[x.mid() for x in row] for row in s.J(u)])
            dx = J.solve(G)
            u = [(u[i] - dx[i, 0]).mid() for i in range(s.D)]
            st = max(abs(cpx(dx[i, 0])) for i in range(s.D))
            if st < tol * (1 + max(abs(cpx(x)) for x in u)): break
        return u, st

    def krawczyk(s, u, rho):
        """u: midpoint list (exact acb). True => unique exact solution in the box u + rect(rho)."""
        D = s.D
        Z = [ball(x, rho) for x in u]
        G = s.G(u)
        Jm = acb_mat([[x.mid() for x in row] for row in s.J(u)])
        Y = Jm.inv()
        Y = acb_mat([[Y[i, j].mid() for j in range(D)] for i in range(D)])
        JZ = acb_mat(s.J(Z))
        C = acb_mat([[(1 if i == j else 0) for j in range(D)] for i in range(D)]) - Y * JZ
        Dl = acb_mat([[acb(arb(0, rho), arb(0, rho))] for _ in range(D)])
        Kv = -(Y * acb_mat([[g] for g in G])) + C * Dl
        ok = True; worst = 0.0
        for i in range(D):
            k = Kv[i, 0]
            for part in (k.real, k.imag):
                hi = max(abs(float(part.upper())), abs(float(part.lower())))
                worst = max(worst, hi / rho)
                if not (part.upper() < rho and part.lower() > -rho): ok = False
        return ok, worst


def box(u, rho): return [ball(x, rho) for x in u]


def sylvester_res(p, q, n):
    """homogeneous resultant of two degree-n binary forms (coeff lists low->high)"""
    N = 2 * n
    rows = []
    P = list(reversed(p)); Q = list(reversed(q))
    for i in range(n): rows.append([acb(0)] * i + P + [acb(0)] * (n - 1 - i))
    for i in range(n): rows.append([acb(0)] * i + Q + [acb(0)] * (n - 1 - i))
    return acb_mat(rows).det()


def krawczyk1(co, r, rho):
    """1-D Krawczyk on the polynomial with ball coefficients co near r. Returns (ok, t): ok => for every
    polynomial in the coefficient box there is exactly one root in r + rect(rho), and it lies in r + rect(t)."""
    d = pder(co)
    y = 1 / peval(d, r).mid()
    y = y.mid()
    Dl = acb(arb(0, rho), arb(0, rho))
    Kk = -y * peval(co, r) + (1 - y * peval(d, ball(r, rho))) * Dl
    ok = (Kk.real.upper() < rho and Kk.real.lower() > -rho and Kk.imag.upper() < rho and Kk.imag.lower() > -rho)
    t = max(abs(float(Kk.real.upper())), abs(float(Kk.real.lower())), abs(float(Kk.imag.upper())), abs(float(Kk.imag.lower())))
    return ok, t * (1 + 1e-9)


def newton1(co_mid, z, iters=60):
    d = pder(co_mid)
    for _ in range(iters):
        dz = peval(co_mid, z) / peval(d, z)
        z = (z - dz).mid()
        if abs(cpx(dz)) < 1e-90 * (1 + abs(cpx(z))): break
    return z


def disjoint(a, b):
    return not a.overlaps(b)


def enc_r(x):
    m, e = x.mid().man_exp(); return (int(m), int(e))


def enc(z):
    """exact encoding of the midpoint of an acb: ((man, exp), (man, exp))"""
    return (enc_r(z.real), enc_r(z.imag))


def dec_r(t):
    m, e = t; return arb(m) * arb(2) ** e


def dec(t):
    return acb(dec_r(t[0]), dec_r(t[1]))


def dec_f(t):
    return complex(float(dec_r(t[0])), float(dec_r(t[1])))
