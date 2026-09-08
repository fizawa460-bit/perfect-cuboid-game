#!/usr/bin/env python3
"""Cheap structural verifier for Stage32EX5 MAIN-STATE.json.

This checks routing/credit firewalls through EX5-02 only. It does not prove
receiver closure, route qualification, or any mathematical claim.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE_PATH = HERE / "MAIN-STATE.json"

EXPECTED_TERMINALS = {
    "QUALIFIED_INDEPENDENT_STAGE32_ROUTE_ESTABLISHED",
    "FROZEN_BREADTH_PACKAGE_EXHAUSTED_WITHOUT_QUALIFIED_ROUTE",
}
EXPECTED_FAMILIES = {
    "EFFECTIVE_CONE_FIXED_COMPONENT_LANE",
    "EQUGENERIC_HILBERT_SEVERI_LANE",
    "MODULAR_UNIFORMIZATION_LANE",
    "GALOIS_DESCENT_LANE",
    "EXACT_ENUMERATION_LANE",
    "LOCAL_GLOBAL_SINGULARITY_LANE",
    "CROSS_STAGE_WEAPON_IMPORT_LANE",
}


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def main() -> None:
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))

    require(state.get("schema") == "STAGE32EX5_MAIN_COMPACT_STATE_V1_EX5_02_COMPLETE",
            "unexpected state schema")
    require(state.get("stage") == "32EX5", "wrong stage")
    execution = state["execution"]
    require(execution["main_command"] == "stage32ex5-mainbatch", "wrong main command")
    require(execution["audit_command"] == "stage32ex5-audit", "wrong audit command")

    completion = state["completion_contract"]
    require(set(completion["allowed_terminal_outcomes"]) == EXPECTED_TERMINALS,
            "terminal outcome contract mismatch")
    require(completion["EX5_route_decision_closure_is_Stage32_full_target_closure"] is False,
            "EX5 closure must not equal Stage32 closure")
    require(completion["qualified_route_requires_retained_nontrivial_receiver_effect"] is True,
            "qualified route must require a retained receiver effect")
    require(completion["bounded_exhaustion_is_global_no_route_theorem"] is False,
            "bounded exhaustion must remain bounded")

    families = state["route_families"]
    require(set(families["required_initial_families"]) == EXPECTED_FAMILIES,
            "route-family set mismatch")
    require(families["scratch_results_authoritative"] is False,
            "scratch results cannot be authoritative")
    require(families["candidate_universe_version"] is None,
            "EX5-03 candidate universe cannot be pre-frozen")

    receiver = state["receiver_contract"]
    require(receiver["frozen_version"] == "EX5_RECEIVER_TARGET_CONTRACT_V1",
            "EX5 frozen receiver contract missing")
    require(receiver["source_lock_artifact"] ==
            "stages/stage32-ex5/ex5-00-source-lock-target-contract.json",
            "EX5-00 artifact path mismatch")
    require(receiver["receiver_ledger_artifact"] ==
            "stages/stage32-ex5/ex5-01-exact-receiver-ledger.json",
            "EX5-01 ledger path mismatch")
    require(receiver["coverage_graph_artifact"] ==
            "stages/stage32-ex5/ex5-02-current-coverage-dependency-graph.json",
            "EX5-02 graph path mismatch")
    require(receiver["unibranch_degree_row_count"] == 183, "unibranch row count drift")
    require(receiver["row_count"] == 185, "receiver ledger row count drift")
    require(receiver["coverage_checksum"] ==
            "3a700ed40b5d0e6bf212f569ed85279a15ac90bb8a87a96e61f01729ffa0ca95",
            "receiver coverage checksum drift")
    require(receiver["status_counts"] == {
        "CLOSED": 5, "OPEN": 180, "UNKNOWN": 0, "CONDITIONAL": 0, "OUT_OF_SCOPE": 0
    }, "receiver status counts drift")
    require(receiver["coverage_graph_canonical_sha256"] ==
            "7d1f3c6fa3ec2f1b8f15690ca50efc5ab2b826a20d741659cfaf867431afa4f0",
            "coverage graph canonical drift")
    require(receiver["coverage_graph_primary_open_mapping_count"] == 180,
            "coverage graph open mapping count drift")
    require(receiver["coverage_graph_special_v6_overlay_row_count"] == 1,
            "coverage graph special overlay count drift")
    for key in ("source_lock_complete", "receiver_ledger_complete",
                "receiver_ledger_coverage_certified",
                "current_coverage_dependency_graph_complete"):
        require(receiver[key] is True, f"receiver contract incomplete: {key}")
    require(receiver["chat_or_memory_counts_treated_as_authority"] is False,
            "chat/memory cannot define receiver authority")
    require(receiver["V6_O210_Q602_treated_as_definition_of_all_receivers"] is False,
            "V6/O210/Q602 cannot define all receivers")

    discovery = state["asset_discovery"]
    require(discovery["clean_room_generation_must_precede_asset_solution_lookup"] is True,
            "clean-room ordering lost")
    require(discovery["trigger_leaf"] == "EX5-04_REPOSITORY_ASSET_DISCOVERY_AND_DEDUPLICATION",
            "asset discovery trigger drift")

    bootstrap = state["bootstrap"]
    require(bootstrap["merge_authorized"] is False, "merge must not be authorized")
    require(bootstrap["active_work_pr"] == 1710, "wrong active EX5 work PR")

    frontier = state["frontier"]
    for key in ("EX5_00_source_lock_complete", "receiver_population_contract_complete",
                "receiver_ledger_complete", "receiver_ledger_coverage_certified",
                "current_coverage_dependency_graph_complete"):
        require(frontier[key] is True, f"frontier flag must be complete: {key}")
    for key in ("clean_room_candidate_universe_frozen", "arsenal_dedup_complete",
                "route_scorecard_complete", "primary_route_selected",
                "primary_microdiagnostic_complete", "nontrivial_receiver_effect_obtained",
                "qualified_independent_route_established", "frozen_breadth_package_exhausted",
                "audit_ready_EX5_route_decision_closure", "EX5_route_decision_closure"):
        require(frontier[key] is False, f"future frontier flag pre-credited: {key}")

    current = state["current"]
    require(current["status"] == "EX5_02_CURRENT_COVERAGE_DEPENDENCY_GRAPH_COMPLETE_UNAUDITED_RETAINED",
            "wrong retained EX5-02 status")
    require(current["leaf"] == "EX5-03_CLEAN_ROOM_MATERIALLY_DISTINCT_ROUTE_GENERATION",
            "EX5-02 completion must route to EX5-03")

    working = state["current_leaf_working_set"]
    for path in (
        "stages/stage32-ex5/ex5-00-source-lock-target-contract.json",
        "stages/stage32-ex5/ex5-01-exact-receiver-ledger.json",
        "stages/stage32-ex5/ex5-02-current-coverage-dependency-graph.json",
        "stages/stage32-ex5/verify_ex5_02_coverage_graph.py",
    ):
        require(path in working, f"EX5-03 working set missing {path}")

    require(state["credit"]["level"] == "EX5_02_COVERAGE_TOPOLOGY_ONLY_NO_MATHEMATICAL_CREDIT",
            "credit level drift")
    require(state["audit"]["status"] == "NOT_READY_INTERMEDIATE_EX5_02_UNAUDITED",
            "audit readiness drift")

    firewalls = state["firewalls"]
    for key, value in firewalls.items():
        require(value is False, f"firewall {key} must remain false")

    print("PASS: Stage32EX5 MAIN state structural/firewall contract through EX5-02")


if __name__ == "__main__":
    main()
