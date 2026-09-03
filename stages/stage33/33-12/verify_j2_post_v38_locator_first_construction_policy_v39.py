#!/usr/bin/env python3
"""Verify Stage33 V39 locator-first routing and construction authorization."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
ROOT = STAGE33.parent.parent
POLICY = HERE / "j2-post-v38-locator-first-construction-policy-v39.json"
EXPECTED = "2fddd4bda3d853a42656b32483cefd116677e5bd70f633dc4791440b0269b230"
CONTROLLER_SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V60_POST_V39_LOCATOR_FIRST_CONSTRUCTION_ACTIVE"
MAIN_SCHEMA = "STAGE33_MAIN_COMPACT_STATE_V17_POST_V39_LOCATOR_FIRST_CONSTRUCTION_ACTIVE"
NEXT = "QUERY_EVIDENCE_LOCATOR_THEN_CONSTRUCT_REMAINING_GENUINE_H2_MU2_LIFT_IF_MISS"
REMAINING = ["e3", "e1", "e4", "e5", "e6", "e7", "e8", "e9", "e10"]
LOCATOR = ROOT / "docs/evidence-locator/query_evidence.py"
INDEX = ROOT / "docs/evidence-locator/index.json"

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def git_blob(path):
    return subprocess.check_output(["git", "hash-object", "--", str(path)], cwd=ROOT, text=True).strip()

p = json.loads(POLICY.read_text())
pb = dict(p)
claimed = pb.pop("canonical_sha256")
assert claimed == EXPECTED == csha(pb)
assert p["status"] == "OPERATIONAL_ROUTING_REPAIR_NO_MATH_CHANGE"
assert p["routing_contract"]["query_locator_first_for_existing_evidence"] is True
assert p["routing_contract"]["construction_authorized_after_locator_miss"] is True
assert p["routing_contract"]["broad_repository_or_history_fallback_after_miss"] is False
assert p["audit_finding"]["locator_miss_proves_repository_absence"] is False
assert p["audit_finding"]["mathematical_authority_changed"] is False
assert p["current_exact_frontier"]["new_mathematical_column_materialized_in_v39"] is False
assert not any(p["anti_inference"].values())
assert not any(p["promotion_firewall"].values())

assert INDEX.is_file() and LOCATOR.is_file()
assert git_blob(INDEX) == p["source_locks"]["evidence_locator_index_blob_sha1"]
assert git_blob(LOCATOR) == p["source_locks"]["evidence_locator_query_blob_sha1"]
idx = json.loads(INDEX.read_text())
assert idx["schema"] == "PERFECT_CUBOID_EVIDENCE_LOCATOR_V2"
assert idx["policies"]["query_miss_proves_repo_absence"] is False
assert idx["policies"]["locator_match_grants_mathematical_credit"] is False

miss = json.loads(subprocess.check_output(
    [sys.executable, str(LOCATOR), "__stage33_v39_definite_no_match_sentinel__"],
    cwd=ROOT, text=True
))
assert miss["match_count"] == 0
assert miss["firewalls"]["query_miss_proves_repo_absence"] is False
assert miss["firewalls"]["locator_match_grants_mathematical_credit"] is False

controller = json.loads((STAGE33 / "controller.json").read_text())
cb = dict(controller)
controller_sha = cb.pop("projection_canonical_sha256")
assert controller_sha == csha(cb)
assert controller["schema"] == CONTROLLER_SCHEMA
assert controller["advance_allowed"] is True
assert controller["execution"]["advance_allowed"] is True
assert controller["advance_scope"] == "LOCATOR_FIRST_THEN_CONSTRUCT_MISSING_GENUINE_H2_MU2_LIFT"
assert controller["current"]["next_exact_leaf"] == controller["next_item"] == controller["execution"]["next_item"] == NEXT
assert controller["post_v39_routing"]["policy_v39_canonical_sha256"] == EXPECTED
assert controller["post_v39_routing"]["locator_miss_proves_repository_absence"] is False
assert controller["post_v39_routing"]["construction_authorized_after_locator_miss"] is True
assert controller["post_v39_routing"]["broad_historical_search_permitted"] is False
assert controller["stage33_12"]["finite_v4_kummer_adapted_columns_materialized"] == 1
assert controller["stage33_12"]["finite_v4_kummer_columns_materialized"] == 0

state = json.loads((STAGE33 / "MAIN-STATE.json").read_text())
sb = dict(state)
state_sha = sb.pop("canonical_sha256")
assert state_sha == csha(sb)
assert state["schema"] == MAIN_SCHEMA
assert state["controller_projection_canonical_sha256"] == controller_sha
assert state["authority_sync"]["status"] == "SYNCHRONIZED_POST_V39_ROUTING"
assert state["authority_sync"]["mathematical_authority"] == "V25_V36_EXACT_CERTIFICATE_CHAIN"
assert state["authority_sync"]["operational_routing_authority"] == "V39_LOCATOR_FIRST_CONSTRUCTION_POLICY"
assert state["execution_gate"]["advance_allowed"] is True
assert state["execution_gate"]["construction_priority"] == REMAINING
assert state["anti_loop_policy"]["locator_query_is_repeatable_routing_step"] is True
assert state["anti_loop_policy"]["locator_miss_authorizes_new_construction"] is True
assert state["anti_loop_policy"]["broad_repository_or_history_fallback_after_locator_miss"] is False
assert state["current_exact_frontier"]["j2_adapted_columns_materialized"] == 1
assert state["current_exact_frontier"]["original_standard_columns_materialized"] == 0
assert state["current_exact_frontier"]["remaining_adapted_source_labels"] == REMAINING
assert not (HERE / "__x__").exists()
assert not (HERE / "e3-construction-plan-v39.md").exists()

print(json.dumps({
    "success": True,
    "canonical_sha256": EXPECTED,
    "controller_projection_canonical_sha256": controller_sha,
    "main_state_canonical_sha256": state_sha,
    "locator_miss_proves_repo_absence": False,
    "construction_authorized_after_locator_miss": True,
    "broad_history_fallback": False,
    "mathematical_change": False,
    "adapted_columns_materialized": 1,
    "standard_columns_materialized": 0,
    "marker": "PROOF_REPLAY_COMPLETE"
}, sort_keys=True))
