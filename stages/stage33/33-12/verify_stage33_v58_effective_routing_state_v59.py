#!/usr/bin/env python3
"""Verify Stage33 V58 is the effective compact-state routing override without mathematical promotion."""
import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parents[1]
D = H / "33-12"

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

v41 = json.loads((D / "j2-post-v39-arsenal-first-bounded-search-policy-v41.json").read_text())
v57 = json.loads((D / "e3-mask20-b1-gysin-image-gate-v57.json").read_text())
v58 = json.loads((D / "e3-search-routing-supersession-v58.json").read_text())
state = json.loads((H / "MAIN-STATE.json").read_text())
startup = (H / "MAIN-START-HERE.md").read_text()

assert v41["routing_contract"]["one_automatic_bounded_repository_search_after_arsenal_miss"] is True
assert v41["anti_loop"]["automatic_bounded_search_budget_per_missing_object"] == 1
r = v58["routing_contract"]
assert v58["schema"] == "stage33.search_routing_supersession.v58"
assert r["arsenal_first"] is True
assert r["fixed_per_object_search_count_cap"] is None
assert r["repeated_bounded_repository_search_allowed"] is True
assert r["search_miss_proves_repository_absence"] is False
assert r["search_miss_proves_mathematical_nonexistence"] is False
assert "unlimited or open-ended repository search" in r["forbidden"]
assert v58["supersedes_operationally"]["mathematical_content_of_v57"] == "UNCHANGED"

assert v57["exact_b1_route_geometry"]["required_marked_matrix_shape"] == [14, 4]
assert v57["e3_membership_gate"]["proper14_mask_decimal"] == 20
assert v57["e3_membership_gate"]["membership_in_im_Phi_B1"] == "OPEN_NOT_COMPUTED"
assert v57["credit_firewall"]["genuine_full_surface_h2_mu2_lift_for_e3"] is False
assert v57["credit_firewall"]["e3_kummer_column_materialized"] is False
assert v57["credit_firewall"]["stage33_progress"] == "6/11"
assert v57["credit_firewall"]["merge_allowed"] is False

claimed = state["canonical_sha256"]
body = dict(state); body.pop("canonical_sha256")
assert claimed == csha(body)
assert state["schema"] == "STAGE33_MAIN_COMPACT_STATE_V20_V58_REPEATABLE_BOUNDED_SEARCH_ACTIVE"
assert state["stage33_progress"] == "6/11"
assert state["authority_sync"]["operational_routing_authority"] == "V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP"
assert state["authority_sync"]["inherited_operational_routing_authority"] == "V41_ARSENAL_FIRST_ONE_BOUNDED_SEARCH_POLICY"
assert state["authority_sync"]["supersession_scope"] == "FIXED_SEARCH_COUNT_CAP_ONLY_NO_MATHEMATICAL_CHANGE"
assert state["discovery_policy"]["fixed_per_object_search_count_cap"] is None
assert state["discovery_policy"]["repeated_bounded_repository_search_allowed"] is True
assert state["discovery_policy"]["each_repeat_requires_materially_new_mathematical_signal"] is True
assert state["discovery_policy"]["unlimited_or_open_ended_repository_search_allowed"] is False
assert state["discovery_policy"]["automatic_branch_history_archaeology_after_miss_allowed"] is False
assert state["current"]["active_missing_interface"] == "B1_BRANCH_H1_TO_PROPER14_BRAUER_IMAGE_MATRIX"
assert state["current_exact_frontier"]["e3_b1_to_proper14_matrix_shape"] == [14, 4]
assert state["current_exact_frontier"]["e3_b1_membership_status"] == "OPEN_NOT_COMPUTED"
assert state["current_exact_frontier"]["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
assert state["firewalls"]["stage33_12_closed_exact"] is False
assert state["firewalls"]["stage33_13_released"] is False
assert state["firewalls"]["merge_allowed"] is False

assert "no fixed per-object count cap" in startup
assert "Additional bounded searches are allowed" in startup
assert "materially new mathematical signal" in startup
assert "B1_BRANCH_H1_TO_PROPER14_BRAUER_IMAGE_MATRIX" in startup

print(json.dumps({"success": True, "schema": state["schema"], "effective_routing": state["authority_sync"]["operational_routing_authority"], "stage33_progress": state["stage33_progress"], "mathematical_change": False, "merge_allowed": False}, sort_keys=True))
