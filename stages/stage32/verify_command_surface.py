#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
EX5 = REPO / "stages" / "stage32-ex5"
BRIDGE = HERE / "generalization-bridge"
ARCH_EX5 = EX5 / "archive" / "startup-surface-20260914"
ARCH = HERE / "proof" / "historical-routing-blobs"
LANES = HERE / "proof" / "LANE-ADAPTERS.json"
OLD_COMMANDS = ARCH / "COMMANDS-PRE-EX5-STARTUP-COLLAPSE.md"
OLD_VERIFIER = ARCH / "VERIFY-COMMAND-SURFACE-PRE-EX5-STARTUP-COLLAPSE.py"
TMP_VERIFIER = HERE / ".verify_command_surface_pre_ex5_startup_collapse.py"
LEGACY_EX5_START = EX5 / "MAIN-START-HERE.md"

OLD_COMMANDS_BLOB = "8837f7ca1963e73bf5b91c3cbdbc4625341aa469"
OLD_VERIFIER_BLOB = "bfe5fefce877eb0c819f04798fc72957eddedadd"
OLD_EX5_START_BLOB = "47581a734da21dac3d2cabc4dc520d5be1310a49"
RETIRED = (
    "README.md",
    "MAIN-START-HERE.md",
    "MAINBATCH-OPERATIONS.md",
    "CROSS-LANE-STATE.json",
    "CURRENT-ROADMAP.md",
    "CURRENT-AUDIT-CONTRACT.md",
    "AUDIT-CONTRACT.md",
)


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit(f"FAIL: {msg}")


