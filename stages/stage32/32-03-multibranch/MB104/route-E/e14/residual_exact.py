# E14 Theorem A+, residual case (a, b) = (1, 3), EXACT over Q(i).
# If O_1 = p_2^{-1}{beta, beta*} were octahedral, then f = p_2 o p_1^{-1} (after Moebius changes) is a cubic
#   f = c * (t-b1)(t-b2)(t-b3) / ((t-b4)(t-b5)(t-b6)),   {b1..b6} = B' (a Moebius image of B),
# whose four critical values are {1, -1, i, -i}. Then the critical values v_1..v_4 of g = f/c are c^{-1} i^k, so
# their power sums p_1, p_2, p_3 vanish. We compute p_1, p_2, p_3 exactly for all 20 ordered splits.
import itertools, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gq import *
from fractions import Fraction as Fr
# B' = image of B = {0, inf, 1, -1, i, -i} under t -> 1/(t-w), w = 2+3i (generic: no critical point at infinity)
w = G(2, 3)
Bp = [(-w).inv(), G(0), (1 - w).inv(), (-1 - w).inv(), (I - w).inv(), (-I - w).inv()]
# control: B' is octahedral: pairs (0,inf),(1,-1),(i,-i) are mutually harmonic
def cr(a, b, c, d): return (a - c) * (b - d) / ((a - d) * (b - c))
assert all(cr(Bp[x], Bp[x + 1], Bp[y], Bp[y + 1]) == -1 for x, y in ((0, 2), (0, 4), (2, 4)))
def matmul(A, Bm): return [[sum((A[i][k] * Bm[k][j] for k in range(4)), G()) for j in range(4)] for i in range(4)]
def matinv(A):
    n = 4; M = [list(r) + [G(1) if i == j else G() for j in range(n)] for i, r in enumerate(A)]
    for c in range(n):
        piv = next(r for r in range(c, n) if not M[r][c].iszero()); M[c], M[piv] = M[piv], M[c]
        iv = M[c][c].inv(); M[c] = [x * iv for x in M[c]]
        for r in range(n):
            if r != c and not M[r][c].iszero():
                f = M[r][c]; M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [r[n:] for r in M]
def polymat(p, C):
    R = [[G() for _ in range(4)] for _ in range(4)]
    for c in reversed(p):
        R = matmul(R, C); R = [[R[i][j] + (c if i == j else G()) for j in range(4)] for i in range(4)]
    return R
bad = 0; n = 0
for num in itertools.combinations(range(6), 3):
    den = [x for x in range(6) if x not in num]
    Pn = P(1); Qn = P(1)
    for x in num: Pn = pmul(Pn, P(-Bp[x], 1))
    for x in den: Qn = pmul(Qn, P(-Bp[x], 1))
    W = psub(pmul(pder(Pn), Qn), pmul(Pn, pder(Qn)))        # critical points: roots of W
    assert deg(W) == 4 and deg(pgcd(W, Qn)) == 0
    sqf = deg(pgcd(W, pder(W))) == 0      # four simple critical points (needed for the case; recorded)
    Wm = pscale(W, W[-1].inv())
    C = [[G() for _ in range(4)] for _ in range(4)]          # companion matrix of W (multiplication by t)
    for i in range(3): C[i + 1][i] = G(1)
    for i in range(4): C[i][3] = -Wm[i]
    V = matmul(polymat(Pn, C), matinv(polymat(Qn, C)))       # multiplication by g = P/Q on Q(i)[t]/(W)
    ps = []; M = V
    for k in range(3):
        ps.append(sum((M[i][i] for i in range(4)), G())); M = matmul(M, V)
    n += 1
    if sqf and all(p.iszero() for p in ps): bad += 1
    print("split", num, "| simple critical points:", sqf, "| p1, p2, p3 =", ps[0], ps[1], ps[2])
print("%d splits (unordered pairs {num, den} appear twice), %d with simple critical points and p1 = p2 = p3 = 0" % (n, bad))
print("PASS" if n == 20 and bad == 0 else "FAIL")
