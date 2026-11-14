"""Route F, trial F-01: the slack-0 mismatch spectrum (floating-point measurement, not a theorem).

Setting as in route-E E10 section 2 and E11 (k = 8, gamma = 0, slack s1 = s2 = 0).
- p1 runs over the slack-0 maps of degree a, and p2 = q o T, with q of degree b and T a Moebius map.
- O_i is the set of points of local degree 1 over B, labelled a / b / e.
- j (h) counts coincidences of O1 and O2 = T^-1(O_q) with equal (different) labels.
- |Omega| = |O1| + |O2| - 2j - h.

Difference from E11: every T with at least 3 coincidences (any labels) is enumerated. A T with c >= 3 coincidences
arises from exactly C(c,3) unordered source triples, so weighting by 1/C(c,3) counts distinct T.
A T with <= 2 coincidences has |Omega| >= |O1| + |O2| - 4 (the generic value). It is not enumerated; it is reported
as the trivial bound.

Output: for each bidegree, the distinct-T histogram of |Omega| (all pairs, birational or not), and an explicit list of
the distinct T with |Omega| <= OMCUT. Each listed T is tested for birationality (two-fibre test of E11), and
the minimum omega_min over birational pairs is reported.

The degree-1/2/3 slack-0 maps are rebuilt by the same method as route-E/slack0/e11_slack0_small.py (copied, so that
importing does not rerun E11). Cross-check: at (1,1) the distinct T with |Omega| <= 4 are 16 = {0: 4, 4: 12}, as in E11.

usage: python -I -O f01_mismatch_spectrum.py [bidegrees like 1x1 2x2 2x3 3x3] > f01.out
"""
import itertools, json, sys, time
from collections import Counter, defaultdict
from math import comb
import numpy as np
import sympy as sp
import mpmath as mp

# ---------------- slack-0 maps (as in E11) ----------------
mp.mp.dps = 60
I = sp.I; lam = sp.Symbol("lam")
Bv = [I, -I, sp.Integer(1), sp.Integer(-1), sp.Integer(0), sp.oo]


def rows(c, y):
    if c is sp.oo:
        if y is sp.oo: return [[0] * 4 + [0, 0, 0, 1], [0] * 4 + [0, 0, 1, 0]]
        return [[0, 0, 0, 1, 0, 0, 0, -y], [0, 0, 1, 0, 0, 0, -y, 0]]
    v = [c**k for k in range(4)]; dv = [k * c**(k - 1) if k else 0 for k in range(4)]
    if y is sp.oo: return [[0] * 4 + v, [0] * 4 + dv]
    return [v + [-y * x for x in v], dv + [-y * x for x in dv]]


def deg3_maps():
    out = []; stats = []
    for four in itertools.combinations(range(6), 4):
        ys = [Bv[k] for k in four]
        M = sp.Matrix(rows(sp.Integer(0), ys[0]) + rows(sp.oo, ys[1]) + rows(sp.Integer(1), ys[2]) + rows(lam, ys[3]))
        pl = sp.Poly(sp.expand(M.det()), lam)
        if pl.is_zero: stats.append("det=0"); continue
        for bad in (0, 1):
            while pl.degree() > 0 and sp.simplify(pl.eval(bad)) == 0: pl = sp.quo(pl, sp.Poly(lam - bad, lam))
        cfs_mp = [mp.mpc(sp.re(sp.N(c, 70)), sp.im(sp.N(c, 70))) for c in pl.all_coeffs()]
        roots = mp.polyroots(cfs_mp, maxsteps=200, extraprec=200) if pl.degree() > 0 else []
        good = 0
        for r in roots:
            A = mp.matrix(8, 8)
            for a_ in range(8):
                for b_ in range(8):
                    A[a_, b_] = mp.mpc(sp.lambdify(lam, M[a_, b_], "mpmath")(r))
            U, S, V = mp.svd_c(A)
            sv = sorted([abs(S[k]) for k in range(8)])
            if sv[1] < mp.mpf(10) ** -20: continue
            k = min(range(8), key=lambda q: abs(S[q]))
            x = [mp.conj(V[k, q]) for q in range(8)]
            P, Q = x[:4], x[4:]
            res = mp.det(mp.matrix([[P[3], P[2], P[1], P[0], 0, 0], [0, P[3], P[2], P[1], P[0], 0], [0, 0, P[3], P[2], P[1], P[0]],
                                    [Q[3], Q[2], Q[1], Q[0], 0, 0], [0, Q[3], Q[2], Q[1], Q[0], 0], [0, 0, Q[3], Q[2], Q[1], Q[0]]]))
            if abs(res) < mp.mpf(10) ** -30 * max(abs(z) for z in x) ** 6: continue
            good += 1; out.append((list(P), list(Q)))
        stats.append(f"det degree {pl.degree()}, genuine {good}")
    return out, stats


