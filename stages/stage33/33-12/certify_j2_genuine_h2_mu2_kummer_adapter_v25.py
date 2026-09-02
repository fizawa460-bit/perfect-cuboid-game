#!/usr/bin/env python3
"""Reattach the exact V21 named J2 source to the existing genuine Cech H2(mu2) lift.

This is source-first. It does not revive the revoked weight-15 raw H1 target,
C2+C3, or historical named Kummer glue. V21 supplies the current named
beta1 source; the existing corrected-J2 Cech certificate supplies lambda_D.
V25 only composes those exact interfaces and leaves the Pic/2/V4 defect open.
"""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "j2-genuine-h2-mu2-kummer-adapter-v25.json"
LOCKS = {
    "v21_named_source": (HERE / "j2-order4-swap-functional-source-v21.json", "19c464602d6ad1b6c32b0b08c50a6bcc55b8e606642a5ae52e7f51fdc2f12366"),
    "v24_raw_h1_scope_firewall": (HERE / "j2-raw-h1-not-kummer-target-v24.json", "9d104c7d4054b5d92f1df382654b152c30ca0be6ef267aa028fe8b9d78a4687d"),
    "explicit_cech_mu2_lift": (HERE / "j2-corrected-explicit-cech-mu2-lift.json", "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b"),
    "surface_mu2_boundary_contract": (HERE / "j2-full-surface-mu2-zero-defect-contract.json", "55cd01cc8570cb759e7029ddef3b9dac764625a7cdd313c76fd694e37fd478ce"),
    "ct_norm_splitting_module": (HERE / "j2-corrected-ct-norm-splitting-module.json", "b4c04590fe48141e7555b7c5b4c167a677abe422c7e2b83e51805b4d263d10b2"),
}
NEXT = "MATERIALIZE_ACTUAL_CECH_LOCAL_RANK2_LATTICES_AND_OVERLAP_TRANSITION_MATRICES_FOR_LAMBDA_D_AT_T0_TINF_SINF_C21_C22_AND_RESOLUTION_EXCEPTIONALS_THEN_COMPARE_CC_CT_NULLHOMOTOPIES_AND_COMPUTE_MARKED_PIC_MOD2_AND_HS_D2"

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def locked(path, expected):
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj

