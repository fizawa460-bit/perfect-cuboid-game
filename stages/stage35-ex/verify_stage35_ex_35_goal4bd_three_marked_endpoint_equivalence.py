#!/usr/bin/env python3
"""Verify Goal4BD simultaneous three-marked receiver and endpoint-equivalence collapse."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART=P("stages/stage35-ex/35ex-35/goal4bd-simultaneous-three-marked-rankjump-endpoint-equivalence.json")
SRC=P("stages/stage35-ex/35ex-35/goal4bd-simultaneous-three-marked-rankjump-endpoint-equivalence-source-lock.md")
BC=P("stages/stage35-ex/35ex-35/goal4bc-post-goal4as-ledger-exhaustion-fresh-view-audit.json")
L=P("stages/stage35-ex/35ex-35/goal4l-stage14-pythagorean-elliptic-rankjump-receiver.json")
K=P("stages/stage35-ex/35ex-35/goal4k-ratio-discriminant-biquartic-quotient-preflight.json")
AT=P("stages/stage35-ex/35ex-35/goal4at-marked-residual-kummer-local-support.json")
CARD=P("docs/arsenal/cards/formal/S34-W03.md")
STATE=P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED="1fae939f20184ac5bd61b2b9751fb3628201bdd7321f605aade34d5a9de2595e"
LOCKS={
 SRC:"94d010909544cfb8ca823f303436cf3405219d1a",
 BC:"5a5927b35859a6e1500f2fadf9a62b09feeb12e0",
 L:"0717ca307162d5559a005801848288daa91285fd",
 K:"7943d5f1f76354fbca6e89d42a0fc90b10e976c7",
 AT:"3e6949c18b044e38632ba840c3cb7b45b7e62302",
 CARD:"1d5275321f42768a6414d4610ac912c63be43f96",
}
V74="STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"

def blob(path:Path)->str:
    b=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

for p,w in LOCKS.items():
    assert blob(p)==w,(p,blob(p),w)

state=json.loads(STATE.read_text())
assert state["schema"]==V74
assert state["last_audited_authority"]["hostile_review_id"]==5142248509
assert state["claims"]["E1_proved"] is False

bc=json.loads(BC.read_text())
assert bc["canonical_sha256"]=="8fc7c10847b7d819fa267696eca84439304b15f253a7ca9a0f37b0e2e2ab89ea"
assert bc["selected_new_view"]["id"]=="SIMULTANEOUS_THREE_MARKED_RANKJUMP_FIBER_PRODUCT_RECEIVER"
assert bc["next"]["unit"]=="35EX-35_GOAL4BD_SIMULTANEOUS_THREE_MARKED_RANKJUMP_FIBER_PRODUCT_PREFLIGHT"

lj=json.loads(L.read_text())
assert lj["birational_adapter"]["rational_point_transport_complete"] is True
assert lj["birational_adapter"]["elliptic_curve"]=="E_q: Y^2=X*(X-1)*(X+q^2)"
kj=json.loads(K.read_text())
assert "H^2=" in kj["genus_one_receiver"]["curve"]
assert kj["converse_boundary"]["generic_quotient_forgets_common_squareclass"] is True
at=json.loads(AT.read_text())
assert at["source_recovery"]["p"]=="-B/C"
assert at["source_recovery"]["z"]=="D_AB/D_AC"

# Exact cyclic edge/ratio identities.
A,B,C=sp.symbols("A B C", nonzero=True)
RAB=A*A+B*B; RAC=A*A+C*C; RBC=B*B+C*C; W2=A*A+B*B+C*C
pA=-B/C; pB=-C/A; pC=-A/B
zA2=RAB/RAC; zB2=RBC/RAB; zC2=RAC/RBC
assert sp.factor(pA*pB*pC)==-1
assert sp.factor(zA2*zB2*zC2)==1
assert sp.factor(zA2*pC**2*(1+pB**2)-(1+pC**2))==0
assert sp.factor(zB2*pA**2*(1+pC**2)-(1+pA**2))==0
assert sp.factor(zC2*pB**2*(1+pA**2)-(1+pB**2))==0

# Exact quartic-to-space-square identities.
QA=sp.factor((pA**2-zA2)*(zA2-pA**-2))
QB=sp.factor((pB**2-zB2)*(zB2-pB**-2))
QC=sp.factor((pC**2-zC2)*(zC2-pC**-2))
wantA=sp.factor((A*(B**2-C**2)/(B*C*RAC))**2*W2)
wantB=sp.factor((B*(C**2-A**2)/(C*A*RAB))**2*W2)
wantC=sp.factor((C*(A**2-B**2)/(A*B*RBC))**2*W2)
assert sp.factor(QA-wantA)==0
assert sp.factor(QB-wantB)==0
assert sp.factor(QC-wantC)==0

# Four cross equations are generically independent: exact rational witness.
pa,pb,pc,za,zb,zc=sp.symbols("pa pb pc za zb zc")
f=[
 pa*pb*pc+1,
 za*zb*zc-1,
 za**2*pc**2*(1+pb**2)-(1+pc**2),
 zb**2*pa**2*(1+pc**2)-(1+pa**2),
]
J=sp.Matrix(f).jacobian([pa,pb,pc,za,zb,zc])
w={pa:sp.Rational(-39,80),pb:sp.Rational(-60,11),pc:sp.Rational(-44,117),
   za:sp.Rational(125,244),zb:sp.Rational(267,125),zc:sp.Rational(244,267)}
assert all(sp.factor(x.subs(w))==0 for x in f)
assert J.subs(w).rank()==4

# Primitive common-squareclass odd-prime linear identities.
assert sp.expand(RAB+RAC-RBC)==2*A*A
assert sp.expand(RAB+RBC-RAC)==2*B*B
assert sp.expand(RAC+RBC-RAB)==2*C*C

# 2-adic parity branch: all three face sums even forces all edge parities equal;
# primitive then all odd, and three odd squares sum to 3 mod 8.
allowed=[]
for a in (0,1):
  for b in (0,1):
    for c in (0,1):
      if a==b==c==0: continue
      if (a+b)%2==0 and (a+c)%2==0 and (b+c)%2==0:
        allowed.append((a,b,c))
assert allowed==[(1,1,1)]
assert (1+1+1)%8==3
assert all((s*s)%8 in (0,1,4) for s in range(8))
assert 3 not in {(s*s)%8 for s in range(8)}

src=SRC.read_text()
for marker in ("(BD-P)","(BD-Z)","(BD-FR)","(BD-WA)","(BD-WB)","(BD-WC)",
               "(BD-DELTA)","(BD-ODD)","(BD-2)","(BD-COLLAPSE)","(BD-EQUIV)",
               "35EX-35_GOAL4BE_GCD_RESERVOIR_QUADRATIC_RECIPROCITY_CYCLE_PREFLIGHT"):
    assert marker in src,marker

art=json.loads(ART.read_text())
x=dict(art); got=x.pop("canonical_sha256")
calc=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
assert got==calc==EXPECTED,(got,calc)
assert art["authority"]["state_schema"]==V74
assert art["stacked_parent"]["exact_head_sha"]=="d10024852a7f32605e769edf3c2b57406ea1175e"
assert art["stacked_parent"]["aggregate_run"]==34303815379
assert art["stacked_parent"]["aggregate_job"]==102317031982
assert art["cross_face_compatibility"]["independent_cross_equation_count"]==4
assert art["dimension"]["joint_receiver_generic_dimension"]==2
assert art["space_square_identity"]["joint_rational_point_forces_W2_square"] is True
assert art["common_face_squareclass"]["odd_support_empty"] is True
assert art["common_face_squareclass"]["delta_trivial_forced"] is True
assert art["endpoint_equivalence"]["positive_rational_perfect_cuboid_endpoint_equivalent"] is True
assert art["endpoint_equivalence"]["joint_receiver_smaller_than_endpoint"] is False
assert art["result"]["endpoint_equivalence_obtained"] is True
assert art["result"]["new_branch_pruning_obtained"] is False
assert art["next"]["unit"]=="35EX-35_GOAL4BE_GCD_RESERVOIR_QUADRATIC_RECIPROCITY_CYCLE_PREFLIGHT"
for k,v in art["credit_firewall"].items():
    assert v is False,(k,v)

print("STAGE35_EX_GOAL4BD_THREE_MARKED_ENDPOINT_EQUIVALENCE=PASS")
print("cross_equation_rank=4")
print("joint_receiver_generic_dimension=2")
print("common_face_squareclass_delta=1")
print("endpoint_equivalence=true")
print("branch_pruning=false")
print("canonical_sha256="+EXPECTED)
