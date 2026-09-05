#!/usr/bin/env python3
"""Generate/check Stage33 MAIN compact state at the exact V89 frontier."""
import argparse, hashlib, json
from pathlib import Path

H=Path(__file__).resolve().parent
D=H/"33-12"
OUT=H/"MAIN-STATE.json"
CONTROLLER=H/"controller.json"
NEXT="V89A_SOURCE_BIND_RETAINED_AT_MOD2_SUPPORT_1_8_10_TO_LITERAL_PICARD_DIVISOR_OR_DIRECT_CECH_KUMMER_DATUM"
BASE=json.loads('{"anti_loop_policy":{"do_not_identify_proper14_axes_3_5_with_boundary_A2_positions":true,"do_not_promote_coordinate_conjugate_route_family_failure_to_global_H2_mu2_nonexistence":true,"do_not_relabel_j2_literal_cech_as_e3":true,"do_not_reopen_coordinate_conjugate_sign_quotient_gysin_after_v85":true,"do_not_treat_retained_support_1_8_10_as_literal_divisor_labels":true},"authority_sync":{"controller_current_leaf_projection_synchronized":false,"controller_global_authority_locked":true,"frontier_authority":"V89_PROPER14_DUAL_TO_DISCRIMINANT_QUOTIENT_BRIDGE","mathematical_authority":"V25_V36_EXACT_CERTIFICATE_CHAIN_PLUS_BRANCH_E3_V41_THROUGH_V89","operational_routing_authority":"V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP","status":"V89_BRANCH_EXACT_FRONTIER_PROJECTED_CONTROLLER_GLOBAL_FIREWALLS_LOCKED","supersession_scope":"BRANCH_CURRENT_LEAF_ONLY_NO_CONTROLLER_GLOBAL_CREDIT_CHANGE"},"branch_exact_frontier_authority":"stages/stage33/33-12/e3-proper14-dual-to-discriminant-quotient-bridge-v89.json","controller_schema":"STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE","current":{"active_missing_interface":"SOURCE_BIND_RETAINED_AT_MOD2_SUPPORT_1_8_10_TO_LITERAL_PICARD_DIVISOR_OR_DIRECT_CECH_KUMMER_DATUM","logical_internal_branch":"33-13_FINITE_V4_KUMMER_MATRIX_REPAIR","next_exact_leaf":"V89A_SOURCE_BIND_RETAINED_AT_MOD2_SUPPORT_1_8_10_TO_LITERAL_PICARD_DIVISOR_OR_DIRECT_CECH_KUMMER_DATUM","substep":"E3_V89A_SOURCE_BIND_RETAINED_AT_MOD2_SUPPORT_1_8_10","unit":"33-12"},"current_exact_frontier":{"e3_b1_branch_h1_dimension":4,"e3_complete_residue_audit_materialized":false,"e3_dual_pairing_bridge_rank_f2":14,"e3_genuine_full_surface_h2_mu2_lift_materialized":false,"e3_global_H2_mu2_nonexistence_claim":false,"e3_literal_cech_seed_materialized":false,"e3_literal_kummer_function_materialized":false,"e3_literal_picard_divisor_materialized":false,"e3_proper14_is_dual_not_at2_element":true,"e3_proper14_mask_decimal":20,"e3_proper14_support_one_based":[3,5],"e3_retained_at_mod2_quotient_coordinate_f2":[1,0,0,0,0,0,0,1,0,1,0,0,0,0],"e3_retained_at_mod2_quotient_support_one_based":[1,8,10],"e3_retained_at_mod2_solution_unique":true,"j2_adapted_columns_materialized":1,"j2_adapted_columns_total":10,"original_standard_columns_materialized":0},"current_leaf_working_set":["docs/research-os/policies/repository-asset-discovery.md","docs/arsenal/index.json","docs/arsenal/cards/provisional/S33-PW04.md","docs/arsenal/cards/provisional/S33-PW07.md","stages/stage33/33-12/e3-proper14-dual-to-discriminant-quotient-bridge-v89.json","stages/stage33/33-12/e3-direct-cech-seed-contract-v88.json","stages/stage33/33-12/e3-independent-proper14-source-v41.json","stages/stage33/33-12/e3-proper14-boundary-basis-definitions-v45.json","stages/stage33/33-07/picard-discriminant-compact.json","stages/stage33/33-07/proper-brauer2-from-discriminant.json","stages/stage33/33-07/certify_proper_brauer2_from_discriminant.py"],"detailed_machine_authority":"stages/stage33/controller.json","discovery_policy":{"arsenal_index":"docs/arsenal/index.json","current_arsenal_cards":["S33-PW04","S33-PW07"],"each_repeat_requires_materially_new_mathematical_signal":true,"fixed_per_object_search_count_cap":null,"ordinary_order":["ARSENAL","REPEATABLE_BOUNDED_REPOSITORY_SEARCH_WHEN_MATERIALLY_NEW_SIGNAL","CONSTRUCT"],"repeated_bounded_repository_search_allowed":true,"search_miss_proves_mathematical_nonexistence":false,"search_miss_proves_repository_absence":false,"unbounded_repository_search_allowed":false},"execution_gate":{"advance_allowed":true,"advance_scope":"V89A_SOURCE_BIND_RETAINED_AT_MOD2_SUPPORT_1_8_10","next_expected_command":"V89A_SOURCE_BIND_RETAINED_AT_MOD2_SUPPORT_1_8_10_TO_LITERAL_PICARD_DIVISOR_OR_DIRECT_CECH_KUMMER_DATUM","stop_semantics":"LEAF_GATE_ONLY_NOT_ALGORITHM_EXHAUSTION"},"firewalls":{"endpoint_credit":false,"merge_allowed":false,"perfect_cuboid_existence_claim":false,"perfect_cuboid_nonexistence_claim":false,"receiver_credit":false,"stage33_07_reclosed":false,"stage33_08_released":false,"stage33_12_closed_exact":false,"stage33_13_released":false,"theorem_credit":false},"locked_facts":{"picard_discriminant_compact":{"sha256":"4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0"},"proper_brauer2_from_discriminant":{"sha256":"c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"},"v41":{"sha256":"04c6ead2226c87defff085fc641ee80867e1fdf4b07baa28c5e97d2c5e534ac6"},"v45":{"sha256":"a1dafa0be79c80d7275cd2629278bf6a56d6e592f90738316e71ca2689f9feb5"},"v88":{"sha256":"1d8f7b9478f48a3aa2137524180afea0a8e0bbf909e4ece04b1a07ee44d365b7"},"v89":{"sha256":"26bf699fd92e261e1ae40066ad0fd5aece9cb896f28a385367786de1d0460639"}},"resolved_investigations":{"e3_coordinate_conjugate_sign_quotient_family":"CLOSED_EXACT_V85_DO_NOT_REOPEN","e3_direct_cech_seed_contract":"CLOSED_CONTRACT_V88_SEED_UNMATERIALIZED","e3_literal_source_binding":"OPEN_V89A_SUPPORT_1_8_10_TO_LITERAL_GEOMETRY_OR_DIRECT_CECH_KUMMER_DATUM","e3_proper14_dual_to_discriminant_quotient_bridge":"CLOSED_EXACT_V89_UNIQUE_SUPPORT_1_8_10"},"role":"ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE","schema":"STAGE33_MAIN_COMPACT_STATE_V28_V89_DISCRIMINANT_QUOTIENT_BRIDGE_SOURCE_BINDING_ACTIVE","stage33_progress":"6/11"}')
LOCKS={
 D/"e3-independent-proper14-source-v41.json":"04c6ead2226c87defff085fc641ee80867e1fdf4b07baa28c5e97d2c5e534ac6",
 D/"e3-proper14-boundary-basis-definitions-v45.json":"a1dafa0be79c80d7275cd2629278bf6a56d6e592f90738316e71ca2689f9feb5",
 D/"e3-direct-cech-seed-contract-v88.json":"1d8f7b9478f48a3aa2137524180afea0a8e0bbf909e4ece04b1a07ee44d365b7",
 D/"e3-proper14-dual-to-discriminant-quotient-bridge-v89.json":"26bf699fd92e261e1ae40066ad0fd5aece9cb896f28a385367786de1d0460639",
 H/"33-07"/"picard-discriminant-compact.json":"4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0",
 H/"33-07"/"proper-brauer2-from-discriminant.json":"c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
}

