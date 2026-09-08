#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import materialize_e3_v91c1x_r5b3b3a_match_27_carriers_to_retained_33 as mat

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1x-r5b3b3a-match-27-carriers-to-retained-33.json"
CERT_SHA = "36bd375d08b4ebd852bb101851b108fae7e76780f2a35b6ea033948f9ddb8e77"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
NEXT = "V91C1X_R5B3B3B_CLASSIFY_NOVEL_CARRIERS_BY_FULL_SIGN_NORM_AND_UNIFY_ALL_27"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main():
    stored = json.loads(CERT.read_text(encoding="utf-8"))
    body = dict(stored)
    claimed = body.pop("canonical_sha256", None)
    if claimed != CERT_SHA or csha(body) != CERT_SHA:
        raise SystemExit("R5B3B3A canonical sha invalid")
    rebuilt = mat.build_certificate()
    if rebuilt != stored:
        raise SystemExit("R5B3B3A exact replay differs from stored certificate")
    if stored["candidate"] != "V91C1X_R5B3B3A_MATCH_27_SYMBOL_CARRIERS_TO_RETAINED_STAGE33_07_33_CARRIERS":
        raise SystemExit("R5B3B3A candidate moved")
    if stored["entry"]["authority"] != AUTHORITY or stored["entry"]["stage33_progress"] != "6/11":
        raise SystemExit("authority or Stage33 progress moved")

    retained = stored["retained_stage33_07_33"]
    if (retained["distinct_projective_carrier_count"], retained["boundary_only_hyperplane_count"], retained["off_boundary_candidate_hyperplane_count"]) != (33, 18, 15):
        raise SystemExit("retained Stage33-07 33-carrier split moved")
    if retained["source_certificate_is_the_formal_stage33_07_33_carrier_inventory_not_a_naive_reconstruction_from_boundary_function_packages"] is not True:
        raise SystemExit("retained source-semantics firewall lost")

    part = stored["match_partition"]
    expected = {
        "current_carrier_count": 27,
        "matched_retained_33_count": 7,
        "novel_relative_to_retained_33_count": 20,
        "pi_D_matched_count": 0,
        "pi_D_novel_count": 20,
        "f_D_matched_count": 7,
        "f_D_novel_count": 0,
        "matched_boundary_only_count": 4,
        "matched_off_boundary_count": 3,
    }
    for key, value in expected.items():
        if part[key] != value:
            raise SystemExit(f"R5B3B3A partition count moved: {key}")
    if len(part["carrier_rows"]) != 27 or len(part["matched_carrier_ids"]) != 7 or len(part["novel_carrier_ids"]) != 20:
        raise SystemExit("R5B3B3A carrier row partition moved")
    for row in part["carrier_rows"]:
        if row["appears_in_f_D"] == row["appears_in_pi_D"]:
            raise SystemExit(f"carrier member partition lost: {row['carrier_id']}")
        if row["appears_in_f_D"] and not row["matches_retained_stage33_07_carrier"]:
            raise SystemExit(f"f_D carrier unexpectedly novel: {row['carrier_id']}")
        if row["appears_in_pi_D"] and row["matches_retained_stage33_07_carrier"]:
            raise SystemExit(f"pi_D carrier unexpectedly retained: {row['carrier_id']}")

    status = stored["construction_status"]
    for key in [
        "retained_stage33_07_33_carrier_inventory_exactly_source_locked",
        "r5b3b2_27_carriers_partitioned_by_exact_projective_match",
        "retained_stage33_07_norm_split_reused_for_matched_carriers",
    ]:
        if status[key] is not True:
            raise SystemExit(f"R5B3B3A construction progress lost: {key}")
    for key in [
        "novel_carrier_full_sign_norms_factorized",
        "all_27_carriers_classified_boundary_vs_offboundary",
        "all_27_carriers_prime_decomposed_on_resolved_surface",
        "combined_tame_residue_squareclasses_audited",
        "offboundary_codimension_one_residue_cancellation_verified",
        "single_global_a2_02_kummer_or_brauer_representative_materialized",
    ]:
        if status[key] is not False:
            raise SystemExit(f"R5B3B3A construction firewall violated: {key}")
    if stored["next_exact_leaf"] != NEXT:
        raise SystemExit("R5B3B3A routing moved")
    for key, value in stored["credit_firewall"].items():
        if value is not False:
            raise SystemExit(f"R5B3B3A credit firewall violated: {key}")

    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B3B3A_27_TO_RETAINED_33_MATCH_VERIFIED",
        "certificate_sha256": claimed,
        "matched_retained_33_count": 7,
        "novel_relative_to_retained_33_count": 20,
        "pi_D_novel_count": 20,
        "f_D_matched_count": 7,
        "next_exact_leaf": NEXT,
        "stage33_progress": "6/11",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
