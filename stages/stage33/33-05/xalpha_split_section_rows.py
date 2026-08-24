#!/usr/bin/env python3
"""Exact Stage33-05 x-alpha progress certificate.

Two split horizontal divisors on the generic ruled fiber give two independent
Creutz--Viray x-alpha rows.  Together with the already locked rank-3 image,
this reduces the unknown NS restriction to one nonzero graph direction.  The
previously materialized extension-mixing matrices then act trivially on the
2-dimensional Brauer quotient, independently of which of the seven graph
lines is the final NS relation.

This does NOT identify that final graph line and does NOT certify descent of
geometric invariant classes to Br(K_c)/Br(Q).
"""
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
t, s = sp.symbols("t s")
i = sp.I
s2 = sp.sqrt(2)

# Generic fiber of the ruled K3 model, after y=w/t.
F = sp.expand(t**2 * (1-s**2)**2 + s**2 * (1-t**2)**2)
Gp = sp.expand(t*(1-s**2) + i*s*(1-t**2))
Gm = sp.expand(t*(1-s**2) - i*s*(1-t**2))

# Two exact split sections.
assert sp.factor(F.subs(s, 1)) == (t-1)**2 * (t+1)**2
assert sp.factor(F.subs(s, t)) == 2*t**2 * (t-1)**2 * (t+1)**2
assert sp.factor(Gp.subs(s, 1)) == -i*(t-1)*(t+1)
assert sp.factor(Gm.subs(s, 1)) ==  i*(t-1)*(t+1)
assert sp.factor(Gp.subs(s, t)) == -(1+i)*t*(t-1)*(t+1)
assert sp.factor(Gm.subs(s, t)) == (-1+i)*t*(t-1)*(t+1)

# Common branch normalization in the elliptic model E: y^2=x^3-x.
# The odd node labels agree with cv_exact_graph_lifts_and_galois.py; even
# labels are their negatives under the common-normalization identification.
def simp(x):
    return sp.simplify(x)

def neg(P):
    return None if P is None else (simp(P[0]), simp(-P[1]))

def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if simp(x1-x2) == 0:
        if simp(y1+y2) == 0:
            return None
        m = simp((3*x1**2-1)/(2*y1))
    else:
        m = simp((y2-y1)/(x2-x1))
    x3 = simp(m**2-x1-x2)
    y3 = simp(m*(x1-x3)-y1)
    return (x3, y3)

def addmany(points):
    out = None
    for P in points:
        out = add(out, P)
    return out

P1 = (-s2-1, -i*(2+s2))
P3 = (1-s2, 2-s2)
P5 = (1+s2, -2-s2)
P7 = (-1+s2, i*(2-s2))
E = {
    "e1": P1, "e2": neg(P1),
    "e3": P3, "e4": neg(P3),
    "e5": P5, "e6": neg(P5),
    "e7": P7, "e8": neg(P7),
}
for P in E.values():
    assert simp(P[1]**2 - (P[0]**3-P[0])) == 0

J1 = (sp.Integer(0), sp.Integer(0))
J2 = (sp.Integer(1), sp.Integer(0))
J12 = (sp.Integer(-1), sp.Integer(0))

# For s=1:
#   div(x-alpha ratio)=e3+e5-e4-e6.
# For s=t the common e1/e8 intersections cancel between the two branch
# components and
#   div(x-alpha ratio)=e3+e6-e4-e5.
# The diagonal K(t)^* factor k=t^2-1 has
#   div(k)=e3+e4+e5+e6-2e7-2e8.
# Removing k leaves an even divisor.  Its half-divisor class on E determines
# the Jac[2] coordinate exactly.
half_s1 = addmany([neg(E["e4"]), neg(E["e6"]), E["e7"], E["e8"]])
half_st = addmany([neg(E["e4"]), neg(E["e5"]), E["e7"], E["e8"]])
assert all(simp(a-b) == 0 for a, b in zip(half_s1, J1))
assert all(simp(a-b) == 0 for a, b in zip(half_st, J12))

