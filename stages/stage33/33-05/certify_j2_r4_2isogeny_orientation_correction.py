#!/usr/bin/env python3
"""Exact R4 2-isogeny orientation correction for the repaired J2 torsor.

Dependency-free. This verifier audits the binary-quartic Jacobian, so the
homogeneous space used for the named H^1(E) class has Jacobian Kc itself,
rather than the Tr-isogenous comparison curve.
"""
from fractions import Fraction
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CERT = ROOT / "j2-r4-2isogeny-orientation-correction.json"


def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p


def add(a,b):
    n=max(len(a),len(b))
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)])


def scale(a,c):
    return trim([c*x for x in a])


def sub(a,b):
    return add(a,scale(b,-1))


def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return trim(out)


def powp(a,n):
    out=[1]
    for _ in range(n):
        out=mul(out,a)
    return out


def eq(a,b):
    return trim(a)==trim(b)


t=[0,1]
one=[1]
t2=mul(t,t)
A=powp(add(t2,one),2)
r=powp(sub(t2,one),2)
b=scale(mul(t2,r),4)
q=add(add(powp(t,4),scale(t2,-6)),one)
Dp=add(add(t2,scale(t,-2)),[-1])
Dm=add(add(t2,scale(t,2)),[-1])

# Fixed 2-isogeny identities.
assert eq(sub(powp(A,2),scale(b,4)),powp(q,2))
assert eq(add(powp(Dp,2),powp(Dm,2)),scale(A,2))
assert eq(mul(Dp,Dm),q)

# Binary quartic invariants I,J. f2 cancels from a0*e0.
Iw=add(powp(A,2),scale(b,12))
Jw=sub(scale(mul(A,b),72),scale(powp(A,3),2))
Ic=add(scale(powp(A,2),4),scale(powp(q,2),12))
Jc=add(scale(powp(A,3),16),scale(mul(A,powp(q,2)),-144))

# Short Weierstrass coefficients for y^2=x^3+c*x^2+d*x:
# x -> X-c/3 gives X^3 + (d-c^2/3)X + (2c^3/27-cd/3).
def as_frac(p):
    return [Fraction(x) for x in p]


A_f=as_frac(A)
b_f=as_frac(b)
q2_f=as_frac(powp(q,2))
short_E_A=add(b_f,scale(powp(A_f,2),Fraction(-1,3)))
short_E_B=add(scale(powp(A_f,3),Fraction(2,27)),scale(mul(A_f,b_f),Fraction(-1,3)))
short_Ep_A=add(q2_f,scale(powp(A_f,2),Fraction(-4,3)))
short_Ep_B=add(scale(powp(A_f,3),Fraction(-16,27)),scale(mul(A_f,q2_f),Fraction(2,3)))

# Weil's binary-quartic Jacobian is y^2=x^3-27 I x-27 J.
# The old (+A,b/d) quartic is the E' curve after u=3 scaling.
assert eq(scale(Iw,-27),scale(short_Ep_A,3**4))
assert eq(scale(Jw,-27),scale(short_Ep_B,3**6))
# The corrected (-2A,q^2/d) quartic is Kc E after u=6 scaling.
assert eq(scale(Ic,-27),scale(short_E_A,6**4))
assert eq(scale(Jc,-27),scale(short_E_B,6**6))

# Source locks: the corrected CV class is rho -> Tr with squareclass f2.
r3=json.loads((ROOT/"j2-corrected-cv-e2-cocycle.json").read_text())
assert r3["canonical_sha256"]=="8440400fd7eff183830bb16e991a6fb6f253b1774a76384ed2a3dc8adc951312"
assert r3["cv_lemma_4_6"]["xi_rho"]=="Tr"
assert r3["fixed_rational_E2_kummer_coordinates"]["squareclass_pair"][0]=="1"

old=json.loads((ROOT/"j2-r4-tr-kernel-torsor-reduction.json").read_text())
assert old["canonical_sha256"]=="a2b13adf8bf186796058baf88de4853a10682577298f4c75f508ddd8a0c4b3ec"
leg=json.loads((ROOT/"j2-r4-legendre-torsion-glue-reduction.json").read_text())
assert leg["canonical_sha256"]=="5dad98eeefbecfef52a9531afbdbd5f48aa2e9016bd9a8045f84d731d77f1e63"

hist=json.loads((ROOT.parent/"33-12"/"j2-class2-batch3-go-no-go.json").read_text())
assert hist["class2_go_no_go"]["verdict"]=="NO_GO_AFTER_BATCH3"
assert hist["firewalls"]["j2_explicit_torsor_surface_materialized"] is False

c=json.loads(CERT.read_text())
assert c["attempt"]==4
assert c["orientation_audit"]["attempt1_named_torsor_credit_revoked"] is True
assert c["orientation_audit"]["attempt1_semantic_reclassification"].startswith("DUAL_2ISOGENY")
ct=c["corrected_named_geometric_torsor"]
assert ct["jacobian"]=="E_Kc"
assert ct["kernel_exact_sequence"]=="0 -> <Tr> -> E_Kc -> Eprime_Tr -> 0"
assert ct["equation"]=="N^2=f2*U^4-2*(t^2+1)^2*U^2*V^2+((t^4-6*t^2+1)^2/f2)*V^4"
assert ct["factorization_after_multiplying_by_f2"]=="f2*N^2=(f2*U^2-Dplus^2*V^2)*(f2*U^2-Dminus^2*V^2)"
ng=c["historical_no_go_reaudit"]
assert ng["explicit_Kc_jacobian_genus_one_model_materialized"] is True
assert ng["global_K3_minimal_regular_model_NS_discriminant_form_materialized"] is False
assert ng["candidate_minimum_norms"]==[4,8,12]
assert ng["marked_Brauer_functional_selected"] is False
assert c["cycle_protocol"]["CYCLE_ROUTE_STATUS"]=="PASS_NEW_GATE_FROM_STRONGER_VIEW"
assert c["firewalls"]["Q_defined_descent_credit_restored"] is False
assert c["firewalls"]["stage33_05_reclosed"] is False
assert c["firewalls"]["stage33_12_closed_exact"] is False
assert c["firewalls"]["stage33_13_released"] is False

dct=dict(c)
got=dct.pop("canonical_sha256")
canonical=json.dumps(dct,sort_keys=True,separators=(",",":")).encode()
assert got==hashlib.sha256(canonical).hexdigest()
print(json.dumps({
    "success":True,
    "status":c["status"],
    "canonical_sha256":got,
    "old_quartic_jacobian":"Eprime_Tr",
    "corrected_quartic_jacobian":"E_Kc",
    "candidate_minimum_norms":[4,8,12],
    "next_exact_leaf":c["next_exact_leaf"],
},indent=2,sort_keys=True))
