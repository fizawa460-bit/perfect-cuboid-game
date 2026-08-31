#!/usr/bin/env python3
"""Certify the exact semantic-u1 normalization and its retained data gap.

This is deliberately a blocker certificate, not a guessed Kummer column.  It
derives the integral half-lattice numerator support from the locked semantic
PicK basis and records the exact full-surface Smith normalization.  The
current branch has only two of the six required BigK pullback rows, while the
historical full map and retained Smith right transform are not retained.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
S33 = HERE.parent
SEMANTIC_BASIS = HERE / "j2-semantic-kc-picard-basis.json"
SEMANTIC_TARGET = HERE / "j2-semantic-kc-discriminant-2torsion-target.json"
ORIENTATION = HERE / "j2-cv-d2-semantic-orientation.json"
SIX_PULLBACKS = HERE / "j2-ct-six-kc-support-fullpic64-pullbacks.json"
RECOVERY_AUDIT = HERE / "first-exact-kummer-column-j2-recovery-audit.json"
MARKED_BASIS = S33 / "33-09" / "marked-picard-basis-source.json"
RETAINED_PICARD = S33 / "33-07" / "retained-picard-base-sparse.json"
DISCRIMINANT = S33 / "33-07" / "picard-discriminant-compact.json"
PROPER14 = S33 / "33-07" / "proper-brauer2-from-discriminant.json"
KCMAPS = S33 / "33-07" / "kc-picard-maps.json"
RETAINED_SMITH = S33 / "33-07" / "retained-common-smith-transport-actual-swaps.json"
OUT = HERE / "j2-semantic-u1-full-surface-smith-normalization-blocker.json"

LOCKS = {
    SEMANTIC_BASIS: "c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0",
    SEMANTIC_TARGET: "0b5d7dfdefbb0f2b7c37396ada35c0bee462dfeb625eb18262be0e862205d8df",
    ORIENTATION: "0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e",
    SIX_PULLBACKS: "592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d",
    RECOVERY_AUDIT: "1174b98316f6e78e886540192cf9af378b9dac8e91a8359f2fb2e174ca3fc3b5",
    MARKED_BASIS: "0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f",
    RETAINED_PICARD: "e41df3f84760b941440035a388baac88602126c80140139ddf9c187bedf0bb49",
    DISCRIMINANT: "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0",
    PROPER14: "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
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


def build():
    semantic_basis = locked(SEMANTIC_BASIS)
    semantic_target = locked(SEMANTIC_TARGET)
    orientation = locked(ORIENTATION)
    six_pullbacks = locked(SIX_PULLBACKS)
    recovery = locked(RECOVERY_AUDIT)
    locked(MARKED_BASIS)
    locked(RETAINED_PICARD)
    discriminant = locked(DISCRIMINANT)
    proper14 = locked(PROPER14)

    conclusion = orientation["exact_conclusion"]
    assert conclusion["named_CV_J2_semantic_discriminant_label"] == "u1"
    assert conclusion["named_CV_J2_fixed_marked_Kc_coordinate_f2"] == [1, 0]

    u1 = next(
        row for row in semantic_target["semantic_half_lattice_basis"]
        if row["label"] == "u1"
    )
    numerator = u1["numerator_mod2"]
    assert len(numerator) == 20
    support_positions = [i + 1 for i, value in enumerate(numerator) if value]
    assert support_positions == [1, 2, 5, 6, 14, 15]

    curve_slots = semantic_basis["curve_slots_1based"]
    assert max(support_positions) <= len(curve_slots)
    required_bigk = [curve_slots[i - 1] for i in support_positions]
    assert required_bigk == [2, 4, 9, 10, 47, 49]

    available_bigk = six_pullbacks["target_BigK_support_1based"]
    available_required = sorted(set(required_bigk) & set(available_bigk))
    missing_required = sorted(set(required_bigk) - set(available_bigk))
    assert available_required == [47, 49]
    assert missing_required == [2, 4, 9, 10]
    assert recovery["current_missing_bridges"][
        "Kc20_to_full_surface_Pic64_numeric_matrix_retained_in_current_branch"
    ] is False
    assert recovery["current_missing_bridges"][
        "historical_pullback_map_artifact_currently_retrievable"
    ] is False
    assert not KCMAPS.exists()
    assert not RETAINED_SMITH.exists()

    mods = discriminant["discriminant_moduli"]
    assert mods == [2] * 4 + [4] * 6 + [8] * 4
    assert proper14["proper_geometric_Br2_dimension_f2"] == 14

    out = {
        "schema": "STAGE33_12_J2_SEMANTIC_U1_FULL_SURFACE_SMITH_NORMALIZATION_BLOCKER_V1",
        "stage": "33-12",
        "status": "BLOCKED_EXACT_MISSING_RETAINED_NUMERIC_INTERFACE",
        "source_locks": {
            "semantic_picard_basis_canonical_sha256": LOCKS[SEMANTIC_BASIS],
            "semantic_discriminant_target_canonical_sha256": LOCKS[SEMANTIC_TARGET],
            "semantic_orientation_canonical_sha256": LOCKS[ORIENTATION],
            "six_ct_pullbacks_canonical_sha256": LOCKS[SIX_PULLBACKS],
            "recovery_audit_canonical_sha256": LOCKS[RECOVERY_AUDIT],
            "marked_picard_basis_canonical_sha256": LOCKS[MARKED_BASIS],
            "retained_picard_base_canonical_sha256": LOCKS[RETAINED_PICARD],
            "full_surface_discriminant_canonical_sha256": LOCKS[DISCRIMINANT],
            "proper_brauer2_canonical_sha256": LOCKS[PROPER14],
            "stoll_repository": "MichaelStollBayreuth/Verification",
            "stoll_commit": semantic_basis["upstream_source_lock"]["commit"],
            "stoll_path": semantic_basis["upstream_source_lock"]["path"],
            "stoll_git_blob_sha1": six_pullbacks["source_locks"]["stoll_git_blob_sha1"],
            "historical_successful_pullback_maps_run_id": recovery["source_locks"][
                "historical_successful_pullback_maps_run_id"
            ],
            "expected_unretained_Kc_maps_path": str(KCMAPS.relative_to(S33.parent.parent)),
            "expected_unretained_full_surface_Smith_path": str(
                RETAINED_SMITH.relative_to(S33.parent.parent)
            ),
        },
        "exact_resolved_normalization": {
            "semantic_label": "u1",
            "semantic_coordinate_f2": [1, 0],
            "semantic_half_lattice_numerator_mod2": numerator,
            "semantic_basis_support_positions_1based": support_positions,
            "semantic_support_BigK_indices_1based": required_bigk,
            "full_surface_integral_numerator": (
                "n_S=sum(MatKtoS[row_i]) for BigK rows i in [2,4,9,10,47,49]"
            ),
            "integral_dual_quotient_representative": "z=(n_S*pmPic)/2",
            "magma_smith_convention": "D,U,V=SmithForm(pmPic); y=z*V",
            "full_surface_discriminant_moduli": mods,
            "A_T_2_coordinate_rule": (
                "for each of the 14 nontrivial Smith factors m_i, require "
                "y_i mod m_i in {0,m_i/2}; bit_i=(y_i/(m_i/2)) mod 2"
            ),
            "proper_Br2_dual_convention": (
                "the ordered proper-Br2 14D basis is the F2 dual of these same "
                "ordered A_T[2] coordinates"
            ),
            "arbitrary_factor_two_choice_remaining": False,
            "arbitrary_14D_adapter_remaining": False,
        },
        "exact_missing_numeric_data": {
            "required_BigK_pullback_rows_1based": required_bigk,
            "required_rows_already_retained_1based": available_required,
            "required_rows_missing_1based": missing_required,
            "historical_full_Kc20_to_fullPic64_map_retained": False,
            "historical_full_map_artifact_retrievable": False,
            "retained_full_surface_Magma_Smith_right_transform_V_retained": False,
            "full_surface_A_T_2_14D_coordinate_materialized": False,
            "proper_Br2_14D_coordinate_materialized": False,
            "retained_10D_coordinate_materialized": False,
            "first_75D_matrix_column_materialized": False,
        },
        "resolved_investigations": {
            "named_semantic_orientation": "RESOLVED_DO_NOT_REOPEN",
            "old_103D_adapter_ambiguity": "SUPERSEDED_DO_NOT_REOPEN",
            "normalization_problem": (
                "RESOLVED_TO_EXACT_FORMULA; ONLY_PINNED_NUMERIC_ROWS_AND_SMITH_V_MISSING"
            ),
        },
        "next_exact_leaf": (
            "MATERIALIZE_PINNED_BIGK_ROWS_2_4_9_10_AND_RETAINED_MAGMA_SMITH_V; "
            "APPLY_Z_EQUALS_N_S_TIMES_PM_PIC_OVER_2_THEN_Y_EQUALS_Z_TIMES_V; "
            "SOLVE_RETAINED10_AND_PLACE_LOCKED_WEIGHT15_TARGET"
        ),
        "promotion_firewall": {
            "semantic_u1_assumed_equal_to_proper_Br2_e0": False,
            "dimension_only_column_guess_used": False,
            "fake_zero_column_created": False,
            "revoked_historical_J2_zero_column_reused": False,
            "finite_v4_kummer_columns_materialized": 0,
            "stage33_12_closed_exact": False,
            "stage33_13_released": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    out["canonical_sha256"] = csha(out)
    return out


if __name__ == "__main__":
    out = build()
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "certificate_sha256": out["canonical_sha256"],
        "required_BigK_rows": out["exact_missing_numeric_data"][
            "required_BigK_pullback_rows_1based"
        ],
        "missing_BigK_rows": out["exact_missing_numeric_data"][
            "required_rows_missing_1based"
        ],
        "matrix_columns_materialized": 0,
    }, sort_keys=True))
