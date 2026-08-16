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
assert ctrl["backflow"]["post_checkpoint50_global_delta"] is False
assert ctrl["backflow"]["envelope_synchronized"] is True
assert ctrl["backflow"]["interaction_classification_synchronized"] is True

if ctrl["audit_status"] == "PENDING":
    assert ctrl["checkpoint60_deep_stop_rule_satisfied"] is False
    assert ctrl["deep_stop_pending_hostile_audit"] is True
    assert ctrl["checkpoint60_closed"] is False
    assert ctrl["stage70_allowed"] is False
    assert ctrl["advance_allowed"] is False
    assert ctrl["next_checkpoint"] == 60
    assert ctrl["merge_allowed"] is False
elif ctrl["audit_status"] == "PASS":
    assert ctrl["checkpoint60_deep_stop_rule_satisfied"] is True
    assert ctrl["deep_stop_pending_hostile_audit"] is False
    assert ctrl["checkpoint60_closed"] is True
    assert ctrl["stage70_allowed"] is True
    assert ctrl["advance_allowed"] is True
    assert ctrl["next_checkpoint"] == 70
    assert ctrl["merge_allowed"] is True
else:
    raise AssertionError(ctrl["audit_status"])

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
for marker in [
    "R505_EXACT_TARGET_RECEIVER_ACCEPTED=true",
    "R506_TORIC_SUBSUMPTION_ACCEPTED=true",
    "R505_MATHEMATICS_REOPEN_REQUIRED=false",
    "R506_MATHEMATICS_REOPEN_REQUIRED=false",
    "REPO_REUSE_HANDOFF_COMPLETE=true",
    "DISCOVERY_EVIDENCE_BLOCK_COMPLETE=true",
]: require(r5056, marker)

stage23 = read("stages/stage23/post-stage25-r01/result.md")
for marker in [
    "RATIO_LOWER=N2/N1>>B^(-3/4)(log B)^(-3)",
    "SECOND_ORDER_INTERACTION_SIGN=POSITIVE_DIVERGENT",
    "TARGET_POSITIVE_POWER_EXPONENT=1/4",
]: require(stage23, marker)

stage24 = read("stages/stage24/post-stage25-r01/result.md")
for marker in [
    "CURRENT_TARGET_LOWER=N2(B)>>B^(1/4)",
    "CURRENT_SURVIVOR_RATIO_LOWER=N2/M2>>B^(-3/4)(log B)^(-5)",
    "STAGE24_GLOBAL_INTERACTION_SIGN=POSITIVE_DIVERGENT",
    "SECOND_ORDER_INTERACTION_SIGN=POSITIVE_DIVERGENT",
]: require(stage24, marker)

policy = read("stages/stage25/25-60/continuation-policy.md")
require(policy, "remaining open items require genuinely new external mathematics")
require(policy, "no repo-native attack compatible with the Stage14/15 deep-review reopen conditions remains live")

# Lifecycle-aware no-bypass check. Checkpoint60 itself remains immutable; later
# reentry is legal only after checkpoint70 audit/merge and the audited closeout.
reentry = json.loads(read("stages/stage25/25-reentry-controller.json"))
assert reentry["starts_after"]["stage25_checkpoint"] == 70
assert reentry["starts_after"]["audit_verdict"] == "PASS"
assert reentry["starts_after"]["closeout_merged"] is True
if reentry["status"] == "BLOCKED_UNTIL_STAGE25_AUDITED_CLOSEOUT":
    assert reentry["current_phase"] is None
else:
    assert reentry["unlock_evidence"]["checkpoint70_audit_verdict"] == "PASS"
    assert reentry["unlock_evidence"]["closeout_pr"] == 1000
    assert reentry["unlock_evidence"]["closeout_merge_commit"] == "12e1cb027e3123328702393ebdb3e3687ca0a169"
    assert reentry["unlock_evidence"]["main_stage25_closed"] is True
    assert reentry["stage26_gate"]["stage25_main_closed"] is True
    assert reentry["current_phase"] in (10, 20, 30, 40, 50, 60, 70)
    if reentry["current_phase"] > 10:
        p10 = reentry["phase10_submission"]
        assert reentry["phases"]["10"]["status"] == "AUDITED_PASS_MERGED"
        assert p10["audit_status"] == "PASS"
        assert p10["pr"] == 1002
        assert p10["merge_commit"] == "5cb7dc8792faf575c1e21fce8166f094af6d7b14"

sync = read("stages/stage25/25-60/checkpoint60-deep-stop-sync.md")
require(sync, "CHECKPOINT60_DEEP_STOP_RULE_CANDIDATE=true")
require(sync, "BACKFLOW_SYNC_CHECK=PASS_NO_DELTA_AFTER_CHECKPOINT50")
require(sync, "NEXT_EXPECTED_COMMAND=Stage25-audit")

print("STAGE25_60_ROUTE_STATUS_SYNC=PASS")
print("STAGE25_60_BACKFLOW_SYNC=PASS_NO_DELTA_AFTER_CHECKPOINT50")
print("STAGE25_60_REENTRY_BYPASS_CHECK=PASS")
print(f"CHECKPOINT60_DEEP_STOP_RULE_SATISFIED={str(ctrl['checkpoint60_deep_stop_rule_satisfied']).lower()}")
print(f"STAGE70_ALLOWED={str(ctrl['stage70_allowed']).lower()}")
