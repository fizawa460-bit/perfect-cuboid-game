"""Compiled kernels of search5.py (numba).

scan():  for one query cover f and one label code, every (query 4-subset, table entry) pair whose cross-ratios meet
         the window, followed by search4's compiled pre-filter (verify_nb.prefilter: 24 orderings of the table
         subset, label test, cross-ratio window (5), Moebius map from three points, count of query points with a
         table point within chordal 1e-4, early exit) and search4's one-to-one bound (7), all in one pass.  The
         table cross-ratio and its condition number S are recomputed from the stored points (the table holds only
         the key, the table cover and the subset index).
selfscan(): the same for the 24 covers U∘f (same source points, labels moved by U): brute force over the few
         subsets, no table.
Window rules, thresholds and the order of the tests are search4's (see search4.py (5)-(7)); what is new is only
where the numbers come from."""
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
def _cross4(a0, a1, b0, b1, c0, c1, d0, d1):
    num = _wedge(a0, a1, c0, c1) * _wedge(b0, b1, d0, d1)
    den = _wedge(a0, a1, d0, d1) * _wedge(b0, b1, c0, c1)
    return _sph(num, den)

@njit(cache=True)
def _cond4(a0, a1, b0, b1, c0, c1, d0, d1):
    return (1.0 / abs(_wedge(a0, a1, b0, b1)) + 1.0 / abs(_wedge(a0, a1, c0, c1)) + 1.0 / abs(_wedge(a0, a1, d0, d1))
            + 1.0 / abs(_wedge(b0, b1, c0, c1)) + 1.0 / abs(_wedge(b0, b1, d0, d1)) + 1.0 / abs(_wedge(c0, c1, d0, d1)))

@njit(cache=True)
def _kap(x, y, z):
    d1 = np.sqrt(x * x + y * y + (z + 1) ** 2); d2 = np.sqrt(x * x + y * y + (z - 1) ** 2); d3 = np.sqrt((x - 1) ** 2 + y * y + z * z)
    d = min(d1, min(d2, d3))
    return min(1.0, 10 * d)

@njit(cache=True)
def _frame(a0, a1, b0, b1, c0, c1):
    det = a0 * b1 - b0 * a1
    l0 = (b1 * c0 - b0 * c1) / det; l1 = (-a1 * c0 + a0 * c1) / det
    return a0 * l0, b0 * l1, a1 * l0, b1 * l1

@njit(cache=True)
def _prefilter_one(f0, f1, flab, s, q0, q1, ql, T, perm24, TOL, EPS4, maxfail, outp, outn):
    """search4/verify_nb.prefilter for one (query subset s, table subset T) pair, plus the one-to-one bound.
    Appends surviving orderings to outp; returns (number appended, number that passed the cross-ratio test)."""
    nA = len(f0); nB = len(q0); na = 0; ncand = 0
    x0, x1, x2 = _cross4(f0[s[0]], f1[s[0]], f0[s[1]], f1[s[1]], f0[s[2]], f1[s[2]], f0[s[3]], f1[s[3]])
    SX = _cond4(f0[s[0]], f1[s[0]], f0[s[1]], f1[s[1]], f0[s[2]], f1[s[2]], f0[s[3]], f1[s[3]]); kx = _kap(x0, x1, x2)
    y = np.empty(4, np.int64); hitj = np.zeros(nB, np.bool_)
    for p in range(24):
        ok = True
        for k in range(4):
            y[k] = T[perm24[p, k]]
            if ql[y[k]] != flab[s[k]]: ok = False; break
        if not ok: continue
        y0, y1_, y2 = _cross4(q0[y[0]], q1[y[0]], q0[y[1]], q1[y[1]], q0[y[2]], q1[y[2]], q0[y[3]], q1[y[3]])
        d = np.sqrt((y0 - x0) ** 2 + (y1_ - x1) ** 2 + (y2 - x2) ** 2)
        SY = _cond4(q0[y[0]], q1[y[0]], q0[y[1]], q1[y[1]], q0[y[2]], q1[y[2]], q0[y[3]], q1[y[3]]); ky = _kap(y0, y1_, y2)
        win = min(TOL * (SX + SY) * min(1.0, max(kx, ky) / 10 * 1.01 + 1e-12), EPS4)
        if not d <= win: continue
        ncand += 1
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
                    hit = True; hitj[j] = True     # (every close table point is marked: needed for the one-to-one bound)
            if not hit:
                fail += 1
                if fail > maxfail: break
        if fail <= maxfail:
            ncl = nA - fail; ncol = 0
            for j in range(nB):
                if hitj[j]: ncol += 1
            if nA + nB - 2 * min(ncl, ncol) <= 4:
                if outn[0] >= len(outp): return -1, ncand          # caller enlarges the buffer and repeats
                outp[outn[0]] = p; outn[0] += 1; na += 1
    return na, ncand

