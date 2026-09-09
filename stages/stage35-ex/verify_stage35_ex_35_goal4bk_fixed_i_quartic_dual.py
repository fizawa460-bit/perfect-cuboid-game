#!/usr/bin/env python3
"""Verify Goal4BK: fixed-i quartic dual and surviving 2-adic ray-class compensator."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s
ART = P("stages/stage35-ex/35ex-35/goal4bk-fixed-i-quartic-dual-two-adic-ray-class.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bk-fixed-i-quartic-dual-two-adic-ray-class-source-lock.md")
BJ = P("stages/stage35-ex/35ex-35/goal4bj-global-gaussian-k2-quartic-character-adapter.json")
BH = P("stages/stage35-ex/35ex-35/goal4bh-reservoir-leading-unit-space-face-sign-cycle.json")
BF = P("stages/stage35-ex/35ex-35/goal4bf-oriented-gaussian-quartic-reciprocity-reservoir-lift.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")
EXPECTED = "9d2ce7bedca1d38716903027d05aa58b6672c2fd069dc4121a0e7c579c94a636"
SRC_BLOB = "5d37b13027562d039f15f2ec1bb635d3f0a5809e"
BJ_BLOB = "b8a20fd879a80215e9fa3fa8094bf979565de3c8"
BH_BLOB = "80534af2bc071cbc3a2d6426c495cd3d5e6dbefc"
BF_BLOB = "b015280d80c958608bdbabd3a590c0bf482b25bc"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"

def blob(path: Path) -> str:
    b=path.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def checkcanon(obj: dict) -> None:
    x=dict(obj); got=x.pop("canonical_sha256")
    calc=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    assert got==calc==EXPECTED,(got,calc)

for p,e in ((SRC,SRC_BLOB),(BJ,BJ_BLOB),(BH,BH_BLOB),(BF,BF_BLOB)):
    assert blob(p)==e,(p,blob(p),e)
state=json.loads(STATE.read_text())
assert state["schema"]==V74
assert state["last_audited_authority"]["hostile_review_id"]==5142248509
assert state["claims"]["E1_proved"] is False and state["claims"]["stage35_closed"] is False
bj=json.loads(BJ.read_text())
assert bj["canonical_sha256"]=="a1208a9ac7ec291074a36fe4d795e13b31eee22653fa83bcdef3b7eae120ac4e"
assert bj["result"]["global_gaussian_orientation_carrier_constructed"] is True
assert bj["result"]["quartic_class_recovers_sigma"] is True
src=SRC.read_text()
for marker in ("(BK-Xi)","(BK-val)","(BK-chi)","(BK-supp-i)","(BK-primary-examples)","(BK-primary-Xi)","(BK-ratio-a)","(BK-q)","CANONICAL_FIXED_I_QUARTIC_DUAL=true","35EX-35_GOAL4BL_XI_TWO_ADIC_RAY_CLASS_PARITY_PREFLIGHT"):
    assert marker in src,marker
art=json.loads(ART.read_text()); checkcanon(art)
assert art["source_locks"]["goal4bk_source"]["blob_sha1"]==SRC_BLOB
assert art["source_locks"]["goal4bj"]["blob_sha1"]==BJ_BLOB
parent=art["stacked_parent"]
assert parent["exact_head_sha"]=="ffbb6ee4864490113bfa551fb1e14614c30f5051"
assert parent["aggregate_run"]==34312988913 and parent["aggregate_job"]==102344458981
fd=art["fixed_unit_quartic_dual"]
assert fd["ambient_canonical_dual_constructed"] is True
assert fd["source_fixed_value_constructed"] is False
supp=art["supplementary_law"]
assert supp["formula"]=="(i/(A+B*i))_4=i^((1-A)/2) for primary A+B*i"
assert supp["primary_fixes_A_mod_8"] is False
assert [x["norm"] for x in supp["examples"]]==[5,13,17]
two=art["two_adic_compensator"]
assert two["primary_congruence_forces_chi_i_Xi_constant"] is False
assert two["two_adic_ray_class_value_source_fixed"] is False
co=art["cofactor_test"]
assert "sigma_a*" in co["direction_A_ratio"]
assert co["normalization_is_prime_dependent"] is True
assert co["fixed_global_source_cofactor_dual_obtained"] is False
res=art["result"]
assert res["canonical_fixed_i_quartic_dual_obtained"] is True
assert res["chi_i_has_local_orientation_sensitivity"] is True
assert res["chi_i_Xi_source_constant_obtained"] is False
assert res["two_adic_ray_class_compensator_remains"] is True
assert res["global_quartic_reciprocity_contradiction_obtained"] is False
assert res["new_branch_pruning_obtained"] is False
assert art["next"]["unit"]=="35EX-35_GOAL4BL_XI_TWO_ADIC_RAY_CLASS_PARITY_PREFLIGHT"
for k,v in art["credit_firewall"].items(): assert v is False,(k,v)
print("STAGE35_EX_GOAL4BK_FIXED_I_QUARTIC_DUAL=PASS")
print("canonical_fixed_i_dual=true")
print("two_adic_ray_class_compensator_remains=true")
print("canonical_sha256="+EXPECTED)
