#!/usr/bin/env python3
"""Verify Stage33 ordinary startup is synchronized to the exact V89 frontier."""
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
V89 = HERE / "e3-proper14-dual-to-discriminant-quotient-bridge-v89.json"

V89_SHA = "26bf699fd92e261e1ae40066ad0fd5aece9cb896f28a385367786de1d0460639"
NEXT = "V89A_SOURCE_BIND_RETAINED_AT_MOD2_SUPPORT_1_8_10_TO_LITERAL_PICARD_DIVISOR_OR_DIRECT_CECH_KUMMER_DATUM"
EXPECTED_WORKING_SET = [
    "docs/research-os/policies/repository-asset-discovery.md",
    "docs/arsenal/index.json",
    "docs/arsenal/cards/provisional/S33-PW04.md",
    "docs/arsenal/cards/provisional/S33-PW07.md",
    "stages/stage33/33-12/e3-proper14-dual-to-discriminant-quotient-bridge-v89.json",
    "stages/stage33/33-12/e3-direct-cech-seed-contract-v88.json",
    "stages/stage33/33-12/e3-independent-proper14-source-v41.json",
    "stages/stage33/33-12/e3-proper14-boundary-basis-definitions-v45.json",
    "stages/stage33/33-07/picard-discriminant-compact.json",
    "stages/stage33/33-07/proper-brauer2-from-discriminant.json",
    "stages/stage33/33-07/certify_proper_brauer2_from_discriminant.py",
]

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

state = json.loads(STATE.read_text(encoding="utf-8"))
sb = dict(state)
claimed_state = sb.pop("canonical_sha256")
assert claimed_state == csha(sb)

v89 = json.loads(V89.read_text(encoding="utf-8"))
vb = dict(v89)
claimed_v89 = vb.pop("canonical_sha256")
assert claimed_v89 == V89_SHA == csha(vb)

controller = json.loads((STAGE / "controller.json").read_text(encoding="utf-8"))
cb = dict(controller)
controller_sha = cb.pop("projection_canonical_sha256")
assert controller_sha == csha(cb)
assert state["controller_projection_canonical_sha256"] == controller_sha

assert state["schema"] == "STAGE33_MAIN_COMPACT_STATE_V28_V89_DISCRIMINANT_QUOTIENT_BRIDGE_SOURCE_BINDING_ACTIVE"
assert state["authority_sync"]["frontier_authority"] == "V89_PROPER14_DUAL_TO_DISCRIMINANT_QUOTIENT_BRIDGE"
assert state["branch_exact_frontier_authority"].endswith("e3-proper14-dual-to-discriminant-quotient-bridge-v89.json")
assert state["current"]["next_exact_leaf"] == NEXT
assert state["current"]["active_missing_interface"] == "SOURCE_BIND_RETAINED_AT_MOD2_SUPPORT_1_8_10_TO_LITERAL_PICARD_DIVISOR_OR_DIRECT_CECH_KUMMER_DATUM"

f = state["current_exact_frontier"]
assert f["e3_proper14_mask_decimal"] == 20
assert f["e3_proper14_support_one_based"] == [3, 5]
assert f["e3_proper14_is_dual_not_at2_element"] is True
assert f["e3_dual_pairing_bridge_rank_f2"] == 14
assert f["e3_retained_at_mod2_quotient_support_one_based"] == [1, 8, 10]
assert f["e3_retained_at_mod2_solution_unique"] is True
assert f["e3_literal_picard_divisor_materialized"] is False
assert f["e3_literal_kummer_function_materialized"] is False
assert f["e3_literal_cech_seed_materialized"] is False
assert f["e3_complete_residue_audit_materialized"] is False
assert f["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
assert f["e3_global_H2_mu2_nonexistence_claim"] is False

assert v89["e3_transport"]["proper14_mask_decimal"] == f["e3_proper14_mask_decimal"]
assert v89["e3_transport"]["proper14_support_one_based"] == f["e3_proper14_support_one_based"]
assert v89["e3_transport"]["retained_at_mod2_quotient_support_one_based"] == f["e3_retained_at_mod2_quotient_support_one_based"]
assert v89["dual_pairing_bridge"]["rank_f2"] == f["e3_dual_pairing_bridge_rank_f2"]
assert v89["next_exact_leaf"] == state["current"]["next_exact_leaf"]

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

startup = START.read_text(encoding="utf-8")
assert "MAIN-STATE.json` is the single mutable ordinary-startup authority" in startup
assert "current_leaf_working_set" in startup
assert "Current exact frontier:" not in startup
assert "V85" not in startup
assert "V89" not in startup
assert "Repository traversal itself follows `AGENTS.md`" in startup
assert "repeatable bounded search" in startup
assert "materially new mathematical signal" in startup

rules = RULES.read_text(encoding="utf-8")
assert "Frontier-promotion synchronization" in rules
assert "same change" in rules
assert "`MAIN-START-HERE.md` must not contain mutable frontier/version/leaf/progress" in rules

print(json.dumps({
    "success": True,
    "marker": "V90_STAGE33_V89_CURRENT_STARTUP_ALIGNMENT_COMPLETE",
    "state_canonical_sha256": claimed_state,
    "v89_canonical_sha256": V89_SHA,
    "frontier": state["authority_sync"]["frontier_authority"],
    "next_exact_leaf": NEXT,
    "working_set_size": len(EXPECTED_WORKING_SET),
    "stage33_progress": state["stage33_progress"],
    "merge_allowed": False,
}, sort_keys=True))
