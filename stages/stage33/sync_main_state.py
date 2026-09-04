#!/usr/bin/env python3
"""Generate/check Stage33 MAIN compact state at the exact V65 J1 one-bit discriminator frontier."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

H=Path(__file__).resolve().parent
D=H/"33-12"
ROOT=H.parent.parent
OUT=H/"MAIN-STATE.json"
CONTROLLER_SCHEMA="STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE"
CONTROLLER_SHA="18d8aa4e0ab7a946f5ae5205de2cfddc4b55f867338e92242e5db7cac6f87554"
LOCKS={
"v61":(D/"e3-b1-c22-pic0-2-basis-v61.json","48ec6b2ffb91d549041ff5ec667ff88d493becf01d89e1bb5974134b3b0a53f6"),
"v62":(D/"e3-b1-full-domain-basis-v62.json","353e68438334a0da71dfdbc09a8bf60e7e511598cf54a173338735686f1c3f4c"),
"v63":(D/"e3-b1-c22-kappa-a-literal-cech-lift-v63.json","7714c722f7f30cae1fac03edd34821d1e84372bf3d7663dc2c62a98fde6b186c"),
"v64":(D/"e3-b1-c22-named-torsion-normalization-bridge-v64.json","55679ba16710e3b78ab46ab699ea73ecc3fc56faab4cb7edc5a02e487df3de38"),
"v65":(D/"e3-b1-j1-marked-kc-discriminator-gate-v65.json","7ebef9a6182522f772f198d8c1572acc48cd8441f6158312d1f3f3f2c7fcc01c"),
"j2":(D/"j2-cv-d2-semantic-orientation.json","0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e")}

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def locked(path,expected):
    o=json.loads(path.read_text()); b=dict(o); claimed=b.pop("canonical_sha256")
    assert claimed==expected==csha(b),path
    return o

ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
assert not (H/"MAIN-BATCH-HANDOFF.md").exists()
assert (ROOT/"docs/research-os/policies/repository-asset-discovery.md").is_file()
arsenal=json.loads((ROOT/"docs/arsenal/index.json").read_text())
assert str(arsenal.get("schema","")).startswith("RESEARCH_ARSENAL_")

c=json.loads((H/"controller.json").read_text()); cb=dict(c); controller_sha=cb.pop("projection_canonical_sha256")
assert c["schema"]==CONTROLLER_SCHEMA and controller_sha==CONTROLLER_SHA==csha(cb)
assert c["merge_allowed"] is False and c["execution"]["merge_allowed"] is False

z={k:locked(p,h) for k,(p,h) in LOCKS.items()}
assert [x["class_name"] for x in z["v61"]["ordered_c22_pic0_2_basis"]]==["kappa_A","kappa_D"]
assert [x["class"] for x in z["v62"]["ordered_b1_h1_basis"]]==["cc(kappa_A)","cc(kappa_D)","kappa_A","kappa_D"]
assert z["v63"]["surface_mu2_lift"]["surface_mu2_lift_materialized"] is True
assert z["v63"]["proper14_coordinate_interface"]["column_index"]==3
assert z["v64"]["exact_bridge"]["kappa_A"]["named_torsion"]=="J1"
assert z["v64"]["exact_bridge"]["kappa_D"]["named_torsion"]=="J2"
assert z["v64"]["marked_kc_interface"]["kappa_D"]["coordinate_f2"]==[1,0]
assert z["v64"]["marked_kc_interface"]["kappa_A"]["coordinate_candidates_f2"]==[[0,1],[1,1]]
assert z["v65"]["locked_frontier"]["remaining_ambiguity_bits"]==1
assert z["v65"]["credit_firewall"]["j1_marked_kc_coordinate_selected"] is False
mn=z["j2"]["kernel_fingerprint_identification"]["minimum_norm_to_functional"]
assert mn["4"]==[0,1] and mn["12"]==[1,1]

p58=json.loads((D/"e3-search-routing-supersession-v58.json").read_text())
assert p58["routing_contract"]["arsenal_first"] is True
assert p58["routing_contract"]["fixed_per_object_search_count_cap"] is None
assert p58["routing_contract"]["repeated_bounded_repository_search_allowed"] is True

out=json.loads(r"""{"anti_loop_policy":{"do_not_relabel_j2_specific_twisted_kernel_as_j1":true,"do_not_reuse_contact_bits_as_marked_kc_bits":true,"do_not_use_arbitrary_gl2_complement":true,"do_not_use_source_automorphism_without_exact_target_action":true},"authority_sync":{"controller_current_leaf_is_pre_v61_legacy":true,"controller_current_leaf_projection_synchronized":false,"controller_global_authority_locked":true,"frontier_authority":"V65_J1_ONE_BIT_DISCRIMINATOR_GATE","mathematical_authority":"V25_V36_EXACT_CERTIFICATE_CHAIN_PLUS_BRANCH_E3_V41_V57_V61_V65","operational_routing_authority":"V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP","status":"V65_BRANCH_EXACT_FRONTIER_PROJECTED_CONTROLLER_GLOBAL_FIREWALLS_LOCKED","supersession_scope":"BRANCH_CURRENT_LEAF_ONLY_NO_CONTROLLER_GLOBAL_CREDIT_CHANGE"},"branch_exact_frontier_authority":"stages/stage33/33-12/e3-b1-j1-marked-kc-discriminator-gate-v65.json","controller_projection_canonical_sha256":"18d8aa4e0ab7a946f5ae5205de2cfddc4b55f867338e92242e5db7cac6f87554","controller_schema":"STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE","current":{"active_missing_interface":"J1_MARKED_KC_IMAGE_ONE_BIT_DISCRIMINATOR","logical_internal_branch":"33-13_FINITE_V4_KUMMER_MATRIX_REPAIR","next_exact_leaf":"RESOLVE_J1_IMAGE_BETWEEN_u2_AND_u1_PLUS_u2_BY_ONE_EXACT_MARKED_TRANSPORT_OR_INDEPENDENT_SOURCE_SIDE_FINGERPRINT_THEN_DECODE_PROPER14_COLUMN3","substep":"E3_A2_4B_RESOLVE_C22_KAPPA_A_MARKED_KC_COLUMN3","unit":"33-12"},"current_exact_frontier":{"J1_marked_kc_coordinate_candidates_f2":[[0,1],[1,1]],"J1_marked_kc_remaining_ambiguity_bits":1,"J2_marked_kc_coordinate_f2":[1,0],"e3_b1_branch_h1_dimension":4,"e3_b1_column3_literal_symbol_materialized":true,"e3_b1_column3_marked_coordinate_materialized":false,"e3_b1_column4_proper14_mask_decimal":25,"e3_b1_membership_status":"OPEN_NOT_COMPUTED","e3_b1_ordered_domain_basis":["cc(kappa_A)","cc(kappa_D)","kappa_A","kappa_D"],"e3_genuine_full_surface_h2_mu2_lift_materialized":false,"e3_proper14_mask_decimal":20,"j2_adapted_columns_materialized":1,"j2_adapted_columns_total":10,"kappa_A_named_torsion":"J1","kappa_D_named_torsion":"J2","original_standard_columns_materialized":0,"target_minimum_norm_fingerprint":{"u1+u2":12,"u2":4}},"current_leaf_working_set":["docs/research-os/policies/repository-asset-discovery.md","docs/arsenal/index.json","docs/arsenal/cards/provisional/S33-PW04.md","docs/arsenal/cards/provisional/S33-PW07.md","stages/stage33/ROADMAP-33-12-V65-J1-DISCRIMINATOR.md","stages/stage33/33-12/e3-b1-j1-marked-kc-discriminator-gate-v65.json","stages/stage33/33-12/e3-b1-c22-named-torsion-normalization-bridge-v64.json","stages/stage33/33-12/j2-cv-d2-semantic-orientation.json"],"detailed_machine_authority":"stages/stage33/controller.json","discovery_policy":{"arsenal_index":"docs/arsenal/index.json","current_arsenal_cards":["S33-PW04","S33-PW07"],"each_repeat_requires_materially_new_mathematical_signal":true,"effective_routing_override":"stages/stage33/33-12/e3-search-routing-supersession-v58.json","fixed_per_object_search_count_cap":null,"ordinary_order":["ARSENAL","REPEATABLE_BOUNDED_REPOSITORY_SEARCH_WHEN_MATERIALLY_NEW_SIGNAL","CONSTRUCT"],"repeated_bounded_repository_search_allowed":true,"search_miss_proves_mathematical_nonexistence":false,"search_miss_proves_repository_absence":false,"unbounded_repository_search_allowed":false},"execution_gate":{"advance_allowed":true,"advance_scope":"A2_4B_J1_ONE_BIT_DISCRIMINATOR_WITH_EXACT_TRANSPORT_OR_INDEPENDENT_SOURCE_FINGERPRINT","next_expected_command":"ARSENAL_FIRST_FOR_EXACT_J1_DISCRIMINATOR_THEN_CONSTRUCT_ONE_SOURCE_LOCKED_TRANSPORT_OR_FINGERPRINT","stop_semantics":"LEAF_GATE_ONLY_NOT_ALGORITHM_EXHAUSTION"},"firewalls":{"endpoint_credit":false,"merge_allowed":false,"perfect_cuboid_existence_claim":false,"perfect_cuboid_nonexistence_claim":false,"receiver_credit":false,"stage33_07_reclosed":false,"stage33_08_released":false,"stage33_12_closed_exact":false,"stage33_13_released":false,"theorem_credit":false},"locked_facts":{"v61":{"sha256":"48ec6b2ffb91d549041ff5ec667ff88d493becf01d89e1bb5974134b3b0a53f6"},"v62":{"sha256":"353e68438334a0da71dfdbc09a8bf60e7e511598cf54a173338735686f1c3f4c"},"v63":{"sha256":"7714c722f7f30cae1fac03edd34821d1e84372bf3d7663dc2c62a98fde6b186c"},"v64":{"sha256":"55679ba16710e3b78ab46ab699ea73ecc3fc56faab4cb7edc5a02e487df3de38"},"v65":{"sha256":"7ebef9a6182522f772f198d8c1572acc48cd8441f6158312d1f3f3f2c7fcc01c"}},"resolved_investigations":{"b1_c22_pic0_2_basis":"CLOSED_EXACT_V61_DO_NOT_REOPEN","b1_full_ordered_domain_basis":"CLOSED_EXACT_V62_DO_NOT_REOPEN","j1_marked_kc_image":"OPEN_EXACTLY_ONE_BIT_V65","kappa_A_literal_cech_surface_lift":"CLOSED_EXACT_V63_DO_NOT_REOPEN","kappa_A_named_torsion":"CLOSED_EXACT_J1_V64_DO_NOT_REOPEN","kappa_D_named_torsion_and_marked_orientation":"CLOSED_EXACT_J2_TO_U1_V64_DO_NOT_REOPEN"},"role":"ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE","schema":"STAGE33_MAIN_COMPACT_STATE_V21_V65_J1_ONE_BIT_DISCRIMINATOR_ACTIVE","stage33_progress":"6/11","work_checkpoint":{"authority":"OPERATIONAL_ONLY_NOT_PROOF","status":"EMPTY"}}""")
assert out["controller_projection_canonical_sha256"]==controller_sha
out["canonical_sha256"]=csha(out)
rendered=json.dumps(out,sort_keys=True,separators=(",",":"))+"\n"
if a.check:
    assert OUT.exists() and OUT.read_text()==rendered,"MAIN-STATE.json is stale; run sync_main_state.py"
    mode="check"
else:
    OUT.write_text(rendered); mode="write"
print(json.dumps({"success":True,"mode":mode,"canonical_sha256":out["canonical_sha256"],"current_leaf":out["current"]["active_missing_interface"],"stop_semantics":out["execution_gate"]["stop_semantics"],"merge_allowed":False},sort_keys=True))
