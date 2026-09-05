#!/usr/bin/env python3
"""Verify V91C1B A2_02 resolved exceptional valuations and strict-transform carrier preflight."""
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
S11 = HERE.parent / "33-11"
CERT = HERE / "e3-v91c1b-a2-02-resolved-valuation-carrier-preflight.json"
V91C1A = HERE / "e3-v91c1a-a2-02-literal-boundary-seed-localization.json"
PW08 = HERE.parents[2] / "docs" / "arsenal" / "cards" / "provisional" / "S33-PW08.md"

SMALL = S11 / "materialize_stage33_11_smallest_direct_exceptional_valuations.py"
REMAIN = S11 / "materialize_stage33_11_remaining_representative_direct_exceptional_valuations.py"
CARRIERS = S11 / "materialize_stage33_11_all_generator_strict_transform_carriers.py"
SCOUT = S11 / "materialize_stage33_11_carrier_prime_refinement_scout.py"
ORBITS = S11 / "materialize_stage33_11_carrier_geometric_orbit_reduction.py"

GENERATED = [
    S11 / "stage33-11-smallest-direct-exceptional-valuations.json",
    S11 / "stage33-11-remaining-representative-direct-exceptional-valuations.json",
    S11 / "stage33-11-all-generator-strict-transform-carriers.json",
]

CERT_SHA = "4398be760e937e1aba279af5fd099b029dc9998675503b5df7130e714ee81387"
V91C1A_SHA = "7f81ce5da7a4880cf0ffa048ab335fe2db9a643158d26144f45d0de22604b403"
BLOB_LOCKS = {
    PW08: "c9e13a917811581578f833ea93619d85f717be6d",
    SMALL: "14541416d8d5f891d36d677be0872878026b1795",
    REMAIN: "85342c41f79a3b12782c718672a715e506dfd77b",
    CARRIERS: "ad8704b8c5c5c4b248d1fa553a7a44a05b39e21d",
    SCOUT: "eb39cad76e5d98bc698fb52ba4ec96a9f1d86ff2",
    ORBITS: "8ef79bcffed1cc214c617395bd40ad819562b018",
}
SOURCE = "A2_02"
COMPONENTS = [
    "EXC_003", "EXC_004", "EXC_011", "EXC_012",
    "SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008",
]
NEXT = (
    "V91C1C_REFINE_A2_02_STRICT_TRANSFORM_HYPERPLANE_CARRIERS_"
    "TO_ACTUAL_HEIGHT_ONE_PRIMES_AND_VERIFY_CC_CT_TRANSPORT"
)


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob_sha1(raw: bytes):
    return hashlib.sha1(
        b"blob " + str(len(raw)).encode() + b"\0" + raw
    ).hexdigest()


