#!/usr/bin/env python3
"""Verify hostile-audited V91C1A Stage33 MAIN startup projection."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parents[1]
D = H / "33-12"
STATE = H / "MAIN-STATE.json"
V91C = D / "e3-v91c-type-safe-cech-adapter-interface.json"
V91C1A = D / "e3-v91c1a-a2-02-literal-boundary-seed-localization.json"

STATE_SHA = "5ef0145cbe203b6d0964b985402b28063515247ea9c8b8587d82c4b6e44b354c"
V91C_SHA = "da156e8fcbd59743073b5a3d8ba5359c533b0b045adddc41877310974cdc1754"
V91C1A_SHA = "7f81ce5da7a4880cf0ffa048ab335fe2db9a643158d26144f45d0de22604b403"
NEXT = "V91C1B_ATTACH_A2_02_LITERAL_BOUNDARY_FUNCTION_PACKAGES_TO_RESOLVED_FULL_SURFACE_HEIGHT_ONE_AND_RESOLUTION_EXCEPTIONAL_VALUATIONS_WITH_CECH_CARTIER_TRANSITION_DATA"
COMPONENTS = ["EXC_003","EXC_004","EXC_011","EXC_012","SIDE_002","SIDE_004","SIDE_006","SIDE_008"]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canon(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


state = json.loads(STATE.read_text(encoding="utf-8"))
body = dict(state)
claimed = body.pop("canonical_sha256")
assert claimed == STATE_SHA == csha(body)

v91c = load_canon(V91C, V91C_SHA)
v91c1a = load_canon(V91C1A, V91C1A_SHA)

assert state["schema"] == "STAGE33_MAIN_COMPACT_STATE_V31_V91C1A_LITERAL_A2_02_PACKAGE_ACTIVE"
assert state["authority_sync"]["frontier_authority"] == "V91C1A_A2_02_LITERAL_BOUNDARY_PACKAGE_LOCALIZED"
assert state["branch_exact_frontier_authority"].endswith("e3-v91c1a-a2-02-literal-boundary-seed-localization.json")
assert state["current"]["next_exact_leaf"] == NEXT
assert state["stage33_progress"] == "6/11"
assert state["firewalls"]["merge_allowed"] is False

audit = state["audit_provenance"]
assert audit["v91c1a_pr"] == 1613
assert audit["hostile_audit_review"] == 5121286657
assert audit["hostile_audit_verdict"] == "PASS"
assert audit["audit_pass_credit"] is True
assert audit["exact_audited_head"] == "12191226e71878bb252a2e764a856fa336586b72"
assert audit["merge_commit"] == "d6d49a7a5b7678442d5c26080926f3f80032c4d4"

front = state["current_exact_frontier"]
assert front["a2_02_literal_boundary_record_localized"] is True
assert front["a2_02_component_count"] == 8
assert front["a2_02_component_ids"] == COMPONENTS
assert front["a2_02_claimed_e3_coefficient"] is False
assert front["a2_02_claimed_mask20_image"] is False
assert front["full_surface_cech_transition_cartier_assembly_materialized"] is False
assert front["e3_marked_brauer_image_from_boundary_functions_materialized"] is False

assert v91c["type_firewall"]["retired_object_remains_forbidden"] is True
assert v91c1a["literal_package_record"]["component_ids_in_source_order"] == COMPONENTS
assert v91c1a["selection_semantics"]["selected_direction_is_claimed_e3_coefficient"] is False
assert v91c1a["selection_semantics"]["single_direction_is_claimed_to_map_to_mask20"] is False
assert v91c1a["target_firewall"]["full_surface_cech_transition_glue_materialized"] is False
assert v91c1a["target_firewall"]["cartier_transition_binding_materialized"] is False
assert v91c1a["target_firewall"]["exact_marked_brauer_image_equal_mask20_materialized"] is False
assert v91c1a["next_exact_leaf"] == NEXT

assert "stages/stage33/33-11/materialize_stage33_11_a2_26_explicit_gersten_difference_preimage.py" in state["current_leaf_working_set"]
assert state["anti_loop_policy"]["do_not_treat_a2_02_preflight_direction_as_e3_coefficient"] is True

print(json.dumps({
    "success": True,
    "marker": "V94_V91C1A_HOSTILE_AUDITED_STARTUP_COMPLETE",
    "state_sha256": STATE_SHA,
    "v91c1a_sha256": V91C1A_SHA,
    "frontier": state["authority_sync"]["frontier_authority"],
    "next_exact_leaf": NEXT,
    "stage33_progress": state["stage33_progress"],
}, sort_keys=True))
