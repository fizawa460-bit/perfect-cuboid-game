#!/usr/bin/env python3
"""Verify Goal4BS: parking audit and intermediate hostile-audit checkpoint."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bs-post-boundary-derived-backup-parking-audit.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bs-post-boundary-derived-backup-parking-audit-source-lock.md")
BR = P("stages/stage35-ex/35ex-35/goal4br-derived-fourth-square-defect-squareclass.json")
BQ = P("stages/stage35-ex/35ex-35/goal4bq-y-zero-boundary-escape-conductor-depth.json")
E02 = P("stages/stage35-ex/35ex-02/canonical-gcd-and-2adic-lemma.md")
E03 = P("stages/stage35-ex/35ex-03/double-primitive-counterexample-normal-form.md")
E04 = P("stages/stage35-ex/35ex-04/product-rectangle-reduction.md")
E05 = P("stages/stage35-ex/35ex-05/result.md")
E06 = P("stages/stage35-ex/35ex-06/four-factor-gcd-support.md")
POL = P("docs/research-os/policies/hostile-audit-and-freshness.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "15cc0c486f6a95342010b8097469082b0069504aded8b393a9ff9c966997f88b"
LOCKS = {
    SRC:"374a30ad8b69610120ee79ab40a8a517814a091c",
    BR:"93b27e113b96567ee9c76434eca9ec3148c2628f",
    BQ:"e9917a4b14d14c105a6474c8ebba478af9f76d8f",
    E02:"9df24c83ed23e5d13397a2971706a5ac7def9461",
    E03:"af067616178b4b146265acc831ec5d0f2a380e23",
    E04:"186226223798e89e97d504ead7931b8209d63282",
    E05:"be6facc351eb864258b7f2ced3baf85f3dbbbfe9",
    E06:"9f3a3215536f7b9c52ddfd629b9af856fd7bb86c",
    POL:"39e230600300569818fc3a78784bf780b4463588",
}
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"

def blob(path: Path) -> str:
    b=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

for path, expected in LOCKS.items():
    assert blob(path)==expected, (path, blob(path), expected)

state=json.loads(STATE.read_text())
assert state["schema"]==V74
assert state["last_audited_authority"]["hostile_review_id"]==5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

br=json.loads(BR.read_text())
bq=json.loads(BQ.read_text())
assert br["canonical_sha256"]=="d6793ec7438854df18d3a3335d7a513c2edab7f5fde4bcf7b9af75b98a3e67ea"
assert br["result"]["new_branch_pruning_obtained"] is False
assert bq["canonical_sha256"]=="6a1642dda5e86c545ae2ae8123e98114b7a339e587f77e6f4a26118a70f88360"
assert bq["result"]["global_endpoint_height_adapter_obtained"] is False

assert "g0 = c*p" in E02.read_text()
assert "two simultaneous primitive-Pythagorean branches" in E05.read_text()
assert "FINITE_SQUARECLASS_REDUCTION_PROVED=false" in E06.read_text()

pol=POL.read_text()
assert "roughly `90` commits" in pol
assert "intermediate hostile audit" in pol
assert "Do not push additional substantive retained mathematical work" in pol

src=SRC.read_text()
for marker in (
    "LIVE:\n  none",
    "UNTESTED_AND_ACTIONABLE_WITH_CURRENT_RETAINED_INPUTS:\n  none",
    "HISTORICAL_EQUIVALENT_TO_35EX_02_THROUGH_06",
    "BLOCKED_MISSING_GLOBAL_RATIONAL_REALIZATION_HEIGHT_ADAPTER",
    "INTERMEDIATE_HOSTILE_AUDIT_CHECKPOINT=true",
    "CYCLE_PARKING_AUDIT_COMPLETE=true",
):
    assert marker in src, marker

art=json.loads(ART.read_text())
x=dict(art)
got=x.pop("canonical_sha256")
calc=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
assert got==calc==EXPECTED, (got,calc)
assert art["stacked_parent"]["exact_head_sha"]=="85b3e201c75030139977540c3bd8c274084851a5"
assert art["stacked_parent"]["aggregate_run"]==34323244536
assert art["stacked_parent"]["aggregate_job"]==102376597662
assert art["breadth_audit"]["live_candidates"]==0
assert art["breadth_audit"]["untested_actionable_candidates"]==0
assert art["breadth_audit"]["parking_audit_complete"] is True
assert art["classifications"]["pesch_canonical_gcd_factor_graph"]=="HISTORICAL_EQUIVALENT_TO_35EX_02_THROUGH_06"
assert art["checkpoint"]["retained_commit_count_at_parent"]==91
assert art["checkpoint"]["warning_zone_entered"] is True
assert art["checkpoint"]["intermediate_hostile_audit_checkpoint"] is True
assert art["checkpoint"]["freeze_after_exact_green"] is True
assert art["checkpoint"]["self_awarded_hostile_audit_pass"] is False
assert art["checkpoint"]["further_substantive_retained_research_allowed_before_audit"] is False
assert art["result"]["hostile_audit_pass_awarded"] is False
assert art["result"]["new_branch_pruning_obtained"] is False
assert art["result"]["E1_proved"] is False
assert art["next"]["action"]=="RUN_INDEPENDENT_INTERMEDIATE_HOSTILE_AUDIT_ON_EXACT_GOAL4BS_HEAD"
assert all(v is False for v in art["credit_firewall"].values())

print("STAGE35_EX_GOAL4BS_PARKING_CHECKPOINT=PASS")
print("live_candidates=0")
print("parking_audit_complete=true")
print("intermediate_hostile_audit_checkpoint=true")
print("hostile_audit_pass_awarded=false")
print("canonical_sha256="+EXPECTED)
