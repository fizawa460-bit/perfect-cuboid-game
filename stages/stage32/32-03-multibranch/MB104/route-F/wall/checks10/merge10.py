"""checks10 / merge10.py -- step 2 (connection): when do two clusters have the same conjugator?

Lemma M (ANSWER-09 sec. 3). Let y1, z1 be adjacent anchors of a cluster C1 and y2, z2 adjacent anchors of a cluster
C2 (deep lifts on one sheet), g1, g2 in N(Gamma_0) their conjugators. If g1^{-1} g2 moves y1 and z1 by less than
l_min, then g1 = g2. [proved: N(Gamma_0) preserves the tiling; a non-trivial element moves y1 to another vertex
(>= l_min) or fixes y1 and rotates z1 to another neighbour (>= l_min).]

Part A [estimate]: the depth that makes the hypothesis automatic. Put c = the midpoint of [y1, y2], d(y1, y2) = rho,
  z_i adjacent to y_i in any of the 8 tiling directions. Lemma B2 at c (a deep point; not necessarily an anchor) with
  radius L'' = rho/2 + l_min gives g~ with d(F, g~) <= e := eps(R, L'') on B(c, L''). F = g_i at y_i, z_i, so
  k_i := g~^{-1} g_i moves y_i, z_i by <= e, and d(g1^{-1} g2 y1, y1) <= e + D, where D is the largest displacement
  at y1 and z1 of an isometry moving y2 and z2 by <= e (sampling, floating point). Condition: e + D < l_min.
  Prints, for rho = 2h, 2.914, 2 l_min, 3.632 (the tiling distances between two anchors with no anchor between
  them), the least R (grid 0.25) and N0(R).
usage (from the repository root):  python3 -I stages/stage32/32-03-multibranch/MB104/route-F/wall/checks10/merge10.py
"""
import sys, math
sys.dont_write_bytecode = True
import numpy as np
S2 = math.sqrt(2); lmin = math.acosh(1 + S2); alt = math.asinh(math.sinh(lmin) * math.sin(math.pi / 4))


def eps(R, L):
    t, u = math.tanh(R / 2), math.tanh(L / 2)
    if u >= t: return float("inf")
    s = u / t; eta = 1 - t * t
    E = s * eta * (1 + s) / (1 - s) + u * (1 - t) / t
    return 2 * E / (1 - (u + E) ** 2) if u + E < 1 else float("inf")
def N0(R): return (math.cosh(R + lmin / 2) - 1) / (math.cosh(lmin / 2) - 1)
def mink(a, b): return -a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
def dist(a, b): return math.acosh(max(1.0, -mink(a, b)))
def rotm(ph): return np.array([[1, 0, 0], [0, math.cos(ph), -math.sin(ph)], [0, math.sin(ph), math.cos(ph)]])
def boost(d, th):
    c, s = math.cosh(d), math.sinh(d)
    Bx = np.array([[c, s, 0], [s, c, 0], [0, 0, 1]])
    return rotm(th) @ Bx @ rotm(th).T
O = np.array([1.0, 0, 0])


def config(rho, a1, a2):
    """c = origin; y1, y2 at -rho/2, +rho/2 on the x-axis; z_i adjacent to y_i in direction a_i."""
    y1 = boost(rho / 2, math.pi) @ O; y2 = boost(rho / 2, 0) @ O
    z1 = boost(rho / 2, math.pi) @ boost(lmin, a1) @ O
    z2 = boost(rho / 2, 0) @ boost(lmin, a2) @ O
    return y1, z1, y2, z2


def D(e, y1, z1, y2, z2):
    best = 0.0
    T2 = boost(rho_cur / 2, 0)
    for ra in np.linspace(0, e, 6):
        for ta in np.linspace(0, 2 * math.pi, 16, endpoint=False):
            for ph in np.linspace(-2.5 * e, 2.5 * e, 41):
                K = T2 @ boost(ra, ta) @ rotm(ph) @ np.linalg.inv(T2)      # moves y2 by exactly ra
                if dist(K @ y2, y2) > e + 1e-12 or dist(K @ z2, z2) > e: continue
                best = max(best, dist(K @ y1, y1), dist(K @ z1, z1))
                if best > lmin: return best
    return best


rows = []
print("Part A [estimate]: least depth R with e + D < l_min (two clusters at distance rho get one conjugator)")
for rho in (2 * alt, 2.914035, 2 * lmin, 3.631582):
    rho_cur = rho
    Lpp = rho / 2 + lmin
    found = None
    for R in np.arange(6.0, 16.01, 0.25):
        e = eps(R, Lpp)
        if not e < lmin: continue
        worst = 0.0
        for k1 in range(8):
            for k2 in range(8):
                y1, z1, y2, z2 = config(rho, k1 * math.pi / 4, k2 * math.pi / 4)
                worst = max(worst, e + D(e, y1, z1, y2, z2))
                if worst >= lmin: break
            if worst >= lmin: break
        if worst < lmin:
            found = (R, e, worst); break
    if found:
        R, e, w = found
        print("  rho = %.4f: R = %.2f (eps(R, %.3f) = %.4f, e + D = %.4f < %.4f); N0(R) = %.0f; (1,1): n >= %d"
              % (rho, R, Lpp, e, w, lmin, N0(R), math.floor(N0(R) - 1.5) + 1))
        rows.append((rho, R))
    else:
        print("  rho = %.4f: no R <= 16" % rho)
print("PASS" if len(rows) == 4 else "FAIL")
