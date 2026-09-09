#!/usr/bin/env python3
"""Verify Goal4BF: source-oriented Gaussian quartic lift and residual phase gauge."""
from __future__ import annotations

import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
P=lambda s: ROOT/s
ART=P("stages/stage35-ex/35ex-35/goal4bf-oriented-gaussian-quartic-reciprocity-reservoir-lift.json")
SRC=P("stages/stage35-ex/35ex-35/goal4bf-oriented-gaussian-quartic-reciprocity-reservoir-lift-source-lock.md")
BE=P("stages/stage35-ex/35ex-35/goal4be-gcd-reservoir-quadratic-reciprocity-cycle.json")
AU=P("stages/stage35-ex/35ex-35/goal4au-three-direction-marked-kummer-gcd-allocation.json")
AX=P("stages/stage35-ex/35ex-35/goal4ax-cross-face-lattice-norm-torsor-compatibility.json")
STATE=P("stages/stage35-ex/MAIN-STATE.json")
EXPECTED="73145db6fd0f1faa9622ccce183c06f09893ce3fe8497d65cb9f84df46fd799a"
SRC_BLOB="a54aa70b1a9e7b3a1f2a1b7daa77afcab1b4face"
BE_BLOB="5f72efb10727980670adb10bf56a4df333978dc2"
AU_BLOB="d0dd0597046daf54ad9fcc74991221710a27f12c"
AX_BLOB="208e153181185f9234f688f524432ae10579f5d4"
V74="STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"

def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def checkcanon(o):
    x=dict(o); got=x.pop("canonical_sha256")
    calc=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    assert got==calc==EXPECTED,(got,calc)

assert blob(SRC)==SRC_BLOB
assert blob(BE)==BE_BLOB
assert blob(AU)==AU_BLOB
assert blob(AX)==AX_BLOB
state=json.loads(STATE.read_text())
assert state["schema"]==V74
assert state["last_audited_authority"]["hostile_review_id"]==5142248509
assert state["claims"]["E1_proved"] is False

be=json.loads(BE.read_text())
assert be["canonical_sha256"]=="feffef319deaf6104fc14f1b055462e70ae99068fd8564c73e8cf86abbae1a16"
assert be["result"]["new_Jacobi_reciprocity_cycle_obtained"] is True
assert be["rank_analysis"]["one_pairwise_Jacobi_bit_free"] is True
assert be["next"]["unit"]=="35EX-35_GOAL4BF_ORIENTED_GAUSSIAN_QUARTIC_RECIPROCITY_RESERVOIR_LIFT_PREFLIGHT"
ax=json.loads(AX.read_text())
assert ax["result"]["positive_endpoint_open_reconstructed"] is True
assert ax["result"]["new_nontrivial_H1_torsor_class_obtained"] is False

src=SRC.read_text()
for m in ("(BF-iota-a)","(BF-Pa)","(BF-one-side)","(BF-val)","(BF-primary)","(BF-Sigma)","(BF-Q4a)","(BF-QR4)","(BF-two-phases)","(BF-square)","(BF-G)","(BF-5)","35EX-35_GOAL4BG_GAUSSIAN_SQUARE_ROOT_FACE_PHASE_COMPATIBILITY_PREFLIGHT"):
    assert m in src,m

# Exact ell=5 orientation diagnostic.  Primary pi=-1-2i has norm 5,
# a odd, b even, a+b=-3 == 1 mod 4, and selects i=2 mod 5.
p=5; a=-1; b=-2
assert a*a+b*b==p and a%2==1 and b%2==0 and (a+b-1)%4==0
root=(-a*pow(b,-1,p))%p
assert root==2 and root*root%p==p-1
# Both Goal4BE local models select the same total ratio/root.
for x,bb in ((1,2),(2,1)):
    y=c=1
    ratio=(x*bb*pow(y*c,-1,p))%p
    assert ratio==root
    # x*b-i*y*c vanishes in Z[i]/pi via i -> root.
    assert (x*bb-root*y*c)%p==0
# The order-four residue character at norm 5 is exponent 1.
assert pow(2,(p-1)//4,p)==root

art=json.loads(ART.read_text()); checkcanon(art)
assert art["source_locks"]["goal4bf_source"]["blob_sha1"]==SRC_BLOB
assert art["source_locks"]["goal4be"]["blob_sha1"]==BE_BLOB
assert art["source_locks"]["goal4au"]["blob_sha1"]==AU_BLOB
assert art["source_locks"]["goal4ax"]["blob_sha1"]==AX_BLOB
parent=art["stacked_parent"]
assert parent["exact_head_sha"]=="c44909b47f00091da6229d60304786dc446f6a37"
assert parent["aggregate_run"]==34305612045
assert parent["aggregate_job"]==102322719891
og=art["oriented_gaussian_primes"]
assert og["conjugate_selected_factor_A"] is False
assert og["unique_primary_generator"] is True
assert art["oriented_kernels"]["source_orientation_canonical"] is True
q=art["quartic_lift"]
assert q["square_recovers_goal4be_quadratic_character"] is True
assert q["norm_correction_explicit"] is True
pg=art["phase_gauge"]
assert pg["oriented_reciprocity_eliminates_all_conjugate_phases"] is False
assert pg["goal4be_free_bit_closed"] is False
res=art["result"]
assert res["source_oriented_gaussian_prime_lift_obtained"] is True
assert res["cross_conjugate_phase_gauge_remains"] is True
assert res["quartic_reciprocity_alone_closes_BE_free_bit"] is False
assert res["new_branch_pruning_obtained"] is False
assert art["next"]["unit"]=="35EX-35_GOAL4BG_GAUSSIAN_SQUARE_ROOT_FACE_PHASE_COMPATIBILITY_PREFLIGHT"
for k,v in art["credit_firewall"].items(): assert v is False,(k,v)
print("STAGE35_EX_GOAL4BF_ORIENTED_GAUSSIAN_QUARTIC_LIFT=PASS")
print("source_orientation_canonical=true")
print("cross_conjugate_phase_gauge_remains=true")
print("BE_free_bit_closed=false")
print("branch_pruning=false")
print("canonical_sha256="+EXPECTED)
