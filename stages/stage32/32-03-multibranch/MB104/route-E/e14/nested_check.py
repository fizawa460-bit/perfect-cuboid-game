# E14 Theorem A+ : numerical checks (double precision; every decision has a margin printed below).
#  (1) the residual case of the proof: a = 1, b = 3, p2 a cubic with simple critical points over Q = B minus an
#      antipodal pair; is p2^{-1}(antipodal pair) Moebius-equivalent to B ("octahedral")?
#  (2) falsification test of Theorem A+ for a = 1: for all 15 slack-0 maps of degree 2 and all 60 of degree 3,
#      no 6-subset of the odd set O_2 is octahedral.
# Octahedral  <=>  the six points split into three pairs that are mutually harmonic (cross-ratio -1).
import itertools, cmath
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
# a generic Moebius image of B, so that no point is at infinity
mu = lambda t: (t * (0.7 + 0.2j) + 0.3 - 0.1j) / (t * (0.2 - 0.5j) + 1.1 + 0.4j)
Bg = [mu(0), (0.7 + 0.2j) / (0.2 - 0.5j), mu(1), mu(-1), mu(1j), mu(-1j)]      # images of 0, inf, 1, -1, i, -i
ANTI = [(0, 1), (2, 3), (4, 5)]
print("control: defect(B_g) = %.2e" % defect(Bg))
def mob3(s1, s2, s3):                      # N with N(s1)=0, N(s2)=inf, N(s3)=1, as matrix
    c = (s3 - s2) / (s3 - s1)
    return np.array([[c, -c * s1], [1, -s2]])
def apply(M, t): return (M[0, 0] * t + M[0, 1]) / (M[1, 0] * t + M[1, 1])
sig = np.array([[0.9 + 0.3j, 0.2 - 0.6j], [0.4 + 0.1j, 1.0 - 0.2j]])   # generic source Moebius (no source point at inf)
def compose_mob(num, den, S):              # (num/den)(S t), numpy coefficient arrays (highest first)
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
def cubics(S):                              # the 4 slack-0 cubics with critical values S (E11 par. 9 normal form)
    N = mob3(S[0], S[1], S[2]); z = apply(N, S[3]); Ninv = np.linalg.inv(N)
    H = np.polysub(np.polymul([1, 0], np.polymul([3, -2], np.polymul([3, -2], [3, -2]))), z * np.array([2, -1]))
    out = []
    for k in np.roots(H):
        num = np.array([2 * k - 1, 2 - 3 * k, 0, 0]); den = np.array([1, -k])     # F_k, critical values 0, inf, 1, z
        num, den = compose_mob(num, den, sig)
        n2 = Ninv[0, 0] * num + Ninv[0, 1] * np.concatenate([np.zeros(len(num) - len(den)), den])
        d2 = Ninv[1, 0] * num + Ninv[1, 1] * np.concatenate([np.zeros(len(num) - len(den)), den])
        out.append((n2, d2))
    return out
def odd_set(num, den, S_idx):
    O = []; sep = 9e9; dbl = 0
    for j, v in enumerate(Bg):
        r = list(fibre(num, den, v))
        if j in S_idx:                      # one double and one simple point
            d = sorted((abs(r[x] - r[y]), x, y) for x in range(3) for y in range(x + 1, 3))
            dbl = max(dbl, d[0][0]); sep = min(sep, d[1][0])
            O.append(r[3 - d[0][1] - d[0][2]])
        else:
            sep = min(sep, min(abs(r[x] - r[y]) for x in range(3) for y in range(x + 1, 3))); O += r
    return O, dbl, sep
# (1) residual case
print("(1) residual case a = 1, b = 3:")
worst1 = 9e9
for (i, j) in ANTI:
    S_idx = [x for x in range(6) if x not in (i, j)]
    for (num, den) in cubics([Bg[x] for x in S_idx]):
        pts = list(fibre(num, den, Bg[i])) + list(fibre(num, den, Bg[j]))
        d = defect(pts); worst1 = min(worst1, d)
print("   12 maps (3 antipodal pairs x 4 cubics): smallest octahedral defect = %.4f (octahedral would be 0)" % worst1)
# (2) a = 1 against every slack-0 map of degree 2 and 3
print("(2) a = 1, all slack-0 maps of degree 2 and 3:")
worst2 = 9e9; n2 = 0
for (i, j) in itertools.combinations(range(6), 2):
    N = mob3(Bg[i], Bg[j], Bg[[x for x in range(6) if x not in (i, j)][0]])
    O = []
    for x in range(6):
        if x in (i, j): continue
        w = cmath.sqrt(apply(N, Bg[x])); O += [w, -w]
    n2 += 1
    for sub in itertools.combinations(O, 6): worst2 = min(worst2, defect(list(sub)))
print("   degree 2: %d maps, 28 subsets each: smallest defect = %.4f" % (n2, worst2))
worst3 = 9e9; n3 = 0; dblmax = 0; sepmin = 9e9
for S_idx in itertools.combinations(range(6), 4):
    for (num, den) in cubics([Bg[x] for x in S_idx]):
        O, dbl, sep = odd_set(num, den, S_idx); n3 += 1
        dblmax = max(dblmax, dbl); sepmin = min(sepmin, sep)
        assert len(O) == 10
        for sub in itertools.combinations(O, 6): worst3 = min(worst3, defect(list(sub)))
print("   degree 3: %d maps, 210 subsets each: smallest defect = %.4f" % (n3, worst3))
print("   root clustering: double roots split by <= %.1e, distinct points separated by >= %.1e" % (dblmax, sepmin))
ok = worst1 > 0.1 and worst2 > 0.1 and worst3 > 0.01 and n2 == 15 and n3 == 60 and dblmax < 1e-5 and sepmin > 1e-3
print("PASS" if ok else "FAIL")
