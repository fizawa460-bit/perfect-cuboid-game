#!/usr/bin/env python3
"""Generate/check Stage33 MAIN compact state at the merged V91B frontier."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parent
D = H / "33-12"
OUT = H / "MAIN-STATE.json"
CONTROLLER = H / "controller.json"

NEXT = "V91C_CONSTRUCT_EXACT_BOUNDARY_FUNCTION_A2_TO_V91_MARKED_DISCRIMINANT_PROPER14_ADAPTER"
TARGET = [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
TARGET_NUM = [2, 3, 0, 7, 0, 0, 6, 4, 4, 2, 2, 2, 6, 0, 2, 7, 1, 5, 7, 0, 0, 4, 4, 4, 4, 0, 4, 4, 5, 6, 0, 2, 0, 0, 5, 0, 6, 2, 6, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 6, 4, 0, 0, 3, 5, 0, 6, 2, 6, 2, 0, 0, 0]
ORDER = ['A2_02', 'A2_03', 'A2_24', 'A2_25', 'A2_26', 'A2_04', 'A2_01', 'A2_07', 'A2_05', 'A2_10', 'A2_08', 'A2_09', 'A2_16', 'A2_15']

CANON_LOCKS = {
    D / "e3-direct-cech-seed-contract-v88.json": "1d8f7b9478f48a3aa2137524180afea0a8e0bbf909e4ece04b1a07ee44d365b7",
    D / "e3-retained-at-marked-picard-dual-source-v91.json": "729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9",
    D / "e3-v91b-boundary-function-adapter-gap.json": "7d0669f8c8ec6e590838095640b69cc0e9c8f76088a0c89f74cc8f49235d7443",
    D / "e3-v91c-type-safe-cech-adapter-interface.json": "da156e8fcbd59743073b5a3d8ba5359c533b0b045adddc41877310974cdc1754",
    D / "boundary-function-generator-source-lock.json": "aaacc000f2e5fbbe733789f5f2a19d6c2cb14b5d3a26d0b8e508eea1f3bc8c96",
    D / "boundary-function-scalar-descent-certificate.json": "e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b",
}
BLOB_LOCKS = {
    D / "e3-a1-1-type-correction-v50.json": "1aa59da6303b6f8b0286c9c32fdc72960bc0dc85",
    D / "e3-v25-method-rewire-v51.json": "32ab508f836f8d3a40570d686232bf67aeaa6152",
    D / "e3-mask20-literal-cech-preimage-gap-v52.json": "15ae7ebf8ddaf9d8771d48bc93caa0705e4ebf67",
}
WORKING_SET = ['docs/research-os/policies/repository-asset-discovery.md', 'docs/arsenal/index.json', 'docs/arsenal/cards/provisional/S33-PW04.md', 'docs/arsenal/cards/provisional/S33-PW07.md', 'docs/arsenal/cards/provisional/S33-PW08.md', 'stages/stage33/33-12/e3-v91b-boundary-function-adapter-gap.json', 'stages/stage33/33-12/e3-v91c-type-safe-cech-adapter-interface.json', 'stages/stage33/33-12/e3-a1-1-type-correction-v50.json', 'stages/stage33/33-12/e3-v25-method-rewire-v51.json', 'stages/stage33/33-12/e3-mask20-literal-cech-preimage-gap-v52.json', 'stages/stage33/33-12/e3-direct-cech-seed-contract-v88.json', 'stages/stage33/33-12/e3-retained-at-marked-picard-dual-source-v91.json', 'stages/stage33/33-12/boundary-function-generator-source-lock.json', 'stages/stage33/33-12/boundary-function-scalar-descent-certificate.json', 'stages/stage33/33-09/marked-picard-basis-source.json', 'stages/stage33/33-09/marked-picard-basis-bridge-certified.json']

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def git_blob_sha1(raw: bytes):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def load_canon(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == CANON_LOCKS[path] == csha(body), path
    return obj

def load_blob(path):
    raw = path.read_bytes()
    assert git_blob_sha1(raw) == BLOB_LOCKS[path], path
    return json.loads(raw)

def build(work):
    controller = json.loads(CONTROLLER.read_text(encoding="utf-8"))
    cb = dict(controller)
    controller_sha = cb.pop("projection_canonical_sha256")
    assert controller_sha == csha(cb)
    assert controller_sha == "02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773"
    assert controller["schema"] == "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE"
    assert controller["merge_allowed"] is False and controller["execution"]["merge_allowed"] is False

    v50 = load_blob(D / "e3-a1-1-type-correction-v50.json")
    v51 = load_blob(D / "e3-v25-method-rewire-v51.json")
    v52 = load_blob(D / "e3-mask20-literal-cech-preimage-gap-v52.json")
    v88 = load_canon(D / "e3-direct-cech-seed-contract-v88.json")
    v91 = load_canon(D / "e3-retained-at-marked-picard-dual-source-v91.json")
    v91b = load_canon(D / "e3-v91b-boundary-function-adapter-gap.json")
    v91c = load_canon(D / "e3-v91c-type-safe-cech-adapter-interface.json")
    bf = load_canon(D / "boundary-function-generator-source-lock.json")
    scalar = load_canon(D / "boundary-function-scalar-descent-certificate.json")

    assert v50["retired_assumption"]["status"] == "RETIRED_WRONG_OBJECT_TYPE"
    assert v50["retired_assumption"]["v47_14_column_construction_contract_superseded"] is True
    assert v51["exact_rewire"]["retired_route_remains_forbidden"] is True
    assert v51["arsenal_routing"]["pw05_direct_14d_bridge_route"] is False
    assert v52["bounded_inspection"]["available_marked_picard_data"]["literal_function_divisor_transition_preimage_for_mask20_materialized"] is False
    assert v88["v88_construction_contract"]["smallest_missing_seed"].startswith("one source-specific literal geometric seed")
    assert v91["e3_source_binding"]["retained_at_mod2_quotient_coordinate_f2"] == TARGET
    assert v91["e3_source_binding"]["marked_indlist_picard_dual_numerator_mod8_64"] == TARGET_NUM
    assert v91b["positive_retained_asset"]["ordered_source_directions"] == ORDER
    assert v91b["positive_retained_asset"]["package_count"] == 134
    assert v91b["positive_retained_asset"]["literal_boundary_function_packages_materialized"] is True
    assert v91c["entry_authority"]["hostile_audit_verdict"] == "FAIL_FRESHNESS_ONLY"
    assert v91c["entry_authority"]["audit_pass_credit"] is False
    assert v91c["type_firewall"]["retired_object_remains_forbidden"] is True
    assert v91c["adapter_definition"]["materialized"] is False
    assert len(bf["generator_records"]) == 14
    assert [r["source_direction"] for r in bf["generator_records"]] == ORDER
    assert scalar["working_generator_count"] == 14
    assert scalar["working_generator_ids"] == ORDER
    assert scalar["boundary_function_package_count"] == 134
    assert scalar["exact_conclusion"]["all_cc_ct_function_level_scalar_ratios_equal_one"] is True

    state = json.loads(r'''{"anti_loop_policy":{"do_not_identify_proper14_axes_3_5_with_boundary_A2_positions":true,"do_not_promote_boundary_function_scalar_descent_alone_to_global_h2_mu2":true,"do_not_promote_coordinate_conjugate_route_family_failure_to_global_H2_mu2_nonexistence":true,"do_not_reintroduce_retired_v47_14x14_p_w_after_v50":true,"do_not_relabel_j2_literal_cech_as_e3":true,"do_not_reopen_coordinate_conjugate_sign_quotient_gysin_after_v85":true,"do_not_treat_marked_picard_dual_class_as_integral_picard_divisor":true,"do_not_treat_retained_support_1_8_10_as_literal_divisor_labels":true},"audit_provenance":{"audit_pass_credit":false,"hostile_audit_review":5120883188,"hostile_audit_verdict":"FAIL_FRESHNESS_ONLY","mathematics_and_route_selection_passed_in_review":true,"merge_commit":"29ce620a693f7cbdec48bce9b720cc02dfe5fa74","merged_by_user_after_math_pass":true,"v91b_pr":1604},"authority_sync":{"controller_current_leaf_projection_synchronized":false,"controller_global_authority_locked":true,"frontier_authority":"V91B_LITERAL_BOUNDARY_FUNCTION_ASSET_LOCALIZED","mathematical_authority":"V25_V36_EXACT_CERTIFICATE_CHAIN_PLUS_BRANCH_E3_V41_THROUGH_V91B","operational_routing_authority":"V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP","status":"V91B_MERGED_FRONTIER_PROJECTED_V91C_TYPE_SAFE_CECH_ADAPTER_ACTIVE","supersession_scope":"BRANCH_CURRENT_LEAF_ONLY_NO_CONTROLLER_GLOBAL_CREDIT_CHANGE"},"branch_exact_frontier_authority":"stages/stage33/33-12/e3-v91b-boundary-function-adapter-gap.json","controller_projection_canonical_sha256":"02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773","controller_schema":"STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE","current":{"active_missing_interface":"TYPE_SAFE_SOURCE_BOUND_FULL_SURFACE_CECH_TRANSITION_CARTIER_ASSEMBLY_AND_EXACT_MASK20_BRAUER_IMAGE_BINDING","logical_internal_branch":"33-13_FINITE_V4_KUMMER_MATRIX_REPAIR","next_exact_leaf":"V91C_CONSTRUCT_EXACT_BOUNDARY_FUNCTION_A2_TO_V91_MARKED_DISCRIMINANT_PROPER14_ADAPTER","substep":"E3_V91C_TYPE_SAFE_BOUNDARY_FUNCTION_CECH_MARKED_BRAUER_ADAPTER","unit":"33-12"},"current_exact_frontier":{"boundary_function_cc_ct_scalar_ratios_all_one":true,"boundary_function_package_count":134,"boundary_function_working_generator_count":14,"direct_a2_to_k_14x14_bridge_forbidden":true,"e3_b1_branch_h1_dimension":4,"e3_complete_residue_audit_materialized":false,"e3_dual_pairing_bridge_rank_f2":14,"e3_genuine_full_surface_h2_mu2_lift_materialized":false,"e3_global_H2_mu2_nonexistence_claim":false,"e3_literal_boundary_function_route_source_localized":true,"e3_literal_cech_seed_materialized":false,"e3_literal_kummer_function_materialized":false,"e3_literal_picard_divisor_materialized":false,"e3_marked_brauer_image_from_boundary_functions_materialized":false,"e3_marked_picard_dual_numerator_mod8_64":[2,3,0,7,0,0,6,4,4,2,2,2,6,0,2,7,1,5,7,0,0,4,4,4,4,0,4,4,5,6,0,2,0,0,5,0,6,2,6,0,0,0,0,0,0,2,0,0,2,0,6,4,0,0,3,5,0,6,2,6,2,0,0,0],"e3_marked_picard_dual_roundtrip_exact":true,"e3_marked_picard_dual_source_bound":true,"e3_proper14_is_dual_not_at2_element":true,"e3_proper14_mask_decimal":20,"e3_proper14_support_one_based":[3,5],"e3_retained_at_mod2_quotient_coordinate_f2":[1,0,0,0,0,0,0,1,0,1,0,0,0,0],"e3_retained_at_mod2_quotient_support_one_based":[1,8,10],"e3_retained_at_mod2_solution_unique":true,"full_surface_cech_transition_cartier_assembly_materialized":false,"j2_adapted_columns_materialized":1,"j2_adapted_columns_total":10,"original_standard_columns_materialized":0},"current_leaf_working_set":["docs/research-os/policies/repository-asset-discovery.md","docs/arsenal/index.json","docs/arsenal/cards/provisional/S33-PW04.md","docs/arsenal/cards/provisional/S33-PW07.md","docs/arsenal/cards/provisional/S33-PW08.md","stages/stage33/33-12/e3-v91b-boundary-function-adapter-gap.json","stages/stage33/33-12/e3-v91c-type-safe-cech-adapter-interface.json","stages/stage33/33-12/e3-a1-1-type-correction-v50.json","stages/stage33/33-12/e3-v25-method-rewire-v51.json","stages/stage33/33-12/e3-mask20-literal-cech-preimage-gap-v52.json","stages/stage33/33-12/e3-direct-cech-seed-contract-v88.json","stages/stage33/33-12/e3-retained-at-marked-picard-dual-source-v91.json","stages/stage33/33-12/boundary-function-generator-source-lock.json","stages/stage33/33-12/boundary-function-scalar-descent-certificate.json","stages/stage33/33-09/marked-picard-basis-source.json","stages/stage33/33-09/marked-picard-basis-bridge-certified.json"],"detailed_machine_authority":"stages/stage33/controller.json","discovery_policy":{"arsenal_index":"docs/arsenal/index.json","current_arsenal_cards":["S33-PW04","S33-PW07","S33-PW08"],"each_repeat_requires_materially_new_mathematical_signal":true,"fixed_per_object_search_count_cap":null,"ordinary_order":["ARSENAL","REPEATABLE_BOUNDED_REPOSITORY_SEARCH_WHEN_MATERIALLY_NEW_SIGNAL","CONSTRUCT"],"repeated_bounded_repository_search_allowed":true,"search_miss_proves_mathematical_nonexistence":false,"search_miss_proves_repository_absence":false,"unbounded_repository_search_allowed":false},"execution_gate":{"advance_allowed":true,"advance_scope":"V91C_TYPE_SAFE_BOUNDARY_FUNCTION_CECH_ADAPTER","next_expected_command":"V91C_CONSTRUCT_EXACT_BOUNDARY_FUNCTION_A2_TO_V91_MARKED_DISCRIMINANT_PROPER14_ADAPTER","stop_semantics":"LEAF_GATE_ONLY_NOT_ALGORITHM_EXHAUSTION"},"firewalls":{"endpoint_credit":false,"merge_allowed":false,"perfect_cuboid_existence_claim":false,"perfect_cuboid_nonexistence_claim":false,"receiver_credit":false,"stage33_07_reclosed":false,"stage33_08_released":false,"stage33_12_closed_exact":false,"stage33_13_released":false,"theorem_credit":false},"locked_facts":{"boundary_function_generator":{"sha256":"aaacc000f2e5fbbe733789f5f2a19d6c2cb14b5d3a26d0b8e508eea1f3bc8c96"},"boundary_function_scalar_descent":{"sha256":"e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b"},"v50":{"git_blob_sha1":"1aa59da6303b6f8b0286c9c32fdc72960bc0dc85"},"v51":{"git_blob_sha1":"32ab508f836f8d3a40570d686232bf67aeaa6152"},"v52":{"git_blob_sha1":"15ae7ebf8ddaf9d8771d48bc93caa0705e4ebf67"},"v88":{"sha256":"1d8f7b9478f48a3aa2137524180afea0a8e0bbf909e4ece04b1a07ee44d365b7"},"v91":{"sha256":"729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9"},"v91b":{"sha256":"7d0669f8c8ec6e590838095640b69cc0e9c8f76088a0c89f74cc8f49235d7443"},"v91c_current_leaf_contract":{"authority":"CURRENT_LEAF_CONTRACT_NOT_MERGED_FRONTIER_PROOF","sha256":"da156e8fcbd59743073b5a3d8ba5359c533b0b045adddc41877310974cdc1754"}},"resolved_investigations":{"e3_boundary_function_route":"SOURCE_LOCALIZED_EXACT_V91B_LITERAL_FUNCTION_PACKAGES_134_SCALARS_ONE","e3_coordinate_conjugate_sign_quotient_family":"CLOSED_EXACT_V85_DO_NOT_REOPEN","e3_direct_cech_seed_contract":"CLOSED_CONTRACT_V88_SEED_UNMATERIALIZED","e3_literal_integral_picard_divisor_branch":"CLOSED_EXACT_V91A_TYPE_OBSTRUCTION","e3_marked_picard_dual_source_binding":"CLOSED_EXACT_V91_SUPPORT_1_8_10_MARKED_INDLIST_DUAL_CLASS","e3_old_a2_to_k_14x14_p_w":"RETIRED_WRONG_OBJECT_TYPE_V50_DO_NOT_REOPEN","e3_v91c_adapter_semantics":"TYPE_SAFE_COHOMOLOGICAL_FUNCTION_CECH_TO_MARKED_BRAUER_NOT_BASIS_CHANGE"},"role":"ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE","schema":"STAGE33_MAIN_COMPACT_STATE_V30_V91B_BOUNDARY_FUNCTION_ASSET_ACTIVE","stage33_progress":"6/11"}''')
    state["work_checkpoint"] = work
    state["controller_projection_canonical_sha256"] = controller_sha
    assert state["current_leaf_working_set"] == WORKING_SET
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
        "v91b_audit_verdict": expected["audit_provenance"]["hostile_audit_verdict"],
        "v91b_audit_pass_credit": expected["audit_provenance"]["audit_pass_credit"],
    }, sort_keys=True))

if __name__ == "__main__":
    main()
