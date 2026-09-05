#!/usr/bin/env python3
"""Verify V91C type-safe cohomological adapter interface."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c-type-safe-cech-adapter-interface.json"
V50 = HERE / "e3-a1-1-type-correction-v50.json"
V51 = HERE / "e3-v25-method-rewire-v51.json"
V52 = HERE / "e3-mask20-literal-cech-preimage-gap-v52.json"
V88 = HERE / "e3-direct-cech-seed-contract-v88.json"
V91 = HERE / "e3-retained-at-marked-picard-dual-source-v91.json"
V91B = HERE / "e3-v91b-boundary-function-adapter-gap.json"
BF = HERE / "boundary-function-generator-source-lock.json"
SCALAR = HERE / "boundary-function-scalar-descent-certificate.json"

CANON_LOCKS = {
    CERT: "da156e8fcbd59743073b5a3d8ba5359c533b0b045adddc41877310974cdc1754",
    V88: "1d8f7b9478f48a3aa2137524180afea0a8e0bbf909e4ece04b1a07ee44d365b7",
    V91: "729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9",
    V91B: "7d0669f8c8ec6e590838095640b69cc0e9c8f76088a0c89f74cc8f49235d7443",
    BF: "aaacc000f2e5fbbe733789f5f2a19d6c2cb14b5d3a26d0b8e508eea1f3bc8c96",
    SCALAR: "e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b",
}
BLOB_LOCKS = {
    V50: "1aa59da6303b6f8b0286c9c32fdc72960bc0dc85",
    V51: "32ab508f836f8d3a40570d686232bf67aeaa6152",
    V52: "15ae7ebf8ddaf9d8771d48bc93caa0705e4ebf67",
}
ORDER = ["A2_02","A2_03","A2_24","A2_25","A2_26","A2_04","A2_01","A2_07","A2_05","A2_10","A2_08","A2_09","A2_16","A2_15"]
NEXT = "V91C1_ASSEMBLE_ONE_SOURCE_BOUND_FULL_SURFACE_CECH_TRANSITION_CARTIER_REPRESENTATIVE_FROM_RETAINED_BOUNDARY_FUNCTION_PACKAGES_AND_COMPUTE_MARKED_BRAUER_IMAGE_MASK20"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(raw: bytes):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_canon(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == CANON_LOCKS[path] == csha(body), path
    return obj


def load_blob(path):
    raw = path.read_bytes()
    assert git_blob_sha1(raw) == BLOB_LOCKS[path], path
    return json.loads(raw)


cert = load_canon(CERT)
v50 = load_blob(V50)
v51 = load_blob(V51)
v52 = load_blob(V52)
v88 = load_canon(V88)
v91 = load_canon(V91)
v91b = load_canon(V91B)
bf = load_canon(BF)
scalar = load_canon(SCALAR)

assert cert["schema"] == "stage33.e3.v91c.type_safe_cech_adapter_interface.v1"
assert cert["status"] == "PASS_EXACT_V91C_TYPE_SAFE_COHOMOLOGICAL_ADAPTER_INTERFACE_FIXED_FULL_SURFACE_CECH_GLUE_STILL_MISSING"
entry = cert["entry_authority"]
assert entry["pr"] == 1604
assert entry["merged"] is True
assert entry["merge_commit"] == "29ce620a693f7cbdec48bce9b720cc02dfe5fa74"
assert entry["hostile_audit_review"] == 5120883188
assert entry["hostile_audit_verdict"] == "FAIL_FRESHNESS_ONLY"
assert entry["mathematics_and_route_selection_passed_in_review"] is True
assert entry["audit_pass_credit"] is False

assert v50["retired_assumption"]["status"] == "RETIRED_WRONG_OBJECT_TYPE"
assert v50["retired_assumption"]["v47_14_column_construction_contract_superseded"] is True
assert v50["exact_type_statement"]["direct_boundary_source_to_K_linear_map_is_stage_A"] is False
assert v50["exact_type_statement"]["working_14_boundary_directions_are_proved_basis_of_K"] is False
assert v51["exact_rewire"]["retired_route_remains_forbidden"] is True
assert v51["arsenal_routing"]["pw05_direct_14d_bridge_route"] is False
assert v52["bounded_inspection"]["available_marked_picard_data"]["literal_function_divisor_transition_preimage_for_mask20_materialized"] is False
assert v88["v88_construction_contract"]["smallest_missing_seed"].startswith("one source-specific literal geometric seed")
assert v91["e3_source_binding"]["source_bound_to_actual_140_class_marking"] is True
assert v91b["positive_retained_asset"]["ordered_source_directions"] == ORDER

fire = cert["type_firewall"]
assert fire["retired_object_remains_forbidden"] is True
assert fire["direct_boundary_source_to_K_basis_identification_allowed"] is False
assert fire["zero_absolute_connecting_value_means_K_coordinate_zero"] is False
assert fire["positional_or_dimension_identification_allowed"] is False
assert "not a 14x14 basis change" in fire["v91c_name_interpretation"]

positive = cert["positive_retained_asset"]
assert positive["ordered_source_directions"] == ORDER
assert positive["working_generator_count"] == 14
assert positive["boundary_function_package_count"] == 134
assert positive["literal_boundary_function_packages_materialized"] is True
assert positive["all_package_divisor_vectors_match_audited_stage33_11e"] is True
assert positive["all_cc_ct_function_level_scalar_ratios_equal_one"] is True
assert len(bf["generator_records"]) == 14
assert [r["source_direction"] for r in bf["generator_records"]] == ORDER
assert scalar["working_generator_count"] == 14
assert scalar["boundary_function_package_count"] == 134
assert scalar["exact_conclusion"]["all_cc_ct_function_level_scalar_ratios_equal_one"] is True

# Bounded artifact-interface check only: these two retained assets do not themselves
# claim full-surface Cech transition or Cartier glue. This is not repository absence.
bf_raw = BF.read_text(encoding="utf-8").lower()
assert "transition" not in bf_raw
assert "cartier" not in bf_raw
ai = cert["artifact_interface_audit"]
assert ai["full_surface_cech_transition_glue_materialized_in_locked_boundary_function_asset"] is False
assert ai["cartier_transition_binding_materialized_in_locked_boundary_function_asset"] is False
assert ai["exact_marked_brauer_image_computation_equal_mask20_materialized"] is False
assert ai["repo_absence_claim"] is False
assert ai["mathematical_nonexistence_claim"] is False

adapter = cert["adapter_definition"]
assert adapter["proper14_mask_decimal"] == 20
assert adapter["proper14_support_one_based"] == [3, 5]
assert adapter["retained_at_mod2_quotient_support_one_based"] == [1, 8, 10]
assert adapter["materialized"] is False
assert cert["exact_consequence"]["old_p_w_14x14_route_reopened"] is False
assert cert["exact_consequence"]["v91c_type_safe_adapter_semantics_fixed"] is True
assert cert["exact_consequence"]["genuine_full_surface_h2_mu2_lift_for_e3"] is False
assert cert["next_exact_leaf"] == NEXT
assert cert["credit_firewall"]["stage33_progress"] == "6/11"
for key in ("stage33_12_closed_exact", "stage33_13_released", "e3_kummer_column_materialized", "receiver_credit", "theorem_credit", "endpoint_credit", "merge_allowed"):
    assert cert["credit_firewall"][key] is False

print(json.dumps({
    "success": True,
    "marker": "V91C_TYPE_SAFE_CECH_ADAPTER_INTERFACE_COMPLETE",
    "certificate_sha256": CANON_LOCKS[CERT],
    "working_generator_count": 14,
    "package_count": 134,
    "proper14_mask": 20,
    "old_p_w_reopened": False,
    "adapter_materialized": False,
    "next_exact_leaf": NEXT,
}, sort_keys=True))