@njit(cache=True)
def scan(f0, f1, flab, subs, perm24, P6, TOL, EPS4, maxfail,
         keys, ete, esb, ntier, tstart, tend, tW, tsmax,
         TREP, TTPV, IMAP, QCLS, SUBB, B0, B1, CLSB, myclass, cap):
    """subs (R, 4): query subsets with the current label code.  Table entries of tier k are keys[tstart[k]:tend[k]]
    (sorted by cell*4 + (y+1), cell = floor((x+1)/tW[k])), ete = table cover, esb = subset index.  Table cover te
    is rep TREP[te] with labelled position map TTPV[te] (IMAP, QCLS, SUBB rows).  Entries whose rep has
    CLSB[rep] == myclass (myclass >= 0) are skipped (f's own Aut(B) class: the self part).
    Returns survivors (subset row, te, sb, perm) and counters [raw entries, window passes, prefilter candidates]."""
    nB = B0.shape[1]
    o_r = np.empty(cap, np.int64); o_te = np.empty(cap, np.int64); o_sb = np.empty(cap, np.int64); o_p = np.empty(cap, np.int64)
    no = 0; cnt = np.zeros(3, np.int64)
    q0 = np.empty(nB, np.complex128); q1 = np.empty(nB, np.complex128); ql = np.empty(nB, np.int64)
    outp = np.empty(24, np.int64); outn = np.zeros(1, np.int64); T = np.empty(4, np.int64)
    for r in range(len(subs)):
        s = subs[r]
        SQ = _cond4(f0[s[0]], f1[s[0]], f0[s[1]], f1[s[1]], f0[s[2]], f1[s[2]], f0[s[3]], f1[s[3]])
        for o in range(6):
            a = s[P6[o, 0]]; b = s[P6[o, 1]]; c = s[P6[o, 2]]; d = s[P6[o, 3]]
            x, yv, z = _cross4(f0[a], f1[a], f0[b], f1[b], f0[c], f1[c], f0[d], f1[d])
            KQ = min(1.0, _kap(x, yv, z) / 10 * 1.01 + 1e-12)
            for k in range(ntier):
                if tend[k] <= tstart[k]: continue
                w = min(TOL * (SQ + tsmax[k]) * KQ, EPS4)
                W = tW[k]
                c1 = int(np.floor((x - w + 1) / W)); c2 = int(np.floor((x + w + 1) / W))
                kk = keys[tstart[k]:tend[k]]
                for cell in range(c1, c2 + 1):
                    lo = np.searchsorted(kk, cell * 4.0 + (yv - w + 1) - 1e-9) + tstart[k]
                    hi = np.searchsorted(kk, cell * 4.0 + (yv + w + 1) + 1e-9, 'right') + tstart[k]
                    cnt[0] += hi - lo
                    for e in range(lo, hi):
                        te = ete[e]; rep = TREP[te]
                        if myclass >= 0 and CLSB[rep] == myclass: continue
                        t = TTPV[te]; sb = esb[e]
                        for m in range(4): T[m] = SUBB[t, sb, m]
                        i0 = IMAP[t, T[0]]; i1 = IMAP[t, T[1]]; i2 = IMAP[t, T[2]]; i3 = IMAP[t, T[3]]
                        tx, ty, tz = _cross4(B0[rep, i0], B1[rep, i0], B0[rep, i1], B1[rep, i1], B0[rep, i2], B1[rep, i2], B0[rep, i3], B1[rep, i3])
                        dd = np.sqrt((tx - x) ** 2 + (ty - yv) ** 2 + (tz - z) ** 2)
                        if not dd <= w: continue          # quick reject (the entry window below is never larger than w for this tier)
                        ST = _cond4(B0[rep, i0], B1[rep, i0], B0[rep, i1], B1[rep, i1], B0[rep, i2], B1[rep, i2], B0[rep, i3], B1[rep, i3])
                        if not dd <= min(TOL * (SQ + ST) * KQ, EPS4): continue
                        cnt[1] += 1
                        for j in range(nB):
                            q0[j] = B0[rep, IMAP[t, j]]; q1[j] = B1[rep, IMAP[t, j]]; ql[j] = QCLS[t, j]
                        outn[0] = 0
                        na, nc = _prefilter_one(f0, f1, flab, s, q0, q1, ql, T, perm24, TOL, EPS4, maxfail, outp, outn)
                        cnt[2] += nc
                        for u in range(outn[0]):
                            if no >= cap: return o_r[:0], o_te[:0], o_sb[:0], o_p[:0], cnt, True
                            o_r[no] = r; o_te[no] = te; o_sb[no] = sb; o_p[no] = outp[u]; no += 1
    return o_r[:no], o_te[:no], o_sb[:no], o_p[:no], cnt, False

