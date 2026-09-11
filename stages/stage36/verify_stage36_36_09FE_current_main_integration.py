#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage36/MAIN-STATE.json"
RECEIPT = ROOT / "stages/stage36/36-09FE/current-main-integration.json"
FE_CERT = ROOT / "stages/stage36/36-09FE/rho-forced-crt-factor-shape-realization-preflight.json"
FE_SOURCE = ROOT / "stages/stage36/36-09FE/rho-forced-crt-factor-shape-realization-source-lock.md"
FE_VERIFY = ROOT / "stages/stage36/verify_stage36_36_09FE.py"

EXPECTED = {
    FE_CERT: "56a30188f0e09e6a54ad5b395ac8aea3f4274b0b",
    FE_SOURCE: "bf002a79950da8e9c0387df638ff05a519bdd9fe",
    FE_VERIFY: "b83dfaf85c53d0a291d710bbdbc604a07f1828a1",
}

def blob(path):
    return subprocess.check_output(["git", "hash-object", str(path.relative_to(ROOT))], cwd=ROOT, text=True).strip()

for path, expected in EXPECTED.items():
    actual = blob(path)
    assert actual == expected, (path, actual, expected)

s = json.loads(STATE.read_text())
r = json.loads(RECEIPT.read_text())
fe = json.loads(FE_CERT.read_text())

assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V296_36_09FE_EXACT_GREEN_FF_UNLOCKED"
assert s["authority_frontier"]["36-09FE"]["certificate_blob_sha"] == EXPECTED[FE_CERT]
assert s["authority_frontier"]["36-09FE"]["source_blob_sha"] == EXPECTED[FE_SOURCE]
assert s["authority_frontier"]["36-09FE"]["verifier_blob_sha"] == EXPECTED[FE_VERIFY]
assert s["claims"]["FE_both_seed17_branches_factor_shape_realized_proved"] is True
assert s["claims"]["candidate_parameter_set_shrunk"] is False
assert s["claims"]["receiver_emptiness_proved"] is False
assert s["claims"]["R29_CAMP2_closed"] is False
assert s["claims"]["Q11_CAMPEDELLI_closed"] is False
assert s["claims"]["endpoint_closed"] is False
assert s["claims"]["perfect_cuboid_nonexistence_claim"] is False

assert r["schema"] == "STAGE36_V296_FE_CURRENT_MAIN_INTEGRATION_V1"
assert r["source_pr"] == 1752
assert r["historical_source"]["final_stacked_head"] == "ca3646e5a7073b6a750a5a5470392672f189c6fc"
assert r["historical_source"]["stage36_tree_sha"] == "a3a9e3b52696c1b1061353d2c396d10da9abf5ec"
assert r["historical_source"]["last_hostile_pass_review_id"] == 5154394408
assert r["historical_source"]["last_hostile_pass_exact_head"] == "074bdffe73692b8048bc08999dd50e4d025de012"
assert r["historical_source"]["last_hostile_pass_scope_end"] == "36-09ER"
assert r["current_main_integration"]["parent_main_sha"] == "3d6776d6a484093b77b20cf13e4c1833622466d4"
assert r["current_main_integration"]["post_ER_scope_requires_fresh_hostile_audit"] is True
assert r["current_main_integration"]["current_integration_hostile_audit_pass"] is False
assert r["current_main_integration"]["merge_authorized"] is False
assert r["latest_checkpoint"]["leaf"] == "36-09FE"
assert r["latest_checkpoint"]["next_leaf"] == "36-09FF_RHO_FORCED_CRT_FACTOR_SHAPE_UNBOUNDED_CONTROL_PREFLIGHT"
assert r["latest_checkpoint"]["fixed_parameter_exclusion_registry_count"] == 224
assert all(v is False for k,v in r["claims"].items() if k != "FE_both_seed17_branches_factor_shape_realized_proved")

assert fe["finite_compatibility_theorem"]["both_seed17_branches_nonempty_in_exact_FB_factor_shape"] is True
assert fe["finite_compatibility_theorem"]["unbounded_realization_proved"] is False
assert fe["finite_compatibility_theorem"]["infinitely_many_realizations_proved"] is False
assert fe["registry_impact"]["provisional_count"] == 224
assert fe["route_result"]["next_leaf"] == "36-09FF_RHO_FORCED_CRT_FACTOR_SHAPE_UNBOUNDED_CONTROL_PREFLIGHT"

print("STAGE36_V296_FE_CURRENT_MAIN_INTEGRATION=PASS")
print("prior_hostile_pass_scope=through_36-09ER")
print("fresh_hostile_audit_required_for_ES_through_FE=true")
print("credit_ceiling=AUDIT_PENDING_STAGE36_V296_FE_FINITE_COMPATIBILITY_NO_RECEIVER_OR_ENDPOINT_CREDIT")
