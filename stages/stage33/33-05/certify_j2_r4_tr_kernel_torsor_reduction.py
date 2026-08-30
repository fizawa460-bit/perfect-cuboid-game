#!/usr/bin/env python3
"""R4 exact reduction for the repaired J2 Tr-kernel torsor.

This is deliberately dependency-free. It does NOT select the marked Kc
Brauer coordinate. It materializes the named 2-cover attached to the R3
Creutz--Viray cocycle and reduces R4 to one primitive lattice/glue computation.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def padd(a,b):
    n=max(len(a),len(b))
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)])


def pscale(a,c):
    return trim([c*x for x in a])


def psub(a,b):
    return padd(a,pscale(b,-1))


def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return trim(out)


def ppow(a,n):
    out=[1]
    for _ in range(n):
        out=pmul(out,a)
    return out


# Z[t] identities.
t=[0,1]
t2=pmul(t,t)
one=[1]
r=ppow(psub(t2,one),2)
q=padd(padd(ppow(t,4),pscale(t2,-6)),one)
a=ppow(padd(t2,one),2)
c=pscale(pmul(t,psub(t2,one)),2)
b=pmul(c,c)
Dp=padd(padd(t2,pscale(t,-2)),[-1])
Dm=padd(padd(t2,pscale(t,2)),[-1])

assert psub(psub(pmul(a,a),pscale(b,4)),pmul(q,q)) == [0]
assert psub(padd(a,pscale(c,2)),pmul(Dm,Dm)) == [0]
assert psub(psub(a,pscale(c,2)),pmul(Dp,Dp)) == [0]


# Evaluate q at a+b*sqrt(2), with sqrt(2)^2=2.
def qmul(x,y):
    a0,b0=x; a1,b1=y
    return (a0*a1+2*b0*b1, a0*b1+b0*a1)


def qadd(x,y):
    return (x[0]+y[0],x[1]+y[1])


def eval_poly(p,x):
    acc=(0,0)
    power=(1,0)
    for coeff in p:
        acc=qadd(acc,(coeff*power[0],coeff*power[1]))
        power=qmul(power,x)
    return acc


r2=(-1,-1)   # -(1+sqrt(2))
r4=(1,-1)    # 1-sqrt(2)
assert eval_poly(q,r2) == (0,0)
assert eval_poly(q,r4) == (0,0)

# Lock the actual repaired R3 input, not a historical d=2/T0 candidate.
r3=json.loads((ROOT/"j2-corrected-cv-e2-cocycle.json").read_text(encoding="utf-8"))
assert r3["canonical_sha256"] == "8440400fd7eff183830bb16e991a6fb6f253b1774a76384ed2a3dc8adc951312"
assert r3["cv_lemma_4_6"]["xi_rho"] == "Tr"
assert r3["cv_lemma_4_6"]["cocycle_bits_in_fixed_basis"] == [0,1]
assert r3["fixed_rational_E2_kummer_coordinates"]["squareclass_pair"][0] == "1"
assert "sqrt(2)" in r3["fixed_rational_E2_kummer_coordinates"]["squareclass_pair"][1]

cert = {
  "schema":"STAGE33_05_J2_R4_TR_KERNEL_TORSOR_REDUCTION_V1",
  "status":"PASS_EXACT_R4_TR_KERNEL_TORSOR_REDUCTION_LATTICE_PENDING",
  "repair_leaf":"R4",
  "attempt":1,
  "source_lock":{
    "r3_certificate":"stages/stage33/33-05/j2-corrected-cv-e2-cocycle.json",
    "r3_certificate_canonical_sha256":"8440400fd7eff183830bb16e991a6fb6f253b1774a76384ed2a3dc8adc951312",
    "r3_cocycle":"xi(rho)=Tr",
    "r3_kummer_squareclass_pair":["1","f2"],
    "fixed_generic_fiber":"Y^2=X*(X-r)*(X-q)"
  },
  "fixed_data":{
    "r":"(t^2-1)^2",
    "q":"t^4-6*t^2+1",
    "Tr":"((t^2-1)^2,0)",
    "f2":"(t+1+sqrt(2))/(t-1+sqrt(2))",
    "Dplus":"t^2-2*t-1",
    "Dminus":"t^2+2*t-1"
  },
  "tr_kernel_shift":{
    "coordinate_change":"x=X-r",
    "shifted_curve":"y^2=x*(x^2+a*x+b)",
    "a":"(t^2+1)^2",
    "b":"[2*t*(t^2-1)]^2",
    "Tr_after_shift":"(0,0)",
    "b_is_square":True
  },
  "tr_kernel_2isogenous_comparison_surface":{
    "curve":"E'_Tr: y^2=x*(x^2-2*a*x+q^2)=x*(x-Dplus^2)*(x-Dminus^2)",
    "identity_a2_minus_4b":"a^2-4*b=q^2",
    "root_identity_plus":"a+2*sqrt(b)=Dminus^2 with sqrt(b)=2*t*(t^2-1)",
    "root_identity_minus":"a-2*sqrt(b)=Dplus^2 with sqrt(b)=2*t*(t^2-1)",
    "role":"COMPARISON_2_ISOGENOUS_JACOBIAN_ONLY",
    "is_named_J2_torsor":False
  },
  "named_repaired_J2_2cover":{
    "kernel":"<Tr>",
    "descent_squareclass":"d=f2",
    "equation":"N^2=f2*U^4+(t^2+1)^2*U^2*V^2+([2*t*(t^2-1)]^2/f2)*V^4",
    "standard_form":"N^2=d*U^4+a*U^2*V^2+(b/d)*V^4 for y^2=x*(x^2+a*x+b)",
    "splits_over":"Kgeom(sqrt(f2))",
    "obvious_bisection_chart":"V=0 gives N^2=f2*U^4",
    "bisection_base_double_cover":"w^2=f2",
    "bisection_branch_points":["r2=-(1+sqrt(2))","r4=1-sqrt(2)"],
    "branch_points_are_q_roots":True,
    "bisection_genus":0
  },
  "lattice_reduction":{
    "candidate_minimum_norms":[4,8,12],
    "candidate_functionals":{"4":[0,1],"8":[1,0],"12":[1,1]},
    "candidate_set_reduced":False,
    "minimum_norm_selected":False,
    "marked_brauer_coordinate_selected":False,
    "exact_missing_interface":"COMPUTE_PRIMITIVE_NS_DISCRIMINANT_FORM_OR_EQUIVALENT_COMPONENT_GLUE_OF_THE_NAMED_f2_Tr_TORSOR_AND_MATCH_ONE_OF_THE_THREE_KERNEL_LATTICES",
    "next_local_data":"Use the explicit rational bisection w^2=f2 and its ramification at the two q-root I2 fibers r2,r4 to compute component-incidence/glue; do not replace the torsor by the 2-isogenous comparison surface."
  },
  "firewalls":{
    "Q_defined_descent_credit_restored":False,
    "stage33_05_reclosed":False,
    "stage33_12_closed_exact":False,
    "stage33_13_released":False,
    "class3_promoted":False,
    "theorem_credit":False,
    "receiver_credit":False,
    "endpoint_credit":False,
    "perfect_cuboid_existence_claim":False,
    "perfect_cuboid_nonexistence_claim":False
  },
  "exact_new_information":"The repaired J2 class is now an explicit Tr-kernel 2-cover with d=f2; after shifting Tr to (0,0), b is an exact square and the Tr-isogenous comparison curve splits as x*(x-Dplus^2)*(x-Dminus^2). The named torsor is not identified with that comparison curve.",
  "next_exact_leaf":"R4_COMPUTE_NAMED_f2_Tr_TORSOR_NS_DISCRIMINANT_FORM_OR_EQUIVALENT_COMPONENT_GLUE_AND_SELECT_MINIMUM_NORM_4_8_12"
}
canonical=json.dumps(cert,sort_keys=True,separators=(",",":")).encode()
cert["canonical_sha256"]=hashlib.sha256(canonical).hexdigest()
assert cert["canonical_sha256"] == "a2b13adf8bf186796058baf88de4853a10682577298f4c75f508ddd8a0c4b3ec"
(ROOT/"j2-r4-tr-kernel-torsor-reduction.json").write_text(
    json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8"
)
print(json.dumps({
    "success":True,
    "status":cert["status"],
    "canonical_sha256":cert["canonical_sha256"],
    "next_exact_leaf":cert["next_exact_leaf"]
},indent=2,sort_keys=True))
