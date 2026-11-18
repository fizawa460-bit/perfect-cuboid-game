"""Exact slack-0 Hurwitz numbers by characters (Murnaghan-Nakayama) + removal of disconnected covers.
H(n,t) = (#transitive tuples (g1..g6), g_y involution with t_y transpositions, prod = 1) / n!"""
import sys, itertools
from fractions import Fraction
from functools import lru_cache
from math import factorial, comb
def partitions(n, m=None):
    if m is None: m = n
    if n == 0: yield (); return
    for k in range(min(n, m), 0, -1):
        for p in partitions(n - k, k): yield (k,) + p
@lru_cache(None)
def chi(lam, mu):  # MN rule, mu a tuple of cycle lengths
    if not mu: return 1 if sum(lam) == 0 else 0
    r, rest = mu[0], mu[1:]
    # remove border strips of size r: use beta-numbers
    L = len(lam); beta = [lam[i] + L - 1 - i for i in range(L)]
    tot = 0
    for i, b in enumerate(beta):
        nb = b - r
        if nb < 0 or nb in beta: continue
        sign = (-1) ** sum(1 for c in beta if nb < c < b)
        newb = sorted([c for c in beta if c != b] + [nb], reverse=True)
        Ln = len(newb); nl = tuple(x for x in (newb[i] - (Ln - 1 - i) for i in range(Ln)) if x > 0)
        tot += sign * chi(nl, rest)
    return tot
def csize(n, t): return factorial(n) // (2 ** t * factorial(t) * factorial(n - 2 * t))
@lru_cache(None)
def A(n, t):  # all tuples
    if n == 0: return 1 if all(x == 0 for x in t) else 0
    if any(2 * x > n for x in t): return 0
    s = Fraction(0)
    for lam in partitions(n):
        d = chi(lam, (1,) * n); pr = Fraction(1)
        for x in t: pr *= Fraction(chi(lam, (2,) * x + (1,) * (n - 2 * x)), d)
        s += pr * d * d
    r = s / factorial(n)
    for x in t: r *= csize(n, x)
    assert r.denominator == 1; return int(r)
@lru_cache(None)
def C(n, t):  # transitive tuples
    tot = A(n, t)
    for k in range(1, n):  # block containing point 0 has size k
        for tp in itertools.product(*[range(x + 1) for x in t]):
            if any(2 * x > k for x in tp) or any(2 * (x - y) > n - k for x, y in zip(t, tp)): continue
            tot -= comb(n - 1, k - 1) * C(k, tp) * A(n - k, tuple(x - y for x, y in zip(t, tp)))
    return tot
if __name__ == '__main__':
    n = int(sys.argv[1]); tot = Fraction(0); out = {}
    for t in itertools.product(range(n // 2 + 1), repeat=6):
        if sum(t) != 2 * n - 2: continue
        h = Fraction(C(n, t), factorial(n)); out[t] = h; tot += h
    print(n, float(tot))
    if len(sys.argv) > 2:
        import pickle; pickle.dump(out, open(sys.argv[2], 'wb'))
