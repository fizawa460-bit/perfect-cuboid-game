#!/usr/bin/env python3
from pathlib import Path
import json

root = Path(__file__).resolve().parents[3]


def text(rel):
    p = root / rel
    assert p.exists(), f"missing {rel}"
    return p.read_text(encoding="utf-8")


def data(rel):
    return json.loads(text(rel))


r = text("stages/stage25/25-70/result.md")
f = text("stages/stage25/final.md")
m = text("stages/stage25/manifest-r01.md")
a = text("docs/stage25-arsenal-promotion.md")
l = text("stages/stage25/25-70/aggressive-search-ledger.md")
audit70 = text("stages/stage25/25-70/audit.md")
c25 = data("stages/stage25/25-controller.json")
c70 = data("stages/stage25/25-70/controller.json")
c60 = data("stages/stage25/25-60/checkpoint60-deep-stop-controller.json")
reentry = data("stages/stage25/25-reentry-controller.json")

# checkpoint60 authorization
assert c60["checkpoint60_deep_stop_rule_satisfied"] is True
assert c60["checkpoint60_closed"] is True
assert c60["stage70_allowed"] is True
assert c60["audit_status"] == "PASS"
assert c60["next_checkpoint"] == 70

# theorem stack markers
for s in (r, f):
    assert "M_1(B)" in s or "M1(B)" in s
    assert "B^{1/4}" in s or "B^(1/4)" in s
    assert "B^{1/2+\\varepsilon}" in s or "B^(1/2+epsilon)" in s
    assert "THIN_BUT_POSITIVE_POWER_INFINITE" in s
    assert "TRUE_TARGET_EXPONENT_IDENTIFIED=false" in s
    assert "PERFECT_CUBOID_CONCLUSION=NONE" in s

# ratio exponents and causal sign
assert "B^{-7/4}" in r
assert "B^{-3/2+\\varepsilon}" in r
assert "positive divergent interaction" in r.lower()
assert "B^{1/4}(\\log B)^{-7}" in r

# route registry boundary
for marker in (
    "R501=PROVED_AUDITED_THETA_B_QUARTER",
    "R502=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_AUDITED_PASS",
    "R503=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_AUDITED_PASS",
    "R506=CLOSED_NO_INDEPENDENT_ROUTE_WITH_CERTIFICATE_PREVIOUS_MATH_ACCEPTED",
):
    assert marker in r or marker in m
assert "EXTERNAL_THEOREM_GATE" in r and "R504" in r and "R505" in r

# required Stage70 materializations
assert c70["self_contained_bundle_materialized"] is True
assert c70["arsenal_promotion_materialized"] is True
assert c70["aggressive_search_ledger_materialized"] is True
assert "SELF_CONTAINED_BUNDLE_MATERIALIZED=true" in m
assert "ARSENAL_PROMOTION_MATERIALIZED=true" in m
assert "AGGRESSIVE_SEARCH_LEDGER_MATERIALIZED=true" in m
assert "S25-W01" in a and "S25-W04" in a
assert "CLOSEOUT_SUBMISSION_JUSTIFIED=true" in l

# backflow must be current without fabricating a new theorem delta inside the
# original Stage25 main closeout. Later reentry theorems live in their own lane.
assert c70["backflow_status"] == "PASS_NO_DELTA_AFTER_CHECKPOINT50"
assert c70["global_stage25_lower_changed_after_checkpoint50"] is False
assert "BACKFLOW_STATUS=PASS_NO_DELTA_AFTER_CHECKPOINT50" in r

# This verifier is lifecycle-aware. The immutable checkpoint70 contract must
# remain valid before audit, after audit, after merge, and while later reentry
# phases execute. Reentry progression is not a modification of the closed
# checkpoint70 theorem stack.
audit_status = c70["audit_status"]
closeout_merged = bool(c70.get("closeout_merged", False))
reentry_unlocked = bool(c70.get("stage25_reentry_unlocked", False))
assert audit_status in ("PENDING", "PASS")
assert c70["close_stage_after_audit_pass"] is True
assert c70["parent_controller_sync_required_after_audit_pass"] is True
assert reentry["starts_after"]["stage25_checkpoint"] == 70
assert reentry["starts_after"]["audit_verdict"] == "PASS"
assert reentry["starts_after"]["closeout_merged"] is True
assert reentry["stage26_gate"]["stage26_allowed"] is False

if audit_status == "PENDING":
    assert closeout_merged is False
    assert reentry_unlocked is False
    assert c70["advance_allowed"] is False
    assert c70["merge_allowed"] is False
    assert reentry["status"] == "BLOCKED_UNTIL_STAGE25_AUDITED_CLOSEOUT"
    lifecycle = "SUBMISSION_PENDING"
