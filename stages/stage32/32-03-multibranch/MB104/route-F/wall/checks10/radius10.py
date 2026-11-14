"""checks10 / radius10.py -- the radii of the cluster argument and the degree thresholds that come with them.

Part A (tiling): the vertices of the {3,8} tiling of H (lifts of the six cone points of P^1(2^6); equilateral
  triangles with angles pi/4) up to distance 4.0 from a vertex, by reflecting triangles (floating point, 1e-9).
  Prints the distances that occur between tiling vertices, checks each against the trace candidates of E13
  (cosh d = 1 + m + n sqrt2), and checks the lemma: two vertices at distance < 2h are adjacent (distance l_min),
  where 2h = 2 * altitude, cosh 2h = 3 + 2 sqrt2.
Part B (radii): for the star radius L = 1.6 (edges = tiling edges, which never cross):
  - R_B(1.6) of E13 (trace gap Delta < 2, width eps < 2 w), recomputed with route-E/e13/thmb_constants.py;
  - R_spec: Lemma B1 with the gaps of the OCCURRING distances (Part A) instead of the trace gap 2;
  - R_eps: the mirror exclusion of Lemma B3 alone (eps(R, 1.6) < 2 * 0.25, width certified by thmb_constants);
  - R_E-based: Lemma B1 from E15 Theorem E (path points (R - l_min)-deep).
Part C (thresholds): N0(R) of E14 Proposition L(c) and the least n for which some anchor must be R-deep:
  type (1,1): |A| = 2n + 3 > 2 (s1' + s2') N0(R) with s1' + s2' = (m1 + m2)/2 = 1;
  types (2,2), (1,3): |A| = 2n + 2 or 2a + 3 > 4 N0(R).
usage (from the repository root):  python3 -I stages/stage32/32-03-multibranch/MB104/route-F/wall/checks10/radius10.py
"""
import sys, os, math, subprocess
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
THMB = os.path.normpath(os.path.join(HERE, "..", "..", "..", "route-E", "e13", "thmb_constants.py"))
S2 = math.sqrt(2)
lmin = math.acosh(1 + S2)
alt = math.asinh(math.sinh(lmin) * math.sin(math.pi / 4))
ok = True


def mink(a, b): return -a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
def cross(a, b):                      # Minkowski normal of the plane through a, b
    return (a[1] * b[2] - a[2] * b[1], a[0] * b[2] - a[2] * b[0], -(a[0] * b[1] - a[1] * b[0]))
def refl(v, a, b):
    n = cross(a, b); k = 2 * mink(v, n) / mink(n, n)
    return tuple(v[i] - k * n[i] for i in range(3))
def dist(a, b): return math.acosh(max(1.0, -mink(a, b)))


# ---------------- Part A ----------------
# circumradius rho of the equilateral triangle: cosh l = cosh^2 rho + sinh^2 rho / 2
rho = math.acosh(math.sqrt((math.cosh(lmin) + 0.5) / 1.5))
V0 = [(math.cosh(rho), math.sinh(rho) * math.cos(2 * math.pi * k / 3), math.sinh(rho) * math.sin(2 * math.pi * k / 3))
      for k in range(3)]
assert all(abs(dist(V0[i], V0[j]) - lmin) < 1e-12 for i in range(3) for j in range(i + 1, 3))
RMAX = 4.0
center = V0[0]
def key(v): return tuple(round(c, 5) for c in v)
verts = {key(v): v for v in V0}
tris = {tuple(sorted(key(v) for v in V0)): V0}
front = [V0]
while front:
    nf = []
    for T in front:
        for i in range(3):
            a, b = T[(i + 1) % 3], T[(i + 2) % 3]
            c = refl(T[i], a, b)
            if dist(center, c) > RMAX + lmin: continue
            NT = (c, a, b); k = tuple(sorted(key(v) for v in NT))
            if k in tris: continue
            tris[k] = NT; nf.append(NT); verts.setdefault(key(c), c)
    front = nf
ds = sorted(dist(center, v) for v in verts.values() if 1e-9 < dist(center, v) <= RMAX)
occ = []
for d in ds:
    if not occ or d - occ[-1][0] > 1e-7: occ.append([d, 1])
    else: occ[-1][1] += 1
# candidates of E13: cosh d = 1 + m + n sqrt2 with conjugate of (m + n sqrt2) in [-2, 0]
cands = []
for n in range(0, 200):
    for m in range(int(n * S2) - 3, int(n * S2) + 3):
        if -2 - 1e-12 <= m - n * S2 <= 1e-12 and m + n * S2 > 0 and 1 + m + n * S2 <= math.cosh(RMAX) + 1:
            cands.append((math.acosh(1 + m + n * S2), m, n))
cands.sort()
def match(d):
    for c in cands:
        if abs(c[0] - d) < 1e-7: return c
    return None
print("Part A: {3,8} tiling, %d vertices within %.1f of a vertex" % (len(ds), RMAX))
print("  occurring distances (d, number of vertices, cosh d = 1 + m + n sqrt2):")
for d, cnt in occ:
    c = match(d)
    print("    %.6f  %4d  %s" % (d, cnt, ("m = %d, n = %d" % (c[1], c[2])) if c else "NOT A CANDIDATE"))
    ok &= c is not None
