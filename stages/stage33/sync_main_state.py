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
U1_SMITH_BLOCKER = (
    HERE / "33-12" / "j2-semantic-u1-full-surface-smith-normalization-blocker.json"
)
OUT = HERE / "MAIN-STATE.json"

LOCKS = {
    ORIENTATION: "0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e",
    PROPER14: "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
    TARGET_BASIS: "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890",
    NAMED_TARGET: "4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3",
    U1_SMITH_BLOCKER: "9a8c9bcc420a7ad60bb6d71326bc04000da676ec4bb222e0cc4266c2aadf3d7f",
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
u1_smith_blocker = locked(U1_SMITH_BLOCKER)

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
normalization = u1_smith_blocker["exact_resolved_normalization"]
missing_numeric = u1_smith_blocker["exact_missing_numeric_data"]
assert normalization["semantic_label"] == "u1"
assert normalization["semantic_coordinate_f2"] == [1, 0]
assert normalization["semantic_support_BigK_indices_1based"] == [2, 4, 9, 10, 47, 49]
assert normalization["arbitrary_factor_two_choice_remaining"] is False
assert normalization["arbitrary_14D_adapter_remaining"] is False
assert missing_numeric["required_rows_missing_1based"] == [2, 4, 9, 10]
assert missing_numeric["proper_Br2_14D_coordinate_materialized"] is False

coordinates = target["coordinates_f2"]
out = {
    "schema": "STAGE33_MAIN_COMPACT_STATE_V2",
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
            "semantic_support_BigK_indices_1based": normalization[
                "semantic_support_BigK_indices_1based"
            ],
            "required_rows_already_retained_1based": missing_numeric[
                "required_rows_already_retained_1based"
            ],
            "required_rows_missing_1based": missing_numeric[
                "required_rows_missing_1based"
            ],
            "integral_dual_quotient_representative": normalization[
                "integral_dual_quotient_representative"
            ],
            "magma_smith_convention": normalization["magma_smith_convention"],
            "certificate": (
                "stages/stage33/33-12/"
                "j2-semantic-u1-full-surface-smith-normalization-blocker.json"
            ),
            "canonical_sha256": LOCKS[U1_SMITH_BLOCKER],
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
            "status": "RESOLVED_FORMULA_ONLY_DO_NOT_REOPEN_AS_GENERIC_ADAPTER_AMBIGUITY",
            "fact": (
                "The exact route is n_S from pinned BigK rows [2,4,9,10,47,49], "
                "z=(n_S*pmPic)/2, then y=z*V in the retained Magma Smith convention. "
                "Only rows [2,4,9,10] and the retained numeric V are missing."
            ),
            "source_certificate": (
                "stages/stage33/33-12/"
                "j2-semantic-u1-full-surface-smith-normalization-blocker.json"
            ),
            "source_canonical_sha256": LOCKS[U1_SMITH_BLOCKER],
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
        "required_BigK_pullback_rows_missing_1based": missing_numeric[
            "required_rows_missing_1based"
        ],
        "retained_full_surface_Magma_Smith_right_transform_V_retained": False,
        "deterministic_after_proper14_coordinate": True,
        "matrix_columns_materialized": stage["finite_v4_kummer_columns_materialized"],
        "first_exact_75D_column_materialized": stage["first_exact_kummer_column_materialized"],
    },
    "current_leaf_working_set": [
        "stages/stage33/33-12/j2-semantic-u1-full-surface-smith-normalization-blocker.json",
        "stages/stage33/33-12/certify_j2_semantic_u1_full_surface_smith_normalization_blocker.py",
        "stages/stage33/33-12/verify_j2_semantic_u1_full_surface_smith_normalization_blocker.py",
        "stages/stage33/33-12/j2-semantic-kc-discriminant-2torsion-target.json",
        "stages/stage33/33-12/j2-semantic-kc-picard-basis.json",
        "stages/stage33/33-07/picard-discriminant-compact.json",
        "stages/stage33/33-09/marked-picard-basis-source.json",
    ],
    "targeted_expansion_hints": {
        "orientation_proof_only_if_needed": "stages/stage33/33-12/j2-cv-d2-semantic-orientation.json",
        "proper14_coordinate_convention_only_if_needed": "stages/stage33/33-07/proper-brauer2-from-discriminant.json",
        "retained10_basis_replay_only_if_needed": "stages/stage33/33-12/full-surface-pic2-kummer-target.json",
        "semantic_u1_normalization_blocker": "stages/stage33/33-12/j2-semantic-u1-full-surface-smith-normalization-blocker.json",
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
