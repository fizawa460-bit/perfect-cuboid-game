#!/usr/bin/env python3
"""Cheap structural verifier for Stage32EX5 MAIN-STATE.json.

This checks routing/credit firewalls only. It does not prove receiver coverage,
route qualification, or any mathematical claim.
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

    require(state.get("stage") == "32EX5", "wrong stage")
    execution = state.get("execution", {})
    require(execution.get("main_command") == "stage32ex5-mainbatch", "wrong main command")
    require(execution.get("audit_command") == "stage32ex5-audit", "wrong audit command")

    completion = state.get("completion_contract", {})
    require(set(completion.get("allowed_terminal_outcomes", [])) == EXPECTED_TERMINALS,
            "terminal outcome contract mismatch")
    require(completion.get("EX5_route_decision_closure_is_Stage32_full_target_closure") is False,
            "EX5 closure must not equal Stage32 closure")
    require(completion.get("qualified_route_requires_retained_nontrivial_receiver_effect") is True,
            "qualified route must require a retained receiver effect")
    require(completion.get("bounded_exhaustion_is_global_no_route_theorem") is False,
            "bounded exhaustion must remain bounded")

    families = state.get("route_families", {})
    require(set(families.get("required_initial_families", [])) == EXPECTED_FAMILIES,
            "route-family set mismatch")
    require(families.get("scratch_results_authoritative") is False,
            "scratch results cannot be authoritative")

    receiver = state.get("receiver_contract", {})
    require(receiver.get("chat_or_memory_counts_treated_as_authority") is False,
            "chat/memory cannot define receiver authority")
    require(receiver.get("V6_O210_Q602_treated_as_definition_of_all_receivers") is False,
            "V6/O210/Q602 cannot silently define all receivers")

    discovery = state.get("asset_discovery", {})
    require(discovery.get("policy_path") == "docs/research-os/policies/repository-asset-discovery.md",
            "asset discovery policy path mismatch")
    require(discovery.get("arsenal_index_path") == "docs/arsenal/index.json",
            "arsenal index path mismatch")
    require(discovery.get("clean_room_generation_must_precede_asset_solution_lookup") is True,
            "clean-room generation ordering lost")

    bootstrap = state.get("bootstrap", {})
    require(bootstrap.get("merge_authorized") is False, "merge must not be authorized")

    firewalls = state.get("firewalls", {})
    false_keys = [
        "receiver_ledger_promoted_to_mathematical_closure",
        "route_score_promoted_to_mathematical_credit",
        "theorem_name_promoted_without_population_adapter",
        "arsenal_keyword_match_promoted_to_applicability",
        "sample_result_promoted_to_receiver_wide_result",
        "finite_search_miss_promoted_to_impossibility",
        "V6_only_result_promoted_to_stage32_wide_progress",
        "other_stage_provisional_result_imported_as_authority",
        "duplicate_MAIN_or_EX1_EX4_route_promoted_as_independent",
        "bounded_candidate_package_exhaustion_promoted_to_global_no_route_theorem",
        "EX5_route_decision_closure_promoted_to_stage32_closure",
        "blocked_route_treated_as_stage_exhaustion",
        "stage32_main_credit",
        "Q602_excluded",
        "O210_excluded",
        "O212_plus_advance_allowed",
        "stage32_closed",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
    ]
    for key in false_keys:
        require(firewalls.get(key) is False, f"firewall {key} must be false")

    current = state.get("current", {})
    require(current.get("leaf") == "EX5-00_SOURCE_LOCK_AND_STAGE32_TARGET_RECEIVER_CONTRACT",
            "bootstrap must start at EX5-00")

    print("PASS: Stage32EX5 MAIN state structural/firewall contract")


if __name__ == "__main__":
    main()
