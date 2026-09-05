#!/usr/bin/env python3
"""Generate/check Stage33 MAIN compact state at hostile-audited V91C1A."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parent
D = H / "33-12"
OUT = H / "MAIN-STATE.json"
CONTROLLER = H / "controller.json"
V91C = D / "e3-v91c-type-safe-cech-adapter-interface.json"
V91C1A = D / "e3-v91c1a-a2-02-literal-boundary-seed-localization.json"
BF = D / "boundary-function-generator-source-lock.json"
SCALAR = D / "boundary-function-scalar-descent-certificate.json"

EXPECTED = json.loads(r'''{"anti_loop_policy":{"do_not_identify_proper14_axes_3_5_with_boundary_A2_positions":true,"do_not_promote_boundary_function_scalar_descent_alone_to_global_h2_mu2":true,"do_not_promote_coordinate_conjugate_route_family_failure_to_global_H2_mu2_nonexistence":true,"do_not_reintroduce_retired_v47_14x14_p_w_after_v50":true,"do_not_relabel_j2_literal_cech_as_e3":true,"do_not_reopen_coordinate_conjugate_sign_quotient_gysin_after_v85":true,"do_not_treat_a2_02_preflight_direction_as_e3_coefficient":true,"do_not_treat_marked_picard_dual_class_as_integral_picard_divisor":true,"do_not_treat_retained_support_1_8_10_as_literal_divisor_labels":true},"audit_provenance":{"audit_pass_credit":true,"checkpoint_job":101304775240,"checkpoint_run":33965495569,"exact_audited_head":"12191226e71878bb252a2e764a856fa336586b72","exact_chain_job":101304774843,"exact_chain_run":33965495587,"hostile_audit_review":5121286657,"hostile_audit_verdict":"PASS","merge_commit":"d6d49a7a5b7678442d5c26080926f3f80032c4d4","merged_after_hostile_pass":true,"v91c1a_pr":1613},"authority_sync":{"controller_current_leaf_projection_synchronized":false,"controller_global_authority_locked":true,"frontier_authority":"V91C1A_A2_02_LITERAL_BOUNDARY_PACKAGE_LOCALIZED","mathematical_authority":"V25_V36_EXACT_CERTIFICATE_CHAIN_PLUS_BRANCH_E3_V41_THROUGH_V91C1A","operational_routing_authority":"V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP","status":"V91C1A_HOSTILE_AUDITED_MERGED_V91C1B_RESOLVED_SURFACE_ATTACHMENT_ACTIVE","supersession_scope":"BRANCH_CURRENT_LEAF_ONLY_NO_CONTROLLER_GLOBAL_CREDIT_CHANGE"},"branch_exact_frontier_authority":"stages/stage33/33-12/e3-v91c1a-a2-02-literal-boundary-seed-localization.json","canonical_sha256":"5ef0145cbe203b6d0964b985402b28063515247ea9c8b8587d82c4b6e44b354c","controller_projection_canonical_sha256":"02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773","controller_schema":"STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE","current":{"active_missing_interface":"A2_02_RESOLVED_FULL_SURFACE_HEIGHT_ONE_AND_RESOLUTION_EXCEPTIONAL_VALUATION_ATTACHMENT_WITH_CECH_CARTIER_TRANSITION_DATA","logical_internal_branch":"33-13_FINITE_V4_KUMMER_MATRIX_REPAIR","next_exact_leaf":"V91C1B_ATTACH_A2_02_LITERAL_BOUNDARY_FUNCTION_PACKAGES_TO_RESOLVED_FULL_SURFACE_HEIGHT_ONE_AND_RESOLUTION_EXCEPTIONAL_VALUATIONS_WITH_CECH_CARTIER_TRANSITION_DATA","substep":"E3_V91C1B_A2_02_RESOLVED_VALUATION_CECH_CARTIER_ATTACHMENT","unit":"33-12"},"current_exact_frontier":{"a2_02_claimed_e3_coefficient":false,"a2_02_claimed_mask20_image":false,"a2_02_component_count":8,"a2_02_component_ids":["EXC_003","EXC_004","EXC_011","EXC_012","SIDE_002","SIDE_004","SIDE_006","SIDE_008"],"a2_02_literal_boundary_record_localized":true,"a2_02_raw_order":2,"a2_02_scalar_action_record_count":16,"a2_02_scalar_candidate_target_count":24,"a2_02_scalar_ratios_all_one":true,"boundary_function_cc_ct_scalar_ratios_all_one":true,"boundary_function_package_count":134,"boundary_function_working_generator_count":14,"direct_a2_to_k_14x14_bridge_forbidden":true,"e3_b1_branch_h1_dimension":4,"e3_complete_residue_audit_materialized":false,"e3_dual_pairing_bridge_rank_f2":14,"e3_genuine_full_surface_h2_mu2_lift_materialized":false,"e3_global_H2_mu2_nonexistence_claim":false,"e3_literal_boundary_function_route_source_localized":true,"e3_literal_cech_seed_materialized":false,"e3_literal_kummer_function_materialized":false,"e3_literal_picard_divisor_materialized":false,"e3_marked_brauer_image_from_boundary_functions_materialized":false,"e3_marked_picard_dual_numerator_mod8_64":[2,3,0,7,0,0,6,4,4,2,2,2,6,0,2,7,1,5,7,0,0,4,4,4,4,0,4,4,5,6,0,2,0,0,5,0,6,2,6,0,0,0,0,0,0,2,0,0,2,0,6,4,0,0,3,5,0,6,2,6,2,0,0,0],"e3_marked_picard_dual_roundtrip_exact":true,"e3_marked_picard_dual_source_bound":true,"e3_proper14_is_dual_not_at2_element":true,"e3_proper14_mask_decimal":20,"e3_proper14_support_one_based":[3,5],"e3_retained_at_mod2_quotient_coordinate_f2":[1,0,0,0,0,0,0,1,0,1,0,0,0,0],"e3_retained_at_mod2_quotient_support_one_based":[1,8,10],"e3_retained_at_mod2_solution_unique":true,"full_surface_cech_transition_cartier_assembly_materialized":false,"j2_adapted_columns_materialized":1,"j2_adapted_columns_total":10,"original_standard_columns_materialized":0},"current_leaf_working_set":["docs/research-os/policies/repository-asset-discovery.md","docs/arsenal/index.json","docs/arsenal/cards/provisional/S33-PW04.md","docs/arsenal/cards/provisional/S33-PW07.md","docs/arsenal/cards/provisional/S33-PW08.md","stages/stage33/33-12/e3-v91c-type-safe-cech-adapter-interface.json","stages/stage33/33-12/e3-v91c1a-a2-02-literal-boundary-seed-localization.json","stages/stage33/33-12/e3-direct-cech-seed-contract-v88.json","stages/stage33/33-12/e3-retained-at-marked-picard-dual-source-v91.json","stages/stage33/33-12/boundary-function-generator-source-lock.json","stages/stage33/33-12/boundary-function-scalar-descent-certificate.json","stages/stage33/33-11/materialize_stage33_11_a2_26_explicit_gersten_difference_preimage.py","stages/stage33/33-11/stage33-11-a2-26-explicit-gersten-difference-preimage.json","stages/stage33/33-09/marked-picard-basis-source.json","stages/stage33/33-09/marked-picard-basis-bridge-certified.json"],"detailed_machine_authority":"stages/stage33/controller.json","discovery_policy":{"arsenal_index":"docs/arsenal/index.json","current_arsenal_cards":["S33-PW04","S33-PW07","S33-PW08"],"each_repeat_requires_materially_new_mathematical_signal":true,"fixed_per_object_search_count_cap":null,"ordinary_order":["ARSENAL","REPEATABLE_BOUNDED_REPOSITORY_SEARCH_WHEN_MATERIALLY_NEW_SIGNAL","CONSTRUCT"],"repeated_bounded_repository_search_allowed":true,"search_miss_proves_mathematical_nonexistence":false,"search_miss_proves_repository_absence":false,"unbounded_repository_search_allowed":false},"execution_gate":{"advance_allowed":true,"advance_scope":"V91C1B_A2_02_RESOLVED_SURFACE_CECH_CARTIER_ATTACHMENT","next_expected_command":"V91C1B_ATTACH_A2_02_LITERAL_BOUNDARY_FUNCTION_PACKAGES_TO_RESOLVED_FULL_SURFACE_HEIGHT_ONE_AND_RESOLUTION_EXCEPTIONAL_VALUATIONS_WITH_CECH_CARTIER_TRANSITION_DATA","stop_semantics":"LEAF_GATE_ONLY_NOT_ALGORITHM_EXHAUSTION"},"firewalls":{"endpoint_credit":false,"merge_allowed":false,"perfect_cuboid_existence_claim":false,"perfect_cuboid_nonexistence_claim":false,"receiver_credit":false,"stage33_07_reclosed":false,"stage33_08_released":false,"stage33_12_closed_exact":false,"stage33_13_released":false,"theorem_credit":false},"locked_facts":{"boundary_function_generator":{"sha256":"aaacc000f2e5fbbe733789f5f2a19d6c2cb14b5d3a26d0b8e508eea1f3bc8c96"},"boundary_function_scalar_descent":{"sha256":"e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b"},"v88":{"sha256":"1d8f7b9478f48a3aa2137524180afea0a8e0bbf909e4ece04b1a07ee44d365b7"},"v91":{"sha256":"729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9"},"v91b":{"sha256":"7d0669f8c8ec6e590838095640b69cc0e9c8f76088a0c89f74cc8f49235d7443"},"v91c":{"sha256":"da156e8fcbd59743073b5a3d8ba5359c533b0b045adddc41877310974cdc1754"},"v91c1a":{"sha256":"7f81ce5da7a4880cf0ffa048ab335fe2db9a643158d26144f45d0de22604b403"}},"resolved_investigations":{"e3_boundary_function_route":"SOURCE_LOCALIZED_EXACT_V91B_LITERAL_FUNCTION_PACKAGES_134_SCALARS_ONE","e3_coordinate_conjugate_sign_quotient_family":"CLOSED_EXACT_V85_DO_NOT_REOPEN","e3_direct_cech_seed_contract":"CLOSED_CONTRACT_V88_SEED_UNMATERIALIZED","e3_literal_integral_picard_divisor_branch":"CLOSED_EXACT_V91A_TYPE_OBSTRUCTION","e3_marked_picard_dual_source_binding":"CLOSED_EXACT_V91_SUPPORT_1_8_10_MARKED_INDLIST_DUAL_CLASS","e3_old_a2_to_k_14x14_p_w":"RETIRED_WRONG_OBJECT_TYPE_V50_DO_NOT_REOPEN","e3_v91c1a_a2_02_preflight":"HOSTILE_AUDITED_LITERAL_PACKAGE_LOCALIZATION_ONLY_NOT_E3_COEFFICIENT","e3_v91c_adapter_semantics":"TYPE_SAFE_COHOMOLOGICAL_FUNCTION_CECH_TO_MARKED_BRAUER_NOT_BASIS_CHANGE"},"role":"ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE","schema":"STAGE33_MAIN_COMPACT_STATE_V31_V91C1A_LITERAL_A2_02_PACKAGE_ACTIVE","stage33_progress":"6/11","work_checkpoint":{"authority":"OPERATIONAL_ONLY_NOT_PROOF","status":"EMPTY"}}''')
LOCKS = {
    V91C: "da156e8fcbd59743073b5a3d8ba5359c533b0b045adddc41877310974cdc1754",
    V91C1A: "7f81ce5da7a4880cf0ffa048ab335fe2db9a643158d26144f45d0de22604b403",
    BF: "aaacc000f2e5fbbe733789f5f2a19d6c2cb14b5d3a26d0b8e508eea1f3bc8c96",
    SCALAR: "e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b",
}
CONTROLLER_SHA = "02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773"
NEXT = "V91C1B_ATTACH_A2_02_LITERAL_BOUNDARY_FUNCTION_PACKAGES_TO_RESOLVED_FULL_SURFACE_HEIGHT_ONE_AND_RESOLUTION_EXCEPTIONAL_VALUATIONS_WITH_CECH_CARTIER_TRANSITION_DATA"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canon(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == LOCKS[path] == csha(body), path
    return obj


def validate_sources():
    controller = json.loads(CONTROLLER.read_text(encoding="utf-8"))
    body = dict(controller)
    claimed = body.pop("projection_canonical_sha256")
    assert claimed == CONTROLLER_SHA == csha(body)
    assert controller["merge_allowed"] is False
    assert controller["execution"]["merge_allowed"] is False

    v91c = load_canon(V91C)
    v91c1a = load_canon(V91C1A)
    bf = load_canon(BF)
    scalar = load_canon(SCALAR)

    assert v91c["type_firewall"]["retired_object_remains_forbidden"] is True
    assert v91c1a["status"] == "PASS_EXACT_V91C1A_A2_02_LITERAL_BOUNDARY_PACKAGE_LOCALIZED_FULL_SURFACE_CECH_CARTIER_BINDING_STILL_MISSING"
    assert v91c1a["literal_package_record"]["source_direction"] == "A2_02"
    assert v91c1a["literal_package_record"]["component_count"] == 8
    assert v91c1a["selection_semantics"]["selected_direction_is_claimed_e3_coefficient"] is False
    assert v91c1a["selection_semantics"]["single_direction_is_claimed_to_map_to_mask20"] is False
    assert v91c1a["next_exact_leaf"] == NEXT
    assert len(bf["generator_records"]) == 14
    assert scalar["boundary_function_package_count"] == 134
    assert scalar["exact_conclusion"]["all_cc_ct_function_level_scalar_ratios_equal_one"] is True


def validate_expected():
    body = dict(EXPECTED)
    claimed = body.pop("canonical_sha256")
    assert claimed == "5ef0145cbe203b6d0964b985402b28063515247ea9c8b8587d82c4b6e44b354c" == csha(body)
    assert EXPECTED["audit_provenance"]["hostile_audit_verdict"] == "PASS"
    assert EXPECTED["audit_provenance"]["hostile_audit_review"] == 5121286657
    assert EXPECTED["audit_provenance"]["merge_commit"] == "d6d49a7a5b7678442d5c26080926f3f80032c4d4"
    assert EXPECTED["current"]["next_exact_leaf"] == NEXT
    assert EXPECTED["stage33_progress"] == "6/11"
    assert EXPECTED["firewalls"]["merge_allowed"] is False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not args.check and not args.write:
        args.check = True

    validate_sources()
    validate_expected()

    if args.write:
        OUT.write_text(json.dumps(EXPECTED, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")

    if args.check:
        current = json.loads(OUT.read_text(encoding="utf-8"))
        assert current == EXPECTED
        print(json.dumps({
            "success": True,
            "marker": "V94_V91C1A_HOSTILE_AUDITED_AUTHORITY_SYNC_COMPLETE",
            "state_sha256": "5ef0145cbe203b6d0964b985402b28063515247ea9c8b8587d82c4b6e44b354c",
            "frontier": EXPECTED["authority_sync"]["frontier_authority"],
            "next_exact_leaf": NEXT,
            "stage33_progress": EXPECTED["stage33_progress"],
            "merge_allowed": EXPECTED["firewalls"]["merge_allowed"],
        }, sort_keys=True))


if __name__ == "__main__":
    main()
