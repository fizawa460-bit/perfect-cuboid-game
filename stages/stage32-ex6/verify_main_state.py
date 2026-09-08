#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STATE = HERE / "MAIN-STATE.json"
STARTUP = HERE / "MAIN-START-HERE.md"


def fail(msg: str) -> None:
    raise RuntimeError(msg)


def main() -> int:
    try:
        state = json.loads(STATE.read_text())
        if state.get("schema") != "STAGE32EX6_MAIN_COMPACT_STATE_V1_CLAIM_DAG_ENROLLMENT":
            fail("unexpected EX6 state schema")
        if state.get("role") != "ORDINARY_STAGE32EX6_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE":
            fail("EX6 state role drift")
        lineage = state.get("lineage", {})
        if lineage.get("research_pr") != 1697:
            fail("EX6 research PR drift")
        if lineage.get("final_research_head") != "205cf415424a84dbf716c75a61e945165b36912d":
            fail("EX6 final research head drift")
        if lineage.get("merge_commit") != "3358c6335dde42efd64d0704887edd1c581f5e52":
            fail("EX6 merge commit drift")
        if lineage.get("bounded_hostile_reaudit_review") != 5136845518:
            fail("EX6 bounded hostile re-audit review drift")
        if lineage.get("bounded_hostile_reaudit_result") != "PASS_EXCLUDING_FRESHNESS":
            fail("EX6 bounded hostile re-audit result drift")

        completion = state.get("completion_contract", {})
        if completion.get("current_outcome") != "O266_ENDPOINT_NOT_CLOSED":
            fail("EX6 endpoint decision drift")
        if completion.get("o266_endpoint_excluded") is not False:
            fail("EX6 must not claim O266 exclusion")
        if completion.get("o264_descent_authorized") is not False:
            fail("EX6 must not authorize O264 descent")

        current = state.get("current", {})
        if current.get("status") != "STOPPED_PENDING_NEW_ENDPOINT_INPUT":
            fail("EX6 stop status drift")
        if current.get("reentry_requires_new_input") is not True:
            fail("EX6 re-entry must require new input")

        authority = state.get("authority", {})
        if authority.get("state_itself_grants_mathematical_credit") is not False:
            fail("EX6 routing state cannot grant mathematical credit")
        if authority.get("stage32_main_authority_unchanged") is not True:
            fail("EX6 enrollment must preserve Stage32 MAIN authority")
        if authority.get("promotion_to_stage32_main_requires_explicit_current_target_adapter") is not True:
            fail("EX6 promotion adapter gate missing")
        if authority.get("promotion_to_stage32_main_requires_hostile_audit") is not True:
            fail("EX6 hostile-audit promotion gate missing")

        credit = state.get("credit", {})
        for key in (
            "o266_endpoint_excluded",
            "o264_or_lower_excluded",
            "stage32_main_credit",
            "stage32_closed",
            "perfect_cuboid_existence_claim",
            "perfect_cuboid_nonexistence_claim",
        ):
            if credit.get(key) is not False:
                fail(f"EX6 forbidden credit drift: {key}")

        for rel in state.get("current_leaf_working_set", []):
            path = ROOT / rel
            if not path.is_file():
                fail(f"EX6 current leaf path missing: {rel}")

        startup = STARTUP.read_text()
        if "Claim-DAG synchronization trigger" not in startup:
            fail("EX6 startup missing claim-sync hook")
        if "stages/stage32/proof/CLAIM-SYNC-CONTRACT.md" not in startup:
            fail("EX6 startup missing central claim-sync contract")
        for trigger in (
            "RETAINED_CONSOLIDATION",
            "AUTHORITY_OR_AUDIT_TRANSITION",
            "EX_TO_MAIN_PROMOTION",
            "ACTIVE_FRONTIER_REMAP",
            "FINAL_MILESTONE_TRANSITION",
        ):
            if trigger not in startup:
                fail(f"EX6 startup missing trigger {trigger}")

        print(json.dumps({
            "verdict": "PASS_STAGE32EX6_MAIN_STATE",
            "outcome": completion["current_outcome"],
            "status": current["status"],
            "stage32_main_credit": False,
            "o266_endpoint_excluded": False,
            "o264_descent_authorized": False,
        }, sort_keys=True))
        return 0
    except Exception as exc:
        print(json.dumps({"verdict": "FAIL_STAGE32EX6_MAIN_STATE", "error": str(exc)}, sort_keys=True))
        return 1


if __name__ == "__main__":
    sys.exit(main())
