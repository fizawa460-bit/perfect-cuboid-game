#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
EX5 = REPO / "stages" / "stage32-ex5"
ARCH_EX5 = EX5 / "archive" / "startup-surface-20260914"
ARCH = HERE / "proof" / "historical-routing-blobs"
LANES = HERE / "proof" / "LANE-ADAPTERS.json"
OLD_COMMANDS = ARCH / "COMMANDS-PRE-EX5-STARTUP-COLLAPSE.md"
OLD_VERIFIER = ARCH / "VERIFY-COMMAND-SURFACE-PRE-EX5-STARTUP-COLLAPSE.py"
OLD_MAIN_START = ARCH / "MAIN-START-HERE-PRE-ACTIVE-SPECIALIST-MONITOR.md"
TMP_VERIFIER = HERE / ".verify_command_surface_pre_ex5_startup_collapse.py"
LEGACY_EX5_START = EX5 / "MAIN-START-HERE.md"
LIVE_MAIN_START = HERE / "MAIN-START-HERE.md"
FIB_RUNKEY = REPO / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/runkeys/000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
FIB_WORKFLOW = REPO / ".github/workflows/stage32-mb-fib-isotropic-shell-pilot.yml"
FIB_PREFLIGHT_VERIFIER = REPO / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_000707_fibration_isotropic_shells_preflight.py"

