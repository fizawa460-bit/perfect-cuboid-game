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
    schema = state["schema"]
    req(schema in {
        "STAGE32EX5_MAIN_COMPACT_STATE_V5_POST_1765_MERGE",
        "STAGE32EX5_MAIN_COMPACT_STATE_V6_BC2_25_AUDIT_BOUNDARY",
        "STAGE32EX5_MAIN_COMPACT_STATE_V7_BC2_25_AUDIT_CONSUMED_BC2_26_PREFLIGHT",
    }, "live EX5 schema drift")

    bootstrap = state["bootstrap"]
    if schema.endswith("V5_POST_1765_MERGE"):
        req(bootstrap["active_work_pr"] is None and bootstrap["work_branch"] is None,
            "merged #1765 leaked forward as active work surface")
        req(state["current"]["next_route"] == "BC2_25_POST_MERGE_UNKNOWN_REFINEMENT_PREFLIGHT",
            "post-merge BC2-25 route drift")
    elif schema.endswith("V6_BC2_25_AUDIT_BOUNDARY"):
        req(bootstrap["active_work_pr"] == 1776 and bootstrap["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch",
            "BC2-25 active work surface drift")
        req(state["current"]["next_route"] == "HOSTILE_AUDIT_BC2_25_RECHECK",
            "BC2-25 audit-first route drift")
        req(state["intermediate_audit_boundary"]["new_audit_boundary_exists"] is True,
            "BC2-25 audit boundary missing")
        req(state["intermediate_audit_boundary"]["bc2_26_execution_authorized"] is False,
            "BC2-26 authorization leak")
    else:
        req(bootstrap["active_work_pr"] == 1776 and bootstrap["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch",
            "BC2-26 active work surface drift")
        req(state["current"]["next_route"] == "BC2_26_BOUNDARY34_PARTITION_BOUNDED",
            "BC2-26 bounded route drift")
        audit = state["intermediate_audit_boundary"]
        req(audit["last_hostile_audit_status"] == "PASS" and audit["last_hostile_audit_review_id"] == 5177354131,
            "BC2-25 PASS receipt not consumed")
        req(audit["new_audit_boundary_exists"] is False and audit["bc2_26_execution_authorized"] is True,
            "BC2-26 bounded authorization drift")

    req(bootstrap["latest_merged_pr"] == 1765,
        "latest merged EX5 PR provenance drift")
    req(bootstrap["merge_authorized"] is False,
        "historical merge authorization leaked forward")
    req(state["frontier"]["FULL178_complete"] is False,
        "local EX5 work promoted to FULL178 closure")
    req(state["credit"]["stage32_main_credit"] is False,
        "local EX5 work promoted to Stage32 MAIN credit")

    spec = importlib.util.spec_from_file_location("bc2_00_v4_frozen", FROZEN_V4_VERIFIER)
    req(spec is not None and spec.loader is not None, "cannot load frozen BC2-00 verifier")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    compat = json.loads(json.dumps(state))
    compat["schema"] = "STAGE32EX5_MAIN_COMPACT_STATE_V4_FULL178_FINAL_CHAIN_SYNC"
    cycle1 = compat.setdefault("prior_audited_authority", {}).setdefault("cycle1", {})
    cycle1.setdefault("breadth_cycle", "EX5_BREADTH_CYCLE_1")
    cycle1.setdefault("scope_firewall", "EX5_BREADTH_CYCLE_1_ONLY")
    frontier = compat.setdefault("frontier", {})
    frontier.setdefault("runtime_exceptional_index_to_projective_node_bridge_complete", True)

    class StateCompatProxy:
        def read_text(self, *args, **kwargs):
            return json.dumps(compat)

    module.MAIN_STATE = StateCompatProxy()
    module.main()
    print(f"PASS BC2-00 historical replay under live EX5 schema {schema}")


if __name__ == "__main__":
    main()
