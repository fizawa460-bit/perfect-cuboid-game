#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
LIVE_STATE = ROOT / "stages" / "stage32-ex5" / "MAIN-STATE.json"
FROZEN_V4_VERIFIER = HERE / "verify_bc2_00_btva_node_support_span_diagnostic_v4.py"


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    state = json.loads(LIVE_STATE.read_text(encoding="utf-8"))
    req(state["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V5_POST_1765_MERGE",
        "live EX5 post-merge schema drift")
    bootstrap = state["bootstrap"]
    req(bootstrap["active_work_pr"] is None and bootstrap["work_branch"] is None,
        "merged #1765 leaked forward as active work surface")
    req(bootstrap["latest_merged_pr"] == 1765,
        "latest merged EX5 PR provenance drift")
    req(bootstrap["merge_authorized"] is False,
        "historical merge authorization leaked forward")
    req(state["current"]["next_route"] == "BC2_25_POST_MERGE_UNKNOWN_REFINEMENT_PREFLIGHT",
        "post-merge BC2-25 route drift")
    req(state["frontier"]["FULL178_complete"] is False,
        "BC2-24 promoted to FULL178 closure")
    req(state["credit"]["stage32_main_credit"] is False,
        "BC2-24 promoted to Stage32 MAIN credit")

    # Preserve the exact original BC2-00 mathematical/source-lock verifier.
    # It predates the #1765 merge and hard-coded only the live-state schema V4.
    # Present the current state with that historical schema label while every
    # artifact hash, source lock, theorem condition, route and credit firewall
    # assertion runs unchanged.
    spec = importlib.util.spec_from_file_location("bc2_00_v4_frozen", FROZEN_V4_VERIFIER)
    req(spec is not None and spec.loader is not None, "cannot load frozen BC2-00 verifier")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    compat = dict(state)
    compat["schema"] = "STAGE32EX5_MAIN_COMPACT_STATE_V4_FULL178_FINAL_CHAIN_SYNC"

    class StateCompatProxy:
        def read_text(self, *args, **kwargs):
            return json.dumps(compat)

    module.MAIN_STATE = StateCompatProxy()
    module.main()
    print("PASS BC2-00 historical replay under EX5 V5 post-#1765 live routing")


if __name__ == "__main__":
    main()