def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> None:
    commands = (HERE / "COMMANDS.md").read_text(encoding="utf-8")
    for token in (
        "stage32mainbatch", "stage32audit",
        "stage32-01-178-mainbatch", "stage32-01-178-audit",
        "stage32ex5-mainbatch", "stage32ex5-audit",
        "stage32cut-mainbatch", "stage32cut-audit",
        "stage32mb-mainbatch", "stage32mb-audit",
        "stage32bridge-mainbatch", "stage32bridge-audit",
    ):
        req(token in commands, f"canonical command missing: {token}")
    req("Lane startup entrypoints are resolved by `stages/stage32/proof/LANE-ADAPTERS.json`" in commands,
        "command registry missing lane startup authority")
    req("Stage32EX5 is intentionally collapsed to `stages/stage32-ex5/MAIN-STATE.json`" in commands,
        "command registry missing EX5 startup collapse")
    req("not a second startup contract" in commands, "command registry still acts as startup contract")
    req("## Stable startup invariants" not in commands and "Before substantive work, every active `*-mainbatch`" not in commands,
        "command registry reintroduced duplicate startup procedure")

    req(all(not (EX5 / name).exists() for name in RETIRED),
        "retired EX5 startup surface leaked back into live stage root")
    req(all((ARCH_EX5 / name).is_file() for name in RETIRED),
        "retired EX5 startup surface missing from archive")

    lanes = json.loads(LANES.read_text(encoding="utf-8"))
    rows = [row for row in lanes["lanes"] if row.get("lane") == "EX5"]
    req(len(rows) == 1, "EX5 lane adapter missing or duplicated")
    ex5 = rows[0]
    req(ex5["state_path"] == "stages/stage32-ex5/MAIN-STATE.json", "EX5 state path drift")
    req(ex5["startup_path"] == "stages/stage32-ex5/MAIN-STATE.json", "EX5 startup path not collapsed")
    req(ex5["demand_state_path"] is None, "EX5 stale local demand mirror still live")

    bridge_rows = [row for row in lanes["lanes"] if row.get("lane") == "BRIDGE"]
    req(len(bridge_rows) == 1, "BRIDGE lane adapter missing or duplicated")
    bridge = bridge_rows[0]
    req(bridge["state_path"] == "stages/stage32/generalization-bridge/STATE.json", "BRIDGE state path drift")
    req(bridge["startup_path"] == "stages/stage32/generalization-bridge/MAIN-START-HERE.md", "BRIDGE startup path drift")
    req(bridge["demand_state_path"] is None, "BRIDGE unexpected local demand mirror")
    req(bridge["lane_status"] == "ACTIVE_GENERALIZATION_FEASIBILITY_SPECIALIST", "BRIDGE lane status drift")
    req(bridge["demand_role"] == "ROUTABLE", "BRIDGE demand role drift")
    req(bridge["active_frontier_refs"] == ["S32.FULL178.NUMERICAL_CENSUS.V1"], "BRIDGE frontier drift")

    bridge_mission = json.loads((BRIDGE / "MISSION.json").read_text(encoding="utf-8"))
    req(bridge_mission["status"] == "ACTIVE", "BRIDGE mission unexpectedly inactive")
    req(bridge_mission["operator_commands"]["main"] == "stage32bridge-mainbatch", "BRIDGE command drift")
    req(bridge_mission["operator_commands"]["audit"] == "stage32bridge-audit", "BRIDGE audit command drift")
    req(bridge_mission["routing"]["authority"] == "stages/stage32/MAIN-STATE.json", "BRIDGE routing authority drift")
    req(bridge_mission["routing"]["current_main_credit_auto_promotion"] is False, "BRIDGE self-promotion enabled")
    req(bridge_mission["route_safety"]["terminal_by_terminal_fallback_forbidden"] is True,
        "BRIDGE top-down anti-fallback rule missing")
    req(bridge_mission["credit_firewall"]["stage32_main_pruning_credit"] is False,
        "BRIDGE mission starts with MAIN credit")

    bridge_state = json.loads((BRIDGE / "STATE.json").read_text(encoding="utf-8"))
    req(bridge_state["current_node"] == "BR101", "BRIDGE initial node drift")
    req(bridge_state["routing"]["source_lane_authority_mutation"] is False,
        "BRIDGE may mutate source-lane authority")
    req(bridge_state["routing"]["main_credit_auto_promotion"] is False,
        "BRIDGE state self-promotion enabled")
    req(bridge_state["routing"]["terminal_by_terminal_fallback_forbidden"] is True,
        "BRIDGE state lost top-down anti-fallback rule")
    req(bridge_state["credit_firewall"]["merge_authorized"] is False,
        "BRIDGE merge authorization leak")
    bridge_start = (BRIDGE / "MAIN-START-HERE.md").read_text(encoding="utf-8")
    req("stage32bridge-mainbatch" in bridge_start and "CROSS-LANE-DEMANDS.json" in bridge_start,
        "BRIDGE demand-aware startup missing")
    req("NO GENERALIZATION" in bridge_start, "BRIDGE no-go path missing")
    req("terminal-by-terminal" in bridge_start, "BRIDGE anti-local fallback boundary missing")

    state = json.loads((EX5 / "MAIN-STATE.json").read_text(encoding="utf-8"))
    req(state["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V5_POST_1765_MERGE", "EX5 retained V5 state drift")
    req(state["bootstrap"]["merge_authorized"] is False, "EX5 merge authorization leak")

    req(blob(OLD_COMMANDS) == OLD_COMMANDS_BLOB, "pre-collapse COMMANDS snapshot drift")
    req(blob(OLD_VERIFIER) == OLD_VERIFIER_BLOB, "pre-collapse command verifier snapshot drift")
    req(blob(ARCH_EX5 / "MAIN-START-HERE.md") == OLD_EX5_START_BLOB, "archived EX5 startup snapshot drift")

    live_commands = (HERE / "COMMANDS.md").read_bytes()
    old_start = LEGACY_EX5_START.read_bytes() if LEGACY_EX5_START.exists() else None
    old_tmp = TMP_VERIFIER.read_bytes() if TMP_VERIFIER.exists() else None
    try:
        (HERE / "COMMANDS.md").write_bytes(OLD_COMMANDS.read_bytes())
        LEGACY_EX5_START.write_bytes((ARCH_EX5 / "MAIN-START-HERE.md").read_bytes())
        TMP_VERIFIER.write_bytes(OLD_VERIFIER.read_bytes())
        runpy.run_path(str(TMP_VERIFIER), run_name="__main__")
    finally:
        (HERE / "COMMANDS.md").write_bytes(live_commands)
        if old_start is None:
            if LEGACY_EX5_START.exists():
                LEGACY_EX5_START.unlink()
        else:
            LEGACY_EX5_START.write_bytes(old_start)
        if old_tmp is None:
            if TMP_VERIFIER.exists():
                TMP_VERIFIER.unlink()
        else:
            TMP_VERIFIER.write_bytes(old_tmp)

    req((HERE / "COMMANDS.md").read_bytes() == live_commands, "live COMMANDS restore failed")
    req(not LEGACY_EX5_START.exists() if old_start is None else LEGACY_EX5_START.read_bytes() == old_start,
        "retired EX5 startup leaked after compatibility replay")
    print("PASS: Stage32 shared command/startup contracts preserved; EX5 collapse and BRIDGE enrollment verified")
    print("historical pre-collapse command contract replayed transiently with no live-path resurrection")


if __name__ == "__main__":
    main()
