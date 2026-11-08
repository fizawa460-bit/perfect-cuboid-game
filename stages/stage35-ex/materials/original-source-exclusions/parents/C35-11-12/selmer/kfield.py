"""Sextic field K = Q[t]/P(t), P = t^6-5t^5-8t^4-5t^3-8t^2-5t-1, with integral basis from Wolfram:
w = 1, t, (1+t+t^2)/2, (1+t^3)/2, (1+t^2+t^4)/4, (t+t^3+t^5)/4.
Exact arithmetic with Fractions. Provides: multiplication table, element <-> basis coords,
norm (via resultant / determinant), and decomposition of p*O_K via the finite algebra O/pO."""
from fractions import Fraction as Fr
from itertools import product
P = [-1, -5, -8, -5, -8, -5, 1]
N = 6
BASIS = [[1], [0, 1], [Fr(1, 2), Fr(1, 2), Fr(1, 2)], [Fr(1, 2), 0, 0, Fr(1, 2)],
         [Fr(1, 4), 0, Fr(1, 4), 0, Fr(1, 4)], [0, Fr(1, 4), 0, Fr(1, 4), 0, Fr(1, 4)]]

def pad(a):
    a = [Fr(x) for x in a]
    return a + [Fr(0)] * (N - len(a))

def polmulmod(a, b):
    r = [Fr(0)] * (2 * N - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    for d in range(2 * N - 2, N - 1, -1):
        c = r[d]
        if c:
            for i in range(N + 1):
                r[d - N + i] -= c * P[i]
    return r[:N]

B = [pad(b) for b in BASIS]
# change of basis: power coords -> basis coords; solve with Fractions (Gaussian elimination)
def solve(M, v):
    n = len(M)
    A = [row[:] + [v[i]] for i, row in enumerate(M)]
    for c in range(n):
        piv = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[piv] = A[piv], A[c]
        inv = 1 / A[c][c]
        A[c] = [x * inv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [A[i][n] for i in range(n)]

MT = [[list(range(0))] * N for _ in range(N)]   # MT[i][j] = basis coords of w_i*w_j
Bt = [[B[j][i] for j in range(N)] for i in range(N)]   # columns = basis vectors (power coords)
def to_basis(powc):
    return solve(Bt, pad(powc))
def to_pow(bc):
    r = [Fr(0)] * N
    for c, b in zip(bc, B):
        for i in range(N):
            r[i] += c * b[i]
    return r
for i in range(N):
    for j in range(N):
        MT[i][j] = to_basis(polmulmod(B[i], B[j]))
assert all(x.denominator == 1 for i in range(N) for j in range(N) for x in MT[i][j]), "basis not closed"
MTi = [[[int(x) for x in MT[i][j]] for j in range(N)] for i in range(N)]

def mulb(x, y, mod=None):
    r = [0] * N
    for i, a in enumerate(x):
        if a:
            for j, b in enumerate(y):
                if b:
                    for k, c in enumerate(MTi[i][j]):
                        r[k] += a * b * c
    if mod: r = [v % mod for v in r]
    return r

def det(M):
    M = [[Fr(x) for x in row] for row in M]
    n, d = len(M), Fr(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None: return Fr(0)
        if piv != c: M[c], M[piv] = M[piv], M[c]; d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return d

def norm(x):
    """x in basis coords (integers or Fractions): det of multiplication matrix"""
    cols = [mulb_fr(x, [1 if k == j else 0 for k in range(N)]) for j in range(N)]
    return det([[cols[j][i] for j in range(N)] for i in range(N)])

def mulb_fr(x, y):
    r = [Fr(0)] * N
    for i, a in enumerate(x):
        if a:
            for j, b in enumerate(y):
                if b:
                    for k, c in enumerate(MTi[i][j]):
                        r[k] += a * b * c
    return r

if __name__ == "__main__":
    # discriminant check: det(trace form)
    def trace(x):
        return sum(mulb_fr(x, [1 if k == j else 0 for k in range(N)])[j] for j in range(N))
    e = [[1 if k == j else 0 for k in range(N)] for j in range(N)]
    TM = [[trace(mulb(e[i], e[j])) for j in range(N)] for i in range(N)]
    print("field discriminant (trace form det):", det(TM))
    # structure of O/2O: radical via Frobenius kernel powers
    import itertools
    p = 2
    elems = list(itertools.product(range(p), repeat=N))
    def mulp(x, y): return tuple(mulb(list(x), list(y), p))
    def powp(x, k):
        r = tuple([1] + [0] * (N - 1))
        for _ in range(k): r = mulp(r, x)
        return r
    nil = [x for x in elems if powp(x, 6) == tuple([0] * N)]
    idem = [x for x in elems if mulp(x, x) == x]
    print("O/2O: #nilpotents", len(nil), "(=2^dim rad)", "#idempotents", len(idem))
    # primitive idempotents and residue degrees
    zero = tuple([0] * N)
    prim = [e1 for e1 in idem if e1 != zero and not any(e2 not in (zero, e1) and mulp(e1, e2) == e2 for e2 in idem)]
    for e1 in prim:
        comp = set(mulp(e1, x) for x in elems)        # component e1*R, local ring O/p^e
        nilc = [x for x in comp if powp(x, 6) == zero]
        import math
        dimR = int(math.log2(len(comp))); dimrad = int(math.log2(len(nilc)))
        f = dimR - dimrad
        print("component: dim", dimR, "residue degree f =", f, "e =", dimR // f)
