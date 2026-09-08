#!/usr/bin/env python3
"""Cheap structural verifier for Stage32EX5 MAIN-STATE.json through EX5-03.

This checks routing/credit firewalls only. It does not qualify a route, discharge
a receiver, or grant mathematical/Stage32 MAIN credit.
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
    require(state["schema"] == "STAGE32EX5_MAIN_COMPACT_STATE_V1_EX5_03_COMPLETE",
            "unexpected state schema")
    require(state["stage"] == "32EX5", "wrong stage")
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
    require(families["candidate_universe_version"] == "EX5_CLEANROOM_CANDIDATES_V1",
            "candidate universe not frozen")
    require(families["candidate_universe_artifact"] ==
            "stages/stage32-ex5/ex5-03-clean-room-route-universe.json",
            "EX5-03 artifact path drift")
    require(families["candidate_universe_verifier"] ==
            "stages/stage32-ex5/verify_ex5_03_clean_room_routes.py",
            "EX5-03 verifier path drift")
    require((families["family_record_count"], families["generated_candidate_count"],
             families["semantically_irrelevant_family_count"]) == (7, 6, 1),
            "EX5-03 candidate counts drift")
    require(families["primary_route_id"] is None and families["backup_route_ids"] == [],
            "EX5-05 route selection cannot be pre-credited")
    require(families["scratch_results_authoritative"] is False,
            "scratch results cannot be authoritative")

    receiver = state["receiver_contract"]
    require(receiver["unibranch_degree_row_count"] == 183, "unibranch row count drift")
    require(receiver["row_count"] == 185, "receiver ledger row count drift")
    require(receiver["coverage_checksum"] ==
            "3a700ed40b5d0e6bf212f569ed85279a15ac90bb8a87a96e61f01729ffa0ca95",
            "receiver coverage checksum drift")
    require(receiver["coverage_graph_canonical_sha256"] ==
            "7d1f3c6fa3ec2f1b8f15690ca50efc5ab2b826a20d741659cfaf867431afa4f0",
            "coverage graph canonical drift")
    require(receiver["status_counts"] == {
        "CLOSED": 5, "OPEN": 180, "UNKNOWN": 0, "CONDITIONAL": 0, "OUT_OF_SCOPE": 0
    }, "receiver status counts drift")
    require(receiver["V6_O210_Q602_treated_as_definition_of_all_receivers"] is False,
            "V6/O210/Q602 cannot define all receivers")

    discovery = state["asset_discovery"]
    require(discovery["policy_path"] == "docs/research-os/policies/repository-asset-discovery.md",
            "asset discovery policy path drift")
    require(discovery["arsenal_index_path"] == "docs/arsenal/index.json",
            "Arsenal index path drift")
    require(discovery["trigger_leaf"] == "EX5-04_REPOSITORY_ASSET_DISCOVERY_AND_DEDUPLICATION",
            "asset discovery trigger drift")
    require(discovery["clean_room_generation_must_precede_asset_solution_lookup"] is True,
            "clean-room ordering lost")
    require(discovery["clean_room_generation_complete"] is True,
            "EX5-03 completion flag lost")
    for key in ("repository_asset_discovery_performed", "arsenal_index_read", "deduplication_performed"):
        require(discovery[key] is False, f"EX5-04 work pre-credited: {key}")

    bootstrap = state["bootstrap"]
    require(bootstrap["merge_authorized"] is False, "merge must not be authorized")
    require(bootstrap["active_work_pr"] == 1710, "wrong active EX5 work PR")

    frontier = state["frontier"]
    for key in ("EX5_00_source_lock_complete", "receiver_population_contract_complete",
                "receiver_ledger_complete", "receiver_ledger_coverage_certified",
                "current_coverage_dependency_graph_complete", "clean_room_candidate_universe_frozen"):
        require(frontier[key] is True, f"frontier flag must be complete: {key}")
    for key in ("arsenal_dedup_complete", "route_scorecard_complete", "primary_route_selected",
                "primary_microdiagnostic_complete", "nontrivial_receiver_effect_obtained",
                "qualified_independent_route_established", "frozen_breadth_package_exhausted",
                "audit_ready_EX5_route_decision_closure", "EX5_route_decision_closure"):
        require(frontier[key] is False, f"future frontier flag pre-credited: {key}")
    require(frontier["backup_route_count"] == 0, "backup routes cannot be preselected")
    require(frontier["terminal_outcome"] is None, "terminal outcome cannot be set")

    current = state["current"]
    require(current["status"] ==
            "EX5_03_CLEAN_ROOM_CANDIDATE_UNIVERSE_FROZEN_UNAUDITED_RETAINED",
            "wrong retained EX5-03 status")
    require(current["leaf"] == "EX5-04_REPOSITORY_ASSET_DISCOVERY_AND_DEDUPLICATION",
            "EX5-03 completion must route to EX5-04")

    working = state["current_leaf_working_set"]
    required_order = [
        "stages/stage32-ex5/ex5-03-clean-room-route-universe.json",
        "stages/stage32-ex5/verify_ex5_03_clean_room_routes.py",
        "stages/stage32-ex5/stage32-ex5.md",
        "docs/research-os/policies/repository-asset-discovery.md",
        "docs/arsenal/index.json",
    ]
    require(working == required_order, "EX5-04 working-set/order drift")
    require(working.index("docs/research-os/policies/repository-asset-discovery.md") <
            working.index("docs/arsenal/index.json"),
            "asset policy must precede Arsenal index")

    require(state["credit"]["level"] ==
            "EX5_03_CLEAN_ROOM_CANDIDATE_UNIVERSE_ONLY_NO_MATHEMATICAL_CREDIT",
            "credit level drift")
    require(state["audit"]["status"] == "NOT_READY_INTERMEDIATE_EX5_03_UNAUDITED",
            "audit readiness drift")

    for key, value in state["firewalls"].items():
        require(value is False, f"firewall {key} must remain false")

    print("PASS: Stage32EX5 MAIN state structural/firewall contract through EX5-03")


if __name__ == "__main__":
    main()
