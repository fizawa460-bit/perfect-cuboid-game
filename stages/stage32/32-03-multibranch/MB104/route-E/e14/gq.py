# Exact arithmetic in Q(i) and Q(i)[t] (no external libraries).
from fractions import Fraction as Fr
class G:
    __slots__ = ("a", "b")
    def __init__(s, a=0, b=0): s.a = Fr(a); s.b = Fr(b)
    def __add__(s, o): o = G.c(o); return G(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __neg__(s): return G(-s.a, -s.b)
    def __sub__(s, o): o = G.c(o); return G(s.a - o.a, s.b - o.b)
    def __rsub__(s, o): return G.c(o) - s
    def __mul__(s, o): o = G.c(o); return G(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def inv(s): n = s.a * s.a + s.b * s.b; return G(s.a / n, -s.b / n)
    def __truediv__(s, o): return s * G.c(o).inv()
    def __eq__(s, o): o = G.c(o); return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def iszero(s): return s.a == 0 and s.b == 0
    def __repr__(s): return "(%s, %s)" % (s.a, s.b)
    @staticmethod
    def c(o): return o if isinstance(o, G) else G(o, 0)
I = G(0, 1)
# polynomials: lists of G, lowest degree first, no trailing zeros
def trim(p):
    p = list(p)
    while p and p[-1].iszero(): p.pop()
    return p
def P(*cs): return trim([G.c(c) for c in cs])
def deg(p): return len(p) - 1
def padd(p, q):
    n = max(len(p), len(q)); return trim([(p[i] if i < len(p) else G()) + (q[i] if i < len(q) else G()) for i in range(n)])
def pscale(p, c): return trim([x * c for x in p])
def psub(p, q): return padd(p, pscale(q, -1))
def pmul(p, q):
    if not p or not q: return []
    r = [G() for _ in range(len(p) + len(q) - 1)]
    for i, x in enumerate(p):
        if x.iszero(): continue
        for j, y in enumerate(q): r[i + j] = r[i + j] + x * y
    return trim(r)
def pder(p): return trim([p[i] * i for i in range(1, len(p))])
def pdivmod(p, q):
    p = list(p); out = [G() for _ in range(max(len(p) - len(q) + 1, 0))]; li = q[-1].inv()
    while len(p) >= len(q) and p:
        c = p[-1] * li; d = len(p) - len(q); out[d] = c
        for i, y in enumerate(q): p[i + d] = p[i + d] - c * y
        p = trim(p)
    return trim(out), p
def pgcd(p, q):
    while q: p, q = q, pdivmod(p, q)[1]
    return pscale(p, p[-1].inv()) if p else p
def peval(p, x):
    r = G()
    for c in reversed(p): r = r * x + c
    return r
def pcompose(p, q):                     # p(q(t))
    r = []
    for c in reversed(p): r = padd(pmul(r, q), [c])
    return r
