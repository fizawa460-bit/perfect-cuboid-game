#!/usr/bin/env python3
import hashlib
import json
import pathlib

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parent
u1, v1, u2, v2 = sp.symbols("u1 v1 u2 v2")
I = sp.I
A1 = v1**2-u1**2
A2 = v2**2-u2**2
X = u1*v1*A2
Y = u2*v2*A1
F = sp.expand(X**2+Y**2)
Bp = sp.expand(X+I*Y)
Bm = sp.expand(X-I*Y)

assert sp.expand(Bp*Bm-F) == 0
assert sp.conjugate(Bp).xreplace({sp.conjugate(u1):u1, sp.conjugate(v1):v1,
                                  sp.conjugate(u2):u2, sp.conjugate(v2):v2}) == Bm

# Every monomial of B+ and B- has bidegree (2,2) in the two P1 factors.
def bidegrees(poly):
    P = sp.Poly(poly, u1, v1, u2, v2, extension=I)
    out = set()
    for exps, _ in P.terms():
        out.add((exps[0]+exps[1], exps[2]+exps[3]))
    return sorted(out)

assert bidegrees(Bp) == [(2, 2)]
assert bidegrees(Bm) == [(2, 2)]

# B+ intersect B- iff X=Y=0. The factor structure gives exactly four corners
# plus A1=A2=0, which gives four finite sign points.
points = []
for p1 in [(0,1),(1,0)]:
    for p2 in [(0,1),(1,0)]:
        points.append((p1,p2,"corner"))
for e1 in (-1,1):
    for e2 in (-1,1):
        points.append(((e1,1),(e2,1),"A1=A2=0"))
assert len(points) == 8 and len({(a,b) for a,b,_ in points}) == 8
for (a,b), (c,d), _ in points:
    subs = {u1:a, v1:b, u2:c, v2:d}
    assert sp.expand(X.subs(subs)) == 0
    assert sp.expand(Y.subs(subs)) == 0

# Exact local Jacobian determinants for (X,Y), one chart per corner and the
# v1=v2=1 chart for the four A1=A2 points. Nonzero means B+ and B- cross transversely.
t, s, q, r = sp.symbols("t s q r")
local_models = {
    "00": (t*(1-s**2), s*(1-t**2), {t:0,s:0}),
    "0inf": (t*(r**2-1), r*(1-t**2), {t:0,r:0}),
    "inf0": (q*(1-s**2), s*(q**2-1), {q:0,s:0}),
    "infinf": (q*(r**2-1), r*(q**2-1), {q:0,r:0}),
}
dets = {}
for name, (lx, ly, pt) in local_models.items():
    vars_ = list(pt.keys())
    det = sp.Matrix([[sp.diff(lx,z) for z in vars_],
                     [sp.diff(ly,z) for z in vars_]]).det().subs(pt)
    dets[name] = int(det)
    assert det != 0

finite_dets = {}
xf = t*(1-s**2)
yf = s*(1-t**2)
Jf = sp.Matrix([[sp.diff(xf,t),sp.diff(xf,s)],
                [sp.diff(yf,t),sp.diff(yf,s)]]).det()
for e1 in (-1,1):
    for e2 in (-1,1):
        det = sp.expand(Jf.subs({t:e1,s:e2}))
        finite_dets[f"{e1},{e2}"] = int(det)
        assert det != 0

certificate = {
    "schema":"STAGE33_05_BRANCH_GALOIS_REGRESSION_V1",
    "F_factorization_over_Qi":"(X+iY)(X-iY)",
    "branch_component_bidegrees":[2,2],
    "complex_conjugation_swaps_branch_components":True,
    "branch_component_intersection_count":8,
    "intersection_types":{"corners":4,"A1_equals_A2_zero":4},
    "corner_jacobian_determinants":dets,
    "finite_jacobian_determinants":finite_dets,
    "all_intersections_transverse":True,
    "brauer_action_inferred_from_component_swap":False,
    "next_exact_leaf":"L33-05-CV-PRESENTATION",
}
raw = json.dumps(certificate, indent=2, sort_keys=True)+"\n"
(ROOT/"branch-galois-certificate.json").write_text(raw, encoding="utf-8")
print(raw, end="")
print("CERTIFICATE_SHA256="+hashlib.sha256(raw.encode()).hexdigest())
