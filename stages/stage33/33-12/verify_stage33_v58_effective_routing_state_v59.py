#!/usr/bin/env python3
"""Replay immutable V58 routing while allowing later exact Stage33 frontiers."""
import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parents[1]
ROOT = H.parent.parent
D = H / "33-12"

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

v41 = json.loads((D / "j2-post-v39-arsenal-first-bounded-search-policy-v41.json").read_text())
v57 = json.loads((D / "e3-mask20-b1-gysin-image-gate-v57.json").read_text())
v58 = json.loads((D / "e3-search-routing-supersession-v58.json").read_text())
state = json.loads((H / "MAIN-STATE.json").read_text())
startup = (H / "MAIN-START-HERE.md").read_text()
agents = (ROOT / "AGENTS.md").read_text()

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

# Immutable V57 historical boundary.
assert v57["exact_b1_route_geometry"]["required_marked_matrix_shape"] == [14, 4]
assert v57["e3_membership_gate"]["proper14_mask_decimal"] == 20
assert v57["e3_membership_gate"]["membership_in_im_Phi_B1"] == "OPEN_NOT_COMPUTED"
assert v57["credit_firewall"]["genuine_full_surface_h2_mu2_lift_for_e3"] is False
assert v57["credit_firewall"]["e3_kummer_column_materialized"] is False
assert v57["credit_firewall"]["stage33_progress"] == "6/11"
assert v57["credit_firewall"]["merge_allowed"] is False

# Successor-safe live-state checks.  V79 may have computed and frozen the B1
# membership gate; V59 must not force the live state back to V57 OPEN status.
claimed = state["canonical_sha256"]
body = dict(state); body.pop("canonical_sha256")
assert claimed == csha(body)
assert state["stage33_progress"] == "6/11"
assert state["authority_sync"]["operational_routing_authority"] == "V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP"
assert state["discovery_policy"]["fixed_per_object_search_count_cap"] is None
assert state["discovery_policy"]["repeated_bounded_repository_search_allowed"] is True
assert state["discovery_policy"]["each_repeat_requires_materially_new_mathematical_signal"] is True
assert state["discovery_policy"]["unbounded_repository_search_allowed"] is False
assert state["current_exact_frontier"]["e3_b1_branch_h1_dimension"] == 4
assert state["current_exact_frontier"]["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
assert state["firewalls"]["stage33_12_closed_exact"] is False
assert state["firewalls"]["stage33_13_released"] is False
assert state["firewalls"]["merge_allowed"] is False

assert "V58" in startup
assert "repeatable bounded search" in startup
assert "materially new mathematical signal" in startup
assert "Repository traversal itself follows `AGENTS.md`" in startup
assert "a search miss never proves repository-wide absence" in agents.lower()

print(json.dumps({
    "success": True,
    "schema": state["schema"],
    "effective_routing": state["authority_sync"]["operational_routing_authority"],
    "historical_v57_gate_replayed": True,
    "later_frontier_allowed": True,
    "stage33_progress": state["stage33_progress"],
    "mathematical_change_to_v58": False,
    "merge_allowed": False
}, sort_keys=True))
