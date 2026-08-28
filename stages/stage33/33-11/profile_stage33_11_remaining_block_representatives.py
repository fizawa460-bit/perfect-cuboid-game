#!/usr/bin/env python3
"""Reduce the 21 remaining Stage33-11 directions to exact symmetry-block reps."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "profile_stage33_11_equivariant_forced_zero_blocks.py"
OUT = HERE / "stage33-11-remaining-block-representatives.json"
WORKING = {2, 3, 24, 25, 26}
QDIM = 26


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


ns = {"__name__": "__main__", "__file__": str(BASE)}
exec(compile(BASE.read_text(encoding="utf-8"), str(BASE), "exec"), ns)
base = ns["cert"]
source_records = ns["source_records"]
cyclic = base["cyclic_source_submodules"]["records"]

# Every named direction belongs to exactly one canonical cyclic source module.
flat = [i for rec in cyclic for i in rec["named_source_directions_1based"]]
if sorted(flat) != list(range(1, QDIM + 1)):
    raise SystemExit("cyclic source-module partition moved")

covered_classes = []
remaining_classes = []
for rec in cyclic:
    members = rec["named_source_directions_1based"]
    member_set = set(members)
    if member_set <= WORKING:
        covered_classes.append(rec)
        continue
    if member_set & WORKING:
        raise SystemExit(f"working directions split a cyclic class: {members}")
    rep = min(members)
    provenance = []
    for idx1 in members:
        src = source_records[idx1 - 1]
        provenance.append({
            "source_direction_1based": idx1,
            "source_basis_name": src["source_basis_name"],
            "parent_order": int(src["parent_order"]),
            "parent_multiplier": int(src["parent_multiplier"]),
            "raw_order2_first_residue_function_liftable": bool(src["raw_order2_first_residue_function_liftable"]),
            "raw_representative_has_order4_crossing_entries": bool(src["raw_representative_has_order4_crossing_entries"]),
            "selected_crossing_count": src.get("selected_crossing_count"),
            "nontrivial_component_function_count": src.get("nontrivial_component_function_count"),
        })
    remaining_classes.append({
        "representative_direction_1based": rep,
        "representative_basis_name": source_records[rep - 1]["source_basis_name"],
        "cyclic_submodule_dimension_f2": rec["dimension_f2"],
        "named_source_directions_1based": members,
        "named_direction_count": len(members),
        "contains_raw_order2_liftable_direction": any(p["raw_order2_first_residue_function_liftable"] for p in provenance),
        "contains_order4_crossing_representative": any(p["raw_representative_has_order4_crossing_entries"] for p in provenance),
        "provenance": provenance,
    })

remaining_classes.sort(key=lambda r: (
    not r["contains_raw_order2_liftable_direction"],
    r["cyclic_submodule_dimension_f2"],
    r["representative_direction_1based"],
))
remaining_directions = sorted(i for rec in remaining_classes for i in rec["named_source_directions_1based"])
if remaining_directions != sorted(set(range(1, QDIM + 1)) - WORKING):
    raise SystemExit("remaining direction coverage mismatch")

cert = {
    "schema": "STAGE33_11_REMAINING_BLOCK_REPRESENTATIVES_V1",
    "stage": "33-11",
    "branch": "33-11c_REMAINING_21_MIXED_ORDER_BLOCK_ORBIT_PRODUCTION",
    "source_locks": {
        "equivariant_forced_zero_block_profile_sha256": base["canonical_sha256"],
    },
    "already_main_working_directions_1based": sorted(WORKING),
    "already_main_working_cyclic_class_count": len(covered_classes),
    "remaining_named_direction_count": len(remaining_directions),
    "remaining_distinct_cyclic_submodule_count": len(remaining_classes),
    "remaining_block_records": remaining_classes,
    "priority_representatives_1based": [r["representative_direction_1based"] for r in remaining_classes],
    "priority_representative_names": [r["representative_basis_name"] for r in remaining_classes],
    "exact_consequence": {
        "remaining_21_directions_reduced_to_block_representatives": True,
        "one_verified_representative_may_determine_each_block_only_after_equivariant_transport_is_materialized": True,
        "connecting_columns_exact_audited": 0,
        "main_working_columns_materialized": 5,
        "stage33_11_closed_exact": False,
        "next_main_task": "MATERIALIZE_FIRST_REMAINING_BLOCK_REPRESENTATIVE_AND_ITS_EQUIVARIANT_TRANSPORT",
    },
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "remaining_named_directions": len(remaining_directions),
    "remaining_cyclic_blocks": len(remaining_classes),
    "priority_representatives": cert["priority_representative_names"],
    "certificate_sha256": cert["canonical_sha256"],
    "next": cert["exact_consequence"]["next_main_task"],
}, indent=2, sort_keys=True))
