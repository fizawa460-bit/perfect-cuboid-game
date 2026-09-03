#!/usr/bin/env python3
"""Verify the completed post-V36 controller/generator synchronization."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
RECEIPT = HERE / "j2-post-v36-controller-generator-sync-v38.json"
EXPECTED = "ece3684e2802f68651d3c526e43a705903665c6f6011ae282c15fbce2bdc76a1"
REMAINING = ["e3", "e1", "e4", "e5", "e6", "e7", "e8", "e9", "e10"]

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

controller_schema_now = json.loads((STAGE33 / "controller.json").read_text())["schema"]
if controller_schema_now == "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V60_POST_V39_LOCATOR_FIRST_CONSTRUCTION_ACTIVE":
    import runpy
    runpy.run_path(str(HERE / "verify_j2_post_v38_locator_first_construction_policy_v39.py"), run_name="__main__")
    raise SystemExit(0)

r = json.loads(RECEIPT.read_text())
rb = dict(r)
claimed = rb.pop("canonical_sha256")
assert claimed == EXPECTED == csha(rb)
assert r["status"] == "OPERATIONAL_AUTHORITY_SYNC_COMPLETE_NO_MATH_CHANGE"
controller = json.loads((STAGE33 / "controller.json").read_text())
cb = dict(controller)
controller_sha = cb.pop("projection_canonical_sha256")
assert controller_sha == r["source_locks"]["controller_projection_canonical_sha256"] == csha(cb)
assert controller["schema"] == r["synchronization"]["controller_schema"]
assert controller["advance_allowed"] is False
assert controller["execution"]["advance_allowed"] is False
assert controller["post_v36_authority"]["status"] == "SYNCHRONIZED_EXACT_PROJECTION_NO_MATH_CHANGE"
assert controller["stage33_12"]["finite_v4_kummer_adapted_columns_materialized"] == 1
assert controller["stage33_12"]["finite_v4_kummer_columns_materialized"] == 0
state = json.loads((STAGE33 / "MAIN-STATE.json").read_text())
sb = dict(state)
state_sha = sb.pop("canonical_sha256")
assert state_sha == r["source_locks"]["main_state_canonical_sha256"] == csha(sb)
assert state["schema"] == r["synchronization"]["main_state_schema"]
assert state["authority_sync"]["status"] == "SYNCHRONIZED_POST_V36"
assert state["authority_sync"]["override_active"] is False
assert state["authority_sync"]["controller_and_generator_synchronized"] is True
assert state["work_checkpoint"] == {"authority": "OPERATIONAL_ONLY_NOT_PROOF", "status": "EMPTY"}
assert state["current_exact_frontier"]["j2_adapted_columns_materialized"] == 1
assert state["current_exact_frontier"]["original_standard_columns_materialized"] == 0
assert state["current_exact_frontier"]["remaining_adapted_source_labels"] == REMAINING
assert state["execution_gate"]["advance_allowed"] is False
assert r["current_exact_frontier"]["new_mathematical_column_materialized_in_v38"] is False
assert r["anti_inference"]["mathematical_authority_changed_by_sync"] is False
assert not any(r["anti_inference"].values())
assert not any(r["promotion_firewall"].values())
print(json.dumps({"success": True, "canonical_sha256": EXPECTED, "controller_projection_canonical_sha256": controller_sha, "main_state_canonical_sha256": state_sha, "authority_sync": "SYNCHRONIZED_POST_V36", "adapted_columns_materialized": 1, "standard_columns_materialized": 0, "mathematical_change": False, "marker": "PROOF_REPLAY_COMPLETE"}, sort_keys=True))
