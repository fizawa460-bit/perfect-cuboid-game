"""Compiled kernels of search6.py (numba): scan_nb.py (degree8-20261120) with an exact integer 2-D grid key and
odd points stored affinely (z, inf flag) instead of unit homogeneous pairs.  _prefilter_one / _prefilter_dedupe /
selfscan are scan_nb's, unchanged.  New: _hp (point from z, inf), count_entries / fill_entries (table build for one
label code and one x-slice, all tiers), scan6 (window lookups on the grid).

Original description of scan_nb.py:

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
def _prefilter_dedupe(f0, f1, flab, s, q0, q1, ql, T, perm24, TOL, EPS4, maxfail, outp, outn, seen, nseen):
    """_prefilter_one, but a Moebius map already counted for this table cover (seen[:nseen[0]], normalised by its
    largest entry, equal to 1e-7) is not counted again: the self part meets each map through many quadruples, and
    search4/search5 keep one survivor per (cover, map rounded to 6 digits) anyway."""
    nA = len(f0); nB = len(q0); ncand = 0
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
        mx = M00
        if abs(M01) > abs(mx): mx = M01
        if abs(M10) > abs(mx): mx = M10
        if abs(M11) > abs(mx): mx = M11
        n0 = M00 / mx; n1 = M01 / mx; n2 = M10 / mx; n3 = M11 / mx
        dup = False
        for k in range(nseen[0]):
            if abs(seen[k, 0] - n0) < 1e-7 and abs(seen[k, 1] - n1) < 1e-7 and abs(seen[k, 2] - n2) < 1e-7 and abs(seen[k, 3] - n3) < 1e-7:
                dup = True; break
        if dup: continue
        if nseen[0] < seen.shape[0]:
            seen[nseen[0], 0] = n0; seen[nseen[0], 1] = n1; seen[nseen[0], 2] = n2; seen[nseen[0], 3] = n3; nseen[0] += 1
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
                outp[outn[0]] = p; outn[0] += 1
    return ncand


@njit(cache=True, inline='always')
def _hp(z, inf):
    """unit homogeneous pair of an affine point (inf: the point (1, 0))"""
    if inf: return 1.0 + 0j, 0j
    nz = np.sqrt(1.0 + abs(z) ** 2)
    return z / nz, 1.0 / nz + 0j

@njit(cache=True)
def _entry(Z, INF, rep, IMAP, t, SUBB, sb):
    i0 = IMAP[t, SUBB[t, sb, 0]]; i1 = IMAP[t, SUBB[t, sb, 1]]; i2 = IMAP[t, SUBB[t, sb, 2]]; i3 = IMAP[t, SUBB[t, sb, 3]]
    a0, a1 = _hp(Z[rep, i0], INF[rep, i0]); b0, b1 = _hp(Z[rep, i1], INF[rep, i1])
    c0, c1 = _hp(Z[rep, i2], INF[rep, i2]); d0, d1 = _hp(Z[rep, i3], INF[rep, i3])
    x, y, zz = _cross4(a0, a1, b0, b1, c0, c1, d0, d1)
    S = _cond4(a0, a1, b0, b1, c0, c1, d0, d1)
    return x, y, zz, S

@njit(cache=True)
def _tier(S, TIERS):
    k = 0
    while k + 2 < len(TIERS) and S >= TIERS[k + 1]: k += 1
    return k

@njit(cache=True)
def count_entries(TREP, TTPV, IMAP, SUBB, SCODE, Z, INF, code, xlo, xhi, TIERS, cnt):
    """cnt[k] += number of table entries of label code `code`, tier k, with x in [xlo, xhi)"""
    nsub = SUBB.shape[1]
    for te in range(len(TREP)):
        t = TTPV[te]; rep = TREP[te]
        for sb in range(nsub):
            if SCODE[t, sb] != code: continue
            x, y, zz, S = _entry(Z, INF, rep, IMAP, t, SUBB, sb)
            if x < xlo or x >= xhi: continue
            cnt[_tier(S, TIERS)] += 1

@njit(cache=True)
def fill_entries(TREP, TTPV, IMAP, SUBB, SCODE, Z, INF, code, xlo, xhi, TIERS, W, NY, start, pos, key, ete, esb):
    """write the entries counted by count_entries: tier k goes to key[start[k] + ...]; key = cx * NY + cy with
    cx = floor((x + 1) / W[k]), cy = floor((y + 1) / W[k]) (exact integers, no rounding slack needed)"""
    nsub = SUBB.shape[1]
    for te in range(len(TREP)):
        t = TTPV[te]; rep = TREP[te]
        for sb in range(nsub):
            if SCODE[t, sb] != code: continue
            x, y, zz, S = _entry(Z, INF, rep, IMAP, t, SUBB, sb)
            if x < xlo or x >= xhi: continue
            k = _tier(S, TIERS); e = start[k] + pos[k]; pos[k] += 1
            key[e] = np.int64(np.floor((x + 1) / W[k])) * NY[k] + np.int64(np.floor((y + 1) / W[k]))
            ete[e] = te; esb[e] = sb

@njit(cache=True)
def scan6(f0, f1, flab, subs, perm24, P6, TOL, EPS4, maxfail,
          keys, ete, esb, ntier, tstart, tend, tW, NY, tsmax, xlo, xhi,
          TREP, TTPV, IMAP, QCLS, SUBB, Z, INF, CLSB, myclass, cap):
    """scan() of scan_nb on the integer grid: for each query subset ordering with x within the slice (+ window), the
    cells cx in [floor((x - w + 1)/W), floor((x + w + 1)/W)] are looked up with cy in the same range (one contiguous
    key range per cx); when that is more than 64 cells wide, the whole x-slab is scanned instead.  Then the same
    exact window test, pre-filter and one-to-one bound as scan()."""
    nB = Z.shape[1]
    o_r = np.empty(cap, np.int64); o_te = np.empty(cap, np.int64); o_sb = np.empty(cap, np.int64); o_p = np.empty(cap, np.int64)
    no = 0; cnt = np.zeros(8, np.int64)
    q0 = np.empty(nB, np.complex128); q1 = np.empty(nB, np.complex128); ql = np.empty(nB, np.int64)
    outp = np.empty(24, np.int64); outn = np.zeros(1, np.int64); T = np.empty(4, np.int64)
    for r in range(len(subs)):
        s = subs[r]
        SQ = _cond4(f0[s[0]], f1[s[0]], f0[s[1]], f1[s[1]], f0[s[2]], f1[s[2]], f0[s[3]], f1[s[3]])
        for o in range(6):
            a = s[P6[o, 0]]; b = s[P6[o, 1]]; c = s[P6[o, 2]]; d = s[P6[o, 3]]
            x, yv, z = _cross4(f0[a], f1[a], f0[b], f1[b], f0[c], f1[c], f0[d], f1[d])
            KQ = min(1.0, _kap(x, yv, z) / 10 * 1.01 + 1e-12)
            wmax = min(TOL * (SQ + tsmax[ntier - 1]) * KQ, EPS4)
            if x + wmax < xlo or x - wmax >= xhi: continue
            for k in range(ntier):
                if tend[k] <= tstart[k]: continue
                w = min(TOL * (SQ + tsmax[k]) * KQ, EPS4)
                Wk = tW[k]; NYk = NY[k]
                c1 = np.int64(np.floor((x - w - 1e-12 + 1) / Wk)); c2 = np.int64(np.floor((x + w + 1e-12 + 1) / Wk))
                y1 = np.int64(np.floor((yv - w - 1e-12 + 1) / Wk)); y2 = np.int64(np.floor((yv + w + 1e-12 + 1) / Wk))
                kk = keys[tstart[k]:tend[k]]
                if c2 - c1 > 64:
                    ranges_lo = np.searchsorted(kk, c1 * NYk) + tstart[k]; ranges_hi = np.searchsorted(kk, (c2 + 1) * NYk) + tstart[k]
                    nr = 1
                else:
                    nr = c2 - c1 + 1; ranges_lo = 0; ranges_hi = 0
                for ci in range(nr):
                    if c2 - c1 > 64:
                        lo = ranges_lo; hi = ranges_hi
                    else:
                        cell = c1 + ci
                        lo = np.searchsorted(kk, cell * NYk + y1) + tstart[k]
                        hi = np.searchsorted(kk, cell * NYk + y2, 'right') + tstart[k]
                    cnt[0] += hi - lo
                    if c2 - c1 > 64: cnt[4] += hi - lo
                    else: cnt[3] += hi - lo
                    cnt[5 + min(k, 2)] += hi - lo
                    for e in range(lo, hi):
                        if c2 - c1 > 64:
                            cy = keys[e] % NYk
                            if cy < y1 or cy > y2: continue
                        te = ete[e]; rep = TREP[te]
                        if myclass >= 0 and CLSB[rep] == myclass: continue
                        t = TTPV[te]; sb = esb[e]
                        for m in range(4): T[m] = SUBB[t, sb, m]
                        tx, ty, tz, ST = _entry(Z, INF, rep, IMAP, t, SUBB, sb)
                        dd = np.sqrt((tx - x) ** 2 + (ty - yv) ** 2 + (tz - z) ** 2)
                        if not dd <= w: continue
                        if not dd <= min(TOL * (SQ + ST) * KQ, EPS4): continue
                        cnt[1] += 1
                        for j in range(nB):
                            q0[j], q1[j] = _hp(Z[rep, IMAP[t, j]], INF[rep, IMAP[t, j]]); ql[j] = QCLS[t, j]
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
    ORD = np.argsort(CODE, kind='mergesort'); CODES_S = CODE[ORD]
    seen = np.empty((4096, 4), np.complex128); nseen = np.zeros(1, np.int64)
    for ui in range(len(Us)):
        u = Us[ui]; nseen[0] = 0
        for j in range(nA):
            q0[j] = f0[UMAP[u, j]]; q1[j] = f1[UMAP[u, j]]; ql[j] = UCLS[u, j]
        for sb in range(USUB.shape[1]):
            for m in range(4): T[m] = USUB[u, sb, m]
            tx, ty, tz = _cross4(q0[T[0]], q1[T[0]], q0[T[1]], q1[T[1]], q0[T[2]], q1[T[2]], q0[T[3]], q1[T[3]])
            ST = _cond4(q0[T[0]], q1[T[0]], q0[T[1]], q1[T[1]], q0[T[2]], q1[T[2]], q0[T[3]], q1[T[3]])
            l0 = ql[T[0]]; l1 = ql[T[1]]; l2 = ql[T[2]]; l3 = ql[T[3]]
            ll = np.sort(np.array([l0, l1, l2, l3])); tcode = ((ll[0] * 3 + ll[1]) * 3 + ll[2]) * 3 + ll[3]
            lo = np.searchsorted(CODES_S, tcode); hi = np.searchsorted(CODES_S, tcode, 'right')
            for rr in range(lo, hi):
                r = ORD[rr]
                for o in range(6):
                    dd = np.sqrt((tx - CR[r, o, 0]) ** 2 + (ty - CR[r, o, 1]) ** 2 + (tz - CR[r, o, 2]) ** 2)
                    if not dd <= min(TOL * (SQ[r] + ST) * KQ[r, o], EPS4): continue
                    cnt[1] += 1
                    outn[0] = 0
                    nc = _prefilter_dedupe(f0, f1, flab, subs[r], q0, q1, ql, T, perm24, TOL, EPS4, maxfail, outp, outn, seen, nseen)
                    cnt[2] += nc
                    for k in range(outn[0]):
                        if no >= cap: return o_r[:0], o_u[:0], o_sb[:0], o_p[:0], cnt, True
                        o_r[no] = r; o_u[no] = u; o_sb[no] = sb; o_p[no] = outp[k]; no += 1
    return o_r[:no], o_u[:no], o_sb[:no], o_p[:no], cnt, False
