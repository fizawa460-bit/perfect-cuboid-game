#!/usr/bin/env python3
"""Build or verify the compact Stage33 MAIN startup state.

The full controller remains the detailed machine authority.  This projection
contains only the fields and exact interfaces needed to start an ordinary MAIN
batch without rereading compatibility shims or historical repair state.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTROLLER = HERE / "controller.json"
ORIENTATION = HERE / "33-12" / "j2-cv-d2-semantic-orientation.json"
PROPER14 = HERE / "33-07" / "proper-brauer2-from-discriminant.json"
TARGET_BASIS = HERE / "33-12" / "full-surface-pic2-kummer-target.json"
NAMED_TARGET = HERE / "33-12" / "j2-named-v4-h1-target-before-source-orientation.json"
U1_SMITH_SOURCE = HERE / "33-12" / "j2-semantic-u1-full-surface-smith-source.json"
U1_DUAL_BLOCKER = HERE / "33-12" / "j2-semantic-u1-at2-to-proper-br2-dual-adapter-blocker.json"
ORDER4 = HERE / "33-12" / "j2-order4-brauer-lift-reduction.json"
OUT = HERE / "MAIN-STATE.json"

LOCKS = {
    ORIENTATION: "0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e",
    PROPER14: "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
    TARGET_BASIS: "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890",
    NAMED_TARGET: "4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3",
    U1_SMITH_SOURCE: "ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec",
    U1_DUAL_BLOCKER: "f5d1336e21dd5563ec6466811b5e1c3cacc6def17e4dbe4968023d9bd3756399",
    ORDER4: "a524121930e1c712bd8d8220415ef1836b11cd6eb11f2bb44f70dc844f6d85b0",
}


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def locked(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == LOCKS[path] == csha(body), path
    return obj


controller = json.loads(CONTROLLER.read_text(encoding="utf-8"))
orientation = locked(ORIENTATION)
proper14 = locked(PROPER14)
target_basis = locked(TARGET_BASIS)
named_target = locked(NAMED_TARGET)
u1_smith_source = locked(U1_SMITH_SOURCE)
u1_dual_blocker = locked(U1_DUAL_BLOCKER)
order4 = locked(ORDER4)

current = controller["current"]
stage = controller["stage33_12"]
conclusion = orientation["exact_conclusion"]
target = named_target["retained_H1_projection"]
domain = target_basis["proper_invariant_domain"]
assert conclusion["orientation_materialized"] is True
assert conclusion["named_CV_J2_semantic_discriminant_label"] == "u1"
assert conclusion["named_CV_J2_fixed_marked_Kc_coordinate_f2"] == [1, 0]
assert conclusion["semantic_candidate_count_before"] == 3
assert conclusion["semantic_candidate_count_after"] == 1
assert orientation["firewalls"]["Br2_identified_canonically_with_A_T_2torsion"] is False
assert orientation["firewalls"]["proper_Br2_14D_coordinate_guessed"] is False
assert domain["dimension_f2"] == 10
assert len(domain["basis_rows_original_proper_br2_coordinates_f2"]) == 10
assert proper14["proper_geometric_Br2_dimension_f2"] == 14
assert target["retained_H1_dimension_f2"] == 75
assert target["coordinate_weight"] == 15 and target["nonzero"] is True
normalization = u1_smith_source["exact_normalization"]
progress = u1_dual_blocker["exact_new_progress"]
missing_dual = u1_dual_blocker["exact_missing_interface"]
shortcut = u1_dual_blocker["exact_shortcut_rejection"]
assert progress["semantic_u1_BigK_support_1based"] == [2, 4, 9, 10, 47, 49]
assert progress["all_six_full_surface_pullback_rows_materialized"] is True
assert progress["literal_retained_Magma_Smith_V_materialized"] is True
assert normalization["full_surface_A_T_2_coordinates_f2"] == [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0]
assert shortcut["copied_vector_is_joint_V4_invariant"] is False
assert missing_dual["proper_Br2_14D_coordinate_materialized"] is False
assert order4["next_numeric_leaf"]["materialize_additional_BigK_pullback_rows_1based"] == [20, 35, 39, 67]
assert order4["promotion_firewall"]["proper_Br2_14D_coordinate_materialized"] is False

coordinates = target["coordinates_f2"]
out = {
    "schema": "STAGE33_MAIN_COMPACT_STATE_V4",
    "role": "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE",
    "detailed_machine_authority": "stages/stage33/controller.json",
    "controller_schema": controller["schema"],
    "stage33_progress": controller["stage33_progress"],
    "current": {
        "unit": current["unit"],
        "logical_internal_branch": current["logical_internal_branch"],
        "substep": current["substep"],
        "active_missing_interface": current["active_missing_interface"],
        "next_exact_leaf": current["next_exact_leaf"],
    },
    "exact_reusable_inputs": {
        "named_J2_semantic_orientation": {
            "materialized": True,
            "label": "u1",
            "fixed_marked_Kc_coordinate_f2": [1, 0],
            "certificate": "stages/stage33/33-12/j2-cv-d2-semantic-orientation.json",
            "canonical_sha256": LOCKS[ORIENTATION],
        },
        "proper_Br2_source": {
            "ambient_dimension_f2": 14,
            "retained_invariant_dimension_f2": 10,
            "retained_10D_basis_rows_in_proper14_coordinates_f2": domain[
                "basis_rows_original_proper_br2_coordinates_f2"
            ],
            "retained_basis_sha256": domain["basis_sha256"],
            "proper14_certificate": "stages/stage33/33-07/proper-brauer2-from-discriminant.json",
            "proper14_canonical_sha256": LOCKS[PROPER14],
            "target_basis_canonical_sha256": LOCKS[TARGET_BASIS],
        },
        "named_J2_locked_target": {
            "ambient_dimension_f2": 75,
            "coordinate_weight": 15,
            "nonzero": True,
            "coordinates_f2": coordinates,
            "certificate": "stages/stage33/33-12/j2-named-v4-h1-target-before-source-orientation.json",
            "canonical_sha256": LOCKS[NAMED_TARGET],
        },
        "semantic_u1_full_surface_smith_normalization": {
            "formula_materialized": True,
            "semantic_support_BigK_indices_1based": progress["semantic_u1_BigK_support_1based"],
            "required_rows_missing_1based": [],
            "retained_Magma_Smith_V_materialized": True,
            "integral_dual_quotient_representative_z": normalization["integral_dual_quotient_representative_z"],
            "magma_smith_convention": normalization["formula"],
            "full_surface_A_T_2_coordinates_f2": normalization["full_surface_A_T_2_coordinates_f2"],
            "certificate": (
                "stages/stage33/33-12/"
                "j2-semantic-u1-full-surface-smith-source.json"
            ),
            "canonical_sha256": LOCKS[U1_SMITH_SOURCE],
        },
        "semantic_u1_to_proper_Br2_dual_blocker": {
            "copied_A_T_2_coefficients_rejected": True,
            "copied_dual_cc_invariance_defect_f2": shortcut["copied_vector_cc_invariance_defect_f2"],
            "active_missing_interface": missing_dual["name"],
            "certificate": "stages/stage33/33-12/j2-semantic-u1-at2-to-proper-br2-dual-adapter-blocker.json",
            "canonical_sha256": LOCKS[U1_DUAL_BLOCKER],
        },
        "j2_order4_brauer_lift_reduction": {
            "materialized": True,
            "required_BigK_rows_1based": order4["semantic_order4_generator"]["required_BigK_rows_1based"],
            "reuse_rows_1based": order4["next_numeric_leaf"]["reuse_already_materialized_BigK_rows_1based"],
            "missing_rows_1based": order4["next_numeric_leaf"]["materialize_additional_BigK_pullback_rows_1based"],
            "candidate_normalization": order4["candidate_full_surface_brauer_lift_normalization"],
            "certificate": "stages/stage33/33-12/j2-order4-brauer-lift-reduction.json",
            "canonical_sha256": LOCKS[ORDER4],
        },
    },
    "resolved_investigations": {
        "named_J2_semantic_orientation": {
            "status": "RESOLVED_DO_NOT_REINVESTIGATE_IN_ORDINARY_MAIN",
            "fact": {
                "semantic_discriminant_label": conclusion[
                    "named_CV_J2_semantic_discriminant_label"
                ],
                "fixed_marked_Kc_coordinate_f2": conclusion[
                    "named_CV_J2_fixed_marked_Kc_coordinate_f2"
                ],
                "candidate_count_before": conclusion["semantic_candidate_count_before"],
                "candidate_count_after": conclusion["semantic_candidate_count_after"],
            },
            "source_certificate": "stages/stage33/33-12/j2-cv-d2-semantic-orientation.json",
            "source_canonical_sha256": LOCKS[ORIENTATION],
        },
        "Br2_vs_discriminant_coordinate_shortcut": {
            "status": "PROHIBITED_SHORTCUT_DO_NOT_RETRY",
            "fact": (
                "Do not identify semantic discriminant u1 with current proper-Br2 "
                "e0 without an explicit full-surface adapter."
            ),
            "source_certificate": "stages/stage33/33-12/j2-cv-d2-semantic-orientation.json",
            "source_canonical_sha256": LOCKS[ORIENTATION],
        },
        "semantic_u1_full_surface_normalization_trace": {
            "status": "RESOLVED_NUMERIC_AT2_DO_NOT_REOPEN",
            "fact": (
                "Pinned rows [2,4,9,10,47,49] and literal retained Magma Smith V "
                "give full-surface A_T[2]=[0,0,0,0,0,0,0,1,0,1,0,1,1,0]."
            ),
            "source_certificate": (
                "stages/stage33/33-12/"
                "j2-semantic-u1-full-surface-smith-source.json"
            ),
            "source_canonical_sha256": LOCKS[U1_SMITH_SOURCE],
        },
        "order4_lift_reduction": {
            "status": "RESOLVED_EXACT_NEXT_NUMERIC_LEAF_FOUR_ROWS_ONLY",
            "fact": "Transporting t1/4 instead of only doubled u1=t1/2 exposes exactly four additional required BigK rows [20,35,39,67]; no repo-wide search is required.",
            "source_certificate": "stages/stage33/33-12/j2-order4-brauer-lift-reduction.json",
            "source_canonical_sha256": LOCKS[ORDER4],
        },
        "A_T_2_coefficients_to_proper_dual_shortcut": {
            "status": "REJECTED_EXACT_DO_NOT_RETRY",
            "fact": (
                "Copying the A_T[2] coefficients to the ordered proper-Br2 dual basis "
                "fails cc invariance with defect [1,0,1,1,0,0,0,0,0,0,0,0,0,0]."
            ),
            "source_certificate": "stages/stage33/33-12/j2-semantic-u1-at2-to-proper-br2-dual-adapter-blocker.json",
            "source_canonical_sha256": LOCKS[U1_DUAL_BLOCKER],
        },
    },
    "anti_loop_reopen_policy": {
        "ordinary_main_rule": (
            "Do not reinvestigate resolved_investigations while all listed source "
            "locks still match."
        ),
        "reopen_only_if": [
            "a listed source canonical_sha256 changes",
            "an authoritative current certificate contradicts the recorded fact",
            "the user explicitly requests hostile audit or historical revalidation",
        ],
    },
    "open_datum": {
        "corrected_J2_current_proper_Br2_14D_coordinate_materialized": False,
        "corrected_J2_retained_10D_coordinate_materialized": False,
        "semantic_u1_full_surface_smith_normalization_formula_materialized": True,
        "semantic_u1_full_surface_A_T_2_coordinate_materialized": True,
        "semantic_u1_full_surface_A_T_2_coordinate_f2": normalization["full_surface_A_T_2_coordinates_f2"],
        "required_BigK_pullback_rows_missing_1based": [20, 35, 39, 67],
        "retained_full_surface_Magma_Smith_right_transform_V_retained": True,
        "active_missing_interface": current["active_missing_interface"],
        "deterministic_after_proper14_coordinate": True,
        "matrix_columns_materialized": stage["finite_v4_kummer_columns_materialized"],
        "first_exact_75D_column_materialized": stage["first_exact_kummer_column_materialized"],
    },
    "current_leaf_working_set": [
        "stages/stage33/33-12/j2-order4-brauer-lift-reduction.json",
        "stages/stage33/33-12/certify_j2_order4_brauer_lift_reduction.py",
        "stages/stage33/33-12/verify_j2_order4_brauer_lift_reduction.py",
        "stages/stage33/33-12/j2-semantic-u1-full-surface-smith-source.json",
        "stages/stage33/33-07/proper-brauer2-from-discriminant.json",
        "stages/stage33/33-12/full-surface-pic2-kummer-target.json",
    ],
    "targeted_expansion_hints": {
        "orientation_proof_only_if_needed": "stages/stage33/33-12/j2-cv-d2-semantic-orientation.json",
        "proper14_coordinate_convention_only_if_needed": "stages/stage33/33-07/proper-brauer2-from-discriminant.json",
        "retained10_basis_replay_only_if_needed": "stages/stage33/33-12/full-surface-pic2-kummer-target.json",
        "semantic_u1_smith_source": "stages/stage33/33-12/j2-semantic-u1-full-surface-smith-source.json",
        "proper_dual_adapter_blocker": "stages/stage33/33-12/j2-semantic-u1-at2-to-proper-br2-dual-adapter-blocker.json",
        "order4_lift_reduction": "stages/stage33/33-12/j2-order4-brauer-lift-reduction.json",
        "human_checkpoint_only_if_needed": "stages/stage33/33-12/result.md"
    },
    "default_startup_exclusions": [
        "stages/stage33/controller-post-r5-hs-d2-override.json",
        "stages/stage33/33-05/j2-post-r5-hs-d2-state.json",
        "stages/stage33/33-05/j2-representative-repair-state.json",
        "stages/stage33/HISTORY.md",
        "stages/stage33/ROADMAP.md",
        "stages/stage33/ROADMAP-33-07-REPAIR-BAND.md",
    ],
    "firewalls": {
        "merge_allowed": controller["merge_allowed"],
        "stage33_12_closed_exact": controller["release_gates"]["stage33_12_closed_exact"],
        "stage33_07_reclosed": controller["release_gates"]["stage33_07_reclosed"],
        "stage33_08_released": controller["release_gates"]["stage33_08_released"],
        "theorem_credit": controller["theorem_credit"],
        "receiver_credit": controller["receiver_credit"],
        "endpoint_credit": controller["endpoint_credit"],
        "perfect_cuboid_existence_claim": controller["perfect_cuboid_existence_claim"],
        "perfect_cuboid_nonexistence_claim": controller["perfect_cuboid_nonexistence_claim"],
    },
}
out["canonical_sha256"] = csha(out)

parser = argparse.ArgumentParser()
parser.add_argument("--check", action="store_true")
args = parser.parse_args()
rendered = json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n"
if args.check:
    assert OUT.read_text(encoding="utf-8") == rendered
    print(json.dumps({"success": True, "canonical_sha256": out["canonical_sha256"]}, sort_keys=True))
else:
    OUT.write_text(rendered, encoding="utf-8")
    print(json.dumps({"success": True, "canonical_sha256": out["canonical_sha256"]}, sort_keys=True))
