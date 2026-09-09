#!/usr/bin/env python3
"""Verify Goal4BP: post-Gaussian blind/Arsenal fresh-route audit."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s
ART = P("stages/stage35-ex/35ex-35/goal4bp-post-gaussian-ray-tower-fresh-route-audit.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bp-post-gaussian-ray-tower-fresh-route-audit-source-lock.md")
BO = P("stages/stage35-ex/35ex-35/goal4bo-deeper-lambda8-order-lift.json")
BB = P("stages/stage35-ex/35ex-35/goal4bb-arbitrary-finite-brauer-subgroup-nonobstruction.json")
AQ = P("stages/stage35-ex/35ex-35/goal4aq-unit-character-bm-endpoint-equivalence.json")
AY = P("stages/stage35-ex/35ex-35/goal4ay-derived-cuboid-involution-nonlinear-descent.json")
CYCLE = P("docs/research-os/policies/cycle-exploration-safety-protocol.md")
S34 = P("docs/arsenal/cards/formal/S34-W01.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")
EXPECTED = "da3394acde77d9e7f13d83bc04466d6e8aafbeabac40314af286871d3dcf3c8e"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"

def blob(path: Path) -> str:
    b = path.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def checkcanon(obj: dict) -> None:
    x=dict(obj); got=x.pop("canonical_sha256")
    calc=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    assert got==calc==EXPECTED,(got,calc)

locks = {
 SRC:"27e9db18a68fcd7d90898fda8fd093fea6e55171",
 BO:"08f70a2dbd3c2b61e246d26835046965dc13d412",
 BB:"54190746afae7e6e8fece7b065311a5ae0b36023",
 AQ:"593d22b7905d93451e43311540be1c219bbc75d7",
 AY:"2cb4e8fc58690b4a820c02c5e0e52ec0a299333c",
 CYCLE:"4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37",
 S34:"01a8e90e34b4aa46edbfa825803d488e5230e9d0",
}
for p,h in locks.items(): assert blob(p)==h,(p,blob(p),h)
state=json.loads(STATE.read_text())
assert state["schema"]==V74
assert state["last_audited_authority"]["hostile_review_id"]==5142248509
assert state["claims"]["E1_proved"] is False and state["claims"]["stage35_closed"] is False
bo=json.loads(BO.read_text()); bb=json.loads(BB.read_text()); aq=json.loads(AQ.read_text()); ay=json.loads(AY.read_text())
assert bo["canonical_sha256"]=="20439e1eda541da3bb8f8b8d5bbac1cc7e4f476ad9b7dc69ed5632a7cbfd8c9b"
assert bo["result"]["mechanical_deeper_conductor_route_fail_closed"] is True
assert bb["result"]["every_finite_Brauer_subgroup_BM_nonempty"] is True
assert aq["result"]["full_unit_character_route"]=="ENDPOINT_EQUIVALENT_BLOCKER"
assert ay["result"]["classical_operator_full_fourth_square_preservation_obtained"] is False
src=SRC.read_text()
for marker in ("BP-A", "BP-B", "Y_ZERO_BOUNDARY_ESCAPE_CONDUCTOR_DEPTH", "DERIVED_FOURTH_SQUARE_DEFECT_TWO_CYCLE", "S34-W01", "CYCLE_EXHAUSTIVE_VIEW_AUDIT=true", "35EX-35_GOAL4BQ_Y_ZERO_BOUNDARY_ESCAPE_CONDUCTOR_DEPTH_PREFLIGHT"):
    assert marker in src,marker
art=json.loads(ART.read_text()); checkcanon(art)
p=art["stacked_parent"]
assert p["exact_head_sha"]=="c23d7f9bbcd43b1ebbfa233e7fc1e8c6612d48da"
assert p["aggregate_run"]==34318593424 and p["aggregate_job"]==102362097586
assert p["hostile_audited"] is False
assert art["blind_pass"]["executed_before_arsenal"] is True
assert art["blind_pass"]["gaussian_carrier_re_evaluation_forbidden_as_new_route"] is True
assert art["ledger"]["live"]==["Y_ZERO_BOUNDARY_ESCAPE_CONDUCTOR_DEPTH"]
assert art["ledger"]["untested"]==["DERIVED_FOURTH_SQUARE_DEFECT_TWO_CYCLE"]
sv=art["selected_new_view"]
assert sv["removed_boundary"]=="y=0" and sv["arsenal_direct_weapon_found"] is False
bv=art["backup_view"]
assert bv["S34_W01_triggered"] is False
ce=art["cycle_exit"]
assert ce["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True and ce["CYCLE_BLIND_REDISCOVERY"] is True
assert ce["CYCLE_SPLIT_TRIGGERED"] is False
res=art["result"]
assert res["post_gaussian_fresh_view_audit_complete"] is True
assert res["new_source_fixed_boundary_view_selected"] is True
assert res["derived_fourth_square_defect_preserved_untested"] is True
assert res["branch_pruning_obtained"] is False
assert art["next"]["unit"]=="35EX-35_GOAL4BQ_Y_ZERO_BOUNDARY_ESCAPE_CONDUCTOR_DEPTH_PREFLIGHT"
for k,v in art["credit_firewall"].items(): assert v is False,(k,v)
print("STAGE35_EX_GOAL4BP_POST_GAUSSIAN_FRESH_ROUTE_AUDIT=PASS")
print("selected=Y_ZERO_BOUNDARY_ESCAPE_CONDUCTOR_DEPTH")
print("backup=DERIVED_FOURTH_SQUARE_DEFECT_TWO_CYCLE")
print("split_triggered=false")
print("canonical_sha256="+EXPECTED)
