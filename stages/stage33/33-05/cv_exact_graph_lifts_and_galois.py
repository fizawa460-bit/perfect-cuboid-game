#!/usr/bin/env python3
"""Exact CV graph lifts via the elliptic normalization, with finite Galois mixing.

This replaces the node-parity-only residual g3 pilot by genuine functions whose
odd divisors are exactly the requested node pairs modulo 2.  No degree search
is used: each graph function is a chord/tangent quotient on E:y^2=x^3-x.
"""
import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
t,z,X,Y,d = sp.symbols("t z X Y d")
i = sp.I
s2 = sp.sqrt(2)
q = t**4 - 6*t**2 + 1
D = 8*(s2-1)

# Quartic normalization -> j=1728 elliptic curve.
r4 = 1-s2
x_of_t = sp.cancel((t-(1+s2))/((1+s2)*t+1))
y_of_tz = sp.cancel(i*s2/(1+s2) * z/(t-r4)**2)
assert sp.simplify((y_of_tz**2-(x_of_t**3-x_of_t)).subs(z**2,q)) == 0

# Reduction in M=Q(i,sqrt(2),d), d^2=8(sqrt(2)-1).
def red_d(expr):
    expr = sp.together(sp.expand(expr))
    num, den = sp.fraction(expr)
    def redpoly(p):
        P = sp.Poly(sp.expand(p), d, domain="EX")
        out = 0
        for (e,), c in P.terms():
            out += c * D**(e//2) * (d if e & 1 else 1)
        return sp.expand(out)
    return sp.simplify(redpoly(num)/redpoly(den))

# E group law, exact in M.
def neg(P):
    return None if P is None else (P[0], -P[1])

def add(P,Q):
    if P is None: return Q
    if Q is None: return P
    x1,y1=P; x2,y2=Q
    if red_d(x1-x2)==0:
        if red_d(y1+y2)==0: return None
        m=red_d((3*x1**2-1)/(2*y1))
    else:
        m=red_d((y2-y1)/(x2-x1))
    x3=red_d(m**2-x1-x2)
    y3=red_d(m*(x1-x3)-y1)
    return (sp.factor(x3),sp.factor(y3))

def double(P): return add(P,P)

def on_E(P):
    return P is None or red_d(P[1]**2-(P[0]**3-P[0]))==0

# B+ node points in E-coordinates.  Values are independently implied by the
# frozen normalization certificate (e1,e3,e5,e7 on B+).
P1=(-s2-1, -i*(2+s2))
P3=(1-s2, 2-s2)
P5=(1+s2, -2-s2)
P7=(-1+s2, i*(2-s2))
for P in (P1,P3,P5,P7): assert on_E(P)

R1=add(P1,P3); R2=add(P1,P5); R3=add(P1,P7)
assert R1==(i,1-i)
assert R2==(-i,1+i)
assert R3==(0,0)

# Exact halves. H1 requires one quadratic extension; H2 is its complex
# conjugate. H3 is already defined over Q(i).
xH1=-i*(s2-1)+d/2
yH1=i*(-2+s2)*(1-i)*(d+4*i)/4
xH2=sp.conjugate(xH1).xreplace({sp.conjugate(d):d})
yH2=sp.conjugate(yH1).xreplace({sp.conjugate(d):d})
H1=(red_d(xH1),red_d(yH1)); H2=(red_d(xH2),red_d(yH2)); H3=(i,1-i)
for H,R in ((H1,R1),(H2,R2),(H3,R3)):
    assert on_E(H)
    assert double(H)==R

# Chord/tangent line functions.  The chord through P,Q and tangent at H have
# the same third intersection -R because 2H=P+Q=R. Their quotient therefore
# has divisor P+Q-2H, hence odd support exactly P+Q.
def line_chord(P,Q):
    m=red_d((Q[1]-P[1])/(Q[0]-P[0]))
    return sp.expand(Y-P[1]-m*(X-P[0]))

def line_tangent(H):
    m=red_d((3*H[0]**2-1)/(2*H[1]))
    return sp.expand(Y-H[1]-m*(X-H[0]))

def verify_line_factor(line, roots):
    # Substitute y=line(x) into y^2-(x^3-x), then compare roots/multiplicity.
    yline=sp.solve(sp.Eq(line,0),Y)[0]
    poly=sp.expand(yline**2-(X**3-X))
    lc=sp.Poly(poly,X,domain="EX").LC()
    target=lc
    for r,mult in roots:
        target*= (X-r)**mult
    diff=sp.Poly(sp.expand(poly-target),X,domain="EX")
    for c in diff.all_coeffs():
        if red_d(c)!=0:
            raise SystemExit("line divisor factorization failed")

records=[]
for name,P,Q,H,R in (("q1",P1,P3,H1,R1),("q2",P1,P5,H2,R2),("q3",P1,P7,H3,R3)):
    chord=line_chord(P,Q); tangent=line_tangent(H)
    verify_line_factor(chord,[(P[0],1),(Q[0],1),(R[0],1)])
    verify_line_factor(tangent,[(H[0],2),(R[0],1)])
    records.append({
        "class":name,
        "odd_node_edges":{"q1":["e1","e3"],"q2":["e1","e5"],"q3":["e1","e7"]}[name],
        "P":[sp.sstr(P[0]),sp.sstr(P[1])],
        "Q":[sp.sstr(Q[0]),sp.sstr(Q[1])],
        "R=P+Q":[sp.sstr(R[0]),sp.sstr(R[1])],
        "half_H":[sp.sstr(H[0]),sp.sstr(H[1])],
        "chord":sp.sstr(chord),
        "tangent":sp.sstr(tangent),
        "function_on_Bplus":sp.sstr(sp.cancel(chord/tangent)),
        "divisor_identity":"div(chord/tangent)=P+Q-2H",
        "function_on_Bminus":"complex conjugate of Bplus function",
    })

# Explicitly retire the former node-parity-only g3.  Its norm on B+ has extra
# quintic odd support, so it is not an ell_C lift.
s = i*(1-t**2+z)/(2*t)
g3_old=sp.cancel((t**2*s+t**2+s)/(t**2*s-t**2+t*s+t-s-1))
num,den=sp.fraction(g3_old)
def lin_coeff(poly):
    poly=sp.expand(poly)
    return sp.expand(poly.subs(z,0)),sp.expand(sp.diff(poly,z).subs(z,0))
A,B=lin_coeff(num); C,Dd=lin_coeff(den)
norm_num=sp.factor(A*A-B*B*q,extension=i)
norm_den=sp.factor(C*C-Dd*Dd*q,extension=i)
forbidden_num=sp.Poly(t**5-2*i*t**2-t-i,t,extension=i)
forbidden_den=sp.Poly(t**5+t**4+(-1+4*i)*t**3+t**2+t-1,t,extension=i)
assert sp.rem(sp.Poly(norm_num,t,extension=i),forbidden_num)==0
assert sp.rem(sp.Poly(norm_den,t,extension=i),forbidden_den)==0

# Finite Galois extension and extension mixing.
# d has irreducible quartic x^4+16x^2-64 over Q; adjoining i gives the normal
# degree-8 field M.  Automorphisms used below:
# tau: d -> -d
# ct : sqrt2 -> -sqrt2, d -> i(1+sqrt2)d
# cc : i -> -i, d fixed (real choice)
def tau_expr(e): return sp.expand(e.subs(d,-d))
def ct_expr(e):
    a=sp.symbols("_dtmp")
    return sp.expand(e.xreplace({d:a,s2:-s2}).subs(a,i*(1+s2)*d))

def sigma_point(H,fn): return (red_d(fn(H[0])),red_d(fn(H[1])))
J1=(0,0); J2=(1,0); J12=(-1,0)
def torsion_label(P):
    if P is None: return "0"
    for lab,T in (("J1",J1),("J2",J2),("J1+J2",J12)):
        if red_d(P[0]-T[0])==0 and red_d(P[1]-T[1])==0: return lab
    raise SystemExit(f"non-2-torsion extension correction {P}")

mix={}
for sig,fn in (("tau",tau_expr),("ct",ct_expr)):
    arr=[]
    for H in (H1,H2,H3):
        corr=add(sigma_point(H,fn),neg(H))
        arr.append(torsion_label(corr))
    mix[sig]=arr
assert mix["tau"]==["J1","J1","0"]
assert mix["ct"]==["J2","J1+J2","0"]

# Column-action matrices on [J1,J2,q1,q2,q3].
I5=[[1 if r==c else 0 for c in range(5)] for r in range(5)]
tau=[row[:] for row in I5]; tau[0][2]^=1; tau[0][3]^=1
ct=[row[:] for row in I5]; ct[1][2]^=1; ct[0][3]^=1; ct[1][3]^=1
cc=[row[:] for row in I5]  # pair basis (h,cc(h)); Jac diagonal identification.

cert={
    "schema":"STAGE33_05_CV_EXACT_GRAPH_LIFTS_GALOIS_V1",
    "source_lock":{
        "creutz_viray":"Lemma 4.2, Definition 4.3, Proposition 4.4, Theorem 5.2 / Corollary 5.4",
        "arxiv":"1306.3251v3",
        "normalization":"z^2=t^4-6*t^2+1",
    },
    "elliptic_model":{"equation":"y^2=x^3-x","x":sp.sstr(x_of_t),"y":sp.sstr(y_of_tz)},
    "graph_lifts":records,
    "graph_lift_count":3,
    "graph_divisor_conditions_exact":True,
    "old_bidegree21_g3_retired":True,
    "old_g3_forbidden_norm_factor_numerator":sp.sstr(forbidden_num.as_expr()),
    "old_g3_forbidden_norm_factor_denominator":sp.sstr(forbidden_den.as_expr()),
    "constant_field":{
        "M":"Q(i,sqrt(2),d), d^2=8(sqrt(2)-1)",
        "d_minpoly_over_Q":"d^4+16*d^2-64",
        "degree_over_Q":8,
        "normal_closure_already_M":True,
    },
    "basis_order":["J1","J2","q1","q2","q3"],
    "extension_mixing":mix,
    "galois_action_matrices_column_convention":{"cc":cc,"ct":ct,"tau":tau},
    "full_LcE_basis_materialized":True,
    "full_LcE_basis_reason":"2 Jac functions from prior leaf plus 3 exact chord/tangent graph lifts; associated-graded classes form the 5D quotient basis",
    "creutz_viray_divisor_conditions_complete_for_basis":True,
    "extension_mixing_complete_for_basis":True,
    "xalpha_matrix_materialized":False,
    "brauer_quotient_action_exact":False,
    "q_relevant_surviving_dimension_certified":False,
    "next_exact_leaf":"L33-05-COMPUTE-NS-RESTRICTION-XALPHA-3x5-THEN-QUOTIENT-GALOIS",
    "loop_guard":"Do not resume bounded degree graph-function searches; exact graph lifts are closed.",
    "theorem_credit":False,
    "endpoint_credit":False,
}
canonical=json.dumps(cert,sort_keys=True,separators=(",",":")).encode()
cert["canonical_sha256"]=hashlib.sha256(canonical).hexdigest()
(ROOT/"cv-exact-graph-lifts-galois.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({
    "success":True,
    "full_LcE_basis_materialized":True,
    "old_g3_retired":True,
    "extension_field_degree":8,
    "tau_mixing":mix["tau"],
    "ct_mixing":mix["ct"],
    "next_exact_leaf":cert["next_exact_leaf"],
    "certificate_sha256":cert["canonical_sha256"],
},indent=2,sort_keys=True))