# Basis order frozen by cv_exact_graph_lifts_and_galois.py:
# [J1,J2,q1,q2,q3].
xalpha_rows = [
    [1,0,0,0,0],       # s=1  -> J1
    [1,1,0,0,0],       # s=t  -> J1+J2
]

def rank2(rows):
    a = [r[:] for r in rows]
    rr = 0
    for c in range(len(a[0])):
        p = next((j for j in range(rr, len(a)) if a[j][c]), None)
        if p is None:
            continue
        a[rr], a[p] = a[p], a[rr]
        for j in range(len(a)):
            if j != rr and a[j][c]:
                a[j] = [x ^ y for x, y in zip(a[j], a[rr])]
        rr += 1
    return rr

assert rank2(xalpha_rows) == 2
locked_xalpha_image_dimension = 3
remaining_relation_dimension = locked_xalpha_image_dimension - rank2(xalpha_rows)
assert remaining_relation_dimension == 1

# Since J1,J2 are already in im(x-alpha), row operations normalize the final
# relation to one nonzero graph vector [0,0,a,b,c].
graph_line_candidates = [[0,0,*v] for v in itertools.product((0,1), repeat=3) if any(v)]
assert len(graph_line_candidates) == 7
for row in graph_line_candidates:
    assert rank2(xalpha_rows + [row]) == 3

# Exact Galois action already materialized on [J1,J2,q1,q2,q3].  Column
# convention: tau/ct may add only Jac directions to q_i; cc is identity.
I5 = [[1 if r == c else 0 for c in range(5)] for r in range(5)]
tau = [r[:] for r in I5]
tau[0][2] ^= 1
tau[0][3] ^= 1
ct = [r[:] for r in I5]
ct[1][2] ^= 1
ct[0][3] ^= 1
ct[1][3] ^= 1
cc = [r[:] for r in I5]

# Modulo the already certified J1,J2 relation plane, all three generators are
# the identity on the graph quotient.  Hence after quotienting by any one of
# the seven possible residual graph lines, the 2D geometric Brauer quotient
# still has identity action.
for M in (tau, ct, cc):
    assert [row[2:] for row in M[2:]] == [[1,0,0],[0,1,0],[0,0,1]]

brauer_quotient_dimension = 5 - locked_xalpha_image_dimension
assert brauer_quotient_dimension == 2

cert = {
    "schema": "STAGE33_05_XALPHA_TWO_ROWS_AND_QUOTIENT_ACTION_V1",
    "generic_fiber": "(w/t)^2=F/t^2",
    "basis_order": ["J1","J2","q1","q2","q3"],
    "split_divisor_xalpha_rows": [
        {"divisor":"s=1", "row":[1,0,0,0,0], "class":"J1=(0,0) on y^2=x^3-x"},
        {"divisor":"s=t", "row":[1,1,0,0,0], "class":"J1+J2=(-1,0) on y^2=x^3-x"},
    ],
    "explicit_xalpha_row_count": 2,
    "explicit_xalpha_row_rank": 2,
    "locked_xalpha_image_dimension": locked_xalpha_image_dimension,
    "remaining_xalpha_relation_dimension": remaining_relation_dimension,
    "remaining_relation_normal_form": "[0,0,a,b,c], (a,b,c) nonzero",
    "remaining_graph_line_candidate_count": len(graph_line_candidates),
    "remaining_graph_line_candidates": graph_line_candidates,
    "full_xalpha_matrix_materialized": False,
    "brauer_quotient_dimension": brauer_quotient_dimension,
    "galois_generators_checked": ["tau","ct","cc"],
    "galois_action_mod_Jac_relation_plane": "identity on q1,q2,q3",
    "geometric_Br2_quotient_action_exact": True,
    "geometric_Br2_quotient_action": "identity",
    "geometric_Br2_GQ_invariant_dimension": 2,
    "descent_obstruction_accounted": False,
    "Q_defined_arithmetic_representatives_materialized": False,
    "Q_relevant_surviving_dimension_certified": False,
    "next_exact_leaf": "L33-05-RESTRICT-PICKARD-GENERATORS-SELECT-1-OF-7-GRAPH-LINES",
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT/"xalpha-two-rows-quotient-action.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(cert, indent=2, sort_keys=True))
