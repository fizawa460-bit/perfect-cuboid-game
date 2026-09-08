#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
D2 = HERE / "e3-v91c1x-r5b2d2-swap23-317-cover-common-refinement.json"
R5B3A = HERE / "e3-v91c1x-r5b3a-a2-02-317-1757-literal-package-pullbacks.json"
C4B1A = HERE / "e3-v91c1x-r5b3b3c4b1a-exceptional-nonsquare-obstruction-census-and-correction-preflight.json"
C4B1B = HERE / "e3-v91c1x-r5b3b3c4b1b-uniformizer-scalar-gauge-obstruction-reduction.json"
C4B1C = HERE / "e3-v91c1x-r5b3b3c4b1c-nonconstant-exceptional-swap23-correction-preflight.json"
E5D = HERE / "e3-v91c1x-r5b3b3c4b1e5d-pole-ideal-constant-gm-action-units.json"
E5E = HERE / "e3-v91c1x-r5b3b3c4b1e5e-pole-factor-cartier-legitimacy.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e5f-whole-cover-action-transport-debt-partition.json"

D2_SHA = "3165eab3d08ed29dcba429ed9f397d49054739459b08507e6a63d1cba2d66cbb"
R5B3A_SHA = "b694cd2aee502e13186cbe68e65ddce7a845e54e546c8cf548c1386ac5a71d31"
C4B1A_SHA = "2bdd01db7b77de5e1587bb0a1c367da5039610b1266c8d5e77b10a63742e3a6f"
C4B1B_SHA = "d2cc6934d96c2fc4f227e606692a47bed3e2687539303b939b755d05ea0b6ef9"
C4B1C_SHA = "07c1865506e93d3fa71d6bb8b8435b4e944f2558ec8e042770b8659cba1736d8"
E5D_SHA = "bd5ebd3bd923433597c7f0f9dc2a07d222df10f9aa118273beca74ad4ff28fd0"
E5E_SHA = "2a790f1103554c05d450140c6cd12104dec1dded9d259f6ac364c5f9a819cb5e"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(
            f"canonical source lock moved {path.name}: "
            f"claimed={claimed} actual={actual} expected={expected}"
        )
    return obj


