#!/usr/bin/env python3
from __future__ import annotations

import json
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


def main() -> None:
    commands = text(HERE / "COMMANDS.md")
    for token in (
        "stage32mainbatch",
        "stage32audit",
        "stage32-01-178-mainbatch",
        "stage32-01-178-audit",
        "stage32ex5-mainbatch",
        "stage32ex5-audit",
    ):
        req(token in commands, f"canonical command missing: {token}")

    main_start = text(HERE / "MAIN-START-HERE.md")
    req("Ordinary `stage32mainbatch`" in main_start, "MAIN command not canonical")
    req("controller and researcher" in main_start.lower(), "MAIN research role missing")
    for stale in ("`Stage32-main-batch`", "`stage32main batch`"):
        req(stale not in main_start, f"stale MAIN spelling retained: {stale}")
    req("stages/stage32/COMMANDS.md" in main_start, "MAIN startup does not read command registry")

    mission = load(HERE / "32-01-178" / "MISSION.json")
    req(mission["status"] == "ACTIVE", "178 mission unexpectedly inactive")
    req(mission["operator_commands"]["cycle"] == "stage32-01-178-mainbatch", "178 cycle command drift")
    req(mission["operator_commands"]["audit"] == "stage32-01-178-audit", "178 audit command drift")
    req(mission["dispatch"]["future_parallel_dispatch_enabled"] is False, "178 child fanout re-enabled")
    sync = mission["operator_sync"]
    req(sync["routing_authority"] == "stages/stage32/MAIN-STATE.json", "178 routing authority drift")
    req(sync["startup_snapshot_is_historical"] is True, "178 stale snapshot not firewalled")
    req(sync["latest_ex5_merged_pr"] == 1765, "178 EX5 merge observation stale")

    ex5 = load(REPO / "stages" / "stage32-ex5" / "MAIN-STATE.json")
    req(ex5["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V5_POST_1765_MERGE", "EX5 post-merge schema drift")
    b = ex5["bootstrap"]
    req(b["active_work_pr"] is None and b["work_branch"] is None, "EX5 stale active PR/branch")
    req(b["latest_merged_pr"] == 1765, "EX5 merged PR provenance drift")
    req(b["merge_authorized"] is False, "EX5 inherited old merge authorization")
    req(ex5["current"]["next_route"] == "BC2_25_POST_MERGE_UNKNOWN_REFINEMENT_PREFLIGHT", "EX5 next route drift")
    req(ex5["next_step"]["bc2_25_deferred_until_after_merge"] is False, "EX5 still merge-first blocked")

    ex5_start = text(REPO / "stages" / "stage32-ex5" / "MAIN-START-HERE.md")
    req("PR #1765 is merged" in ex5_start, "EX5 startup still treats #1765 as open")
    req("stage32ex5-mainbatch" in ex5_start, "EX5 command missing")
    req("stages/stage32/COMMANDS.md" in ex5_start, "EX5 startup does not read command registry")

    print("PASS: Stage32 command surface is canonical and post-merge synchronized")
    print("MAIN=controller+researcher; FULL178=stage32-01-178-mainbatch; EX5=stage32ex5-mainbatch")
    print("parallel_child_lanes=HISTORICAL_ONLY_BY_DEFAULT")


if __name__ == "__main__":
    main()
