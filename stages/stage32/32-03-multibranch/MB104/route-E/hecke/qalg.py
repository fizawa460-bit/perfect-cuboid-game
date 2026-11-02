"""Exact arithmetic in the Bolza order Q_B (KKSV) over K = Q(sqrt2).
K elements: pairs (a, b) = a + b*sqrt2 with Fractions.  Quaternions in D_B = (-3, sqrt2): 4-tuples over K in basis
1, i, j, k=ij (i^2=-3, j^2=sqrt2).  Bolza basis: e0=1, e1=alpha=(1+i)/2, e2=beta, e3=alpha*beta."""
from fractions import Fraction as Fr
Z0 = (Fr(0), Fr(0)); ONE = (Fr(1), Fr(0)); S2 = (Fr(0), Fr(1))
def ka(p, q): return (p[0] + q[0], p[1] + q[1])
def ks(p, q): return (p[0] - q[0], p[1] - q[1])
def km(p, q): return (p[0]*q[0] + 2*p[1]*q[1], p[0]*q[1] + p[1]*q[0])
def kn(p): return p[0]*p[0] - 2*p[1]*p[1]               # field norm
def kinv(p):
    n = kn(p); return (p[0]/n, -p[1]/n)
def kc(c): return (Fr(c), Fr(0))
A = kc(-3); B = S2; AB = km(A, B); mAB = (-AB[0], -AB[1]); mB = (-B[0], -B[1]); mA = (-A[0], -A[1])
def qm(x, y):
    a0, a1, a2, a3 = x; b0, b1, b2, b3 = y; m = km
    r0 = ka(ka(m(a0,b0), m(A, m(a1,b1))), ka(m(B, m(a2,b2)), m(mAB, m(a3,b3))))
    r1 = ka(ka(m(a0,b1), m(a1,b0)), ka(m(mB, m(a2,b3)), m(B, m(a3,b2))))
    r2 = ka(ka(m(a0,b2), m(a2,b0)), ka(m(A, m(a1,b3)), m(mA, m(a3,b1))))
    r3 = ka(ka(m(a0,b3), m(a3,b0)), ka(m(a1,b2), (-m(a2,b1)[0], -m(a2,b1)[1])))
    return (r0, r1, r2, r3)
def qa(*xs):
    o = (Z0,)*4
    for x in xs: o = tuple(ka(o[t], x[t]) for t in range(4))
    return o
def qs(c, x): return tuple(km(c, x[t]) for t in range(4))
def nrd(x):
    a0, a1, a2, a3 = x
    return ka(ka(km(a0,a0), km(mA, km(a1,a1))), ka(km(mB, km(a2,a2)), km(AB, km(a3,a3))))
def conj(x): return (x[0], (-x[1][0], -x[1][1]), (-x[2][0], -x[2][1]), (-x[3][0], -x[3][1]))
def qinv(x): return qs(kinv(nrd(x)), conj(x))
def tr(x): return (2*x[0][0], 2*x[0][1])
Q1 = (ONE, Z0, Z0, Z0); I = (Z0, ONE, Z0, Z0); J = (Z0, Z0, ONE, Z0)
alpha = qs((Fr(1,2), Fr(0)), qa(Q1, I))
gamma = qm(qs((Fr(1,6), Fr(0)), qa(qs(kc(3), Q1), I)), qa(Q1, qs((Fr(-1), Fr(-1)), J)))
beta = qm(alpha, qa(Q1, qs((Fr(-1), Fr(1)), gamma)))
BASIS = [Q1, alpha, beta, qm(alpha, beta)]
# coordinates in the Bolza basis: solve the 4x4 linear system over K (Gaussian elimination)
def _solve(M, v):
    n = len(M); M = [list(r) + [v[i]] for i, r in enumerate(M)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != Z0); M[c], M[p] = M[p], M[c]
        iv = kinv(M[c][c]); M[c] = [km(iv, t) for t in M[c]]
        for r in range(n):
            if r != c and M[r][c] != Z0:
                f = M[r][c]; M[r] = [ks(M[r][t], km(f, M[c][t])) for t in range(n + 1)]
    return [M[r][n] for r in range(n)]
_BM = [[BASIS[c][r] for c in range(4)] for r in range(4)]   # columns = basis vectors in (1,i,j,k)
def coords(x): return _solve(_BM, list(x))
def is_integral(x):
    return all(c[0].denominator == 1 and c[1].denominator == 1 for c in coords(x))
