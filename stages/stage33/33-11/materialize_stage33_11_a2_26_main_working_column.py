#!/usr/bin/env python3
"""Materialize the Stage33-11 MAIN working A2_26 connecting column.

The visible boundary package and the direct exceptional-divisor valuations are
machine-exact.  MAIN is allowed to pin the still-open strict-transform /
off-boundary purity correction to a Q-defined/V4-fixed representative.  Under
that explicitly unaudited convention the five cc/ct decoder bits are zero.

This remains a working certificate only: it never promotes the exact 0/26
counter, Stage33-11 closure, Stage33-12, theorem, or endpoint credit.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DECODER = HERE / "stage33-11-a2-26-restriction-decoder.json"
AMBIENT = HERE / "stage33-11-a2-26-ambient-boundary-galois.json"
PREIMAGE = HERE / "stage33-11-a2-26-explicit-gersten-difference-preimage.json"
EXCVAL = HERE / "stage33-11-a2-26-direct-exceptional-valuations.json"
OUT = HERE / "stage33-11-a2-26-main-working-column.json"
EXPECTED_AMBIENT_SHA = "e3d779e68d878234d5574ce71cee33ca83f6918f808a7e35c460dd5e56021a35"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_checked(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if csha(body) != claimed:
        raise SystemExit(f"canonical hash mismatch for {path.name}")
    return obj


decoder = load_checked(DECODER)
ambient = load_checked(AMBIENT)
preimage = load_checked(PREIMAGE)
excval = load_checked(EXCVAL)

if decoder.get("schema") != "STAGE33_11_A2_26_CC_CT_RESTRICTION_DECODER_V1":
    raise SystemExit("A2_26 decoder schema moved")
if not decoder.get("decoder", {}).get("all_32_coefficient_vectors_roundtrip_verified"):
    raise SystemExit("A2_26 decoder is not exhaustive")
if decoder.get("decoder", {}).get("joint_restriction_rank_on_allowed_space_f2") != 5:
    raise SystemExit("A2_26 decoder lost rank five")
if ambient.get("canonical_sha256") != EXPECTED_AMBIENT_SHA:
    raise SystemExit("A2_26 ambient boundary certificate moved")
if not ambient.get("exact_checks", {}).get("explicit_ambient_boundary_package_v4_fixed"):
    raise SystemExit("visible A2_26 boundary package is not V4-fixed")
if preimage.get("source_direction") != "A2_26":
    raise SystemExit("A2_26 explicit-preimage source moved")
if preimage.get("repair_frontier", {}).get("ambient_function_package_difference_before_purity_correction_is_zero") is not True:
    raise SystemExit("ambient function package difference is not exact zero")
if excval.get("schema") != "STAGE33_11_A2_26_DIRECT_EXCEPTIONAL_VALUATIONS_V1":
    raise SystemExit("direct exceptional valuation schema moved")
if excval.get("source_locks", {}).get("explicit_gersten_preimage_sha256") != preimage["canonical_sha256"]:
    raise SystemExit("direct exceptional valuations no longer lock the explicit preimage")
if not excval.get("summary", {}).get("all_factor_vectors_cc_ct_equivariant"):
    raise SystemExit("factor-level exceptional valuation equivariance failed")
if not excval.get("summary", {}).get("all_component_vectors_cc_ct_equivariant"):
    raise SystemExit("component-level exceptional valuation equivariance failed")
if excval.get("summary", {}).get("exceptional_locus_galois_difference_before_purity_correction") != "ZERO_EXACT":
    raise SystemExit("exceptional-locus Galois difference moved")

observed_bits = excval["main_working_bridge"]["five_bit_vector_under_q_defined_v4_fixed_purity_pin"]
if observed_bits != [0, 0, 0, 0, 0]:
    raise SystemExit("MAIN working five-bit pin moved away from zero")

inv = decoder["decoder"]["observation_to_allowed_basis_matrix_f2_5x5"]
allowed_coeffs = [
    sum((observed_bits[k] & 1) * (int(inv[k][j]) & 1) for k in range(5)) & 1
    for j in range(5)
]
if allowed_coeffs != [0, 0, 0, 0, 0]:
    raise SystemExit("zero observation did not decode to zero finite-H1 class")

cert = {
    "schema": "STAGE33_11_A2_26_MAIN_WORKING_COLUMN_V2",
    "stage": "33-11",
    "branch": "33-11c_A2_26_MAIN_WORKING_EXPLICIT_PREIMAGE",
    "source_direction": {
        "name": "A2_26",
        "source_index_1based": 26,
    },
    "exact_inputs": {
        "visible_boundary_package_v4_fixed": True,
        "ambient_boundary_certificate_sha256": ambient["canonical_sha256"],
        "explicit_ambient_function_preimage_certificate_sha256": preimage["canonical_sha256"],
        "direct_exceptional_valuation_certificate_sha256": excval["canonical_sha256"],
        "exceptional_locus_galois_difference_before_purity_correction": "ZERO_EXACT",
        "restriction_decoder_sha256": decoder["canonical_sha256"],
        "finite_H1_allowed_dimension_f2": 5,
        "joint_cc_ct_decoder_injective": True,
    },
    "main_working_convention": {
        "id": "PIN_REMAINING_STRICT_TRANSFORM_PURITY_CORRECTION_Q_DEFINED_V4_FIXED_PENDING_AUDIT",
        "exactly_computed_before_pin": [
            "visible four-component ambient boundary package",
            "ambient rational-function Galois factor multisets",
            "all ambient-factor exceptional valuations at 48 blow-up centers",
            "cc/ct exceptional-valuation equivariance",
        ],
        "remaining_assumption": "strict-transform/off-boundary purity correction may be chosen Q-defined/V4-fixed",
        "cc_ct_observation_bits_f2": observed_bits,
        "five_bit_certificate_materialized": True,
        "decoded_allowed_basis_coefficients_f2": allowed_coeffs,
        "finite_v4_H1_class": "ZERO",
        "explicit_gersten_difference_preimage_working_value": "ZERO",
        "absolute_connecting_class_working_value": "ZERO",
    },
    "progress": {
        "main_working_column_materialized": True,
        "main_working_columns_materialized": 1,
        "exact_audited_column_materialized": False,
        "exact_audited_columns_materialized": 0,
        "stage33_11_exact_exit_progress": "0/26",
        "main_development_progress": "1/26",
        "next_main_direction": "A2_25",
    },
    "audit_debt": {
        "required": True,
        "narrowed_by_this_leaf": True,
        "resolved_locally": "exceptional-divisor valuations at all 48 blow-up centers",
        "still_required": "strict-transform/off-boundary height-one decomposition plus proof that the purity correction admits the pinned Q-defined/V4-fixed representative",
        "failure_action": "invalidate this working column and recompute A2_26 before Stage33-11 exact closure",
    },
    "firewalls": {
        "stage33_11_closed_exact": False,
        "stage33_12_released": False,
        "stage33_08_released": False,
        "stage33_07_closed": False,
        "theorem_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "source": "A2_26",
    "exceptional_valuations": "MATERIALIZED_EXACT",
    "five_bit_certificate": observed_bits,
    "main_working_value": "ZERO",
    "main_development_progress": "1/26",
    "exact_audited_progress": "0/26",
    "audit_debt": True,
    "next": "A2_25",
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
