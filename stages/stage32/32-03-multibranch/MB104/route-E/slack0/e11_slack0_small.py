"""E11 §4: Problem W at slack 0 (k = 8, gamma = 0), bidegrees (2,2), (2,3), (3,3); positive control (1,1).
Slack-0 maps: degree 1 = identity; degree 2 = M(t^2) with critical values in B (15); degree 3 = four simple critical
values in B, computed exactly as roots of an 8x8 determinant in the fourth critical point lam (sympy over Q(i)), then
kernels/fibres in mpmath (50-60 digits): 15 x 4 = 60 maps.  p1 = fixed representative, p2 = q o T; T is determined by a
coincident triple (label-matched when j >= 3); homogeneous coordinates, numpy.  Birationality: (p1, p2) must not factor
through a common map (tested on two generic fibres of p1).  Fail-closed expected counts; numerical separation gap checked.
usage: python -I -O e11_slack0_small.py   (about 4 minutes)"""

import itertools, json
import sympy as sp
import mpmath as mp
mp.mp.dps = 60
I = sp.I; lam = sp.Symbol("lam")
Bv = [I, -I, sp.Integer(1), sp.Integer(-1), sp.Integer(0), sp.oo]


def rows(c, y):
    """two linear conditions on (P0..P3, Q0..Q3): critical point c with critical value y"""
    if c is sp.oo:
        if y is sp.oo: return [[0] * 4 + [0, 0, 0, 1], [0] * 4 + [0, 0, 1, 0]]
        return [[0, 0, 0, 1, 0, 0, 0, -y], [0, 0, 1, 0, 0, 0, -y, 0]]
    v = [c**k for k in range(4)]; dv = [k * c**(k - 1) if k else 0 for k in range(4)]
    if y is sp.oo: return [[0] * 4 + v, [0] * 4 + dv]
    return [v + [-y * x for x in v], dv + [-y * x for x in dv]]


def poly_eval(cf, t): return sum(cf[k] * t**k for k in range(len(cf)))


def deg3_maps():
    out = []; stats = []
    for four in itertools.combinations(range(6), 4):
        ys = [Bv[k] for k in four]
        M = sp.Matrix(rows(sp.Integer(0), ys[0]) + rows(sp.oo, ys[1]) + rows(sp.Integer(1), ys[2]) + rows(lam, ys[3]))
        det = sp.expand(M.det())
        pl = sp.Poly(det, lam)
        if pl.is_zero: stats.append((four, "det=0")); continue
        # remove spurious roots lam = 0, 1 (critical points collide)
        for bad in (0, 1):
            while pl.degree() > 0 and sp.simplify(pl.eval(bad)) == 0: pl = sp.quo(pl, sp.Poly(lam - bad, lam))
        cfs = [complex(sp.N(c, 70)) for c in pl.all_coeffs()]
        cfs_mp = [mp.mpc(sp.re(sp.N(c, 70)), sp.im(sp.N(c, 70))) for c in pl.all_coeffs()]
        roots = mp.polyroots(cfs_mp, maxsteps=200, extraprec=200) if pl.degree() > 0 else []
        good = 0
        for r in roots:
            # numeric matrix at lam = r
            A = mp.matrix(8, 8)
            for a in range(8):
                for b in range(8):
                    f = sp.lambdify(lam, M[a, b], "mpmath"); A[a, b] = mp.mpc(f(r))
            U, S, V = mp.svd_c(A)
            sv = sorted([abs(S[k]) for k in range(8)])
            if sv[1] < mp.mpf(10) ** -20: stats.append((four, "kernel>1")); continue
            k = min(range(8), key=lambda q: abs(S[q]))
            x = [mp.conj(V[k, q]) for q in range(8)]
            P, Q = x[:4], x[4:]
            # genuine: resultant of P, Q nonzero and degree 3 (max(deg P, deg Q) == 3)
            res = mp.det(mp.matrix([[P[3], P[2], P[1], P[0], 0, 0], [0, P[3], P[2], P[1], P[0], 0], [0, 0, P[3], P[2], P[1], P[0]],
                                    [Q[3], Q[2], Q[1], Q[0], 0, 0], [0, Q[3], Q[2], Q[1], Q[0], 0], [0, 0, Q[3], Q[2], Q[1], Q[0]]]))
            nrm = max(abs(z) for z in x)
            if abs(res) < mp.mpf(10) ** -30 * nrm ** 6: stats.append((four, "degenerate")); continue
            good += 1
            out.append((list(P), list(Q)))
        stats.append((four, f"det degree {pl.degree()}, genuine {good}"))
    return out, stats


import sys, itertools
import numpy as np
import mpmath as mp
from collections import Counter
mp.mp.dps = 50
LAB = {"I": "a", "-I": "a", "1": "b", "-1": "b", "0": "e", "oo": "e"}
BH = {"I": (1j, 1), "-I": (-1j, 1), "1": (1, 1), "-1": (-1, 1), "0": (0, 1), "oo": (1, 0)}   # homogeneous (x : z)
TOL = 1e-8