mp.mp.dps = 50
LAB = {"I": 0, "-I": 0, "1": 1, "-1": 1, "0": 2, "oo": 2}           # labels a, b, e as 0, 1, 2
BH = {"I": (1j, 1), "-I": (-1j, 1), "1": (1, 1), "-1": (-1, 1), "0": (0, 1), "oo": (1, 0)}
TOL = 1e-8


def nrm(v):
    v = np.asarray(v, dtype=complex); return v / np.linalg.norm(v)


def roots_hom(F):
    n = len(F) - 1
    Fm = [mp.mpc(c) for c in F]
    scale = max(abs(c) for c in Fm)
    deg = max(k for k in range(n + 1) if abs(Fm[k]) > scale * mp.mpf(10) ** -35)
    out = [(1, 0)] * (n - deg)
    if deg > 0:
        for r in mp.polyroots(list(reversed(Fm[:deg + 1])), maxsteps=300, extraprec=300):
            out.append((complex(r), 1))
    return [nrm(p) for p in out]


def map_data(P, Q):
    n = len(P) - 1; pts = []
    for key, (yx, yz) in BH.items():
        F = [yz * P[k] - yx * Q[k] for k in range(n + 1)]
        rts = roots_hom(F)
        for r in rts:
            mult = sum(1 for s in rts if abs(r[0] * s[1] - r[1] * s[0]) < 1e-12)
            if mult == 1: pts.append((r, LAB[key]))
            elif mult % 2 == 1: raise ValueError("odd multiplicity >= 3: not slack 0")
    return pts


def peval(P, Q, v):
    n = len(P) - 1; x, z = v
    return nrm([sum(complex(P[k]) * x**k * z**(n - k) for k in range(n + 1)),
                sum(complex(Q[k]) * x**k * z**(n - k) for k in range(n + 1))])


DEG3 = None


def maps_of_degree(n):
    global DEG3
    if n == 1: return [([mp.mpc(0), mp.mpc(1)], [mp.mpc(1), mp.mpc(0)])]
    if n == 2:
        res = []
        for y1, y2 in itertools.combinations(list(BH), 2):
            c = (mp.mpc(0.37, 0.81), mp.mpc(1))
            Y1, Y2 = [mp.mpc(v) for v in BH[y1]], [mp.mpc(v) for v in BH[y2]]
            A = mp.matrix([[Y1[0], Y2[0]], [Y1[1], Y2[1]]]); be_al = mp.lu_solve(A, mp.matrix([c[0], c[1]]))
            al, be = be_al[0], be_al[1]
            res.append(([al * Y1[0], 0, be * Y2[0]], [al * Y1[1], 0, be * Y2[1]]))
        return res
    if n == 3:
        if DEG3 is None:
            DEG3, st = deg3_maps()
            assert len(DEG3) == 60 and st == ["det degree 4, genuine 4"] * 15, st
        return DEG3
    raise ValueError(n)


def frame(p0, p1, p2):
    M = np.stack([p0, p1], axis=-1)
    co = np.linalg.solve(M, p2[..., None])[..., 0]
    return M * co[..., None, :]


def is_nonbirational(a, b, Pa, Qa, Pb, Qb, T):
    """E11 two-fibre test: q o T constant on two generic fibres of p1 (only possible if a > 1 and a | b)."""
    if a == 1 or b % a: return False
    for z0 in (np.array([0.4127 + 0.2291j, 1]), np.array([-1.37 + 0.61j, 1])):
        y0 = peval(Pa, Qa, nrm(z0))
        fib = roots_hom([y0[1] * Pa[m] - y0[0] * Qa[m] for m in range(a + 1)])
        imgs = [peval(Pb, Qb, nrm(T @ v)) for v in fib]
        if not all(abs(imgs[0][0] * w[1] - imgs[0][1] * w[0]) < 1e-9 for w in imgs): return False
    return True


def tkey(T):
    """canonical numeric key of a Moebius map: images of 0, 1, oo, rounded"""
    def aff(v):
        v = T @ v
        return "inf" if abs(v[1]) < 1e-9 * abs(v[0]) else (round((v[0] / v[1]).real, 6), round((v[0] / v[1]).imag, 6))
    return (aff(np.array([0, 1])), aff(np.array([1, 1])), aff(np.array([1, 0])))


