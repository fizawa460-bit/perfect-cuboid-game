"""checks10 / zeros10.py -- zeros of q' - sigma o p at the smooth vertices of a cluster (Lemma Z).

Lemma Z (statement in ANSWER-09 sec. 4). Let V = dev1(v~) be the image of a smooth vertex v of tau_p (p(v) in B, local
degree 2), g in N(Gamma_0) inducing sigma, and suppose d(F zeta, g zeta) < 2r on the circle |zeta - V| = r for some
r < l_min / 2 (F = dev2 o s1 holomorphic near V). Then q' - sigma o p has exactly one zero (with multiplicity) in the
disc of v corresponding to B(V, r). (Fixed-point index of e_V o g^{-1} F, which is 2r-close... see the answer.)

Part A [estimate]: when does the hypothesis of Lemma Z follow from depth? V is adjacent (in tau_p) to a deep anchor
  y of the cluster, which has another cluster anchor z adjacent to it at angle theta = k pi/4 from V (k = 1..4).
  Lemma B2 at y with radius L' = l_min + r gives g~ with d(F, g~) <= e1 := eps(R, L') on B(y, L'); F = g at y and z,
  so k := g^{-1} g~ moves y and z by <= e1; D := the largest displacement of such a k on the circle |zeta - V| = r
  (computed by sampling all isometries with these two constraints: grid, floating point). Condition: e1 + D < 2r.
  Prints the least R (grid 0.05) for which some r < l_min/2 works for every theta, and N0 there.
Part B [computed, 50 digits]: the local mechanism on exact data. For slack-0 maps p of degree 3, 4 (F-02) and a
  Moebius map mu close to the identity, q' := p o mu (so sigma = id and F is close to g = id everywhere). Then the
  2n zeros of q' - p are: exactly one within 1e-2 of each of the 2n - 2 critical points of p (= smooth vertices of
  tau_p), and two near the fixed points of mu. (No common cone points here; this checks only the local count.)
usage (from the repository root):  python3 -I stages/stage32/32-03-multibranch/MB104/route-F/wall/checks10/zeros10.py
"""
import sys, os, math, json, importlib.util, io, contextlib
sys.dont_write_bytecode = True
import numpy as np
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
S2 = math.sqrt(2); lmin = math.acosh(1 + S2)
ok = True


def eps(R, L):
    t, u = math.tanh(R / 2), math.tanh(L / 2)
    s = u / t; eta = 1 - t * t
    E = s * eta * (1 + s) / (1 - s) + u * (1 - t) / t
    return 2 * E / (1 - (u + E) ** 2) if u + E < 1 else float("inf")
def N0(R): return (math.cosh(R + lmin / 2) - 1) / (math.cosh(lmin / 2) - 1)


# ---------------- Part A ----------------
def pt(d, th): return np.array([math.cosh(d), math.sinh(d) * math.cos(th), math.sinh(d) * math.sin(th)])
def mink(a, b): return -a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
def dist(a, b): return math.acosh(max(1.0, -mink(a, b)))
def boost(d, th):            # translation by d in direction th (hyperboloid model)
    c, s = math.cosh(d), math.sinh(d); ct, st = math.cos(th), math.sin(th)
    Rz = np.array([[1, 0, 0], [0, ct, -st], [0, st, ct]])
    Bx = np.array([[c, s, 0], [s, c, 0], [0, 0, 1]])
    return Rz @ Bx @ Rz.T
def rot(ph): return np.array([[1, 0, 0], [0, math.cos(ph), -math.sin(ph)], [0, math.sin(ph), math.cos(ph)]])
Y = pt(0, 0); Vp = pt(lmin, 0)
def circle(r, m=24):
    B = boost(lmin, 0)
    return [B @ pt(r, 2 * math.pi * j / m) for j in range(m)]
def Dmax(e1, r, theta):
    Z = pt(lmin, theta); C = circle(r); best = 0.0
    for ra in np.linspace(0, e1, 5):
        for ta in np.linspace(0, 2 * math.pi, 16, endpoint=False):
            T = boost(ra, ta)
            for ph in np.linspace(-3 * e1, 3 * e1, 31):
                K = T @ rot(ph)
                if dist(K @ Z, Z) > e1: continue
                best = max(best, max(dist(K @ c, c) for c in C))
    return best
