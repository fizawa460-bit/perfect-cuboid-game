#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def data(rel: str):
    p = ROOT / rel
    assert p.exists(), f"missing {rel}"
    return json.loads(p.read_text(encoding="utf-8"))


def text(rel: str) -> str:
    p = ROOT / rel
    assert p.exists(), f"missing {rel}"
    return p.read_text(encoding="utf-8")


controller = data("stages/stage25/25-reentry-controller.json")
parent = data("stages/stage25/25-controller.json")
closeout = data("stages/stage25/25-70/controller.json")
roadmap = text("docs/stage25-reentry-roadmap.md")
operations = text("docs/stage25-reentry-operations.md")

# Immutable unlock contract.
assert controller["starts_after"]["stage25_checkpoint"] == 70
assert controller["starts_after"]["audit_verdict"] == "PASS"
assert controller["starts_after"]["closeout_merged"] is True
assert controller["starts_after"]["unresolved_repair_bypass_allowed"] is False
assert parent["status"] == "CLOSED"
assert parent["checkpoint_status"]["70"] == "PROVED_AUDITED_PASS"
assert parent["state"]["NEXT_STAGE"] == "Stage25-reentry"
assert closeout["audit_status"] == "PASS"
assert closeout["closeout_merged"] is True
assert closeout["stage25_reentry_unlocked"] is True

# Fixed phase plan and route identity discipline.
expected = {
    "10": "Stage25-um-r001a",
    "20": "Stage25-u24-r002a",
    "30": "Stage25-u23-r003a",
    "40": "Stage25-u22-r004a",
    "50": "Stage25-u21-r005a",
    "60": "Stage25-u20-r006a",
    "70": "Stage25-um-r007a",
}
assert list(controller["phases"]) == list(expected)
pattern = re.compile(r"^Stage25-(?:u\d+|um)-r0\d{2}[a-z]$")
for phase, task_id in expected.items():
    assert controller["phases"][phase]["task_id"] == task_id
    assert pattern.match(task_id), task_id
    assert task_id in roadmap
assert "Stage25-reentry-main-batch" in roadmap
assert "Stage25-reentry-audit" in operations
assert "24 -> 23 -> 22 -> 21 -> 20" in roadmap

policy = controller["derived_route_policy"]
assert policy["maximum_simultaneous_active_routes"] == 3
assert policy["route_ids_recycled"] is False
assert policy["parent_phase_audit_required_before_recursive_launch"] is True
assert policy["next_route_serial"] >= 8
route_re = re.compile(r"-r0(\d{2})[a-z]$")
serials = []
for item in controller.get("propagation_queue", []):
    m = route_re.search(item["route_id"])
    assert m, item["route_id"]
    serials.append(int(m.group(1)))
if serials:
    assert len(serials) == len(set(serials))
    assert policy["next_route_serial"] == max(serials) + 1

# Stage26 stays blocked throughout reentry.
gate = controller["stage26_gate"]
assert gate["stage25_main_closed"] is True
assert gate["all_reentry_phases_audited"] is False
assert gate["unresolved_internal_routes"] is True
assert gate["stage26_allowed"] is False
assert controller["safety"]["finite_data_as_asymptotic_proof"] is False
assert controller["safety"]["stage25_current_deep_stop_rule_relaxed"] is False

# Phase10 must be fully audited and merged before any later state.
p10 = controller["phase10_submission"]
assert controller["phases"]["10"]["status"] == "AUDITED_PASS_MERGED"
assert p10["audit_status"] == "PASS"
assert p10["pr"] == 1002
assert p10["merge_commit"] == "5cb7dc8792faf575c1e21fce8166f094af6d7b14"

current = controller["current_phase"]
assert current in (10, 20, 30, 40, 50, 60, 70)
status = controller["status"]

