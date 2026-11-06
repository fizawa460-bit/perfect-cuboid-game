"""E08, k = 8, b = 2: no degree-2 map phi on R = P^1_t satisfies |Omega(phi)| <= 4.
Omega(phi) = union over chi in {a, b, e} of the odd locus of q_chi(phi)/q_chi, B = {±i} ∪ {±1} ∪ {0, oo}.
Lemma (E08 §2): |Omega| <= 4 forces at least five points of B to land in B (2j + h >= 10).  Two genuine degree-2
maps that agree at five points coincide (P Q' - P' Q is a binary quartic with five zeros), so for each choice of
five sources and five images the solution space must be one-dimensional.  Exact arithmetic in Q(i); the final odd
locus is computed with sympy only for the survivors of an exact necessary prefilter.
usage: python -I -O e08_k8_b2.py"""
import itertools, sys
from fractions import Fraction as F
class G:
    __slots__ = ("re", "im")
    def __init__(s, re, im=0): s.re, s.im = F(re), F(im)
    def __add__(s, o): return G(s.re + o.re, s.im + o.im)
    def __sub__(s, o): return G(s.re - o.re, s.im - o.im)
    def __mul__(s, o): return G(s.re*o.re - s.im*o.im, s.re*o.im + s.im*o.re)
    def __truediv__(s, o):
        n = o.re*o.re + o.im*o.im; return G((s.re*o.re + s.im*o.im)/n, (s.im*o.re - s.re*o.im)/n)
    def __eq__(s, o): return s.re == o.re and s.im == o.im
    def __hash__(s): return hash((s.re, s.im))
    def z(s): return s.re == 0 and s.im == 0
Z, O = G(0), G(1)
B = [(G(0, 1), O), (G(0, -1), O), (O, O), (G(-1), O), (Z, O), (O, Z)]   # homogeneous (x0 : x1)
LAB = "aabbee"
def row(src, dst):            # y1 P(x) - y0 Q(x) = 0, P = sum p_k X^k Y^(2-k)
    x0, x1 = src; y0, y1 = dst
    m = [x1*x1, x0*x1, x0*x0]
    return [y1*v for v in m] + [Z - y0*v for v in m]
def kernel(M):
    M = [r[:] for r in M]; n = len(M[0]); piv = []; r = 0
    for c in range(n):
        p = next((i for i in range(r, len(M)) if not M[i][c].z()), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]; inv = O / M[r][c]; M[r] = [x*inv for x in M[r]]
        for i in range(len(M)):
            if i != r and not M[i][c].z():
                f = M[i][c]; M[i] = [a - f*b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fc in free:
        v = [Z]*n; v[fc] = O
        for i, pc in enumerate(piv): v[pc] = Z - M[i][fc]
        basis.append(v)
    return basis
def same(p, q): return (p[0]*q[1] - p[1]*q[0]).z()
def ev(v, x):
    x0, x1 = x; m = [x1*x1, x0*x1, x0*x0]
    P = m[0]*v[0] + m[1]*v[1] + m[2]*v[2]; Q = m[0]*v[3] + m[1]*v[4] + m[2]*v[5]
    return (P, Q)
def res2(v):                  # resultant of the binary quadratic forms P, Q
    p0, p1, p2, q0, q1, q2 = v
    a = p2*q0 - p0*q2; return a*a - (p2*q1 - p1*q2)*(p1*q0 - p0*q1)
from collections import Counter
dims = Counter(); kers = {}
for srcs in itertools.combinations(range(6), 5):
    for imgs in itertools.product(range(6), repeat=5):
        K = kernel([row(B[s], B[d]) for s, d in zip(srcs, imgs)]); dims[len(K)] += 1
        if len(K) != 1: continue
        v = K[0]; pv = next(x for x in v if not x.z()); v = tuple(x / pv for x in v)
        kers[v] = 1
cnt = Counter(); surv = []
for v in kers:
    if res2(v).z(): cnt["degenerate"] += 1; continue
    j = h = 0
    for p, l in zip(B, LAB):
        y = ev(v, p)
        for q, m in zip(B, LAB):
            if same(y, q): j += (m == l); h += (m != l)
    if 2*j + h >= 10: surv.append(v)
    else: cnt["prefilter"] += 1
print("systems:", sum(dims.values()), "kernel dims:", dict(sorted(dims.items())), "distinct 1-dim kernels:", len(kers))
print("degenerate:", cnt["degenerate"], " removed by 2j+h>=10:", cnt["prefilter"], " survivors:", len(surv))
import sympy as sp
X, Y = sp.symbols("X Y")
def sx(g): return sp.Rational(g.re.numerator, g.re.denominator) + sp.I*sp.Rational(g.im.numerator, g.im.denominator)
QCH = {"a": lambda u, w: u**2 + w**2, "b": lambda u, w: w**2 - u**2, "e": lambda u, w: u*w}
def odd(f):
    r = sp.Integer(1)
    for g, m in sp.sqf_list(sp.Poly(f, X, Y, extension=sp.I))[1]:
        if m % 2: r *= g.as_expr()
    return r
om = Counter()
for v in surv:
    c = [sx(x) for x in v]
    P = c[0]*Y**2 + c[1]*X*Y + c[2]*X**2; Q = c[3]*Y**2 + c[4]*X*Y + c[5]*X**2
    L = sp.Integer(1)
    for ch in "abe":
        o = odd(sp.expand(QCH[ch](P, Q) * QCH[ch](X, Y)))
        L = o if L == 1 else (sp.lcm(L, o, X, Y, extension=sp.I) if o != 1 else L)
    om[sp.Poly(L, X, Y).total_degree() if L != 1 else 0] += 1
print("|Omega| over genuine survivors:", dict(om))
allowed = sum(n for k, n in om.items() if k <= 4)
ok = (sum(dims.values()) == 46656 and dict(dims) == {1: 45576, 2: 1044, 3: 36} and len(kers) == 26370
      and cnt["degenerate"] == 810 and cnt["prefilter"] == 25344 and len(surv) == 216 and dict(om) == {8: 216}
      and allowed == 0)
print("allowed (|Omega| <= 4):", allowed)
print("PASS" if ok else "FAIL")
if not ok: raise SystemExit(1)
