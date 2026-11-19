"""Compiled pre-filter for search4.py (numba).  For every (query 4-subset R, table entry) pair that passed the key
window it does exactly what search3/search4 do in numpy, in the same order, and stops early:
  for each of the 24 orderings of the table 4-subset: same labels?  cross-ratio within the window WIN (search4 (5))?
  Möbius map M from the first three points (mob3v), images of all nA query points, and the count nclose of query
  points whose image has a table point at chordal distance < 1e-4 (the same 'close' test as search3's skip rule).
It returns only the candidates with nA + nB - 2 nclose <= 4 (a necessary condition for |Omega| <= 4; search3 drops all
others as '>4(skipped)' or records them with |Omega| > 4), and stops counting as soon as too many query points are
unmatched.  The survivors then go through the unchanged numpy/40-digit code of search4."""
import numpy as np
from numba import njit

@njit(cache=True, inline='always')
def _wedge(a0, a1, b0, b1):
    return a0 * b1 - a1 * b0

@njit(cache=True)
def _sph(num, den):
    d = abs(num) ** 2 + abs(den) ** 2
    z = 2 * num * np.conj(den) / d
    return z.real, z.imag, (abs(num) ** 2 - abs(den) ** 2) / d

@njit(cache=True)
def _cross(P0, P1, i0, i1, i2, i3):
    num = _wedge(P0[i0], P1[i0], P0[i2], P1[i2]) * _wedge(P0[i1], P1[i1], P0[i3], P1[i3])
    den = _wedge(P0[i0], P1[i0], P0[i3], P1[i3]) * _wedge(P0[i1], P1[i1], P0[i2], P1[i2])
    return _sph(num, den)

@njit(cache=True)
def _condS(P0, P1, idx):
    t = 0.0
    for a in range(4):
        for b in range(a + 1, 4):
            t += 1.0 / abs(_wedge(P0[idx[a]], P1[idx[a]], P0[idx[b]], P1[idx[b]]))
    return t

@njit(cache=True)
def _kap(x, y, z):
    # search3 kappa(): min(1, 10 * distance to the nearest of (0,0,-1), (0,0,1), (1,0,0))
    d1 = np.sqrt(x * x + y * y + (z + 1) ** 2); d2 = np.sqrt(x * x + y * y + (z - 1) ** 2); d3 = np.sqrt((x - 1) ** 2 + y * y + z * z)
    d = min(d1, min(d2, d3))
    return min(1.0, 10 * d)

@njit(cache=True)
def _frame(a0, a1, b0, b1, c0, c1):
    # columns a, b scaled by l with l0 a + l1 b = c
    det = a0 * b1 - b0 * a1
    l0 = (b1 * c0 - b0 * c1) / det; l1 = (-a1 * c0 + a0 * c1) / det
    return a0 * l0, b0 * l1, a1 * l0, b1 * l1     # matrix [[m00, m01], [m10, m11]]