OLD_COMMANDS_BLOB = "8837f7ca1963e73bf5b91c3cbdbc4625341aa469"
OLD_VERIFIER_BLOB = "bfe5fefce877eb0c819f04798fc72957eddedadd"
OLD_MAIN_START_BLOB = "2b659d7e7bde120de764de8b2c260faefe78a18e"
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
        "stage32mb-mainbatch", "stage32mb-fib", "stage32mb-fib-audit", "stage32mb-audit",
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

    fib_rows = [row for row in lanes["lanes"] if row.get("lane") == "MB-FIB"]
    req(len(fib_rows) == 0, "MB-FIB must remain outside the Stage32 claim-lane adapter registry")

    fib_state = json.loads((REPO / "stages/stage32/final-chain/32-03-multibranch/fib/STATE.json").read_text(encoding="utf-8"))
    req(fib_state["schema"] == "STAGE32_MB_FIB_STATE_V1", "MB-FIB state schema drift")
    req(fib_state["command"] == "stage32mb-fib", "MB-FIB command drift")
    req(fib_state["audit_command"] == "stage32mb-fib-audit", "MB-FIB audit command drift")
    req(fib_state["command_modes"]["audit"]["invocation"] == "stage32mb-fib-audit", "MB-FIB audit invocation drift")
    req(fib_state["consumer_lane"] == "MB", "MB-FIB consumer drift")
    req(fib_state["routing"]["registered_lane_adapter"] is False, "MB-FIB unexpectedly registered as claim lane")
    req(fib_state["routing"]["ordinary_mb_mainbatch_preloads_this_lane"] is False, "MB-FIB leaked into ordinary MB startup")
    req(fib_state["routing"]["fib_freeze_blocks_mb_mainbatch"] is False, "MB-FIB freeze incorrectly blocks MB mainbatch")
    fib_key = json.loads(FIB_RUNKEY.read_text(encoding="utf-8"))
    req(fib_key["schema"] == "STAGE32_MB104_000707_FIBRATION_ISOTROPIC_SHELLS_RUNKEY_V1", "MB-FIB runkey schema drift")
    req(int(fib_state["execution"]["runkey_generation"]) == int(fib_key["generation"]), "MB-FIB STATE/runkey generation drift")
    req(blob(FIB_RUNKEY) == fib_state["imported_source"]["research_surface_runkey_git_blob"], "MB-FIB retained runkey blob drift")
    req(blob(FIB_WORKFLOW) == fib_state["imported_source"]["research_surface_workflow_git_blob"], "MB-FIB retained workflow blob drift")
    req(blob(FIB_PREFLIGHT_VERIFIER) == fib_state["imported_source"]["preflight_verifier_git_blob"], "MB-FIB preflight verifier blob drift")

    if fib_state["execution"]["heavy_armed"]:
        req(fib_state["execution"]["execution_authorized"] is True, "MB-FIB armed STATE lacks execution authorization")
        req(fib_key["armed"] is True and fib_key["mode"] == "RECOVERY" and int(fib_key["generation"]) >= 17, "MB-FIB armed recovery mode drift")
        req(fib_state["audit"]["status"] == "PASS", "MB-FIB armed without hostile-audit PASS")
        req(fib_key["execution_gate"]["hostile_audit_status"] == "PASS", "MB-FIB armed runkey lacks audit PASS")
        req(fib_key["execution_gate"]["hostile_audit_exact_head"] == fib_state["audit"]["audited_exact_head"], "MB-FIB audit exact-head drift")
        req(fib_key["execution_gate"]["hostile_audit_review_id"] == fib_state["audit"]["hostile_audit_review_id"], "MB-FIB audit receipt drift")
        req(fib_key["execution_gate"]["automatic_execution_authorized"] is True, "MB-FIB armed key lacks automatic authorization")
        req(fib_key["execution_gate"]["state_transition_recorded"] is True, "MB-FIB armed key lacks state transition")
        req(fib_key["execution_gate"]["current_head_execution_blocked"] is False, "MB-FIB armed key still blocked")
        req(fib_key["execution_gate"]["pilot_only"] is True, "MB-FIB armed outside pilot-only scope")
        req(fib_key["execution_gate"]["scaleout_authorized"] is False, "MB-FIB premature scaleout authorization")
    else:
        req(fib_state["execution"]["execution_authorized"] is False, "MB-FIB unarmed STATE execution authorization leak")
        req(fib_key["armed"] is False, "MB-FIB unarmed runkey drift")
        req(fib_key["execution_gate"]["automatic_execution_authorized"] is False, "MB-FIB unarmed key automatic authorization leak")
        req(fib_key["execution_gate"]["current_head_execution_blocked"] is True, "MB-FIB unarmed key unexpectedly unblocked")
        if fib_key["mode"] == "COLD":
            pass
        elif fib_key["mode"] == "RECOVERY":
            req(int(fib_key["generation"]) == 23, "MB-FIB disarmed RECOVERY is allowed only for consumed Gen23")
            req(fib_state["status"] == "GEN23_EXECUTED_PARTIAL_281_COMPLETE_30_TIMEOUT__DISARMED__ZERO_CREDIT", "MB-FIB Gen23 disarm STATE status drift")
            req(fib_state["execution"]["active_transition"] == "GEN23_RECOVERY_X60_SINGLETON_RESIDUAL62_EXECUTED__DISARMED", "MB-FIB Gen23 disarm transition drift")
            req(fib_key["execution_gate"]["release_scope"] == "GEN23_RELEASE_CONSUMED__NO_REPEAT_EXECUTION__SUCCESSOR_REQUIRES_NEW_SEMANTIC_ADVANCE_AND_AUDIT", "MB-FIB Gen23 release-consumed scope drift")
            req(int(fib_key["execution_gate"]["last_numerical_attempt_generation"]) == 23, "MB-FIB Gen23 last-attempt generation drift")
            req(int(fib_key["execution_gate"]["last_numerical_attempt_run_id"]) == 35663858139, "MB-FIB Gen23 last-attempt run drift")
            req(int(fib_state["execution"]["last_attempt"]["generation"]) == 23, "MB-FIB Gen23 STATE last-attempt generation drift")
            req(int(fib_state["execution"]["last_attempt"]["run_id"]) == 35663858139, "MB-FIB Gen23 STATE last-attempt run drift")
            req(int(fib_state["execution"]["last_attempt"]["complete_child_count"]) == 281, "MB-FIB Gen23 COMPLETE carry count drift")
            req(int(fib_state["execution"]["last_attempt"]["incomplete_child_count"]) == 30, "MB-FIB Gen23 residual timeout count drift")
        else:
            req(False, "MB-FIB unexpected unarmed mode")

    req(all(v is False for v in fib_state["credit_firewall"].values()), "MB-FIB credit firewall leak")

    state = json.loads((EX5 / "MAIN-STATE.json").read_text(encoding="utf-8"))
    req(state["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V5_POST_1765_MERGE", "EX5 retained V5 state drift")
    req(state["bootstrap"]["merge_authorized"] is False, "EX5 merge authorization leak")

    main_start = LIVE_MAIN_START.read_text(encoding="utf-8")
    req("ACTIVE-SPECIALIST-MONITOR-CONTRACT.json" in main_start,
        "MAIN startup missing active-specialist monitor contract")
    req("Mandatory live specialist sweep" in main_start,
        "MAIN startup missing mandatory live specialist sweep")
    req("S32.DEMAND.N398.178.MAIN.PARITY_SYNTHESIS.V1" in main_start,
        "MAIN startup missing N398 handoff route")
    req("PICARD64-PARITY-CROSS-LANE-SYNTHESIS-V1.json" in main_start,
        "MAIN startup missing parity synthesis boundary")

    req(blob(OLD_COMMANDS) == OLD_COMMANDS_BLOB, "pre-collapse COMMANDS snapshot drift")
    req(blob(OLD_VERIFIER) == OLD_VERIFIER_BLOB, "pre-collapse command verifier snapshot drift")
    req(blob(OLD_MAIN_START) == OLD_MAIN_START_BLOB, "pre-monitor MAIN startup snapshot drift")
    req(blob(ARCH_EX5 / "MAIN-START-HERE.md") == OLD_EX5_START_BLOB, "archived EX5 startup snapshot drift")

    live_commands = (HERE / "COMMANDS.md").read_bytes()
    live_main_start = LIVE_MAIN_START.read_bytes()
    old_start = LEGACY_EX5_START.read_bytes() if LEGACY_EX5_START.exists() else None
    old_tmp = TMP_VERIFIER.read_bytes() if TMP_VERIFIER.exists() else None
    try:
        (HERE / "COMMANDS.md").write_bytes(OLD_COMMANDS.read_bytes())
        LIVE_MAIN_START.write_bytes(OLD_MAIN_START.read_bytes())
        LEGACY_EX5_START.write_bytes((ARCH_EX5 / "MAIN-START-HERE.md").read_bytes())
        TMP_VERIFIER.write_bytes(OLD_VERIFIER.read_bytes())
        runpy.run_path(str(TMP_VERIFIER), run_name="__main__")
    finally:
        (HERE / "COMMANDS.md").write_bytes(live_commands)
        LIVE_MAIN_START.write_bytes(live_main_start)
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
    req(LIVE_MAIN_START.read_bytes() == live_main_start, "live MAIN startup restore failed")
    req(not LEGACY_EX5_START.exists() if old_start is None else LEGACY_EX5_START.read_bytes() == old_start,
        "retired EX5 startup leaked after compatibility replay")
    print("PASS: Stage32 shared command/startup contracts preserved; EX5 duplicate startup surface retired")
    print("PASS: current MAIN active-specialist monitor contract present")
    print("historical pre-collapse command/startup contract replayed transiently with no live-path resurrection")


if __name__ == "__main__":
    main()
