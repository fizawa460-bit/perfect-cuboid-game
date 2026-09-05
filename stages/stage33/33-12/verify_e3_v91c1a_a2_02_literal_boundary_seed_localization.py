#!/usr/bin/env python3
"""Verify V91C1A exact A2_02 literal boundary-function package localization."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1a-a2-02-literal-boundary-seed-localization.json"
V91 = HERE / "e3-retained-at-marked-picard-dual-source-v91.json"
V91C = HERE / "e3-v91c-type-safe-cech-adapter-interface.json"
BF = HERE / "boundary-function-generator-source-lock.json"
SCALAR = HERE / "boundary-function-scalar-descent-certificate.json"

CANON_LOCKS = {
    CERT: "7f81ce5da7a4880cf0ffa048ab335fe2db9a643158d26144f45d0de22604b403",
    V91: "729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9",
    V91C: "da156e8fcbd59743073b5a3d8ba5359c533b0b045adddc41877310974cdc1754",
    BF: "aaacc000f2e5fbbe733789f5f2a19d6c2cb14b5d3a26d0b8e508eea1f3bc8c96",
    SCALAR: "e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b",
}
SOURCE = "A2_02"
COMPONENTS = [
    "EXC_003", "EXC_004", "EXC_011", "EXC_012",
    "SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008",
]
EXCEPTIONALS = COMPONENTS[:4]
SIDES = COMPONENTS[4:]
NEXT = (
    "V91C1B_ATTACH_A2_02_LITERAL_BOUNDARY_FUNCTION_PACKAGES_TO_RESOLVED_FULL_SURFACE_"
    "HEIGHT_ONE_AND_RESOLUTION_EXCEPTIONAL_VALUATIONS_WITH_CECH_CARTIER_TRANSITION_DATA"
)


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_canon(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == CANON_LOCKS[path] == csha(body), path
    return obj


cert = load_canon(CERT)
v91 = load_canon(V91)
v91c = load_canon(V91C)
bf = load_canon(BF)
scalar = load_canon(SCALAR)

assert cert["schema"] == "stage33.e3.v91c1a.a2_02_literal_boundary_seed_localization.v1"
assert cert["status"] == (
    "PASS_EXACT_V91C1A_A2_02_LITERAL_BOUNDARY_PACKAGE_LOCALIZED_"
    "FULL_SURFACE_CECH_CARTIER_BINDING_STILL_MISSING"
)
assert cert["entry_authority"]["v91c_status"] == v91c["status"]
assert cert["source_locks"]["v91_canonical_sha256"] == CANON_LOCKS[V91]
assert cert["source_locks"]["v91c_canonical_sha256"] == CANON_LOCKS[V91C]
assert cert["source_locks"]["boundary_function_generator_source_lock_sha256"] == CANON_LOCKS[BF]
assert cert["source_locks"]["boundary_function_scalar_descent_sha256"] == CANON_LOCKS[SCALAR]

# The selected record is only a deterministic first retained literal package.
# It is not an e3 coefficient, a proper14 coordinate, or the retired P_W bridge.
sel = cert["selection_semantics"]
assert sel["selected_source_direction"] == SOURCE
assert sel["selected_direction_is_claimed_e3_coefficient"] is False
assert sel["selected_direction_is_identified_with_proper14_axis"] is False
assert sel["single_direction_is_claimed_to_map_to_mask20"] is False
assert sel["old_p_w_14x14_basis_bridge_used"] is False
assert v91c["type_firewall"]["retired_object_remains_forbidden"] is True
assert v91c["type_firewall"]["direct_boundary_source_to_K_basis_identification_allowed"] is False

# Recompute the exact A2_02 package localization from the locked parent asset.
matches = [r for r in bf["generator_records"] if r["source_direction"] == SOURCE]
assert len(matches) == 1
record = matches[0]
assert int(record["raw_order"]) == 2
packages = record["component_packages"]
assert len(packages) == 8
assert [p["component_id"] for p in packages] == COMPONENTS
assert [p["kind"] for p in packages[:4]] == ["EXCEPTIONAL"] * 4
assert [p["kind"] for p in packages[4:]] == ["SIDE"] * 4
assert {int(p["denominator"]["exponent"]) for p in packages} == {2}
assert all("coefficients_Qi" in p["denominator"] for p in packages)
assert all(len(p["numerator_factors"]) == 2 for p in packages)
assert {
    int(f.get("exponent", 1))
    for p in packages
    for f in p["numerator_factors"]
} == {1}
assert all("coefficients_Qi" in f for p in packages for f in p["numerator_factors"])

lit = cert["literal_package_record"]
assert lit["source_direction"] == SOURCE
assert lit["raw_order"] == 2
assert lit["component_count"] == 8
assert lit["component_ids_in_source_order"] == COMPONENTS
assert lit["exceptional_component_ids"] == EXCEPTIONALS
assert lit["side_component_ids"] == SIDES
assert lit["all_component_package_denominator_exponents"] == [2]
assert lit["all_component_package_numerator_factor_exponents"] == [1]
assert lit["all_component_packages_have_literal_denominator_and_numerator_factor_data"] is True
assert lit["record_is_source_bound_by_parent_canonical_lock"] is True

# Independently bind the function-level scalar descent record for the same source.
smatches = [r for r in scalar["generator_records"] if r["source_direction"] == SOURCE]
assert len(smatches) == 1
srec = smatches[0]
assert srec == {
    "action_scalar_record_count": 16,
    "action_scalar_records_sha256": "96ffaf2a0918193f8bd2fbb422a20a26557aa1747b57f8704b47d49251bd1c46",
    "all_candidate_scalar_ratios_one": True,
    "candidate_target_count": 24,
    "component_count": 8,
    "raw_order": 2,
    "source_direction": SOURCE,
}
s = cert["scalar_descent_record"]
for key in (
    "source_direction", "raw_order", "component_count", "action_scalar_record_count",
    "candidate_target_count", "action_scalar_records_sha256",
    "all_candidate_scalar_ratios_one",
):
    assert s[key] == srec[key]
assert s["all_package_divisor_vectors_match_audited_stage33_11e"] is True
assert scalar["exact_conclusion"]["all_package_divisor_vectors_match_audited_stage33_11e"] is True
assert scalar["exact_conclusion"]["all_cc_ct_function_level_scalar_ratios_equal_one"] is True

# Preserve the V91/V91C target types exactly; no positional identification is allowed.
target = cert["target_firewall"]
assert target["proper14_mask_decimal"] == 20
assert target["proper14_support_one_based"] == [3, 5]
assert target["retained_at_mod2_quotient_support_one_based"] == [1, 8, 10]
assert v91["e3_source_binding"]["retained_at_mod2_quotient_support_one_based"] == [1, 8, 10]
assert target["a2_02_position_used_as_proper14_coordinate"] is False
assert target["a2_02_literal_record_alone_determines_e3_brauer_class"] is False
for key in (
    "full_surface_cech_transition_glue_materialized",
    "cartier_transition_binding_materialized",
    "codimension_one_and_resolution_exceptional_residue_audit_complete",
    "exact_marked_brauer_image_equal_mask20_materialized",
    "genuine_full_surface_h2_mu2_lift_for_e3",
):
    assert target[key] is False

exact = cert["exact_consequence"]
assert exact["one_retained_literal_boundary_function_record_localized_exactly"] is True
assert exact["one_record_can_be_recomputed_from_locked_parent_assets_without_duplicate_literal_truth"] is True
for key in (
    "v91c1_full_representative_assembly_complete",
    "e3_boundary_function_combination_materialized",
    "full_surface_cech_cartier_adapter_materialized",
    "marked_brauer_image_mask20_materialized",
):
    assert exact[key] is False

assert cert["next_exact_leaf"] == NEXT
assert cert["credit_firewall"]["stage33_progress"] == "6/11"
for key in (
    "stage33_12_closed_exact", "stage33_13_released", "e3_kummer_column_materialized",
    "receiver_credit", "theorem_credit", "endpoint_credit", "merge_allowed",
):
    assert cert["credit_firewall"][key] is False

print(json.dumps({
    "success": True,
    "marker": "V91C1A_A2_02_LITERAL_BOUNDARY_PACKAGE_LOCALIZED",
    "certificate_sha256": CANON_LOCKS[CERT],
    "source_direction": SOURCE,
    "raw_order": 2,
    "component_count": 8,
    "component_ids": COMPONENTS,
    "scalar_action_record_count": 16,
    "all_scalar_ratios_one": True,
    "e3_coefficient_selected": False,
    "full_surface_cech_cartier_materialized": False,
    "proper14_mask": 20,
    "stage33_progress": "6/11",
    "next_exact_leaf": NEXT,
}, sort_keys=True))