elif not closeout_merged:
    assert reentry_unlocked is False
    assert c70["advance_allowed"] is True
    assert c70["merge_allowed"] is True
    assert c70.get("audit_record") == "stages/stage25/25-70/audit.md"
    assert "AUDIT_VERDICT=PASS" in audit70
    assert reentry["status"] == "BLOCKED_UNTIL_STAGE25_AUDITED_CLOSEOUT"
    lifecycle = "AUDITED_PASS_AWAITING_MERGE"
else:
    assert reentry_unlocked is True
    assert c70["advance_allowed"] is True
    assert c70["merge_allowed"] is True
    assert c70.get("audit_record") == "stages/stage25/25-70/audit.md"
    assert c70.get("closeout_pr") == 1000
    assert c70.get("closeout_merge_commit") == "12e1cb027e3123328702393ebdb3e3687ca0a169"
    assert "AUDIT_VERDICT=PASS" in audit70

    # Canonical parent remains the audited closed Stage25 surface forever after
    # merge, even while reentry research creates new downstream interfaces.
    assert c25["status"] == "CLOSED"
    assert c25["checkpoint_status"]["70"] == "PROVED_AUDITED_PASS"
    assert c25["state"]["CURRENT_CHECKPOINT"] == 70
    assert c25["state"]["MAIN_STATUS"] == "COMPLETE"
    assert c25["state"]["AUDIT_STATUS"] == "PASS"
    assert c25["state"]["NEXT_STAGE"] == "Stage25-reentry"

    assert reentry["unlock_evidence"]["checkpoint70_audit_verdict"] == "PASS"
    assert reentry["unlock_evidence"]["closeout_pr"] == 1000
    assert reentry["unlock_evidence"]["closeout_merge_commit"] == c70["closeout_merge_commit"]
    assert reentry["unlock_evidence"]["main_stage25_closed"] is True
    assert reentry["stage26_gate"]["stage25_main_closed"] is True
    assert reentry["stage26_gate"]["all_reentry_phases_audited"] is False
    assert reentry["stage26_gate"]["stage26_allowed"] is False

    current_phase = reentry["current_phase"]
    assert current_phase in (10, 20, 30, 40, 50, 60, 70)

    if current_phase == 10:
        assert reentry["status"] in (
            "PHASE10_READY_PENDING_SYNC_REAUDIT",
            "PHASE10_READY_AFTER_STAGE25_AUDITED_CLOSEOUT_MERGE",
            "PHASE10_SUBMITTED_PENDING_FRESH_AUDIT",
            "PHASE10_AUDITED_PASS_AWAITING_MERGE",
        )
        lifecycle = "POST_MERGE_REENTRY_PHASE10"
    else:
        # Any later phase is legal only after phase10 was actually audited and
        # merged. This is the no-bypass firewall relevant to checkpoint70.
        p10 = reentry["phase10_submission"]
        assert reentry["phases"]["10"]["status"] == "AUDITED_PASS_MERGED"
        assert p10["audit_status"] == "PASS"
        assert p10["pr"] == 1002
        assert p10["merge_commit"] == "5cb7dc8792faf575c1e21fce8166f094af6d7b14"
        # Every standard phase strictly before the current one must already be
        # in an audited-pass state. The current phase itself may be submitted.
        phase_order = [10, 20, 30, 40, 50, 60, 70]
        idx = phase_order.index(current_phase)
        for prior in phase_order[:idx]:
            state = reentry["phases"][str(prior)]["status"]
            if prior == 10:
                assert state == "AUDITED_PASS_MERGED"
            else:
                assert "AUDITED_PASS" in state, (prior, state)
        assert reentry["status"].startswith(f"PHASE{current_phase}_")
        lifecycle = f"POST_MERGE_REENTRY_PHASE{current_phase}"

print("STAGE25_70_CLOSEOUT_CONTRACT=PASS")
print("CHECKPOINT60_DEEP_STOP_DEPENDENCY=PASS")
print("FINAL_THEOREM_STACK_BINDING=PASS")
print("ROUTE_REGISTRY_BOUNDARY=PASS")
print("BACKFLOW_NO_DELTA_BINDING=PASS")
print("REENTRY_BYPASS_FIREWALL=PASS")
print(f"CHECKPOINT70_AUDIT_STATE={audit_status}")
print(f"CHECKPOINT70_LIFECYCLE={lifecycle}")
