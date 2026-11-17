"""checks12 / lemma12.py -- request 11: the two-sided comparison lemma (Lemma M) checked on a compact orbifold.

Lemma M.  X a closed hyperbolic orbifold, rho_1 its metric, F a finite set of points; rho_2 the hyperbolic metric of
the orbifold obtained by doubling the cone order at the points of F (order 1 -> 2, or m -> 2m).  In the universal cover
H of X every lift of a point of F becomes a cone point of order 2 of the lifted rho_2.  With u = log(rho_2/rho_1):
      u_model(d_1)  <=  u(x)  <=  (1/2) sum over the lifts f of F of Q_1(cosh d(x, f)),
d_1 = distance to the nearest lift, u_model(d) = log((1+r)/(2 sqrt r)), r = tanh(d/2), Q_1(c) = (c/2) log((c+1)/(c-1)) - 1.

Test: X = P^1(3,2,8) (cone orders 3, 2, 8 at J = 0, 1, oo), F = one of the three cone points, so rho_2 is the metric
of P^1(3,2,16), P^1(3,4,8) or P^1(6,2,8).  Both metrics are Schwarz triangle functions (mpmath, 50 digits).
The lifts of F are the corresponding vertices of the (3,2,8) tiling: generated with the rotation group, all lifts
within distance RMAX of the origin; the rest of the sum is estimated by the area count (reported separately).
usage:  python3 -I stages/stage32/32-03-multibranch/MB104/route-F/wall/checks12/lemma12.py
"""
import sys
sys.dont_write_bytecode = True
import numpy as np
import mpmath as mp
from scipy.spatial import cKDTree
mp.mp.dps = 50
ok = True
RMAX = 8.5


class Tri:
    """metric of P^1(1/l, 1/m, 1/nu) (angles pi*l, pi*m, pi*nu at J = 0, 1, oo), density w.r.t. |dJ|; s maps the upper
    half plane to the triangle with the vertex of J = 0 at the origin and the vertex of J = 1 on the positive axis."""
    def __init__(s, l, m, nu):
        s.l, s.m, s.nu = l, m, nu
        s.c = 1 - l; s.a = (s.c - m + nu) / 2; s.b = (s.c - m - nu) / 2
        c0 = mp.acosh((mp.cos(mp.pi * nu) + mp.cos(mp.pi * l) * mp.cos(mp.pi * m)) / (mp.sin(mp.pi * l) * mp.sin(mp.pi * m)))
        s.tB = mp.tanh(c0 / 2)
        s1 = mp.hyp2f1(s.a - s.c + 1, s.b - s.c + 1, 2 - s.c, 1) / mp.hyp2f1(s.a, s.b, s.c, 1)
        s.k = s.tB / s1
        b0 = mp.acosh((mp.cos(mp.pi * m) + mp.cos(mp.pi * l) * mp.cos(mp.pi * nu)) / (mp.sin(mp.pi * l) * mp.sin(mp.pi * nu)))
        s.vC = mp.tanh(b0 / 2) * mp.expjpi(l)                    # vertex of J = oo
    def ys(s, J):
        return (mp.hyp2f1(s.a, s.b, s.c, J), J ** (1 - s.c) * mp.hyp2f1(s.a - s.c + 1, s.b - s.c + 1, 2 - s.c, J))
    def point(s, J):
        y1, y2 = s.ys(J); return s.k * y2 / y1
    def rho(s, J):
        y1, y2 = s.ys(J)
        W = s.l * abs(J) ** (s.l - 1) * abs(1 - J) ** (s.m - 1)
        return 2 * s.k * W / (abs(y1) ** 2 - s.k ** 2 * abs(y2) ** 2)


