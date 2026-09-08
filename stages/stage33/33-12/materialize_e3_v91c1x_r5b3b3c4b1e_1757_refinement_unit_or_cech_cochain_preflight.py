#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
D2 = HERE / "e3-v91c1x-r5b2d2-swap23-317-cover-common-refinement.json"
C4B1D = HERE / "e3-v91c1x-r5b3b3c4b1d-swap23-tangent-pullback-comparison.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b1e-1757-refinement-unit-or-cech-cochain-preflight.json"

D2_SHA = "3165eab3d08ed29dcba429ed9f397d49054739459b08507e6a63d1cba2d66cbb"
C4B1D_SHA = "0b63663ce9e4eda381e7665dbf7722969898ebf931806b5eec3687579882c11e"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
TARGETS = ["EXC_003", "EXC_004", "EXC_011", "EXC_012"]


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


def factor_signature(row: dict) -> list[str]:
    return sorted(
        x["projective_factor_sha256"]
        for x in row["squareclass_difference"]["odd_irreducible_factors"]
    )


def build_certificate() -> dict:
    d2 = load_locked(D2, D2_SHA)
    c4b1d = load_locked(C4B1D, C4B1D_SHA)

    if d2["common_refinement_index"]["total_piece_count"] != 1757:
        raise SystemExit("R5B2D2 common refinement count moved")
    if not d2["common_refinement_index"]["equals_1757"]:
        raise SystemExit("R5B2D2 no longer identifies the common refinement as 1757")
    if not d2["construction_status"]["cover_action_or_common_refinement_materialized"]:
        raise SystemExit("R5B2D2 common refinement materialization moved")

    consequence = c4b1d["exact_consequence"]
    if not consequence["four_current_nonconstant_residue_squareclasses_compared_on_common_function_fields"]:
        raise SystemExit("C4B1D comparison boundary moved")
    if consequence["all_four_current_residue_classes_swap23_compatible"]:
        raise SystemExit("C4B1D unexpectedly became swap23-compatible")
    if consequence["source_bound_cech_or_refinement_unit_correction_materialized"]:
        raise SystemExit("C4B1D already claims the correction now targeted by C4B1E")

    node_rows = {
        row["source_node"]: row
        for row in d2["exceptional_common_refinement"]["node_rows"]
    }
    if any(eid not in node_rows for eid in TARGETS):
        raise SystemExit("one of the four C4B1D exceptional sources escaped the D2 refinement")

    orbits = c4b1d["swap23_nonconstant_orbit_comparison"]["orbits"]
    if len(orbits) != 2:
        raise SystemExit("C4B1D orbit count moved")

    attachment_rows = []
    orbit_rows = []
    seen_sources = set()
    directed_count = 0

    for orbit in orbits:
        members = sorted(orbit["orbit_members"])
        directed = orbit["directed_comparisons"]
        if len(members) != 2 or len(directed) != 2:
            raise SystemExit("C4B1D two-point swap23 orbit shape moved")
        if orbit["same_squareclass_in_both_directions"]:
            raise SystemExit("C4B1D orbit unexpectedly became squareclass-compatible")
        if not orbit["source_bound_p1_involution_verified"]:
            raise SystemExit("C4B1D source-bound P1 involution verification moved")

        pair_factor_signatures = []
        for comparison in directed:
            source = comparison["source_exceptional_id"]
            target = comparison["target_exceptional_id"]
            if source not in TARGETS or target not in TARGETS:
                raise SystemExit("C4B1D directed comparison target set moved")
            if source in seen_sources:
                raise SystemExit(f"duplicate directed source in C4B1D: {source}")
            seen_sources.add(source)

            refinement = node_rows[source]
            if refinement["acted_target_node"] != target:
                raise SystemExit(
                    f"C4B1D/D2 swap23 target mismatch: {source}: "
                    f"{target} != {refinement['acted_target_node']}"
                )
            if refinement["common_refinement_piece_count"] != 36:
                raise SystemExit(f"D2 exceptional piece count moved for {source}")

            sq = comparison["squareclass_difference"]
            if sq["square_trivial"]:
                raise SystemExit(f"C4B1D difference unexpectedly square-trivial for {source}->{target}")
            if comparison["classification"] != "NONSQUARE_SQUARECLASS_DIFFERENCE_AFTER_SOURCE_BOUND_SWAP23_TANGENT_PULLBACK":
                raise SystemExit(f"C4B1D classification moved for {source}->{target}")

            sig = factor_signature(comparison)
            pair_factor_signatures.append(sig)
            attachment_rows.append({
                "source_exceptional_id": source,
                "target_exceptional_id": target,
                "difference_classification": comparison["classification"],
                "difference_rational_Qi_t_sha256": comparison["source_over_pulled_target_rational_Qi_t_sha256"],
                "difference_factorization_scalar_Qi": sq["factorization_scalar_Qi"],
                "difference_coefficient_is_square_in_Qi": sq["coefficient_is_square_in_Qi"],
                "difference_odd_irreducible_factor_count": sq["odd_irreducible_factor_count"],
                "difference_odd_factor_projective_sha256": sig,
                "source_bound_pgl2_matrix_sha256": comparison["pgl2_matrix_sha256"],
                "d2_common_refinement_piece_count": refinement["common_refinement_piece_count"],
                "d2_36_piece_descriptors_sha256": refinement["36_piece_descriptors_sha256"],
                "d2_pulled_target_node_localizer_factorized_recipe_sha256": refinement["pulled_target_node_localizer_factorized_recipe_sha256"],
                "d2_swap23_tangent_map_derivative_commitment_sha256": refinement["swap23_tangent_map_derivative_commitment_sha256"],
            })
            directed_count += 1

        same_odd_support = pair_factor_signatures[0] == pair_factor_signatures[1]
        if not same_odd_support:
            raise SystemExit(f"forward/reverse C4B1D odd factor support moved on orbit {members}")
        orbit_rows.append({
            "orbit_members": members,
            "directed_comparison_count": 2,
            "forward_reverse_same_odd_factor_support": True,
            "odd_factor_projective_sha256": pair_factor_signatures[0],
            "literal_square_root_1_cochain_on_1757_refinement_materialized": False,
        })

    if directed_count != 4 or seen_sources != set(TARGETS):
        raise SystemExit("C4B1D four-directed-comparison boundary moved")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c4b1e.refinement_unit_or_cech_cochain_preflight.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C4B1E_SOURCE_BOUND_1757_REFINEMENT_UNIT_OR_CECH_COCHAIN_REALIZATION_FOR_SWAP23_ORBIT_DIFFERENCES",
        "role": "EXACT_NONCREDIT_ATTACHMENT_OF_THE_FOUR_C4B1D_SWAP23_ORBIT_DIFFERENCE_SQUARECLASSES_TO_THE_SOURCE_BOUND_1757_COMMON_REFINEMENT",
        "entry": {
            "authority": AUTHORITY,
            "stage33_progress": "6/11",
            "merged_parent_pr": 1695,
        },
        "source_locks": {
            "r5b2d2_swap23_317_cover_common_refinement_sha256": D2_SHA,
            "r5b3b3c4b1d_swap23_tangent_pullback_comparison_sha256": C4B1D_SHA,
        },
        "preflight_counts": {
            "global_common_refinement_piece_count": 1757,
            "nonconstant_swap23_orbit_count": 2,
            "directed_orbit_difference_count": directed_count,
            "exceptional_common_refinement_piece_slots_attached": directed_count * 36,
        },
        "orbit_attachment": {
            "rows": orbit_rows,
            "directed_rows": sorted(
                attachment_rows,
                key=lambda row: (row["source_exceptional_id"], row["target_exceptional_id"]),
            ),
        },
        "exact_consequence": {
            "all_four_c4b1d_orbit_differences_attached_to_their_source_bound_d2_exceptional_refinement_blocks": True,
            "all_four_d2_acted_targets_match_the_c4b1d_source_bound_swap23_targets": True,
            "both_swap23_orbits_have_forward_reverse_matching_odd_factor_support": True,
            "source_bound_1757_common_refinement_already_materialized": True,
            "literal_per_piece_refinement_unit_for_orbit_difference_materialized": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
            "exceptional_residue_cancellation_verified": False,
            "unramifiedness_verified": False,
        },
        "diagnostic_boundary": {
            "what_is_now_exact": "the four non-square C4B1D orbit-difference squareclass commitments are source/target matched to the exact four 36-piece exceptional blocks of the already-materialized 1757 swap23 common refinement",
            "what_is_still_missing": "literal cover-indexed unit/cochain formulas realizing those difference squareclasses on the refinement, together with r_ij^2=ell_ij and the required triple-overlap action-difference identity",
            "hash_only_attachment_is_not_a_cech_cochain": True,
            "nonsquare_global_difference_is_not_used_as_an_allowed_global_correction": True,
        },
        "next_exact_step": "reconstruct the literal C4B1D difference rational functions and D2 per-piece localizer/projection formulas on the four attached 36-piece blocks; then solve or refute the required cover-indexed ell_ij/r_ij equations before any H2-fixedness credit",
        "parallel_outstanding_leaf": c4b1d["parallel_outstanding_leaf"],
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    cert = build_certificate()
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        print(f"wrote {OUT}")
        print(cert["canonical_sha256"])
        return
    if not OUT.exists():
        raise SystemExit(f"missing materialized certificate: {OUT}")
    current = json.loads(OUT.read_text(encoding="utf-8"))
    if current != cert:
        raise SystemExit("materialized C4B1E preflight certificate differs from exact rebuild")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
