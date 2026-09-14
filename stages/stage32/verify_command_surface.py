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
    req("stages/stage32/MAIN-STATE.json" in commands, "command registry missing MAIN authority path")
    req("stages/stage32/proof/CROSS-LANE-DEMANDS.json" in commands, "command registry missing demand authority path")
    req("Each lane's startup/read order belongs only in that lane's `MAIN-START-HERE.md`" in commands,
        "command registry does not separate lane startup ownership")
    for stale in (
        "currently #1800",
        "Current MAIN transition",
        "Candidate V22 authority",
        "47,589,703,313,957,134,804,198",
    ):
        req(stale not in commands, f"dynamic/stale MAIN state retained in command registry: {stale}")

    demand_registry = load(HERE / "proof" / "CROSS-LANE-DEMANDS.json")
    req(demand_registry.get("stage") == 32, "cross-lane demand registry stage drift")
    req(isinstance(demand_registry.get("demands"), list), "cross-lane demand registry malformed")

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

    start178 = text(HERE / "32-01-178" / "MAIN-START-HERE.md")
    req("single authoritative startup/read-order contract" in start178, "178 canonical startup ownership missing")
    req("stage32-01-178-mainbatch" in start178, "178 canonical command missing from startup")
    req("stages/stage32/MAIN-STATE.json" in start178, "178 startup missing MAIN authority")
    req("stages/stage32/proof/CROSS-LANE-DEMANDS.json" in start178, "178 demand-aware startup missing")
    req("MISSION.json" in start178 and "on-demand only" in start178, "178 historical mission removed from startup incorrectly")
    req("COMMANDS.md" in start178 and "not a second 178 startup contract" in start178,
        "178 command-registry/startup separation missing")
    req("CROSS-LANE-STARTUP-CONTRACT.md" in start178 and "on-demand reference" in start178,
        "178 shared demand prose not bounded to on-demand reference")
    req("PR #1765" not in start178 and "N357" not in start178,
        "178 startup still pins stale lane/current-history identifiers")

    mainbatch178 = text(HERE / "32-01-178" / "MAINBATCH.md")
    req("stages/stage32/32-01-178/MAIN-START-HERE.md" in mainbatch178,
        "178 MAINBATCH does not delegate to canonical startup")
    req("only authoritative startup/read-order contract" in mainbatch178,
        "178 MAINBATCH still acts as a second startup contract")
    req("MISSION.json" in mainbatch178 and "on-demand" in mainbatch178,
        "178 MAINBATCH still treats mission history as ordinary startup")
    req("Read only, in this order" not in mainbatch178,
        "178 MAINBATCH retains a duplicate startup sequence")
    req("PR #1765" not in mainbatch178 and "BC2-24" not in mainbatch178,
        "178 MAINBATCH retains stale EX5 checkpoint routing")

    ex5 = load(REPO / "stages" / "stage32-ex5" / "MAIN-STATE.json")
    req(ex5["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V5_POST_1765_MERGE", "EX5 retained state schema drift")
    b = ex5["bootstrap"]
    req(b["latest_merged_pr"] == 1765, "EX5 merged PR provenance drift")
    req(b["merge_authorized"] is False, "EX5 inherited old merge authorization")
    req(ex5["current"]["next_route"] == "BC2_25_POST_MERGE_UNKNOWN_REFINEMENT_PREFLIGHT", "EX5 retained local-route history drift")
    req(ex5["next_step"]["bc2_25_deferred_until_after_merge"] is False, "EX5 still merge-first blocked")

    ex5_start = text(REPO / "stages" / "stage32-ex5" / "MAIN-START-HERE.md")
    req("PR #1765 is merged" in ex5_start, "EX5 startup lost merged provenance")
    req("stage32ex5-mainbatch" in ex5_start, "EX5 command missing")
    req("stages/stage32/COMMANDS.md" in ex5_start, "EX5 startup does not read command registry")
    req("higher-priority OPEN demand" in ex5_start, "EX5 startup lost generic producer-priority rule")
    req("SATISFIED" in ex5_start and "CUT192-EX5-E8-HANDOFF-SATISFIED.json" in ex5_start, "EX5 startup has stale producer wait state")

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

    print("PASS: Stage32 command registry is state-free and lane startup contracts are authority-separated")
    print("178 startup=MAIN-START-HERE only; MISSION/history=on-demand; demand registry=machine authority")


if __name__ == "__main__":
    main()