def orbit(T, v0):
    """orbit of v0 (complex, in the unit disc) under the rotation group of the triangle, within RMAX (double)."""
    w3 = np.exp(2j * np.pi * float(T.l)); t = float(T.tB)
    rotA = lambda z: w3 * z
    rotAi = lambda z: np.conj(w3) * z
    # rotation about B = t by the angle 2 pi m
    em = np.exp(2j * np.pi * float(T.m))
    def rotB(z, e=em):
        y = (z - t) / (1 - t * z); y = e * y
        return (y + t) / (1 + t * y)
    gens = [rotA, rotAi, rotB, lambda z: rotB(z, np.conj(em))]
    emb = lambda z: (2 * np.arctanh(np.minimum(np.abs(z), 1 - 1e-15)))[:, None] * np.stack([np.cos(np.angle(z)), np.sin(np.angle(z))], axis=1)
    pts = np.array([complex(v0)]); frontier = pts.copy()
    while len(frontier):
        cand = np.concatenate([g(frontier) for g in gens])
        cand = cand[2 * np.arctanh(np.abs(cand)) <= RMAX + 2.0]
        if not len(cand): break
        e = emb(cand)
        # dedup inside cand
        tr = cKDTree(e); keep = np.ones(len(cand), bool)
        for i, j in tr.query_pairs(1e-6): keep[max(i, j)] = False
        cand = cand[keep]
        d, _ = cKDTree(emb(pts)).query(emb(cand))
        frontier = cand[d > 1e-6]
        pts = np.concatenate([pts, frontier])
    return pts[2 * np.arctanh(np.abs(pts)) <= RMAX]


def hdist(z, P):
    return np.arccosh(1 + 2 * np.abs(z - P) ** 2 / ((1 - abs(z) ** 2) * (1 - np.abs(P) ** 2)))


Q1 = lambda d: np.cosh(d) * np.log(1 / np.tanh(d / 2)) - 1
um = lambda d: np.log((1 + np.tanh(d / 2)) / (2 * np.sqrt(np.tanh(d / 2))))
T1 = Tri(mp.mpf(1) / 3, mp.mpf(1) / 2, mp.mpf(1) / 8)
rng = np.random.default_rng(12)
samples = [mp.mpc(float(x), float(abs(y)) + 0.02) for x, y in zip(rng.normal(0.5, 1.5, 40), rng.normal(0, 1.5, 40))]
samples += [mp.mpc(0, "0.001"), mp.mpc(1, "0.001"), mp.mpc(0, 400), mp.mpc("0.5", "0.01"), mp.mpc(-30, 1), mp.mpc(40, 2)]
cases = [("oo: 8 -> 16", Tri(mp.mpf(1) / 3, mp.mpf(1) / 2, mp.mpf(1) / 16), T1.vC, 16),
         ("1:  2 -> 4", Tri(mp.mpf(1) / 3, mp.mpf(1) / 4, mp.mpf(1) / 8), T1.tB, 4),
         ("0:  3 -> 6", Tri(mp.mpf(1) / 6, mp.mpf(1) / 2, mp.mpf(1) / 8), mp.mpc(0), 6)]
area_tri = float(mp.pi * (1 - mp.mpf(1) / 3 - mp.mpf(1) / 2 - mp.mpf(1) / 8))
for name, T2, v0, mult in cases:
    P = orbit(T1, v0)
    dens = 1.0 / (2 * (mult // 2) * area_tri)                    # lifts per unit area: one vertex per 2*(old order) triangles
    expect = dens * 2 * np.pi * (np.cosh(RMAX) - 1)
    tail = dens * 2 * np.pi * (2.0 / 3.0) * np.exp(-RMAX) * 0.5 * 1.02 * 2   # int_R^oo sinh r (2/3)e^{-2r} dr ~ (1/3) e^{-R}; factor 2 margin
    worst_lo, worst_hi, rows = 1e9, 1e9, []
    for J in samples:
        u = float(mp.log(T2.rho(J)) - mp.log(T1.rho(J)))
        z = complex(T1.point(J)); d = np.sort(hdist(z, P))
        lo = float(um(d[0])); hi = 0.5 * float(np.sum(Q1(d))) + 0.5 * tail
        worst_lo = min(worst_lo, u - lo); worst_hi = min(worst_hi, hi - u)
        rows.append((d[0], lo, u, hi))
    rows.sort()
    good = worst_lo > 0 and worst_hi > 0 and abs(len(P) / expect - 1) < 0.05
    ok &= good
    print("F = point over J = %s: %d lifts within %.1f (area count %.0f); tail allowance %.1e; min(u - lower) = %.2e, min(upper - u) = %.2e  %s"
          % (name, len(P), RMAX, expect, 0.5 * tail, worst_lo, worst_hi, "ok" if good else "FAIL"))
    for r in rows[:: max(1, len(rows) // 8)]:
        print("     nearest lift %.3f:  u_model = %.5f  <=  u = %.5f  <=  (1/2) sum Q_1 = %.5f   (u/upper = %.2f, u*exp(2 d1) = %.2f)"
              % (r[0], r[1], r[2], r[3], r[2] / r[3], r[2] * np.exp(2 * r[0])))
print("PASS" if ok else "FAIL")
