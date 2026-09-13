#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage36/MAIN-STATE.json"
RECEIPT = ROOT / "stages/stage36/36-09FE/current-main-integration.json"
OLD_CONSUMPTION = ROOT / "stages/stage36/36-09FE/current-main-hostile-audit-pass-consumption.json"
FE_CERT = ROOT / "stages/stage36/36-09FE/rho-forced-crt-factor-shape-realization-preflight.json"
FE_SOURCE = ROOT / "stages/stage36/36-09FE/rho-forced-crt-factor-shape-realization-source-lock.md"
FE_VERIFY = ROOT / "stages/stage36/verify_stage36_36_09FE.py"

CURRENT_MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"
OLD_MAIN = "3d6776d6a484093b77b20cf13e4c1833622466d4"
OLD_AUDIT_HEAD = "33bf92c13bc37862c5337564af399156826a8706"
OLD_AUDIT_REVIEW = 5175426557
EXPECTED = {
    FE_CERT: "56a30188f0e09e6a54ad5b395ac8aea3f4274b0b",
    FE_SOURCE: "bf002a79950da8e9c0387df638ff05a519bdd9fe",
    FE_VERIFY: "b83dfaf85c53d0a291d710bbdbc604a07f1828a1",
    OLD_CONSUMPTION: "1a9cfbbb134afa2f822dc9ef0f29bd3fc59f8560",
}

def blob(path):
    return subprocess.check_output(["git", "hash-object", str(path.relative_to(ROOT))], cwd=ROOT, text=True).strip()

for path, expected in EXPECTED.items():
    actual = blob(path)
    assert actual == expected, (path, actual, expected)

s = json.loads(STATE.read_text())
r = json.loads(RECEIPT.read_text())
c = json.loads(OLD_CONSUMPTION.read_text())
fe = json.loads(FE_CERT.read_text())

assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V296R3_36_09FE_CURRENT_MAIN_REAUDIT_FROZEN"
assert s["status"] == "HOSTILE_AUDIT_FREEZE"
assert s["base_main_sha"] == CURRENT_MAIN
assert s["authority_frontier"]["36-09FE"]["certificate_blob_sha"] == EXPECTED[FE_CERT]
assert s["authority_frontier"]["36-09FE"]["source_blob_sha"] == EXPECTED[FE_SOURCE]
assert s["authority_frontier"]["36-09FE"]["verifier_blob_sha"] == EXPECTED[FE_VERIFY]
assert s["authority_frontier"]["36-09FE"]["historical_current_main_hostile_audit_review_id"] == OLD_AUDIT_REVIEW
assert s["authority_frontier"]["36-09FE"]["historical_current_main_hostile_audit_exact_head"] == OLD_AUDIT_HEAD
assert s["freshness"]["current_main"] == CURRENT_MAIN
assert s["freshness"]["previous_audited_integration_parent_main"] == OLD_MAIN
assert s["freshness"]["current_main_integration_reaudit_required"] is True
assert s["hostile_audit_checkpoint"]["previous_result"] == "PASS_CONSUMED"
assert s["hostile_audit_checkpoint"]["previous_review_id"] == OLD_AUDIT_REVIEW
assert s["hostile_audit_checkpoint"]["audited_exact_head"] == OLD_AUDIT_HEAD
assert s["hostile_audit_checkpoint"]["new_checkpoint_pending"] is True
assert s["hostile_audit_checkpoint"]["pending_scope"] == "CURRENT_MAIN_INTEGRATION_FRESHNESS_AT_36_09FE"
assert s["current"]["unit"] == "36-09FE"
assert s["current"]["substantive_batch_pr_continues"] is False
assert s["current"]["36_09FF_entry_allowed"] is False
assert s["promotion_gates"]["historical_post_ER_fresh_hostile_audit_pass_consumed"] is True
assert s["promotion_gates"]["current_main_fresh_hostile_audit_pass_consumed"] is False
assert s["promotion_gates"]["36_09FF_entry_allowed"] is False
for key in ("candidate_parameter_set_shrunk","receiver_emptiness_proved","R29_CAMP2_closed","Q11_CAMPEDELLI_closed","endpoint_closed","perfect_cuboid_nonexistence_claim"):
    assert s["claims"][key] is False

assert r["schema"] == "STAGE36_V296R3_FE_CURRENT_MAIN_DRIFT_REAUDIT_PENDING_V1"
assert r["source_pr"] == 1788
assert r["previous_current_main_integration"]["parent_main_sha"] == OLD_MAIN
assert r["previous_current_main_integration"]["fresh_hostile_audit_review_id"] == OLD_AUDIT_REVIEW
assert r["previous_current_main_integration"]["fresh_hostile_audit_exact_head"] == OLD_AUDIT_HEAD
assert r["previous_current_main_integration"]["pass_consumption_blob_sha1"] == EXPECTED[OLD_CONSUMPTION]
assert r["current_main_integration"]["parent_main_sha"] == CURRENT_MAIN
assert r["current_main_integration"]["post_ER_scope_requires_fresh_hostile_audit"] is True
assert r["current_main_integration"]["current_integration_hostile_audit_pass"] is False
assert r["current_main_integration"]["current_integration_hostile_audit_pass_consumed"] is False
assert r["current_main_integration"]["hostile_audit_pending"] is True
assert r["current_main_integration"]["merge_authorized"] is False
assert r["latest_checkpoint"]["next_leaf_entry_allowed"] is False
assert r["credit_ceiling"] == "AUDIT_PENDING_STAGE36_V296_FE_FINITE_COMPATIBILITY_NO_RECEIVER_OR_ENDPOINT_CREDIT"
assert all(v is False for k,v in r["claims"].items() if k != "FE_both_seed17_branches_factor_shape_realized_proved")

assert c["hostile_audit_result"] == "PASS"
assert c["audited_exact_head"] == OLD_AUDIT_HEAD
assert c["hostile_audit_review_id"] == OLD_AUDIT_REVIEW
assert c["current_main_at_audit"] == OLD_MAIN
assert c["current_main_at_consumption"] == OLD_MAIN
assert c["main_drift_since_audit"] is False

assert fe["finite_compatibility_theorem"]["both_seed17_branches_nonempty_in_exact_FB_factor_shape"] is True
assert fe["finite_compatibility_theorem"]["unbounded_realization_proved"] is False
assert fe["finite_compatibility_theorem"]["infinitely_many_realizations_proved"] is False
assert fe["registry_impact"]["provisional_count"] == 224
assert fe["route_result"]["next_leaf"] == "36-09FF_RHO_FORCED_CRT_FACTOR_SHAPE_UNBOUNDED_CONTROL_PREFLIGHT"

print("STAGE36_V296R3_CURRENT_MAIN_REAUDIT_FREEZE=PASS")
print(f"current_main={CURRENT_MAIN}")
print(f"historical_hostile_audit_review_id={OLD_AUDIT_REVIEW}")
print("fresh_current_main_hostile_audit_pending=true")
print("36_09FF_entry_allowed=false")
print("credit_ceiling=AUDIT_PENDING_STAGE36_V296_FE_FINITE_COMPATIBILITY_NO_RECEIVER_OR_ENDPOINT_CREDIT")