@njit(cache=True)
def selfscan(f0, f1, flab, subs, perm24, P6, TOL, EPS4, maxfail, Us, UMAP, UCLS, USUB, cap):
    """Self part: the 'table' is the covers U∘f (u in Us): their odd point list is f's points in the order UMAP[u]
    with class labels UCLS[u]; USUB[u] (nsub, 4) are their key subsets (positions in that list).  Brute force over
    the query subsets subs (all codes) and the key subsets; same window and pre-filter as scan()."""
    nA = len(f0)
    o_r = np.empty(cap, np.int64); o_u = np.empty(cap, np.int64); o_sb = np.empty(cap, np.int64); o_p = np.empty(cap, np.int64)
    no = 0; cnt = np.zeros(3, np.int64)
    q0 = np.empty(nA, np.complex128); q1 = np.empty(nA, np.complex128); ql = np.empty(nA, np.int64)
    outp = np.empty(24, np.int64); outn = np.zeros(1, np.int64); T = np.empty(4, np.int64)
    R = len(subs)
    SQ = np.empty(R); CR = np.empty((R, 6, 3)); KQ = np.empty((R, 6)); CODE = np.empty(R, np.int64)
    for r in range(R):
        s = subs[r]
        SQ[r] = _cond4(f0[s[0]], f1[s[0]], f0[s[1]], f1[s[1]], f0[s[2]], f1[s[2]], f0[s[3]], f1[s[3]])
        for o in range(6):
            a = s[P6[o, 0]]; b = s[P6[o, 1]]; c = s[P6[o, 2]]; d = s[P6[o, 3]]
            x, yv, z = _cross4(f0[a], f1[a], f0[b], f1[b], f0[c], f1[c], f0[d], f1[d])
            CR[r, o, 0] = x; CR[r, o, 1] = yv; CR[r, o, 2] = z
            KQ[r, o] = min(1.0, _kap(x, yv, z) / 10 * 1.01 + 1e-12)
        l = np.sort(flab[s]); CODE[r] = ((l[0] * 3 + l[1]) * 3 + l[2]) * 3 + l[3]
    for ui in range(len(Us)):
        u = Us[ui]
        for j in range(nA):
            q0[j] = f0[UMAP[u, j]]; q1[j] = f1[UMAP[u, j]]; ql[j] = UCLS[u, j]
        for sb in range(USUB.shape[1]):
            for m in range(4): T[m] = USUB[u, sb, m]
            tx, ty, tz = _cross4(q0[T[0]], q1[T[0]], q0[T[1]], q1[T[1]], q0[T[2]], q1[T[2]], q0[T[3]], q1[T[3]])
            ST = _cond4(q0[T[0]], q1[T[0]], q0[T[1]], q1[T[1]], q0[T[2]], q1[T[2]], q0[T[3]], q1[T[3]])
            l0 = ql[T[0]]; l1 = ql[T[1]]; l2 = ql[T[2]]; l3 = ql[T[3]]
            ll = np.sort(np.array([l0, l1, l2, l3])); tcode = ((ll[0] * 3 + ll[1]) * 3 + ll[2]) * 3 + ll[3]
            for r in range(R):
                if CODE[r] != tcode: continue
                for o in range(6):
                    dd = np.sqrt((tx - CR[r, o, 0]) ** 2 + (ty - CR[r, o, 1]) ** 2 + (tz - CR[r, o, 2]) ** 2)
                    if not dd <= min(TOL * (SQ[r] + ST) * KQ[r, o], EPS4): continue
                    cnt[1] += 1
                    outn[0] = 0
                    na, nc = _prefilter_one(f0, f1, flab, subs[r], q0, q1, ql, T, perm24, TOL, EPS4, maxfail, outp, outn)
                    cnt[2] += nc
                    for k in range(outn[0]):
                        if no >= cap: return o_r[:0], o_u[:0], o_sb[:0], o_p[:0], cnt, True
                        o_r[no] = r; o_u[no] = u; o_sb[no] = sb; o_p[no] = outp[k]; no += 1
    return o_r[:no], o_u[:no], o_sb[:no], o_p[:no], cnt, False
