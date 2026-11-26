"""Compiled kernels of search7.py (numba): the five-point key.

A 5-point set {p_0..p_4} of P^1 has five 4-point subsets (omit p_e); each has a Moebius-invariant j-invariant
J_e = j(lambda_e) / 1728 (any ordering of the four points gives the same J_e).  The key of the set is
    K = (sum_e s_e, sum_e s_e[2]^2) in R^4,   s_e = point of J_e on the unit sphere (as _sph),
which is invariant under Moebius maps AND under reordering of the five points, so the table stores each 5-subset
once and the query looks up each of its 5-subsets once (no orderings).

Window.  Points carry an error delta (chordal, unit homogeneous pairs); every wedge w_ij then has relative error
<= delta / |w_ij|.  With n = w13 w24, d = w14 w23 (n - d = w12 w34), normalised by m = max(|n|, |d|):
    J = (4/27) T^3 / D,   T = v^2 - v e + e^2,   D = v^2 e^2 (v - e)^2   (v = n/m, e = d/m),
and to first order the sphere point s of J moves by at most  delta * S * phi,  S = sum over the six pairs of
1/|w_ij| (_cond4), phi = (4 |J| + (8/3) |T|^2 / |D|) / (1 + |J|^2)  (|dD/D| <= 2 delta S, |dT| <= 3 delta S m^2;
phi -> 0 when J -> infinity, which is where the sphere compresses).  Each key coordinate moves by at most twice the
sum of the five |ds_e| (z^2 has Lipschitz constant 2), so with Phi = sum_e S_e phi_e of each side we test
    max_i |K_i(X) - K_i(Y)| <= w = 2.1 * DEL * (Phi_X + Phi_Y) + 1e-13,
DEL = delta per point (search7 env DELTA7, default 1e-12).  The stored doubles are the 60-digit points rounded:
measured chordal error <= 1.6e-16 (degree 8 L5 and degree 9 L7 samples), so DEL = 1e-12 has a margin of > 6000
(search6's TOL = 1e-9 is a window scale that also absorbs its ordering-dependent cross-ratio conditioning).  The bound is symmetric in the five points (no correspondence of the quadruples is needed) and
separable (Phi of the table entry is stored).

Key points of a table cover: Fb5 odd points taken round-robin over the branch points (first point of each fibre,
then the second, ...), so that they do not all lie in one fibre: a fibre that is one orbit of an automorphism group of
the cover is rigid up to Moebius maps (e.g. six points with cyclic symmetry), and many different covers then share the
same keys.  Any fixed choice per cover is valid (>= 5 of any Fb5 points are matched).  KP is indexed by cover
(KP[cover] = its Fb5 key positions, PID = the C(Fb5, 5) subsets of range(Fb5): names kept from the per-profile version).

Table: entries (cover, subset) of one slice of K_0, in a dense 2-D grid of cells (G x G in (K_0, K_1)), CSR layout,
each with its K (float64, as computed: the tests are exact) and Phi (float32, used as Phi * (1 + 1e-6)); the
window ranges carry 1e-11 for the rounding of the bisection keys (sub * 16 + K_2 + 5 <= 1040, ulp 2.3e-13).  A surviving (query subset, entry) is tried in the 120 orderings: the two
quadruples (0123), (1234) must meet search6's own window, then search6's Moebius map from three points, count of
query points with a table point within chordal 1e-4 (maxfail) and one-to-one bound, as scan_nb._prefilter_one,
but without the label test (labels depend on the coset of the table cover; search7 checks every coset after)."""
import numpy as np
from numba import njit, prange
from scan6_nb import _wedge, _sph, _cross4, _cond4, _kap, _frame, _hp


