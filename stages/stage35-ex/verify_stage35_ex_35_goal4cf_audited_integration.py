#!/usr/bin/env python3
"""Verify audited Goal4CF consumption on the current-main V74 authority line."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "stages" / "stage35-ex" / "35ex-35"
STATE = ROOT / "stages" / "stage35-ex" / "MAIN-STATE.json"
HANDOFF = ROOT / "stages" / "stage35-ex" / "MAIN-BATCH-HANDOFF.md"
RECEIPT = BASE / "goal4cf-hostile-audit-pass-consumption.json"
LEDGER = BASE / "goal4cf-research-route-ledger.md"
SOURCE = BASE / "goal4cf-selected-direction-minimal-discriminant-height-source-lock.md"
CERT = BASE / "goal4cf-selected-direction-minimal-discriminant-height.json"
HISTORICAL_VERIFIER = ROOT / "stages" / "stage35-ex" / "verify_stage35_ex_35_goal4cf_selected_discriminant_height.py"

V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"
EXPECTED = {
    SOURCE: "a94e98e560793cf91548a67bd37989915de00e7a",
    CERT: "60fae382dd97ab6a905b1678681f829b59595e56",
    HISTORICAL_VERIFIER: "e0f623087b8814f9d7ab7f8ced6d7d71f5de0033",
}
EXPECTED_SOURCE_LF = "5e3dc56dc751795095f142765e0b4d4dd31e95c7f9a348a5176ea17f3e9cb88b"
EXPECTED_CERT_CANONICAL = "46207a23fc54745851db52e9090fe147772dfb22eff49875d01d42d3fab9667d"


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


for path, expected in EXPECTED.items():
    actual = git_blob(path)
    assert actual == expected, (path, actual, expected)

assert lf_sha256(SOURCE) == EXPECTED_SOURCE_LF

state = json.loads(STATE.read_text(encoding="utf-8"))
assert state["schema"] == V74
assert state["last_audited_authority"]["unit"] == "35EX-35_GOAL4AK_SECOND_CLASS_QI_CYCLIC_EXPLICIT_F_B_ASSEMBLY"
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False
assert state["claims"]["perfect_cuboid_existence_claim"] is False
assert state["claims"]["perfect_cuboid_nonexistence_claim"] is False

receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
assert receipt["schema"] == "STAGE35_EX_GOAL4CF_HOSTILE_AUDIT_PASS_CONSUMPTION_V1"
assert receipt["source_pr"] == 1766
assert receipt["source_audit"]["result"] == "PASS"
assert receipt["source_audit"]["mathematical_pass_review_id"] == 5164213568
assert receipt["source_audit"]["mathematical_pass_exact_head"] == "2ffe07f31d56caf78261d032b7e5a78d500dd146"
assert receipt["source_audit"]["lifecycle_repair_pass_review_id"] == 5174608648
assert receipt["source_audit"]["lifecycle_repair_exact_head"] == "a059c12ecd298258fa59feac653eb750d7143767"
assert receipt["source_audit"]["no_drift_revalidation_review_id"] == 5174722371
assert receipt["exact_head_ci"]["aggregate_run"] == 34556563263
assert receipt["exact_head_ci"]["goal4cf_dedicated_run"] == 34556563288
assert receipt["current_main_integration"]["parent_main_sha"] == "9ce9abcde2880d6de10dd7f408feb18fb9fab630"
assert receipt["current_main_integration"]["formal_authority_schema"] == V74
assert receipt["current_main_integration"]["formal_authority_review_id"] == 5142248509
assert receipt["current_main_integration"]["source_goal4cf_hostile_audit_pass"] is True
assert receipt["current_main_integration"]["current_integration_hostile_audit_pass"] is False
assert receipt["current_main_integration"]["merge_authorized"] is False
assert receipt["credit_ceiling"] == "AUDITED_SELECTED_DIRECTION_QUANTITATIVE_DISCRIMINANT_HEIGHT_ADAPTER_NO_E1_CREDIT"
assert receipt["result"]["selected_direction_endpoint_bound"] == "12288*abs(Delta_min(E_*))>=W^10"
assert all(v is False for v in receipt["claims"].values())

cert = json.loads(CERT.read_text(encoding="utf-8"))
assert cert["schema"] == "STAGE35_EX_GOAL4CF_SELECTED_DISCRIMINANT_HEIGHT_V1"
assert cert["canonical_sha256"] == EXPECTED_CERT_CANONICAL
assert canonical_sha(cert) == EXPECTED_CERT_CANONICAL
assert cert["result"]["endpoint_bound"] == "12288*abs(Delta_min(E_*))>=W^10"
assert cert["result"]["exact_minimal_discriminant"] == "(r*s*t)^4/256"
assert cert["result"]["new_selected_direction_height_adapter"] is True

ledger = LEDGER.read_text(encoding="utf-8")
for marker in (
    "HISTORICAL_SOURCE_PR=1766",
    "HISTORICAL_FINAL_HEAD=a059c12ecd298258fa59feac653eb750d7143767",
    "HISTORICAL_SOURCE_MERGEABLE_TO_MAIN=false",
    "CURRENT_INTEGRATION_PR=1773",
    "FORMAL_AUTHORITY=V74/Goal4AK",
    "CREDIT_CEILING=AUDITED_SELECTED_DIRECTION_QUANTITATIVE_DISCRIMINANT_HEIGHT_ADAPTER_NO_E1_CREDIT",
    "Goal4AT — marked residual Kummer local support",
    "Goal4AU — three-direction Kummer gcd allocation",
    "Goal4BD — simultaneous three-marked rank-jump receiver",
    "Goal4AW — marked elliptic height comparison",
    "Goal4AZ — amplification / stronger counting",
    "Goal4BS — first parking boundary",
    "Goal4BT→Goal4CE reopen — canonical gcd/local completion",
    "ALL_SOURCE_SELECTED_E1_COMMON_GCD_LOCAL_FAMILIES_COMPLETE=true",
    "CURRENT_AMPLIFIERS_BEAT_SQRT_COUNTING=false",
    "SELECTED_PHYSICAL_MARKED_LOCAL_HEIGHT_COMPARISON_PREFLIGHT",
):
    assert marker in ledger, marker

handoff = HANDOFF.read_text(encoding="utf-8")
for marker in (
    "Goal4CF",
    "review `5174608648`",
    "a059c12ecd298258fa59feac653eb750d7143767",
    "goal4cf-research-route-ledger.md",
    "AUDITED_SELECTED_DIRECTION_QUANTITATIVE_DISCRIMINANT_HEIGHT_ADAPTER_NO_E1_CREDIT",
    "SELECTED_PHYSICAL_MARKED_LOCAL_HEIGHT_COMPARISON_PREFLIGHT",
    "Formal authority remains **V74 / Goal4AK**",
):
    assert marker in handoff, marker

print("STAGE35_EX_GOAL4CF_AUDITED_CURRENT_MAIN_INTEGRATION=PASS")
print("source_goal4cf_hostile_audit_pass=true")
print("research_route_provenance_ledger=present")
print("formal_authority=V74/Goal4AK")
print("credit_ceiling=AUDITED_SELECTED_DIRECTION_QUANTITATIVE_DISCRIMINANT_HEIGHT_ADAPTER_NO_E1_CREDIT")
print("current_integration_hostile_audit_pass=false")
print("merge_authorized=false")
