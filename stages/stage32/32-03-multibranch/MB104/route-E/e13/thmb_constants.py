"""E13 Theorem B constants (floating point unless stated; candidate spectrum and degeneracy tests are exact).
- spectrum: |tr| = 2cosh d for a product of two elliptic involutions of Gamma_0 lies in 2 + 2Z[sqrt2] with
  conjugate in [-2, 2] (Lemma 1(b), (b')); we list ALL such candidates up to a length (a superset of what occurs);
- triangles x, y, z with d(x,y), d(x,z) <= l0 and d(y,z) <= 2 l0, sides from the candidate spectrum; exact test of
  degeneracy (collinearity) in Q(sqrt2); width w = min over geodesics L of max_j d(p_j, L), numerically;
- Delta(R, l0) (Step B1) and eps(R, l0) (Step B2); R_B(l0) = least R with Delta < 2 and eps < 2 w_min.
Run from the repository root: python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e13/thmb_constants.py [L]"""
import sys, math
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
S2 = math.sqrt(2)
L0 = float(sys.argv[1]) if len(sys.argv) > 1 else 3.2   # the star radius L (= 2 l0 in Theorem B)
def spectrum(dmax):
    out = []                                   # T/2 = cosh d = 1 + m + n sqrt2 as exact pair (1+m, n)
    # m + n sqrt2 <= cosh(dmax) and m >= n sqrt2 - 2 force n <= (cosh(dmax) + 2)/(2 sqrt2); n < 0 is impossible
    nmax = int((math.cosh(dmax) + 2) / (2 * S2)) + 2
    for n in range(0, nmax + 1):
        for m in range(math.floor(n * S2 - 2) - 1, math.ceil(n * S2) + 2):
            if not (-2 <= m - n * S2 <= 0) or m + n * S2 <= 0: continue
            c = 1 + m + n * S2
            if c <= math.cosh(dmax) + 1e-12: out.append(((1 + m, n), math.acosh(c)))
    return sorted(set(out), key=lambda z: z[1])
