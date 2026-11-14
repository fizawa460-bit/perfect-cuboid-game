"""checks12 / metric12.py -- request 11: comparison of the two hyperbolic metrics rho_p = p^* rho_B, rho_q' = q'^* rho_B.

rho_B = hyperbolic metric (curvature -1) of the orbifold P^1(2^6), cone points B = {0, oo, +-1, +-i}.
It is the pull-back by the octahedral invariant J = W8^3 / (108 f^4)  (f = w(w^4-1), W8 = w^8+14w^4+1;
J = 0 at the face centres, 1 at the edge midpoints, oo at the vertices) of the metric of the (3,2,8) triangle orbifold,
computed from the Schwarz triangle function s = y2/y1,
  y1 = F(a,b;c;J), y2 = J^(1-c) F(a-c+1,b-c+1;2-c;J),  c = 2/3, a = 7/48, b = 1/48,
  rho_J = 2k|W| / (|y1|^2 - k^2|y2|^2),  W = (1-c) J^(-c) (1-J)^(-1/2),  k = tanh(c0/2)/|s(1)|, cosh c0 = cos(pi/8)/sin(pi/3).

Part A (mpmath, 50 digits): the identity W8^3 - E^2 = 108 f^4; the edge length int_0^1 rho_B = l_min (cosh l_min = 1+sqrt2);
        curvature -1 (Laplacian of log rho_B by high-precision differences) at random points.
Part B (exact model): H with one extra cone point of order 2:  u_model(d) = log((1+r)/(2 sqrt r)), r = tanh(d/2);
        u_model <= (1/2) Q_1(cosh d)  (Q_1 = Legendre function, (Delta-2)Q_1 = 0), and both ~ const * exp(-2d).
Part C (data): pairs (p, q' = q o T) with many common odd points (census9.search with a larger `keep`).
        u = log rho_p - log rho_q' at the nodes of a spherical grid, d = rho_p-distance to Omega = O(p) symm.diff. O(q')
        (Dijkstra on a nearest-neighbour graph; d is only the abscissa, accurate to a few percent, calibrated on l_min).
        Reported: sup of |u| over {d >= t}, least-squares slope of log sup|u| against t, and a 50-digit re-evaluation of u
        at sample nodes.  Records with O(p) = O(q') as sets (type (0,0)): u = 0 identically (check of the method).
usage (from the repository root; numpy, scipy, mpmath):
  python3 -I stages/stage32/32-03-multibranch/MB104/route-F/wall/checks12/metric12.py [grid points, default 8000]   (about 16 minutes)
"""
import sys, os, io, json, contextlib
sys.dont_write_bytecode = True
import numpy as np
import mpmath as mp
from scipy.special import hyp2f1
from scipy.spatial import cKDTree
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import dijkstra

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "checks9"))
import census9 as C9
mp.mp.dps = 50
ok = True
A_, B_, C_ = mp.mpf(7) / 48, mp.mpf(1) / 48, mp.mpf(2) / 3


def _k():
    c0 = mp.acosh(mp.cos(mp.pi / 8) / mp.sin(mp.pi / 3))
    s1 = mp.hyp2f1(A_ - C_ + 1, B_ - C_ + 1, 2 - C_, 1) / mp.hyp2f1(A_, B_, C_, 1)
    return mp.tanh(c0 / 2) / s1
K_MP = _k(); K = float(K_MP)


def J_and_dJ(w, lib):
    f = w * (w ** 4 - 1); W8 = w ** 8 + 14 * w ** 4 + 1
    df = 5 * w ** 4 - 1; dW8 = 8 * w ** 7 + 56 * w ** 3
    J = W8 ** 3 / (108 * f ** 4)
    return J, abs(J) * abs(3 * dW8 / W8 - 4 * df / f)


def rhoB_mp(w):
    """density of rho_B w.r.t. |dw| at a finite w (mp)."""
    w = mp.mpc(w)
    if abs(w) > 1: return rhoB_mp(1 / w) / abs(w) ** 2          # w -> 1/w is an octahedral rotation
    J, dJ = J_and_dJ(w, mp)
    y1 = mp.hyp2f1(A_, B_, C_, J); y2 = J ** (1 - C_) * mp.hyp2f1(A_ - C_ + 1, B_ - C_ + 1, 2 - C_, J)
    Wr = (1 - C_) * abs(J) ** (-C_) * abs(1 - J) ** (-mp.mpf(1) / 2)
    return 2 * K_MP * Wr / (abs(y1) ** 2 - K_MP ** 2 * abs(y2) ** 2) * dJ


