#!/usr/bin/env python3
"""Reattach post-V27 scalar exceptional geometry without reviving the superseded
historical ct-overlap promotion.

This audit deliberately distinguishes:
  * exact scalar valuations / even-norm local parity constraints that remain reusable;
  * the unresolved current integral rank-two Cech lattices and overlap matrices.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
OUT = HERE / "j2-post-v27-exceptional-overlap-inheritance-audit-v28.json"

LOCKS = {
    "v25_current_named_j2": (
        HERE / "j2-genuine-h2-mu2-kummer-adapter-v25.json",
        "d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c",
    ),
    "v27_boundary_valuations": (
        HERE / "j2-ct-norm-splitting-boundary-valuations-v27.json",
        "355c2a6dcb27f163ba6236a4e6790f090d03dbd7e74c89d76c2cf7a5c2e1ccc4",
    ),
    "explicit_cech_mu2_lift": (
        HERE / "j2-corrected-explicit-cech-mu2-lift.json",
        "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b",
    ),
    "actual_boundary_sheet_frames": (
        HERE / "j2-ct-norm-actual-boundary-sheet-frames.json",
        "5b961822dc10e7a1a424ed87ba6307d83efd3a0b31671db305a609269094937b",
    ),
    "resolution_exceptional_sheet_frames": (
        HERE / "j2-ct-norm-resolution-exceptional-sheet-frames.json",
        "bbde421a54d2b7159f8d3ff4cf641cbddf2bbbc45fe4791cb7ed18d7cfb69591",
    ),
    "local_lattice_parity_constraints": (
        HERE / "j2-ct-norm-local-lattice-parity-constraints.json",
        "c941d34444b365fb03be188b9c72569c607b02da76efa1d5034994b2ed44f533",
    ),
    "historical_ct_overlap_candidate": (
        HERE / "j2-ct-actual-cech-overlap-parities-and-marked-pic-mod2.json",
        "68077141a4f792eefb47ebfd5db46ae9e785a0bef286449fc888663f2f2f5c3c",
    ),
    "pre_kummer_descent_cochain": (
        S33 / "33-05" / "j2-corrected-pre-kummer-descent-cochain.json",
        "940df53040c6f5245914effbfb7d752a08c61b6d593586952b322e4069415106",
    ),
}

EXPECTED = "919c1fd1dfb57f0e86677e64052636918082d7ef0cf9a9f79afe51051eb96095"


def csha(obj: dict) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), (path, claimed, csha(body))
    return obj


def build() -> dict:
    d = {name: locked(path, digest) for name, (path, digest) in LOCKS.items()}
    v25 = d["v25_current_named_j2"]
    v27 = d["v27_boundary_valuations"]
    explicit = d["explicit_cech_mu2_lift"]
    boundary = d["actual_boundary_sheet_frames"]
    exc = d["resolution_exceptional_sheet_frames"]
    parity = d["local_lattice_parity_constraints"]
    historical = d["historical_ct_overlap_candidate"]
    pre = d["pre_kummer_descent_cochain"]

    rem = v25["remaining_interface"]
    assert rem["actual_cech_local_rank2_lattices_materialized"] is False
    assert rem["actual_cc_ct_overlap_transition_matrices_materialized"] is False
    assert rem["standard_kummer_columns_materialized"] == 0

    vf = v27["certified_frontier"]
    assert vf["named_boundary_splitting_valuations_materialized"] == [
        "t=0", "t=infinity", "s=infinity", "C21", "C22"
    ]
    assert vf["resolution_exceptional_splitting_valuations_materialized"] is False
    assert boundary["canonical_sha256"] == LOCKS["actual_boundary_sheet_frames"][1]

    ib = exc["exact_information_boundary"]
    assert ib["actual_ct_resolution_exceptional_scalar_frames_materialized"] is True
    assert ib["all_12_Kc_resolution_exceptionals_accounted_for"] is True
    assert ib["actual_lambda_D_local_rank2_lattices_materialized"] is False
    assert ib["actual_cc_ct_overlap_transition_matrices_materialized"] is False
    assert exc["singular_partition"]["branch_crossing_nodes"] == 4
    assert exc["singular_partition"]["unbranched_lifts_of_quotient_A1_nodes"] == 8

    exf = exc["actual_ct_resolution_exceptional_sheet_frames"]
    actual_orders = {
        "E_00": {
            "plus": [exf["E_00"]["sheet_plus"]["ord_u"], exf["E_00"]["sheet_plus"]["ord_sigma_u"]],
            "minus": [exf["E_00"]["sheet_minus"]["ord_u"], exf["E_00"]["sheet_minus"]["ord_sigma_u"]],
            "norm": exf["E_00"]["ord_norm"],
        },
        "E_0inf": {
            "plus": [exf["E_0inf"]["sheet_plus"]["ord_u"], exf["E_0inf"]["sheet_plus"]["ord_sigma_u"]],
            "minus": [exf["E_0inf"]["sheet_minus"]["ord_u"], exf["E_0inf"]["sheet_minus"]["ord_sigma_u"]],
            "norm": exf["E_0inf"]["ord_norm"],
        },
        "E_inf0": {
            "plus": [exf["E_inf0"]["sheet_plus"]["ord_u"], exf["E_inf0"]["sheet_plus"]["ord_sigma_u"]],
            "minus": [exf["E_inf0"]["sheet_minus"]["ord_u"], exf["E_inf0"]["sheet_minus"]["ord_sigma_u"]],
            "norm": exf["E_inf0"]["ord_norm"],
        },
        "E_infinf": {
            "plus": [exf["E_infinf"]["sheet_plus"]["ord_u"], exf["E_infinf"]["sheet_plus"]["ord_sigma_u"]],
            "minus": [exf["E_infinf"]["sheet_minus"]["ord_u"], exf["E_infinf"]["sheet_minus"]["ord_sigma_u"]],
            "norm": exf["E_infinf"]["ord_norm"],
        },
    }

    pib = parity["exact_information_boundary"]
    assert pib["even_norm_local_determinant_parities_materialized"] is True
    assert pib["actual_lambda_D_full_local_rank2_lattices_materialized"] is False
    assert pib["actual_cc_ct_overlap_transition_matrices_materialized"] is False
    assert parity["fixed_partial_marked_pic_mod2"]["is_final_ct_defect"] is False

    hib = historical["exact_information_boundary"]
    assert hib["actual_ct_overlap_determinant_parities_materialized"] is True
    assert hib["actual_ct_defect_marked_Pic_mod2_materialized"] is True
    assert historical["split_dvr_overlap_matrix"]["basis_change"] == \
        "G=diag(u_minus,1), so G*Y_norm*G^-1=J"
    assert "actual_cc_ct_overlap_transition_matrices_materialized" not in hib

    pab = pre["audit_boundary"]
    assert "Do not identify normalization half-divisor descent with the Kc surface Kummer lift" \
        in pab["forbidden_promotion"]
    assert pab["full_surface_mu2_lift_materialized"] is False

    assert explicit["surface_mu2_lift"]["genuine_surface_H2_mu2_lift_materialized"] is True
    assert explicit["galois_defect_generic_splittings"]["pic_mod2_integral_coordinates_materialized"] is False

    out = {
        "schema": "STAGE33_12_J2_POST_V27_EXCEPTIONAL_AND_OVERLAP_INHERITANCE_AUDIT_V28",
        "stage": "33-12",
        "status": "PASS_EXACT_RESOLUTION_EXCEPTIONAL_SCALAR_FRONTIER_REATTACHED_OLD_CT_OVERLAP_PROMOTION_REJECTED",
        "source_locks": {name: digest for name, (_, digest) in LOCKS.items()},
        "reattached_exact_scalar_geometry": {
            "named_boundary_valuations_materialized": True,
            "resolution_exceptional_scalar_valuations_materialized": True,
            "branch_crossing_exceptional_count": 4,
            "unbranched_quotient_A1_lift_exceptional_count": 8,
            "all_12_Kc_resolution_exceptionals_accounted_for": True,
            "branch_crossing_orders": actual_orders,
            "eight_unbranched_quotient_A1_exceptionals_generic_orders": {
                "u": exc["quotient_A1_exceptional_frames"]["generic_ord_u_on_every_auxiliary_q_cover_component"],
                "sigma_u": exc["quotient_A1_exceptional_frames"]["generic_ord_sigma_u_on_every_auxiliary_q_cover_component"],
                "norm": exc["quotient_A1_exceptional_frames"]["generic_ord_norm"],
            },
        },
        "retainable_local_parity_constraints": {
            "even_norm_local_determinant_parities_materialized": True,
            "forced_parities": parity["forced_local_determinant_parities"],
            "fixed_partial_marked_Pic_mod2": parity["fixed_partial_marked_pic_mod2"]["coordinates"],
            "fixed_partial_is_final_ct_defect": False,
            "odd_boundary_and_qroot_overlap_data_still_require_actual_current_lattices": True,
        },
        "historical_overlap_promotion_audit": {
            "historical_artifact_claimed_ct_overlap_determinant_parities": True,
            "historical_artifact_claimed_ct_marked_Pic_mod2_nonzero": True,
            "historical_candidate_coordinates": historical["actual_ct_defect_marked_pic_mod2"]["coordinates"],
            "historical_candidate_inherited_as_current_authority": False,
            "reason_1": "The historical certificate materializes determinant-parity formulas and a symbolic generic basis change G=diag(u_minus,1), but not the required resolved-chart integral rank-two lattice bases and complete overlap transition matrices.",
            "reason_2": "Its T0/Tinf sheet selection consumes the pre-Kummer descent cochain, whose own audit boundary explicitly forbids promotion from normalization half-divisor descent to the Kc surface Kummer lift without an explicit CV/surface Picard adapter.",
            "reason_3": "V25 is later current authority and explicitly keeps actual Cech local rank-two lattices and actual cc/ct overlap transition matrices false.",
            "historical_ct_defect_may_be_used_as_proof_of_current_ct_defect": False,
        },
        "current_exact_information_boundary": {
            "actual_cech_local_rank2_lattices_materialized": False,
            "actual_cc_ct_overlap_transition_matrices_materialized": False,
            "actual_ct_defect_marked_Pic_mod2_materialized": False,
            "pic_mod2_defect_1cocycle_materialized": False,
            "v4_connecting_cocycle_materialized": False,
            "hs_d2_2cocycle_materialized": False,
            "standard_kummer_columns_materialized": 0,
        },
        "next_exact_leaf": "MATERIALIZE_CURRENT_LAMBDA_D_INTEGRAL_RANK2_BASES_ON_T0_TINF_SINF_C21_C22_AND_ALL_12_RESOLUTION_EXCEPTIONAL_CHARTS_WITH_EXPLICIT_OVERLAP_2X2_MATRICES_THEN_REPLAY_T0_TINF_QROOT_DETERMINANT_PARITIES_AND_COMPUTE_CURRENT_MARKED_PIC_MOD2_DEFECT",
        "acceptance_contract_for_next_leaf": {
            "must_bind_to_current_lambda_D_from_v25": True,
            "must_list_integral_rank2_basis_on_each_required_chart": True,
            "must_list_explicit_2x2_transition_matrix_on_each_load_bearing_overlap": True,
            "must_verify_matrix_entries_are_regular_in_the_declared_overlap_ring": True,
            "must_verify_determinants_reproduce_v27_and_v28_scalar_valuation_constraints": True,
            "must_not_use_pre_kummer_sheet_selection_as_surface_authority_without_current_adapter": True,
            "must_not_promote_symbolic_generic_basis_change_alone": True,
        },
        "promotion_firewall": {
            "stage33_progress": "6/11",
            "stage33_12_closed_exact": False,
            "stage33_07_reclosed": False,
            "stage33_08_released": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_allowed": False,
        },
    }
    assert csha(out) == EXPECTED
    return out


def main() -> None:
    out = build()
    if "--check" in sys.argv:
        assert locked(OUT, EXPECTED) == {**out, "canonical_sha256": EXPECTED}
    else:
        payload = dict(out)
        payload["canonical_sha256"] = EXPECTED
        OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "success": True,
        "canonical_sha256": EXPECTED,
        "resolution_exceptional_scalar_valuations_materialized": True,
        "historical_ct_overlap_promoted": False,
        "actual_cech_local_rank2_lattices_materialized": False,
        "standard_kummer_columns_materialized": 0,
        "marker": "PROOF_REPLAY_COMPLETE",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
