#!/usr/bin/env python3
"""Verify Goal4BR: derived fourth-square defect squareclass and reservoir swap."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4br-derived-fourth-square-defect-squareclass.json")
SRC = P("stages/stage35-ex/35ex-35/goal4br-derived-fourth-square-defect-squareclass-source-lock.md")
BQ = P("stages/stage35-ex/35ex-35/goal4bq-y-zero-boundary-escape-conductor-depth.json")
AY = P("stages/stage35-ex/35ex-35/goal4ay-derived-cuboid-involution-nonlinear-descent.json")
AU = P("stages/stage35-ex/35ex-35/goal4au-three-direction-marked-kummer-gcd-allocation.json")
GCD = P("stages/stage35-ex/35ex-35/private-edge-gcd-six-variable-decomposition.json")
S34 = P("docs/arsenal/cards/formal/S34-W01.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "d6793ec7438854df18d3a3335d7a513c2edab7f5fde4bcf7b9af75b98a3e67ea"
SRC_BLOB = "07eaad7797a9a4f2f21852ea90dce633fac23a07"
BQ_BLOB = "e9917a4b14d14c105a6474c8ebba478af9f76d8f"
AY_BLOB = "2cb4e8fc58690b4a820c02c5e0e52ec0a299333c"
AU_BLOB = "d0dd0597046daf54ad9fcc74991221710a27f12c"
GCD_BLOB = "d0cd03a5ff744d5f6536b6d2784c0e0d543fea48"
S34_BLOB = "01a8e90e34b4aa46edbfa825803d488e5230e9d0"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def checkcanon(obj: dict) -> None:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)


for path, expected in ((SRC,SRC_BLOB),(BQ,BQ_BLOB),(AY,AY_BLOB),(AU,AU_BLOB),(GCD,GCD_BLOB),(S34,S34_BLOB)):
    assert blob(path) == expected, (path, blob(path), expected)

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

bq = json.loads(BQ.read_text())
assert bq["canonical_sha256"] == "6a1642dda5e86c545ae2ae8123e98114b7a339e587f77e6f4a26118a70f88360"
assert bq["result"]["boundary_depth_D_n_equals_n"] is True
assert bq["result"]["global_endpoint_height_adapter_obtained"] is False

ay = json.loads(AY.read_text())
assert ay["canonical_sha256"] == "513e4085d1f5309a52580c3f716db0de6e549a07619351e4098e3b159766c41d"
assert ay["derived_operator"]["six_variable_action"] == "(x,y,z ; a,b,c) -> (a,b,c ; x,y,z)"
assert ay["derived_operator"]["involution"] is True
assert ay["fourth_square_gate"]["derived_fourth_square_from_original_proved"] is False

# Symbolic completion identity after six-variable reduction.
x,y,z,a,b,c = sp.symbols("x y z a b c")
rab2=(y*a)**2+(z*b)**2
rac2=(x*a)**2+(z*c)**2
rbc2=(x*b)**2+(y*c)**2
P2=sp.expand(rab2*rac2*rbc2)
R2=(x*y*z*a*b*c)**2
W2=(x*y*a)**2+(x*z*b)**2+(y*z*c)**2
QD=(x*a*b)**2+(y*a*c)**2+(z*b*c)**2
assert sp.expand(P2+R2-W2*QD) == 0

# Deterministic regression on classical Euler bricks. This is evidence replay,
# not the proof of the global statements; the source lock contains the primewise proof.
BRICKS=[
    (44,117,240),(85,132,720),(140,480,693),(160,231,792),
    (240,252,275),(429,880,2340),(495,4888,8160),
]
for A,B,C in BRICKS:
    X=math.gcd(A,B); Y=math.gcd(A,C); Z=math.gcd(B,C)
    aa=A//(X*Y); bb=B//(X*Z); cc=C//(Y*Z)
    rab=math.isqrt((Y*aa)**2+(Z*bb)**2)
    rac=math.isqrt((X*aa)**2+(Z*cc)**2)
    rbc=math.isqrt((X*bb)**2+(Y*cc)**2)
    assert rab*rab == (Y*aa)**2+(Z*bb)**2
    assert rac*rac == (X*aa)**2+(Z*cc)**2
    assert rbc*rbc == (X*bb)**2+(Y*cc)**2
    PP=rab*rac*rbc; RR=X*Y*Z*aa*bb*cc
    G=math.gcd(PP,RR)
    ha=math.gcd(aa,rbc); hb=math.gcd(bb,rac); hc=math.gcd(cc,rab)
    jx=math.gcd(X,rab); jy=math.gcd(Y,rac); jz=math.gcd(Z,rbc)
    assert G == ha*hb*hc*jx*jy*jz
    p=PP//G; r=RR//G
    assert math.gcd(p,r)==1 and p%2==1 and r%2==0
    qd=(X*aa*bb)**2+(Y*aa*cc)**2+(Z*bb*cc)**2
    sf=[prime for prime,e in sp.factorint(qd).items() if e%2]
    assert all(prime%4==1 for prime in sf), (A,B,C,qd,sf)

src = SRC.read_text()
for marker in (
    "(BR-QD)", "(BR-COMP)", "(BR-CLASS)", "(BR-SUPPORT)",
    "(BR-face-gcd)", "(BR-GFACT)", "(BR-STRIP)", "(BR-extra)",
    "(BR-RES-SWAP)", "(BR-DEFECT-CYCLE)", "S34_W01_TRIGGERED=false",
    "35EX-35_GOAL4BS_POST_BOUNDARY_DERIVED_BACKUP_PARKING_AUDIT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["stacked_parent"]["exact_head_sha"] == "930c649ed32104c3faf1f22074423707ad2c6a40"
assert art["stacked_parent"]["aggregate_run"] == 34322296008
assert art["stacked_parent"]["aggregate_job"] == 102373228786
assert art["source_locks"]["goal4br_source"]["blob_sha1"] == SRC_BLOB
assert art["completion"]["identity"] == "P^2+R^2=W^2*Q_D"
assert art["completion"]["gcd_p_r"] == 1
assert art["completion"]["p_parity"] == "odd"
assert art["completion"]["r_parity"] == "even"
assert art["reservoir_factorization"]["G_factorization"] == "G=h_a*h_b*h_c*j_x*j_y*j_z"
assert art["squareclass_support"]["Q_D_squarefree_even_prime_present"] is False
assert art["squareclass_support"]["Q_D_squarefree_3mod4_prime_present"] is False
assert art["conditional_square_receiver"]["extra_hypothesis_from_original_endpoint"] is False
assert art["derived_involution"]["reservoir_swap"] == "(h_a,h_b,h_c) <-> (j_x,j_y,j_z)"
assert art["arsenal_boundary"]["S34_W01_triggered"] is False
res=art["result"]
assert res["Q_D_squarefree_support_only_odd_1mod4"] is True
assert res["original_endpoint_forces_Q_D_square"] is False
assert res["finite_squareclass_family_obtained"] is False
assert res["strict_descent_obtained"] is False
assert res["new_branch_pruning_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BS_POST_BOUNDARY_DERIVED_BACKUP_PARKING_AUDIT"
assert all(v is False for v in art["credit_firewall"].values())

print("STAGE35_EX_GOAL4BR_DERIVED_DEFECT_SQUARECLASS=PASS")
print("Q_D_squarefree_support_only_odd_1mod4=true")
print("reservoir_swap=h<->j")
print("original_endpoint_forces_Q_D_square=false")
print("S34_W01_triggered=false")
print("canonical_sha256="+EXPECTED)
