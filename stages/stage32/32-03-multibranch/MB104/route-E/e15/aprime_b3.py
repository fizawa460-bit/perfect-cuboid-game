# E15, section 4: is the setting of E14 Theorem A' (s2 = 0, O1 inside O2, s1 > 0) realised with b <= 3 ?
# For b <= 3 the only numerical possibility is (a, s1, m, b) = (2, 1, 0, 3):
#   p2 a slack-0 cubic, p1 of degree 2 with exactly one critical value in B, and O1 = O2.
# Then O2 (10 points) is invariant under the deck involution sigma of p1, sigma has no fixed point in O2, and the
# five sigma-orbits together with the image of ONE fixed point of sigma form a Moebius image of B ("octahedral").
# Test (double precision, margins printed): for each of the 60 slack-0 cubics, list all Moebius involutions
# preserving O2 and compute the octahedral defect of the quotient configuration.
# Controls: (c1) planted example: O = preimage under a degree-2 map of 5 points of a Moebius image of B whose
#                sixth point is a critical value; the routine must find it with defect ~ 0;
#           (c2) the involutions preserving B and acting freely on it (octahedral group: 6 edge rotations).
# The enumeration only lists involutions that move the first two reference points; every involution acting freely
# on the set is of this kind.
import itertools
import numpy as np
PAIRINGS = [p for p in itertools.permutations(range(6))
            if p[0] < p[1] and p[2] < p[3] and p[4] < p[5] and p[0] < p[2] < p[4]]
def cr(a, b, c, d): return (a - c) * (b - d) / ((a - d) * (b - c))
def defect(pts):
    best = 9e9
    for p in PAIRINGS:
        pr = [(pts[p[0]], pts[p[1]]), (pts[p[2]], pts[p[3]]), (pts[p[4]], pts[p[5]])]
        e = max(abs(cr(pr[i][0], pr[i][1], pr[j][0], pr[j][1]) + 1) for i in range(3) for j in range(i + 1, 3))
        best = min(best, e)
    return best
mu = lambda t: (t * (0.7 + 0.2j) + 0.3 - 0.1j) / (t * (0.2 - 0.5j) + 1.1 + 0.4j)
Bg = [mu(0), (0.7 + 0.2j) / (0.2 - 0.5j), mu(1), mu(-1), mu(1j), mu(-1j)]
def mob3(s1, s2, s3):
    c = (s3 - s2) / (s3 - s1)
    return np.array([[c, -c * s1], [1, -s2]])
def apply(M, t): return (M[0, 0] * t + M[0, 1]) / (M[1, 0] * t + M[1, 1])
sig = np.array([[0.9 + 0.3j, 0.2 - 0.6j], [0.4 + 0.1j, 1.0 - 0.2j]])
def compose_mob(num, den, S):
    n = max(len(num), len(den)) - 1
    a = np.array([S[0, 0], S[0, 1]]); c = np.array([S[1, 0], S[1, 1]])
    def sub(p):
        p = np.concatenate([np.zeros(n + 1 - len(p)), p]); out = np.zeros(1, dtype=complex)
        for j, co in enumerate(p):
            term = np.array([co], dtype=complex)
            for _ in range(n - j): term = np.polymul(term, a)
            for _ in range(j): term = np.polymul(term, c)
            out = np.polyadd(out, term)
        return out
    return sub(num), sub(den)
def fibre(num, den, v): return np.roots(np.polysub(num, v * den))
def cubics(S):
    N = mob3(S[0], S[1], S[2]); z = apply(N, S[3]); Ninv = np.linalg.inv(N)
    H = np.polysub(np.polymul([1, 0], np.polymul([3, -2], np.polymul([3, -2], [3, -2]))), z * np.array([2, -1]))
    out = []
    for k in np.roots(H):
        num = np.array([2 * k - 1, 2 - 3 * k, 0, 0]); den = np.array([1, -k])
        num, den = compose_mob(num, den, sig)
        n2 = Ninv[0, 0] * num + Ninv[0, 1] * np.concatenate([np.zeros(len(num) - len(den)), den])
        d2 = Ninv[1, 0] * num + Ninv[1, 1] * np.concatenate([np.zeros(len(num) - len(den)), den])
        out.append((n2, d2))
    return out
