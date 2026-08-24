#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
t, s, z = sp.symbols("t s z")
i = sp.I
q = sp.expand(t**4 - 6*t**2 + 1)
Gp = sp.expand(t*(1-s**2) + i*s*(1-t**2))
Gm = sp.expand(t*(1-s**2) - i*s*(1-t**2))

# Explicit common normalization F = Qbar(t,z), z^2=q(t).  The two branch
# components differ only by the sign of i in the map to the ambient s-coordinate.
s_plus = i*(1-t**2+z)/(2*t)
s_minus = -i*(1-t**2+z)/(2*t)

def reduce_z2(expr):
    num, den = sp.together(expr).as_numer_denom()
    numr = sp.rem(sp.Poly(sp.expand(num), z), sp.Poly(z**2-q, z)).as_expr()
    denr = sp.rem(sp.Poly(sp.expand(den), z), sp.Poly(z**2-q, z)).as_expr()
    return sp.simplify(numr/denr)

assert reduce_z2(Gp.subs(s,s_plus)) == 0
assert reduce_z2(Gm.subs(s,s_minus)) == 0
# Complex conjugation swaps B+ and B- while fixing the abstract functions t,z.
assert sp.conjugate(s_plus).xreplace({sp.conjugate(t):t,sp.conjugate(z):z}) == s_minus

# Eight B+ cap B- nodes.  z-value means z itself at finite t; at infinity it
# means Zinf=z/t^2.  Values on B- are obtained from the same normalization and
# are listed separately because complex conjugation changes i in the residue field.
nodes = [
    {"edge":"e1","t":"0","s":"0",        "z_plus":"-1",  "z_minus":"-1"},
    {"edge":"e2","t":"0","s":"infinity", "z_plus":"1",   "z_minus":"1"},
    {"edge":"e3","t":"1","s":"1",        "z_plus":"-2*i","z_minus":"2*i"},
    {"edge":"e4","t":"1","s":"-1",       "z_plus":"2*i", "z_minus":"-2*i"},
    {"edge":"e5","t":"-1","s":"1",       "z_plus":"2*i", "z_minus":"-2*i"},
    {"edge":"e6","t":"-1","s":"-1",      "z_plus":"-2*i","z_minus":"2*i"},
    {"edge":"e7","t":"infinity","s":"0", "zinf_plus":"1","zinf_minus":"1"},
    {"edge":"e8","t":"infinity","s":"infinity","zinf_plus":"-1","zinf_minus":"-1"},
]

# Verify finite node values against z^2=q and the normalization maps whenever
# t is nonzero finite.  At t=0 and infinity the entries are exact chart limits.
for rec in nodes[2:6]:
    tv=sp.Integer(int(rec["t"])); sv=sp.Integer(int(rec["s"]))
    zp=sp.sympify(rec["z_plus"],locals={"i":i}); zm=sp.sympify(rec["z_minus"],locals={"i":i})
    assert sp.simplify(zp**2-q.subs(t,tv)) == 0
    assert sp.simplify(zm**2-q.subs(t,tv)) == 0
    assert sp.simplify(s_plus.subs({t:tv,z:zp})-sv) == 0
    assert sp.simplify(s_minus.subs({t:tv,z:zm})-sv) == 0

# q(0)=1.  At infinity q/t^4 -> 1, so the two points have z/t^2=+/-1.
assert q.subs(t,0) == 1
u=sp.symbols("u")
qinf=sp.expand(u**4*q.subs(t,1/u))
assert qinf.subs(u,0) == 1

# Complex conjugation preserves every geometric node edge: it swaps the two
# normalization components and conjugates the listed residue value.
for rec in nodes:
    if "z_plus" in rec:
        zp=sp.sympify(rec["z_plus"],locals={"i":i})
        zm=sp.sympify(rec["z_minus"],locals={"i":i})
        assert sp.conjugate(zp) == zm
    else:
        assert rec["zinf_plus"] == rec["zinf_minus"]

