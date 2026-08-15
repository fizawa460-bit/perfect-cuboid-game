#!/usr/bin/env python3
from pathlib import Path
import json

root = Path(__file__).resolve().parents[3]
p = root / "stages/stage25/25-60"

def read(rel):
    return (root / rel).read_text(encoding="utf-8")

def require(text, marker):
    assert marker in text, f"missing marker: {marker}"

ctrl = json.loads((p / "checkpoint60-deep-stop-controller.json").read_text(encoding="utf-8"))
assert ctrl["checkpoint60_deep_stop_rule_candidate"] is True
assert ctrl["checkpoint60_deep_stop_rule_satisfied"] is False
assert ctrl["deep_stop_pending_hostile_audit"] is True
assert ctrl["stage70_allowed"] is False
assert ctrl["audit_status"] == "PENDING"
assert ctrl["next_checkpoint"] == 60
assert ctrl["backflow"]["post_checkpoint50_global_delta"] is False
assert ctrl["backflow"]["envelope_synchronized"] is True
assert ctrl["backflow"]["interaction_classification_synchronized"] is True

expected_routes = {
    "R501": "PROVED_AUDITED_Theta_B_QUARTER",
    "R502": "CLOSED_NO_UPGRADE_WITH_CERTIFICATE_AUDITED_PASS",
    "R503": "EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_AUDITED_PASS",
    "R504": "EXTERNAL_THEOREM_GATE_AUDITED_PASS_AFTER_REPO_NATIVE_CLOSURES",
    "R505": "EXTERNAL_THEOREM_GATE_WITH_PREVIOUS_HOSTILE_MATH_ACCEPTED",
    "R506": "CLOSED_NO_INDEPENDENT_ROUTE_WITH_CERTIFICATE_AUDITED_ACCEPTED",
    "R507": "PROVED_AUDITED_R501_PRIMITIVE_HEIGHT_RIGIDITY",
}
assert ctrl["route_status"] == expected_routes

r502 = read("stages/stage25/25-60/audit-recheck.md")
require(r502, "R502_STATUS=CLOSED_NO_UPGRADE_WITH_CERTIFICATE")
require(r502, "R502_EXACT_FAMILY_GROWTH_ACCEPTED=Theta(B^(1/4))")

r503 = read("stages/stage25/25-60/r503-audit.md")
require(r503, "R503_ROUTE_STATUS=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE")
require(r503, "R503_DIRECT_GENERIC_SECTION_ROUTE=CLOSED")

r504 = json.loads(read("stages/stage25/25-60/r504-exceptional-search-controller.json"))
assert r504["full_split_prym_route"] == "EXTERNAL_THEOREM_GATE_AUDITED_PASS"
assert r504["full_split_exceptional_prym_e0_isogeny_locus"] == "OPEN_EXTERNAL"
assert r504["rank_two_growing_lattice_route"] == "CLOSED_NO_QUARTER_UPGRADE_WITH_HEIGHT_CERTIFICATE_AUDITED_PASS"
assert r504["global_stage25_lower_changed"] is False

r5056 = read("stages/stage25/25-60/r505-r506-audit-recheck2.md")
require(r5056, "R505_EXACT_TARGET_RECEIVER_ACCEPTED=true")
require(r5056, "R506_TORIC_SUBSUMPTION_ACCEPTED=true")
require(r5056, "R505_MATHEMATICS_REOPEN_REQUIRED=false")
require(r5056, "R506_MATHEMATICS_REOPEN_REQUIRED=false")
require(r5056, "REPO_REUSE_HANDOFF_COMPLETE=true")
require(r5056, "DISCOVERY_EVIDENCE_BLOCK_COMPLETE=true")

stage23 = read("stages/stage23/post-stage25-r01/result.md")
require(stage23, "RATIO_LOWER=N2/N1>>B^(-3/4)(log B)^(-3)")
require(stage23, "SECOND_ORDER_INTERACTION_SIGN=POSITIVE_DIVERGENT")
require(stage23, "TARGET_POSITIVE_POWER_EXPONENT=1/4")

stage24 = read("stages/stage24/post-stage25-r01/result.md")
require(stage24, "CURRENT_TARGET_LOWER=N2(B)>>B^(1/4)")
require(stage24, "CURRENT_SURVIVOR_RATIO_LOWER=N2/M2>>B^(-3/4)(log B)^(-5)")
require(stage24, "STAGE24_GLOBAL_INTERACTION_SIGN=POSITIVE_DIVERGENT")
require(stage24, "SECOND_ORDER_INTERACTION_SIGN=POSITIVE_DIVERGENT")

policy = read("stages/stage25/25-60/continuation-policy.md")
require(policy, "remaining open items require genuinely new external mathematics")
require(policy, "no repo-native attack compatible with the Stage14/15 deep-review reopen conditions remains live")

reentry = json.loads(read("stages/stage25/25-reentry-controller.json"))
assert reentry["status"] == "BLOCKED_UNTIL_STAGE25_AUDITED_CLOSEOUT"
assert reentry["starts_after"]["stage25_checkpoint"] == 70
assert reentry["starts_after"]["audit_verdict"] == "PASS"
assert reentry["starts_after"]["closeout_merged"] is True

sync = read("stages/stage25/25-60/checkpoint60-deep-stop-sync.md")
require(sync, "CHECKPOINT60_DEEP_STOP_RULE_CANDIDATE=true")
require(sync, "CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false")
require(sync, "BACKFLOW_SYNC_CHECK=PASS_NO_DELTA_AFTER_CHECKPOINT50")
require(sync, "NEXT_EXPECTED_COMMAND=Stage25-audit")

print("STAGE25_60_ROUTE_STATUS_SYNC=PASS")
print("STAGE25_60_BACKFLOW_SYNC=PASS_NO_DELTA_AFTER_CHECKPOINT50")
print("STAGE25_60_REENTRY_BYPASS_CHECK=PASS")
print("CHECKPOINT60_DEEP_STOP_RULE_CANDIDATE=PASS")
print("CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false")
print("STAGE70_ALLOWED=false")
