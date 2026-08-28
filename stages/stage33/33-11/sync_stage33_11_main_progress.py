#!/usr/bin/env python3
"""Overlay complete Stage33-11 MAIN working progress after exact checkpoint sync.

This overlay is intentionally not an exact/audited promotion.  It consumes the
complete MAIN working certificate, records every pinned assumption as audit
debt, and keeps Stage33-12 plus all theorem/endpoint release firewalls closed.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CTRL = ROOT / "stages" / "stage33" / "controller.json"
HERE = ROOT / "stages" / "stage33" / "33-11"
A26 = HERE / "stage33-11-a2-26-main-working-column.json"
SMALL = HERE / "stage33-11-smallest-main-working-columns.json"
BLOCKS = HERE / "stage33-11-remaining-block-representatives.json"
ALL = HERE / "stage33-11-all-blocks-main-working.json"
QDIM = 26

w = json.loads(A26.read_text(encoding="utf-8"))
s = json.loads(SMALL.read_text(encoding="utf-8"))
r = json.loads(BLOCKS.read_text(encoding="utf-8"))
a = json.loads(ALL.read_text(encoding="utf-8"))
if w.get("schema") != "STAGE33_11_A2_26_MAIN_WORKING_COLUMN_V1":
    raise SystemExit("A2_26 MAIN working certificate schema moved")
if s.get("schema") != "STAGE33_11_SMALLEST_MAIN_WORKING_COLUMNS_V1":
    raise SystemExit("smallest MAIN working package schema moved")
if r.get("schema") != "STAGE33_11_REMAINING_BLOCK_REPRESENTATIVES_V1":
    raise SystemExit("remaining block representative schema moved")
if a.get("schema") != "STAGE33_11_ALL_BLOCKS_MAIN_WORKING_V1":
    raise SystemExit("complete MAIN working package schema moved")
if s.get("progress", {}).get("main_working_progress") != "5/26":
    raise SystemExit("smallest MAIN working progress moved")
if s.get("progress", {}).get("exact_exit_progress") != "0/26":
    raise SystemExit("smallest MAIN package cannot promote exact closure")
if r.get("remaining_named_direction_count") != 21:
    raise SystemExit("remaining named direction count moved")
if not s.get("audit_debt", {}).get("required"):
    raise SystemExit("smallest MAIN working package must retain audit debt")

progress = a.get("progress", {})
working_map = a.get("working_map", {})
audit_debt = a.get("audit_debt", {})
firewalls = a.get("firewalls", {})
if progress.get("main_working_progress") != "26/26":
    raise SystemExit("complete MAIN working progress is not 26/26")
if progress.get("main_working_columns_materialized") != QDIM:
    raise SystemExit("complete MAIN working column count is not 26")
if not progress.get("main_working_map_complete"):
    raise SystemExit("complete MAIN working map flag is false")
if progress.get("exact_exit_progress") != "0/26" or progress.get("exact_audited_columns_materialized") != 0:
    raise SystemExit("MAIN overlay refuses any unaudited exact promotion")
if progress.get("stage33_11_closed_exact"):
    raise SystemExit("MAIN overlay refuses exact Stage33-11 closure")
if working_map.get("main_working_coverage") != "26/26":
    raise SystemExit("working map coverage is not 26/26")
if working_map.get("named_source_direction_count") != QDIM:
    raise SystemExit("working map named direction count is not 26")
if working_map.get("named_source_directions_covered") != list(range(1, QDIM + 1)):
    raise SystemExit("working map does not cover exactly A2_01..A2_26")
if working_map.get("remaining_unmaterialized_main_directions") != 0:
    raise SystemExit("working map still has unmaterialized MAIN directions")
if working_map.get("absolute_connecting_map_working_value") != "ZERO_MAP":
    raise SystemExit("complete MAIN working convention moved away from ZERO_MAP")
if not audit_debt.get("required"):
    raise SystemExit("complete MAIN working package lost audit debt")
if audit_debt.get("smallest_direction_debt") != s["audit_debt"]["directions"]:
    raise SystemExit("smallest-direction audit debt was not preserved")
if audit_debt.get("remaining_block_representative_count") != r["remaining_distinct_cyclic_submodule_count"]:
    raise SystemExit("remaining block audit-debt count moved")
if audit_debt.get("remaining_block_representative_debt") != r["priority_representative_names"]:
    raise SystemExit("remaining block audit-debt representatives moved")
for key in (
    "arithmetic_localization_connecting_map_computed_exact",
    "stage33_12_released",
    "stage33_08_released",
    "theorem_credit",
    "endpoint_credit",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    if firewalls.get(key):
        raise SystemExit(f"MAIN working package illegally opened firewall: {key}")

small_debt = audit_debt["smallest_direction_debt"]
block_debt = audit_debt["remaining_block_representative_debt"]
c = json.loads(CTRL.read_text(encoding="utf-8"))
children = {x["id"]: x for x in c["repair_children"]}
s11 = children["33-11"]
s12 = children["33-12"]

s11["status"] = "MAIN_IMPLEMENTATION_COMPLETE_26_OF_26_AUDIT_PENDING"
s11["connecting_columns_explicitly_materialized"] = QDIM
s11["connecting_columns_main_working"] = QDIM
s11["connecting_columns_exact_audited"] = 0
s11["main_working_progress"] = "26/26"
s11["exact_exit_progress"] = "0/26"
s11["main_working_map_complete"] = True
s11["audit_required"] = True
s11["audit_passed"] = False
s11["audit_debt_columns"] = small_debt
s11["audit_debt"] = {
    "required": True,
    "smallest_direction_working_zero_pins_1based": small_debt,
    "remaining_cyclic_block_representative_working_zero_pins": block_debt,
    "remaining_cyclic_block_representative_count": len(block_debt),
    "question": audit_debt["question"],
    "failure_action": audit_debt["failure_action"],
}
s11["smallest_main_working_columns"] = {
    "certificate_sha256": s["canonical_sha256"],
    "directions": small_debt,
    "working_absolute_value": "ZERO",
    "audit_required": True,
    "audit_question": s["audit_debt"]["question"],
}
s11["a2_26_main_working_column"] = {
    "certificate_sha256": w["canonical_sha256"],
    "working_absolute_value": w["main_working_convention"]["absolute_connecting_class_working_value"],
    "stronger_visible_boundary_certificate_available": True,
}
s11["remaining_block_reduction"] = {
    "certificate_sha256": r["canonical_sha256"],
    "remaining_named_directions": r["remaining_named_direction_count"],
    "remaining_cyclic_blocks": r["remaining_distinct_cyclic_submodule_count"],
    "priority_representatives_1based": r["priority_representatives_1based"],
    "priority_representative_names": r["priority_representative_names"],
}
s11["complete_main_working_map"] = {
    "certificate_sha256": a["canonical_sha256"],
    "coverage": "26/26",
    "named_source_directions_covered": working_map["named_source_directions_covered"],
    "working_absolute_value": "ZERO_MAP",
    "exact_audited_columns": 0,
    "audit_required": True,
}
for b in s11.get("branches", []):
    if b.get("id") == "33-11c":
        b["main_status"] = "MAIN_IMPLEMENTATION_COMPLETE_26_OF_26_AUDIT_PENDING"
        b["preferred_next_pointer"] = "hostile-audit-pinned-working-assumptions"

s12["status"] = "BLOCKED_PENDING_33_11_COMPLETE_EXACT_COVERAGE"
s12["prerequisites_satisfied"] = False
s12["blocked_by"] = "33-11_EXACT_OPEN_0_OF_26_MAIN_WORKING_26_OF_26_AUDIT_PENDING"

c["current_item"] = "Stage33-11_ARITHMETIC_LOCALIZATION_CONNECTING_MAP_MAIN_IMPLEMENTATION_COMPLETE_AUDIT_PENDING"
c["audit_required"] = True
c["merge_allowed"] = False
c["advance_allowed"] = False
c["advance_scope"] = "NONE_UNTIL_STAGE33_11_WORKING_ASSUMPTIONS_AUDITED_OR_REPLACED"
c["next_item"] = "Stage33-11_HOSTILE_AUDIT_PINNED_WORKING_ASSUMPTIONS"
c["next_expected_command"] = "Stage33-audit"
checkpoint = c.setdefault("controller_writeback_checkpoint", {})
checkpoint["stage33_11_status"] = "MAIN_IMPLEMENTATION_COMPLETE_AUDIT_PENDING"
checkpoint["stage33_11_main_working_progress"] = "26/26"
checkpoint["stage33_11_exact_exit_progress"] = "0/26"
checkpoint["stage33_11_main_working_map_complete"] = True
checkpoint["stage33_11_audit_debt_columns"] = small_debt
checkpoint["stage33_11_audit_debt_block_representatives"] = block_debt
checkpoint["stage33_11_smallest_main_working_columns_sha256"] = s["canonical_sha256"]
checkpoint["stage33_11_remaining_block_representatives_sha256"] = r["canonical_sha256"]
checkpoint["stage33_11_all_blocks_main_working_sha256"] = a["canonical_sha256"]
checkpoint["stage33_11_remaining_cyclic_blocks"] = r["remaining_distinct_cyclic_submodule_count"]
checkpoint["stage33_11_next_branch"] = "AUDIT_PENDING_NO_33_12_RELEASE"
checkpoint["stage33_08_released"] = False
checkpoint["theorem_credit"] = False
checkpoint["endpoint_credit"] = False

# MAIN implementation completion must not mutate exact/downstream firewalls.
c["stage33_08_released"] = False
c["stage33_08_release_allowed"] = False
c["stage33_40_released"] = False
c["stage33_40_release_allowed"] = False
c["theorem_credit"] = False
c["endpoint_credit"] = False
c["stage33_closed"] = False
c["brauer_manin_set_empty_proved"] = False
c["perfect_cuboid_existence_claim"] = False
c["perfect_cuboid_nonexistence_claim"] = False

CTRL.write_text(json.dumps(c, indent=2, sort_keys=False) + "\n", encoding="utf-8")
print("STAGE33_11_MAIN_PROGRESS=26/26")
print("STAGE33_11_EXACT_PROGRESS=0/26")
print("STAGE33_11_MAIN_IMPLEMENTATION=COMPLETE_AUDIT_PENDING")
print("AUDIT_DEBT_SMALLEST_DIRECTIONS=" + json.dumps(small_debt))
print("AUDIT_DEBT_BLOCK_REPRESENTATIVES=" + json.dumps(block_debt))
print("STAGE33_12_RELEASED=false")
