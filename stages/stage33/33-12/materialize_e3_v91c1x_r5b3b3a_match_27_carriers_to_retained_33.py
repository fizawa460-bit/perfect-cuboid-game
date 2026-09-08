#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import materialize_e3_v91c1x_r5b3b2_a2_02_formal_tame_symbol_hidden_carrier_inventory as b3b2mat

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
SPLIT = S07 / "ambient-linear-carrier-boundary-offboundary-split.json"
OUT = HERE / "e3-v91c1x-r5b3b3a-match-27-carriers-to-retained-33.json"
B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
SPLIT_SHA = "13140597dd2196a0593038534a789a75b2f92cf389df34b2f61462835a9b6abb"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
COORDS = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]
ZERO_QI = [0, 1, 0, 1]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical lock moved: {path.name}")
    return obj


def split_coefficients(row):
    sparse = {x["coordinate"]: x["coefficient_Qi"] for x in row["ambient_linear_form"]}
    return [sparse.get(name, ZERO_QI) for name in COORDS]


def build_certificate():
    b3b2 = load(B3B2, B3B2_SHA)
    split = load(SPLIT, SPLIT_SHA)

    if split["carrier_split"]["total_distinct_projective_ambient_linear_forms"] != 33:
        raise SystemExit("retained Stage33-07 distinct carrier count moved")
    if split["carrier_split"]["boundary_only_hyperplanes"] != 18:
        raise SystemExit("retained Stage33-07 boundary-only count moved")
    if split["carrier_split"]["off_boundary_candidate_hyperplanes"] != 15:
        raise SystemExit("retained Stage33-07 off-boundary count moved")

    retained = {}
    for row in split["carrier_records"]:
        coeffs = split_coefficients(row)
        key, normalized = b3b2mat.projective_key(coeffs)
        if key in retained:
            raise SystemExit(f"duplicate projective key in retained 33: {row['carrier_index_1based']}")
        retained[key] = {
            "retained_carrier_index_1based": int(row["carrier_index_1based"]),
            "projective_linear_form_Qi_sha256": key,
            "normalized_coefficients_Qi": normalized,
            "classification": row["classification"],
            "boundary_only": bool(row["boundary_only"]),
            "norm_factorization_over_Qi": row["norm_factorization_over_Qi"],
        }
    if len(retained) != 33:
        raise SystemExit(f"retained Stage33-07 projective carrier count moved: {len(retained)}")

    current = b3b2["finite_linear_carrier_inventory"]["carrier_rows"]
    if len(current) != 27:
        raise SystemExit("R5B3B2 27-carrier inventory moved")

    rows = []
    matched = []
    novel = []
    for row in current:
        key = row["projective_linear_form_Qi_sha256"]
        is_match = key in retained
        old = retained.get(key)
        out = {
            "carrier_id": row["carrier_id"],
            "projective_linear_form_Qi_sha256": key,
            "appears_in_pi_D": row["appears_in_pi_D"],
            "appears_in_f_D": row["appears_in_f_D"],
            "matches_retained_stage33_07_carrier": is_match,
            "retained_carrier_index_1based": old["retained_carrier_index_1based"] if old else None,
            "retained_classification": old["classification"] if old else None,
            "retained_boundary_only": old["boundary_only"] if old else None,
        }
        rows.append(out)
        (matched if is_match else novel).append(row["carrier_id"])

    pi_matched = sum(r["appears_in_pi_D"] and r["matches_retained_stage33_07_carrier"] for r in rows)
    f_matched = sum(r["appears_in_f_D"] and r["matches_retained_stage33_07_carrier"] for r in rows)
    pi_novel = sum(r["appears_in_pi_D"] and not r["matches_retained_stage33_07_carrier"] for r in rows)
    f_novel = sum(r["appears_in_f_D"] and not r["matches_retained_stage33_07_carrier"] for r in rows)
    matched_boundary = sum(r["matches_retained_stage33_07_carrier"] and r["retained_boundary_only"] is True for r in rows)
    matched_off = sum(r["matches_retained_stage33_07_carrier"] and r["retained_boundary_only"] is False for r in rows)

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3a.match_27_carriers_to_retained_33.v2",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3A_MATCH_27_SYMBOL_CARRIERS_TO_RETAINED_STAGE33_07_33_CARRIERS",
        "role": "EXACT_NONCREDIT_REUSE_PARTITION_BEFORE_PRIME_DECOMPOSITION_AND_TAME_RESIDUE_AUDIT",
        "entry": {"pr": 1695, "authority": AUTHORITY, "stage33_progress": "6/11"},
        "source_locks": {
            "r5b3b2_formal_symbol_carrier_inventory_sha256": B3B2_SHA,
            "stage33_07_ambient_linear_carrier_boundary_offboundary_split_sha256": SPLIT_SHA,
        },
        "retained_stage33_07_33": {
            "distinct_projective_carrier_count": len(retained),
            "boundary_only_hyperplane_count": split["carrier_split"]["boundary_only_hyperplanes"],
            "off_boundary_candidate_hyperplane_count": split["carrier_split"]["off_boundary_candidate_hyperplanes"],
            "source_certificate_is_the_formal_stage33_07_33_carrier_inventory_not_a_naive_reconstruction_from_boundary_function_packages": True,
        },
        "match_partition": {
            "current_carrier_count": len(rows),
            "matched_retained_33_count": len(matched),
            "novel_relative_to_retained_33_count": len(novel),
            "matched_carrier_ids": matched,
            "novel_carrier_ids": novel,
            "pi_D_matched_count": pi_matched,
            "pi_D_novel_count": pi_novel,
            "f_D_matched_count": f_matched,
            "f_D_novel_count": f_novel,
            "matched_boundary_only_count": matched_boundary,
            "matched_off_boundary_count": matched_off,
            "carrier_rows": rows,
        },
        "construction_status": {
            "retained_stage33_07_33_carrier_inventory_exactly_source_locked": True,
            "r5b3b2_27_carriers_partitioned_by_exact_projective_match": True,
            "retained_stage33_07_norm_split_reused_for_matched_carriers": True,
            "novel_carrier_full_sign_norms_factorized": False,
            "all_27_carriers_classified_boundary_vs_offboundary": False,
            "all_27_carriers_prime_decomposed_on_resolved_surface": False,
            "combined_tame_residue_squareclasses_audited": False,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "single_global_a2_02_kummer_or_brauer_representative_materialized": False,
        },
        "exact_consequence": {
            "prime_decomposition_work_is_partitioned_into_reused_stage33_07_carriers_and_genuinely_new_carriers": True,
            "matched_carriers_inherit_only_the_retained_stage33_07_boundary_vs_offboundary_sign_norm_classification": True,
            "this_match_partition_alone_does_not_identify_prime_divisors_or_prove_residue_cancellation": True,
        },
        "next_missing_object": "FULL_SIGN_NORM_FACTORIZATION_FOR_ONLY_THE_NOVEL_R5B3B2_CARRIERS_THEN_UNIFIED_27_CARRIER_BOUNDARY_OFFBOUNDARY_CLASSIFICATION_BEFORE_PRIME_DECOMPOSITION",
        "next_exact_leaf": "V91C1X_R5B3B3B_CLASSIFY_NOVEL_CARRIERS_BY_FULL_SIGN_NORM_AND_UNIFY_ALL_27",
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    p = cert["match_partition"]
    print(json.dumps({
        "success": True,
        "candidate": cert["candidate"],
        "canonical_sha256": cert["canonical_sha256"],
        "matched_retained_33_count": p["matched_retained_33_count"],
        "novel_relative_to_retained_33_count": p["novel_relative_to_retained_33_count"],
        "pi_D_matched_count": p["pi_D_matched_count"],
        "pi_D_novel_count": p["pi_D_novel_count"],
        "f_D_matched_count": p["f_D_matched_count"],
        "f_D_novel_count": p["f_D_novel_count"],
        "matched_boundary_only_count": p["matched_boundary_only_count"],
        "matched_off_boundary_count": p["matched_off_boundary_count"],
        "stage33_progress": "6/11",
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
