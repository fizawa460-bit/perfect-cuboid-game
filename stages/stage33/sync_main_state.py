#!/usr/bin/env python3
"""Generate/check Stage33 MAIN compact state at the exact V91 frontier."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parent
D = H / "33-12"
M = H / "33-09"
L = H / "33-07"
OUT = H / "MAIN-STATE.json"
CONTROLLER = H / "controller.json"
NEXT = "V91A_LIFT_MARKED_PICARD_DUAL_CLASS_SUPPORT_1_8_10_TO_LITERAL_DIVISOR_OR_DIRECT_CECH_KUMMER_DATUM"
TARGET = [1,0,0,0,0,0,0,1,0,1,0,0,0,0]
TARGET_NUM = [2,3,0,7,0,0,6,4,4,2,2,2,6,0,2,7,1,5,7,0,0,4,4,4,4,0,4,4,5,6,0,2,0,0,5,0,6,2,6,0,0,0,0,0,0,2,0,0,2,0,6,4,0,0,3,5,0,6,2,6,2,0,0,0]
WORKING_SET = [
    "docs/research-os/policies/repository-asset-discovery.md",
    "docs/arsenal/index.json",
    "docs/arsenal/cards/provisional/S33-PW04.md",
    "docs/arsenal/cards/provisional/S33-PW07.md",
    "stages/stage33/33-12/e3-retained-at-marked-picard-dual-source-v91.json",
    "stages/stage33/33-12/e3-proper14-dual-to-discriminant-quotient-bridge-v89.json",
    "stages/stage33/33-12/e3-direct-cech-seed-contract-v88.json",
    "stages/stage33/33-12/e3-proper14-boundary-basis-definitions-v45.json",
    "stages/stage33/33-09/marked-picard-basis-source.json",
    "stages/stage33/33-09/marked-picard-basis-bridge-certified.json",
    "stages/stage33/33-07/picard-discriminant-compact.json",
]
LOCKS = {
    D / "e3-proper14-boundary-basis-definitions-v45.json": "a1dafa0be79c80d7275cd2629278bf6a56d6e592f90738316e71ca2689f9feb5",
    D / "e3-direct-cech-seed-contract-v88.json": "1d8f7b9478f48a3aa2137524180afea0a8e0bbf909e4ece04b1a07ee44d365b7",
    D / "e3-proper14-dual-to-discriminant-quotient-bridge-v89.json": "26bf699fd92e261e1ae40066ad0fd5aece9cb896f28a385367786de1d0460639",
    D / "e3-retained-at-marked-picard-dual-source-v91.json": "729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9",
    M / "marked-picard-basis-source.json": "0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f",
    M / "marked-picard-basis-bridge-certified.json": "039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92",
    L / "picard-discriminant-compact.json": "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0",
}


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == LOCKS[path] == csha(body), path
    return obj


def build(work):
    controller = json.loads(CONTROLLER.read_text(encoding="utf-8"))
    cb = dict(controller)
    controller_sha = cb.pop("projection_canonical_sha256")
    assert controller_sha == csha(cb)
    assert controller["schema"] == "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE"
    assert controller["merge_allowed"] is False and controller["execution"]["merge_allowed"] is False

    v45 = load_locked(D / "e3-proper14-boundary-basis-definitions-v45.json")
    v88 = load_locked(D / "e3-direct-cech-seed-contract-v88.json")
    v89 = load_locked(D / "e3-proper14-dual-to-discriminant-quotient-bridge-v89.json")
    v91 = load_locked(D / "e3-retained-at-marked-picard-dual-source-v91.json")
    source = load_locked(M / "marked-picard-basis-source.json")
    bridge = load_locked(M / "marked-picard-basis-bridge-certified.json")
    load_locked(L / "picard-discriminant-compact.json")

    assert v45["non_identification_lock"]["positional_identification_allowed"] is False
    assert v88["bounded_negative_findings"]["proper14_axis_labels_3_and_5_supply_literal_geometry"] is False
    assert v89["dual_pairing_bridge"]["rank_f2"] == 14
    assert v89["e3_transport"]["retained_at_mod2_quotient_coordinate_f2"] == TARGET
    assert v89["e3_transport"]["retained_at_mod2_quotient_support_one_based"] == [1, 8, 10]
    assert v89["e3_transport"]["solution_unique"] is True
    assert bridge["source_locks"]["marked_bridge_certificate_sha256"] == source["canonical_sha256"]
    assert v91["source_locks"]["stage33_09_marked_picard_bridge_sha256"] == bridge["canonical_sha256"]
    bind = v91["e3_source_binding"]
    assert bind["retained_at_mod2_quotient_coordinate_f2"] == TARGET
    assert bind["retained_at_mod2_quotient_support_one_based"] == [1, 8, 10]
    assert bind["marked_indlist_picard_dual_numerator_mod8_64"] == TARGET_NUM
    assert bind["mixed_coordinate_roundtrip_exact"] is True
    assert bind["source_bound_to_actual_140_class_marking"] is True
    consequence = v91["exact_consequence"]
    assert consequence["retained_support_1_8_10_source_bound_to_marked_picard_dual_class"] is True
    assert consequence["all_14_retained_mixed_smith_generators_source_bound_to_marked_picard_dual_basis"] is True
    for key in (
        "literal_picard_divisor_materialized",
        "literal_kummer_function_materialized",
        "literal_cech_seed_materialized",
        "complete_residue_audit_materialized",
        "genuine_full_surface_h2_mu2_lift_for_e3",
    ):
        assert consequence[key] is False
    assert v91["next_exact_leaf"] == NEXT

    state = {
        "anti_loop_policy": {
            "do_not_identify_proper14_axes_3_5_with_boundary_A2_positions": True,
            "do_not_promote_coordinate_conjugate_route_family_failure_to_global_H2_mu2_nonexistence": True,
            "do_not_relabel_j2_literal_cech_as_e3": True,
            "do_not_reopen_coordinate_conjugate_sign_quotient_gysin_after_v85": True,
            "do_not_treat_marked_picard_dual_class_as_integral_picard_divisor": True,
            "do_not_treat_retained_support_1_8_10_as_literal_divisor_labels": True,
        },
        "authority_sync": {
            "controller_current_leaf_projection_synchronized": False,
            "controller_global_authority_locked": True,
            "frontier_authority": "V91_MARKED_PICARD_DUAL_SOURCE_BINDING",
            "mathematical_authority": "V25_V36_EXACT_CERTIFICATE_CHAIN_PLUS_BRANCH_E3_V41_THROUGH_V91",
            "operational_routing_authority": "V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP",
            "status": "V91_BRANCH_EXACT_FRONTIER_PROJECTED_CONTROLLER_GLOBAL_FIREWALLS_LOCKED",
            "supersession_scope": "BRANCH_CURRENT_LEAF_ONLY_NO_CONTROLLER_GLOBAL_CREDIT_CHANGE",
        },
        "branch_exact_frontier_authority": "stages/stage33/33-12/e3-retained-at-marked-picard-dual-source-v91.json",
        "controller_schema": "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE",
        "current": {
            "active_missing_interface": "LIFT_MARKED_PICARD_DUAL_CLASS_SUPPORT_1_8_10_TO_LITERAL_DIVISOR_OR_DIRECT_CECH_KUMMER_DATUM",
            "logical_internal_branch": "33-13_FINITE_V4_KUMMER_MATRIX_REPAIR",
            "next_exact_leaf": NEXT,
            "substep": "E3_V91A_LIFT_MARKED_PICARD_DUAL_CLASS_SUPPORT_1_8_10_TO_LITERAL_GEOMETRY",
            "unit": "33-12",
        },
        "current_exact_frontier": {
            "e3_b1_branch_h1_dimension": 4,
            "e3_complete_residue_audit_materialized": False,
            "e3_dual_pairing_bridge_rank_f2": 14,
            "e3_genuine_full_surface_h2_mu2_lift_materialized": False,
            "e3_global_H2_mu2_nonexistence_claim": False,
            "e3_literal_cech_seed_materialized": False,
            "e3_literal_kummer_function_materialized": False,
            "e3_literal_picard_divisor_materialized": False,
            "e3_marked_picard_dual_numerator_mod8_64": TARGET_NUM,
            "e3_marked_picard_dual_roundtrip_exact": True,
            "e3_marked_picard_dual_source_bound": True,
            "e3_proper14_is_dual_not_at2_element": True,
            "e3_proper14_mask_decimal": 20,
            "e3_proper14_support_one_based": [3, 5],
            "e3_retained_at_mod2_quotient_coordinate_f2": TARGET,
            "e3_retained_at_mod2_quotient_support_one_based": [1, 8, 10],
            "e3_retained_at_mod2_solution_unique": True,
            "j2_adapted_columns_materialized": 1,
            "j2_adapted_columns_total": 10,
            "original_standard_columns_materialized": 0,
        },
        "current_leaf_working_set": WORKING_SET,
        "detailed_machine_authority": "stages/stage33/controller.json",
        "discovery_policy": {
            "arsenal_index": "docs/arsenal/index.json",
            "current_arsenal_cards": ["S33-PW04", "S33-PW07"],
            "each_repeat_requires_materially_new_mathematical_signal": True,
            "fixed_per_object_search_count_cap": None,
            "ordinary_order": ["ARSENAL", "REPEATABLE_BOUNDED_REPOSITORY_SEARCH_WHEN_MATERIALLY_NEW_SIGNAL", "CONSTRUCT"],
            "repeated_bounded_repository_search_allowed": True,
            "search_miss_proves_mathematical_nonexistence": False,
            "search_miss_proves_repository_absence": False,
            "unbounded_repository_search_allowed": False,
        },
        "execution_gate": {
            "advance_allowed": True,
            "advance_scope": "V91A_LIFT_MARKED_PICARD_DUAL_CLASS_SUPPORT_1_8_10",
            "next_expected_command": NEXT,
            "stop_semantics": "LEAF_GATE_ONLY_NOT_ALGORITHM_EXHAUSTION",
        },
        "firewalls": {
            "endpoint_credit": False,
            "merge_allowed": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "receiver_credit": False,
            "stage33_07_reclosed": False,
            "stage33_08_released": False,
            "stage33_12_closed_exact": False,
            "stage33_13_released": False,
            "theorem_credit": False,
        },
        "locked_facts": {
            "marked_picard_basis_bridge": {"sha256": LOCKS[M / "marked-picard-basis-bridge-certified.json"]},
            "marked_picard_basis_source": {"sha256": LOCKS[M / "marked-picard-basis-source.json"]},
            "picard_discriminant_compact": {"sha256": LOCKS[L / "picard-discriminant-compact.json"]},
            "v45": {"sha256": LOCKS[D / "e3-proper14-boundary-basis-definitions-v45.json"]},
            "v88": {"sha256": LOCKS[D / "e3-direct-cech-seed-contract-v88.json"]},
            "v89": {"sha256": LOCKS[D / "e3-proper14-dual-to-discriminant-quotient-bridge-v89.json"]},
            "v91": {"sha256": LOCKS[D / "e3-retained-at-marked-picard-dual-source-v91.json"]},
        },
        "resolved_investigations": {
            "e3_coordinate_conjugate_sign_quotient_family": "CLOSED_EXACT_V85_DO_NOT_REOPEN",
            "e3_direct_cech_seed_contract": "CLOSED_CONTRACT_V88_SEED_UNMATERIALIZED",
            "e3_literal_source_binding": "PARTIAL_EXACT_V91_MARKED_PICARD_DUAL_BOUND_LITERAL_DIVISOR_OR_CECH_KUMMER_STILL_OPEN",
            "e3_marked_picard_dual_source_binding": "CLOSED_EXACT_V91_SUPPORT_1_8_10_MARKED_INDLIST_DUAL_CLASS",
            "e3_proper14_dual_to_discriminant_quotient_bridge": "CLOSED_EXACT_V89_UNIQUE_SUPPORT_1_8_10",
        },
        "role": "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE",
        "schema": "STAGE33_MAIN_COMPACT_STATE_V29_V91_MARKED_PICARD_DUAL_SOURCE_BINDING_ACTIVE",
        "stage33_progress": "6/11",
        "controller_projection_canonical_sha256": controller_sha,
        "work_checkpoint": work,
    }
    state["canonical_sha256"] = csha(state)
    return state


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    current = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    work = current.get("work_checkpoint", {"authority": "OPERATIONAL_ONLY_NOT_PROOF", "status": "EMPTY"})
    assert work.get("authority") == "OPERATIONAL_ONLY_NOT_PROOF"
    expected = build(work)
    if args.check:
        assert current == expected
    else:
        OUT.write_text(json.dumps(expected, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "mode": "check" if args.check else "write",
        "canonical_sha256": expected["canonical_sha256"],
        "frontier": expected["authority_sync"]["frontier_authority"],
        "next_exact_leaf": expected["current"]["next_exact_leaf"],
        "working_set_size": len(expected["current_leaf_working_set"]),
        "stage33_progress": expected["stage33_progress"],
        "merge_allowed": expected["firewalls"]["merge_allowed"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