@njit(cache=True)
def prefilter(f0, f1, flab, subA, R, QI, T, QP0, QP1, QL, perm24, TOL, EPS4, nB, maxfail):
    """f0, f1: query points (unit homogeneous); R: query subset index; QI: table cover; T: table 4-subset (sorted).
    Returns (pair index, perm index) of the survivors and the number of candidates that passed the cross-ratio test."""
    m = len(R); nA = len(f0)
    outc = np.empty(m * 2 + 16, np.int64); outp = np.empty(m * 2 + 16, np.int64); no = 0; ncand = 0
    for c in range(m):
        s = subA[R[c]]; qi = QI[c]
        q0 = QP0[qi]; q1 = QP1[qi]; ql = QL[qi]
        x0, x1, x2 = _cross(f0, f1, s[0], s[1], s[2], s[3])
        SX = _condS(f0, f1, s); kx = _kap(x0, x1, x2)
        for p in range(24):
            y = np.empty(4, np.int64)
            ok = True
            for k in range(4):
                y[k] = T[c, perm24[p, k]]
                if ql[y[k]] != flab[s[k]]: ok = False; break
            if not ok: continue
            y0, y1_, y2 = _cross(q0, q1, y[0], y[1], y[2], y[3])
            d = np.sqrt((y0 - x0) ** 2 + (y1_ - x1) ** 2 + (y2 - x2) ** 2)
            SY = _condS(q0, q1, y); ky = _kap(y0, y1_, y2)
            win = min(TOL * (SX + SY) * min(1.0, max(kx, ky) / 10 * 1.01 + 1e-12), EPS4)
            if not d <= win: continue
            ncand += 1
            # M = frame(Y) @ inv(frame(X))
            a00, a01, a10, a11 = _frame(f0[s[0]], f1[s[0]], f0[s[1]], f1[s[1]], f0[s[2]], f1[s[2]])
            b00, b01, b10, b11 = _frame(q0[y[0]], q1[y[0]], q0[y[1]], q1[y[1]], q0[y[2]], q1[y[2]])
            det = a00 * a11 - a01 * a10
            i00 = a11 / det; i01 = -a01 / det; i10 = -a10 / det; i11 = a00 / det
            M00 = b00 * i00 + b01 * i10; M01 = b00 * i01 + b01 * i11
            M10 = b10 * i00 + b11 * i10; M11 = b10 * i01 + b11 * i11
            fail = 0
            for i in range(nA):
                u0 = M00 * f0[i] + M01 * f1[i]; u1 = M10 * f0[i] + M11 * f1[i]
                nu = np.sqrt(abs(u0) ** 2 + abs(u1) ** 2)
                hit = False
                for j in range(nB):
                    if abs(u0 * q1[j] - u1 * q0[j]) < 1e-4 * nu:     # chordal distance < 1e-4 (q points are unit vectors)
                        hit = True; break
                if not hit:
                    fail += 1
                    if fail > maxfail: break
            if fail <= maxfail:
                if no >= len(outc):
                    outc = np.concatenate((outc, np.empty(len(outc), np.int64))); outp = np.concatenate((outp, np.empty(len(outp), np.int64)))
                outc[no] = c; outp[no] = p; no += 1
    return outc[:no], outp[:no], ncand

@njit(cache=True)
def self_filter(f0, f1, XI, YI, maxfail):
    """Self part: M maps the ordered quadruple XI[c] of f onto the quadruple YI[c] of f (first three points, mob3v).
    True where at most maxfail points of f have no point of f within chordal distance 1e-4 of their image
    (search3 keeps exactly these: nA + nB - 2 nclose <= 4)."""
    m = len(XI); nA = len(f0); out = np.zeros(m, np.bool_)
    for c in range(m):
        s = XI[c]; y = YI[c]
        a00, a01, a10, a11 = _frame(f0[s[0]], f1[s[0]], f0[s[1]], f1[s[1]], f0[s[2]], f1[s[2]])
        b00, b01, b10, b11 = _frame(f0[y[0]], f1[y[0]], f0[y[1]], f1[y[1]], f0[y[2]], f1[y[2]])
        det = a00 * a11 - a01 * a10
        i00 = a11 / det; i01 = -a01 / det; i10 = -a10 / det; i11 = a00 / det
        M00 = b00 * i00 + b01 * i10; M01 = b00 * i01 + b01 * i11
        M10 = b10 * i00 + b11 * i10; M11 = b10 * i01 + b11 * i11
        fail = 0
        for i in range(nA):
            u0 = M00 * f0[i] + M01 * f1[i]; u1 = M10 * f0[i] + M11 * f1[i]
            nu = np.sqrt(abs(u0) ** 2 + abs(u1) ** 2)
            hit = False
            for j in range(nA):
                if abs(u0 * f1[j] - u1 * f0[j]) < 1e-4 * nu:
                    hit = True; break
            if not hit:
                fail += 1
                if fail > maxfail: break
        out[c] = fail <= maxfail
    return out