def rhoB_np(w):
    w = np.asarray(w, dtype=complex)
    big = np.abs(w) > 1
    ww = np.where(big, 1 / np.where(big, w, 1), w)
    J, dJ = J_and_dJ(ww, np)
    a, b, c = float(A_), float(B_), float(C_)
    y1 = hyp2f1(a, b, c, J); y2 = J ** (1 - c) * hyp2f1(a - c + 1, b - c + 1, 2 - c, J)
    Wr = (1 - c) * np.abs(J) ** (-c) * np.abs(1 - J) ** (-0.5)
    r = 2 * K * Wr / (np.abs(y1) ** 2 - K ** 2 * np.abs(y2) ** 2) * dJ
    return np.where(big, r / np.abs(np.where(big, w, 1)) ** 2, r)


def pv(c, z, lib):
    if lib is mp: return mp.polyval(list(reversed(c)), z)
    return np.polyval(np.array([complex(x) for x in reversed(c)]), z)


def rho_pull(P, Q, z, lib):
    """density of p^* rho_B w.r.t. |dz| for p = P/Q (coefficients low -> high)."""
    dP = [i * P[i] for i in range(1, len(P))]; dQ = [i * Q[i] for i in range(1, len(Q))]
    p_, q_ = pv(P, z, lib), pv(Q, z, lib)
    num = pv(dP, z, lib) * q_ - p_ * pv(dQ, z, lib)
    if lib is mp:
        if abs(q_) > abs(p_): return rhoB_mp(p_ / q_) * abs(num) / abs(q_) ** 2
        return rhoB_mp(q_ / p_) * abs(num) / abs(p_) ** 2      # rho_B invariant under w -> 1/w
    inv = np.abs(q_) <= np.abs(p_)
    val = np.where(inv, q_ / np.where(inv, p_, 1), p_ / np.where(inv, 1, q_))
    den = np.where(inv, np.abs(p_), np.abs(q_)) ** 2
    return rhoB_np(val) * np.abs(num) / den


def compose_mob(P, Q, M, n):
    """coefficients of (P/Q) o T, T = (M00 z + M01)/(M10 z + M11)."""
    def sub(Cf):
        out = [mp.mpc(0)] * (n + 1)
        for i, ci in enumerate(Cf):
            term = [mp.mpc(1)]
            for _ in range(i): term = polymul(term, [M[0, 1], M[0, 0]])
            for _ in range(n - i): term = polymul(term, [M[1, 1], M[1, 0]])
            for k, t in enumerate(term): out[k] += ci * t
        return out
    return sub(list(P) + [mp.mpc(0)] * (n + 1 - len(P))), sub(list(Q) + [mp.mpc(0)] * (n + 1 - len(Q)))


