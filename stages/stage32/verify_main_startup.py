#!/usr/bin/env python3
from __future__ import annotations

import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
START = HERE / "MAIN-START-HERE.md"
COMMANDS = HERE / "COMMANDS.md"
AUTHORITY_VERIFIER = HERE / "verify_main_startup_authority_v15.py"


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    startup = START.read_text(encoding="utf-8")
    commands = COMMANDS.read_text(encoding="utf-8")

    req("Ordinary `stage32mainbatch` reads, in this order:" in startup,
        "canonical MAIN startup command missing")
    req("stages/stage32/COMMANDS.md" in startup,
        "canonical command registry missing from MAIN startup")
    req("controller and researcher" in startup.lower(),
        "MAIN controller+researcher role missing")
    req("only the paths listed in `MAIN-STATE.json.current_leaf_working_set`" in startup,
        "bounded startup working-set rule missing")
    req("Do not merge without explicit user authorization." in startup,
        "merge firewall missing")
    for stale in ("`Stage32-main-batch`", "`stage32main batch`", "`stage32 mainbatch`"):
        req(stale not in startup, f"stale MAIN alias retained in live startup: {stale}")

    for token in (
        "stage32mainbatch",
        "stage32audit",
        "stage32-01-178-mainbatch",
        "stage32-01-178-audit",
        "stage32ex5-mainbatch",
        "stage32ex5-audit",
    ):
        req(token in commands, f"canonical command missing from registry: {token}")

    # V15 is the live startup authority after the hostile-audited CUT195 wave3
    # was composed against hostile-reaudited V14 authority, proved disjoint
    # from N357/current consumed cuts, and consumed as a bounded numerical
    # pruning increment. The V15 replacement head still requires its own
    # hostile re-audit before any further MAIN promotion.
    runpy.run_path(str(AUTHORITY_VERIFIER), run_name="__main__")

    runpy.run_path(str(HERE / "verify_command_surface.py"), run_name="__main__")
    print("PASS Stage32 canonical startup command surface")


if __name__ == "__main__":
    main()
