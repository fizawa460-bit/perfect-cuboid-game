"""CHECK-03: nullity of bidegree (u,u) forms with multiplicity >= mu at the 12 matched points of B x B, mod p = 998244353 (i in F_p).
Reproduces the table of the external reply (REPLY-04 A, first given in the reply to request 3). usage: python -I nullity_check.py > nullity_check.out
"""
# nullity of "bidegree (u,u) forms with multiplicity >= mu at the 12 matched points of BxB", mod p (p = 1 mod 4)
import itertools, sys

p = 998244353  # = 1 mod 4
I = pow(3, (p - 1) // 4, p); assert I * I % p == p - 1
B = {"e": [(0, 1), (1, 0)], "b": [(1, 1), (p - 1, 1)], "a": [(I, 1), (p - I, 1)]}
pts = [(x, y) for l in B for x in B[l] for y in B[l]]
def rank(M):
    M = [r[:] for r in M]; r = 0; ncol = len(M[0]) if M else 0
    for c in range(ncol):
        piv = next((i for i in range(r, len(M)) if M[i][c] % p), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]; iv = pow(M[r][c], p - 2, p)
        M[r] = [v * iv % p for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]:
                f = M[i][c]; M[i] = [(vi - f * vr) % p for vi, vr in zip(M[i], M[r])]
        r += 1
    return r
from math import comb
def cond(u, mu):
    mons = [(i, j) for i in range(u + 1) for j in range(u + 1)]  # x0^i x1^(u-i) y0^j y1^(u-j)
    rows = []
    for (X, Y) in pts:
        # local chart: pick affine coord; point (x0:x1) with x1 != 0 -> x=x0/x1 + s ; else x1/x0
        for da in range(mu):
            for db in range(mu - da):
                row = []
                for (i, j) in mons:
                    def coef(P, k, d):  # d-th Taylor coeff at P of monomial t0^k t1^(u-k), dehomogenised
                        t0, t1 = P
                        if t1:  # set t1=1, t0 = t0 + s : (t0+s)^k
                            return comb(k, d) * pow(t0, k - d, p) if d <= k else 0
                        else:   # t0=1, t1 = s : s^(u-k)
                            return 1 if u - k == d else 0
                    row.append(coef(X, i, da) * coef(Y, j, db) % p)
                rows.append(row)
    return (u + 1) ** 2 - rank(rows)
for u, mu in [(1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3)]:
    print((u, mu), "nullity", cond(u, mu))
