"""E08, k = 4, b = 2: no degree-2 map phi on R = P^1_rho satisfies |Omega(phi)| <= 4.
B_u = odd powers of zeta8 (q_u = rho^4 + 1), B_v = mu_4 (q_v = rho^4 - 1); infinity is not a branch value.
Lemma (E08 §2): |Omega| <= 4 forces j = 8 (all eight points label-preservingly into B).  Five points already fix a
genuine degree-2 map, so we solve on the first five points (1-dim kernels only) and check the other three.
usage: python -I -O e08_k4_b2.py"""
import itertools
import sympy as sp
from collections import Counter
X, Y = sp.symbols("X Y")
EXT = [sp.sqrt(2), sp.I]
z = sp.sqrt(2) / 2 + sp.I * sp.sqrt(2) / 2
B = [(sp.expand(z**k), 1) for k in range(8)]
LAB = ["v" if k % 2 == 0 else "u" for k in range(8)]


def row(src, dst):
    m = [src[0]**k * src[1]**(2 - k) for k in range(3)]
    return [sp.expand(dst[1] * v) for v in m] + [sp.expand(-dst[0] * v) for v in m]


QCH = {"u": lambda a, c: a**4 + c**4, "v": lambda a, c: a**4 - c**4}


def odd(f):
    r = sp.Integer(1)
    for g, m in sp.sqf_list(sp.Poly(f, X, Y, extension=EXT))[1]:
        if m % 2:
            r *= g.as_expr()
    return sp.expand(r)


found = {}
nk = 0
for imgs in itertools.product(*[[q for q in range(8) if LAB[q] == LAB[s]] for s in range(5)]):
    ns = sp.Matrix([row(B[s], B[d]) for s, d in zip(range(5), imgs)]).nullspace(simplify=True)
    if len(ns) != 1:
        continue
    nk += 1
    v = list(ns[0])
    pv = next(x for x in v if sp.simplify(x) != 0)
    v = [sp.radsimp(sp.simplify(x / pv)) for x in v]
    P = sp.expand(sum(v[k] * X**k * Y**(2 - k) for k in range(3)))
    Q = sp.expand(sum(v[3 + k] * X**k * Y**(2 - k) for k in range(3)))
    if sp.gcd(sp.Poly(P, X, Y, extension=EXT), sp.Poly(Q, X, Y, extension=EXT)).total_degree() > 0:
        continue
    good = True
    for s in range(5, 8):
        pv_ = sp.simplify(P.subs({X: B[s][0], Y: 1}))
        qv = sp.simplify(Q.subs({X: B[s][0], Y: 1}))
        if qv == 0 or not any(sp.simplify(pv_ / qv - B[q][0]) == 0 for q in range(8) if LAB[q] == LAB[s]):
            good = False
            break
    if good:
        found[tuple(sp.srepr(x) for x in v)] = (P, Q)
oms = []
for P, Q in found.values():
    L = sp.lcm(odd(sp.expand(QCH["u"](P, Q) * QCH["u"](X, Y))), odd(sp.expand(QCH["v"](P, Q) * QCH["v"](X, Y))),
               X, Y, extension=EXT)
    oms.append(sp.Poly(L, X, Y).total_degree())
print("1-dim kernels:", nk, " label-preserving genuine maps on all 8 points:", len(found), " |Omega|:", dict(Counter(oms)))
ok = nk == 1016 and len(found) == 32 and dict(Counter(oms)) == {8: 32}
print("PASS" if ok else "FAIL")
if not ok:
    raise SystemExit(1)
