#!/usr/bin/env python3
"""Materialize the Stage33-11 MAIN working A2_26 connecting column.

MAIN-batch is allowed to advance past the off-boundary purity-correction audit
question.  The exact visible boundary package is already certified V4-fixed.
For production progress we therefore pin the remaining purity correction to a
Q-defined/V4-fixed representative and record the resulting zero absolute
connecting class as a *working* column.

This file is intentionally explicit about the debt: it is not an exact closure
certificate, does not count toward the hostile-audited 26/26 exit condition,
and cannot release Stage33-12.  It only lets MAIN continue to the next named
source direction while audit independently checks the pinned representative.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DECODER = HERE / "stage33-11-a2-26-restriction-decoder.json"
AMBIENT = HERE / "stage33-11-a2-26-ambient-boundary-galois.json"
OUT = HERE / "stage33-11-a2-26-main-working-column.json"
EXPECTED_AMBIENT_SHA = "e3d779e68d878234d5574ce71cee33ca83f6918f808a7e35c460dd5e56021a35"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


decoder = json.loads(DECODER.read_text(encoding="utf-8"))
ambient = json.loads(AMBIENT.read_text(encoding="utf-8"))
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

# MAIN working convention.  Audit owns the proof obligation that such a pinned
# off-boundary purity correction is legitimate in the global Gersten lift.
observed_bits = [0, 0, 0, 0, 0]
inv = decoder["decoder"]["observation_to_allowed_basis_matrix_f2_5x5"]
allowed_coeffs = [
    sum((observed_bits[k] & 1) * (int(inv[k][j]) & 1) for k in range(5)) & 1
    for j in range(5)
]
if allowed_coeffs != [0, 0, 0, 0, 0]:
    raise SystemExit("zero observation did not decode to zero finite-H1 class")

cert = {
    "schema": "STAGE33_11_A2_26_MAIN_WORKING_COLUMN_V1",
    "stage": "33-11",
    "branch": "33-11c_A2_26_MAIN_WORKING_COLUMN",
    "source_direction": {
        "name": "A2_26",
        "source_index_1based": 26,
    },
    "exact_inputs": {
        "visible_boundary_package_v4_fixed": True,
        "ambient_boundary_certificate_sha256": ambient["canonical_sha256"],
        "restriction_decoder_sha256": decoder["canonical_sha256"],
        "finite_H1_allowed_dimension_f2": 5,
        "joint_cc_ct_decoder_injective": True,
    },
    "main_working_convention": {
        "id": "PIN_OFFBOUNDARY_PURITY_CORRECTION_Q_DEFINED_V4_FIXED_PENDING_AUDIT",
        "offboundary_purity_correction_assumed_q_defined": True,
        "offboundary_purity_correction_assumed_v4_fixed": True,
        "cc_ct_observation_bits_f2": observed_bits,
        "decoded_allowed_basis_coefficients_f2": allowed_coeffs,
        "finite_v4_H1_class": "ZERO",
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
        "question": "verify that the pinned off-boundary purity correction can be chosen Q-defined/V4-fixed and that the resulting absolute connecting class is zero",
        "failure_action": "invalidate this working column and recompute A2_26 before Stage33-11 exact closure",
    },
    "firewalls": {
        "stage33_11_closed_exact": False,
        "stage33_12_released": False,
        "stage33_08_released": False,
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
    "main_working_value": "ZERO",
    "main_development_progress": "1/26",
    "exact_audited_progress": "0/26",
    "audit_debt": True,
    "next": "A2_25",
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
