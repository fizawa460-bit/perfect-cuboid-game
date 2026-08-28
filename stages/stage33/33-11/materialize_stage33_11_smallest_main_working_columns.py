#!/usr/bin/env python3
"""Materialize the five raw-order2 smallest directions as MAIN working columns.

These directions were isolated exactly by Stage33-11c as independently
raw-order2 liftable.  MAIN pins a Q-defined global Gersten representative for
each direction so development can continue into the remaining mixed-order
block.  The pin is an explicit audit debt: none of these five columns counts
for the exact Stage33-11 exit until hostile audit verifies the global lift.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROFILE_SCRIPT = HERE / "profile_stage33_11_smallest_block_target_images.py"
A26_WORKING = HERE / "stage33-11-a2-26-main-working-column.json"
OUT = HERE / "stage33-11-smallest-main-working-columns.json"
EXPECTED_PROFILE = "45e42d6f3577654df7a4126cad5e2eee651c38fdce3c5cf8289b5f96707f2edc"
SMALLEST = [2, 3, 24, 25, 26]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


ns = {"__name__": "__main__", "__file__": str(PROFILE_SCRIPT)}
exec(compile(PROFILE_SCRIPT.read_text(encoding="utf-8"), str(PROFILE_SCRIPT), "exec"), ns)
profile = ns["cert"]
source_records = ns["source_records"]
if profile.get("canonical_sha256") != EXPECTED_PROFILE:
    raise SystemExit("smallest-block target profile moved")
if [r["source_direction_1based"] for r in profile["smallest_direction_records"]] != SMALLEST:
    raise SystemExit("smallest direction ordering moved")

# A2_26 has the stronger explicit visible-boundary certificate and its own
# working-column materialization.  Require agreement with the block package.
a26 = json.loads(A26_WORKING.read_text(encoding="utf-8"))
if a26.get("schema") != "STAGE33_11_A2_26_MAIN_WORKING_COLUMN_V1":
    raise SystemExit("A2_26 working-column schema moved")
if a26.get("main_working_convention", {}).get("absolute_connecting_class_working_value") != "ZERO":
    raise SystemExit("A2_26 working value moved")

records = []
for idx1 in SMALLEST:
    src = source_records[idx1 - 1]
    prof = next(r for r in profile["smallest_direction_records"] if r["source_direction_1based"] == idx1)
    expected_name = f"A2_{idx1:02d}"
    if src.get("source_basis_name") != expected_name or prof.get("source_basis_name") != expected_name:
        raise SystemExit(f"source ordering moved at {idx1}")
    if not src.get("raw_order2_first_residue_function_liftable"):
        raise SystemExit(f"{expected_name} is no longer raw-order2 liftable")
    records.append({
        "source_direction_1based": idx1,
        "source_basis_name": expected_name,
        "exact_raw_order2_first_residue_function_liftable": True,
        "exact_K_naturality_allowed_dimension_f2": prof["K_factor_allowed_value_subspace_dimension_f2"],
        "exact_finite_H1_naturality_allowed_dimension_f2": prof["finite_H1_factor_allowed_value_subspace_dimension_f2"],
        "exact_joint_cc_ct_restriction_rank_f2": prof["finite_H1_allowed_values_joint_restriction_rank_f2"],
        "exact_joint_cc_ct_restriction_kernel_dimension_f2": prof["finite_H1_allowed_values_joint_restriction_kernel_dimension_f2"],
        "main_working_global_lift_convention": "PIN_Q_DEFINED_GLOBAL_GERSTEN_REPRESENTATIVE_PENDING_AUDIT",
        "main_working_absolute_connecting_class": "ZERO",
        "main_working_column_materialized": True,
        "exact_audited_column_materialized": False,
        "audit_required": True,
    })

cert = {
    "schema": "STAGE33_11_SMALLEST_MAIN_WORKING_COLUMNS_V1",
    "stage": "33-11",
    "branch": "33-11c_SMALLEST_RAW_ORDER2_MAIN_WORKING_COLUMNS",
    "source_locks": {
        "smallest_block_target_profile_sha256": EXPECTED_PROFILE,
        "a2_26_main_working_column_sha256": a26["canonical_sha256"],
    },
    "working_columns": records,
    "progress": {
        "main_working_columns_materialized": 5,
        "main_working_progress": "5/26",
        "exact_audited_columns_materialized": 0,
        "exact_exit_progress": "0/26",
        "remaining_main_directions": 21,
        "next_main_task": "REMAINING_21_MIXED_ORDER_BLOCK_ORBIT_PRODUCTION",
    },
    "audit_debt": {
        "required": True,
        "directions": [f"A2_{i:02d}" for i in SMALLEST],
        "question": "verify the pinned Q-defined global Gersten representative for each raw-order2 smallest direction and recompute any nonzero absolute class",
        "failure_action": "replace only failing working columns before exact Stage33-11 closure",
    },
    "firewalls": {
        "stage33_11_closed_exact": False,
        "stage33_12_released": False,
        "stage33_08_released": False,
        "theorem_credit": False,
        "endpoint_credit": False,
    },
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "main_working_progress": "5/26",
    "exact_exit_progress": "0/26",
    "directions": [r["source_basis_name"] for r in records],
    "next": cert["progress"]["next_main_task"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
