"""E06, k = 4: S = <u -> -u, v -> -v> on C8: u^2 = (r^4+4)/4, v^2 = (r^4-4)/4, R = C8/S = P^1_r.  With r = sqrt2*rho the
branch values are B_u = {rho^4 = -1} (odd powers of zeta8) and B_v = {rho^4 = 1} (even powers); infinity is not a
branch value.  Same marked S-cover along psi1, psi2 = T∘psi1 forces q_chi(T psi1)/q_chi(psi1) to be squares for
chi = u, v (q_u = rho^4+1, q_v = rho^4-1; denominators (gamma rho+delta)^4 are squares), so every point of
Delta(T) = (B_u symdiff T^-1 B_u) ∪ (B_v symdiff T^-1 B_v) has even local degrees and |Delta| <= 4 + 4(g-1)/n.
|Delta| = 16 - 2j - h <= 4 forces j >= 4, so T sends some 3 points of B into B.  Exact arithmetic in Q(zeta8)."""
from fractions import Fraction as F
import itertools
class Z8:  # a0 + a1 z + a2 z^2 + a3 z^3, z^4 = -1
    __slots__ = ("c",)
    def __init__(s, c): s.c = tuple(F(x) for x in c)
    def __add__(s, o): return Z8([a + b for a, b in zip(s.c, o.c)])
    def __sub__(s, o): return Z8([a - b for a, b in zip(s.c, o.c)])
    def __neg__(s): return Z8([-a for a in s.c])
    def __mul__(s, o):
        r = [F(0)]*4
        for i, a in enumerate(s.c):
            if a == 0: continue
            for j, b in enumerate(o.c):
                if b == 0: continue
                k = i + j
                if k >= 4: r[k-4] -= a*b
                else: r[k] += a*b
        return Z8(r)
    def sigma(s, k):  # z -> z^k (k odd)
        r = Z8([0, 0, 0, 0])
        for i, a in enumerate(s.c):
            e = (i*k) % 8; term = [F(0)]*4
            if e < 4: term[e] = a
            else: term[e-4] = -a
            r = r + Z8(term)
        return r
    def inv(s):
        p = s.sigma(3) * s.sigma(5) * s.sigma(7); n = (s * p).c[0]
        return Z8([x / n for x in p.c])
    def __truediv__(s, o): return s * o.inv()
    def iszero(s): return all(x == 0 for x in s.c)
    def __eq__(s, o): return isinstance(o, Z8) and s.c == o.c
    def __hash__(s): return hash(s.c)
    def __repr__(s): return "z8" + repr(tuple(str(x) for x in s.c))
INF = "oo"
def zpow(k):
    k %= 8; c = [0]*4
    if k < 4: c[k] = 1
    else: c[k-4] = -1
    return Z8(c)
ZERO, ONE = Z8([0, 0, 0, 0]), Z8([1, 0, 0, 0])
PTS = {zpow(k): ("u" if k % 2 else "v") for k in range(8)}
B = list(PTS)
def apply(M, z):
    a, b, c, d = M
    if z == INF: return INF if c.iszero() else a / c
    num, den = a*z + b, c*z + d
    return INF if den.iszero() else num / den
def to01inf(z1, z2, z3):  # all finite here
    return (z2 - z3, -(z1*(z2 - z3)), z2 - z1, -(z3*(z2 - z1)))
def inv(M): a, b, c, d = M; return (d, -b, -c, a)
def mul(M, N):
    a, b, c, d = M; e, f, g, h = N
    return (a*e + b*g, a*f + b*h, c*e + d*g, c*f + d*h)
def normalize(M):
    piv = next(x for x in M if not x.iszero()); return tuple(x / piv for x in M)
cands = set()
src0 = B[:3]
for src in itertools.permutations(B, 3):
    S_ = to01inf(*src)
    for dst in itertools.permutations(B, 3):
        T = normalize(mul(inv(to01inf(*dst)), S_))
        a, b, c, d = T
        if not (a*d - b*c).iszero(): cands.add(T)
def preimage(T, p): return apply(inv(T), p)
from collections import Counter
dist = Counter(); keep = []
for T in cands:
    D = set()
    for chi in "uv":
        Bc = {p for p in B if PTS[p] == chi}
        D |= (Bc ^ {preimage(T, p) for p in Bc})
    j = sum(1 for p in B if apply(T, p) in PTS and PTS[apply(T, p)] == PTS[p])
    h = sum(1 for p in B if apply(T, p) in PTS and PTS[apply(T, p)] != PTS[p])
    if len(D) != 16 - 2*j - h: raise SystemExit("FAIL: counting identity")
    dist[len(D)] += 1
    if len(D) <= 4:
        inB = all(p in PTS for p in D); TinB = all(apply(T, p) in PTS for p in D)
        keep.append((len(D), j, h, inB, TinB))
print("k=4 candidate T:", len(cands), " |Delta| distribution:", sorted(dist.items()))
print("allowed (|Delta|<=4):", len(keep), Counter(keep))

ok = len(cands) == 8976 and len(keep) == 8 and all(k[0] == 0 for k in keep)
print("PASS" if ok else "FAIL")
if not ok: raise SystemExit(1)