@njit(cache=True, inline='always')
def _jsph(a0, a1, b0, b1, c0, c1, d0, d1):
    """sphere point of j(lambda)/1728 for the four points (any order)"""
    n = _wedge(a0, a1, c0, c1) * _wedge(b0, b1, d0, d1)
    d = _wedge(a0, a1, d0, d1) * _wedge(b0, b1, c0, c1)
    m = max(abs(n), abs(d)); n = n / m; d = d / m
    t = n * n - n * d + d * d; e = n - d; D = n * n * d * d * e * e
    x, y, z = _sph(4.0 / 27.0 * t * t * t, D)
    if abs(D) == 0: return x, y, z, 1e300
    aJ = 4.0 / 27.0 * abs(t) ** 3 / abs(D)
    return x, y, z, (4 * aJ + 8.0 / 3.0 * abs(t) ** 2 / abs(D)) / (1 + aJ * aJ)

@njit(cache=True)
def _key5(P0, P1, K):
    """K[0:4] = key of the five points (P0[k], P1[k]); returns Phi = sum_e S_e phi_e (see Window)"""
    for i in range(4): K[i] = 0.0
    S5 = 0.0
    for e in range(5):
        idx = np.empty(4, np.int64); m = 0
        for k in range(5):
            if k != e: idx[m] = k; m += 1
        a, b, c, d = idx[0], idx[1], idx[2], idx[3]
        x, y, z, phi = _jsph(P0[a], P1[a], P0[b], P1[b], P0[c], P1[c], P0[d], P1[d])
        K[0] += x; K[1] += y; K[2] += z; K[3] += z * z
        S5 += _cond4(P0[a], P1[a], P0[b], P1[b], P0[c], P1[c], P0[d], P1[d]) * phi
    return S5

@njit(cache=True)
def _key5s(P0, P1, K, SV):
    """_key5, also SV[e] = sphere point of J_e (quadruple without point e)"""
    for i in range(4): K[i] = 0.0
    S5 = 0.0
    for e in range(5):
        idx = np.empty(4, np.int64); m = 0
        for k in range(5):
            if k != e: idx[m] = k; m += 1
        a, b, c, d = idx[0], idx[1], idx[2], idx[3]
        x, y, z, phi = _jsph(P0[a], P1[a], P0[b], P1[b], P0[c], P1[c], P0[d], P1[d])
        SV[e, 0] = x; SV[e, 1] = y; SV[e, 2] = z
        K[0] += x; K[1] += y; K[2] += z; K[3] += z * z
        S5 += _cond4(P0[a], P1[a], P0[b], P1[b], P0[c], P1[c], P0[d], P1[d]) * phi
    return S5

@njit(cache=True, inline='always')
def _win5(SX, SY, DEL, EPS4):
    return 2.1 * DEL * (SX + SY) + 1e-13

@njit(cache=True)
def _tkey(Z, INF, rep, KP, PID, sb, P0, P1, K):
    for k in range(5):
        i = KP[rep, PID[sb, k]]; P0[k], P1[k] = _hp(Z[rep, i], INF[rep, i])
    return _key5(P0, P1, K)

@njit(cache=True, inline='always')
def _cell(K, Phi, xlo, TI, GK, NYK, BASE):
    k = 0
    while k + 1 < len(GK) and Phi >= TI[k + 1]: k += 1
    return BASE[k] + np.int64((K[0] - xlo) / GK[k]) * NYK[k] + np.int64((K[1] + 5.0) / GK[k])

@njit(cache=True)
def count7(Z, INF, NT, KP, PID, xlo, xhi, TI, GK, NYK, BASE, cnt):
    """cnt[cell] += 1 for every entry (cover r < NT, subset sb) with K_0 in [xlo, xhi); tier k by Phi in
    [TI[k], TI[k+1]), cell = BASE[k] + cx * NYK[k] + cy on the grid of width GK[k]"""
    P0 = np.empty(5, np.complex128); P1 = np.empty(5, np.complex128); K = np.empty(4)
    for r in range(NT):
        for sb in range(PID.shape[0]):
            Phi = _tkey(Z, INF, r, KP, PID, sb, P0, P1, K)
            if K[0] < xlo or K[0] >= xhi: continue
            cnt[_cell(K, Phi, xlo, TI, GK, NYK, BASE)] += 1

