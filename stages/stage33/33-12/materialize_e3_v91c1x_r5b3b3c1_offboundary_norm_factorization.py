#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b3b3b_classify_20_novel_carriers_and_unify_27 as b3b3b

HERE = Path(__file__).resolve().parent
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
B3B3B = HERE / "e3-v91c1x-r5b3b3b-classify-20-novel-carriers-and-unify-27.json"
OUT = HERE / "e3-v91c1x-r5b3b3c1-offboundary-norm-factorization.json"
B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
B3B3B_SHA = "7f52f0988cb82983afc0759272e2420e73944b4258940aeffc8a9923816c4a7d"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def factor_row(row):
    poly = b3b3b.full_sign_norm_poly(row["normalized_coefficients_Qi"])
    if poly.total_degree() != 16:
        raise SystemExit(f"full sign norm degree moved: {row['carrier_id']}")
    coeff, factors = sp.factor_list(poly.as_expr(), *b3b3b.BASE, extension=sp.I)
    rebuilt = sp.Poly(coeff, *b3b3b.BASE, extension=sp.I)
    out = []
    for fac_expr, multiplicity in factors:
        fac = sp.Poly(fac_expr, *b3b3b.BASE, extension=sp.I)
        rebuilt *= fac**multiplicity
        normalized = b3b3b.normalize_norm(fac)
        out.append({
            "factor_total_degree": int(fac.total_degree()),
            "multiplicity": int(multiplicity),
            "normalized_factor_sha256": csha(normalized),
            "normalized_factor_term_count": len(normalized),
        })
    if sp.Poly(rebuilt - poly, *b3b3b.BASE, extension=sp.I) != sp.Poly(0, *b3b3b.BASE, extension=sp.I):
        raise SystemExit(f"factor reconstruction failed: {row['carrier_id']}")
    if sum(x["factor_total_degree"] * x["multiplicity"] for x in out) != 16:
        raise SystemExit(f"factor degree sum moved: {row['carrier_id']}")
    return {
        "carrier_id": row["carrier_id"],
        "projective_linear_form_Qi_sha256": row["projective_linear_form_Qi_sha256"],
        "factor_count_distinct": len(out),
        "factor_count_with_multiplicity": sum(x["multiplicity"] for x in out),
        "squarefree_factorization": all(x["multiplicity"] == 1 for x in out),
        "factor_degree_multiset": sorted(
            [x["factor_total_degree"] for x in out for _ in range(x["multiplicity"])]
        ),
        "factors": out,
    }


def build_certificate():
    b3b2 = b3b3b.load(B3B2, B3B2_SHA)
    b3b3b_cert = b3b3b.load(B3B3B, B3B3B_SHA)
    inv = b3b2["finite_linear_carrier_inventory"]
    cls = b3b3b_cert["unified_27_classification"]
    off_ids = list(cls["off_boundary_carrier_ids"])
    if len(off_ids) != cls["off_boundary_count"]:
        raise SystemExit("off-boundary carrier count/list mismatch")
    rows = {r["carrier_id"]: r for r in inv["carrier_rows"]}
    if any(cid not in rows for cid in off_ids):
        raise SystemExit("off-boundary carrier escaped R5B3B2 inventory")

    factored = [factor_row(rows[cid]) for cid in off_ids]
    degree_patterns = Counter(tuple(r["factor_degree_multiset"]) for r in factored)
    factor_to_carriers = defaultdict(list)
    for row in factored:
        for fac in row["factors"]:
            factor_to_carriers[fac["normalized_factor_sha256"]].append(row["carrier_id"])
    shared = [
        {"normalized_factor_sha256": sha, "carrier_ids": sorted(ids), "carrier_count": len(ids)}
        for sha, ids in sorted(factor_to_carriers.items())
        if len(ids) > 1
    ]

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c1.offboundary_norm_factorization.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C1_FACTOR_ONLY_OFFBOUNDARY_FULL_SIGN_NORMS",
        "role": "EXACT_NONCREDIT_IRREDUCIBLE_FACTORIZATION_OF_THE_R5B3B3B_OFFBOUNDARY_BASE_NORMS_BEFORE_RESOLVED_SURFACE_PRIME_DECOMPOSITION",
        "entry": {"pr": 1695, "authority": AUTHORITY, "stage33_progress": "6/11"},
        "source_locks": {
            "r5b3b2_formal_symbol_carrier_inventory_sha256": B3B2_SHA,
            "r5b3b3b_unified_boundary_classification_sha256": B3B3B_SHA,
        },
        "exact_factorization": {
            "coefficient_field": "Q(i)",
            "ambient_ring": "Q(i)[a1,a2,a3]",
            "input_full_sign_norm_degree": 16,
            "off_boundary_carrier_count": len(factored),
            "all_and_only_r5b3b3b_off_boundary_carriers_processed": [r["carrier_id"] for r in factored] == off_ids,
            "all_factorizations_reconstructed_exactly": True,
            "all_factor_degree_sums_equal_16": all(sum(r["factor_degree_multiset"]) == 16 for r in factored),
            "all_factorizations_squarefree": all(r["squarefree_factorization"] for r in factored),
            "factor_degree_pattern_histogram": {
                "+".join(map(str, pattern)): count for pattern, count in sorted(degree_patterns.items())
            },
            "unique_irreducible_factor_sha256_count": len(factor_to_carriers),
            "shared_irreducible_factor_support": shared,
            "carrier_rows": factored,
        },
        "construction_status": {
            "offboundary_norm_irreducible_factorization_materialized": True,
            "all_offboundary_carrier_hyperplane_sections_prime_decomposed_on_resolved_surface": False,
            "combined_tame_residue_squareclasses_audited": False,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "single_global_a2_02_kummer_or_brauer_representative_materialized": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "equivalent_unimodular_cech_glue_materialized": False,
            "same_representative_swap23_transport_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
        },
        "exact_consequence": {
            "base_norm_factorization_is_now_finite_and_exact_for_every_offboundary_carrier": True,
            "base_norm_irreducible_factors_are_not_identified_with_resolved_surface_prime_divisors_without_an_exact_adapter": True,
            "no_unramifiedness_or_residue_cancellation_follows_from_factorization_alone": True,
        },
        "next_missing_object": "EXACT_ADAPTER_FROM_EACH_R5B3B3C1_IRREDUCIBLE_BASE_NORM_FACTOR_TO_THE_PRIME_DIVISORS_OF_THE_CORRESPONDING_LINEAR_HYPERPLANE_SECTION_ON_THE_RESOLVED_SURFACE_THEN_COMBINED_TAME_RESIDUE_SQUARECLASS_ON_EACH_SUCH_PRIME",
        "next_exact_leaf": "V91C1X_R5B3B3C2_RESOLVED_SURFACE_PRIME_DECOMPOSITION_AND_COMBINED_TAME_RESIDUES_OVER_C1_FACTORS",
        "credit_firewall": {
            "authority_promotion": False,
            "hostile_audit_credit": False,
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
            "merge_allowed": False,
        },
    }
    body = dict(cert)
    cert["canonical_sha256"] = csha(body)
    return cert


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    cert = build_certificate()
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    else:
        print(json.dumps(cert, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
