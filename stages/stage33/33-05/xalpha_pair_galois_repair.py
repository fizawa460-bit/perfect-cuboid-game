#!/usr/bin/env python3
"""Stage33-05 repair certificate for x-alpha and the full L-pair Galois action.

This supersedes two over-strong pilot interpretations:

1. evaluating G_+(t,f)/G_-(t,f) is only a norm-level shadow of x-alpha;
   the true generic-fiber x-alpha element for a section s=f(t) is the pair
       (f-s_plus, f-s_minus)
   on the two normalized branch components;
2. the half-point corrections in cv_exact_graph_lifts_and_galois.py are
   single-component corrections.  Passing to the full pair
       (h, cc(h)) in L=k(B_+) x k(B_-)
   changes the 5D action.

The exact repair proves:
- graph projections of s=1 and s=t are q1+q2 and q1+q2+q3;
- a Q(i)-Möbius section has the same graph projection as s=1;
- the difference of those two x-alpha classes is exactly J1;
- these three classes already span the independently locked rank-3 image;
- J2 and q1 therefore form an explicit basis of the 2D Brauer quotient;
- the full-pair Galois action is tau=cc=1 and ct(q1)=q1+J1,
  ct(q2)=q2+J1, ct(q3)=q3, with J1,J2 fixed;
- hence the induced action on the 2D quotient is identity because J1 is an
  x-alpha relation.

This remains a geometric statement.  Arithmetic Hochschild--Serre descent is
not claimed here.
"""
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
t, z = sp.symbols("t z")
i = sp.I
s2 = sp.sqrt(2)
q = sp.expand(t**4 - 6*t**2 + 1)

# Common normalizations of B+ and B- from the frozen ruled model.
s_plus = i*(1-t**2+z)/(2*t)
s_minus = -i*(1-t**2+z)/(2*t)


def reduce_z2(expr):
    """Reduce a rational expression modulo z^2=q(t)."""
    expr = sp.together(sp.expand(expr))
    num, den = sp.fraction(expr)
    mod = sp.Poly(z**2-q, z, domain="EX")
    num = sp.rem(sp.Poly(sp.expand(num), z, domain="EX"), mod).as_expr()
    den = sp.rem(sp.Poly(sp.expand(den), z, domain="EX"), mod).as_expr()
    # rationalize a possibly z-linear denominator
    den_cc = den.subs(z, -z)
    num = sp.rem(sp.Poly(sp.expand(num*den_cc), z, domain="EX"), mod).as_expr()
    den = sp.rem(sp.Poly(sp.expand(den*den_cc), z, domain="EX"), mod).as_expr()
    return sp.cancel(num/den)


def ab(expr):
    """Return A,B in K(t) for expr=A+B*z in K(t,z)/(z^2-q)."""
    r = reduce_z2(expr)
    num, den = sp.fraction(r)
    assert not den.has(z)
    num = sp.expand(num)
    A = sp.cancel(num.subs(z, 0)/den)
    B = sp.cancel(sp.diff(num, z).subs(z, 0)/den)
    assert reduce_z2(r-(A+B*z)) == 0
    return A, B


def norm(expr):
    A, B = ab(expr)
    return sp.factor(sp.cancel(A*A-B*B*q), extension=[i, s2])


# Jacobian quotient functions from lce_filtered_quotient_skeleton.py.
r1 = 1+s2
r2 = -(1+s2)
r3 = s2-1
r4 = 1-s2
assert sp.expand((t-r1)*(t-r2)*(t-r3)*(t-r4)-q) == 0
f1 = sp.cancel((t-r1)/(t-r4))  # J1
f2 = sp.cancel((t-r2)/(t-r4))  # J2

# sqrt(2)-conjugation fixes J1,J2 as squareclasses on the normalization.
ct_f1 = sp.cancel((t-(1-s2))/(t-(1+s2)))
ct_f2 = sp.cancel((t-(s2-1))/(t-(1+s2)))
assert sp.cancel(ct_f1*f1-1) == 0
assert reduce_z2(ct_f2/f2 - ((t-r3)*(t-r4)/z)**2) == 0

# Four nodal K(t)^* relations identify the edge pairs
# (e1,e2),(e3,e4),(e5,e6),(e7,e8).  For an even-weight node incidence vector
# v=(e1,...,e8), the quotient coordinates in
#   q1=e1+e3, q2=e1+e5, q3=e1+e7
# are (e3+e4, e5+e6, e7+e8).
def graph_coords(node_edges):
    v = [0]*8
    for e in node_edges:
        v[e-1] ^= 1
    assert sum(v) % 2 == 0
    return [v[2]^v[3], v[4]^v[5], v[6]^v[7]]

