#!/usr/bin/env python3
"""Verify Stage33 ordinary startup is synchronized to the exact V91 frontier."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
ROOT = STAGE.parent.parent
STATE = STAGE / "MAIN-STATE.json"
START = STAGE / "MAIN-START-HERE.md"
RULES = STAGE / "RULES.md"
V91 = HERE / "e3-retained-at-marked-picard-dual-source-v91.json"

V91_SHA = "729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9"
NEXT = "V91A_LIFT_MARKED_PICARD_DUAL_CLASS_SUPPORT_1_8_10_TO_LITERAL_DIVISOR_OR_DIRECT_CECH_KUMMER_DATUM"
TARGET_NUM = [2,3,0,7,0,0,6,4,4,2,2,2,6,0,2,7,1,5,7,0,0,4,4,4,4,0,4,4,5,6,0,2,0,0,5,0,6,2,6,0,0,0,0,0,0,2,0,0,2,0,6,4,0,0,3,5,0,6,2,6,2,0,0,0]
EXPECTED_WORKING_SET = [
    "docs/research-os/policies/repository-asset-discovery.md",
    "docs/arsenal/index.json",
    "docs/arsenal/cards/provisional/S33-PW04.md",
    "docs/arsenal/cards/provisional/S33-PW07.md",
    "stages/stage33/33-12/e3-retained-at-marked-picard-dual-source-v91.json",
    "stages/stage33/33-12/e3-proper14-dual-to-discriminant-quotient-bridge-v89.json",
    "stages/stage33/33-12/e3-direct-cech-seed-contract-v88.json",
    "stages/stage33/33-12/e3-proper14-boundary-basis-definitions-v45.json",
    "stages/stage33/33-09/marked-picard-basis-source.json",
    "stages/stage33/33-09/marked-picard-basis-bridge-certified.json",
    "stages/stage33/33-07/picard-discriminant-compact.json",
]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


state = json.loads(STATE.read_text(encoding="utf-8"))
sb = dict(state)
claimed_state = sb.pop("canonical_sha256")
assert claimed_state == csha(sb)

v91 = json.loads(V91.read_text(encoding="utf-8"))
vb = dict(v91)
claimed_v91 = vb.pop("canonical_sha256")
assert claimed_v91 == V91_SHA == csha(vb)

controller = json.loads((STAGE / "controller.json").read_text(encoding="utf-8"))
cb = dict(controller)
controller_sha = cb.pop("projection_canonical_sha256")
assert controller_sha == csha(cb)
assert state["controller_projection_canonical_sha256"] == controller_sha

assert state["schema"] == "STAGE33_MAIN_COMPACT_STATE_V29_V91_MARKED_PICARD_DUAL_SOURCE_BINDING_ACTIVE"
assert state["authority_sync"]["frontier_authority"] == "V91_MARKED_PICARD_DUAL_SOURCE_BINDING"
assert state["branch_exact_frontier_authority"].endswith("e3-retained-at-marked-picard-dual-source-v91.json")
assert state["current"]["next_exact_leaf"] == NEXT
assert state["current"]["active_missing_interface"] == "LIFT_MARKED_PICARD_DUAL_CLASS_SUPPORT_1_8_10_TO_LITERAL_DIVISOR_OR_DIRECT_CECH_KUMMER_DATUM"

f = state["current_exact_frontier"]
assert f["e3_proper14_mask_decimal"] == 20
assert f["e3_proper14_support_one_based"] == [3, 5]
assert f["e3_proper14_is_dual_not_at2_element"] is True
assert f["e3_dual_pairing_bridge_rank_f2"] == 14
assert f["e3_retained_at_mod2_quotient_support_one_based"] == [1, 8, 10]
assert f["e3_retained_at_mod2_solution_unique"] is True
assert f["e3_marked_picard_dual_source_bound"] is True
assert f["e3_marked_picard_dual_roundtrip_exact"] is True
assert f["e3_marked_picard_dual_numerator_mod8_64"] == TARGET_NUM
assert f["e3_literal_picard_divisor_materialized"] is False
assert f["e3_literal_kummer_function_materialized"] is False
assert f["e3_literal_cech_seed_materialized"] is False
assert f["e3_complete_residue_audit_materialized"] is False
assert f["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
assert f["e3_global_H2_mu2_nonexistence_claim"] is False

bind = v91["e3_source_binding"]
assert bind["retained_at_mod2_quotient_support_one_based"] == f["e3_retained_at_mod2_quotient_support_one_based"]
assert bind["marked_indlist_picard_dual_numerator_mod8_64"] == f["e3_marked_picard_dual_numerator_mod8_64"]
assert bind["mixed_coordinate_roundtrip_exact"] == f["e3_marked_picard_dual_roundtrip_exact"]
assert bind["source_bound_to_actual_140_class_marking"] == f["e3_marked_picard_dual_source_bound"]
assert v91["next_exact_leaf"] == state["current"]["next_exact_leaf"]

assert state["current_leaf_working_set"] == EXPECTED_WORKING_SET
for rel in EXPECTED_WORKING_SET:
    assert (ROOT / rel).is_file(), rel

assert state["stage33_progress"] == "6/11"
for key in (
    "stage33_12_closed_exact",
    "stage33_13_released",
    "receiver_credit",
    "theorem_credit",
    "endpoint_credit",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
    "merge_allowed",
):
    assert state["firewalls"][key] is False

assert state["anti_loop_policy"]["do_not_treat_marked_picard_dual_class_as_integral_picard_divisor"] is True
assert state["resolved_investigations"]["e3_marked_picard_dual_source_binding"].startswith("CLOSED_EXACT_V91")
assert "LITERAL_DIVISOR_OR_CECH_KUMMER_STILL_OPEN" in state["resolved_investigations"]["e3_literal_source_binding"]

startup = START.read_text(encoding="utf-8")
assert "MAIN-STATE.json` is the single mutable ordinary-startup authority" in startup
assert "current_leaf_working_set" in startup
assert "Current exact frontier:" not in startup
assert "V85" not in startup
assert "V89" not in startup
assert "V91" not in startup
assert "Repository traversal itself follows `AGENTS.md`" in startup
assert "repeatable bounded search" in startup
assert "materially new mathematical signal" in startup

rules = RULES.read_text(encoding="utf-8")
assert "Frontier-promotion synchronization" in rules
assert "same change" in rules
assert "`MAIN-START-HERE.md` must not contain mutable frontier/version/leaf/progress" in rules

print(json.dumps({
    "success": True,
    "marker": "V92_STAGE33_V91_CURRENT_STARTUP_ALIGNMENT_COMPLETE",
    "state_canonical_sha256": claimed_state,
    "v91_canonical_sha256": V91_SHA,
    "frontier": state["authority_sync"]["frontier_authority"],
    "next_exact_leaf": NEXT,
    "working_set_size": len(EXPECTED_WORKING_SET),
    "stage33_progress": state["stage33_progress"],
    "merge_allowed": False,
}, sort_keys=True))