def nrm(v):
    v = np.asarray(v, dtype=complex); return v / np.linalg.norm(v)


def roots_hom(F):
    """roots of a binary form F (coeff list F[k] of x^k z^(n-k)) as homogeneous unit vectors, with multiplicity"""
    n = len(F) - 1
    Fm = [mp.mpc(c) for c in F]
    scale = max(abs(c) for c in Fm)
    deg = max(k for k in range(n + 1) if abs(Fm[k]) > scale * mp.mpf(10) ** -35)
    out = [(1, 0)] * (n - deg)            # roots at infinity (z = 0)
    if deg > 0:
        for r in mp.polyroots(list(reversed(Fm[:deg + 1])), maxsteps=300, extraprec=300):
            out.append((complex(r), 1))
    return [nrm(p) for p in out]


def map_data(P, Q):
    """odd points (local degree 1 over B) with labels, for p = P/Q given as coefficient lists (mp numbers)"""
    n = len(P) - 1; pts = []
    for key, (yx, yz) in BH.items():
        F = [yz * P[k] - yx * Q[k] for k in range(n + 1)]   # yz*P - yx*Q = 0 <=> p = y
        rts = roots_hom(F)
        for k, r in enumerate(rts):   # local degree = number of roots coinciding with r
            mult = sum(1 for s in rts if abs(r[0] * s[1] - r[1] * s[0]) < 1e-12)
            if mult == 1: pts.append((r, LAB[key]))
            elif mult % 2 == 1: raise ValueError("odd multiplicity >= 3: not slack 0")
    return pts


def peval(P, Q, v):
    """p(v) for homogeneous v -> homogeneous image"""
    n = len(P) - 1; x, z = v
    return nrm([sum(complex(P[k]) * x**k * z**(n - k) for k in range(n + 1)), sum(complex(Q[k]) * x**k * z**(n - k) for k in range(n + 1))])


def maps_of_degree(n):
    if n == 1: return [([mp.mpc(0), mp.mpc(1)], [mp.mpc(1), mp.mpc(0)])]   # p = x / z
    if n == 2:
        res = []
        keys = list(BH)
        for y1, y2 in itertools.combinations(keys, 2):
            # p = M(t^2): M(0) = y1, M(oo) = y2, M(1) = c; as binary forms in (x, z)
            c = (mp.mpc(0.37, 0.81), mp.mpc(1))
            Y1, Y2 = [mp.mpc(v) for v in BH[y1]], [mp.mpc(v) for v in BH[y2]]
            # M = [[al*Y1x, be*Y2x],[al*Y1z, be*Y2z]] maps (0:1)->? use columns: M(e2)=Y1 (t=0 is (0:1)), M(e1)=Y2, M(1,1)=c
            A = mp.matrix([[Y1[0], Y2[0]], [Y1[1], Y2[1]]]); be_al = mp.lu_solve(A, mp.matrix([c[0], c[1]]))
            al, be = be_al[0], be_al[1]
            # p(x:z) = M(z^2 : x^2)?  we need M applied to (s : 1) with s = t^2, i.e. homogeneous (x^2 : z^2) -> s at index
            # M (s, 1)^T with column 1 <- Y2 (s = oo) and column 2 <- Y1 (s = 0): M = [be*Y2 | al*Y1] acting on (s, 1)
            P = [al * Y1[0], 0, be * Y2[0]]; Q = [al * Y1[1], 0, be * Y2[1]]   # coefficients of z^2, xz, x^2
            res.append((P, Q))
        return res
    if n == 3:
        return DEG3



DEG3, DEG3STATS = deg3_maps()

