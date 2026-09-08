#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import materialize_e3_v91c1x_r5b3b2_a2_02_formal_tame_symbol_hidden_carrier_inventory as b3b2mat

HERE = Path(__file__).resolve().parent
B3B2 = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
BF = HERE / "boundary-function-generator-source-lock.json"
OUT = HERE / "e3-v91c1x-r5b3b3a-match-27-carriers-to-retained-33.json"
B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
BF_SHA = "aaacc000f2e5fbbe733789f5f2a19d6c2cb14b5d3a26d0b8e508eea1f3bc8c96"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical lock moved: {path.name}")
    return obj


def add_old(old, coeffs, source, component, member, exponent):
    key, normalized = b3b2mat.projective_key(coeffs)
    row = old.setdefault(key, {
        "projective_linear_form_Qi_sha256": key,
        "normalized_coefficients_Qi": normalized,
        "retained_generator_appearances": [],
    })
    row["retained_generator_appearances"].append({
        "source_direction": source,
        "component_id": component,
        "member": member,
        "exponent": int(exponent),
    })


def build_certificate():
    b3b2 = load(B3B2, B3B2_SHA)
    bf = load(BF, BF_SHA)
    old = {}
    total_occ = 0
    for source in bf["generator_records"]:
        direction = source["source_direction"]
        for package in source["component_packages"]:
            component = package["component_id"]
            for factor in package["numerator_factors"]:
                exp = int(factor.get("exponent", 1))
                add_old(old, factor["coefficients_Qi"], direction, component, "NUMERATOR", exp)
                total_occ += 1
            den = package["denominator"]
            add_old(old, den["coefficients_Qi"], direction, component, "DENOMINATOR", -int(den["exponent"]))
            total_occ += 1
    if len(old) != 33:
        raise SystemExit(f"retained generator distinct carrier count moved: {len(old)}")

    current = b3b2["finite_linear_carrier_inventory"]["carrier_rows"]
    if len(current) != 27:
        raise SystemExit("R5B3B2 27-carrier inventory moved")
    rows = []
    matched = []
    novel = []
    for row in current:
        key = row["projective_linear_form_Qi_sha256"]
        is_match = key in old
        out = {
            "carrier_id": row["carrier_id"],
            "projective_linear_form_Qi_sha256": key,
            "appears_in_pi_D": row["appears_in_pi_D"],
            "appears_in_f_D": row["appears_in_f_D"],
            "matches_retained_33_generator_carrier": is_match,
            "retained_generator_appearance_count": len(old[key]["retained_generator_appearances"]) if is_match else 0,
            "retained_generator_appearances": old[key]["retained_generator_appearances"] if is_match else [],
        }
        rows.append(out)
        (matched if is_match else novel).append(row["carrier_id"])

    pi_matched = sum(r["appears_in_pi_D"] and r["matches_retained_33_generator_carrier"] for r in rows)
    f_matched = sum(r["appears_in_f_D"] and r["matches_retained_33_generator_carrier"] for r in rows)
    pi_novel = sum(r["appears_in_pi_D"] and not r["matches_retained_33_generator_carrier"] for r in rows)
    f_novel = sum(r["appears_in_f_D"] and not r["matches_retained_33_generator_carrier"] for r in rows)

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3a.match_27_carriers_to_retained_33.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3A_MATCH_27_SYMBOL_CARRIERS_TO_RETAINED_33_GENERATOR_CARRIERS",
        "role": "EXACT_NONCREDIT_REUSE_PARTITION_BEFORE_PRIME_DECOMPOSITION_AND_TAME_RESIDUE_AUDIT",
        "entry": {"pr": 1695, "authority": AUTHORITY, "stage33_progress": "6/11"},
        "source_locks": {
            "r5b3b2_formal_symbol_carrier_inventory_sha256": B3B2_SHA,
            "boundary_function_generator_source_lock_sha256": BF_SHA,
        },
        "retained_33_reconstruction": {
            "distinct_projective_generator_carrier_count": len(old),
            "raw_factor_occurrence_count": total_occ,
            "reconstructed_directly_from_all_source_direction_component_packages": True,
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
            "carrier_rows": rows,
        },
        "construction_status": {
            "retained_33_generator_carrier_inventory_exactly_reconstructed": True,
            "r5b3b2_27_carriers_partitioned_by_exact_projective_match": True,
            "retained_stage33_07_norm_split_replayed_for_matched_carriers": False,
            "novel_carrier_full_sign_norms_factorized": False,
            "all_27_carriers_prime_decomposed_on_resolved_surface": False,
            "combined_tame_residue_squareclasses_audited": False,
            "offboundary_codimension_one_residue_cancellation_verified": False,
            "single_global_a2_02_kummer_or_brauer_representative_materialized": False,
        },
        "exact_consequence": {
            "prime_decomposition_work_can_be_split_into_reusable_retained_carriers_and_genuinely_new_carriers": True,
            "this_match_partition_alone_does_not_identify_prime_divisors_or_prove_residue_cancellation": True,
        },
        "next_missing_object": "REPLAY_RETAINED_STAGE33_07_SIGN_NORM_CLASSIFICATION_ON_MATCHED_CARRIERS_AND_FACTOR_FULL_SIGN_NORMS_OF_NOVEL_CARRIERS_THEN_DECOMPOSE_ALL_OFFBOUNDARY_SUPPORT_TO_PRIMES",
        "next_exact_leaf": "V91C1X_R5B3B3B_CLASSIFY_MATCHED_AND_NOVEL_CARRIERS_BY_FULL_SIGN_NORM",
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
        "stage33_progress": "6/11",
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
