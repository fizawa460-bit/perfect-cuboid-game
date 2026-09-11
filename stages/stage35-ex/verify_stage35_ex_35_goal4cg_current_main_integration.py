#!/usr/bin/env python3
"""Verify Goal4CG current-main integration without importing the historical Stage35EX file forest."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "stages" / "stage35-ex" / "35ex-35"
STATE = ROOT / "stages" / "stage35-ex" / "MAIN-STATE.json"
HANDOFF = ROOT / "stages" / "stage35-ex" / "MAIN-BATCH-HANDOFF.md"
CF_RECEIPT = BASE / "goal4cf-hostile-audit-pass-consumption.json"
CG_RECEIPT = BASE / "goal4cg-current-main-integration.json"
SOURCE = BASE / "goal4cg-selected-physical-marked-local-height-comparison-source-lock.md"
CERT = BASE / "goal4cg-selected-physical-marked-local-height-comparison.json"
HISTORICAL_VERIFIER = ROOT / "stages" / "stage35-ex" / "verify_stage35_ex_35_goal4cg_selected_marked_height.py"

V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"
EXPECTED_BLOBS = {
    SOURCE: "c47e5c9a9faac08949f451e306c700102831dcb8",
    CERT: "473fe8a39596cb5741fc8709b22cd22590a0f67c",
    HISTORICAL_VERIFIER: "1c753fc01a99efdd88e991fef15347c899d3dc37",
}
EXPECTED_SOURCE_LF = "8528b2b818dd505c277372dd44a313e60399e7361503d753376d2899a7010e44"
EXPECTED_CERT_CANONICAL = "d7eb73b45871c66e2c0ded5c566ae2c6f5e914483419d31823ab2f99e6ad13de"
EXPECTED_SOURCE_HEAD = "67fa8115211119cb667caacabde7d52133507f6f"
EXPECTED_PARENT_MAIN = "9a05bdbe2dbb1ba50ef68425c80f5c289260f5da"


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()


def lf_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    raw = text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def canonical_sha(obj: dict) -> str:
    payload = dict(obj)
    payload.pop("canonical_sha256", None)
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


for path, expected in EXPECTED_BLOBS.items():
    assert git_blob(path) == expected, (path, git_blob(path), expected)

assert lf_sha256(SOURCE) == EXPECTED_SOURCE_LF

state = json.loads(STATE.read_text(encoding="utf-8"))
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False
assert state["claims"]["perfect_cuboid_existence_claim"] is False
assert state["claims"]["perfect_cuboid_nonexistence_claim"] is False

cf = json.loads(CF_RECEIPT.read_text(encoding="utf-8"))
assert cf["schema"] == "STAGE35_EX_GOAL4CF_HOSTILE_AUDIT_PASS_CONSUMPTION_V1"
assert cf["source_audit"]["result"] == "PASS"
assert cf["result"]["selected_direction_endpoint_bound"] == "12288*abs(Delta_min(E_*))>=W^10"

receipt = json.loads(CG_RECEIPT.read_text(encoding="utf-8"))
assert receipt["schema"] == "STAGE35_EX_GOAL4CG_CURRENT_MAIN_INTEGRATION_V1"
assert receipt["source_pr"] == 1771
assert receipt["source_checkpoint"]["exact_head"] == EXPECTED_SOURCE_HEAD
assert receipt["source_checkpoint"]["dedicated_ci_run"] == 34555204989
assert receipt["source_checkpoint"]["dedicated_ci_job"] == 103126305682
assert receipt["source_checkpoint"]["hostile_audit_pass"] is False
assert receipt["current_main_integration"]["parent_main_sha"] == EXPECTED_PARENT_MAIN
assert receipt["current_main_integration"]["formal_authority_schema"] == V74
assert receipt["current_main_integration"]["goal4cf_current_main_integrated"] is True
assert receipt["current_main_integration"]["current_integration_hostile_audit_pass"] is False
assert receipt["current_main_integration"]["merge_authorized"] is False
assert all(v is False for v in receipt["claims"].values())

cert = json.loads(CERT.read_text(encoding="utf-8"))
assert cert["schema"] == "STAGE35_EX_GOAL4CG_SELECTED_MARKED_HEIGHT_V1"
assert cert["status"] == "PROVISIONAL_EXACT_EXPLICIT_UPPER_AND_PETSCHE_BLOCKER_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT"
assert cert["canonical_sha256"] == EXPECTED_CERT_CANONICAL
assert canonical_sha(cert) == EXPECTED_CERT_CANONICAL
assert cert["height_upper"]["naive_x"] == "h_x(P_*)<=6 log W"
assert cert["height_upper"]["canonical"] == "hhat(P_*)<=17/3 log W"
assert abs(cert["height_upper"]["explicit_upper_coefficient"] - 17 / 3) < 1e-15

pc = cert["petsche_comparison"]
best = 10 / (10**15 * 4**6 * math.log(104613 * 16)**2)
assert abs(pc["best_case_logW_coefficient"] - best) < 1e-35
assert best < 1.19e-20
assert best < 17 / 3
assert pc["strict_coefficient_win"] is False

assert cert["semistable_conductor"]["szpiro_lower"] == "sigma(E_*)>=4"
assert cert["semistable_conductor"]["uniform_szpiro_upper_obtained"] is False
assert cert["local_component_blocker"]["name"] == "UNIFORM_MARKED_BAD_PRIME_COMPONENT_INDEX_CONTROL"
assert cert["result"]["route_status"] == "BLOCKED_EXPLICIT_UPPER_OBTAINED_NO_LOWER_COEFFICIENT_WIN"
assert cert["credit_firewall"]["E1_proved"] is False
assert cert["credit_firewall"]["stage35_closed"] is False

handoff = HANDOFF.read_text(encoding="utf-8")
for marker in (
    "Goal4CG current-main integration",
    "67fa8115211119cb667caacabde7d52133507f6f",
    "h_x(P_*) <= 6 log W",
    "hhat(P_*) <= 17/3 log W",
    "UNIFORM_MARKED_BAD_PRIME_COMPONENT_INDEX_CONTROL",
    "Formal authority remains **V74 / Goal4AK**",
    "No E1, Stage35, endpoint, or Perfect Cuboid credit",
):
    assert marker in handoff, marker

print("STAGE35_EX_GOAL4CG_CURRENT_MAIN_INTEGRATION=PASS")
print("formal_authority=V74/Goal4AK")
print("goal4cf_current_main_integrated=true")
print("goal4cg_source_checkpoint=67fa8115211119cb667caacabde7d52133507f6f")
print("explicit_upper=hhat(P_*)<=17/3 log W")
print("strict_petsche_coefficient_win=false")
print("next=UNIFORM_MARKED_BAD_PRIME_COMPONENT_INDEX_CONTROL_THEN_BREADTH_REOPEN")
print("current_integration_hostile_audit_pass=false")
print("merge_authorized=false")
