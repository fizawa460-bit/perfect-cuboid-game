#!/usr/bin/env python3
"""Verify the V91B-promoted Stage33 MAIN startup projection with V91C active."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parents[1]
D = H / "33-12"
STATE = H / "MAIN-STATE.json"
V91B = D / "e3-v91b-boundary-function-adapter-gap.json"
V91C = D / "e3-v91c-type-safe-cech-adapter-interface.json"

STATE_SHA = "e1310be6736a51142b938d2010fa43538632efe8bbf6a765f482f4533914b8c8"
V91B_SHA = "7d0669f8c8ec6e590838095640b69cc0e9c8f76088a0c89f74cc8f49235d7443"
V91C_SHA = "da156e8fcbd59743073b5a3d8ba5359c533b0b045adddc41877310974cdc1754"
NEXT = "V91C_CONSTRUCT_EXACT_BOUNDARY_FUNCTION_A2_TO_V91_MARKED_DISCRIMINANT_PROPER14_ADAPTER"
V91C1 = "V91C1_ASSEMBLE_ONE_SOURCE_BOUND_FULL_SURFACE_CECH_TRANSITION_CARTIER_REPRESENTATIVE_FROM_RETAINED_BOUNDARY_FUNCTION_PACKAGES_AND_COMPUTE_MARKED_BRAUER_IMAGE_MASK20"

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

v91b = load_canon(V91B, V91B_SHA)
v91c = load_canon(V91C, V91C_SHA)

assert state["schema"] == "STAGE33_MAIN_COMPACT_STATE_V30_V91B_BOUNDARY_FUNCTION_ASSET_ACTIVE"
assert state["authority_sync"]["frontier_authority"] == "V91B_LITERAL_BOUNDARY_FUNCTION_ASSET_LOCALIZED"
assert state["branch_exact_frontier_authority"] == "stages/stage33/33-12/e3-v91b-boundary-function-adapter-gap.json"
assert state["current"]["next_exact_leaf"] == NEXT
assert state["current"]["active_missing_interface"] == "TYPE_SAFE_SOURCE_BOUND_FULL_SURFACE_CECH_TRANSITION_CARTIER_ASSEMBLY_AND_EXACT_MASK20_BRAUER_IMAGE_BINDING"
assert state["stage33_progress"] == "6/11"
assert state["firewalls"]["merge_allowed"] is False

audit = state["audit_provenance"]
assert audit["v91b_pr"] == 1604
assert audit["hostile_audit_review"] == 5120883188
assert audit["hostile_audit_verdict"] == "FAIL_FRESHNESS_ONLY"
assert audit["mathematics_and_route_selection_passed_in_review"] is True
assert audit["audit_pass_credit"] is False
assert audit["merged_by_user_after_math_pass"] is True
assert audit["merge_commit"] == "29ce620a693f7cbdec48bce9b720cc02dfe5fa74"

front = state["current_exact_frontier"]
assert front["e3_literal_boundary_function_route_source_localized"] is True
assert front["boundary_function_working_generator_count"] == 14
assert front["boundary_function_package_count"] == 134
assert front["boundary_function_cc_ct_scalar_ratios_all_one"] is True
assert front["direct_a2_to_k_14x14_bridge_forbidden"] is True
assert front["full_surface_cech_transition_cartier_assembly_materialized"] is False
assert front["e3_marked_brauer_image_from_boundary_functions_materialized"] is False

anti = state["anti_loop_policy"]
assert anti["do_not_reintroduce_retired_v47_14x14_p_w_after_v50"] is True
assert anti["do_not_promote_boundary_function_scalar_descent_alone_to_global_h2_mu2"] is True
assert "stages/stage33/33-12/e3-v91c-type-safe-cech-adapter-interface.json" in state["current_leaf_working_set"]

assert v91b["status"] == "PASS_EXACT_V91B_LITERAL_BOUNDARY_FUNCTION_ASSET_LIVE_PROPER14_ADAPTER_STILL_MISSING"
assert v91c["entry_authority"]["hostile_audit_verdict"] == "FAIL_FRESHNESS_ONLY"
assert v91c["entry_authority"]["audit_pass_credit"] is False
assert v91c["type_firewall"]["retired_object_remains_forbidden"] is True
assert v91c["adapter_definition"]["materialized"] is False
assert v91c["next_exact_leaf"] == V91C1

for key in ("stage33_12_closed_exact", "stage33_13_released", "receiver_credit", "theorem_credit", "endpoint_credit", "merge_allowed"):
    assert v91c["credit_firewall"][key] is False

print(json.dumps({
    "success": True,
    "marker": "V93_V91B_PROMOTED_V91C_ACTIVE_STARTUP_COMPLETE",
    "state_sha256": STATE_SHA,
    "v91b_sha256": V91B_SHA,
    "v91c_sha256": V91C_SHA,
    "frontier": state["authority_sync"]["frontier_authority"],
    "active_leaf": state["current"]["next_exact_leaf"],
    "candidate_next_leaf": v91c["next_exact_leaf"],
    "stage33_progress": state["stage33_progress"],
    "merge_allowed": state["firewalls"]["merge_allowed"],
}, sort_keys=True))
