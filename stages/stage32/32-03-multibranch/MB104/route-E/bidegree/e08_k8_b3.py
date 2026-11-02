"""E08, k = 8, b = 3: no degree-3 map phi on R = P^1_t satisfies |Omega(phi)| <= 4.
Lemma (E08 §2): for b = 3, |Omega| <= 4 forces j = 6 (all six points of B go label-preservingly into B, with odd local
degree) and Sigma o = 10, i.e. exactly four critical values, all in B, each fiber of type (2,1).  For each of the 64
label-preserving assignments the 6x8 linear system has a kernel V; on P(V) we impose
disc_X(y1 P - y0 Q) proportional to the product of the four chosen points of B, and keep only genuine degree-3 maps.
A positive control (phi = t(t^2+3)/(3t^2+1), critical values +-1 doubled) checks that the solver finds a known map.
usage: python -I -O e08_k8_b3.py"""
import itertools
import sympy as sp
from collections import Counter
I = sp.I
X, Y, y0, y1, lam = sp.symbols("X Y y0 y1 lam")
B = [(I, 1), (-I, 1), (1, 1), (-1, 1), (0, 1), (1, 0)]
LAB = "aabbee"


def row(src, dst):
    m = [src[0]**k * src[1]**(3 - k) for k in range(4)]
    return [dst[1] * v for v in m] + [-dst[0] * v for v in m]


def forms(v):
    P = sp.expand(sum(v[k] * X**k * Y**(3 - k) for k in range(4)))
    Q = sp.expand(sum(v[4 + k] * X**k * Y**(3 - k) for k in range(4)))
    return P, Q


def disc3(f):
    p = sp.Poly(f, X, Y)
    c = lambda i: p.coeff_monomial(X**i * Y**(3 - i))
    a, b, cc, d = c(3), c(2), c(1), c(0)
    return sp.expand(b**2 * cc**2 - 4 * a * cc**3 - 4 * b**3 * d - 27 * a**2 * d**2 + 18 * a * b * cc * d)


def coprime(P, Q):
    return sp.gcd(sp.Poly(P, X, Y, extension=I), sp.Poly(Q, X, Y, extension=I)).total_degree() == 0


def generic_degenerate(ns):
    """True iff every member of P(V) has a common factor (checked on the generic member)."""
    ms = sp.symbols(f"m0:{len(ns)}")
    P, Q = forms([sp.expand(sum(m * n[i] for m, n in zip(ms, ns))) for i in range(8)])
    g = sp.gcd(sp.Poly(P, X, Y, *ms, extension=I), sp.Poly(Q, X, Y, *ms, extension=I))
    return sp.Poly(g.as_expr(), X, Y).total_degree() > 0


QCH = {"a": lambda u, w: u**2 + w**2, "b": lambda u, w: w**2 - u**2, "e": lambda u, w: u * w}


def omega(P, Q):
    L = sp.Integer(1)
    for ch in "abe":
        o = sp.Integer(1)
        for g, m in sp.sqf_list(sp.Poly(sp.expand(QCH[ch](P, Q) * QCH[ch](X, Y)), X, Y, extension=I))[1]:
            if m % 2:
                o *= g.as_expr()
        if o != 1:
            L = o if L == 1 else sp.lcm(L, o, X, Y, extension=I)
    return sp.Poly(L, X, Y).total_degree() if L != 1 else 0


KER = {}


def kernel(imgs):
    if imgs not in KER:
        KER[imgs] = sp.Matrix([row(B[s], B[d]) for s, d in zip(range(6), imgs)]).nullspace()
    return KER[imgs]


def solve(imgs, targets):
    """Genuine degree-3 maps with B[s] -> B[imgs[s]] and branch form proportional to prod(targets)."""
    ns = kernel(imgs)
    if len(ns) != 2:
        return len(ns), ("DEGENERATE" if generic_degenerate(ns) else "GENUINE-FAMILY")
    Fm = sp.Poly(sp.prod([B[q][1] * y0 - B[q][0] * y1 for q in targets]), y0, y1)
    fc = [Fm.coeff_monomial(y0**i * y1**(4 - i)) for i in range(5)]
    found = []
    for chart in ([n0 + lam * n1 for n0, n1 in zip(ns[0], ns[1])], list(ns[1])):   # lam in C, and lam = oo
        P, Q = forms([sp.expand(x) for x in chart])
        D = sp.Poly(disc3(sp.expand(y1 * P - y0 * Q)), y0, y1)
        dc = [sp.expand(D.coeff_monomial(y0**i * y1**(4 - i))) for i in range(5)]
        eqs = [e for e in (sp.expand(dc[i] * fc[j] - dc[j] * fc[i]) for i in range(5) for j in range(i + 1, 5)) if e != 0]
        if not eqs:
            if P.has(lam) or Q.has(lam):
                if not generic_degenerate(ns):
                    return 2, "GENUINE-FAMILY"
            elif coprime(P, Q) and disc3(sp.expand(y1 * P - y0 * Q)) != 0:
                found.append((P, Q))
            continue
        if not (P.has(lam) or Q.has(lam)):
            continue
        g = eqs[0]
        for e in eqs[1:]:
            g = sp.gcd(g, e, extension=I)
        g = sp.Poly(g, lam, extension=I)
        if g.degree() <= 0:
            continue
        rts = sp.roots(g, multiple=True)
        if len(rts) != g.degree():
            return 2, "UNSOLVED"
        for r in set(rts):
            PP, QQ = sp.expand(P.subs(lam, r)), sp.expand(Q.subs(lam, r))
            if coprime(PP, QQ) and disc3(sp.expand(y1 * PP - y0 * QQ)) != 0:
                found.append((PP, QQ))
    return 2, found


ok = True
# positive control: t(t^2+3)/(3t^2+1) maps i->-i, -i->i, +-1->+-1, 0->0, oo->oo; branch form (y0-y1)^2 (y0+y1)^2
_, fnd = solve((1, 0, 2, 3, 4, 5), [2, 2, 3, 3])
ctrl = isinstance(fnd, list) and any(
    sp.simplify(sp.cancel(P.subs(Y, 1) / Q.subs(Y, 1)) - X * (X**2 + 3) / (3 * X**2 + 1)) == 0 for P, Q in fnd)
print("positive control found:", ctrl)
ok &= ctrl
dims = Counter()
res = Counter()
hits = []
for imgs in itertools.product(*[[q for q in range(6) if LAB[q] == LAB[s]] for s in range(6)]):
    dims[len(kernel(imgs))] += 1
    for four in itertools.combinations(range(6), 4):
        d, r = solve(imgs, list(four))
        if isinstance(r, str):
            res[r] += 1
            continue
        for P, Q in r:
            hits.append((imgs, four, omega(P, Q)))
print("kernel dims over the 64 assignments:", dict(dims))
print("non-generic outcomes:", dict(res), " genuine maps found:", len(hits))
ok &= dict(dims) == {2: 60, 3: 4} and dict(res) == {"DEGENERATE": 4 * 15} and not hits
print("PASS" if ok else "FAIL")
if not ok:
    raise SystemExit(1)
