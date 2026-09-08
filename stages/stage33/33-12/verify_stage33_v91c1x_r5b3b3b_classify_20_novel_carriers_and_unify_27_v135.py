#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import materialize_e3_v91c1x_r5b3b3b_classify_20_novel_carriers_and_unify_27 as mat

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1x-r5b3b3b-classify-20-novel-carriers-and-unify-27.json"
CERT_SHA = "7f52f0988cb82983afc0759272e2420e73944b4258940aeffc8a9923816c4a7d"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
NEXT = "V91C1X_R5B3B3C_FACTOR_AND_PRIME_DECOMPOSE_ONLY_OFFBOUNDARY_CARRIERS_THEN_COMPUTE_COMBINED_TAME_RESIDUES"
BOUNDARY_IDS = ["LIN_002", "LIN_003", "LIN_006", "LIN_014"]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main():
    stored = json.loads(CERT.read_text(encoding="utf-8"))
    body = dict(stored)
    claimed = body.pop("canonical_sha256", None)
    if claimed != CERT_SHA or csha(body) != CERT_SHA:
        raise SystemExit("R5B3B3B canonical sha invalid")
    rebuilt = mat.build_certificate()
    if rebuilt != stored:
        raise SystemExit("R5B3B3B exact replay differs from stored certificate")
    if stored["candidate"] != "V91C1X_R5B3B3B_CLASSIFY_20_NOVEL_PI_CARRIERS_AND_UNIFY_ALL_27_BY_EXACT_SIGN_NORM_SUPPORT":
        raise SystemExit("R5B3B3B candidate moved")
    if stored["entry"]["authority"] != AUTHORITY or stored["entry"]["stage33_progress"] != "6/11":
        raise SystemExit("authority or Stage33 progress moved")

    model = stored["surface_sign_norm_model"]
    if model["full_sign_norm_degree"] != 16 or model["coefficient_field"] != "Q(i)":
        raise SystemExit("sign-norm model moved")
    if model["exact_computation"] != "FOUR_QUADRATIC_NORMS_IN_16_BASIS_MASK_ALGEBRA_WITHOUT_RADICAL_EXPRESSION_EXPANSION":
        raise SystemExit("exact norm computation contract moved")

    novel = stored["novel_20_exact_norm_classification"]
    if novel["carrier_count"] != 20 or novel["boundary_only_count"] != 0 or novel["off_boundary_count"] != 20:
        raise SystemExit("novel 20 classification moved")
    if novel["all_are_pi_D_only"] is not True:
        raise SystemExit("novel carriers are no longer pi_D-only")
    if novel["normalized_norm_term_count_histogram"] != {"114": 4, "150": 8, "153": 8}:
        raise SystemExit("novel norm term histogram moved")
    if novel["irreducible_factorization_of_offboundary_norms_materialized"] is not False:
        raise SystemExit("novel factorization firewall moved")
    if len(novel["carrier_rows"]) != 20:
        raise SystemExit("novel carrier row count moved")
    for row in novel["carrier_rows"]:
        if row["appears_in_pi_D"] is not True or row["appears_in_f_D"] is not False:
            raise SystemExit(f"novel pi/f membership moved: {row['carrier_id']}")
        if row["boundary_only"] is not False or row["normalized_full_sign_norm_term_count"] <= 1:
            raise SystemExit(f"novel offboundary classification moved: {row['carrier_id']}")
        if row["irreducible_noncoordinate_factorization_materialized"] is not False:
            raise SystemExit(f"novel factorization overclaim: {row['carrier_id']}")

    unified = stored["unified_27_classification"]
    expected = {
        "carrier_count": 27,
        "reused_retained_count": 7,
        "newly_classified_by_exact_norm_count": 20,
        "boundary_only_count": 4,
        "off_boundary_count": 23,
        "pi_D_boundary_only_count": 0,
        "pi_D_off_boundary_count": 20,
        "f_D_boundary_only_count": 4,
        "f_D_off_boundary_count": 3,
    }
    for key, value in expected.items():
        if unified[key] != value:
            raise SystemExit(f"unified 27 count moved: {key}")
    if unified["boundary_only_carrier_ids"] != BOUNDARY_IDS:
        raise SystemExit("unified boundary-only ids moved")
    if len(unified["off_boundary_carrier_ids"]) != 23 or set(unified["off_boundary_carrier_ids"]) & set(BOUNDARY_IDS):
        raise SystemExit("unified offboundary ids moved")
    if unified["all_27_carriers_classified_boundary_vs_offboundary"] is not True:
        raise SystemExit("unified 27 classification flag lost")

    status = stored["construction_status"]
    for key in [
        "all_20_novel_pi_D_carrier_full_sign_norms_computed_exactly_over_Qi",
        "all_20_novel_pi_D_carriers_classified_by_exact_norm_support",
        "all_27_carriers_classified_boundary_vs_offboundary",
    ]:
        if status[key] is not True:
            raise SystemExit(f"R5B3B3B construction progress lost: {key}")
    for key in [
        "offboundary_norm_irreducible_factorization_materialized",
        "all_offboundary_carrier_hyperplane_sections_prime_decomposed_on_resolved_surface",
        "combined_tame_residue_squareclasses_audited",
        "offboundary_codimension_one_residue_cancellation_verified",
        "single_global_a2_02_kummer_or_brauer_representative_materialized",
        "line_bundle_gm_1_cocycle_ell_ij_materialized",
        "square_root_1_cochain_r_ij_materialized",
        "literal_mu2_2_cocycle_materialized",
        "equivalent_unimodular_cech_glue_materialized",
        "same_representative_swap23_transport_materialized",
        "triple_overlap_action_difference_identity_verified",
    ]:
        if status[key] is not False:
            raise SystemExit(f"R5B3B3B construction firewall violated: {key}")
    if stored["next_exact_leaf"] != NEXT:
        raise SystemExit("R5B3B3B routing moved")
    for key, value in stored["credit_firewall"].items():
        if value is not False:
            raise SystemExit(f"R5B3B3B credit firewall violated: {key}")

    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B3B3B_20_NOVEL_27_UNIFIED_SIGN_NORM_SUPPORT_VERIFIED",
        "certificate_sha256": claimed,
        "novel_off_boundary_count": 20,
        "unified_boundary_only_count": 4,
        "unified_off_boundary_count": 23,
        "pi_D_off_boundary_count": 20,
        "f_D_off_boundary_count": 3,
        "next_exact_leaf": NEXT,
        "stage33_progress": "6/11",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