def odd_set(num, den, S_idx):
    O = []
    for j, v in enumerate(Bg):
        r = list(fibre(num, den, v))
        if j in S_idx:
            d = sorted((abs(r[x] - r[y]), x, y) for x in range(3) for y in range(x + 1, 3))
            O.append(r[3 - d[0][1] - d[0][2]])
        else:
            O += r
    return O
def involutions(O, tol=1e-6):
    """All Moebius involutions M = [[al, be], [ga, -al]] with M(O) = O; returns (M, worst matching error, gap)."""
    res = []; n = len(O); p = O[0]; nearmiss = 9e9
    for kq in range(1, n):
        q = O[kq]; rest = [x for x in range(1, n) if x != kq]; r = O[rest[0]]
        for ks in rest[1:] + [None]:
            # ks = None: r is NOT moved to a listed partner -> handled by other choices unless r is fixed (excluded)
            if ks is None: continue
            s = O[ks]
            v = np.cross([p + q, 1, -p * q], [r + s, 1, -r * s])
            M = np.array([[v[0], v[1]], [v[2], -v[0]]])
            if abs(np.linalg.det(M)) < 1e-12: continue
            err = 0.0
            for t in O:
                w = apply(M, t); err = max(err, min(abs(w - y) for y in O))
            if err < tol: res.append((M, err))
            else: nearmiss = min(nearmiss, err)
    return res, nearmiss
def quotient_defects(M, O):
    """fixed points f1, f2 of M; coordinate u = ((t - f1)/(t - f2))^2; defects of {5 orbits} + {u = 0} and + {u = inf}."""
    al, be, ga = M[0, 0], M[0, 1], M[1, 0]
    f = np.roots([ga, -2 * al, -be])
    fixed_in_O = min(abs(t - ff) for t in O for ff in f)
    us = []
    for t in O:
        w = ((t - f[0]) / (t - f[1])) ** 2
        if all(abs(w - y) > 1e-6 * max(1, abs(w)) for y in us): us.append(w)
    g = lambda w: (w * (0.3 + 0.9j) + 0.5) / (w * (0.8 - 0.1j) + 1.3j)       # generic Moebius: avoids infinity
    ginf = (0.3 + 0.9j) / (0.8 - 0.1j)
    pts = [g(w) for w in us]
    return len(us), fixed_in_O, defect(pts + [g(0)]) if len(us) == 5 else None, defect(pts + [ginf]) if len(us) == 5 else None
# controls
c2, _ = involutions(Bg)
N6 = mob3(Bg[5], 2.0 + 1.0j, Bg[0])                # sends one point of B_g to 0
tau = lambda t: (t * (1.1 - 0.4j) + 0.6j) / (t * (0.3 + 0.2j) + 0.9)
planted = []
for x in range(5):
    w = np.sqrt(complex(apply(N6, Bg[x]))); planted += [tau(w), tau(-w)]
c1, _ = involutions(planted)
c1def = 9e9
for (M, e) in c1:
    k, fo, d0, dinf = quotient_defects(M, planted)
    if k == 5 and fo > 1e-6: c1def = min(c1def, d0, dinf)
nfree = sum(1 for (M, e) in c2 if quotient_defects(M, Bg)[1] > 1e-6)
print("control c2: involutions preserving B_g without fixed point in B_g: %d (expected 6)" % nfree)
print("control c1: planted example detected with defect %.1e (expected ~0)" % c1def)
# main test
found = 0; n3 = 0; best = 9e9; near = 9e9; ninv = 0
for S_idx in itertools.combinations(range(6), 4):
    for (num, den) in cubics([Bg[x] for x in S_idx]):
        O = odd_set(num, den, S_idx); n3 += 1
        assert len(O) == 10
        invs, nm = involutions(O); near = min(near, nm)
        for (M, err) in invs:
            ninv += 1
            k, fo, d0, dinf = quotient_defects(M, O)
            if k == 5 and fo > 1e-6:
                best = min(best, d0, dinf)
                if min(d0, dinf) < 1e-6: found += 1
print("degree 3: %d slack-0 maps; involutions preserving O2 (all maps together): %d" % (n3, ninv))
print("   smallest error of a rejected involution candidate: %.3e (accepted need < 1e-6)" % near)
if ninv: print("   smallest octahedral defect of a quotient configuration: %.4f" % best)
print("   realisations of (a, s1, m, b) = (2, 1, 0, 3): %d" % found)
ok = nfree == 6 and c1def < 1e-8 and n3 == 60 and near > 1e-3
print("PASS (test valid)" if ok else "FAIL (test not valid)")
