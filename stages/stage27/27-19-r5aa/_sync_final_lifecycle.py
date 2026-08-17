from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTROLLER = ROOT / "stages" / "stage27" / "27-controller.json"
CONTRACT = Path(__file__).with_name("route-contract.json")
AUDIT = Path(__file__).with_name("audit-final.md")

R402_AUDIT = "stages/stage27/27-19-r402c-f/audit.md"
R5_AUDIT = "stages/stage27/27-19-r5aa/audit-final.md"
R402_PR = 1040
R402_MERGE = "21e28d8e418bad9814398acf2495c92841d7e12f"
R5_PR = 1048
R5_MERGE = "011bef9e0d48cea020777ccef65a8e7453df7a48"
ACTIVE_PR = 1051


def dump(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def sync_contract() -> None:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    assert data["task_id"] == "Stage27-19-r5aa"
    assert data["batch_id"] == "Stage27-19-r5"
    assert data["batch_routes"] == [
        "27-19-r5aa",
        "27-19-r5ab",
        "27-19-r5ac",
        "27-19-r5ad",
        "27-19-r5ae",
    ]

    data["status"] = "CLOSED_AUDITED_PASS_MERGED"
    data["final_audit"] = {
        "verdict": "PASS",
        "mathematical_audit": "PASS",
        "ci_audit": "PASS",
        "lifecycle_audit": "PASS",
        "previous_fail_reason": "POST_R5_FRESH_AUDIT_NOT_REGISTERED_IN_REPO",
        "record": R5_AUDIT,
        "pr": R5_PR,
        "merge_commit": R5_MERGE,
        "audited_routes": [
            "27-19-r5aa",
            "27-19-r5ab",
            "27-19-r5ac",
            "27-19-r5ad",
            "27-19-r5ae",
        ],
        "checkpoint": 40,
        "advance_to_checkpoint50": False,
    }
    data["lifecycle_closed"] = True
    data["controller_sync_complete"] = True
    data["controller_sync_policy"] = "SATISFIED_BY_FINAL_AUDIT_REGISTRATION"
    data["next_derived_route"] = "27-19-r5af"
    dump(CONTRACT, data)


def sync_controller() -> None:
    data = json.loads(CONTROLLER.read_text(encoding="utf-8"))
    derived = data["derived_routes"]

    # r402c-f already has a hostile PASS audit and merged PR #1040; clear stale pending lifecycle.
    for suffix in "cdef":
        key = f"Stage27-19-r402{suffix}"
        route = derived[key]
        route["status"] = "INTERMEDIATE_AUDITED_PASS_MERGED"
        route["audit_status"] = "PASS"
        route["audit_record"] = R402_AUDIT
        route["pr"] = R402_PR
        route["merge_commit"] = R402_MERGE
        route["advance_allowed"] = True
        route["merge_allowed"] = True
        route["advance_to_checkpoint50"] = False
    derived["Stage27-19-r402f"]["historical_next_derived_route"] = derived["Stage27-19-r402f"].get(
        "next_derived_route", "27-19-r402g"
    )
    derived["Stage27-19-r402f"]["next_derived_route"] = "27-19-r5aa"

    # Canonical registration for the merged r5aa-r5ae batch.
    derived["Stage27-19-r5"] = {
        "status": "AUDITED_PASS_MERGED_CLOSED",
        "trigger_checkpoint": 40,
        "route_serial": "19-r5",
        "route_kind": "UPPER_REENTRY_PARALLEL",
        "source_stage": "Stage19",
        "parent_route": "Stage27-19-r402c-f",
        "batch_routes": [
            "27-19-r5aa",
            "27-19-r5ab",
            "27-19-r5ac",
            "27-19-r5ad",
            "27-19-r5ae",
        ],
        "audit_status": "PASS",
        "mathematical_audit": "PASS",
        "ci_audit": "PASS",
        "lifecycle_audit": "PASS",
        "previous_fail_reason": "POST_R5_FRESH_AUDIT_NOT_REGISTERED_IN_REPO",
        "audit_record": R5_AUDIT,
        "pr": R5_PR,
        "merge_commit": R5_MERGE,
        "uniform_moving_tau_distinct_core_power_bound": True,
        "uniform_moving_tau_fiber_power_bound": True,
        "norm_support_only_power_saving_barrier": True,
        "strict_sub_sqrt_upper_proved": False,
        "new_mu_lt_half_proved": False,
        "true_N2_exponent_identified": False,
        "advance_to_checkpoint50": False,
        "continue_upper_exploration": True,
        "advance_allowed": True,
        "merge_allowed": True,
        "next_derived_route": "27-19-r5af",
    }

    # Current continuation is already materialized as Draft PR #1051 and remains pending fresh audit.
    derived["Stage27-19-r5af-r5ag"] = {
        "status": "BATCH_SUBMITTED_PENDING_FRESH_AUDIT",
        "trigger_checkpoint": 40,
        "route_serial": "19-r5af-r5ag",
        "route_kind": "UPPER_REENTRY_PARALLEL",
        "source_stage": "Stage19",
        "parent_route": "Stage27-19-r5",
        "batch_routes": ["27-19-r5af", "27-19-r5ag"],
        "audit_status": "PENDING",
        "pr": ACTIVE_PR,
        "advance_to_checkpoint50": False,
        "advance_allowed": False,
        "merge_allowed": False,
        "strict_sub_sqrt_upper_proved": False,
        "new_mu_lt_half_proved": False,
        "true_N2_exponent_identified": False,
        "next_derived_route": "27-19-r5ah",
    }

    data["status"] = "OPEN_CHECKPOINT40_WITH_STAGE19_UPPER_REENTRY_R5AF_R5AG_PENDING_FRESH_AUDIT"
    data["checkpoint_status"]["40"] = (
        "UPPER_ATTACK_AUDITED_PASS_MERGED_WITH_R402C_F_AUDITED_PASS_MERGED_"
        "AND_R5_AUDITED_PASS_MERGED_CLOSED_AND_R5AF_R5AG_PENDING_AUDIT"
    )
    data["checkpoint_status"]["50"] = "BLOCKED_BY_ACTIVE_CHECKPOINT40_DERIVED_ROUTE"

    state = data["state"]
    state["CURRENT_CHECKPOINT"] = 40
    state["MAIN_STATUS"] = "UPPER_REENTRY_STAGE27_19_R5AF_R5AG_SUBMITTED_PENDING_FRESH_AUDIT"
    state["AUDIT_STATUS"] = "PENDING"
    state["ADVANCE_ALLOWED"] = False
    state["NEXT_CHECKPOINT"] = 40
    state["NEXT_STAGE"] = ""
    state["NEW_INPUT_REQUIRED"] = False
    state["HUMAN_DECISION_REQUIRED"] = False
    state["MERGE_ALLOWED"] = False

    data["next_expected_command"] = "Stage27-19-r5-audit"
    dump(CONTROLLER, data)


def write_audit() -> None:
    AUDIT.write_text(
        """# Stage27-19-r5 final lifecycle audit\n\n"
        "```text\n"
        "AUDIT_VERDICT=PASS\n"
        "MATHEMATICAL_AUDIT=PASS\n"
        "CI_AUDIT=PASS\n"
        "LIFECYCLE_AUDIT=PASS\n"
        "PREVIOUS_FAIL_REASON=POST_R5_FRESH_AUDIT_NOT_REGISTERED_IN_REPO\n"
        "REPAIR_SCOPE=FINAL_AUDIT_RECORD+ROUTE_CONTRACT+C27_CONTROLLER_SYNC\n"
        "PR=1048\n"
        "MERGE_COMMIT=011bef9e0d48cea020777ccef65a8e7453df7a48\n"
        "R402C_F_PR=1040\n"
        "R402C_F_MERGE_COMMIT=21e28d8e418bad9814398acf2495c92841d7e12f\n"
        "AUDIT_CLOSE_ROUTE=true\n"
        "CURRENT_CHECKPOINT=40\n"
        "NEXT_CHECKPOINT=40\n"
        "ADVANCE_TO_CHECKPOINT50=false\n"
        "STRICT_SUB_SQRT_UPPER_PROVED=false\n"
        "NEW_MU_LT_HALF_PROVED=false\n"
        "TRUE_N2_EXPONENT_IDENTIFIED=false\n"
        "NEXT_DERIVED_ROUTE=27-19-r5af\n"
        "```\n\n"
        "This record closes the repository lifecycle gap detected after PR #1048 had already merged. "
        "The r5aa-r5ae mathematical claims are not re-proved here: the mathematical audit and dedicated CI were already PASS; "
        "the only failing gate was missing canonical post-merge registration.\n\n"
        "The repair records the merged r5 batch as closed/PASS, synchronizes the already-audited and merged r402c-f predecessor, "
        "and moves the Stage27 controller's active checkpoint40 continuation to the existing r5af-r5ag Draft PR #1051.\n\n"
        "No exponent promotion is made. Checkpoint50 remains blocked, and the next fresh mathematical audit target is r5af-r5ag.\n"
        """,
        encoding="utf-8",
    )


def verify() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    controller = json.loads(CONTROLLER.read_text(encoding="utf-8"))
    assert contract["status"] == "CLOSED_AUDITED_PASS_MERGED"
    assert contract["final_audit"]["verdict"] == "PASS"
    assert contract["controller_sync_complete"] is True
    for suffix in "cdef":
        route = controller["derived_routes"][f"Stage27-19-r402{suffix}"]
        assert route["audit_status"] == "PASS"
        assert route["status"] == "INTERMEDIATE_AUDITED_PASS_MERGED"
    r5 = controller["derived_routes"]["Stage27-19-r5"]
    assert r5["status"] == "AUDITED_PASS_MERGED_CLOSED"
    assert r5["audit_status"] == "PASS"
    assert r5["pr"] == 1048
    active = controller["derived_routes"]["Stage27-19-r5af-r5ag"]
    assert active["audit_status"] == "PENDING"
    assert active["pr"] == 1051
    assert controller["state"]["CURRENT_CHECKPOINT"] == 40
    assert controller["state"]["MAIN_STATUS"].endswith("PENDING_FRESH_AUDIT")
    assert controller["next_expected_command"] == "Stage27-19-r5-audit"
    assert AUDIT.exists()


if __name__ == "__main__":
    sync_contract()
    sync_controller()
    write_audit()
    verify()
    print("Stage27-19-r5 lifecycle synchronization: PASS")