data = {name: locked(path, digest) for name, (path, digest) in LOCKS.items()}
v21 = data["v21_named_source"]
v24 = data["v24_raw_h1_scope_firewall"]
explicit = data["explicit_cech_mu2_lift"]
boundary = data["surface_mu2_boundary_contract"]
split = data["ct_norm_splitting_module"]
assert v21["status"] == "PASS_EXACT_SOURCE_FIRST_NAMED_FUNCTIONAL_MATERIALIZED"
assert v21["named_order4_functional_behavior"]["named_binary_functional"] == "beta1"
assert v21["named_order4_functional_behavior"]["named_binary_functional_coordinate_f2"] == [1, 0]
assert v21["named_full_surface_source"]["proper14_mask_decimal"] == 25
assert v21["named_full_surface_source"]["retained10_mask_decimal"] == 6
assert v21["named_full_surface_source"]["two_bit_value_a_b"] == [0, 1]
assert v21["named_full_surface_source"]["source_coordinate_materialized"] is True
assert v21["exact_geometric_equivariance"]["projection"] == "forget c"
assert v21["exact_geometric_equivariance"]["pullback_naturality_applies"] is True
assert v24["exact_scope_separation"]["raw_cech_H1_may_be_used_as_named_kummer_boundary"] is False
assert v24["supersession"]["old_weight15_vector_revoked_as_named_kummer_matrix_target"] is True
assert v24["promotion_firewall"]["standard_columns_materialized"] == 0
assert explicit["status"] == "PASS_EXACT_EXPLICIT_CECH_SYMBOL_PREIMAGE_AND_SURFACE_MU2_LIFT_PIC_COORDINATES_OPEN"
assert explicit["explicit_cech_preimage"]["concrete_Cech_preimage_e_D_materialized"] is True
assert explicit["surface_mu2_lift"]["genuine_surface_H2_mu2_lift_materialized"] is True
assert explicit["surface_mu2_lift"]["historical_kummer_glue_used"] is False
assert "J2=(f2,1)" in explicit["surface_mu2_lift"]["brauer_image"]
assert boundary["exact_input"]["marked_brauer_coordinate"] == [1, 0]
assert "J2=(f2,1)" in boundary["exact_input"]["class"]
assert boundary["kummer_exact_sequence"]["full_surface_mu2_lift_for_corrected_J2_materialized"] is True
assert boundary["retired_historical_credit"]["historical_named_kummer_glue_producer_tombstoned"] is True
assert v21["named_order4_functional_behavior"]["named_binary_functional_coordinate_f2"] == boundary["exact_input"]["marked_brauer_coordinate"] == [1, 0]
assert split["exact_information_boundary"]["actual_lambda_D_local_rank2_lattices_materialized"] is False
assert split["exact_information_boundary"]["actual_cc_ct_overlap_transition_matrices_materialized"] is False
assert split["next_exact_leaf"] == NEXT
out = {
    "schema": "STAGE33_12_J2_GENUINE_H2_MU2_KUMMER_ADAPTER_V25",
    "stage": "33-12",
    "status": "PASS_EXACT_CURRENT_NAMED_J2_GENUINE_H2_MU2_LIFT_ADAPTER_MATERIALIZED_CONNECTING_COCYCLE_OPEN",
    "source_locks": {name: digest for name, (_, digest) in LOCKS.items()},
    "current_named_source": {"named_binary_functional":"beta1","marked_brauer_coordinate_f2":[1,0],"proper14_mask_decimal":25,"retained10_mask_decimal":6,"two_bit_value_a_b":[0,1],"source_coordinate_materialized":True,"source_first":True,"kc_to_full_surface_projection":"forget c","pullback_naturality_applies":True},
    "genuine_h2_mu2_adapter": {"named_source_and_cech_lift_identified_by_same_marked_brauer_coordinate":True,"kc_surface":"minimal resolution Kc_tilde_bar","kc_lift_class":"lambda_D=alpha(e_D), represented generically by {f2,g22}","kc_lift_brauer_image":"corrected J2=(f2,1)","explicit_cech_preimage_e_D_materialized":True,"genuine_kc_surface_h2_mu2_lift_materialized":True,"full_surface_lift":"pull back lambda_D along the exact V21 projection forget c","full_surface_named_j2_h2_mu2_lift_materialized":True,"historical_kummer_glue_used":False,"raw_weight15_h1_used_as_kummer_boundary":False,"revoked_c2_plus_c3_relation_used":False},
    "supersession": {"v24_raw_h1_scope_firewall_retained":True,"v24_old_weight15_target_remains_revoked":True,"v24_missing_genuine_lift_adapter_resolved_by_v25":True,"historical_named_kummer_glue_restored":False,"standard_kummer_column_materialized":False,"named_source_to_old_raw_h1_target_relation_restored":False},
    "remaining_interface": {"actual_cech_local_rank2_lattices_materialized":False,"actual_cc_ct_overlap_transition_matrices_materialized":False,"pic_mod2_defect_1cocycle_materialized":False,"v4_connecting_cocycle_materialized":False,"hs_d2_2cocycle_materialized":False,"standard_kummer_columns_materialized":0,"next_exact_leaf":NEXT},
    "promotion_firewall": {"stage33_progress":"6/11","stage33_12_closed_exact":False,"stage33_07_reclosed":False,"stage33_08_released":False,"theorem_credit":False,"receiver_credit":False,"endpoint_credit":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False,"merge_allowed":False},
}
out["canonical_sha256"] = csha(out)
if "--check" in sys.argv:
    assert locked(OUT, out["canonical_sha256"]) == out
else:
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({"success":True,"canonical_sha256":out["canonical_sha256"],"named_source_mask":6,"genuine_h2_mu2_lift_adapter_materialized":True,"v4_connecting_cocycle_materialized":False,"standard_kummer_columns_materialized":0,"next_exact_leaf":NEXT,"marker":"PROOF_REPLAY_COMPLETE"}, sort_keys=True))
