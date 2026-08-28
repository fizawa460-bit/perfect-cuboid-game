#!/usr/bin/env python3
"""Materialize a complete 26/26 Stage33-11 MAIN working connecting map.

The five smallest raw-order2 directions are already pinned as working zero
columns.  For each remaining exact cyclic H-submodule, MAIN pins one named
representative to a Q-defined global Gersten lift with working absolute value
zero.  Exact H-equivariance then forces the entire cyclic submodule generated
by that representative to have working value zero.

The only non-exact input is the pinned global Gersten representative for each
block.  It is recorded as hostile-audit debt.  Hence this file gives complete
MAIN development coverage but never promotes the Stage33-11 exact exit.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SMALL = HERE / "stage33-11-smallest-main-working-columns.json"
BLOCKS = HERE / "stage33-11-remaining-block-representatives.json"
OUT = HERE / "stage33-11-all-blocks-main-working.json"
QDIM = 26


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


small = json.loads(SMALL.read_text(encoding="utf-8"))
blocks = json.loads(BLOCKS.read_text(encoding="utf-8"))
if small.get("schema") != "STAGE33_11_SMALLEST_MAIN_WORKING_COLUMNS_V1":
    raise SystemExit("smallest working package schema moved")
if blocks.get("schema") != "STAGE33_11_REMAINING_BLOCK_REPRESENTATIVES_V1":
    raise SystemExit("remaining block profile schema moved")
if small.get("progress", {}).get("main_working_progress") != "5/26":
    raise SystemExit("smallest working progress moved")
if blocks.get("remaining_named_direction_count") != 21:
    raise SystemExit("remaining named direction count moved")

small_records = small["working_columns"]
small_dirs = {int(r["source_direction_1based"]) for r in small_records}
if small_dirs != {2, 3, 24, 25, 26}:
    raise SystemExit("small working direction set moved")

remaining_records = blocks["remaining_block_records"]
remaining_dirs = {
    int(i)
    for block in remaining_records
    for i in block["named_source_directions_1based"]
}
if small_dirs & remaining_dirs:
    raise SystemExit("small and remaining working coverage overlap")
if small_dirs | remaining_dirs != set(range(1, QDIM + 1)):
    raise SystemExit("MAIN working block coverage is not 26/26")

block_working = []
for block in remaining_records:
    rep = int(block["representative_direction_1based"])
    members = [int(i) for i in block["named_source_directions_1based"]]
    if rep not in members:
        raise SystemExit("block representative is not a member")
    if not members:
        raise SystemExit("empty remaining cyclic block")
    block_working.append({
        "representative_direction_1based": rep,
        "representative_basis_name": block["representative_basis_name"],
        "cyclic_submodule_dimension_f2": int(block["cyclic_submodule_dimension_f2"]),
        "named_source_directions_1based": members,
        "named_direction_count": len(members),
        "main_working_representative_convention": "PIN_Q_DEFINED_GLOBAL_GERSTEN_REPRESENTATIVE_PENDING_AUDIT",
        "main_working_representative_absolute_value": "ZERO",
        "exact_transport_used": "H_EQUIVARIANT_LINEARITY_ON_EXACT_CYCLIC_SOURCE_SUBMODULE",
        "working_zero_propagates_to_entire_cyclic_submodule": True,
        "working_zero_propagates_to_all_named_members": True,
        "audit_required_for_representative_pin": True,
    })

# Zero at the generator of a cyclic H-submodule implies zero on every H-image
# and every F2-linear combination, so one working assumption per remaining
# block is sufficient for complete MAIN coverage.
audit_reps = [r["representative_basis_name"] for r in block_working]
all_named = sorted(small_dirs | remaining_dirs)
if all_named != list(range(1, QDIM + 1)):
    raise SystemExit("final named working coverage regression")

cert = {
    "schema": "STAGE33_11_ALL_BLOCKS_MAIN_WORKING_V1",
    "stage": "33-11",
    "branch": "33-11c_COMPLETE_MAIN_WORKING_BLOCK_COVERAGE",
    "source_locks": {
        "smallest_main_working_columns_sha256": small["canonical_sha256"],
        "remaining_block_representatives_sha256": blocks["canonical_sha256"],
    },
    "smallest_working_directions_1based": sorted(small_dirs),
    "remaining_block_working_records": block_working,
    "working_map": {
        "coefficient_field": "F2",
        "absolute_connecting_map_working_value": "ZERO_MAP",
        "named_source_directions_covered": all_named,
        "named_source_direction_count": len(all_named),
        "main_working_coverage": "26/26",
        "remaining_unmaterialized_main_directions": 0,
    },
    "audit_debt": {
        "required": True,
        "smallest_direction_debt": small["audit_debt"]["directions"],
        "remaining_block_representative_debt": audit_reps,
        "remaining_block_representative_count": len(audit_reps),
        "question": "hostile-audit each pinned Q-defined global Gersten representative; exact H-equivariance propagation is retained once a representative is certified",
        "failure_action": "replace only the failing representative block and its propagated working columns before exact Stage33-11 closure",
    },
    "progress": {
        "main_working_columns_materialized": 26,
        "main_working_progress": "26/26",
        "main_working_map_complete": True,
        "exact_audited_columns_materialized": 0,
        "exact_exit_progress": "0/26",
        "stage33_11_closed_exact": False,
        "next_main_task": "AUDIT_OR_REPLACE_PINNED_BLOCK_REPRESENTATIVES_BEFORE_EXACT_PROMOTION",
    },
    "firewalls": {
        "arithmetic_localization_connecting_map_computed_exact": False,
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
    "main_working_progress": "26/26",
    "exact_exit_progress": "0/26",
    "remaining_block_representative_debt": audit_reps,
    "remaining_block_representative_count": len(audit_reps),
    "certificate_sha256": cert["canonical_sha256"],
    "next": cert["progress"]["next_main_task"],
}, indent=2, sort_keys=True))
