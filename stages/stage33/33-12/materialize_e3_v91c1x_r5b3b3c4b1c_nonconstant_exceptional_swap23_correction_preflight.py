#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
D2 = HERE / "e3-v91c1x-r5b2d2-swap23-317-cover-common-refinement.json"
B3A = HERE / "e3-v91c1x-r5b3a-a2-02-317-1757-literal-package-pullbacks.json"
B3B1 = HERE / "e3-v91c1x-r5b3b1-a2-02-317-1757-boundary-uniformizers.json"
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
R2 = HERE / "e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json"
V1D = HERE / "e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"
C4B1A = HERE / "e3-v91c1x-r5b3b3c4b1a-exceptional-nonsquare-obstruction-census-and-correction-preflight.json"
C4B1B = HERE / "e3-v91c1x-r5b3b3c4b1b-uniformizer-scalar-gauge-obstruction-reduction.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1c-nonconstant-exceptional-swap23-correction-preflight.json"

D2_SHA = "3165eab3d08ed29dcba429ed9f397d49054739459b08507e6a63d1cba2d66cbb"
B3A_SHA = "b694cd2aee502e13186cbe68e65ddce7a845e54e546c8cf548c1386ac5a71d31"
B3B1_SHA = "8a5dcb751b312a846a06fac88298166efe8c1fd91ed0988b3cb04a408cfc2654"
B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
R2_SHA = "912f00e0b680c39cdd0b99fb92174b5b45858dceeda4019799260869238766c1"
V1D_SHA = "fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14"
C4B1A_SHA = "2bdd01db7b77de5e1587bb0a1c367da5039610b1266c8d5e77b10a63742e3a6f"
C4B1B_SHA = "d2cc6934d96c2fc4f227e606692a47bed3e2687539303b939b755d05ea0b6ef9"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
NONCONSTANT = ["EXC_003", "EXC_004", "EXC_011", "EXC_012"]


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
            f"canonical source lock moved: {path.name}: "
            f"claimed={claimed} actual={actual} expected={expected}"
        )
    return obj


