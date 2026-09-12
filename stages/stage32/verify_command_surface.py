#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit(f"FAIL: {msg}")


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(text(path))


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def main() -> None:
    commands = text(HERE / "COMMANDS.md")
    for token in (
        "stage32mainbatch", "stage32audit",
        "stage32-01-178-mainbatch", "stage32-01-178-audit",
        "stage32ex5-mainbatch", "stage32ex5-audit",
        "stage32cut-mainbatch", "stage32cut-audit",
        "stage32mb-mainbatch", "stage32mb-audit",
    ):
        req(token in commands, f"canonical command missing: {token}")
    req("CROSS-LANE-DEMANDS.json" in commands, "command registry missing cross-lane demand routing")
    req("S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1" in commands, "command registry missing CUT192 demand")
    req("SATISFIED" in commands and "CUT193" in commands, "command registry has stale CUT192 wait state")
    req("CUT191" in commands and "already consumed" in commands, "command registry does not preserve CUT191 consumption")

    demand_registry = load(HERE / "proof" / "CROSS-LANE-DEMANDS.json")
    demand_rows = {row["demand_id"]: row for row in demand_registry["demands"]}
    cut192_id = "S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1"
    req(cut192_id in demand_rows, "CUT192 demand missing from machine registry")
    cut192 = demand_rows[cut192_id]
    req(cut192["priority"] == "P0_BLOCKING_DOWNSTREAM", "CUT192 machine priority drift")
    req(cut192["status"] == "SATISFIED", "CUT192 machine status is stale")

    main_start = text(HERE / "MAIN-START-HERE.md")
    req("Ordinary `stage32mainbatch`" in main_start, "MAIN command not canonical")
    req("controller and researcher" in main_start.lower(), "MAIN research role missing")
    for stale in ("`Stage32-main-batch`", "`stage32main batch`"):
        req(stale not in main_start, f"stale MAIN spelling retained: {stale}")
    req("stages/stage32/COMMANDS.md" in main_start, "MAIN startup does not read command registry")
    req("stage32cut-mainbatch" in main_start, "MAIN startup missing CUT ownership boundary")
    req("stage32mb-mainbatch" in main_start, "MAIN startup missing MB ownership boundary")
    req("verify_cross_lane_demands.py" in main_start, "MAIN startup missing demand monitor verifier")

    mission = load(HERE / "32-01-178" / "MISSION.json")
    req(mission["status"] == "ACTIVE", "178 mission unexpectedly inactive")
    req(mission["operator_commands"]["cycle"] == "stage32-01-178-mainbatch", "178 cycle command drift")
    req(mission["operator_commands"]["audit"] == "stage32-01-178-audit", "178 audit command drift")
    req(mission["dispatch"]["future_parallel_dispatch_enabled"] is False, "178 child fanout re-enabled")
    sync = mission["operator_sync"]
    req(sync["routing_authority"] == "stages/stage32/MAIN-STATE.json", "178 routing authority drift")
    req(sync["startup_snapshot_is_historical"] is True, "178 stale snapshot not firewalled")
    req(sync["latest_ex5_merged_pr"] == 1765, "178 EX5 merge observation stale")
    start178 = text(HERE / "32-01-178" / "MAIN-START-HERE.md")
    req("stage32-01-178-mainbatch" in start178 and "CROSS-LANE-DEMANDS.json" in start178, "178 demand-aware startup missing")

    ex5 = load(REPO / "stages" / "stage32-ex5" / "MAIN-STATE.json")
    ex5_schema = ex5["schema"]
    allowed_ex5_schemas = {
        "STAGE32EX5_MAIN_COMPACT_STATE_V5_POST_1765_MERGE",
        "STAGE32EX5_MAIN_COMPACT_STATE_V22_BC2_34_TARGETED_REPLAY_AUDIT_BOUNDARY",
        "STAGE32EX5_MAIN_COMPACT_STATE_V23_BC2_34_AUDIT_CONSUMED_BC2_35_EXECUTION",
    }
    req(ex5_schema in allowed_ex5_schemas, "EX5 retained state schema drift")
    b = ex5["bootstrap"]
    req(b["latest_merged_pr"] == 1765, "EX5 merged PR provenance drift")
    req(b["merge_authorized"] is False, "EX5 inherited old merge authorization")

    ex5_start = text(REPO / "stages" / "stage32-ex5" / "MAIN-START-HERE.md")
    req("stage32ex5-mainbatch" in ex5_start, "EX5 command missing")
    req("stages/stage32/COMMANDS.md" in ex5_start, "EX5 startup does not read command registry")

    if ex5_schema == "STAGE32EX5_MAIN_COMPACT_STATE_V5_POST_1765_MERGE":
        req(ex5["current"]["next_route"] == "BC2_25_POST_MERGE_UNKNOWN_REFINEMENT_PREFLIGHT", "EX5 retained local-route history drift")
        req(ex5["next_step"]["bc2_25_deferred_until_after_merge"] is False, "EX5 still merge-first blocked")
        req("PR #1765 is merged" in ex5_start, "EX5 startup lost merged provenance")
        req("higher-priority OPEN demand" in ex5_start, "EX5 startup lost generic producer-priority rule")
        req("SATISFIED" in ex5_start and "CUT192-EX5-E8-HANDOFF-SATISFIED.json" in ex5_start, "EX5 startup has stale producer wait state")
    else:
        req(b["active_work_pr"] == 1776, "EX5 active work PR drift")
        req(b["current_main_sha_observed"] == "e4d3b8b83626526ffeccdbd9c956081735fe1a6e", "EX5 current MAIN observation drift")
        main_auth = ex5["stage32_main_authority"]
        req(main_auth["current_main_schema"] == "STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED", "EX5 MAIN schema drift")
        req(main_auth["current_main_sha"] == "e4d3b8b83626526ffeccdbd9c956081735fe1a6e", "EX5 MAIN SHA drift")
        req(main_auth["full178_numerical_census_complete"] is False, "EX5 falsely closes FULL178")
        req(main_auth["ex5_auto_promotes_to_main"] is False, "EX5 self-promotion enabled")
        routing = ex5["cross_lane_routing"]
        req(routing["open_ex5_producer_demand_count"] == 0, "EX5 has unhandled OPEN producer demand")
        req(routing["satisfied_cut192_handoff_preserved"] is True, "EX5 lost CUT192 satisfied handoff")
        req("PR #1776 remains active/open/draft/unmerged" in ex5_start, "EX5 startup lost active PR provenance")
        req("higher-priority OPEN producer demand" in ex5_start, "EX5 startup lost generic producer-priority rule")
        req("S32.DEMAND.CUT192.EX5.DISJOINT_E8_PICARD64.V1" in ex5_start and "SATISFIED" in ex5_start, "EX5 startup lost satisfied CUT192 demand")
        req("does not grant mathematical credit" in ex5_start.lower(), "EX5 startup missing demand/credit separation")
        current = ex5["current"]
        if ex5_schema == "STAGE32EX5_MAIN_COMPACT_STATE_V22_BC2_34_TARGETED_REPLAY_AUDIT_BOUNDARY":
            req(routing["local_bc2_34_audit_boundary_may_continue"] is True, "EX5 V22 local audit boundary not authorized")
            req(current["leaf"] == "BC2_34_REFINE_REMAINING_FRESH_UNKNOWN_SET", "EX5 V22 BC2-34 leaf drift")
            req(current["status"] == "BC2_34_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED", "EX5 V22 audit status drift")
            req(current["blocker"] == "HOSTILE_AUDIT_BC2_34_REQUIRED", "EX5 V22 audit blocker drift")
            req(current["next_route"] == "HOSTILE_AUDIT_BC2_34_TARGETED_REPLAY", "EX5 V22 next route drift")
            req("stage32ex5-audit" in ex5_start and "BC2-35 is blocked" in ex5_start, "EX5 V22 startup lost audit stop rule")
        else:
            req(routing["local_bc2_35_execution_may_continue"] is True, "EX5 V23 BC2-35 execution not authorized")
            req(current["leaf"] == "BC2_35_REFINE_REMAINING_FRESH_UNKNOWN_SET", "EX5 V23 BC2-35 leaf drift")
            req(current["status"] == "BC2_35_TARGETED_REPLAY_EXECUTION_AUTHORIZED", "EX5 V23 execution status drift")
            req(current["blocker"] == "BC2_35_FRESH_RUNKEY_NOT_YET_CONSUMED", "EX5 V23 execution blocker drift")
            req(current["next_route"] == "BC2_35_REFINE_REMAINING_FRESH_UNKNOWN_SET", "EX5 V23 next route drift")
            req("BC2-34 hostile re-audit PASS" in ex5_start, "EX5 V23 startup lost BC2-34 PASS consumption")
            req("BC2-35 execution" in ex5_start and "BC2-36 is blocked" in ex5_start, "EX5 V23 startup lost execution/next-audit gate")

    cut = load(HERE / "full178-cut" / "MISSION.json")
    req(cut["status"] == "ACTIVE", "CUT mission unexpectedly inactive")
    req(cut["operator_commands"]["main"] == "stage32cut-mainbatch", "CUT command drift")
    req(cut["operator_commands"]["audit"] == "stage32cut-audit", "CUT audit command drift")
    req(cut["routing"]["authority"] == "stages/stage32/MAIN-STATE.json", "CUT routing authority drift")
    req(cut["routing"]["current_main_credit_auto_promotion"] is False, "CUT self-promotion enabled")
    req(cut["inputs"]["required_ex5_property"] == "picard64_exact_completion_interface_available=true", "CUT/EX5 interface contract drift")
    cut_excluded = " ".join(cut["ownership"]["does_not_own"])
    req("EX5 terminal-to-Picard64 adapter" in cut_excluded, "CUT may duplicate EX5 adapter work")
    req("N356" in cut_excluded, "CUT may duplicate 178 work")
    req(cut["credit_firewall"]["stage32_main_pruning_credit"] is False, "CUT mission starts with MAIN credit")
    cut_start = text(HERE / "full178-cut" / "MAIN-START-HERE.md")
    req("stage32cut-mainbatch" in cut_start and "CROSS-LANE-DEMANDS.json" in cut_start, "CUT demand-aware startup missing")
    req("CUT191" in cut_start and "consumed" in cut_start, "CUT startup lost CUT191 separation")
    req("SATISFIED" in cut_start and "CUT193" in cut_start, "CUT startup has stale waiting state")

    mb_dir = HERE / "final-chain" / "32-03-multibranch"
    mb = load(mb_dir / "MISSION.json")
    req(mb["status"] == "ACTIVE", "MB mission unexpectedly inactive")
    req(mb["operator_commands"]["main"] == "stage32mb-mainbatch", "MB command drift")
    req(mb["operator_commands"]["audit"] == "stage32mb-audit", "MB audit command drift")
    req(mb["routing"]["authority"] == "stages/stage32/MAIN-STATE.json", "MB routing authority drift")
    req(mb["routing"]["independent_of_full178_execution"] is True, "MB lost FULL178 independence")
    req(mb["routing"]["main_credit_auto_promotion"] is False, "MB self-promotion enabled")
    locked_preflight_sha = mb["routing"]["preflight_blob_sha1"]
    req(locked_preflight_sha == "f625c14b665af668d9ce6b6e78d0b05a2a27bd27", "MB preflight source lock drift")
    req(git_blob_sha1(mb_dir / "PREFLIGHT.json") == locked_preflight_sha, "MB PREFLIGHT actual Git blob SHA drift")
    req(mb["execution"]["first_leaf"] == "MB101", "MB first leaf drift")
    req(mb["credit_firewall"]["receiver_credit"] is False, "MB starts with receiver credit")
    mb_start = text(mb_dir / "MAIN-START-HERE.md")
    req("stage32mb-mainbatch" in mb_start and "CROSS-LANE-DEMANDS.json" in mb_start, "MB demand-aware startup missing")

    runpy.run_path(str(HERE / "proof" / "verify_cross_lane_demands.py"), run_name="__main__")
    print("PASS: Stage32 command surface is canonical, demand-aware, and authority-separated")
    print("MAIN=global-monitor; EX5=producer-handoff-complete; CUT=consumer-reentered; 178/MB=specialists")
    print("CUT192=SATISFIED_EX5_TO_CUT; CUT193=REENTERED_ZERO_MAIN_CREDIT; CUT191=MAIN_CONSUMED")


if __name__ == "__main__":
    main()
