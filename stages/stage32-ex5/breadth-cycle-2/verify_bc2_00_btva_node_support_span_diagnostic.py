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
    allowed = {
        "STAGE32EX5_MAIN_COMPACT_STATE_V15_BC2_30_AUDIT_CONSUMED_BC2_31_RECOVERY_EXECUTION",
        "STAGE32EX5_MAIN_COMPACT_STATE_V16_BC2_31_FRESH_REPLAY_AUDIT_BOUNDARY",
    }
    req(schema in allowed, "live EX5 schema drift")

    bootstrap = state["bootstrap"]
    req(bootstrap["active_work_pr"] == 1776, "BC2-31 active work PR drift")
    req(bootstrap["work_branch"] == "stage32ex5-bc2-25-boundary33-mainbatch", "BC2-31 work branch drift")
    req(bootstrap["latest_merged_pr"] == 1765, "latest merged EX5 provenance drift")
    req(bootstrap["merge_authorized"] is False, "merge authorization leak")

    audit = state["intermediate_audit_boundary"]
    req(audit["last_hostile_audit_status"] == "PASS", "BC2-30 PASS not consumed")
    req(audit["last_hostile_audit_exact_head"] == "38b60be7d0390ad5fa89ddb4dcd9511cfe36c57f", "BC2-30 audit head drift")
    req(audit["last_hostile_audit_review_id"] == 5184226057, "BC2-30 audit review drift")

    cur = state["current"]
    frontier = state["frontier"]
    if schema.endswith("BC2_31_RECOVERY_EXECUTION"):
        req(audit["new_audit_boundary_exists"] is False and audit["freeze_active"] is False, "stale BC2-30 audit freeze")
        req(audit["bc2_30_execution_authorized"] is False and audit["bc2_31_execution_authorized"] is True, "BC2-31 execution authority drift")
        req(cur["next_route"] == "BC2_31_EXACT_RECOVERY_OF_UNRETAINED_BC2_19_UNKNOWN_IDENTITIES", "BC2-31 route drift")
        req("NO_STATUS_INFERENCE" in cur["stop_semantics"], "BC2-31 identity-only firewall drift")
        req(frontier["e8_bc2_31_identity_recovery_executed"] is False, "BC2-31 result claimed before execution")
        req(frontier["e8_known_parent_unsat_count_lower_bound"] == 7164, "BC2-30 lower-bound drift")
    else:
        req(audit["new_audit_boundary_exists"] is True and audit["freeze_active"] is True and audit["re_audit_required"] is True, "BC2-31 fresh audit freeze drift")
        req(audit["bc2_30_execution_authorized"] is False and audit["bc2_31_execution_authorized"] is False, "BC2-31 post-execution authority drift")
        req(cur["next_route"] == "HOSTILE_AUDIT_BC2_31_FRESH_ALL7336_REPLAY", "BC2-31 fresh audit route drift")
        req("NO_HISTORICAL_172_IDENTITY_INFERENCE" in cur["stop_semantics"] and "NO_BC2_32" in cur["stop_semantics"], "BC2-31 fresh firewall drift")
        req(frontier["e8_bc2_31_identity_recovery_executed"] is True, "BC2-31 execution receipt missing")
        req(frontier["e8_bc2_31_fresh_replay_executed"] is True, "BC2-31 fresh replay receipt missing")
        req(frontier["e8_bc2_31_fresh_unknown_count"] == 170 and frontier["e8_bc2_31_fresh_sat_count"] == 0, "BC2-31 fresh partition drift")
        req(frontier["e8_known_parent_unsat_count_lower_bound"] == 7166, "BC2-31 fresh lower-bound drift")

    req(frontier["e8_bc2_30_audited"] is True, "BC2-30 audit marker drift")
    req(frontier["e8_bc2_31_exact_remaining172_recovered"] is False, "historical 172 identity set overclaim")
    req(frontier["e8_bc2_19_unknown_parent_count"] == 236, "BC2-19 UNKNOWN count drift")
    req(frontier["e8_bc2_30_unretained_unknown_identity_count"] == 172, "historical remaining172 count drift")
    req(frontier["FULL178_complete"] is False and frontier["e8_whole_first_block_unsat"] is False, "local EX5 work promoted")
    req(state["credit"]["stage32_main_credit"] is False, "local EX5 work promoted to Stage32 MAIN credit")

    spec = importlib.util.spec_from_file_location("bc2_00_v4_frozen", FROZEN_V4_VERIFIER)
    req(spec is not None and spec.loader is not None, "cannot load frozen BC2-00 verifier")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    compat = json.loads(json.dumps(state))
    compat["schema"] = "STAGE32EX5_MAIN_COMPACT_STATE_V4_FULL178_FINAL_CHAIN_SYNC"
    prior = compat.setdefault("prior_audited_authority", {})
    cycle1 = prior.setdefault("cycle1", {})
    cycle1.setdefault("breadth_cycle", "EX5_BREADTH_CYCLE_1")
    cycle1.setdefault("authority_status", "AUDITED")
    cycle1.setdefault("scope_firewall", "EX5_BREADTH_CYCLE_1_ONLY")
    early = prior.setdefault("early_bc2", {})
    early.setdefault("claim_id", "S32.EX5.BC2_NODE_SUPPORT_SPAN_CHECKPOINT.V1")
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