# Associated-graded Creutz--Viray filtration:
# Jac(B)[2] = Jac(B+)[2] + Jac(B-)[2], each dimension 2;
# H1(Gamma) has basis e_j+e_8 (j=1..7);
# G1/G2 is one-dimensional here (raw dimension 12 and mc=0).
# Conjugation swaps the two Jac summands, fixes each graph edge and hence H1,
# and necessarily acts trivially on the one-dimensional F2 quotient G1/G2.
cycle_basis=[]
for j in range(7):
    v=[0]*8; v[j]=1; v[7]=1; cycle_basis.append(v)

def rank2(rows):
    A=[r[:] for r in rows]; r=0
    for c in range(len(A[0])):
        p=next((k for k in range(r,len(A)) if A[k][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        for k in range(len(A)):
            if k!=r and A[k][c]: A[k]=[x^y for x,y in zip(A[k],A[r])]
        r+=1
    return r
assert rank2(cycle_basis)==7

jac_cc=[
    [0,0,1,0],
    [0,0,0,1],
    [1,0,0,0],
    [0,1,0,0],
]
# Fixed subspace of a swap of two 2D summands has dimension 2.
jac_fixed_dim=2
h1_fixed_dim=7
g1g2_fixed_dim=1
graded_fixed_dim=jac_fixed_dim+h1_fixed_dim+g1g2_fixed_dim
assert graded_fixed_dim==10

roots=[1+sp.sqrt(2),-(1+sp.sqrt(2)),sp.sqrt(2)-1,-(sp.sqrt(2)-1)]
for r in roots:
    assert sp.simplify(q.subs(t,r))==0
jac_function_basis=[
    f"(t-({sp.sstr(roots[0])}))/(t-({sp.sstr(roots[3])}))",
    f"(t-({sp.sstr(roots[1])}))/(t-({sp.sstr(roots[3])}))",
]

cert={
    "schema":"STAGE33_05_NORMALIZATION_GALOIS_GRADED_SKELETON_V1",
    "common_normalization":"z^2=t^4-6*t^2+1",
    "Bplus_map_s":"i*(1-t^2+z)/(2*t)",
    "Bminus_map_s":"-i*(1-t^2+z)/(2*t)",
    "complex_conjugation_on_normalization":"swap Bplus/Bminus; t,z fixed as functions; constants conjugated",
    "nodes":nodes,
    "complex_conjugation_fixes_all_dual_graph_edges":True,
    "dual_graph_cycle_basis_F2":cycle_basis,
    "H1_Gamma_dimension":7,
    "H1_Gamma_cc_action":"identity",
    "Jac_B_2_dimension":4,
    "Jac_component_2torsion_function_basis_skeleton":jac_function_basis,
    "Jac_cc_associated_graded_matrix":jac_cc,
    "Jac_cc_fixed_dimension":jac_fixed_dim,
    "G1_over_G2_dimension":1,
    "G1_over_G2_cc_action":"identity (only automorphism of a 1D F2 space)",
    "raw_LE_associated_graded_dimension":12,
    "raw_LE_associated_graded_cc_fixed_dimension":graded_fixed_dim,
    "LcE_dimension":5,
    "xalpha_image_dimension":3,
    "full_LcE_cc_action_materialized":False,
    "warning":"associated-graded action does not determine extension mixing or the quotient action on LcE/im(x-alpha)",
    "explicit_LcE_basis_materialized":False,
    "explicit_xalpha_matrix_materialized":False,
    "Q_relevant_surviving_dimension_certified":False,
    "next_exact_leaf":"L33-05-CV-FUNCTION-SYNTHESIS-ON-z2=q-AND-XALPHA",
    "theorem_credit":False,
    "endpoint_credit":False,
}
raw=json.dumps(cert,indent=2,sort_keys=True)+"\n"
(ROOT/"normalization-galois-graded.json").write_text(raw,encoding="utf-8")
print(raw,end="")
print("CERTIFICATE_SHA256="+hashlib.sha256(raw.encode()).hexdigest())
