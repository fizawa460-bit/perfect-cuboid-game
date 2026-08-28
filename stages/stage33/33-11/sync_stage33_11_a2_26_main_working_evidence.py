#!/usr/bin/env python3
"""Overlay the new A2_26 MAIN-working local valuation evidence into controller.

This script is deliberately non-promoting: exact progress stays 0/26 and all
downstream/theorem/endpoint firewalls stay closed.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = ROOT / "stages" / "stage33" / "33-11"
CTRL = ROOT / "stages" / "stage33" / "controller.json"
EXCVAL = HERE / "stage33-11-a2-26-direct-exceptional-valuations.json"
WORK = HERE / "stage33-11-a2-26-main-working-column.json"

v = json.loads(EXCVAL.read_text(encoding="utf-8"))
w = json.loads(WORK.read_text(encoding="utf-8"))
if v.get("schema") != "STAGE33_11_A2_26_DIRECT_EXCEPTIONAL_VALUATIONS_V1":
    raise SystemExit("A2_26 exceptional valuation schema moved")
if w.get("schema") != "STAGE33_11_A2_26_MAIN_WORKING_COLUMN_V2":
    raise SystemExit("A2_26 MAIN working schema moved")
if w.get("progress", {}).get("stage33_11_exact_exit_progress") != "0/26":
    raise SystemExit("overlay refuses exact progress promotion")
if not w.get("audit_debt", {}).get("required"):
    raise SystemExit("overlay requires explicit audit debt")

c = json.loads(CTRL.read_text(encoding="utf-8"))
children = {x["id"]: x for x in c["repair_children"]}
s11 = children["33-11"]
s12 = children["33-12"]

slot = s11.setdefault("stage33_11c_a2_26_reduction", {})
slot["main_working_local_valuation_status"] = "EXCEPTIONAL_LOCUS_EXACT_STRICT_TRANSFORM_PURITY_AUDIT_DEBT"
slot["direct_exceptional_valuation_certificate_sha256"] = v["canonical_sha256"]
slot["all_48_blowup_centers_evaluated_exact"] = True
slot["exceptional_locus_galois_difference_before_purity_correction"] = "ZERO_EXACT"
slot["main_working_five_bit_certificate"] = w["main_working_convention"]["cc_ct_observation_bits_f2"]
slot["main_working_explicit_gersten_difference_preimage"] = w["main_working_convention"]["explicit_gersten_difference_preimage_working_value"]
slot["main_working_connecting_value"] = w["main_working_convention"]["absolute_connecting_class_working_value"]
slot["main_working_certificate_sha256"] = w["canonical_sha256"]
slot["audit_debt_required"] = True
slot["audit_debt_remaining"] = w["audit_debt"]["still_required"]
slot["connecting_column_materialized_exact"] = False
slot["next_exact_task"] = "A2_26_AUDIT_STRICT_TRANSFORM_PURITY_CORRECTION_ONLY"

s11["connecting_columns_exact_audited"] = 0
s11["exact_exit_progress"] = "0/26"
s11["audit_required"] = True
s11["stage33_11c_main_working_a2_26"] = {
    "five_bit_certificate": w["main_working_convention"]["cc_ct_observation_bits_f2"],
    "working_value": "ZERO",
    "certificate_sha256": w["canonical_sha256"],
    "direct_exceptional_valuation_sha256": v["canonical_sha256"],
    "audit_debt": w["audit_debt"]["still_required"],
}
for b in s11.get("branches", []):
    if b.get("id") == "33-11c":
        b["main_status"] = "A2_26_MAIN_WORKING_EXPLICIT_PREIMAGE_EXCEPTIONAL_VALUATIONS_DONE_AUDIT_DEBT_REMAINS"
        b["preferred_next_pointer"] = "continue-main-with-audit-debt-no-33-12-release"

s12["status"] = "BLOCKED_PENDING_33_11_COMPLETE_EXACT_COVERAGE"
s12["prerequisites_satisfied"] = False

checkpoint = c.setdefault("controller_writeback_checkpoint", {})
checkpoint["stage33_11c_a2_26_direct_exceptional_valuation_sha256"] = v["canonical_sha256"]
checkpoint["stage33_11c_a2_26_main_working_certificate_sha256"] = w["canonical_sha256"]
checkpoint["stage33_11c_a2_26_main_working_five_bits"] = w["main_working_convention"]["cc_ct_observation_bits_f2"]
checkpoint["stage33_11c_a2_26_exceptional_locus_difference"] = "ZERO_EXACT"
checkpoint["stage33_11c_a2_26_strict_transform_purity_audit_debt"] = True
checkpoint["stage33_11_exact_exit_progress"] = "0/26"
checkpoint["stage33_12_released"] = False
checkpoint["stage33_08_released"] = False
checkpoint["theorem_credit"] = False
checkpoint["endpoint_credit"] = False

c["merge_allowed"] = False
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
c["current_item"] = "Stage33-11_ARITHMETIC_LOCALIZATION_CONNECTING_MAP_MAIN_WORKING_A2_26_LOCAL_VALUATIONS_DONE"
c["next_item"] = "Stage33-11_MAIN_CONTINUE_WITH_AUDIT_DEBT"
c["next_expected_command"] = "Stage33-main-batch"

CTRL.write_text(json.dumps(c, indent=2, sort_keys=False) + "\n", encoding="utf-8")
print("STAGE33_11_A2_26_DIRECT_EXCEPTIONAL_VALUATIONS=PASS")
print("STAGE33_11_A2_26_MAIN_WORKING_FIVE_BITS=[0,0,0,0,0]")
print("STAGE33_11_EXACT_PROGRESS=0/26")
print("STAGE33_12_RELEASED=false")
