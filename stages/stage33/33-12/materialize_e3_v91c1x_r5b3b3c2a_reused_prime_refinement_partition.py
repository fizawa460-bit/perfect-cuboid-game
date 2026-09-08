#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent

B3B3A = HERE / "e3-v91c1x-r5b3b3a-match-27-carriers-to-retained-33.json"
B3B3B = HERE / "e3-v91c1x-r5b3b3b-classify-20-novel-carriers-and-unify-27.json"
C1 = HERE / "e3-v91c1x-r5b3b3c1-offboundary-norm-factorization.json"
E11_SOURCE = S33 / "33-11e" / "stage33-11e-source-lock.json"
E11_CERT = S33 / "33-11e" / "stage33-11e-prime-galois-transport-certificate.json"
OUT = HERE / "e3-v91c1x-r5b3b3c2a-reused-prime-refinement-partition.json"

B3B3A_SHA = "36bd375d08b4ebd852bb101851b108fae7e76780f2a35b6ea033948f9ddb8e77"
B3B3B_SHA = "7f52f0988cb82983afc0759272e2420e73944b4258940aeffc8a9923816c4a7d"
C1_SHA = "5c092fcec6720d0097d6e7509ce37b1506d7a099015a1a6a004250513d0f29f3"
E11_SOURCE_SHA = "a1bce01bb7041d9cc48bfb7ce6e6f6095afc36ef8bc08fcb1588a885ed61e2e2"
E11_CERT_SHA = "1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
EXPECTED_REUSED = ["LIN_013", "LIN_019", "LIN_024"]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_checked(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if csha(body) != claimed or claimed != expected:
        raise SystemExit(f"canonical lock mismatch: {path}")
    return obj


def build_certificate():
    a = load_checked(B3B3A, B3B3A_SHA)
    b = load_checked(B3B3B, B3B3B_SHA)
    c1 = load_checked(C1, C1_SHA)
    e11s = load_checked(E11_SOURCE, E11_SOURCE_SHA)
    e11 = load_checked(E11_CERT, E11_CERT_SHA)

    off_ids = list(b["unified_27_classification"]["off_boundary_carrier_ids"])
    if len(off_ids) != 23 or len(set(off_ids)) != 23:
        raise SystemExit("R5B3B3B off-boundary inventory moved")

    match_rows = {row["carrier_id"]: row for row in a["match_partition"]["carrier_rows"]}
    c1_rows = {row["carrier_id"]: row for row in c1["exact_factorization"]["carrier_rows"]}
    if set(c1_rows) != set(off_ids):
        raise SystemExit("C1/off-boundary carrier coverage mismatch")

    retained_off = sorted(
        cid for cid in off_ids
        if match_rows[cid]["matches_retained_stage33_07_carrier"]
        and match_rows[cid]["retained_boundary_only"] is False
    )
    if retained_off != EXPECTED_REUSED:
        raise SystemExit(f"reused off-boundary carrier partition moved: {retained_off}")
    novel = sorted(set(off_ids) - set(retained_off))
    if len(novel) != 20:
        raise SystemExit("novel off-boundary count moved")

    frozen_inventory = e11s["carrier_inventory"]
    refinements = e11["carrier_refinements"]
    prime_records = {row["prime_id"]: row for row in e11["prime_inventory"]["records"]}

    reused_rows = []
    reused_prime_ids = set()
    for cid in retained_off:
        m = match_rows[cid]
        carrier_hash = m["projective_linear_form_Qi_sha256"]
        if carrier_hash not in frozen_inventory:
            raise SystemExit(f"retained off-boundary carrier absent from 33-11e inventory: {cid}")
        if carrier_hash not in refinements:
            raise SystemExit(f"retained off-boundary carrier lacks 33-11e refinement: {cid}")
        pieces = refinements[carrier_hash]
        if not pieces:
            raise SystemExit(f"empty 33-11e refinement: {cid}")
        prime_rows = []
        for piece in pieces:
            pid = piece["prime_id"]
            if pid not in prime_records:
                raise SystemExit(f"33-11e prime record absent: {pid}")
            reused_prime_ids.add(pid)
            record = prime_records[pid]
            prime_rows.append({
                "prime_id": pid,
                "scheme_multiplicity_in_carrier": int(piece["multiplicity"]),
                "prime_record_kind": record["kind"],
            })
        c1row = c1_rows[cid]
        reused_rows.append({
            "carrier_id": cid,
            "projective_linear_form_Qi_sha256": carrier_hash,
            "retained_stage33_07_carrier_index_1based": m["retained_carrier_index_1based"],
            "retained_classification": m["retained_classification"],
            "c1_factor_degree_multiset": c1row["factor_degree_multiset"],
            "c1_distinct_factor_count": c1row["factor_count_distinct"],
            "c1_factor_count_with_multiplicity": c1row["factor_count_with_multiplicity"],
            "c1_normalized_full_sign_norm_sha256": c1row["normalized_full_sign_norm_sha256"],
            "strict_height_one_prime_refinement": prime_rows,
            "strict_height_one_prime_count": len(prime_rows),
        })

    novel_rows = []
    for cid in novel:
        m = match_rows[cid]
        carrier_hash = m["projective_linear_form_Qi_sha256"]
        if m["matches_retained_stage33_07_carrier"]:
            raise SystemExit(f"novel row unexpectedly retained: {cid}")
        if carrier_hash in frozen_inventory:
            raise SystemExit(f"novel carrier unexpectedly present in frozen 33-11e inventory: {cid}")
        c1row = c1_rows[cid]
        novel_rows.append({
            "carrier_id": cid,
            "projective_linear_form_Qi_sha256": carrier_hash,
            "c1_factor_degree_multiset": c1row["factor_degree_multiset"],
            "c1_distinct_factor_count": c1row["factor_count_distinct"],
            "c1_normalized_full_sign_norm_sha256": c1row["normalized_full_sign_norm_sha256"],
            "strict_height_one_prime_refinement_status": "NOT_PRESENT_IN_FROZEN_33_11E_30_CARRIER_INVENTORY_REQUIRES_NEW_EXACT_DECOMPOSITION",
        })

    cert = {
        "schema": "stage33.e3.v91c1x_r5b3b3c2a.reused_prime_refinement_partition.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B3B3C2A_REUSE_AUDITED_33_11E_PRIME_REFINEMENTS_AND_ISOLATE_20_NOVEL_CARRIERS",
        "role": "EXACT_NONCREDIT_C2_PREFLIGHT_PARTITION_OF_OFFBOUNDARY_CARRIERS_AGAINST_AUDITED_33_11E_STRICT_HEIGHT_ONE_REFINEMENTS",
        "entry": {"pr": 1695, "authority": AUTHORITY, "stage33_progress": "6/11"},
        "source_locks": {
            "r5b3b3a_sha256": B3B3A_SHA,
            "r5b3b3b_sha256": B3B3B_SHA,
            "r5b3b3c1_sha256": C1_SHA,
            "stage33_11e_source_lock_sha256": E11_SOURCE_SHA,
            "stage33_11e_prime_galois_transport_certificate_sha256": E11_CERT_SHA,
        },
        "exact_partition": {
            "off_boundary_carrier_count": len(off_ids),
            "reused_audited_strict_prime_refinement_carrier_count": len(reused_rows),
            "reused_audited_strict_prime_refinement_carrier_ids": retained_off,
            "reused_distinct_actual_strict_prime_count": len(reused_prime_ids),
            "reused_distinct_actual_strict_prime_ids": sorted(reused_prime_ids),
            "reused_carrier_rows": reused_rows,
            "novel_carrier_count_requiring_new_exact_prime_decomposition": len(novel_rows),
            "novel_carrier_ids_requiring_new_exact_prime_decomposition": novel,
            "novel_carrier_rows": novel_rows,
            "all_23_partitioned_exactly_once": sorted(retained_off + novel) == sorted(off_ids),
            "all_three_reused_carriers_present_in_frozen_33_11e_inventory": True,
            "all_twenty_novel_carriers_absent_from_frozen_33_11e_inventory": True,
        },
        "construction_status": {
            "existing_strict_height_one_prime_refinements_reused_for_three_carriers": True,
            "twenty_novel_carrier_section_prime_decompositions_materialized": False,
            "c1_base_factor_to_strict_prime_adapter_materialized_for_all_21_unique_factors": False,
            "exceptional_prime_attachment_for_all_offboundary_carriers_materialized": False,
            "full_resolved_surface_prime_decomposition_materialized": False,
            "combined_tame_residue_squareclasses_audited": False,
            "offboundary_codimension_one_residue_cancellation_verified": False,
        },
        "exact_consequence": {
            "c2_prime_decomposition_work_reduced_from_23_carrier_sections_to_20_genuinely_new_sections": True,
            "three_reused_carriers_keep_their_audited_33_11e_strict_prime_multisets": True,
            "absence_from_the_frozen_33_11e_inventory_is_not_used_as_a_mathematical_nonexistence_claim": True,
            "strict_prime_reuse_does_not_identify_each_c1_base_norm_factor_with_a_resolved_prime": True,
            "strict_prime_reuse_does_not_supply_exceptional_divisor_multiplicities": True,
            "no_unramifiedness_or_residue_cancellation_follows_from_this_partition": True,
        },
        "next_missing_object": "EXACT_PRIMARY_OR_MINIMAL_PRIME_DECOMPOSITION_OF_Q1_Q2_Q3_Q4_PLUS_EACH_OF_THE_20_NOVEL_LINEAR_CARRIER_EQUATIONS_OVER_QI_THEN_MATCH_EACH_C1_BASE_NORM_FACTOR_TO_THE_RESULTING_STRICT_PRIMES_AND_ATTACH_EXCEPTIONAL_VALUATIONS",
        "next_exact_leaf": "V91C1X_R5B3B3C2B_NOVEL20_STRICT_PRIME_DECOMPOSITION_PREFLIGHT",
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
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUT.write_text(text, encoding="utf-8")
        print(f"wrote {OUT}")
        print(cert["canonical_sha256"])
        return
    if not OUT.exists():
        raise SystemExit(f"certificate missing: {OUT}")
    checked = json.loads(OUT.read_text(encoding="utf-8"))
    if checked != cert:
        raise SystemExit("checked-in C2A certificate differs from exact rebuild")
    print("PASS V91C1X R5B3B3C2A reused-prime refinement partition")
    print(cert["canonical_sha256"])


if __name__ == "__main__":
    main()