def build_certificate() -> dict:
    d2 = load_locked(D2, D2_SHA)
    b3a = load_locked(B3A, B3A_SHA)
    b3b1 = load_locked(B3B1, B3B1_SHA)
    b3b2 = load_locked(B3B2, B3B2_SHA)
    r2 = load_locked(R2, R2_SHA)
    v1d = load_locked(V1D, V1D_SHA)
    c4b1a = load_locked(C4B1A, C4B1A_SHA)
    c4b1b = load_locked(C4B1B, C4B1B_SHA)

    d2_status = d2["construction_status"]
    if not d2_status["cover_action_or_common_refinement_materialized"]:
        raise SystemExit("R5B2D2 common refinement moved")
    if not d2["common_refinement_index"]["equals_1757"]:
        raise SystemExit("R5B2D2 1757 refinement moved")
    if not d2["exact_consequence"]["swap23_action_on_all_48_exceptional_centers_materialized"]:
        raise SystemExit("R5B2D2 exceptional swap23 action moved")

    node_rows = d2["exceptional_common_refinement"]["node_rows"]
    swap = {row["source_node"]: row["acted_target_node"] for row in node_rows}
    if len(swap) != 48 or set(swap) != {f"EXC_{j:03d}" for j in range(1, 49)}:
        raise SystemExit("R5B2D2 exceptional node map is no longer total on 48 nodes")
    if any(swap.get(swap[eid]) != eid for eid in swap):
        raise SystemExit("R5B2D2 exceptional swap23 map ceased to be involutive")
    if set(swap[eid] for eid in NONCONSTANT) != set(NONCONSTANT):
        raise SystemExit("nonconstant obstruction support is not swap23-stable")

    seen = set()
    orbit_rows = []
    for eid in sorted(NONCONSTANT):
        if eid in seen:
            continue
        target = swap[eid]
        members = sorted({eid, target})
        if len(members) != 2:
            raise SystemExit(f"nonconstant obstruction unexpectedly swap23-fixed: {eid}")
        seen.update(members)
        orbit_rows.append({
            "orbit_members": members,
            "source_to_target": {member: swap[member] for member in members},
            "orbit_size": 2,
        })
    if [row["orbit_members"] for row in orbit_rows] != [
        ["EXC_003", "EXC_011"],
        ["EXC_004", "EXC_012"],
    ]:
        raise SystemExit(f"nonconstant swap23 orbit partition moved: {orbit_rows}")

    obstruction_by_id = {
        row["exceptional_id"]: row
        for row in c4b1a["exceptional_obstruction_census"]["nonsquare_obstruction_rows"]
    }
    target_rows = []
    raw_factor_hashes = set()
    for eid in NONCONSTANT:
        row = obstruction_by_id[eid]
        factors = list(row["combined_residue_squareclass"]["odd_irreducible_factors"])
        if not factors:
            raise SystemExit(f"nonconstant target lost odd irreducible factors: {eid}")
        for factor in factors:
            raw_factor_hashes.add(factor["projective_factor_sha256"])
        target_rows.append({
            "exceptional_id": eid,
            "swap23_target_exceptional_id": swap[eid],
            "deterministic_p1_parametrization_sha256": row["deterministic_p1_parametrization_sha256"],
            "frozen_tangent_model_sha256": row["frozen_tangent_model_sha256"],
            "combined_residue_representative_Qi_t_sha256": row["combined_residue_representative_Qi_t_sha256"],
            "odd_irreducible_factors": factors,
            "coefficient_is_square_in_Qi": row["combined_residue_squareclass"]["coefficient_is_square_in_Qi"],
            "odd_carrier_exceptional_order_one_ids": row["odd_carrier_exceptional_order_one_ids"],
        })

    if c4b1b["obstruction_partition"]["nonconstant_function_field_factor_exceptional_ids"] != NONCONSTANT:
        raise SystemExit("C4B1B nonconstant support moved")
    if c4b1b["constant_scalar_squareclass_system"]["consistent_in_Qi_squareclass_group"] is not False:
        raise SystemExit("C4B1B constant scalar system unexpectedly became consistent")

    if v1d["purity_cartier"]["cartier_correction"] != "ZERO":
        raise SystemExit("V91C1D historical Cartier correction moved")
    if v1d["purity_cartier"]["cartier_transition_unit"] != "ONE":
        raise SystemExit("V91C1D historical Cartier transition unit moved")

    r2_status = r2["current_materialization_status"]
    if any([
        r2_status["accepted_source_representative_materialized"],
        r2_status["line_bundle_gm_1_cocycle_ell_ij_materialized"],
        r2_status["square_root_1_cochain_r_ij_materialized"],
        r2_status["triple_overlap_identity_verified"],
    ]):
        raise SystemExit("R2 historical correction-space gate moved")

    current_missing = {
        "equivalent_unimodular_cech_glue_materialized": bool(d2_status["equivalent_unimodular_cech_glue_materialized"]),
        "line_bundle_gm_1_cocycle_ell_ij_materialized": bool(d2_status["line_bundle_gm_1_cocycle_ell_ij_materialized"]),
        "literal_mu2_2_cocycle_materialized": bool(d2_status["literal_mu2_2_cocycle_materialized"]),
        "same_representative_transport_materialized": bool(d2_status["same_representative_transport_materialized"]),
        "square_root_1_cochain_r_ij_materialized": bool(d2_status["square_root_1_cochain_r_ij_materialized"]),
        "triple_overlap_action_difference_identity_verified": bool(d2_status["triple_overlap_action_difference_identity_verified"]),
        "single_global_a2_02_kummer_or_brauer_representative_materialized": bool(
            b3b1["construction_status"]["single_global_a2_02_kummer_or_brauer_representative_materialized"]
        ),
    }
    if any(current_missing.values()):
        raise SystemExit("expected R5 correction-space blocker unexpectedly moved")
    if not b3a["cover_indexed_materialization"]["all_8_packages_pulled_back_to_all_317_source_charts"]:
        raise SystemExit("B3A 317 package pullbacks moved")
    if not b3a["cover_indexed_materialization"]["all_8_packages_assigned_to_all_1757_common_refinement_pieces_via_source_projection"]:
        raise SystemExit("B3A 1757 package assignments moved")
    if not b3b1["cover_indexed_materialization"]["all_8_uniformizers_pulled_back_to_all_317_source_charts"]:
        raise SystemExit("B3B1 317 uniformizer pullbacks moved")
    if not b3b2["formal_tame_symbol_sum"]["formal_symbol_sum_materialized"]:
        raise SystemExit("B3B2 formal symbol sum moved")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1c.nonconstant_exceptional_swap23_correction_preflight.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1C_NONCONSTANT_EXCEPTIONAL_SWAP23_CORRECTION_PREFLIGHT",
        "role": "EXACT_NONCREDIT_PREFLIGHT_REDUCING_NONCONSTANT_EXCEPTIONAL_CORRECTION_TO_TWO_SOURCE_BOUND_SWAP23_ORBITS_AND_IDENTIFYING_MISSING_CECH_DATA",
        "entry": {"pr": 1695, "authority": AUTHORITY, "stage33_progress": "6/11"},
        "source_locks": {
            "r5b2d2_swap23_common_refinement_sha256": D2_SHA,
            "r5b3a_literal_package_pullbacks_sha256": B3A_SHA,
            "r5b3b1_boundary_uniformizers_sha256": B3B1_SHA,
            "r5b3b2_formal_symbol_sum_sha256": B3B2_SHA,
            "r2_literal_mu2_or_unimodular_cech_glue_contract_sha256": R2_SHA,
            "v91c1d_historical_cech_cartier_assembly_sha256": V1D_SHA,
            "r5b3b3c4b1a_obstruction_census_sha256": C4B1A_SHA,
            "r5b3b3c4b1b_scalar_gauge_sha256": C4B1B_SHA,
        },
        "nonconstant_exceptional_targets": {
            "exceptional_count": 4,
            "exceptional_ids": NONCONSTANT,
            "raw_local_projective_factor_hash_count": len(raw_factor_hashes),
            "rows": target_rows,
            "raw_local_factor_hashes_are_not_global_geometric_identifiers_across_distinct_p1_parameterizations": True,
        },
        "swap23_orbit_reduction": {
            "source_bound_exceptional_swap23_action_materialized_by_r5b2d2": True,
            "nonconstant_target_set_is_swap23_stable": True,
            "orbit_count": len(orbit_rows),
            "orbits": orbit_rows,
            "required_transport_scope": "COMPARE_AND_CORRECT_RESIDUE_SQUARECLASSES_ONLY_AFTER_PULLBACK_THROUGH_THE_SOURCE_BOUND_R5B2D2_TANGENT_MAP_AND_1757_COMMON_REFINEMENT",
        },
        "available_r5_inputs": {
            "whole_resolved_surface_317_cover_materialized": True,
            "swap23_1757_common_refinement_materialized": True,
            "eight_literal_residue_functions_on_317_and_1757_materialized": True,
            "eight_matching_boundary_uniformizers_on_317_and_1757_materialized": True,
            "formal_eight_symbol_sum_materialized": True,
        },
        "missing_source_bound_correction_data": current_missing,
        "historical_reuse_audit": {
            "v91c1d_cartier_correction": "ZERO",
            "v91c1d_cartier_transition_unit": "ONE",
            "v91c1d_supplies_no_hidden_nonconstant_correction_for_the_new_r5_symbol_sum": True,
            "j2_literal_cech_template_may_not_be_relabelled_as_a2_02_source_representative": True,
            "reason": "R2 requires a source-bound A2_02 representative and explicitly firewalls J2-specific data from relabelling.",
        },
        "exact_consequence": {
            "constant_uniformizer_gauge_is_already_insufficient": True,
            "nonconstant_exceptional_problem_reduces_equivariantly_to_two_swap23_orbits": True,
            "the_two_orbit_representative_corrections_cannot_be_chosen_independently_of_their_swap23_transports": True,
            "existing_r5_cover_data_is_sufficient_to_state_the_common_refinement_transport_problem": True,
            "existing_r5_data_is_not_yet_sufficient_to_certify_an_allowed_nonconstant_cech_correction": True,
            "no_corrected_global_representative_or_unramifiedness_credit_follows": True,
        },
        "next_missing_object": "EXACT_R5B2D2_TANGENT_MAP_PULLBACK_COMPARISON_OF_THE_C4B1_NONCONSTANT_RESIDUE_CLASSES_ON_ORBITS_EXC_003_EXC_011_AND_EXC_004_EXC_012_THEN_A_SOURCE_BOUND_1757_REFINEMENT_UNIT_OR_CECH_COCHAIN_CORRECTION_WITH_BOUNDARY_RESIDUES_PRESERVED",
        "next_exact_leaf": "V91C1X_R5B3B3C4B1D_SWAP23_TANGENT_PULLBACK_COMPARISON_OF_FOUR_NONCONSTANT_EXCEPTIONAL_RESIDUES",
        "parallel_outstanding_leaf": "V91C1X_R5B3B3C4B2_STRICT_PRIME_CROSS_CARRIER_INCIDENCE_AND_RESIDUE_FIELD_SQUARECLASS_REDUCTION",
        "construction_status": {
            "four_nonconstant_exceptional_targets_source_locked": True,
            "two_swap23_orbits_materialized": True,
            "swap23_tangent_pullback_of_obstruction_squareclasses_computed": False,
            "source_bound_nonconstant_cech_correction_space_materialized": False,
            "corrected_global_representative_materialized": False,
            "exceptional_residue_cancellation_verified": False,
            "all_codimension_one_residue_cancellation_verified": False,
            "unramifiedness_verified": False,
        },
        "credit_firewall": {
            "authority_promotion": False,
            "genuine_full_surface_h2_mu2_lift_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "mask20_credit": False,
            "source_bound_dim5_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "hostile_audit_credit": False,
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
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    else:
        if not OUT.exists():
            raise SystemExit("materialized C4B1C artifact is missing")
        current = json.loads(OUT.read_text(encoding="utf-8"))
        if current != cert:
            raise SystemExit("materialized C4B1C artifact is stale")
    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B3B3C4B1C_NONCONSTANT_SWAP23_PREFLIGHT_EXACT",
        "canonical_sha256": cert["canonical_sha256"],
        "nonconstant_exceptional_count": 4,
        "swap23_orbit_count": cert["swap23_orbit_reduction"]["orbit_count"],
        "orbit_members": [row["orbit_members"] for row in cert["swap23_orbit_reduction"]["orbits"]],
        "next_exact_leaf": cert["next_exact_leaf"],
        "stage33_progress": "6/11",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
