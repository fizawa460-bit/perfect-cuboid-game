#!/usr/bin/env python3
"""Certify the post-Smith A_T[2] -> proper-Br2 dual adapter blocker.

The pinned Magma replay now fixes the full-surface A_T[2] element exactly.
This producer checks that its 14 displayed coefficients cannot be reused as
coefficients in the ordered dual proper-Br2 basis: the former is V4-fixed,
while the copied dual vector is not cc-fixed.  It also checks that the finite
discriminant pairing does not recover the missing functional (it sends this
element to zero).  No fake column or historical J2 zero is promoted.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
S33 = HERE.parent
SOURCE = HERE / "j2-semantic-u1-full-surface-smith-source.json"
ORIENTATION = HERE / "j2-cv-d2-semantic-orientation.json"
PROPER = S33 / "33-07" / "proper-brauer2-from-discriminant.json"
TARGET = HERE / "full-surface-pic2-kummer-target.json"
OUT = HERE / "j2-semantic-u1-at2-to-proper-br2-dual-adapter-blocker.json"

LOCKS = {
    SOURCE: "ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec",
    ORIENTATION: "0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e",
    PROPER: "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
    TARGET: "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890",
}


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def locked(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256")
    assert claimed == LOCKS[path] == csha(body), path
    return obj


def rowmul(v, m):
    return [sum(int(v[i]) * int(m[i][j]) for i in range(len(v))) & 1 for j in range(len(m[0]))]


source = locked(SOURCE)
orientation = locked(ORIENTATION)
proper = locked(PROPER)
target = locked(TARGET)

assert orientation["exact_conclusion"]["named_CV_J2_semantic_discriminant_label"] == "u1"
assert source["semantic_u1_pullback"]["BigK_support_1based"] == [2, 4, 9, 10, 47, 49]
at2 = source["exact_normalization"]["full_surface_A_T_2_coordinates_f2"]
assert at2 == [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0]

A_cc = proper["A_T_two_torsion_cc_action_f2"]
A_ct = proper["A_T_two_torsion_ct_action_f2"]
B_cc = proper["proper_Br2_cc_action_f2"]
B_ct = proper["proper_Br2_ct_action_f2"]
assert rowmul(at2, A_cc) == at2 and rowmul(at2, A_ct) == at2

# The proper basis is the ordered dual basis, not the same vector space.  A
# coefficient copy is therefore a shortcut that must pass the dual action; it
# fails cc exactly in the first four coordinates.
copied_cc = rowmul(at2, B_cc)
copied_ct = rowmul(at2, B_ct)
cc_defect = [a ^ b for a, b in zip(copied_cc, at2)]
ct_defect = [a ^ b for a, b in zip(copied_ct, at2)]
assert cc_defect == [1, 0, 1, 1] + [0] * 10
assert ct_defect == [0] * 14

# The order-two discriminant pairing is a valid covector construction, but is
# degenerate here.  It cannot be silently substituted for the missing marked
# Brauer-functional transport.
mods = source["retained_common_smith_source"]["discriminant_moduli"]
b8 = source["retained_common_smith_source"]["discriminant_bilinear_numerator_over_8_reduced"]
scales = [m // 2 for m in mods]
pairing = []
for i in range(14):
    row = []
    for j in range(14):
        numerator = scales[i] * scales[j] * int(b8[i][j])
        assert numerator % 4 == 0
        row.append((numerator // 4) & 1)
    pairing.append(row)
pairing_covector = rowmul(at2, pairing)
assert pairing_covector == [0] * 14

basis10 = target["proper_invariant_domain"]["basis_rows_original_proper_br2_coordinates_f2"]
assert len(basis10) == 10

out = {
    "schema": "STAGE33_12_J2_SEMANTIC_U1_AT2_TO_PROPER_BR2_DUAL_ADAPTER_BLOCKER_V1",
    "stage": "33-12",
    "status": "PASS_EXACT_AT2_MATERIALIZED_PROPER_BR2_DUAL_ADAPTER_STILL_MISSING",
    "source_locks": {
        "semantic_u1_full_surface_smith_source_sha256": LOCKS[SOURCE],
        "semantic_orientation_sha256": LOCKS[ORIENTATION],
        "proper_brauer2_sha256": LOCKS[PROPER],
        "retained_10D_target_basis_sha256": LOCKS[TARGET],
        "actions_run_id": 33445594316,
        "actions_artifact_id": 9777918626,
        "actions_artifact_zip_sha256": "12c5c5aff99aacc81c5cdcc5b8ef15ee2210a288260c6574dfc849c7af454e19",
    },
    "exact_new_progress": {
        "semantic_u1_BigK_support_1based": [2, 4, 9, 10, 47, 49],
        "all_six_full_surface_pullback_rows_materialized": True,
        "literal_retained_Magma_Smith_V_materialized": True,
        "full_surface_A_T_2_coordinate_f2": at2,
        "full_surface_A_T_2_coordinate_weight": sum(at2),
        "full_surface_A_T_2_coordinate_joint_V4_fixed": True,
        "prior_missing_rows_and_Smith_V_blocker_resolved": True,
    },
    "exact_shortcut_rejection": {
        "ordered_proper_Br2_basis_is_dual_not_identical_to_A_T_2_basis": True,
        "copy_A_T_2_coefficients_into_proper_dual_basis_attempt_f2": at2,
        "copied_vector_cc_image_f2": copied_cc,
        "copied_vector_ct_image_f2": copied_ct,
        "copied_vector_cc_invariance_defect_f2": cc_defect,
        "copied_vector_ct_invariance_defect_f2": ct_defect,
        "copied_vector_is_joint_V4_invariant": False,
        "therefore_copied_vector_has_no_retained_10D_coordinate": True,
        "finite_discriminant_pairing_rank_f2": 4,
        "finite_discriminant_pairing_covector_on_semantic_u1_f2": pairing_covector,
        "finite_discriminant_pairing_recovers_named_J2_functional": False,
    },
    "exact_missing_interface": {
        "name": "CORRECTED_KC_BRAUER_FUNCTIONAL_TO_FULL_SURFACE_PROPER_BR2_DUAL_COORDINATE_ADAPTER",
        "required_output": "14 evaluations of corrected named J2 on the retained full-surface T/2T Smith basis, or an equivalent source-locked Brauer pullback/correspondence matrix",
        "not_missing": [
            "named semantic orientation",
            "semantic u1 full-surface A_T[2] element",
            "BigK rows 2,4,9,10,47,49",
            "retained Magma Smith V",
            "proper-Br2 and retained-10D basis definitions",
        ],
        "generic_103D_adapter_ambiguity_reopened": False,
        "proper_Br2_14D_coordinate_materialized": False,
        "retained_10D_coordinate_materialized": False,
        "first_75D_matrix_column_materialized": False,
    },
    "next_exact_leaf": "MATERIALIZE_CORRECTED_KC_BRAUER_FUNCTIONAL_PULLBACK_EVALUATIONS_ON_RETAINED_FULL_SURFACE_T_MOD_2_SMITH_BASIS_THEN_SOLVE_RETAINED10_AND_PLACE_LOCKED_WEIGHT15_TARGET",
    "promotion_firewall": {
        "semantic_u1_assumed_equal_to_proper_Br2_e0": False,
        "A_T_2_coefficients_reused_as_proper_dual_coefficients": False,
        "finite_discriminant_pairing_zero_promoted_as_J2_zero": False,
        "historical_J2_zero_column_reused": False,
        "fake_zero_column_created": False,
        "finite_v4_kummer_columns_materialized": 0,
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "Q_defined_descent_credit_restored": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
    },
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"success": True, "A_T_2_coordinate": at2, "copied_dual_cc_defect": cc_defect, "canonical_sha256": out["canonical_sha256"]}, sort_keys=True))
