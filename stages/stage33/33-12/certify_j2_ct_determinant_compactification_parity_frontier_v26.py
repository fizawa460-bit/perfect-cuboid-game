#!/usr/bin/env python3
"""Certify the exact post-V25 determinant/compactification parity frontier.

This does not select a compactification branch. It proves from source-locked
artifacts that generic norm/residue data alone cannot determine the actual
ct Pic/2 defect, because two compatible compactifications have opposite
determinant parity and a nonzero marked Pic/2 pullback difference.
"""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "j2-ct-determinant-compactification-parity-frontier-v26.json"
LOCKS = {
    "v25_genuine_h2_mu2_adapter": (HERE / "j2-genuine-h2-mu2-kummer-adapter-v25.json", "d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"),
    "ct_norm_splitting_module": (HERE / "j2-corrected-ct-norm-splitting-module.json", "b4c04590fe48141e7555b7c5b4c167a677abe422c7e2b83e51805b4d263d10b2"),
    "ct_norm_picard_support": (HERE / "j2-corrected-ct-norm-picard-support.json", "77af329d2baf2fe807bf23722c9b320fdfddec2bd1df90ced7758d411c9cf021"),
}
NEXT = "DERIVE_ACTUAL_CT_NORM_SPLITTING_CARTIER_DIVISOR_OR_DETERMINANT_LINE_BUNDLE_ON_RESOLVED_QUOTIENT_THEN_PULL_BACK_TO_MARKED_PIC_KC_MOD2_AND_MATERIALIZE_CECH_LOCAL_RANK2_LATTICES_AND_OVERLAP_TRANSITIONS"

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def locked(path, expected):
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj

data = {name: locked(path, digest) for name, (path, digest) in LOCKS.items()}
v25 = data["v25_genuine_h2_mu2_adapter"]
split = data["ct_norm_splitting_module"]
pic = data["ct_norm_picard_support"]

assert v25["status"] == "PASS_EXACT_CURRENT_NAMED_J2_GENUINE_H2_MU2_LIFT_ADAPTER_MATERIALIZED_CONNECTING_COCYCLE_OPEN"
assert v25["remaining_interface"]["actual_cech_local_rank2_lattices_materialized"] is False
assert v25["remaining_interface"]["actual_cc_ct_overlap_transition_matrices_materialized"] is False
assert v25["remaining_interface"]["standard_kummer_columns_materialized"] == 0
assert split["exact_information_boundary"]["compactification_parity_ambiguity_materialized"] is True
assert split["exact_nonuniqueness_witness"]["generic_norm_and_residue_data_unchanged"] is True
assert split["exact_nonuniqueness_witness"]["determinant_parity_E0"] == 0
assert split["exact_nonuniqueness_witness"]["determinant_parity_E1"] == 1
assert split["exact_nonuniqueness_witness"]["pullback_difference_nonzero_mod2"] is True
assert split["standard_auxiliary_q_cover_compactification"]["identified_with_actual_ct_defect_extension"] is False
assert pic["ct_norm_support"]["component_count"] == 8
assert pic["ct_norm_support"]["q_fiber_component_coordinates_materialized"] is True
assert pic["ct_norm_support"]["norm_splitting_cartier_divisor_on_quotient_materialized"] is False
assert pic["ct_norm_support"]["norm_splitting_determinant_line_bundle_on_quotient_materialized"] is False
components = pic["ct_norm_support"]["q_zero_fiber_components"]
assert len(components) == 8
assert {len(c["marked_semantic_PicK_coordinates"]) for c in components} == {20}

w = split["exact_nonuniqueness_witness"]
aux = split["standard_auxiliary_q_cover_compactification"]
out = {
    "schema": "STAGE33_12_J2_CT_DETERMINANT_COMPACTIFICATION_PARITY_FRONTIER_V26",
    "stage": "33-12",
    "status": "PASS_EXACT_GENERIC_SPLITTING_NONUNIQUENESS_ACTUAL_CT_DETERMINANT_CARTIER_FRONTIER_OPEN",
    "source_locks": {name: digest for name, (_, digest) in LOCKS.items()},
    "certified_frontier": {
        "q_zero_component_count": 8,
        "marked_semantic_picard_coordinate_dimension": 20,
        "q_fiber_component_coordinates_materialized": True,
        "generic_norm_and_residue_data_select_actual_pic_mod2_defect": False,
        "generic_nonuniqueness_witness_materialized": True,
        "compatible_determinant_parities": [0, 1],
        "parity_difference_on_quotient": w["parity_difference_on_quotient"],
        "pullback_difference_marked_semantic_PicK_coordinates": w["pullback_difference_marked_semantic_PicK_coordinates"],
        "pullback_difference_nonzero_mod2": True,
        "standard_auxiliary_cover_candidate_determinant": aux["determinant"],
        "standard_auxiliary_cover_candidate_determinant_mod2": aux["determinant_mod2"],
        "standard_auxiliary_cover_identified_with_actual_ct_defect_extension": False,
    },
    "information_boundary": {
        "norm_splitting_cartier_divisor_on_quotient_materialized": False,
        "norm_splitting_determinant_line_bundle_on_quotient_materialized": False,
        "actual_cech_local_rank2_lattices_materialized": False,
        "actual_cc_ct_overlap_transition_matrices_materialized": False,
        "actual_ct_defect_marked_Pic_mod2_materialized": False,
        "pic_mod2_defect_1cocycle_materialized": False,
        "v4_connecting_cocycle_materialized": False,
        "hs_d2_2cocycle_materialized": False,
        "standard_kummer_columns_materialized": 0,
    },
    "exact_conclusion": {
        "generic_splitting_alone_is_insufficient": True,
        "reason": "Two compactifications with unchanged generic norm/residue data have determinant parity 0 and 1, with nonzero marked Pic/2 pullback difference.",
        "no_branch_selected": True,
        "no_terminal_claim": True,
    },
    "next_exact_leaf": NEXT,
    "promotion_firewall": {
        "stage33_progress": "6/11", "stage33_12_closed_exact": False,
        "stage33_07_reclosed": False, "stage33_08_released": False,
        "theorem_credit": False, "receiver_credit": False, "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False, "perfect_cuboid_nonexistence_claim": False,
        "merge_allowed": False,
    },
}
out["canonical_sha256"] = csha(out)
if "--check" in sys.argv:
    assert locked(OUT, out["canonical_sha256"]) == out
else:
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({"success": True, "canonical_sha256": out["canonical_sha256"], "compatible_determinant_parities": [0,1], "actual_determinant_line_bundle_materialized": False, "actual_cech_local_rank2_lattices_materialized": False, "marker": "PROOF_REPLAY_COMPLETE", "next_exact_leaf": NEXT}, sort_keys=True))
