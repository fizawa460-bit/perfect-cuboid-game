#!/usr/bin/env python3
"""Stage33-05 finite-presentation descent front-end.

This does NOT identify the Hochschild--Serre d2 obstruction with the connecting
class computed below.  It computes the exact connecting homomorphism attached
to the Creutz--Viray G-module presentation

    0 -> R=im(x-alpha) -> LcE -> Br(Kc_bar)[2] -> 0

for the explicit quotient basis [J2,q1].  This is the first finite descent
filter: it tells us whether an invariant geometric Brauer class already has a
Galois-fixed lift in LcE.

The script also performs a Hilbert-90 style elimination of sqrt(2) from the J2
component squareclass.  This produces an explicit Q(i)-defined normalization
function representing J2 on B+.  No claim that the resulting generic central
simple algebra is unramified over Q(i), or that it descends to Q, is made here;
those arithmetic residue/descent checks are the next leaf.
"""
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# F2 presentation and connecting cocycle.
# Basis: [J1,J2,q1,q2,q3].
# Full-pair action from xalpha_pair_galois_repair.py:
# tau=cc=1 and ct adds J1 to q1,q2.
# ---------------------------------------------------------------------------

def addv(a,b):
    return [x ^ y for x,y in zip(a,b)]


def matvec(M,v):
    return [sum(M[r][c]*v[c] for c in range(len(v))) & 1 for r in range(len(M))]

I5 = [[1 if r == c else 0 for c in range(5)] for r in range(5)]
ct = [row[:] for row in I5]
ct[0][2] ^= 1
ct[0][3] ^= 1

J1 = [1,0,0,0,0]
J2 = [0,1,0,0,0]
q1v = [0,0,1,0,0]
q2v = [0,0,0,1,0]
q3v = [0,0,0,0,1]

# The exact image is known up to two immaterial J2 coefficients b,d.
# Verify uniformly that R is pointwise fixed and the quotient calculations do
# not depend on b,d.
rows_by_bd = {}
for b in (0,1):
    for d in (0,1):
        r0 = J1
        r1 = [0,b,1,1,0]
        r2 = [0,d,1,1,1]
        Rbasis = [r0,r1,r2]
        for r in Rbasis:
            assert matvec(ct,r) == r
        rows_by_bd[f"b={b},d={d}"] = Rbasis

# Connecting class of a quotient element represented by l is sigma(l)+l.
def delta_ct(lift):
    return addv(matvec(ct,lift),lift)

assert delta_ct(J2) == [0,0,0,0,0]
assert delta_ct(q1v) == J1

# Because the effective action on R is trivial, H^1(C2,R)=Hom(C2,R)=R and
# all 1-coboundaries are zero.  Therefore delta(q1)=J1 is nonzero and cannot
# be removed by changing q1 by any relation r in R.
for Rbasis in rows_by_bd.values():
    for mask in range(8):
        r = [0]*5
        for j in range(3):
            if (mask >> j) & 1:
                r = addv(r,Rbasis[j])
        assert delta_ct(addv(q1v,r)) == J1
        assert delta_ct(addv(J2,r)) == [0,0,0,0,0]

# ---------------------------------------------------------------------------
# Exact sqrt(2)-descent of the J2 component squareclass.
# ---------------------------------------------------------------------------
t,z = sp.symbols("t z")
s2 = sp.sqrt(2)
q = sp.expand(t**4-6*t**2+1)
r1 = 1+s2
r2 = -(1+s2)
r3 = s2-1
r4 = 1-s2
f2 = sp.cancel((t-r2)/(t-r4))


def reduce_z2(expr):
    expr = sp.together(sp.expand(expr))
    num, den = sp.fraction(expr)
    mod = sp.Poly(z**2-q,z,domain="EX")
    num = sp.rem(sp.Poly(num,z,domain="EX"),mod).as_expr()
    den = sp.rem(sp.Poly(den,z,domain="EX"),mod).as_expr()
    dencc = den.subs(z,-z)
    num = sp.rem(sp.Poly(sp.expand(num*dencc),z,domain="EX"),mod).as_expr()
    den = sp.rem(sp.Poly(sp.expand(den*dencc),z,domain="EX"),mod).as_expr()
    return sp.factor(sp.cancel(num/den))


def ct_expr(expr):
    # sqrt(2)->-sqrt(2), with t,z fixed since q is rational.
    return sp.expand(expr.xreplace({s2:-s2}))

h = sp.cancel((t-r3)*(t-r4)/z)
assert reduce_z2(h*ct_expr(h)-1) == 0

g = 1+h
assert reduce_z2(ct_expr(g)/g - 1/h) == 0

ellJ2 = reduce_z2(f2*g**2)
ellJ2_target = 2*(t**2+z-3)/(t**2-2*t-1)
assert reduce_z2(ellJ2-ellJ2_target) == 0
assert not ellJ2_target.has(s2)
assert reduce_z2(ellJ2_target/f2-g**2) == 0
assert reduce_z2(ct_expr(f2)/f2-h**2) == 0

cert = {
    "schema":"STAGE33_05_CV_PRESENTATION_CONNECTING_COCYCLE_V1",
    "basis_order":["J1","J2","q1","q2","q3"],
    "exact_sequence":"0 -> R=im(x-alpha) -> LcE -> Br(Kc_bar)[2] -> 0",
    "effective_nontrivial_presentation_action_generator":"ct",
    "R_action_under_ct":"identity for all b,d in the exact image normal form",
    "geometric_quotient_basis":["J2","q1"],
    "presentation_connecting_cocycle":{
        "J2":{"ct":"0","class_in_H1_C2_R":"0","fixed_LcE_lift_exists":True},
        "q1":{"ct":"J1","class_in_H1_C2_R":"nonzero","fixed_LcE_lift_exists":False},
    },
    "H1_effective_group_R":"H^1(C2,R)=R because the action is trivial over F2",
    "q1_connecting_class_independent_of_b_d":True,
    "warning":"This CV-presentation connecting class is not automatically the Hochschild-Serre d2 obstruction; q1 still requires lifting the J1 relation through NS/divisor data.",
    "J2_sqrt2_descent":{
        "original_component_squareclass":"f2=(t+1+sqrt(2))/(t-1+sqrt(2))",
        "hilbert90_norm1_factor":"h=((t-(sqrt(2)-1))*(t-(1-sqrt(2))))/z",
        "hilbert90_g":"1+h",
        "QI_defined_Bplus_representative":sp.sstr(ellJ2_target),
        "representative_has_no_sqrt2":True,
        "same_geometric_squareclass_as_J2":True,
    },
    "QI_defined_generic_function_for_J2_materialized":True,
    "QI_arithmetic_unramified_CSA_certified":False,
    "Q_descent_J2_certified":False,
    "Q_descent_q1_certified":False,
    "Q_relevant_surviving_dimension_certified":False,
    "next_exact_leaves":[
        "L33-05-J2-QI-ARITHMETIC-RESIDUES-AND-QI-OVER-Q-DESCENT",
        "L33-05-Q1-LIFT-CONNECTING-J1-THROUGH-NS-THEN-HS-D2",
    ],
    "theorem_credit":False,
    "endpoint_credit":False,
}
canonical = json.dumps(cert,sort_keys=True,separators=(",",":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT/"descent-presentation-cocycle.json").write_text(
    json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8"
)
print(json.dumps(cert,indent=2,sort_keys=True))