def load_canon(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


cert = load_canon(CERT, CERT_SHA)
v91c1a = load_canon(V91C1A, V91C1A_SHA)

for path, expected in BLOB_LOCKS.items():
    assert git_blob_sha1(path.read_bytes()) == expected, path

assert cert["entry_authority"]["v91c1a_canonical_sha256"] == V91C1A_SHA
assert cert["entry_authority"]["v91c1a_audit_verdict"] == "PASS"
assert cert["a2_02_target"]["source_direction"] == SOURCE
assert cert["a2_02_target"]["component_ids"] == COMPONENTS
assert cert["a2_02_target"]["component_count"] == 8
assert v91c1a["literal_package_record"]["component_ids_in_source_order"] == COMPONENTS
assert v91c1a["selection_semantics"]["selected_direction_is_claimed_e3_coefficient"] is False

preexisting = {p: p.exists() for p in GENERATED}
try:
    ns_small = runpy.run_path(str(SMALL), run_name="__main__")
    ns_remain = runpy.run_path(str(REMAIN), run_name="__main__")
    ns_car = runpy.run_path(str(CARRIERS), run_name="__main__")

    small = ns_small["cert"]
    remain = ns_remain["cert"]
    carriers = ns_car["cert"]

    assert small["exact_local_consequence"]["coverage"] == "5/5"
    assert remain["exact_local_consequence"]["coverage"] == "9/9"
    assert carriers["summary"]["working_generator_coverage"] == "14/14"
    assert carriers["summary"]["distinct_global_normalized_linear_carriers"] == 30
    assert carriers["summary"]["all_14_strict_transform_differences_zero_at_carrier_level"] is True
    assert carriers["summary"]["all_14_exceptional_locus_differences_already_zero_exact"] is True
    assert carriers["summary"]["remaining_purity_problem_is_finite_carrier_prime_refinement"] is True

    smatches = [r for r in small["records"] if r["source_direction"] == SOURCE]
    cmatches = [r for r in carriers["records"] if r["source_direction"] == SOURCE]
    assert len(smatches) == len(cmatches) == 1
    srec = smatches[0]
    crec = cmatches[0]

    assert srec["component_count"] == 8
    assert srec["component_ids"] == COMPONENTS
    assert srec["summary"]["all_48_blowup_centers_evaluated_exact"] is True
    assert srec["summary"]["all_factor_vectors_cc_ct_equivariant"] is True
    assert srec["summary"]["all_component_packages_have_cc_ct_valuation_compatible_targets"] is True
    assert srec["summary"]["exceptional_locus_galois_difference_before_purity_correction"] == "ZERO_EXACT"
    assert srec["factor_exceptional_valuation_vectors"]
    assert all(len(v) == 48 for v in srec["factor_exceptional_valuation_vectors"].values())
    assert set(srec["component_exceptional_valuation_vectors"]) == set(COMPONENTS)

    assert crec["component_count"] == 8
    assert crec["distinct_carrier_count"] > 0
    assert set(crec["component_signed_carrier_vectors"]) == set(COMPONENTS)
    assert crec["exact_consequence"]["ambient_strict_transform_carrier_inventory_closed_under_cc_ct"] is True
    assert crec["exact_consequence"]["all_component_signed_carrier_vectors_cc_ct_transport_exact"] is True
    assert crec["exact_consequence"]["strict_transform_difference_zero_at_carrier_level"] == "ZERO_EXACT_CARRIER_LEVEL"

    pos = cert["exact_positive_reuse"]
    assert pos["all_48_blowup_centers_evaluated_exact_for_a2_02"] is True
    assert pos["a2_02_ambient_factor_exceptional_valuation_vectors_materialized"] is True
    assert pos["a2_02_component_exceptional_valuation_vectors_materialized"] is True
    assert pos["a2_02_factor_exceptional_valuation_vectors_cc_ct_equivariant"] is True
    assert pos["a2_02_component_packages_have_cc_ct_valuation_compatible_targets"] is True
    assert pos["a2_02_exceptional_locus_galois_difference_before_purity_correction"] == "ZERO_EXACT"
    assert pos["a2_02_strict_transform_carrier_inventory_materialized"] is True
    assert pos["a2_02_signed_strict_transform_carrier_vectors_cc_ct_transport_exact"] is True
    assert pos["a2_02_strict_transform_difference_at_carrier_level"] == "ZERO_EXACT_CARRIER_LEVEL"
    assert pos["all_14_generator_carrier_coverage_replayed"] == "14/14"
    assert pos["global_normalized_linear_carrier_count_replayed"] == 30

    debt = cert["narrowed_remaining_debt"]
    assert debt["resolved_exceptional_valuation_attachment_still_missing"] is False
    assert debt["ambient_linear_factor_carrier_enumeration_still_missing"] is False
    assert debt["signed_carrier_multiplicity_still_missing"] is False
    assert debt["cc_ct_carrier_transport_still_missing"] is False
    for key in (
        "strict_transform_carrier_prime_refinement_complete",
        "prime_level_cc_ct_transport_complete",
        "purity_offboundary_correction_materialized",
        "full_surface_cech_transition_glue_materialized",
        "cartier_transition_binding_materialized",
        "exact_marked_brauer_image_equal_mask20_materialized",
        "genuine_full_surface_h2_mu2_lift_for_e3",
    ):
        assert debt[key] is False

    tf = cert["type_firewall"]
    for key in (
        "a2_02_is_claimed_e3_coefficient",
        "a2_02_is_identified_with_proper14_axis",
        "a2_02_is_claimed_to_map_to_mask20",
        "carrier_level_zero_promoted_to_prime_level_zero",
        "old_p_w_14x14_basis_bridge_used",
        "repository_search_miss_used_as_absence_proof",
    ):
        assert tf[key] is False

    assert cert["next_exact_leaf"] == NEXT
    assert cert["credit_firewall"]["stage33_progress"] == "6/11"
    for key in (
        "stage33_12_closed_exact", "stage33_13_released",
        "e3_boundary_function_combination_materialized", "e3_kummer_column_materialized",
        "receiver_credit", "theorem_credit", "endpoint_credit", "merge_allowed",
    ):
        assert cert["credit_firewall"][key] is False

    print(json.dumps({
        "success": True,
        "marker": "V91C1B_A2_02_RESOLVED_EXCEPTIONAL_AND_CARRIER_PREFLIGHT",
        "certificate_sha256": CERT_SHA,
        "a2_02_component_count": 8,
        "a2_02_distinct_strict_transform_carriers": crec["distinct_carrier_count"],
        "all_48_exceptional_centers_exact": True,
        "exceptional_locus_difference": "ZERO_EXACT",
        "strict_transform_carrier_difference": "ZERO_EXACT_CARRIER_LEVEL",
        "global_carrier_count": 30,
        "remaining_blocker": debt["remaining_blocker_code"],
        "stage33_progress": "6/11",
        "next_exact_leaf": NEXT,
    }, sort_keys=True))
finally:
    for path, existed in preexisting.items():
        if not existed and path.exists():
            path.unlink()