if current == 20:
    p20 = controller["phase20_submission"]
    assert p20["task_id"] == "Stage25-u24-r002a"
    assert p20["audit_status"] == "PASS"
    assert p20["stronger_result_proved"] is True
    assert p20["new_reusable_weapon_proved"] is True
    assert p20["accepted_theorem"] == "N2,j(B)>>_j B^(1/4) for j=a,b,c"

    if status == "PHASE20_AUDITED_PASS_AWAITING_MERGE_AND_BACKFLOW":
        assert controller["phases"]["20"]["status"] == "AUDITED_PASS_AWAITING_MERGE_AND_BACKFLOW"
        assert p20["pr"] == 1003
        assert controller["phases"]["30"]["status"] == "BLOCKED_UNTIL_PHASE20_BACKFLOW"
        assert controller["propagation_queue"][0]["status"] == "AUTHORIZED_BY_PHASE20_AUDIT_AWAITING_PARENT_MERGE"
    elif status in (
        "PHASE20_BACKFLOW_SUBMITTED_PENDING_FRESH_AUDIT",
        "PHASE20_BACKFLOW_AUDITED_PASS_AWAITING_MERGE",
    ):
        assert controller["phases"]["20"]["status"] in (
            "AUDITED_PASS_MERGED_BACKFLOW_PENDING_AUDIT",
            "AUDITED_PASS_MERGED_BACKFLOW_AUDITED_PASS_AWAITING_MERGE",
        )
        assert p20["pr"] == 1003
        assert p20["merge_commit"] == "1d88e8e3254a383620e221df8a1a1039ebeabcd4"
        r8 = controller["r008a_submission"]
        assert r8["route_id"] == "Stage25-um-r008a"
        assert r8["parent_task"] == "Stage25-u24-r002a"
        assert r8["parent_pr"] == 1003
        assert r8["parent_merge_commit"] == p20["merge_commit"]
        for rel in (r8["result"], r8["registry"], r8["verifier"], r8["workflow"]):
            assert (ROOT / rel).exists(), rel
        queued = [x for x in controller["propagation_queue"] if x["route_id"] == "Stage25-um-r008a"]
        assert len(queued) == 1
        assert queued[0]["blocks_next_phase"] is True
        assert controller["phases"]["30"]["status"] == "BLOCKED_UNTIL_R008A_AUDIT_PASS_MERGE"
        if status == "PHASE20_BACKFLOW_SUBMITTED_PENDING_FRESH_AUDIT":
            assert r8["status"] == "SUBMITTED_PENDING_FRESH_AUDIT"
            assert r8["audit_status"] == "PENDING"
            assert r8["advance_allowed"] is False
            assert r8["merge_allowed"] is False
            assert queued[0]["status"] == "SUBMITTED_PENDING_FRESH_AUDIT"
            assert controller["next_expected_command"] == "Stage25-reentry-audit"
        else:
            assert r8["status"] == "AUDITED_PASS_AWAITING_MERGE"
            assert r8["audit_status"] == "PASS"
            assert r8["advance_allowed"] is True
            assert r8["merge_allowed"] is True
    else:
        raise AssertionError(f"unexpected phase20 lifecycle: {status}")
else:
    # Later phases require phase20 and r008a to have been audited and merged.
    assert current >= 30
    p20 = controller["phase20_submission"]
    assert "AUDITED_PASS_MERGED" in controller["phases"]["20"]["status"]
    assert p20["audit_status"] == "PASS"
    assert p20["merge_commit"] == "1d88e8e3254a383620e221df8a1a1039ebeabcd4"
    r8 = controller["r008a_submission"]
    assert r8["status"] == "AUDITED_PASS_MERGED"
    assert r8["audit_status"] == "PASS"
    assert r8["merge_commit"]
    assert not any(x["route_id"] == "Stage25-um-r008a" and x["blocks_next_phase"] for x in controller["propagation_queue"])

    if status.startswith(f"PHASE{current}_"):
        pass
    elif current == 50 and status.startswith("R011A_"):
        # Legal derived-route lifecycle after phase50 audit+merge.  This branch
        # must preserve all previous gates and may not authorize phase60 early.
        p50 = controller["phase50_submission"]
        assert p50["task_id"] == "Stage25-u21-r005a"
        assert p50["audit_status"] == "PASS"
        assert p50["pr"] == 1009
        assert p50["merge_commit"] == "8765eb73db07da8afb8ad9b1f9a538ff8cd080ee"
        assert controller["phases"]["50"]["status"] == "AUDITED_PASS_MERGED_DERIVED_ROUTE_SUBMITTED"

        r11 = controller["r011a_submission"]
        assert r11["route_id"] == "Stage25-um-r011a"
        assert r11["parent_task"] == "Stage25-u21-r005a"
        assert r11["parent_pr"] == 1009
        assert r11["parent_merge_commit"] == p50["merge_commit"]
        for rel in (
            r11["result"], r11["proof"], r11["analytic_ledger"],
            r11["discovery_ledger"], r11["weapon_delta"],
            r11["verifier"], r11["workflow"],
        ):
            assert (ROOT / rel).exists(), rel
        assert r11["common_dirichlet_pole_slot_ledger_proved"] is False
        assert r11["independent_factorization_proved"] is False

        queued = [x for x in controller["propagation_queue"] if x["route_id"] == "Stage25-um-r011a"]
        assert len(queued) == 1
        assert queued[0]["blocks_next_phase"] is True
        assert controller["phases"]["60"]["status"] == "BLOCKED_UNTIL_R011A_AUDIT_PASS_MERGE"
        assert controller["next_expected_command"] == "Stage25-reentry-audit"

        if status == "R011A_SUBMITTED_PENDING_FRESH_AUDIT":
            assert r11["status"] == "SUBMITTED_PENDING_FRESH_AUDIT"
            assert r11["audit_status"] == "PENDING"
            assert r11["advance_allowed"] is False
            assert r11["merge_allowed"] is False
            assert queued[0]["status"] == "SUBMITTED_PENDING_FRESH_AUDIT"
        else:
            # Future audit promotion may use another R011A_* state, but it must
            # carry an explicit PASS rather than bypassing this branch.
            assert r11["audit_status"] == "PASS"
    else:
        raise AssertionError(f"unexpected later-phase lifecycle: phase={current}, status={status}")

print("STAGE25_REENTRY_CONTROLLER=PASS")
print("STAGE25_REENTRY_PHASE_ORDER=PASS")
print("STAGE25_REENTRY_R008A_NO_BYPASS=PASS")
print("STAGE25_REENTRY_R011A_NO_BYPASS=PASS")
print("STAGE25_DERIVED_PROPAGATION_QUEUE=PASS")
print("STAGE26_GATE_INITIAL_BLOCK=PASS")