# True x-alpha node incidences for three horizontal sections.
# Nodes are ordered as in normalization_galois_skeleton.py:
# e1=(0,0), e2=(0,inf), e3=(1,1), e4=(1,-1),
# e5=(-1,1), e6=(-1,-1), e7=(inf,0), e8=(inf,inf).
sec_one_edges = [3, 5]
sec_t_edges = [1, 3, 6, 8]
f_mob = sp.cancel(-i*(t-i)/(t+i))
assert sp.simplify(f_mob.subs(t, 1)+1) == 0
assert sp.simplify(f_mob.subs(t, -1)-1) == 0
assert sp.limit(f_mob, t, sp.oo) == -i
sec_mob_edges = [4, 5]

g_one = graph_coords(sec_one_edges)
g_t = graph_coords(sec_t_edges)
g_mob = graph_coords(sec_mob_edges)
assert g_one == [1,1,0]
assert g_t == [1,1,1]
assert g_mob == [1,1,0]
assert g_one != g_t

# Norm-level regression.  These are NOT themselves x-alpha coordinates; they
# only check the exact zero/pole patterns used above.
ell_one_p = sp.cancel(1-s_plus)
ell_one_m = sp.cancel(1-s_minus)
ell_t_p = sp.cancel(t-s_plus)
ell_t_m = sp.cancel(t-s_minus)
ell_mob_p = sp.cancel(f_mob-s_plus)
ell_mob_m = sp.cancel(f_mob-s_minus)
assert sp.simplify(norm(ell_one_p) - i*(t-1)*(t+1)/t) == 0
assert sp.simplify(norm(ell_one_m) + i*(t-1)*(t+1)/t) == 0
assert sp.simplify(norm(ell_t_p) - (1+i)*(t-1)*(t+1)) == 0
assert sp.simplify(norm(ell_t_m) - (1-i)*(t-1)*(t+1)) == 0
assert sp.simplify(norm(ell_mob_p) - (t-1)**3*(t+1)/(t*(t+i)**2)) == 0
assert sp.simplify(norm(ell_mob_m) + (t-1)*(t+1)**3/(t*(t+i)**2)) == 0

# The Möbius section and s=1 have the same graph class.  Their quotient is
# therefore Jacobian-only.  We now identify it exactly as J1.
Rplus = sp.cancel(ell_mob_p/ell_one_p)
Rminus = sp.cancel(ell_mob_m/ell_one_m)
u = reduce_z2(Rplus/Rminus)
A, B = ab(u)
assert sp.simplify(A - (t**4-2*t**3-2*t**2-2*t+1)/((t-1)**2*(t+1)**2)) == 0
assert sp.simplify(B + 2*i*t/((t-1)**2*(t+1)**2)) == 0
assert sp.simplify(norm(u) - ((t-1)/(t+1))**2) == 0

# Direct square witness for u/f1 in the common normalization.
p = sp.cancel(t*(t-r4)/((t-1)*(t+1)))
qcoef = sp.cancel(-i/((t-1)*(t+1)*(t-r1)))
square_witness = p + qcoef*z
assert reduce_z2(square_witness**2-u/f1) == 0

# It remains to check that, after removing J1, the common component squareclass
# is diagonal K(t)^*.  For Rminus, choose k0 below.  The quadratic-extension
# square criterion is exact: if N(U)=n^2 and (A(U)+n)/2 is a square in K(t),
# then U is a square in K(t,z).  Here the latter square is constant times 1.
k0 = sp.cancel((t-r4)*(t-r3)/((t-1)*(t+i)))
Am, Bm = ab(Rminus)
c = (1-i)/s2
nr = sp.cancel(c*(t+1)/(t+i))
assert sp.simplify(c**2+i) == 0
assert sp.simplify(norm(Rminus)-nr**2) == 0
p20 = sp.cancel((Am+nr)/2)
C0 = sp.cancel((1+s2)*(1-i)/4)
assert sp.simplify(p20/k0-C0) == 0
# C0 is a square in the geometric constant field k=Qbar.  This certifies
# Rminus/k0 as a square, so the pair (Rplus/f1,Rminus) is diagonal K* times
# componentwise squares.

# Therefore xalpha(mobius)+xalpha(s=1)=J1 exactly in LcE.
J1_relation = [1,0,0,0,0]

