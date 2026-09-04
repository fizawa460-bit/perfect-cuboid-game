#!/usr/bin/env python3
"""Replay immutable V41 routing under V58 and any later exact Stage33 frontier."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
ROOT = STAGE33.parent.parent
POLICY = HERE / "j2-post-v39-arsenal-first-bounded-search-policy-v41.json"
EXPECTED = "32b2ad7da0ad7ced22bd3d27ebc3abec36ed9d8fe037a4e2c676e3e44471a6f8"
CONTROLLER_SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE"

def csha(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

p = json.loads(POLICY.read_text())
pb = dict(p); claimed = pb.pop("canonical_sha256")
assert claimed == EXPECTED == csha(pb)
r = p["routing_contract"]
assert r["arsenal_first_for_existing_cross_stage_weapon"] is True
assert r["one_automatic_bounded_repository_search_after_arsenal_miss"] is True
assert r["broader_repository_history_or_origin_search_requires_explicit_user_authorization"] is True
assert r["arsenal_miss_proves_repository_absence"] is False
assert r["bounded_search_miss_proves_repository_absence"] is False
assert p["anti_loop"]["automatic_bounded_search_budget_per_missing_object"] == 1
assert p["mathematical_authority"] == "V25_V36_EXACT_CERTIFICATE_CHAIN_UNCHANGED"

assert not (ROOT / "docs/evidence-locator").exists()
research = ROOT / "docs/research-os/policies/repository-asset-discovery.md"
arsenal = ROOT / "docs/arsenal/index.json"
assert research.is_file() and arsenal.is_file()
assert str(json.loads(arsenal.read_text()).get("schema", "")).startswith("RESEARCH_ARSENAL_")

c = json.loads((STAGE33 / "controller.json").read_text())
cb = dict(c); cclaimed = cb.pop("projection_canonical_sha256")
assert cclaimed == csha(cb)
assert c["schema"] == CONTROLLER_SCHEMA
route = c["post_v41_routing"]
assert route["policy_v41_canonical_sha256"] == EXPECTED
assert route["arsenal_first"] is True
assert route["automatic_bounded_search_budget_per_missing_object"] == 1
assert route["broader_search_requires_explicit_user_authorization"] is True
assert route["miss_proves_repository_absence"] is False

state = json.loads((STAGE33 / "MAIN-STATE.json").read_text())
sb = dict(state); sclaimed = sb.pop("canonical_sha256")
assert sclaimed == csha(sb)
assert state["controller_projection_canonical_sha256"] == cclaimed
assert state["authority_sync"]["operational_routing_authority"] == "V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP"
assert state["discovery_policy"]["fixed_per_object_search_count_cap"] is None
assert state["discovery_policy"]["repeated_bounded_repository_search_allowed"] is True
assert state["discovery_policy"]["each_repeat_requires_materially_new_mathematical_signal"] is True
assert state["discovery_policy"]["unbounded_repository_search_allowed"] is False
assert all("evidence-locator" not in x for x in state["current_leaf_working_set"])

startup = (STAGE33 / "MAIN-START-HERE.md").read_text()
assert "Arsenal" in startup
assert "no fixed per-object count cap" in startup
assert "materially new mathematical signal" in startup
assert "search miss never proves repository absence" in startup.lower()
assert "controller -> active roadmap -> Arsenal index/card -> exact referenced files" in startup

print(json.dumps({
    "success": True,
    "marker": "V41_ROUTING_REPLAY_COMPLETE_UNDER_LATER_FRONTIER",
    "policy_canonical_sha256": EXPECTED,
    "controller_projection_canonical_sha256": cclaimed,
    "main_state_canonical_sha256": sclaimed,
    "inherited_v41_verified": True,
    "effective_v58_repeatable_bounded_search_verified": True,
    "later_exact_frontier_allowed": True,
    "mathematical_change_to_v41": False
}, sort_keys=True))