def works(R):
    for r in np.linspace(0.40, lmin / 2 - 0.01, 4):
        e1 = eps(R, lmin + r)
        if e1 >= 2 * r: continue
        if all(e1 + Dmax(e1, r, k * math.pi / 4) < 2 * r for k in (1, 2, 3, 4)):
            return r, e1
    return None
print("Part A [estimate]: hypothesis of Lemma Z from depth (V adjacent to a deep cluster anchor y with a cluster neighbour z)")
RZ = None
for R in np.arange(5.0, 12.01, 0.25):
    w = works(R)
    if w:
        RZ = (R, w); break
if RZ:
    R, (r, e1) = RZ
    # refine downward in steps of 0.05
    for R2 in np.arange(R - 0.2, R, 0.05):
        w = works(R2)
        if w: R, (r, e1) = R2, w; break
    print("  least R found: %.2f (r = %.3f, eps(R, l_min + r) = %.4f); N0(R) = %.0f, so (1,1): n >= %d"
          % (R, r, e1, N0(R), math.floor(N0(R) - 1.5) + 1))
else:
    print("  no R <= 12 found"); ok = False


# ---------------- Part B ----------------
spec = importlib.util.spec_from_file_location("census9", os.path.join(HERE, "..", "checks9", "census9.py"))
C9 = importlib.util.module_from_spec(spec); spec.loader.exec_module(C9)
mp.mp.dps = 50
with contextlib.redirect_stdout(io.StringIO()):
    maps = C9.load_maps(3, os.path.join(HERE, "..", "..", "f02"))[:20] + C9.load_maps(4, os.path.join(HERE, "..", "..", "f02"))[::34]
def peval(c, z): return mp.polyval(list(reversed(c)), z)
def pmul(a, b):
    r = [mp.mpc(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += x * y
    return r
def padd(a, b):
    n = max(len(a), len(b)); return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]
def ppow(a, k):
    r = [mp.mpc(1)]
    for _ in range(k): r = pmul(r, a)
    return r
d = mp.mpc("1e-4", "2e-4")
A_, B_, C_, D_ = 1 + d, mp.mpc("3e-4", "-1e-4"), mp.mpc("-2e-4", "1.5e-4"), mp.mpc(1)
good_all = True; nmaps = 0
for m in maps:
    n = m.n
    num = [mp.mpc(0)]; den = [mp.mpc(0)]
    for k in range(n + 1):
        t = pmul(ppow([B_, A_], k), ppow([D_, C_], n - k))
        num = padd(num, [m.P[k] * x for x in t]); den = padd(den, [m.Q[k] * x for x in t])
    # q' - p = (num Q - P den) / (den Q)
    F = padd(pmul(num, m.Q), [-x for x in pmul(m.P, den)])
    while len(F) > 1 and abs(F[-1]) < mp.mpf(10) ** -45: F.pop()
    zs = mp.polyroots(list(reversed(F)), maxsteps=500, extraprec=300)
    crit = [z for z, k in m.crit if z is not None]
    # fixed points of mu: C z^2 + (D - A) z - B = 0
    fx = mp.polyroots([C_, D_ - A_, -B_])
    per_crit = [sum(1 for z in zs if abs(z - c) < 1e-2) for c in crit]
    near_fix = sum(1 for z in zs if min(abs(z - f) for f in fx) < 1e-2)
    inf_crit = len(m.crit) - len(crit)          # a critical point at oo: then deg F drops by one there
    good = all(c == 1 for c in per_crit) and len(zs) + (2 * n - len(F) + 1) == 2 * n and near_fix + sum(per_crit) + inf_crit == 2 * n
    good_all &= good; nmaps += 1
print("Part B [computed, dps 50]: q' = p o mu, mu near the identity: one zero of q' - p next to every critical point of p, "
      "two near the fixed points of mu, on %d maps of degree 3 and 4: %s" % (nmaps, good_all))
ok &= good_all
print("PASS" if ok else "FAIL")
