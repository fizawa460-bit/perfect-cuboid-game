#!/usr/bin/env python3
"""Verify consumption of the independent Goal4BS intermediate hostile-audit PASS."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RECEIPT = ROOT / "stages/stage35-ex/35ex-35/goal4bs-intermediate-hostile-audit-pass-consumption.json"
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"
HANDOFF = ROOT / "stages/stage35-ex/MAIN-BATCH-HANDOFF.md"

r = json.loads(RECEIPT.read_text())
s = json.loads(STATE.read_text())
h = HANDOFF.read_text()

assert r["schema"] == "STAGE35_EX_GOAL4BS_INTERMEDIATE_HOSTILE_AUDIT_PASS_CONSUMPTION_V1"
assert r["status"] == "AUDITED_INTERMEDIATE_PARKING_CHECKPOINT_CONSUMED_NO_E1_CREDIT"
assert r["audit"]["result"] == "PASS"
assert r["audit"]["review_id"] == 5151846948
assert r["audit"]["audited_exact_head_sha"] == "d6f5151c9d95304afe7081c92f40f1d25cc4aa3b"
assert r["audit"]["credit_ceiling"] == "AUDITED_INTERMEDIATE_STAGE35EX_PARKING_CHECKPOINT_NO_E1_CREDIT"
assert r["exact_head_ci"]["aggregate_run"] == 34327910281
assert r["exact_head_ci"]["aggregate_current_job"] == 102390869295
assert r["exact_head_ci"]["goal4bs_checkpoint_run"] == 34327910480
assert r["exact_head_ci"]["goal4bs_checkpoint_job"] == 102389372990
assert r["authority_boundary"]["mathematical_authority_unit"] == "35EX-35_GOAL4AK_SECOND_CLASS_QI_CYCLIC_EXPLICIT_F_B_ASSEMBLY"
assert r["authority_boundary"]["mathematical_authority_hostile_review_id"] == 5142248509
assert r["authority_boundary"]["intermediate_checkpoint_hostile_review_id"] == 5151846948
assert r["authority_boundary"]["goal4bs_audited"] is True
assert r["authority_boundary"]["goal4bs_promoted_to_E1"] is False
assert r["parking"]["live_candidates"] == 0
assert r["parking"]["untested_actionable_with_current_retained_inputs"] == 0
assert r["parking"]["parking_audit_complete"] is True
assert r["parking"]["shared_pr_freeze_for_intermediate_audit_released"] is True
assert r["parking"]["route_status"] == "PARKED_AUDITED_REOPEN_GATED"
assert set(r["reopen_requires_any"]) == {
    "GLOBAL_RATIONAL_REALIZATION_WITH_HEIGHT_CONTROL",
    "NEW_SOURCE_FIXED_E1_INVARIANT",
    "QUANTITATIVE_HEIGHT_DISCRIMINANT_ADAPTER",
}
assert all(v is False for v in r["credit_firewall"].values())

# The intermediate checkpoint does not replace the mathematical authority.
assert s["schema"] == "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"
assert s["last_audited_authority"]["unit"] == "35EX-35_GOAL4AK_SECOND_CLASS_QI_CYCLIC_EXPLICIT_F_B_ASSEMBLY"
assert s["last_audited_authority"]["hostile_review_id"] == 5142248509
assert s["claims"]["E1_proved"] is False
assert s["claims"]["stage35_closed"] is False
assert s["claims"]["perfect_cuboid_existence_claim"] is False
assert s["claims"]["perfect_cuboid_nonexistence_claim"] is False

for marker in (
    "review: `5151846948`",
    "PARKING_AUDIT_COMPLETE=true",
    "ROUTE_STATUS=PARKED_AUDITED_REOPEN_GATED",
    "GLOBAL_RATIONAL_REALIZATION_WITH_HEIGHT_CONTROL",
    "NEW_SOURCE_FIXED_E1_INVARIANT",
    "QUANTITATIVE_HEIGHT_DISCRIMINANT_ADAPTER",
    "No merge.",
):
    assert marker in h, marker

print("STAGE35_EX_GOAL4BS_INTERMEDIATE_AUDIT_CONSUMPTION=PASS")
print("review_id=5151846948")
print("mathematical_authority=V74/Goal4AK")
print("route_status=PARKED_AUDITED_REOPEN_GATED")
print("E1_credit=false")
