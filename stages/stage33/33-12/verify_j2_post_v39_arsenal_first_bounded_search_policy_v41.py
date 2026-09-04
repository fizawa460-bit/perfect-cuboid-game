#!/usr/bin/env python3
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
STATE_SCHEMA = "STAGE33_MAIN_COMPACT_STATE_V19_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE"
NEXT = "ARSENAL_FIRST_THEN_ONE_BOUNDED_SEARCH_THEN_CONSTRUCT_OR_REQUEST_USER_AUTHORIZATION"
SCOPE = "ARSENAL_FIRST_ONE_BOUNDED_SEARCH_THEN_CONSTRUCT_OR_USER_AUTHORIZED_BROADENING"

def csha(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

p = json.loads(POLICY.read_text())
pb = dict(p)
claimed = pb.pop("canonical_sha256")
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
rt = research.read_text()
assert "Stage16 and later" in rt and "Stages12–15" in rt and "## Arsenal" in rt
ai = json.loads(arsenal.read_text())
assert str(ai.get("schema", "")).startswith("RESEARCH_ARSENAL_")

agents = (ROOT / "AGENTS.md").read_text()
assert "Recursive repository-tree acquisition is forbidden by default" in agents
assert "known path is already known" not in agents
assert "If an exact path is already known, fetch that path directly" in agents
assert "use GitHub search rather than recursive tree enumeration" in agents
assert "use GitHub code search" in agents
assert "enumerating the full file set is itself an explicit research requirement" in agents
assert "Stage33 is stricter" in agents
assert "search miss never proves global repository absence" in agents.lower()

c = json.loads((STAGE33 / "controller.json").read_text())
cb = dict(c)
cclaimed = cb.pop("projection_canonical_sha256")
assert cclaimed == csha(cb)
assert c["schema"] == CONTROLLER_SCHEMA
assert c["advance_allowed"] is True and c["execution"]["advance_allowed"] is True
assert c["advance_scope"] == SCOPE
assert c["current"]["next_exact_leaf"] == c["next_item"] == c["execution"]["next_item"] == NEXT
route = c["post_v41_routing"]
assert route["policy_v41_canonical_sha256"] == EXPECTED
assert route["arsenal_first"] is True
assert route["automatic_bounded_search_budget_per_missing_object"] == 1
assert route["broader_search_requires_explicit_user_authorization"] is True
assert route["miss_proves_repository_absence"] is False

state = json.loads((STAGE33 / "MAIN-STATE.json").read_text())
sb = dict(state)
sclaimed = sb.pop("canonical_sha256")
assert sclaimed == csha(sb)
assert state["schema"] == STATE_SCHEMA
assert state["controller_projection_canonical_sha256"] == cclaimed
assert state["execution_gate"]["advance_scope"] == SCOPE
assert state["discovery_policy"]["ordinary_order"] == ["ARSENAL", "ONE_BOUNDED_REPOSITORY_SEARCH", "CONSTRUCT_OR_REQUEST_USER_AUTHORIZATION_FOR_BROADER_SEARCH"]
assert state["discovery_policy"]["automatic_bounded_search_budget_per_missing_object"] == 1
assert state["discovery_policy"]["broader_repository_history_or_origin_search_requires_explicit_user_authorization"] is True
assert all("evidence-locator" not in x for x in state["current_leaf_working_set"])

startup = (STAGE33 / "MAIN-START-HERE.md").read_text()
assert "Arsenal first" in startup
assert "one automatic bounded repository search" in startup
assert "explicit user authorization" in startup
assert "controller -> active roadmap -> Arsenal index/card -> exact referenced files" in startup
assert "recursive repository tree" in startup
assert "search miss never proves repository absence" in startup.lower()

print(json.dumps({
    "success": True,
    "marker": "V41_ROUTING_REPLAY_COMPLETE",
    "policy_canonical_sha256": EXPECTED,
    "controller_projection_canonical_sha256": cclaimed,
    "main_state_canonical_sha256": sclaimed,
    "arsenal_first": True,
    "automatic_bounded_search_budget": 1,
    "broader_search_requires_user_authorization": True,
    "recursive_repository_tree_default_forbidden": True,
    "mathematical_change": False
}, sort_keys=True))
