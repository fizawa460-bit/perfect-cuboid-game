#!/usr/bin/env python3
"""Materialize corrected J2 representative-level descent data without claiming HS d2.

This verifier deliberately stops before the surface Kummer sequence.  It proves
more than fixedness of the 5D CV quotient: for the corrected full-L pair
(f2,1), it constructs explicit square/diagonal witnesses for the relevant
constant-field Galois actions and an explicit descent datum for the geometric
half-divisor D=P_r2-P_r4 on the normalization z^2=q.

It does NOT identify that normalization datum with a class in
H^2(Kc_bar,mu_2), Pic(Kc_bar)/2, or H^2(Q,Pic(Kc_bar)).  Those are the next
load-bearing adapters required before any Q-defined Brauer credit.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent
EXPECTED = {
    "j2-corrected-full-l-representative.json": "466b193b0fda90480484dbc520dcb5938879196c",
    "normalization_galois_skeleton.py": "139a309c52a6646e649d37bdb03c3bb535d29cf1",
    "xalpha_pair_galois_repair.py": "b7f37df50a123ef6c972aa210e7efb5f16535f76",
}


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


for name, sha in EXPECTED.items():
    assert git_blob_sha1(ROOT / name) == sha, (name, git_blob_sha1(ROOT / name), sha)

t, z = sp.symbols("t z")
s2 = sp.sqrt(2)
q = sp.expand(t**4 - 6*t**2 + 1)
r1 = 1 + s2
r2 = -(1 + s2)
r3 = s2 - 1
r4 = 1 - s2
assert sp.expand((t-r1)*(t-r2)*(t-r3)*(t-r4) - q) == 0
f2 = sp.cancel((t-r2)/(t-r4))


def red_z2(expr):
    expr = sp.together(sp.expand(expr))
    num, den = sp.fraction(expr)
    mod = sp.Poly(z**2-q, z, domain="EX")
    # Rationalize a z-linear denominator before reducing.
    den_cc = den.xreplace({z: -z})
    num = sp.rem(sp.Poly(sp.expand(num*den_cc), z, domain="EX"), mod).as_expr()
    den = sp.rem(sp.Poly(sp.expand(den*den_cc), z, domain="EX"), mod).as_expr()
    return sp.cancel(num/den)


def ct(expr):
    return sp.expand(expr.xreplace({s2: -s2}))


# sqrt(2)-conjugation sends r1<->r4 and r2<->r3.
assert sp.simplify(ct(r1)-r4) == 0
assert sp.simplify(ct(r4)-r1) == 0
assert sp.simplify(ct(r2)-r3) == 0
assert sp.simplify(ct(r3)-r2) == 0

ct_f2 = sp.cancel(ct(f2))
u_ct = sp.cancel((t-r3)*(t-r4)/z)
assert red_z2(ct_f2/f2 - u_ct**2) == 0
assert red_z2(u_ct*ct(u_ct) - 1) == 0

# Formal divisor vectors on the smooth quartic normalization.  Coordinates:
# [P_r1,P_r2,P_r3,P_r4,I_plus,I_minus].
# div(t-r_i)=2P_ri-I_plus-I_minus and
# div(z)=P_r1+P_r2+P_r3+P_r4-2I_plus-2I_minus.
div_t = []
for j in range(4):
    v = [0]*6
    v[j] = 2
    v[4] = v[5] = -1
    div_t.append(v)
div_z = [1,1,1,1,-2,-2]

def vadd(a,b): return [x+y for x,y in zip(a,b)]
def vsub(a,b): return [x-y for x,y in zip(a,b)]

div_f2 = vsub(div_t[1], div_t[3])
D = [0,1,0,-1,0,0]
assert div_f2 == [2*x for x in D]
# ct root permutation 1<->4, 2<->3.
ct_D = [-1,0,1,0,0,0]
ctD_minus_D = vsub(ct_D,D)
h_ct = sp.cancel(z/((t-r1)*(t-r2)))
div_h = vsub(vsub(div_z,div_t[0]),div_t[1])
assert div_h == ctD_minus_D
assert red_z2(h_ct*ct(h_ct)-1) == 0
assert red_z2(u_ct*ct(h_ct)-1) == 0

# Full split pair representative witnesses.  Complex conjugation swaps B+ and
# B- while fixing t,z,sqrt(2).  tau is the auxiliary d->-d automorphism and is
# trivial on this J2 subdatum.
ell = (f2, sp.Integer(1))
# ct(ell)=ell*(u_ct^2,1)
assert red_z2(ct_f2 - f2*u_ct**2) == 0
# cc(ell)=(1,f2)=diag(f2)*ell*((1/f2)^2,1)
cc_rhs = (sp.cancel(f2*f2*(1/f2)**2), f2)
assert sp.simplify(cc_rhs[0]-1) == 0 and sp.simplify(cc_rhs[1]-f2) == 0

cert = {
  "schema":"STAGE33_05_J2_CORRECTED_FULL_PAIR_PRE_KUMMER_DESCENT_COCHAIN_V1",
  "status":"PASS_EXACT_PRE_KUMMER_DESCENT_COCHAIN_NO_HS_D2_CREDIT",
  "scope":"CORRECTED_J2_FULL_L_REPRESENTATIVE_AND_NORMALIZATION_HALF_DIVISOR_ONLY",
  "source_locks":{
    "R2_corrected_pair_blob_sha1":EXPECTED["j2-corrected-full-l-representative.json"],
    "normalization_galois_blob_sha1":EXPECTED["normalization_galois_skeleton.py"],
    "xalpha_pair_galois_blob_sha1":EXPECTED["xalpha_pair_galois_repair.py"],
  },
  "normalization":{
    "equation":"z^2=q=t^4-6*t^2+1",
    "roots":{"r1":"1+sqrt(2)","r2":"-(1+sqrt(2))","r3":"sqrt(2)-1","r4":"1-sqrt(2)"},
    "f2":"(t-r2)/(t-r4)",
    "divisor_f2":"2*(P_r2-P_r4)",
    "half_divisor_D":"P_r2-P_r4"
  },
  "sqrt2_conjugation":{
    "root_permutation":["r1<->r4","r2<->r3"],
    "ct_f2_over_f2_square_witness":"u_ct=(t-r3)*(t-r4)/z",
    "identity_ct_f2_over_f2_equals_u_ct_squared":True,
    "u_ct_times_ct_u_ct":"1",
    "half_divisor_difference":"ct(D)-D=P_r3+P_r4-P_r1-P_r2",
    "principal_witness":"h_ct=z/((t-r1)*(t-r2))",
    "identity_div_h_ct_equals_ctD_minus_D":True,
    "h_ct_times_ct_h_ct":"1",
    "u_ct_relation":"u_ct=1/ct(h_ct)",
    "normalization_line_bundle_C2_descent_obstruction_zero":True
  },
  "full_split_pair":{
    "ell":"(f2,1)",
    "tau_action":"exactly fixed on this subdatum",
    "ct_action_relation":"ct(ell)=(ct(f2),1)=ell*(u_ct^2,1)",
    "cc_action":"component swap; cc(ell)=(1,f2)",
    "cc_action_relation":"cc(ell)=diag(f2)*ell*((1/f2)^2,1)",
    "representative_level_square_and_diagonal_witnesses_materialized":True,
    "warning":"These L*/(K*L*^2) representative witnesses are stronger than quotient-vector fixedness but are not yet a full-surface H^2(mu_2) lift."
  },
  "audit_boundary":{
    "geometric_J2_Galois_fixed_reconfirmed":True,
    "corrected_normalization_half_divisor_descent_cochain_materialized":True,
    "full_surface_mu2_lift_materialized":False,
    "pic_mod2_defect_1cocycle_materialized":False,
    "integral_Pic_lift_materialized":False,
    "HS_d2_2cocycle_materialized":False,
    "HS_d2_zero_proved":False,
    "Q_defined_arithmetic_Brauer_representative_proved":False,
    "forbidden_promotion":"Do not identify normalization half-divisor descent with the Kc surface Kummer lift without an explicit CV/surface Picard adapter."
  },
  "new_exact_information":"For corrected f2 the geometric half-divisor D=P_r2-P_r4 has an explicit sqrt(2)-descent isomorphism h_ct whose C2 cocycle is exactly trivial; the full split pair also has explicit tau/ct/cc square+diagonal representative witnesses. The remaining gap is now the functorial lift of this datum to H^2(Kc_bar,mu_2)/Pic and its integral Picard Bockstein, not Galois fixedness of the CV quotient.",
  "next_exact_leaf":"MATERIALIZE_CV_HALF_DIVISOR_TO_KC_SURFACE_MU2_LIFT_AND_COMPUTE_PIC_MOD2_DEFECT_THEN_HS_D2",
  "firewalls":{
    "R0_R4_retained":True,
    "R5_geometric_hostile_replay_pass":True,
    "Q_defined_descent_credit_restored":False,
    "stage33_05_reclosed":False,
    "stage33_12_closed_exact":False,
    "stage33_13_released":False,
    "theorem_credit":False,
    "receiver_credit":False,
    "endpoint_credit":False,
    "perfect_cuboid_existence_claim":False,
    "perfect_cuboid_nonexistence_claim":False,
    "stage33_progress":"5/11"
  }
}
canonical=json.dumps(cert,sort_keys=True,separators=(",",":")).encode()
cert["canonical_sha256"]=hashlib.sha256(canonical).hexdigest()
OUT=ROOT/"j2-corrected-pre-kummer-descent-cochain.json"
if OUT.exists():
    recorded=json.loads(OUT.read_text(encoding="utf-8"))
    assert recorded==cert, "recorded pre-Kummer descent certificate mismatch"
else:
    OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(cert,indent=2,sort_keys=True))