def csha(o):
 return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def load(p):
 o=json.loads(p.read_text()); b=dict(o); h=b.pop("canonical_sha256")
 assert h==LOCKS[p]==csha(b), p
 return o

def build(work):
 c=json.loads(CONTROLLER.read_text()); cb=dict(c); ch=cb.pop("projection_canonical_sha256")
 assert ch==csha(cb)
 assert c["schema"]=="STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE"
 assert c["merge_allowed"] is False and c["execution"]["merge_allowed"] is False
 v41=load(D/"e3-independent-proper14-source-v41.json")
 v45=load(D/"e3-proper14-boundary-basis-definitions-v45.json")
 v88=load(D/"e3-direct-cech-seed-contract-v88.json")
 v89=load(D/"e3-proper14-dual-to-discriminant-quotient-bridge-v89.json")
 load(H/"33-07"/"picard-discriminant-compact.json"); load(H/"33-07"/"proper-brauer2-from-discriminant.json")
 assert v41["e3_source"]["proper14_mask_decimal"]==20
 assert v45["non_identification_lock"]["positional_identification_allowed"] is False
 assert v88["bounded_negative_findings"]["proper14_axis_labels_3_and_5_supply_literal_geometry"] is False
 assert v89["dual_pairing_bridge"]["rank_f2"]==14
 assert v89["e3_transport"]["retained_at_mod2_quotient_support_one_based"]==[1,8,10]
 assert v89["e3_transport"]["solution_unique"] is True and v89["next_exact_leaf"]==NEXT
 e=v89["exact_consequence"]
 assert e["dual_coordinate_to_discriminant_quotient_bridge_materialized"] is True
 for k in ("literal_picard_divisor_materialized","literal_kummer_function_materialized","literal_cech_seed_materialized","complete_residue_audit_materialized","genuine_full_surface_h2_mu2_lift_for_e3"):
  assert e[k] is False
 s=dict(BASE); s["controller_projection_canonical_sha256"]=ch; s["work_checkpoint"]=work; s["canonical_sha256"]=csha(s)
 return s

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
 current=json.loads(OUT.read_text()) if OUT.exists() else {}
 work=current.get("work_checkpoint",{"authority":"OPERATIONAL_ONLY_NOT_PROOF","status":"EMPTY"})
 assert work.get("authority")=="OPERATIONAL_ONLY_NOT_PROOF"
 expected=build(work)
 if a.check: assert current==expected
 else: OUT.write_text(json.dumps(expected,sort_keys=True,separators=(",",":"))+"\n")
 print(json.dumps({"success":True,"mode":"check" if a.check else "write","canonical_sha256":expected["canonical_sha256"],"frontier":expected["authority_sync"]["frontier_authority"],"next_exact_leaf":expected["current"]["next_exact_leaf"],"working_set_size":len(expected["current_leaf_working_set"]),"stage33_progress":expected["stage33_progress"],"merge_allowed":expected["firewalls"]["merge_allowed"]},sort_keys=True))

if __name__=="__main__": main()