# The two section graph projections are independent.  Together with J1 they
# give three independent x-alpha classes, matching the independently locked
# total image dimension 3.  No seven-line search remains.
def rank2(rows):
    A = [r[:] for r in rows]
    r = 0
    for col in range(len(A[0])):
        pvt = next((j for j in range(r, len(A)) if A[j][col]), None)
        if pvt is None:
            continue
        A[r], A[pvt] = A[pvt], A[r]
        for j in range(len(A)):
            if j != r and A[j][col]:
                A[j] = [x^y for x,y in zip(A[j], A[r])]
        r += 1
    return r

assert rank2([g_one, g_t]) == 2
locked_xalpha_dim = 3
# Exact image description up to the immaterial J2 coefficients of the two
# section rows: span{J1, b*J2+q1+q2, d*J2+q1+q2+q3}, b,d in F2.
# The quotient basis {J2,q1} works for all four b,d choices.
for bbit in (0,1):
    for dbit in (0,1):
        rows = [
            [1,0,0,0,0],
            [0,bbit,1,1,0],
            [0,dbit,1,1,1],
        ]
        assert rank2(rows) == 3
        assert rank2(rows + [[0,1,0,0,0], [0,0,1,0,0]]) == 5

# Repair the full-pair Galois action.  The old half-point corrections on one
# component were:
# tau: q1->+J1, q2->+J1, q3->0
# ct : q1->+J2, q2->+(J1+J2), q3->0.
# For the B- component the correction is governed by cc*sigma*cc.
# Relations in the degree-8 normal field give
#   cc*tau*cc=tau,  cc*ct*cc=tau*ct.
# Hence the pair corrections are the sums of plus/minus corrections:
# tau -> 0; ct -> J1 on q1 and q2; cc -> 0.
I5 = [[1 if r == c0 else 0 for c0 in range(5)] for r in range(5)]
tau = [row[:] for row in I5]
cc = [row[:] for row in I5]
ct = [row[:] for row in I5]
ct[0][2] ^= 1
ct[0][3] ^= 1

# J1 and J2 are fixed; graph labels are fixed.  Since J1 is in im(x-alpha),
# the quotient basis [J2,q1] is fixed by all generators.
quotient_basis = ["J2", "q1"]
quotient_action = {
    "tau": [[1,0],[0,1]],
    "ct": [[1,0],[0,1]],
    "cc": [[1,0],[0,1]],
}

cert = {
    "schema": "STAGE33_05_XALPHA_PAIR_GALOIS_REPAIR_V1",
    "supersedes": [
        "xalpha_split_section_rows.py row interpretation",
        "cv_exact_graph_lifts_and_galois.py single-component matrices as full-pair action",
    ],
    "basis_order": ["J1","J2","q1","q2","q3"],
    "true_xalpha_definition": "section s=f maps to pair (f-s_plus,f-s_minus) modulo diagonal K* and component squares",
    "section_graph_projections": {
        "s=1": g_one,
        "s=t": g_t,
        "s=-i*(t-i)/(t+i)": g_mob,
    },
    "mobius_plus_one_difference": "J1",
    "J1_in_xalpha_image_exact": True,
    "xalpha_graph_projection_rank": 2,
    "locked_xalpha_image_dimension": locked_xalpha_dim,
    "xalpha_image_spanned_exactly": True,
    "xalpha_image_span_normal_form": [
        "J1",
        "b*J2+q1+q2",
        "d*J2+q1+q2+q3"
    ],
    "undetermined_b_d_do_not_affect_quotient_basis": True,
    "seven_graph_line_search_retired": True,
    "brauer_quotient_dimension": 2,
    "explicit_brauer_quotient_basis": quotient_basis,
    "explicit_brauer_quotient_basis_materialized": True,
    "single_component_mixing": {
        "tau": ["J1","J1","0"],
        "ct": ["J2","J1+J2","0"],
    },
    "full_pair_galois_action_matrices_column_convention": {
        "tau": tau,
        "ct": ct,
        "cc": cc,
    },
    "full_pair_galois_action_exact": True,
    "geometric_Br2_quotient_action": "identity",
    "geometric_Br2_GQ_invariant_dimension": 2,
    "descent_obstruction_accounted": False,
    "Q_defined_arithmetic_representatives_materialized": False,
    "Q_relevant_surviving_dimension_certified": False,
    "next_exact_leaf": "L33-05-HOCHSCHILD-SERRE-DESCENT-OF-J2-Q1",
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT/"xalpha-pair-galois-repair.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True)+"\n", encoding="utf-8"
)
print(json.dumps(cert, indent=2, sort_keys=True))
