#!/usr/bin/env python3
"""Verify V91B retained literal boundary-function asset and exact adapter gap."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91b-boundary-function-adapter-gap.json"
V45 = HERE / "e3-proper14-boundary-basis-definitions-v45.json"
V88 = HERE / "e3-direct-cech-seed-contract-v88.json"
V89 = HERE / "e3-proper14-dual-to-discriminant-quotient-bridge-v89.json"
V91 = HERE / "e3-retained-at-marked-picard-dual-source-v91.json"
V91A = HERE / "e3-v91a-literal-integral-divisor-type-obstruction.json"
BF = HERE / "boundary-function-generator-source-lock.json"
SCALAR = HERE / "boundary-function-scalar-descent-certificate.json"

LOCKS = {
    CERT: "7d0669f8c8ec6e590838095640b69cc0e9c8f76088a0c89f74cc8f49235d7443",
    V45: "a1dafa0be79c80d7275cd2629278bf6a56d6e592f90738316e71ca2689f9feb5",
    V88: "1d8f7b9478f48a3aa2137524180afea0a8e0bbf909e4ece04b1a07ee44d365b7",
    V89: "26bf699fd92e261e1ae40066ad0fd5aece9cb896f28a385367786de1d0460639",
    V91: "729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9",
    V91A: "1da7e6c26939a80ec5dec24c19cd04615084982d4fc4f29086273796cef102d9",
    BF: "aaacc000f2e5fbbe733789f5f2a19d6c2cb14b5d3a26d0b8e508eea1f3bc8c96",
    SCALAR: "e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b",
}
ORDER = ["A2_02","A2_03","A2_24","A2_25","A2_26","A2_04","A2_01","A2_07","A2_05","A2_10","A2_08","A2_09","A2_16","A2_15"]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == LOCKS[path] == csha(body), path
    return obj


cert = load_locked(CERT)
v45 = load_locked(V45)
v88 = load_locked(V88)
v89 = load_locked(V89)
v91 = load_locked(V91)
v91a = load_locked(V91A)
bf = load_locked(BF)
scalar = load_locked(SCALAR)

assert cert["schema"] == "stage33.e3.v91b.boundary_function_adapter_gap.v1"
assert cert["status"] == "PASS_EXACT_V91B_LITERAL_BOUNDARY_FUNCTION_ASSET_LIVE_PROPER14_ADAPTER_STILL_MISSING"
assert cert["entry_authority"] == {
    "audited_head": "175c40def5815f8e8cd35d1e60c8d5fc5715bbac",
    "exact_head_ci_job": 101288960143,
    "exact_head_ci_run": 33959570974,
    "merged_main": "9309801b9caffa857adc5599ad5dd686d84d47d8",
    "review_id": 5120803368,
    "v91a_hostile_audit_pass": True,
}
assert v91a["exact_consequence"]["e3_discriminant_class_itself_cannot_be_integral_picard_divisor"] is True
assert v89["e3_transport"]["proper14_mask_decimal"] == 20
assert v89["e3_transport"]["proper14_support_one_based"] == [3, 5]
assert v91["e3_source_binding"]["retained_at_mod2_quotient_support_one_based"] == [1, 8, 10]
assert v88["v88_construction_contract"]["smallest_missing_seed"].startswith("one source-specific literal geometric seed")

bfb = v45["boundary_function_basis"]
assert bfb["dimension_f2"] == 14
assert bfb["ordered_source_directions"] == ORDER
ni = v45["non_identification_lock"]
assert ni["proper14_order_identified_with_boundary_order"] is False
assert ni["positional_identification_allowed"] is False
assert ni["proper14_to_boundary_change_of_basis_materialized"] is False
assert v45["e3_context"]["boundary_source_coordinate_materialized"] is False

assert len(bf["generator_records"]) == 14
assert [x["source_direction"] for x in bf["generator_records"]] == ORDER
assert scalar["working_generator_count"] == 14
assert scalar["working_generator_ids"] == ORDER
assert scalar["boundary_function_package_count"] == 134
ex = scalar["exact_conclusion"]
assert ex["all_14_generator_boundary_function_packages_recovered_with_occurrence_scalars"] is True
assert ex["all_package_divisor_vectors_match_audited_stage33_11e"] is True
assert ex["cc_ct_function_level_scalar_ratios_finitely_materialized"] is True
assert ex["all_cc_ct_function_level_scalar_ratios_equal_one"] is True
assert scalar["distinct_scalar_ratios_Qi"] == [[1,1,0,1]]

p = cert["positive_retained_asset"]
assert p["ordered_source_directions"] == ORDER
assert p["package_count"] == 134
assert p["literal_boundary_function_packages_materialized"] is True
assert p["all_package_divisor_vectors_match_audited_stage33_11e"] is True

a = cert["adapter_audit"]
assert a["proper14_basis_dimension_f2"] == 14 == a["boundary_function_basis_dimension_f2"]
assert a["dimension_match_used_as_identification"] is False
assert a["positional_identification_allowed"] is False
assert a["proper14_to_boundary_change_of_basis_materialized_in_v45"] is False
assert a["v89_v91_source_bind_target_to_marked_picard_discriminant"] is True
assert a["boundary_function_basis_to_v91_marked_discriminant_proper14_adapter_materialized"] is False
assert a["bounded_repository_absence_claim"] is False
assert a["mathematical_nonexistence_claim"] is False

cons = cert["exact_consequence"]
assert cons["literal_boundary_function_route_is_now_source_localized"] is True
for key in ("e3_boundary_function_combination_materialized", "e3_literal_kummer_function_materialized", "e3_literal_cech_seed_materialized", "complete_residue_audit_materialized", "genuine_full_surface_h2_mu2_lift_for_e3"):
    assert cons[key] is False
assert cert["next_exact_leaf"] == "V91C_CONSTRUCT_EXACT_BOUNDARY_FUNCTION_A2_TO_V91_MARKED_DISCRIMINANT_PROPER14_ADAPTER"
assert cert["credit_firewall"]["stage33_progress"] == "6/11"
for key in ("stage33_12_closed_exact", "stage33_13_released", "receiver_credit", "theorem_credit", "endpoint_credit", "merge_allowed"):
    assert cert["credit_firewall"][key] is False

print(json.dumps({
    "success": True,
    "marker": "V91B_E3_LITERAL_BOUNDARY_FUNCTION_ASSET_ADAPTER_GAP_COMPLETE",
    "certificate_sha256": LOCKS[CERT],
    "working_generator_count": 14,
    "package_count": 134,
    "proper14_mask": 20,
    "adapter_materialized": False,
    "next_exact_leaf": cert["next_exact_leaf"],
}, sort_keys=True))