@njit(cache=True)
def fill7(Z, INF, NT, KP, PID, xlo, xhi, TI, GK, NYK, BASE, off, pos, erep, esb, ek, es):
    P0 = np.empty(5, np.complex128); P1 = np.empty(5, np.complex128); K = np.empty(4)
    for r in range(NT):
        for sb in range(PID.shape[0]):
            Phi = _tkey(Z, INF, r, KP, PID, sb, P0, P1, K)
            if K[0] < xlo or K[0] >= xhi: continue
            c = _cell(K, Phi, xlo, TI, GK, NYK, BASE)
            e = off[c] + pos[c]; pos[c] += 1
            erep[e] = r; esb[e] = sb
            for i in range(4): ek[e, i] = K[i]
            es[e] = min(Phi, 3e38)

NPC = 8
PCB = np.array([300.0, 1e3, 3e3, 1e4, 3e4, 1e5, 1e6, np.inf])     # Phi classes inside a sub-row (narrow K_2 ranges for small Phi)

@njit(cache=True, inline='always')
def _pclass(Phi):
    c = 0
    while c < NPC - 1 and Phi >= PCB[c]: c += 1
    return c

@njit(cache=True, parallel=True)
def pcount7(Z, INF, NT, KP, PID, xlo, xhi, nin):
    """parallel build, pass 1: nin[r] = number of subsets of cover r with K_0 in [xlo, xhi)"""
    for r in prange(NT):
        P0 = np.empty(5, np.complex128); P1 = np.empty(5, np.complex128); K = np.empty(4); m = 0
        for sb in range(PID.shape[0]):
            _tkey(Z, INF, r, KP, PID, sb, P0, P1, K)
            if K[0] >= xlo and K[0] < xhi: m += 1
        nin[r] = m

@njit(cache=True, parallel=True)
def pfill7(Z, INF, NT, KP, PID, xlo, xhi, TI, GK, NYK, BASE, start, cell, erep, esb, ek, es, ck):
    """pass 2: entries of cover r at start[r]..; cell index and bisection key ck (as sort_cells) per entry"""
    for r in prange(NT):
        P0 = np.empty(5, np.complex128); P1 = np.empty(5, np.complex128); K = np.empty(4); e = start[r]
        for sb in range(PID.shape[0]):
            Phi = _tkey(Z, INF, r, KP, PID, sb, P0, P1, K)
            if not (K[0] >= xlo and K[0] < xhi): continue
            k = 0
            while k + 1 < len(GK) and Phi >= TI[k + 1]: k += 1
            cy = np.int64((K[1] + 5.0) / GK[k])
            cell[e] = BASE[k] + np.int64((K[0] - xlo) / GK[k]) * NYK[k] + cy
            gs = GK[k] / NSUB; sub = min(max(np.int64(np.floor((K[1] - (cy * GK[k] - 5.0)) / gs)), 0), NSUB - 1)
            ck[e] = (sub * NPC + _pclass(Phi)) * 16.0 + (K[2] + 5.0)
            erep[e] = r; esb[e] = sb
            for i in range(4): ek[e, i] = K[i]
            es[e] = min(Phi, 3e38)
            e += 1

NSUB = 64

@njit(cache=True)
def sort_cells(off, erep, esb, ek, es, ck, BASE, GK, NYK):
    """entries of each cell sorted by ck = (sub * NPC + Phi class) * 16 + (K_2 + 5), sub = K_1 sub-row of the cell (NSUB per cell); the scan bisects ck per sub-row"""
    tk = 0
    for c in range(len(off) - 1):
        lo = off[c]; hi = off[c + 1]
        if hi == lo: continue
        while c >= BASE[tk + 1]: tk += 1
        cy = (c - BASE[tk]) % NYK[tk]; ylo = cy * GK[tk] - 5.0; gs = GK[tk] / NSUB
        for e in range(lo, hi):
            sub = min(max(np.int64(np.floor((ek[e, 1] - ylo) / gs)), 0), NSUB - 1)
            ck[e] = (sub * NPC + _pclass(es[e])) * 16.0 + (ek[e, 2] + 5.0)
        if hi - lo < 2: continue
        o = np.argsort(ck[lo:hi]) + lo
        r2 = erep[o].copy(); s2 = esb[o].copy(); k2 = ek[o].copy(); e2 = es[o].copy(); c2 = ck[o].copy()
        erep[lo:hi] = r2; esb[lo:hi] = s2; ek[lo:hi] = k2; es[lo:hi] = e2; ck[lo:hi] = c2

