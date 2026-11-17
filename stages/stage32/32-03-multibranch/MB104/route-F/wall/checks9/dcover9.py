"""checks9 / dcover9.py -- double covers, composites and the E14 Proposition C families (mpmath, dps 50).

Part 1 (Proposition C families): P = L_n(t^2 + c) and Q = -P (n = 1, 2; c = 2, 1/3 + i/2). The defect points
  (critical points with value outside B, or local degree >= 3) of P and Q coincide: both are {t = 0}.
  Any pair (P, h o P), h an octahedral rotation, has equal defect sets (h preserves B).
Part 2 (double cover through two defects of a mixed pair): for every degree-2 record of type (2, 2), h = 2 found by
  census9, and every x in O(p) \\ O(q'), y in O(q') \\ O(p), pi = the double cover branched at x, y (no type (1,1)
  pair is known, so the mechanism is checked on these records; it does not use the labels).
  Checked: P = p o pi and Q = q' o pi have slack 1 each (E14 slack (|O| - 2 deg - 4)/2), the defect of P is the
  single point over y and the defect of Q the single point over x (distinct), the point over x is a critical point
  of P over B and the point over y one of Q, and (P, Q) has degree 2 onto its image (it factors through pi).
Part 3 (composite lemma): r = double cover branched at two points c1, c2 of O(p0) n O(q0) of a degree-2 record
  (p0, q0) of type (m1, m2, h0). Then p0 o r, q0 o r have slack 0, type (2 m1, 2 m2), h = 2 (h0 - #(H0 n {c1, c2})),
  and degree 2 onto the image. Negative control: a branch point outside O(p0) n O(q0) gives slack > 0.
Part 4 ((t^2, t^2 + t^3)): both maps are critical at t = 0, yet the pair is birational (degree 1 onto the image).
  So a common critical point does not give a common right factor; the composite lemma uses Lueroth instead.
usage (from the repository root):  python3 -I stages/stage32/32-03-multibranch/MB104/route-F/wall/checks9/dcover9.py
"""
import sys, os, itertools, importlib.util, io, contextlib
sys.dont_write_bytecode = True
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("census9", os.path.join(HERE, "census9.py"))
C9 = importlib.util.module_from_spec(spec); spec.loader.exec_module(C9)
mp.mp.dps = 50
BV, LAB, chord, mob = C9.BV, C9.LAB, C9.chord, C9.mob
EPS = mp.mpf(10) ** -25
ok = True


# ---------- polynomials (low -> high, mpc) ----------
def trim(a):
    a = list(a)
    while len(a) > 1 and abs(a[-1]) < mp.mpf(10) ** -40: a.pop()
    return a
def padd(a, b):
    n = max(len(a), len(b)); return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]