def polymul(a, b):
    out = [mp.mpc(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i + j] += x * y
    return out


# ---------------- Part A: rho_B
print("Part A: rho_B (50 digits)")
w0 = mp.mpc("0.37", "0.21")
ident = abs((w0 ** 8 + 14 * w0 ** 4 + 1) ** 3 - (w0 ** 12 - 33 * w0 ** 8 - 33 * w0 ** 4 + 1) ** 2 - 108 * (w0 * (w0 ** 4 - 1)) ** 4)
lmin = mp.quad(lambda t: rhoB_mp(t), [0, mp.mpf(1) / 4, mp.mpf(1) / 2, mp.mpf(3) / 4, 1])
lref = mp.acosh(1 + mp.sqrt(2))
print("  |W8^3 - E^2 - 108 f^4| = %.1e;  int_0^1 rho_B = %s, arccosh(1+sqrt2) = %s, diff %.1e"
      % (float(ident), mp.nstr(lmin, 12), mp.nstr(lref, 12), float(abs(lmin - lref))))
ok &= ident < mp.mpf(10) ** -40 and abs(lmin - lref) < mp.mpf(10) ** -8
worst = 0
for pt in ["0.3+0.2j", "0.55-0.4j", "-0.2+0.7j", "1.4+0.9j", "0.05+0.03j", "0.9+0.3j"]:
    z0 = mp.mpc(complex(pt)); hh = mp.mpf(10) ** -12
    L = lambda dx, dy: mp.log(rhoB_mp(z0 + dx + 1j * dy))
    lap = (L(hh, 0) + L(-hh, 0) + L(0, hh) + L(0, -hh) - 4 * L(0, 0)) / hh ** 2
    worst = max(worst, abs(lap / rhoB_mp(z0) ** 2 - 1))
print("  curvature: max |Laplace(log rho_B)/rho_B^2 - 1| at 6 points = %.1e" % float(worst))
ok &= worst < mp.mpf(10) ** -15
rng = np.random.default_rng(11)
zz = rng.normal(size=300) + 1j * rng.normal(size=300)
dbl = rhoB_np(zz); ref = np.array([float(rhoB_mp(z)) for z in zz])
errA = float(np.max(np.abs(dbl / ref - 1)))
print("  double precision rho_B against 50 digits at 300 random points: max relative error %.1e" % errA)
ok &= errA < 1e-9

# ---------------- Part B: exact model
print("Part B: model (H with one extra cone point of order 2)")
Q1 = lambda d: mp.cosh(d) * mp.log(mp.coth(d / 2)) - 1
um = lambda d: mp.log((1 + mp.tanh(d / 2)) / (2 * mp.sqrt(mp.tanh(d / 2))))
okB = True
for d in [mp.mpf(x) / 10 for x in (1, 3, 5, 10, 15, 20, 30, 40, 60, 80)]:
    u_, v_ = um(d), Q1(d) / 2
    okB &= 0 < u_ < v_
    print("  d = %4.1f   u_model = %.6e   (1/2)Q_1 = %.6e   u_model*exp(2d) = %.5f   (1/2)Q_1*exp(2d) = %.5f   log coth(d/2) [Schwarz-Pick] = %.3e"
          % (float(d), float(u_), float(v_), float(u_ * mp.exp(2 * d)), float(v_ * mp.exp(2 * d)), float(mp.log(mp.coth(d / 2)))))
x0 = mp.mpf("1.7"); hh = mp.mpf(10) ** -10                     # (Delta - 2) Q_1(cosh d) = 0: Q'' + coth d Q' = 2 Q
res = (Q1(x0 + hh) + Q1(x0 - hh) - 2 * Q1(x0)) / hh ** 2 + mp.coth(x0) * (Q1(x0 + hh) - Q1(x0 - hh)) / (2 * hh) - 2 * Q1(x0)
res2 = (um(x0 + hh) + um(x0 - hh) - 2 * um(x0)) / hh ** 2 + mp.coth(x0) * (um(x0 + hh) - um(x0 - hh)) / (2 * hh) - (mp.exp(2 * um(x0)) - 1)
print("  residual of (Delta-2)Q_1 = 0: %.1e;  residual of Delta u = exp(2u) - 1 for u_model: %.1e" % (float(abs(res)), float(abs(res2))))
okB &= abs(res) < mp.mpf(10) ** -15 and abs(res2) < mp.mpf(10) ** -15
ok &= okB

# ---------------- Part C: data
N = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
print("Part C: pairs from the census (grid %d points)" % N)
gi = np.arange(N) + 0.5
phi = np.arccos(1 - 2 * gi / N); th = np.pi * (1 + 5 ** 0.5) * gi
XYZ = np.stack([np.sin(phi) * np.cos(th), np.sin(phi) * np.sin(th), np.cos(phi)], axis=1)


def to_xyz(z):
    if z is None: return np.array([0.0, 0.0, 1.0])
    z = complex(z); m = abs(z) ** 2
    return np.array([2 * z.real, 2 * z.imag, m - 1]) / (m + 1)


def to_z(X): return (X[:, 0] + 1j * X[:, 1]) / (1 - X[:, 2])


def graph_dist(P, Q, sources):
    """rho_p-distance from the source points to all grid nodes (graph approximation)."""
    pts = np.vstack([XYZ] + [to_xyz(s)[None, :] for s in sources])
    tree = cKDTree(pts); dd, nn = tree.query(pts, k=13)
    I = np.repeat(np.arange(len(pts)), 12); Jx = nn[:, 1:].ravel(); ch = dd[:, 1:].ravel()
    mid = pts[I] + pts[Jx]; mid /= np.linalg.norm(mid, axis=1)[:, None]
    zm = to_z(mid)
    with np.errstate(all="ignore"):
        rs = rho_pull(P, Q, zm, np) * (1 + np.abs(zm) ** 2) / 2     # density w.r.t. the spherical metric
    good = np.isfinite(rs) & (rs > 0)
    Wt = coo_matrix((rs[good] * ch[good], (I[good], Jx[good])), shape=(len(pts), len(pts)))
    D = dijkstra(Wt, directed=False, indices=list(range(N, len(pts))), min_only=True)
    return D[:N]


ID_P, ID_Q = [mp.mpc(0), mp.mpc(1)], [mp.mpc(1)]
cal = graph_dist(ID_P, ID_Q, [0])                               # calibration: distance from 0 to 1 in rho_B is l_min
i1 = int(np.argmin(np.linalg.norm(XYZ - to_xyz(1), axis=1)))
calib = float(lref) / cal[i1]
print("  graph distance 0 -> 1 in rho_B: %.4f (exact %.4f); distances are multiplied by %.4f" % (cal[i1], float(lref), calib))
ok &= abs(calib - 1) < 0.08

with contextlib.redirect_stdout(io.StringIO()):
    MAPS = {d: C9.load_maps(d, os.path.join(HERE, "..", "..", "f02")) for d in (1, 2, 3)}
recs = []
for (a, b, keep, first) in [(2, 2, 3, 6), (1, 2, 3, 6), (3, 3, 6, 8)]:
    rr = C9.search(MAPS[a], MAPS[b], a, b, first, False, keep)
    by = {}
    for r in rr:
        key = (a, b, r["m1"], r["m2"], r["h"], r["bdeg"])
        by.setdefault(key, r)                                   # one record of each kind
    recs += sorted(by.items(), key=lambda kv: kv[0])
    print("  bidegree (%d,%d), keep %d: %d records, %d kinds (m1, m2, h, degree onto image)" % (a, b, keep, len(rr), len(by)))
Z = to_z(XYZ)
out = []
for key, r in recs:
    a, b, m1, m2, h, bdeg = key
    p, q, M = r["p"], r["q"], r["M"]
    P2, Q2 = compose_mob(q.P, q.Q, M, q.n)
    Minv = mp.inverse(M)
    Oq = [C9.mob(Minv, z) for z, _ in q.O]
    Op = [z for z, _ in p.O]
    def far(z, S): return all(C9.chord(z, s) > mp.mpf(10) ** -20 for s in S)
    Om = [z for z in Op if far(z, Oq)] + [z for z in Oq if far(z, Op)]
    assert len(Om) == m1 + m2, (key, len(Om))
    with np.errstate(all="ignore"):
        u = np.log(rho_pull(p.P, p.Q, Z, np)) - np.log(rho_pull(P2, Q2, Z, np))
    fin = np.isfinite(u)
    if not Om:
        mx = float(np.max(np.abs(u[fin])))
        print("  (%d,%d) type (0,0) h=%d: O(p) = O(q') as sets;  max |u| on the grid = %.1e" % (a, b, h, mx))
        ok &= mx < 1e-7
        out.append(dict(key=list(key), max_abs_u=mx)); continue
    d = graph_dist(p.P, p.Q, Om) * calib
    ts = np.arange(0.25, d[fin].max(), 0.25); sup = []
    for t in ts:
        sel = fin & (d >= t)
        sup.append(float(np.max(np.abs(u[sel]))) if sel.sum() >= 20 else None)
    pts_fit = [(t, np.log(s)) for t, s in zip(ts, sup) if s and t >= 0.5]
    slope = float(np.polyfit([x for x, _ in pts_fit], [y for _, y in pts_fit], 1)[0]) if len(pts_fit) >= 3 else None
    # 50-digit re-evaluation at sample nodes
    idx = np.nonzero(fin)[0][:: max(1, fin.sum() // 25)]
    err = 0.0
    for i in idx:
        z = mp.mpc(complex(Z[i]))
        um_ = mp.log(rho_pull(p.P, p.Q, z, mp)) - mp.log(rho_pull(P2, Q2, z, mp))
        err = max(err, float(abs(um_ - u[i])))
    ok &= err < 1e-7
    print("  (%d,%d) m1=%d m2=%d h=%d |Omega pts|=%d of %d+%d, degree onto image %d: max d = %.2f, slope of log sup|u| = %s, double vs 50 digits %.1e"
          % (a, b, m1, m2, h, len(Om), len(Op), len(Oq), bdeg, float(d[fin].max()), "%.2f" % slope if slope is not None else "-", err))
    print("      t:        " + " ".join("%8.2f" % t for t in ts))
    print("      sup|u|:   " + " ".join(("%8.1e" % s) if s else "       -" for s in sup))
    out.append(dict(key=list(key), omega_points=len(Om), max_d=float(d[fin].max()), slope=slope, t=[float(t) for t in ts], sup=sup, err=err))
json.dump(out, open(os.path.join(HERE, "metric12.json"), "w"), indent=1)
print("PASS" if ok else "FAIL")