def search(a, b):
    A_maps, B_maps = maps_of_degree(a), maps_of_degree(b)
    A_dat = [map_data(P, Q) for P, Q in A_maps]; B_dat = [map_data(P, Q) for P, Q in B_maps]
    nA, nB = 2 * a + 4, 2 * b + 4
    assert all(len(d) == nA for d in A_dat) and all(len(d) == nB for d in B_dat)
    # j_min: 2j + h >= nA + nB - 4, h <= 4  ->  j >= ceil((nA + nB - 8) / 2)
    jmin = max(0, -(-(nA + nB - 8) // 2))
    LABELPRUNE = jmin >= 3      # a label-matched coincident triple exists only if j >= 3
    first = min(nA, nA - jmin + 3) if LABELPRUNE else nA
    print(f"bidegree ({a},{b}): {len(A_maps)} x {len(B_maps)} maps, |O| = {nA}, {nB}; j >= {jmin}; label pruning {LABELPRUNE}; triples among first {first} points of O1")


    def frame(p0, p1, p2):
        """matrix sending e1 -> p0, e2 -> p1, (1,1) -> p2 (columns scaled); arrays of shape (..., 2)"""
        M = np.stack([p0, p1], axis=-1)                  # (..., 2, 2)
        co = np.linalg.solve(M, p2[..., None])[..., 0]   # (..., 2)
        return M * co[..., None, :]


    GAP = [0.0, 1.0]; hits = []; nonbir = Counter(); tested = 0
    for ia, O1 in enumerate(A_dat):
        X1 = np.array([p for p, _ in O1]); L1 = np.array([l for _, l in O1])
        for ib, Oq in enumerate(B_dat):
            Xq = np.array([p for p, _ in Oq]); Lq = np.array([l for _, l in Oq])
            for tri in itertools.combinations(range(first), 3):
                dsts = [d for d in itertools.permutations(range(nB), 3) if not LABELPRUNE or all(L1[t] == Lq[s] for t, s in zip(tri, d))]
                if not dsts: continue
                dsts = np.array(dsts)
                K = len(dsts); tested += K
                Fs = frame(X1[tri[0]], X1[tri[1]], X1[tri[2]])                       # (2,2)
                Fd = frame(Xq[dsts[:, 0]], Xq[dsts[:, 1]], Xq[dsts[:, 2]])            # (K,2,2)
                T = Fd @ np.linalg.inv(Fs)                                            # T: V0 -> source of q
                Ti = np.linalg.inv(T)
                O2 = np.einsum("kij,nj->kni", Ti, Xq)                                 # (K, nB, 2)
                O2 = O2 / np.linalg.norm(O2, axis=-1, keepdims=True)
                cross = np.abs(X1[None, :, None, 0] * O2[:, None, :, 1] - X1[None, :, None, 1] * O2[:, None, :, 0])  # (K,nA,nB)
                co = cross < TOL
                if co.any(): GAP[0] = max(GAP[0], cross[co].max())
                nc = cross[~co]
                if nc.size: GAP[1] = min(GAP[1], nc.min())
                same = (L1[:, None] == Lq[None, :])
                j = (co & same[None]).sum(axis=(1, 2)); h = (co & ~same[None]).sum(axis=(1, 2))
                om = nA + nB - 2 * j - h
                for k in np.nonzero(om <= 4)[0]:
                    # birationality: (p1, q o T) must not factor through a common map of degree > 1.
                    # test: q o T constant on a generic fibre of p1  <=>  factors (deg p1 = a; common factor of degree a)
                    P1, Q1 = A_maps[ia]; Pq, Qq = B_maps[ib]
                    fac = True
                    for z0 in (np.array([0.4127 + 0.2291j, 1]), np.array([-1.37 + 0.61j, 1])):
                        y0 = peval(P1, Q1, nrm(z0))
                        F = [y0[1] * P1[m] - y0[0] * Q1[m] for m in range(a + 1)]
                        fib = roots_hom(F)
                        imgs = [peval(Pq, Qq, nrm(T[k] @ v)) for v in fib]
                        if not all(abs(imgs[0][0] * w[1] - imgs[0][1] * w[0]) < 1e-9 for w in imgs): fac = False
                    if a > 1 and fac and (b % a == 0):
                        nonbir[int(om[k])] += 1; continue
                    def aff(v):
                        v = T[k] @ v
                        return "inf" if abs(v[1]) < 1e-9 * abs(v[0]) else (round((v[0] / v[1]).real, 6), round((v[0] / v[1]).imag, 6))
                    key = (aff(np.array([0, 1])), aff(np.array([1, 1])), aff(np.array([1, 0])))
                    hits.append((ia, ib, int(om[k]), int(j[k]), int(h[k]), key))
    distinct = {(x[0], x[1], x[5]): x[2] for x in hits}
    print("Moebius maps tested:", tested)
    print("birational configurations with |Omega| <= 4: raw", len(hits), " distinct", len(distinct), " by |Omega|:", dict(Counter(distinct.values())))
    print("non-birational (raw) by |Omega|:", dict(nonbir))
    print("chordal-type gap: max coincidence %.2e, min non-coincidence %.2e" % tuple(GAP))
    return tested, distinct, dict(nonbir), GAP


EXPECT = {(1, 1): (2400, {0: 4, 4: 12}, {}), (2, 2): (98352, {}, {0: 4200, 4: 408}),
          (2, 3): (468096, {}, {}), (3, 3): (3287808, {}, {0: 8400, 4: 496})}
ok = len(DEG3) == 60 and all(s[1] == "det degree 4, genuine 4" for s in DEG3STATS) and len(DEG3STATS) == 15
print("degree-3 slack-0 maps:", len(DEG3), " per 4-subset:", Counter(s[1] for s in DEG3STATS))
for (a, b), (et, edist, enb) in EXPECT.items():
    tested, distinct, nonbir, gap = search(a, b)
    dc = dict(Counter(distinct.values()))
    good = tested == et and dc == edist and nonbir == enb and gap[0] < 1e-10 and gap[1] > 1e-6
    print(f"  ({a},{b}): tested {tested}, birational |Omega|<=4 {dc}, non-birational raw {nonbir}, gap {gap[0]:.1e}/{gap[1]:.1e} ->", "ok" if good else "MISMATCH")
    ok &= good
print("PASS" if ok else "FAIL")
if not ok: raise SystemExit(1)