def kmul(a, b): return (a[0] * b[0] + 2 * a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def ksub(a, b): return (a[0] - b[0], a[1] - b[1])
def degenerate(c1, c2, c3):                    # exact: (c3 - c1 c2)^2 == (c1^2 - 1)(c2^2 - 1)  <=> collinear
    lhs = kmul(ksub(c3, kmul(c1, c2)), ksub(c3, kmul(c1, c2)))
    rhs = kmul(ksub(kmul(c1, c1), (1, 0)), ksub(kmul(c2, c2), (1, 0)))
    return lhs == rhs
def hyp(d, th): return (math.cosh(d), math.sinh(d) * math.cos(th), math.sinh(d) * math.sin(th))
def mink(a, b): return -a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
def width(P):
    best = 1e9
    def f(t, ph):
        n = (math.sinh(t), math.cosh(t) * math.cos(ph), math.cosh(t) * math.sin(ph))
        return max(abs(mink(p, n)) for p in P)
    grid = [(t / 10.0, 2 * math.pi * k / 360) for t in range(-60, 61) for k in range(360)]
    cand = sorted(grid, key=lambda z: f(*z))[:20]
    for t, ph in cand:
        st, sp = 0.05, 2 * math.pi / 360
        v = f(t, ph)
        for _ in range(200):
            moved = False
            for dt, dp in ((st, 0), (-st, 0), (0, sp), (0, -sp)):
                w = f(t + dt, ph + dp)
                if w < v: t, ph, v, moved = t + dt, ph + dp, w, True
            if not moved:
                st /= 2; sp /= 2
                if st < 1e-10: break
        best = min(best, v)
    return math.asinh(best)
spec1 = [s for s in spectrum(L0)]
spec3 = spectrum(2 * L0)
print("L = %.3f; candidate sides <= L:" % L0, [round(d, 4) for _, d in spec1])
print("candidate third sides <= 2L:", len(spec3))
wmin, worst, ndeg, ntri = 1e9, None, 0, 0
for i, (c1, d1) in enumerate(spec1):
    for (c2, d2) in spec1[i:]:
        for (c3, d3) in spec3:
            if d3 > d1 + d2 + 1e-9 or d3 < abs(d1 - d2) - 1e-9: continue
            ntri += 1
            if degenerate(c1, c2, c3): ndeg += 1; continue
            cth = (math.cosh(d1) * math.cosh(d2) - math.cosh(d3)) / (math.sinh(d1) * math.sinh(d2))
            th = math.acos(max(-1.0, min(1.0, cth)))
            w = width([hyp(0, 0), hyp(d1, 0), hyp(d2, th)])
            if w < wmin: wmin, worst = w, (round(d1, 4), round(d2, 4), round(d3, 4))
print("triangle shapes:", ntri, " exactly degenerate:", ndeg, " min width w_min = %.6f at sides %s" % (wmin, worst))
# glide-reflection displacement check: cosh d(p, sigma p) = cosh(tau) cosh^2(delta) + sinh^2(delta) >= cosh(2 delta)
print("glide inequality spot check:", all(math.cosh(t) * math.cosh(dl) ** 2 + math.sinh(dl) ** 2 >= math.cosh(2 * dl) - 1e-12
                                         for t in [0, .1, 1, 3] for dl in [0, .2, 1, 2.5]))
def lam(R, l):
    t, u = math.tanh(R / 2), math.tanh(l / 2); return t * (1 - u * u) / (t * t - u * u)
def Delta(R, l):
    l1 = lam(R, l); lh = l1 * l
    if lh >= R: return float("inf")
    l2 = lam(R, lh)
    return max(2 * math.cosh(2 * l1 * l) - 2 * math.cosh(2 * l), 2 * math.cosh(2 * l2 * lh) - 2 * math.cosh(2 * lh))
def eps(R, l):
    t, u0 = math.tanh(R / 2), math.tanh(l / 2); s = u0 / t; eta = 1 - t * t
    E = s * eta * (1 + s) / (1 - s); Et = E + u0 * (1 - t) / t; up = u0 + Et
    return 2 * Et / (1 - up * up) if up < 1 else float("inf")
R = L0 + 0.01
while not (Delta(R, L0) < 2 and eps(R, L0) < 2 * wmin): R += 0.01
print("R_B(L) = %.2f  (Delta = %.4f < 2, eps = %.6f < 2 w_min = %.6f)" % (R, Delta(R, L0), eps(R, L0), 2 * wmin))
R1 = L0 + 0.01
while not Delta(R1, L0) < 2: R1 += 0.01
print("Delta alone needs R >= %.2f" % R1)

# ---- Certified lower bound for the width (revision 4) ----------------------------------------------------------
# For a triangle with p1 at the origin of the hyperboloid, M(n) := max_j |<P_j, n>| over unit spacelike
# n(t, phi) = (sinh t, cosh t cos phi, cosh t sin phi); width = asinh(min M). Claim: M >= thr everywhere.
# (i) |<P1, n>| = |sinh t|, so M >= thr whenever |t| >= T0 := asinh(thr): only |t| < T0 needs checking.
# (ii) On |t| <= T0, each |<P_j, n>| is Lipschitz with |d/dt| <= cosh(d_j + T0), |d/dphi| <= cosh(T0) sinh(d_j),
#     d_j = d(p1, p_j) <= L; a max of such functions has the same constants. So on a cell with centre c and
#     half-widths (ht, hp): min M >= M(c) - Lt*ht - Lp*hp. Cells are split until this is >= thr (branch and bound).
# Floating point is used; the margins accepted are many orders of magnitude above the rounding error.
def certify(P, dmax, thr):
    T0 = math.asinh(thr); Lt = math.cosh(dmax + T0); Lp = math.cosh(T0) * math.sinh(dmax)
    def M(t, ph):
        n = (math.sinh(t), math.cosh(t) * math.cos(ph), math.cosh(t) * math.sin(ph))
        return max(abs(mink(p, n)) for p in P)
    stack = [(0.0, math.pi * (2 * k + 1) / 64, T0, math.pi / 64) for k in range(64)]
    evals = 0
    while stack:
        t, ph, ht, hp = stack.pop(); evals += 1
        if M(t, ph) - Lt * ht - Lp * hp >= thr: continue
        if ht < 1e-9 or evals > 5_000_000: return False, evals
        stack += [(t + a * ht / 2, ph + b * hp / 2, ht / 2, hp / 2) for a in (-1, 1) for b in (-1, 1)]
    return True, evals
if len(sys.argv) > 2:
    WC = float(sys.argv[2])                      # width to certify for every non-degenerate shape
    thr = math.sinh(WC); bad = 0; tot = 0; ev = 0
    for i, (c1, d1) in enumerate(spec1):
        for (c2, d2) in spec1[i:]:
            for (c3, d3) in spec3:
                if d3 > d1 + d2 + 1e-9 or d3 < abs(d1 - d2) - 1e-9 or degenerate(c1, c2, c3): continue
                cth = (math.cosh(d1) * math.cosh(d2) - math.cosh(d3)) / (math.sinh(d1) * math.sinh(d2))
                th = math.acos(max(-1.0, min(1.0, cth)))
                ok, e = certify([hyp(0, 0), hyp(d1, 0), hyp(d2, th)], max(d1, d2), thr)
                tot += 1; ev += e
                if not ok: bad += 1; print("  NOT certified: sides", round(d1, 4), round(d2, 4), round(d3, 4))
    print("certified width >= %.4f for %d / %d non-degenerate shapes (%d cell evaluations)" % (WC, tot - bad, tot, ev))
    print("condition eps(R_B, L) = %.6f < 2 * %.4f = %.4f: %s" % (eps(R, L0), WC, 2 * WC, eps(R, L0) < 2 * WC and bad == 0))