miss = [c for c in cands if c[0] <= RMAX and not any(abs(c[0] - d) < 1e-7 for d, _ in occ)]
print("  trace candidates <= RMAX that do NOT occur between tiling vertices: %s" % ["%.4f" % c[0] for c in miss])
nb = [d for d, cnt in occ if d < 2 * alt - 1e-9]
lem = len(nb) == 1 and abs(nb[0] - lmin) < 1e-9 and occ[0][1] == 8 and abs(occ[1][0] - 2 * alt) < 1e-7
print("  lemma (distance < 2h implies adjacent): distances below 2h = %s, 8 neighbours, next = 2h = %.6f "
      "(cosh 2h = %.6f, 3 + 2 sqrt2 = %.6f): %s" % (["%.6f" % d for d in nb], 2 * alt, math.cosh(2 * alt), 3 + 2 * S2, lem))
ok &= lem
occd = [d for d, _ in occ]


# ---------------- Part B ----------------
def lam(R, L):
    t, u = math.tanh(R / 2), math.tanh(L / 2)
    return t * (1 - u * u) / (t * t - u * u)
def eps(R, L):
    t, u = math.tanh(R / 2), math.tanh(L / 2)
    s = u / t; eta = 1 - t * t
    E = s * eta * (1 + s) / (1 - s) + u * (1 - t) / t
    return 2 * E / (1 - (u + E) ** 2) if u + E < 1 else float("inf")
L = 1.6
W = 0.25                                       # certified width for L = 1.6 (thmb_constants.py 1.6 0.25)
def least(cond, lo=1.7, hi=12.0):
    if not cond(hi): return None
    for _ in range(60):
        mid = (lo + hi) / 2
        if cond(mid): hi = mid
        else: lo = mid
    return hi
def spec_ok(R):
    l1 = lam(R, L); l2 = lam(R, l1 * L)
    if l1 * L >= R: return False
    lm = max(l1, l2)
    rel = [d for d in occd if d <= lm * 2 * L + 1e-9]
    return all(rel[i + 1] / rel[i] > lm for i in range(len(rel) - 1) if rel[i] <= 2 * L + 1e-9)
R_spec = least(spec_ok)
R_eps = least(lambda R: eps(R, L) < 2 * W)
etaE = lambda d: math.log(math.acosh(math.cosh(d) + 1) / d)
RE = lambda l: 2 * math.atanh(math.exp(-etaE(l)))
dmax_star = 2 * lmin                           # largest distance between two points of a 1.6-star
R_Eb = lmin + RE(dmax_star)
print("Part B: star radius L = 1.6 (edges are tiling edges; they do not cross, so E13 Lemma B4 needs no L = 2 l0)")
out = ""
if os.path.exists(THMB):
    out = subprocess.run([sys.executable, "-I", THMB, "1.6", "0.25"], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if line.startswith("R_B(L)") or line.startswith("certified") or line.startswith("condition"):
            print("  thmb_constants.py 1.6 0.25: " + line)
    ok &= "R_B(L) = 5.49" in out and "6 / 6" in out and "True" in out.splitlines()[-1]
else:
    print("  (route-E/e13/thmb_constants.py not found; R_B(1.6) = 5.49 is quoted from E13 sec. 4.0)")
print("  R_spec  (B1 from the occurring-distance gaps)          = %.3f   lambda = %.4f" % (R_spec, lam(R_spec, L)))
print("  R_eps   (B2/B3 mirror exclusion, eps < 2 x 0.25)        = %.3f   eps = %.4f" % (R_eps, eps(R_eps, L)))
print("  R_E     (B1 from E15 Theorem E: l_min + R_E(2 l_min)) = %.3f   (R_E(2 l_min) = %.3f)" % (R_Eb, RE(dmax_star)))
Rstar = max(R_eps, min(5.49, R_spec, R_Eb))
print("  usable radius R* = max(R_eps, min(5.49, R_spec, R_E)) = %.3f" % Rstar)
ok &= R_spec is not None and R_eps is not None and R_spec <= 5.49 + 1e-9


# ---------------- Part C ----------------
def N0(R): return (math.cosh(R + lmin / 2) - 1) / (math.cosh(lmin / 2) - 1)
print("Part C: N0(R) (E14 Proposition L(c)) and the least degree with a guaranteed R-deep anchor")
print("   R        N0(R)   (1,1): least n   (2,2),(1,3): least n")
rows = [("E13 Theorem B (L = 3.2)", 10.78), ("L = 1.6, E13 constants", 5.49), ("L = 1.6, occurring gaps", R_spec),
        ("mirror exclusion only (floor of B2/B3)", R_eps), ("E15 Theorem E, l_min only", RE(lmin))]
for name, R in rows:
    n0 = N0(R)
    n11 = math.floor((2 * n0 - 3) / 2) + 1          # least n with 2n + 3 > 2 N0
    n22 = math.floor((4 * n0 - 2) / 2) + 1          # least n with 2n + 2 > 4 N0
    print("  %7.3f  %10.1f  %12d  %16d    %s" % (R, n0, n11, n22, name))
ok &= abs(2 * N0(10.78) - 336582) / 336582 < 0.01
print("  check: 2 N0(10.78) = %.0f (E14 sec. 7 uses 336,582)" % (2 * N0(10.78)))
print("PASS" if ok else "FAIL")
