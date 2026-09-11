#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage36/MAIN-STATE.json"
RECEIPT = ROOT / "stages/stage36/36-09FE/current-main-integration.json"
CONSUMPTION = ROOT / "stages/stage36/36-09FE/current-main-hostile-audit-pass-consumption.json"
FE_CERT = ROOT / "stages/stage36/36-09FE/rho-forced-crt-factor-shape-realization-preflight.json"
FE_SOURCE = ROOT / "stages/stage36/36-09FE/rho-forced-crt-factor-shape-realization-source-lock.md"
FE_VERIFY = ROOT / "stages/stage36/verify_stage36_36_09FE.py"

EXPECTED = {
    FE_CERT: "56a30188f0e09e6a54ad5b395ac8aea3f4274b0b",
    FE_SOURCE: "bf002a79950da8e9c0387df638ff05a519bdd9fe",
    FE_VERIFY: "b83dfaf85c53d0a291d710bbdbc604a07f1828a1",
}
AUDITED_HEAD = "33bf92c13bc37862c5337564af399156826a8706"
AUDIT_REVIEW = 5175426557
CURRENT_MAIN = "3d6776d6a484093b77b20cf13e4c1833622466d4"

def blob(path):
    return subprocess.check_output(["git", "hash-object", str(path.relative_to(ROOT))], cwd=ROOT, text=True).strip()

for path, expected in EXPECTED.items():
    actual = blob(path)
    assert actual == expected, (path, actual, expected)

s = json.loads(STATE.read_text())
r = json.loads(RECEIPT.read_text())
c = json.loads(CONSUMPTION.read_text())
fe = json.loads(FE_CERT.read_text())

assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V296R2_36_09FE_AUDIT_PASS_CONSUMED_FF_UNLOCKED"
assert s["status"] == "EXACT_GREEN_CONTINUE"
assert s["base_main_sha"] == CURRENT_MAIN
assert s["authority_frontier"]["36-09FE"]["certificate_blob_sha"] == EXPECTED[FE_CERT]
assert s["authority_frontier"]["36-09FE"]["source_blob_sha"] == EXPECTED[FE_SOURCE]
assert s["authority_frontier"]["36-09FE"]["verifier_blob_sha"] == EXPECTED[FE_VERIFY]
assert s["authority_frontier"]["36-09FE"]["current_main_hostile_audit_review_id"] == AUDIT_REVIEW
assert s["authority_frontier"]["36-09FE"]["current_main_hostile_audit_exact_head"] == AUDITED_HEAD
assert s["claims"]["FE_both_seed17_branches_factor_shape_realized_proved"] is True
assert s["claims"]["candidate_parameter_set_shrunk"] is False
assert s["claims"]["receiver_emptiness_proved"] is False
assert s["claims"]["R29_CAMP2_closed"] is False
assert s["claims"]["Q11_CAMPEDELLI_closed"] is False
assert s["claims"]["endpoint_closed"] is False
assert s["claims"]["perfect_cuboid_nonexistence_claim"] is False
assert s["freshness"]["current_main"] == CURRENT_MAIN
assert s["hostile_audit_checkpoint"]["previous_result"] == "PASS_CONSUMED"
assert s["hostile_audit_checkpoint"]["previous_review_id"] == AUDIT_REVIEW
assert s["hostile_audit_checkpoint"]["audited_exact_head"] == AUDITED_HEAD
assert s["hostile_audit_checkpoint"]["new_checkpoint_pending"] is False
assert s["hostile_audit_checkpoint"]["pass_consumption_receipt"] == "stages/stage36/36-09FE/current-main-hostile-audit-pass-consumption.json"
assert s["current"]["unit"] == "36-09FF"
assert s["current"]["next_exact_leaf"] == "36-09FF_RHO_FORCED_CRT_FACTOR_SHAPE_UNBOUNDED_CONTROL_PREFLIGHT"
assert s["current"]["substantive_batch_pr_continues"] is True
assert s["current"]["36_09FF_entry_allowed"] is True
assert s["promotion_gates"]["post_ER_fresh_hostile_audit_pass_consumed"] is True
assert s["promotion_gates"]["36_09FF_entry_allowed"] is True

