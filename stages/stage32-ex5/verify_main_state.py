#!/usr/bin/env python3
"""Cheap structural verifier for Stage32EX5 MAIN-STATE.json through EX5-06.

This checks routing/credit firewalls only. It does not execute EX5-07, qualify a
route, discharge a receiver, or grant mathematical/Stage32 MAIN credit.
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
EXPECTED_DEDUP_IDS = ["EX5R-EFC-001","EX5R-EHS-001","EX5R-MOD-001","EX5R-LGS-001","EX5R-XSTAGE-001"]


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def main() -> None:
    state = json.loads(STATE_PATH.read_text())
    require(state["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V1_EX5_06_COMPLETE", "unexpected state schema")
    require(state["stage"] == "32EX5", "wrong stage")
    require(state["execution"]["main_command"] == "stage32ex5-mainbatch", "wrong main command")
    require(state["execution"]["audit_command"] == "stage32ex5-audit", "wrong audit command")

    completion = state["completion_contract"]
    require(set(completion["allowed_terminal_outcomes"]) == EXPECTED_TERMINALS, "terminal outcome contract mismatch")
    require(completion["EX5_route_decision_closure_is_Stage32_full_target_closure"] is False, "EX5 closure must not equal Stage32 closure")
    require(completion["qualified_route_requires_retained_nontrivial_receiver_effect"] is True, "qualified route requires receiver effect")
    require(completion["bounded_exhaustion_is_global_no_route_theorem"] is False, "bounded exhaustion must remain bounded")
    require(completion["route_score_table_is_terminal_success"] is False, "score table cannot be terminal success")

    families = state["route_families"]
    require(set(families["required_initial_families"]) == EXPECTED_FAMILIES, "route-family set mismatch")
    require(families["candidate_universe_version"] == "EX5_CLEANROOM_CANDIDATES_V1", "candidate universe drift")
    require((families["family_record_count"], families["generated_candidate_count"], families["semantically_irrelevant_family_count"]) == (7,6,1), "candidate counts drift")
    require(families["dedup_universe_version"] == "EX5_DEDUP_CANDIDATES_V1", "dedup universe drift")
    require(families["deduplicated_candidate_ids"] == EXPECTED_DEDUP_IDS, "dedup ids drift")
    require(families["removed_or_rejected_candidate_ids"] == ["EX5R-GAL-001","EX5R-ENUM-001"], "removed ids drift")
    require(families["scorecard_artifact"] == "stages/stage32-ex5/ex5-05-route-scorecard.json", "scorecard path drift")
    require(families["execution_contract_version"] == "EX5_EXECUTABLE_ROUTE_CONTRACTS_V1", "EX5-06 contract version drift")
    require(families["execution_contract_artifact"] == "stages/stage32-ex5/ex5-06-executable-route-contracts.json", "EX5-06 artifact drift")
    require(families["execution_contract_verifier"] == "stages/stage32-ex5/verify_ex5_06_executable_route_contracts.py", "EX5-06 verifier drift")
    require(families["primary_route_id"] == "EX5R-XSTAGE-001", "primary route drift")
    require(families["backup_route_ids"] == ["EX5R-EFC-001","EX5R-EHS-001"], "backup routes drift")
    require(families["reserve_route_ids"] == ["EX5R-LGS-001","EX5R-MOD-001"], "reserve routes drift")
    require(families["first_microdiagnostic_unit"] == "XSTAGE-PREFLIGHT-01", "first unit drift")
    require(families["scratch_results_authoritative"] is False, "scratch cannot be authoritative")

    receiver = state["receiver_contract"]
    require(receiver["unibranch_degree_row_count"] == 183, "unibranch row count drift")
    require(receiver["row_count"] == 185, "receiver row count drift")
    require(receiver["coverage_checksum"] == "3a700ed40b5d0e6bf212f569ed85279a15ac90bb8a87a96e61f01729ffa0ca95", "coverage checksum drift")
    require(receiver["coverage_graph_canonical_sha256"] == "7d1f3c6fa3ec2f1b8f15690ca50efc5ab2b826a20d741659cfaf867431afa4f0", "coverage graph drift")
    require(receiver["status_counts"] == {"CLOSED":5,"OPEN":180,"UNKNOWN":0,"CONDITIONAL":0,"OUT_OF_SCOPE":0}, "status counts drift")
    require(receiver["V6_O210_Q602_treated_as_definition_of_all_receivers"] is False, "V6 cannot define all receivers")

    discovery = state["asset_discovery"]
    for key in ("repository_asset_discovery_performed","arsenal_index_read","deduplication_performed"):
        require(discovery[key] is True, f"EX5-04 flag lost: {key}")
    require(discovery["index_inspection_mode"] == "RUNNER_SIDE_MACHINE_REGISTRY_VALIDATION_DUE_CONTEXT_GATE", "index mode drift")
    require(discovery["arsenal_index_byte_size"] == 101763, "Arsenal index size drift")
    require(discovery["arsenal_index_whole_fetched_into_chat"] is False, "large index cannot be whole-fetched")

    bootstrap = state["bootstrap"]
    require(bootstrap["merge_authorized"] is False, "merge must remain unauthorized")
    require(bootstrap["active_work_pr"] == 1710, "wrong PR")
    require(bootstrap["base_main_sha"] == "f2a89e613cdf91191a0aada9e90c9fc93373a6c6", "fresh main sync drift")

    frontier = state["frontier"]
    for key in ("EX5_00_source_lock_complete","receiver_population_contract_complete","receiver_ledger_complete","receiver_ledger_coverage_certified","current_coverage_dependency_graph_complete","clean_room_candidate_universe_frozen","arsenal_dedup_complete","route_scorecard_complete","primary_route_selected","executable_route_contracts_complete"):
        require(frontier[key] is True, f"frontier flag must be complete: {key}")
    require(frontier["backup_route_count"] == 2, "backup count drift")
    for key in ("primary_microdiagnostic_complete","nontrivial_receiver_effect_obtained","qualified_independent_route_established","frozen_breadth_package_exhausted","audit_ready_EX5_route_decision_closure","EX5_route_decision_closure"):
        require(frontier[key] is False, f"future frontier precredited: {key}")
    require(frontier["terminal_outcome"] is None, "terminal outcome cannot be set")

    current = state["current"]
    require(current["status"] == "EX5_06_EXECUTABLE_ROUTE_CONTRACTS_COMPLETE_UNAUDITED_RETAINED", "wrong EX5-06 status")
    require(current["leaf"] == "EX5-07_PRIMARY_ROUTE_MICRODIAGNOSTIC", "EX5-06 must route to EX5-07")
    require(current["subroute"] == "EXECUTE_XSTAGE_PREFLIGHT_01_FIELD_OBJECT_POPULATION_ADAPTER_GATE_ONLY", "EX5-07 subroute drift")
    require(current["next_route_on_block"] == "EX5R-EFC-001", "XSTAGE block must move to EFC")

    require(state["current_leaf_working_set"] == [
        "stages/stage32-ex5/ex5-06-executable-route-contracts.json",
        "stages/stage32-ex5/verify_ex5_06_executable_route_contracts.py",
        "stages/stage32-ex5/ex5-05-route-scorecard.json",
        "stages/stage32-ex5/ex5-01-exact-receiver-ledger.json",
        "docs/arsenal/cards/formal/S34-W03.md",
    ], "EX5-07 working set drift")

    require(state["credit"]["level"] == "EX5_06_EXECUTABLE_CONTRACTS_ONLY_NO_MATHEMATICAL_CREDIT", "credit level drift")
    require(state["audit"]["status"] == "NOT_READY_INTERMEDIATE_EX5_06_UNAUDITED", "audit status drift")
    for key, value in state["firewalls"].items():
        require(value is False, f"firewall {key} must remain false")

    print("PASS: Stage32EX5 MAIN state structural/firewall contract through EX5-06")


if __name__ == "__main__":
    main()
