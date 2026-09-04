#!/usr/bin/env python3
"""Generate/check Stage33 MAIN compact state at the exact V71 J1 CV-cocycle frontier."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parent
D = H / "33-12"
ROOT = H.parent.parent
OUT = H / "MAIN-STATE.json"
CONTROLLER_SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE"
CONTROLLER_SHA = "18d8aa4e0ab7a946f5ae5205de2cfddc4b55f867338e92242e5db7cac6f87554"
STATE_SHA = "bc57b431eec982d1a9dd95f39f8777351425485ac266fc60c45198b9b79e7c06"
V69_BLOB = "77638f2f3afb2dc6445f5130addcd52e88bc5767"
V71_SHA = "3e9409ee7537ab4edb12e2416745bbd074f1cc1b02a4fc8a92be643075b8569a"

STATE_TEXT = r'''{"anti_loop_policy":{"do_not_identify_contact_frame_with_marked_kc_frame":true,"do_not_relabel_j2_specific_translation_torsor_or_twisted_kernel_as_j1":true,"do_not_reuse_contact_bits_as_marked_kc_bits":true,"do_not_use_arbitrary_gl2_complement":true,"do_not_use_source_automorphism_without_exact_target_action":true},"authority_sync":{"controller_current_leaf_is_pre_v61_legacy":true,"controller_current_leaf_projection_synchronized":false,"controller_global_authority_locked":true,"frontier_authority":"V71_J1_SPECIFIC_CV_E2_COCYCLE","mathematical_authority":"V25_V36_EXACT_CERTIFICATE_CHAIN_PLUS_BRANCH_E3_V41_V57_V61_V71","operational_routing_authority":"V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP","status":"V71_BRANCH_EXACT_FRONTIER_PROJECTED_CONTROLLER_GLOBAL_FIREWALLS_LOCKED","supersession_scope":"BRANCH_CURRENT_LEAF_ONLY_NO_CONTROLLER_GLOBAL_CREDIT_CHANGE"},"branch_exact_frontier_authority":"stages/stage33/33-12/e3-b1-c22-j1-cv-e2-cocycle-v71.json","canonical_sha256":"bc57b431eec982d1a9dd95f39f8777351425485ac266fc60c45198b9b79e7c06","controller_projection_canonical_sha256":"18d8aa4e0ab7a946f5ae5205de2cfddc4b55f867338e92242e5db7cac6f87554","controller_schema":"STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE","current":{"active_missing_interface":"J1_TRANSLATION_TORSOR_AND_TWISTED_KERNEL_FINGERPRINT","logical_internal_branch":"33-13_FINITE_V4_KUMMER_MATRIX_REPAIR","next_exact_leaf":"D2_MATERIALIZE_J1_TRANSLATION_TORSOR_WITH_d_f1_THEN_COMPUTE_INDEPENDENT_MINIMUM_NORM_4_OR_12","substep":"E3_A2_4B_D2_J1_TRANSLATION_TORSOR_FROM_EXACT_CV_COCYCLE","unit":"33-12"},"current_exact_frontier":{"J1_marked_kc_coordinate_candidates_f2":[[0,1],[1,1]],"J1_marked_kc_remaining_ambiguity_bits":1,"J2_marked_kc_coordinate_f2":[1,0],"contact_to_marked_transport_candidates":["identity","shear_fixing_u1"],"e3_b1_branch_h1_dimension":4,"e3_b1_column3_literal_symbol_materialized":true,"e3_b1_column3_marked_coordinate_materialized":false,"e3_b1_column4_proper14_mask_decimal":25,"e3_b1_membership_status":"OPEN_NOT_COMPUTED","e3_b1_ordered_domain_basis":["cc(kappa_A)","cc(kappa_D)","kappa_A","kappa_D"],"e3_genuine_full_surface_h2_mu2_lift_materialized":false,"e3_proper14_mask_decimal":20,"j1_cv_cocycle_bits_in_fixed_E2_basis":[0,1],"j1_cv_full_L_pair":"(f1,1)","j1_cv_splitting_field":"Kgeom(sqrt(f1))","j1_cv_translation_point":"Tr=(r,0)","j1_translation_torsor_materialized":false,"j1_twisted_kernel_minimum_norm_materialized":false,"j2_adapted_columns_materialized":1,"j2_adapted_columns_total":10,"kappa_A_named_torsion":"J1","kappa_D_named_torsion":"J2","original_standard_columns_materialized":0,"target_minimum_norm_fingerprint":{"u1+u2":12,"u2":4}},"current_leaf_working_set":["docs/research-os/policies/repository-asset-discovery.md","docs/arsenal/index.json","docs/arsenal/cards/provisional/S33-PW04.md","docs/arsenal/cards/provisional/S33-PW07.md","stages/stage33/ROADMAP-33-12-V71-J1-TORSOR.md","stages/stage33/33-12/e3-b1-c22-j1-marked-kc-one-bit-transport-gate-v69.json","stages/stage33/33-12/e3-b1-c22-j1-cv-e2-cocycle-v71.json","stages/stage33/33-05/j2-r4-correct-translation-torsor.json","stages/stage33/33-12/j2-cv-d2-semantic-orientation.json"],"detailed_machine_authority":"stages/stage33/controller.json","discovery_policy":{"arsenal_index":"docs/arsenal/index.json","current_arsenal_cards":["S33-PW04","S33-PW07"],"each_repeat_requires_materially_new_mathematical_signal":true,"effective_routing_override":"stages/stage33/33-12/e3-search-routing-supersession-v58.json","fixed_per_object_search_count_cap":null,"ordinary_order":["ARSENAL","REPEATABLE_BOUNDED_REPOSITORY_SEARCH_WHEN_MATERIALLY_NEW_SIGNAL","CONSTRUCT"],"repeated_bounded_repository_search_allowed":true,"search_miss_proves_mathematical_nonexistence":false,"search_miss_proves_repository_absence":false,"unbounded_repository_search_allowed":false},"execution_gate":{"advance_allowed":true,"advance_scope":"A2_4B_D2_J1_TRANSLATION_TORSOR_AND_INDEPENDENT_MINIMUM_NORM","next_expected_command":"MATERIALIZE_J1_TRANSLATION_TORSOR_FROM_V71_COCYCLE_USING_S33_PW07_THEN_COMPUTE_J1_SPECIFIC_KERNEL_FINGERPRINT","stop_semantics":"LEAF_GATE_ONLY_NOT_ALGORITHM_EXHAUSTION"},"firewalls":{"endpoint_credit":false,"merge_allowed":false,"perfect_cuboid_existence_claim":false,"perfect_cuboid_nonexistence_claim":false,"receiver_credit":false,"stage33_07_reclosed":false,"stage33_08_released":false,"stage33_12_closed_exact":false,"stage33_13_released":false,"theorem_credit":false},"locked_facts":{"v61":{"sha256":"48ec6b2ffb91d549041ff5ec667ff88d493becf01d89e1bb5974134b3b0a53f6"},"v62":{"sha256":"353e68438334a0da71dfdbc09a8bf60e7e511598cf54a173338735686f1c3f4c"},"v63":{"sha256":"7714c722f7f30cae1fac03edd34821d1e84372bf3d7663dc2c62a98fde6b186c"},"v64":{"sha256":"55679ba16710e3b78ab46ab699ea73ecc3fc56faab4cb7edc5a02e487df3de38"},"v65":{"sha256":"7ebef9a6182522f772f198d8c1572acc48cd8441f6158312d1f3f3f2c7fcc01c"},"v68":{"blob_sha1":"9453000948593f21198ecfdff0ccce64d1c8ffd9"},"v69":{"blob_sha1":"77638f2f3afb2dc6445f5130addcd52e88bc5767"},"v71":{"sha256":"3e9409ee7537ab4edb12e2416745bbd074f1cc1b02a4fc8a92be643075b8569a"}},"resolved_investigations":{"b1_c22_pic0_2_basis":"CLOSED_EXACT_V61_DO_NOT_REOPEN","b1_full_ordered_domain_basis":"CLOSED_EXACT_V62_DO_NOT_REOPEN","j1_cv_e2_cocycle":"CLOSED_EXACT_V71_DO_NOT_REOPEN","j1_marked_kc_image":"OPEN_EXACTLY_ONE_BIT_V69","j1_translation_torsor":"OPEN_FROM_V71","j1_transport_reduction":"CLOSED_EXACT_ONE_BIT_V69_DO_NOT_REOPEN","kappa_A_literal_cech_surface_lift":"CLOSED_EXACT_V63_DO_NOT_REOPEN","kappa_A_named_torsion":"CLOSED_EXACT_J1_V64_DO_NOT_REOPEN","kappa_D_named_torsion_and_marked_orientation":"CLOSED_EXACT_J2_TO_U1_V64_DO_NOT_REOPEN"},"role":"ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE","schema":"STAGE33_MAIN_COMPACT_STATE_V22_V71_J1_CV_COCYCLE_TORSOR_ACTIVE","stage33_progress":"6/11","work_checkpoint":{"authority":"OPERATIONAL_ONLY_NOT_PROOF","status":"EMPTY"}}
'''

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def locked_json(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj

ap = argparse.ArgumentParser()
ap.add_argument("--check", action="store_true")
a = ap.parse_args()

assert not (H / "MAIN-BATCH-HANDOFF.md").exists()
assert (ROOT / "docs/research-os/policies/repository-asset-discovery.md").is_file()
assert (ROOT / "docs/arsenal/index.json").is_file()
assert (ROOT / "docs/arsenal/cards/provisional/S33-PW04.md").is_file()
assert (ROOT / "docs/arsenal/cards/provisional/S33-PW07.md").is_file()
assert (H / "ROADMAP-33-12-V71-J1-TORSOR.md").is_file()

controller = json.loads((H / "controller.json").read_text(encoding="utf-8"))
cb = dict(controller)
controller_sha = cb.pop("projection_canonical_sha256")
assert controller["schema"] == CONTROLLER_SCHEMA
assert controller_sha == CONTROLLER_SHA == csha(cb)
assert controller["merge_allowed"] is False
assert controller["execution"]["merge_allowed"] is False

v69 = D / "e3-b1-c22-j1-marked-kc-one-bit-transport-gate-v69.json"
assert git_blob_sha(v69) == V69_BLOB
v69_obj = json.loads(v69.read_text(encoding="utf-8"))
assert v69_obj["d2_verdict"] == "OPEN_ONE_BIT"
assert len(v69_obj["transport_reduction"]["candidate_transports_contact_to_marked"]) == 2

v71 = locked_json(D / "e3-b1-c22-j1-cv-e2-cocycle-v71.json", V71_SHA)
assert v71["cv_cocycle"]["xi_rho"] == "Tr"
assert v71["cv_cocycle"]["cocycle_bits_in_fixed_basis"] == [0, 1]
assert v71["credit_firewall"]["identity_vs_shear_selected"] is False
assert v71["credit_firewall"]["j1_translation_torsor_materialized"] is False

routing = json.loads((D / "e3-search-routing-supersession-v58.json").read_text(encoding="utf-8"))
assert routing["routing_contract"]["arsenal_first"] is True
assert routing["routing_contract"]["repeated_bounded_repository_search_allowed"] is True
assert routing["routing_contract"]["fixed_per_object_search_count_cap"] is None

state = json.loads(STATE_TEXT)
body = dict(state)
claimed = body.pop("canonical_sha256")
assert claimed == STATE_SHA == csha(body)
assert state["controller_projection_canonical_sha256"] == controller_sha
assert state["current"]["active_missing_interface"] == "J1_TRANSLATION_TORSOR_AND_TWISTED_KERNEL_FINGERPRINT"
assert state["execution_gate"]["advance_allowed"] is True
assert state["firewalls"]["merge_allowed"] is False

if a.check:
    assert OUT.exists() and OUT.read_text(encoding="utf-8") == STATE_TEXT, "MAIN-STATE.json is stale; run sync_main_state.py"
    mode = "check"
else:
    OUT.write_text(STATE_TEXT, encoding="utf-8")
    mode = "write"

print(json.dumps({
    "success": True,
    "mode": mode,
    "canonical_sha256": STATE_SHA,
    "current_leaf": state["current"]["active_missing_interface"],
    "frontier": state["authority_sync"]["frontier_authority"],
    "advance_allowed": True,
    "merge_allowed": False,
}, sort_keys=True))