assert r["schema"] == "STAGE36_V296R2_FE_CURRENT_MAIN_INTEGRATION_AUDIT_PASS_CONSUMED_V1"
assert r["source_pr"] == 1752
assert r["historical_source"]["final_stacked_head"] == "ca3646e5a7073b6a750a5a5470392672f189c6fc"
assert r["historical_source"]["stage36_tree_sha"] == "a3a9e3b52696c1b1061353d2c396d10da9abf5ec"
assert r["historical_source"]["last_hostile_pass_review_id"] == 5154394408
assert r["historical_source"]["last_hostile_pass_exact_head"] == "074bdffe73692b8048bc08999dd50e4d025de012"
assert r["historical_source"]["last_hostile_pass_scope_end"] == "36-09ER"
assert r["current_main_integration"]["parent_main_sha"] == CURRENT_MAIN
assert r["current_main_integration"]["post_ER_scope_requires_fresh_hostile_audit"] is True
assert r["current_main_integration"]["fresh_hostile_audit_review_id"] == AUDIT_REVIEW
assert r["current_main_integration"]["fresh_hostile_audit_exact_head"] == AUDITED_HEAD
assert r["current_main_integration"]["current_integration_hostile_audit_pass"] is True
assert r["current_main_integration"]["current_integration_hostile_audit_pass_consumed"] is True
assert r["current_main_integration"]["merge_authorized"] is False
assert r["latest_checkpoint"]["leaf"] == "36-09FE"
assert r["latest_checkpoint"]["next_leaf"] == "36-09FF_RHO_FORCED_CRT_FACTOR_SHAPE_UNBOUNDED_CONTROL_PREFLIGHT"
assert r["latest_checkpoint"]["next_leaf_entry_allowed"] is True
assert r["latest_checkpoint"]["fixed_parameter_exclusion_registry_count"] == 224
assert r["credit_ceiling"] == "AUDITED_STAGE36_V296_FE_FINITE_COMPATIBILITY_NO_RECEIVER_OR_ENDPOINT_CREDIT"
assert all(v is False for k,v in r["claims"].items() if k != "FE_both_seed17_branches_factor_shape_realized_proved")

assert c["schema"] == "STAGE36_36_09FE_CURRENT_MAIN_HOSTILE_AUDIT_PASS_CONSUMPTION_V1"
assert c["audit_pr"] == 1752
assert c["audited_scope"] == "36-09ES_THROUGH_36-09FE"
assert c["audited_exact_head"] == AUDITED_HEAD
assert c["hostile_audit_review_id"] == AUDIT_REVIEW
assert c["hostile_audit_result"] == "PASS"
assert c["exact_head_ci"]["stage36_authority"] == "34567819581/103163437258"
assert c["exact_head_ci"]["repo_wide_integrity"] == "34567819587/103163437305"
assert c["current_main_at_audit"] == CURRENT_MAIN
assert c["current_main_at_consumption"] == CURRENT_MAIN
assert c["main_drift_since_audit"] is False
assert c["consumption_result"]["current_integration_hostile_audit_pass"] is True
assert c["consumption_result"]["current_integration_hostile_audit_pass_consumed"] is True
assert c["consumption_result"]["36_09FF_entry_allowed"] is True
assert c["credit_ceiling"]["merge_authorized"] is False
assert all(v is False for k,v in c["credit_ceiling"].items() if k != "merge_authorized")

assert fe["finite_compatibility_theorem"]["both_seed17_branches_nonempty_in_exact_FB_factor_shape"] is True
assert fe["finite_compatibility_theorem"]["unbounded_realization_proved"] is False
assert fe["finite_compatibility_theorem"]["infinitely_many_realizations_proved"] is False
assert fe["registry_impact"]["provisional_count"] == 224
assert fe["route_result"]["next_leaf"] == "36-09FF_RHO_FORCED_CRT_FACTOR_SHAPE_UNBOUNDED_CONTROL_PREFLIGHT"

print("STAGE36_V296R2_FE_CURRENT_MAIN_AUDIT_PASS_CONSUMED=PASS")
print("fresh_hostile_audit_review_id=5175426557")
print("audited_exact_head=33bf92c13bc37862c5337564af399156826a8706")
print("36_09FF_entry_allowed=true")
print("credit_ceiling=AUDITED_STAGE36_V296_FE_FINITE_COMPATIBILITY_NO_RECEIVER_OR_ENDPOINT_CREDIT")