@njit(cache=True)
def scan7(f0, f1, subs, perm120, TOL, DEL, EPS4, maxfail, off, erep, esb, ek, es, ck, xlo, xhi, TMAX, GK, NXK, NYK, BASE,
          Z, INF, KP, PID, CLSB, myclass, cap, K2MIN):
    """every (query 5-subset r, table entry) with keys within the window, then the ordering / Moebius pre-filter.
    Returns (r, rep, sb, perm) per survivor, counts, overflow flag."""
    nA = len(f0); nB = Z.shape[1]
    o_r = np.empty(cap, np.int64); o_rep = np.empty(cap, np.int64); o_sb = np.empty(cap, np.int64); o_p = np.empty(cap, np.int64)
    no = 0; cnt = np.zeros(6, np.int64)
    P0 = np.empty(5, np.complex128); P1 = np.empty(5, np.complex128); KX = np.empty(4)
    Q0 = np.empty(5, np.complex128); Q1 = np.empty(5, np.complex128); KY = np.empty(4)
    q0 = np.empty(nB, np.complex128); q1 = np.empty(nB, np.complex128); hitj = np.zeros(nB, np.bool_)
    y = np.empty(5, np.int64); s = np.empty(5, np.int64)
    SVX = np.empty((5, 3)); SVY = np.empty((5, 3)); CM = np.zeros((5, 5), np.bool_)
    for r in range(len(subs)):
        for k in range(5):
            s[k] = subs[r, k]; P0[k] = f0[s[k]]; P1[k] = f1[s[k]]
        SX = _key5s(P0, P1, KX, SVX)
        bad = not (np.isfinite(SX) and np.isfinite(KX[0]) and np.isfinite(KX[1]) and np.isfinite(KX[2]) and np.isfinite(KX[3]))
        if bad: cnt[4] += 1
        for tk in range(len(GK)):
          c0 = KX[0]; c1 = KX[1]
          if TMAX[tk] < 0: continue
          wmax = _win5(SX, TMAX[tk], DEL, EPS4) + 1e-11; G = GK[tk]; NYC = NYK[tk]
          if c0 + wmax < xlo or c0 - wmax >= xhi: continue
          if not (wmax < 20.0): wmax = 20.0          # (also catches nan / inf: then every cell of the tier)
          if not (abs(c0) <= 6.0 and abs(c1) <= 6.0): c0 = 0.0; c1 = 0.0; wmax = 20.0
          cx1 = max(np.int64(np.floor((c0 - wmax - xlo) / G)), 0); cx2 = min(np.int64(np.floor((c0 + wmax - xlo) / G)), NXK[tk] - 1)
          cy1 = max(np.int64(np.floor((c1 - wmax + 5.0) / G)), 0); cy2 = min(np.int64(np.floor((c1 + wmax + 5.0) / G)), NYC - 1)
          if cy1 > cy2: continue
          nyr = cy2 - cy1 + 1
          for ci in range(max(cx2 - cx1 + 1, 0) * nyr):       # one cell at a time (entries are sorted by K_2 within a cell)
            cy = cy1 + ci % nyr; cc = BASE[tk] + (cx1 + ci // nyr) * NYC + cy
            lo0 = off[cc]; hi0 = off[cc + 1]
            if hi0 == lo0: continue
            if hi0 - lo0 > K2MIN:
                gs = G / NSUB; ylo = cy * G - 5.0
                s1 = min(max(np.int64(np.floor((c1 - wmax - ylo) / gs)), 0), NSUB - 1)
                s2 = min(max(np.int64(np.floor((c1 + wmax - ylo) / gs)), 0), NSUB - 1)
                if c0 == 0.0 and c1 == 0.0 and wmax == 20.0: s1 = 0; s2 = NSUB - 1
            else:
                s1 = 0; s2 = 0
            nu = (s2 - s1 + 1) * NPC if hi0 - lo0 > K2MIN else 1
            for iu in range(nu):
              if hi0 - lo0 > K2MIN:
                cz = ck[lo0:hi0]; u = s1 * NPC + iu; base = u * 16.0
                if wmax == 20.0:
                    lo = lo0 + np.searchsorted(cz, base - 0.5); hi = lo0 + np.searchsorted(cz, base + 15.5)
                else:
                    wc = min(wmax, _win5(SX, PCB[u % NPC], DEL, EPS4) + 1e-11)
                    lo = lo0 + np.searchsorted(cz, base + KX[2] + 5.0 - wc); hi = lo0 + np.searchsorted(cz, base + KX[2] + 5.0 + wc, 'right')
              else:
                lo = lo0; hi = hi0
              cnt[0] += hi - lo
              for e in range(lo, hi):
                  w = _win5(SX, es[e] * (1 + 1e-6), DEL, EPS4) + 1e-12
                  if (abs(ek[e, 0] - KX[0]) > w or abs(ek[e, 1] - KX[1]) > w or abs(ek[e, 2] - KX[2]) > w
                          or abs(ek[e, 3] - KX[3]) > w): continue
                  rep = erep[e]
                  if myclass >= 0 and CLSB[rep] == myclass: continue
                  cnt[1] += 1
                  sb = esb[e]
                  for k in range(5):
                      i_ = KP[rep, PID[sb, k]]; Q0[k], Q1[k] = _hp(Z[rep, i_], INF[rep, i_])
                  SY = _key5s(Q0, Q1, KY, SVY)
                  w = _win5(SX, SY, DEL, EPS4)
                  if (abs(KY[0] - KX[0]) > w or abs(KY[1] - KX[1]) > w or abs(KY[2] - KX[2]) > w or abs(KY[3] - KX[3]) > w): continue
                  cnt[2] += 1
                  if w > 1e-9: cnt[5] += 1
                  # the ordering must pair quadruple e of X (without s[e]) with a quadruple of Y of the same J:
                  # |s_e(X) - s_e'(Y)| <= w / 2 for a true match (each is <= delta (S phi)_X,e + delta (S phi)_Y,e')
                  for e1 in range(5):
                      for e2 in range(5):
                          CM[e1, e2] = (abs(SVX[e1, 0] - SVY[e2, 0]) <= w and abs(SVX[e1, 1] - SVY[e2, 1]) <= w
                                        and abs(SVX[e1, 2] - SVY[e2, 2]) <= w)
                  loaded = False
                  for p in range(120):
                      okp = True
                      for k in range(5):
                          if not CM[k, perm120[p, k]]: okp = False; break
                      if not okp: continue
                      if not loaded:
                          for j in range(nB): q0[j], q1[j] = _hp(Z[rep, j], INF[rep, j])
                          loaded = True
                      for k in range(5): y[k] = KP[rep, PID[sb, perm120[p, k]]]
                      ok = True
                      for h in range(2):
                          x0, x1, x2 = _cross4(f0[s[h]], f1[s[h]], f0[s[h + 1]], f1[s[h + 1]], f0[s[h + 2]], f1[s[h + 2]], f0[s[h + 3]], f1[s[h + 3]])
                          y0, y1_, y2 = _cross4(q0[y[h]], q1[y[h]], q0[y[h + 1]], q1[y[h + 1]], q0[y[h + 2]], q1[y[h + 2]], q0[y[h + 3]], q1[y[h + 3]])
                          d = np.sqrt((y0 - x0) ** 2 + (y1_ - x1) ** 2 + (y2 - x2) ** 2)
                          SXq = _cond4(f0[s[h]], f1[s[h]], f0[s[h + 1]], f1[s[h + 1]], f0[s[h + 2]], f1[s[h + 2]], f0[s[h + 3]], f1[s[h + 3]])
                          SYq = _cond4(q0[y[h]], q1[y[h]], q0[y[h + 1]], q1[y[h + 1]], q0[y[h + 2]], q1[y[h + 2]], q0[y[h + 3]], q1[y[h + 3]])
                          win = min(TOL * (SXq + SYq) * min(1.0, max(_kap(x0, x1, x2), _kap(y0, y1_, y2)) / 10 * 1.01 + 1e-12), EPS4)
                          if not d <= win: ok = False; break
                      if not ok: continue
                      cnt[3] += 1
                      a00, a01, a10, a11 = _frame(f0[s[0]], f1[s[0]], f0[s[1]], f1[s[1]], f0[s[2]], f1[s[2]])
                      b00, b01, b10, b11 = _frame(q0[y[0]], q1[y[0]], q0[y[1]], q1[y[1]], q0[y[2]], q1[y[2]])
                      det = a00 * a11 - a01 * a10
                      i00 = a11 / det; i01 = -a01 / det; i10 = -a10 / det; i11 = a00 / det
                      M00 = b00 * i00 + b01 * i10; M01 = b00 * i01 + b01 * i11
                      M10 = b10 * i00 + b11 * i10; M11 = b10 * i01 + b11 * i11
                      fail = 0
                      for j in range(nB): hitj[j] = False
                      for i in range(nA):
                          u0 = M00 * f0[i] + M01 * f1[i]; u1 = M10 * f0[i] + M11 * f1[i]
                          nu = np.sqrt(abs(u0) ** 2 + abs(u1) ** 2)
                          hit = False
                          for j in range(nB):
                              if abs(u0 * q1[j] - u1 * q0[j]) < 1e-4 * nu:
                                  hit = True; hitj[j] = True
                          if not hit:
                              fail += 1
                              if fail > maxfail: break
                      if fail <= maxfail:
                          ncl = nA - fail; ncol = 0
                          for j in range(nB):
                              if hitj[j]: ncol += 1
                          if nA + nB - 2 * min(ncl, ncol) <= 4:
                              if no >= cap: return o_r[:0], o_rep[:0], o_sb[:0], o_p[:0], cnt, True
                              o_r[no] = r; o_rep[no] = rep; o_sb[no] = sb; o_p[no] = p; no += 1
    return o_r[:no], o_rep[:no], o_sb[:no], o_p[:no], cnt, False

@njit(cache=True, parallel=True)
def spread_pos(Z, INF, F, out):
    """out[r] = F positions of cover r chosen greedily: the pair of largest chordal distance, then each time the point
    farthest (largest minimum chordal distance) from those chosen (ties: smallest index)"""
    N, n = Z.shape
    for r in prange(N):
        P0 = np.empty(n, np.complex128); P1 = np.empty(n, np.complex128)
        for k in range(n): P0[k], P1[k] = _hp(Z[r, k], INF[r, k])
        D = np.empty((n, n))
        for i in range(n):
            for j in range(n): D[i, j] = abs(P0[i] * P1[j] - P1[i] * P0[j])
        bi = 0; bj = 1; bd = -1.0
        for i in range(n):
            for j in range(i + 1, n):
                if D[i, j] > bd: bd = D[i, j]; bi = i; bj = j
        used = np.zeros(n, np.bool_); used[bi] = True; used[bj] = True
        md = np.empty(n)
        for k in range(n): md[k] = min(D[k, bi], D[k, bj])
        out[r, 0] = bi; out[r, 1] = bj
        for m in range(2, F):
            best = -1; bv = -1.0
            for k in range(n):
                if not used[k] and md[k] > bv: bv = md[k]; best = k
            used[best] = True; out[r, m] = best
            for k in range(n): md[k] = min(md[k], D[k, best])
