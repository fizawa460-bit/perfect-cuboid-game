#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import materialize_e3_v91c1x_r5b3b2_a2_02_formal_tame_symbol_hidden_carrier_inventory as mat

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
CERT_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
CANDIDATE = "V91C1X_R5B3B2_A2_02_FORMAL_TAME_SYMBOL_SUM_AND_HIDDEN_LINEAR_CARRIER_INVENTORY"
COMPONENTS = ["EXC_003", "EXC_004", "EXC_011", "EXC_012", "SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008"]
NEXT = "V91C1X_R5B3B3_DECOMPOSE_LINEAR_CARRIERS_AND_AUDIT_COMBINED_TAME_RESIDUES"
MISSING = "PRIME_DECOMPOSITION_ON_THE_RESOLVED_SURFACE_OF_EACH_DISTINCT_LINEAR_HYPERPLANE_CARRIER_IN_THE_EIGHT_SYMBOL_TERMS_THEN_EXACT_COMBINED_TAME_RESIDUE_SQUARECLASS_ON_EVERY_PRIME_ABOVE_THEM"


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    stored = json.loads(CERT.read_text(encoding="utf-8"))
    claimed = stored.get("canonical_sha256")
    body = dict(stored)
    body.pop("canonical_sha256", None)
    if claimed != CERT_SHA or csha(body) != CERT_SHA:
        raise SystemExit("R5B3B2 canonical sha invalid")
    if mat.build_certificate() != stored:
        raise SystemExit("R5B3B2 exact replay differs from stored certificate")

    if stored["schema"] != "stage33.e3.v91c1x_r5b3b2.a2_02_formal_tame_symbol_hidden_carrier_inventory.v1":
        raise SystemExit("R5B3B2 schema moved")
    if stored["candidate"] != CANDIDATE:
        raise SystemExit("R5B3B2 candidate moved")
    if stored["entry"]["authority"] != AUTHORITY or stored["entry"]["stage33_progress"] != "6/11":
        raise SystemExit("authority or Stage33 progress moved")

    formal = stored["formal_tame_symbol_sum"]
    if formal["source_direction"] != "A2_02" or formal["term_count"] != 8:
        raise SystemExit("formal symbol source/count moved")
    if formal["component_ids_in_source_order"] != COMPONENTS:
        raise SystemExit("formal symbol component order moved")
    if formal["formal_sum_expression"] != "SUM_D [pi_D,f_D]_2 FOR D IN A2_02_EIGHT_COMPONENTS":
        raise SystemExit("formal symbol expression moved")
    if formal["formal_symbol_sum_materialized"] is not True or formal["certified_as_unramified_global_brauer_or_kummer_representative"] is not False:
        raise SystemExit("formal symbol semantic firewall moved")
    terms = formal["terms"]
    if len(terms) != 8 or [r["component_id"] for r in terms] != COMPONENTS:
        raise SystemExit("formal term rows moved")
    for row in terms:
        if row["symbol"] != "[pi_D,f_D]_2":
            raise SystemExit(f"formal symbol notation moved: {row['component_id']}")
        if row["semantics"] != "EXACT_FORMAL_BRAUER_2_SYMBOL_TERM_NOT_YET_CERTIFIED_UNRAMIFIED":
            raise SystemExit(f"formal term semantics moved: {row['component_id']}")
        if len(row["uniformizer_factorized_Qi_sha256"]) != 64 or len(row["residue_function_Qi_sha256"]) != 64:
            raise SystemExit(f"formal term source hash missing: {row['component_id']}")

    inv = stored["finite_linear_carrier_inventory"]
    expected_counts = {
        "unique_projective_linear_carrier_count": 27,
        "uniformizer_pi_unique_linear_carrier_count": 20,
        "residue_function_f_unique_linear_carrier_count": 7,
        "pi_and_f_shared_linear_carrier_count": 0,
    }
    for key, value in expected_counts.items():
        if inv[key] != value:
            raise SystemExit(f"carrier count moved: {key}")
    if inv["all_candidate_nonexceptional_residue_support_is_reduced_to_a_finite_projective_Qi_linear_hyperplane_carrier_inventory"] is not True:
        raise SystemExit("finite carrier support conclusion lost")
    if inv["exceptional_divisor_orders_already_replayed_by_r5b3b1"] is not True:
        raise SystemExit("exceptional-order provenance moved")
    if inv["prime_decomposition_of_every_linear_carrier_on_the_resolved_surface_materialized"] is not False:
        raise SystemExit("prime-decomposition firewall violated")
    if inv["combined_residue_squareclass_on_every_prime_above_the_carriers_materialized"] is not False:
        raise SystemExit("combined-residue firewall violated")

    carriers = inv["carrier_rows"]
    if len(carriers) != 27 or [r["carrier_id"] for r in carriers] != [f"LIN_{i:03d}" for i in range(1, 28)]:
        raise SystemExit("carrier row inventory moved")
    seen_hashes = set()
    pi_count = 0
    f_count = 0
    shared_count = 0
    for row in carriers:
        h = row["projective_linear_form_Qi_sha256"]
        if len(h) != 64 or h in seen_hashes:
            raise SystemExit(f"carrier hash invalid or duplicate: {row['carrier_id']}")
        seen_hashes.add(h)
        coeffs = row["normalized_coefficients_Qi"]
        if len(coeffs) != 7 or any(len(z) != 4 or z[1] == 0 or z[3] == 0 for z in coeffs):
            raise SystemExit(f"normalized Q(i) coefficient vector malformed: {row['carrier_id']}")
        first_nonzero = next((z for z in coeffs if z[0] != 0 or z[2] != 0), None)
        if first_nonzero != [1, 1, 0, 1]:
            raise SystemExit(f"projective normalization moved: {row['carrier_id']}")
        appearances = row["appearances"]
        if not appearances:
            raise SystemExit(f"carrier has no appearances: {row['carrier_id']}")
        for a in appearances:
            if a["symbol_component"] not in COMPONENTS or a["member"] not in {"pi_D", "f_D"} or a["role"] not in {"NUMERATOR", "DENOMINATOR"}:
                raise SystemExit(f"carrier appearance malformed: {row['carrier_id']}")
        pi = any(a["member"] == "pi_D" for a in appearances)
        ff = any(a["member"] == "f_D" for a in appearances)
        if row["appears_in_pi_D"] is not pi or row["appears_in_f_D"] is not ff:
            raise SystemExit(f"carrier member flags disagree with appearances: {row['carrier_id']}")
        pi_count += int(pi)
        f_count += int(ff)
        shared_count += int(pi and ff)
    if (pi_count, f_count, shared_count) != (20, 7, 0):
        raise SystemExit("carrier membership recomputation disagrees with counts")

    supports = inv["per_symbol_support_rows"]
    if len(supports) != 8 or [r["component_id"] for r in supports] != COMPONENTS:
        raise SystemExit("per-symbol carrier support rows moved")
    for row in supports:
        if row["candidate_nonexceptional_residue_support_is_contained_in_pullbacks_of_these_linear_hyperplane_carriers"] is not True:
            raise SystemExit(f"support containment flag moved: {row['component_id']}")
        if not set(row["pi_D_linear_carriers"]).issubset(seen_hashes) or not set(row["f_D_linear_carriers"]).issubset(seen_hashes):
            raise SystemExit(f"support row references unknown carrier: {row['component_id']}")

    reuse = stored["v91c1d_reuse_audit"]
    if reuse["recorded_offboundary_height_one_residue_discrepancy"] != "ZERO_EXACT":
        raise SystemExit("V91C1D recorded label moved")
    for key in [
        "v91c1d_verifier_contains_no_squareclass_computation_path",
        "boundary_uniformizer_producer_explicitly_disclaims_squareclass_and_gersten_lift_credit",
        "v91c1d_zero_exact_label_is_not_a_source_bound_all_codimension_one_residue_witness_for_the_new_symbol_sum",
    ]:
        if reuse[key] is not True:
            raise SystemExit(f"V91C1D reuse diagnosis moved: {key}")
    if reuse["v91c1d_verifier_replays_residue_field_squareclasses_for_the_later_r5b3b1_uniformizers"] is not False:
        raise SystemExit("V91C1D squareclass replay firewall violated")

    status = stored["construction_status"]
    for key in ["eight_term_formal_tame_symbol_sum_assembled", "finite_linear_carrier_support_inventory_materialized"]:
        if status[key] is not True:
            raise SystemExit(f"R5B3B2 progress lost: {key}")
    for key in [
        "all_linear_hyperplane_carriers_prime_decomposed_on_the_resolved_surface",
        "combined_residue_field_squareclass_computed_on_every_prime_above_each_carrier",
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
            raise SystemExit(f"R5B3B2 construction firewall violated: {key}")

    consequence = stored["exact_consequence"]
    for key in [
        "the_candidate_is_now_an_exact_eight_term_formal_symbol_sum_not_merely_eight_unpaired_inputs",
        "possible_nonexceptional_residue_support_is_bounded_by_an_explicit_finite_linear_carrier_inventory",
        "the_remaining_global_gersten_gap_is_not_closed_by_the_old_v91c1d_zero_exact_label",
        "next_computation_is_finite_prime_decomposition_plus_combined_residue_squareclasses_on_the_inventory",
    ]:
        if consequence[key] is not True:
            raise SystemExit(f"R5B3B2 consequence moved: {key}")

    if stored["next_missing_object"] != MISSING or stored["next_exact_leaf"] != NEXT:
        raise SystemExit("R5B3B2 next routing moved")
    for key, value in stored["credit_firewall"].items():
        if value is not False:
            raise SystemExit(f"credit firewall violated: {key}")

    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B3B2_A2_02_FORMAL_TAME_SYMBOL_HIDDEN_CARRIER_INVENTORY_VERIFIED",
        "certificate_sha256": claimed,
        "formal_symbol_term_count": 8,
        "unique_projective_linear_carrier_count": 27,
        "uniformizer_pi_unique_linear_carrier_count": 20,
        "residue_function_f_unique_linear_carrier_count": 7,
        "pi_and_f_shared_linear_carrier_count": 0,
        "next_exact_leaf": NEXT,
        "stage33_progress": "6/11",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