def build_certificate() -> dict:
    d2 = load_locked(D2, D2_SHA)
    r5b3a = load_locked(R5B3A, R5B3A_SHA)
    c4b1a = load_locked(C4B1A, C4B1A_SHA)
    c4b1b = load_locked(C4B1B, C4B1B_SHA)
    c4b1c = load_locked(C4B1C, C4B1C_SHA)
    e5d = load_locked(E5D, E5D_SHA)
    e5e = load_locked(E5E, E5E_SHA)

    idx = d2["common_refinement_index"]
    if idx["total_piece_count"] != 1757 or not idx["covers_whole_resolved_surface"]:
        raise SystemExit("R5B2D2 whole-cover refinement boundary moved")
    if d2["smooth_cover_action"]["smooth_common_refinement_piece_count"] != 29:
        raise SystemExit("R5B2D2 smooth piece count moved")
    if d2["exceptional_common_refinement"]["piece_count_per_node"] != 36:
        raise SystemExit("R5B2D2 exceptional piece multiplicity moved")
    if d2["construction_status"]["same_representative_transport_materialized"]:
        raise SystemExit("R5B2D2 unexpectedly gained same-representative transport")

    packages = r5b3a["a2_02_source"]["package_rows"]
    if len(packages) != 8:
        raise SystemExit("R5B3A eight-package count moved")
    for row in packages:
        pull = row["common_refinement_pullback"]
        if pull["piece_count"] != 1757 or not pull["assignment_is_source_projection_of_317_cover_pullback"]:
            raise SystemExit("R5B3A 1757 package pullback assignment moved")

    census = c4b1a["exceptional_obstruction_census"]
    if census["current_candidate_ramified_exceptional_count"] != 31:
        raise SystemExit("C4B1A ramified exceptional count moved")
    if census["current_candidate_square_or_trivial_exceptional_count"] != 17:
        raise SystemExit("C4B1A square/trivial exceptional count moved")

    partition = c4b1b["obstruction_partition"]
    constant_ids = list(partition["constant_only_exceptional_ids"])
    nonconstant_ids = list(partition["nonconstant_function_field_factor_exceptional_ids"])
    if len(constant_ids) != 27 or partition["constant_only_nonsquare_count"] != 27:
        raise SystemExit("C4B1B constant-only partition moved")
    if len(nonconstant_ids) != 4 or partition["nonconstant_function_field_factor_nonsquare_count"] != 4:
        raise SystemExit("C4B1B nonconstant partition moved")
    if c4b1b["constant_scalar_squareclass_system"]["consistent_in_Qi_squareclass_group"]:
        raise SystemExit("C4B1B constant gauge unexpectedly became consistent")
    if c4b1b["exact_consequence"]["uniformizer_constant_gauge_can_kill_all_27_constant_only_exceptional_obstructions"]:
        raise SystemExit("C4B1B unexpectedly kills all 27 constant obstructions")

    c_targets = c4b1c["nonconstant_exceptional_targets"]
    if sorted(c_targets["exceptional_ids"]) != sorted(nonconstant_ids):
        raise SystemExit("C4B1B/C nonconstant target set mismatch")
    if not c4b1c["swap23_orbit_reduction"]["nonconstant_target_set_is_swap23_stable"]:
        raise SystemExit("C4B1C nonconstant target set ceased to be swap23-stable")

    if e5d["pole_principal_equation_action"]["attached_d2_piece_count"] != 144:
        raise SystemExit("E5D attached piece count moved")
    if not e5e["exact_consequence"]["e5d_constant_gm_coefficients_are_genuine_exceptional_block_pole_line_action_units"]:
        raise SystemExit("E5E genuine action-unit certification moved")
    if not e5e["exact_consequence"]["cartier_legitimacy_persists_on_all_144_attached_d2_exceptional_refinement_pieces_by_localization"]:
        raise SystemExit("E5E 144-piece Cartier localization moved")

    all_ids = {f"EXC_{i:03d}" for i in range(1, 49)}
    nonsquare_ids = set(constant_ids) | set(nonconstant_ids)
    if len(nonsquare_ids) != 31:
        raise SystemExit("31-node nonsquare union moved")
    square_or_trivial_ids = sorted(all_ids - nonsquare_ids)
    if len(square_or_trivial_ids) != 17:
        raise SystemExit("17-node square/trivial complement moved")

    smooth_pieces = 29
    nonconstant_pieces = len(nonconstant_ids) * 36
    constant_only_pieces = len(constant_ids) * 36
    square_or_trivial_pieces = len(square_or_trivial_ids) * 36
    if smooth_pieces + nonconstant_pieces + constant_only_pieces + square_or_trivial_pieces != 1757:
        raise SystemExit("1757 debt partition does not close")

    certified_action_unit_pieces = nonconstant_pieces
    unresolved_same_representative_transport_pieces = 1757 - certified_action_unit_pieces
    if certified_action_unit_pieces != 144 or unresolved_same_representative_transport_pieces != 1613:
        raise SystemExit("E5F action-unit coverage count moved")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e5f.whole_cover_action_transport_debt_partition.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E5F_WHOLE_1757_ACTION_TRANSPORT_DEBT_PARTITION",
        "role": "EXACT_NONCREDIT_PARTITION_OF_THE_1757_SWAP23_COMMON_REFINEMENT_BY_WHAT_SAME_REPRESENTATIVE_ACTION_DATA_IS_AND_IS_NOT_CURRENTLY_CERTIFIED",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "successor_pr": 1722,
            "merged_parent_pr": 1695,
        },
        "source_locks": {
            "r5b2d2_sha256": D2_SHA,
            "r5b3a_sha256": R5B3A_SHA,
            "c4b1a_sha256": C4B1A_SHA,
            "c4b1b_sha256": C4B1B_SHA,
            "c4b1c_sha256": C4B1C_SHA,
            "c4b1e5d_sha256": E5D_SHA,
            "c4b1e5e_sha256": E5E_SHA,
        },
        "whole_cover_partition": {
            "total_common_refinement_piece_count": 1757,
            "smooth_domain_action_only": {
                "piece_count": smooth_pieces,
                "swap23_domain_action_materialized": True,
                "eight_literal_package_pullbacks_available_on_each_piece": True,
                "same_representative_line_action_unit_materialized": False,
            },
            "exceptional_square_or_trivial_residue_blocks": {
                "exceptional_ids": square_or_trivial_ids,
                "node_count": len(square_or_trivial_ids),
                "piece_count": square_or_trivial_pieces,
                "current_formal_symbol_residue_square_or_trivial": True,
                "same_representative_line_action_unit_materialized": False,
                "firewall": "square/trivial current residue does not by itself materialize the same-representative line action transition",
            },
            "exceptional_constant_only_nonsquare_blocks": {
                "exceptional_ids": constant_ids,
                "node_count": len(constant_ids),
                "piece_count": constant_only_pieces,
                "constant_uniformizer_gauge_system_consistent": False,
                "all_27_killed_by_constant_gauge": False,
                "same_representative_line_action_unit_materialized": False,
            },
            "exceptional_nonconstant_blocks_with_genuine_e5d_e5e_action_units": {
                "exceptional_ids": nonconstant_ids,
                "node_count": len(nonconstant_ids),
                "piece_count": nonconstant_pieces,
                "genuine_regular_invertible_pole_line_action_units_materialized": True,
                "cartier_legitimacy_verified": True,
            },
        },
        "coverage_accounting": {
            "genuine_exceptional_block_action_unit_piece_count": certified_action_unit_pieces,
            "same_representative_action_transport_still_unmaterialized_piece_count": unresolved_same_representative_transport_pieces,
            "coverage_fraction_numerator": certified_action_unit_pieces,
            "coverage_fraction_denominator": 1757,
            "partition_closes_exactly": True,
        },
        "exact_consequence": {
            "e5d_e5e_do_not_reduce_the_remaining_debt_to_only_smooth_charts": True,
            "remaining_debt_contains_29_smooth_pieces_plus_44_exceptional_blocks": True,
            "the_44_exceptional_blocks_split_as_27_constant_only_nonsquare_plus_17_square_or_trivial_residue_blocks": True,
            "constant_only_27_block_debt_cannot_be_declared_solved_by_Qi_constant_uniformizer_gauge": True,
            "square_or_trivial_residue_is_not_promoted_to_line_action_glue": True,
            "whole_1757_cover_line_bundle_gm_1_cocycle_materialized": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
            "h2_fixedness_verified": False,
        },
        "next_exact_step": "materialize or refute the same-representative action transport on the bounded 29 smooth common-refinement pieces using the source-bound R5B2D2 smooth action and R5B3A literal package pullbacks; keep the 44 unresolved exceptional blocks as a separate explicit debt rather than assigning unit 1 by residue class",
        "next_exact_leaf": "V91C1X_R5B3B3C4B1E5G_SMOOTH_29_SAME_REPRESENTATIVE_ACTION_TRANSPORT_PREFLIGHT",
        "parallel_outstanding_leaf": "V91C1X_R5B3B3C4B2_STRICT_PRIME_CROSS_CARRIER_INCIDENCE_AND_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
        "credit_firewall": {
            "authority_promotion": False,
            "hostile_audit_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "exceptional_cancellation_credit": False,
            "unramifiedness_credit": False,
            "source_bound_dim5_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        print(json.dumps({
            "success": True,
            "marker": cert["candidate"],
            "certified_action_unit_pieces": cert["coverage_accounting"]["genuine_exceptional_block_action_unit_piece_count"],
            "unresolved_same_representative_transport_pieces": cert["coverage_accounting"]["same_representative_action_transport_still_unmaterialized_piece_count"],
            "certificate_sha256": cert["canonical_sha256"],
            "next_exact_leaf": cert["next_exact_leaf"],
        }, sort_keys=True))
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    current = json.loads(OUT.read_text(encoding="utf-8"))
    if current != cert:
        raise SystemExit("materialized C4B1E5F certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