def pmul(a, b):
    r = [mp.mpc(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += x * y
    return r
def psc(c, a): return [c * x for x in a]
def ppow(a, k):
    r = [mp.mpc(1)]
    for _ in range(k): r = pmul(r, a)
    return r
def pder(a): return [i * a[i] for i in range(1, len(a))] or [mp.mpc(0)]
def peval(a, z): return mp.polyval(list(reversed(a)), z)


def compose(P, Q, A, Bp, n):
    """(P/Q) o (A/Bp), P, Q of formal degree n."""
    num = [mp.mpc(0)]; den = [mp.mpc(0)]
    for k in range(n + 1):
        t = pmul(ppow(A, k), ppow(Bp, n - k))
        if k < len(P): num = padd(num, psc(P[k], t))
        if k < len(Q): den = padd(den, psc(Q[k], t))
    return trim(num), trim(den)


def val(P, Q, z):
    if z is None:
        dP, dQ = len(trim(P)) - 1, len(trim(Q)) - 1
        if dP > dQ: return None
        return trim(P)[-1] / trim(Q)[-1] if dP == dQ else mp.mpc(0)
    q = peval(Q, z)
    return None if abs(q) < mp.mpf(10) ** -35 else peval(P, z) / q


def roots_mult(F):
    F = trim(F)
    if len(F) == 1: return []
    r = mp.polyroots(list(reversed(F)), maxsteps=600, extraprec=300)
    out, used = [], [False] * len(r)
    for i in range(len(r)):
        if used[i]: continue
        g = [j for j in range(i, len(r)) if not used[j] and abs(r[i] - r[j]) < mp.mpf(10) ** -8]
        for j in g: used[j] = True
        out.append((sum(r[j] for j in g) / len(g), len(g)))
    return out


def bdata(P, Q):
    """degree, odd set (point, label index), defect points, critical points over B (all finite or None = oo)."""
    n = max(len(trim(P)), len(trim(Q))) - 1
    pre = []
    for k, bv in enumerate(BV):
        F = trim(list(Q) if bv is None else padd(P, psc(-bv, Q)))
        for z, m in roots_mult(F): pre.append((z, k, m))
        minf = n - (len(F) - 1)
        if minf: pre.append((None, k, minf))
    O = [(z, k) for z, k, m in pre if m == 1]
    critB = [(z, k, m) for z, k, m in pre if m >= 2]
    W = trim(padd(pmul(pder(P), Q), psc(-1, pmul(P, pder(Q)))))
    wr = roots_mult(W)
    winf = (2 * n - 2) - (len(W) - 1)                    # critical order at oo
    crit = list(wr) + ([(None, winf)] if winf > 0 else [])
    defects = []
    for z, m in crit:
        v = val(P, Q, z)
        inB = any(chord(v, b) < EPS for b in BV)
        if (not inB) or m >= 2: defects.append(z)
    slack = mp.mpf(len(O) - 2 * n - 4) / 2
    return dict(n=n, O=O, critB=critB, defects=defects, slack=slack, crit=crit)


def same_pts(A, Bs):
    return len(A) == len(Bs) and all(min(chord(a, b) for b in Bs) < EPS for a in A)


def onto_degree(P1, Q1, P2, Q2):
    t0 = mp.mpc(0.123, 0.456); v0 = val(P1, Q1, t0); w0 = val(P2, Q2, t0)
    fib = roots_mult(padd(P1, psc(-v0, Q1)))
    return sum(m for t, m in fib if chord(val(P2, Q2, t), w0) < mp.mpf(10) ** -20)


def dcover(x, y):
    """pi(s) = M(s^2), M(0) = x, M(oo) = y (finite x, y): returns (A, Bp) with pi = A / Bp."""
    return [mp.mpc(x), 0, -mp.mpc(y)], [mp.mpc(1), 0, mp.mpc(-1)]   # (x - y s^2)/(1 - s^2): M(1) = oo


# ---------- Part 1 ----------
print("Part 1: E14 Proposition C families (L_n(t^2 + c), -L_n(t^2 + c))")
LP, LQ = [mp.mpc(-1), 0, mp.mpc(1)], [mp.mpc(0), mp.mpc(0, 2)]
for c in (mp.mpc(2), mp.mpc(mp.mpf(1) / 3, mp.mpf(1) / 2)):
    P, Q = [c, 0, mp.mpc(1)], [mp.mpc(1)]
    for n in (1, 2):
        P, Q = compose(LP, LQ, P, Q, 2)
        d1 = bdata(P, Q); d2 = bdata(psc(-1, P), Q)
        same = same_pts(d1["defects"], d2["defects"]) and same_pts(d2["defects"], d1["defects"])
        at0 = len(d1["defects"]) == 1 and d1["defects"][0] is not None and abs(d1["defects"][0]) < EPS
        print("  c = %s, n = %d: degree %d, slacks (%s, %s), defects of P %s, of -P %s, equal: %s" %
              (mp.nstr(c, 4), n, d1["n"], d1["slack"], d2["slack"], [mp.nstr(z, 5) for z in d1["defects"]],
               [mp.nstr(z, 5) for z in d2["defects"]], same))
        ok &= same and at0 and d1["slack"] == 1 and d2["slack"] == 1


# ---------- census records of degree 2 ----------
with contextlib.redirect_stdout(io.StringIO()):
    M2 = C9.load_maps(2, None)
    recs = C9.search(M2, M2, 2, 2)
near = [r for r in recs if (r["m1"], r["m2"], r["h"]) == (2, 2, 2)]
print("degree-2 records of type (2,2), h = 2 from census9: %d" % len(near))


def split_points(r):
    p, q, M = r["p"], r["q"], r["M"]
    TO = [(mob(M, z), k) for z, k in p.O]
    xs, ys, common = [], [], []
    for (w, k), (z, _) in zip(TO, p.O):
        d, jj = min((chord(w, u), jj) for jj, (u, kk) in enumerate(q.O))
        if d < EPS: common.append((w, k, q.O[jj][1]))
        else: xs.append((w, k))
    for u, k2 in q.O:
        if min(chord(u, w) for w, _ in TO) >= EPS: ys.append((u, k2))
    return xs, ys, common      # all in the source coordinate of q (q' = q o T, points mapped by T)


def pq_in_qsource(r):
    """p o T^{-1} and q as polynomial pairs in the source coordinate of q."""
    p, q, M = r["p"], r["q"], r["M"]
    Mi = mp.inverse(M)
    A, Bp = [Mi[0, 1], Mi[0, 0]], [Mi[1, 1], Mi[1, 0]]
    P1, Q1 = compose(p.P, p.Q, A, Bp, p.n)
    return (P1, Q1), (list(q.P), list(q.Q))


# ---------- Part 2 ----------
print("Part 2: double cover branched at x in O(p)\\O(q'), y in O(q')\\O(p)")
n2 = same_label = 0
for r in near[:24]:
    xs, ys, common = split_points(r)
    (P1, Q1), (P2, Q2) = pq_in_qsource(r)
    for (x, kx), (y, ky) in itertools.product(xs, ys):
        if x is None or y is None: continue
        same_label += LAB[kx] == LAB[ky]
        A, Bp = dcover(x, y)
        PP = compose(P1, Q1, A, Bp, 2); QQ = compose(P2, Q2, A, Bp, 2)
        dP, dQ = bdata(*PP), bdata(*QQ)
        defP_inf = len(dP["defects"]) == 1 and (dP["defects"][0] is None or abs(dP["defects"][0]) > 1e20)
        defQ_0 = len(dQ["defects"]) == 1 and dQ["defects"][0] is not None and abs(dQ["defects"][0]) < EPS
        crit0_P = any(z is not None and abs(z) < EPS and m == 2 for z, k, m in dP["critB"])
        critinf_Q = any(z is None and m == 2 for z, k, m in dQ["critB"])
        deg = onto_degree(*PP, *QQ)
        good = dP["slack"] == 1 and dQ["slack"] == 1 and defP_inf and defQ_0 and crit0_P and critinf_Q and deg == 2
        ok &= good; n2 += 1
        if n2 <= 3 or not good:
            print("  slacks (%s, %s); defect of P at s = oo: %s; defect of Q at s = 0: %s; s = 0 critical for P over B: %s;"
                  " s = oo critical for Q over B: %s; degree onto image %d" % (dP["slack"], dQ["slack"], defP_inf, defQ_0,
                                                                               crit0_P, critinf_Q, deg))
print("  configurations checked: %d (x, y of the same label: %d; the local statement does not use labels)" % (n2, same_label))
ok &= n2 > 0


# ---------- Part 3 ----------
print("Part 3: composite with a double cover branched in O(p0) n O(q0)")
n3 = 0
for r in near[:12]:
    xs, ys, common = split_points(r)
    (P1, Q1), (P2, Q2) = pq_in_qsource(r)
    H0 = [i for i, (w, k1, k2) in enumerate(common) if LAB[k1] != LAB[k2]]
    for i1, i2 in itertools.combinations(range(len(common)), 2):
        A, Bp = dcover(common[i1][0], common[i2][0])
        PP = compose(P1, Q1, A, Bp, 2); QQ = compose(P2, Q2, A, Bp, 2)
        dP, dQ = bdata(*PP), bdata(*QQ)
        # type of (PP, QQ): compare odd sets with labels
        cm = [(z, k) for z, k in dP["O"] for u, k2 in dQ["O"] if chord(z, u) < EPS and LAB[k] == LAB[k2]]
        ch = [(z, k) for z, k in dP["O"] for u, k2 in dQ["O"] if chord(z, u) < EPS and LAB[k] != LAB[k2]]
        m1 = len(dP["O"]) - len(cm) - len(ch); m2 = len(dQ["O"]) - len(cm) - len(ch)
        hexp = 2 * (len(H0) - len([i for i in (i1, i2) if i in H0]))
        deg = onto_degree(*PP, *QQ)
        good = (dP["slack"] == 0 and dQ["slack"] == 0 and not dP["defects"] and not dQ["defects"]
                and (m1, m2) == (2 * r["m1"], 2 * r["m2"]) and len(ch) == hexp and deg == 2)
        ok &= good; n3 += 1
        if n3 <= 3 or not good:
            print("  slacks (%s, %s), type (%d, %d), h = %d (expected %d), degree onto image %d" %
                  (dP["slack"], dQ["slack"], m1, m2, len(ch), hexp, deg))
    # negative control: one branch point outside O(p0) n O(q0)
    z_out = mp.mpc(0.3711, -0.2219)
    A, Bp = dcover(common[0][0], z_out)
    dP = bdata(*compose(P1, Q1, A, Bp, 2))
    ok &= dP["slack"] > 0
print("  composites checked: %d; negative control (branch point outside the common set) gives slack > 0" % n3)
ok &= n3 > 0


# ---------- Part 4 ----------
print("Part 4: (t^2, t^2 + t^3)")
P1, Q1 = [mp.mpc(0), 0, mp.mpc(1)], [mp.mpc(1)]
P2, Q2 = [mp.mpc(0), 0, mp.mpc(1), mp.mpc(1)], [mp.mpc(1)]
d4 = onto_degree(P1, Q1, P2, Q2)
c1 = abs(peval(pder(P1), 0)) < EPS; c2 = abs(peval(pder(P2), 0)) < EPS
print("  both critical at t = 0: %s; degree onto the image: %d (birational)" % (c1 and c2, d4))
ok &= c1 and c2 and d4 == 1
print("PASS" if ok else "FAIL")