def spectrum(a, b, omcut):
    t0 = time.time()
    A_maps, B_maps = maps_of_degree(a), maps_of_degree(b)
    A_dat = [map_data(P, Q) for P, Q in A_maps]; B_dat = [map_data(P, Q) for P, Q in B_maps]
    nA, nB = 2 * a + 4, 2 * b + 4
    assert all(len(d) == nA for d in A_dat) and all(len(d) == nB for d in B_dat)
    srcs = list(itertools.combinations(range(nA), 3))
    dsts = np.array(list(itertools.permutations(range(nB), 3)))
    hist = Counter()            # |Omega| -> number of distinct T (weighted), all pairs
    low = {}                    # (ia, ib, key) -> (om, j, h, c, nonbir)
    GAP = [0.0, 1.0]; raw = 0
    for ia, O1 in enumerate(A_dat):
        X1 = np.array([p for p, _ in O1]); L1 = np.array([l for _, l in O1])
        for ib, Oq in enumerate(B_dat):
            Xq = np.array([p for p, _ in Oq]); Lq = np.array([l for _, l in Oq])
            same = (L1[:, None] == Lq[None, :])
            Fd = frame(Xq[dsts[:, 0]], Xq[dsts[:, 1]], Xq[dsts[:, 2]])
            for tri in srcs:
                Fs = frame(X1[tri[0]], X1[tri[1]], X1[tri[2]])
                T = Fd @ np.linalg.inv(Fs)
                Ti = np.linalg.inv(T)
                O2 = np.einsum("kij,nj->kni", Ti, Xq)
                O2 = O2 / np.linalg.norm(O2, axis=-1, keepdims=True)
                cross = np.abs(X1[None, :, None, 0] * O2[:, None, :, 1] - X1[None, :, None, 1] * O2[:, None, :, 0])
                co = cross < TOL
                GAP[0] = max(GAP[0], cross[co].max())
                nc = cross[~co]
                if nc.size: GAP[1] = min(GAP[1], nc.min())
                j = (co & same[None]).sum(axis=(1, 2)); h = (co & ~same[None]).sum(axis=(1, 2))
                c = j + h
                om = nA + nB - 2 * j - h
                raw += len(dsts)
                w = 1.0 / np.array([comb(int(x), 3) for x in c])
                for o in np.unique(om): hist[int(o)] += float(w[om == o].sum())
                for k in np.nonzero(om <= omcut)[0]:
                    key = (ia, ib, tkey(T[k]))
                    if key in low: continue
                    nb = is_nonbirational(a, b, *A_maps[ia], *B_maps[ib], T[k])
                    low[key] = (int(om[k]), int(j[k]), int(h[k]), int(c[k]), nb)
    hist = {k: round(v, 6) for k, v in sorted(hist.items())}
    bir = Counter(v[0] for v in low.values() if not v[4]); nonb = Counter(v[0] for v in low.values() if v[4])
    om_bir = min(bir) if bir else None
    # coincidence pattern (j, h) of the extremal birational T
    ext = Counter((v[1], v[2]) for v in low.values() if not v[4] and v[0] == om_bir)
    res = dict(bidegree=[a, b], maps=[len(A_maps), len(B_maps)], O=[nA, nB], raw_T=raw,
               trivial_bound=nA + nB - 4, distinct_T_histogram_all=hist, omcut=omcut,
               birational_low=dict(sorted(bir.items())), nonbirational_low=dict(sorted(nonb.items())),
               omega_min_birational=om_bir, extremal_jh=sorted(ext.items()),
               gap=[GAP[0], GAP[1]], seconds=round(time.time() - t0, 1))
    return res, low


OMCUT = {(1, 1): 4, (1, 2): 6, (1, 3): 8, (2, 2): 8, (2, 3): 9, (3, 3): 10}

if __name__ == "__main__":
    todo = [tuple(int(x) for x in s.split("x")) for s in sys.argv[1:]] or [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
    ok = True
    for a, b in todo:
        res, low = spectrum(a, b, OMCUT[(a, b)])
        print(json.dumps(res))
        sys.stdout.flush()
        if not (res["gap"][0] < 1e-10 and res["gap"][1] > 1e-6):
            print(f"  ({a},{b}) WARNING: separation gap too small"); ok = False
        if (a, b) == (1, 1):
            d = Counter(v[0] for v in low.values() if v[0] <= 4)
            good = dict(d) == {0: 4, 4: 12}
            print("  (1,1) control vs E11 {0: 4, 4: 12}:", dict(d), "ok" if good else "MISMATCH"); ok &= good
        if (a, b) in ((2, 2), (2, 3), (3, 3)):
            good = res["omega_min_birational"] is None or res["omega_min_birational"] > 4
            print(f"  ({a},{b}) consistency with E11 (no birational |Omega|<=4):", "ok" if good else "MISMATCH"); ok &= good
    print("PASS" if ok else "FAIL")
    if not ok: raise SystemExit(1)
