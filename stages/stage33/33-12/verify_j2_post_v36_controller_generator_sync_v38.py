#!/usr/bin/env python3
"""Replay immutable V38 receipt, then verify the live operational layer."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
RECEIPT = HERE / "j2-post-v36-controller-generator-sync-v38.json"
EXPECTED = "ece3684e2802f68651d3c526e43a705903665c6f6011ae282c15fbce2bdc76a1"
REMAINING = ["e3", "e1", "e4", "e5", "e6", "e7", "e8", "e9", "e10"]
V59 = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V59_POST_V36_FIRST_ADAPTED_COLUMN_REUSE_STOP"
V60 = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V60_POST_V39_LOCATOR_FIRST_CONSTRUCTION_ACTIVE"
V61 = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V61_POST_V39_CURRENT_MULTI_REGISTRY_CONSTRUCTION_ACTIVE"
V62 = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


# Immutable historical V38 receipt: always replay this first, regardless of the
# current successor controller.  Live operational promotion must never bypass
# the receipt that the V38 verifier is named to preserve.
r = json.loads(RECEIPT.read_text())
rb = dict(r)
claimed = rb.pop("canonical_sha256")
assert claimed == EXPECTED == csha(rb)
assert r["schema"] == "STAGE33_12_POST_V36_CONTROLLER_GENERATOR_SYNC_V38"
assert r["stage"] == "33-12"
assert r["status"] == "OPERATIONAL_AUTHORITY_SYNC_COMPLETE_NO_MATH_CHANGE"

sync = r["synchronization"]
assert sync["controller_and_generator_synchronized"] is True
assert sync["controller_schema"] == V59
assert sync["main_state_schema"] == "STAGE33_MAIN_COMPACT_STATE_V16_POST_V36_SYNCHRONIZED_REUSE_STOP"
assert sync["generator_write_mode_restored"] is True
assert sync["legacy_controller_keys_preserved"] is True
assert sync["override_cleared"] is True
assert sync["work_checkpoint_cleared"] is True
assert sync["v37_role"] == "SUPERSEDED_OPERATIONAL_REPAIR_RECEIPT_ONLY"

frontier = r["current_exact_frontier"]
assert frontier["j2_adapted_columns_materialized"] == 1
assert frontier["j2_adapted_columns_total"] == 10
assert frontier["original_standard_columns_materialized"] == 0
assert frontier["remaining_adapted_source_labels"] == REMAINING
assert frontier["new_mathematical_column_materialized_in_v38"] is False
assert frontier["next_exact_leaf"] == "WAIT_FOR_NEW_GENUINE_H2_MU2_LIFT_OR_REGISTERED_POSITIVE_EVIDENCE_ASSET"

assert r["anti_inference"]["mathematical_authority_changed_by_sync"] is False
assert not any(r["anti_inference"].values())
assert not any(r["promotion_firewall"].values())

locks = r["source_locks"]
assert locks["v25_genuine_h2_mu2_adapter_canonical_sha256"] == "d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"
assert locks["v33_current_hs_d2_nonzero_canonical_sha256"] == "59385430d2806fd600006b8bee1e02170f28d0a598912555d1e905e556c84b8f"
assert locks["v34_first_adapted_column_canonical_sha256"] == "eb53bd545626efe3b32d407eccd2788e991494203acd718d88100ee7233b909e"
assert locks["v35_handoff_canonical_sha256"] == "4837ebeb0dd4ea97f196f6e4a405923eede73b53f663f9e0acac66aaf4e5f8e9"
assert locks["v36_handoff_canonical_sha256"] == "065c0ca8a92ad0994a88b2a62337a0ceb33af9823e746590e7de590676d6db7c"
assert locks["v37_operational_repair_canonical_sha256"] == "8b3da6a1b747a39a54f329959d3cac0073ec1bc57c21acf9a71f979194de8dcf"

# Mutable live layer.  Frozen V38 controller/MAIN-state hashes are compared only
# on the exact V59 projection.  Successor controllers must instead prove their
# own self-consistency and then run their own operational routing verifier.
controller = json.loads((STAGE33 / "controller.json").read_text())
cb = dict(controller)
controller_sha = cb.pop("projection_canonical_sha256")
assert controller_sha == csha(cb)
controller_schema_now = controller["schema"]

state = json.loads((STAGE33 / "MAIN-STATE.json").read_text())
sb = dict(state)
state_sha = sb.pop("canonical_sha256")
assert state_sha == csha(sb)

if controller_schema_now == V59:
    assert controller_sha == locks["controller_projection_canonical_sha256"]
    assert controller["advance_allowed"] is False
    assert controller["execution"]["advance_allowed"] is False
    assert controller["post_v36_authority"]["status"] == "SYNCHRONIZED_EXACT_PROJECTION_NO_MATH_CHANGE"
    assert controller["stage33_12"]["finite_v4_kummer_adapted_columns_materialized"] == 1
    assert controller["stage33_12"]["finite_v4_kummer_columns_materialized"] == 0
    assert state_sha == locks["main_state_canonical_sha256"]
    assert state["schema"] == sync["main_state_schema"]
    assert state["authority_sync"]["status"] == "SYNCHRONIZED_POST_V36"
    assert state["authority_sync"]["override_active"] is False
    assert state["authority_sync"]["controller_and_generator_synchronized"] is True
    assert state["work_checkpoint"] == {"authority": "OPERATIONAL_ONLY_NOT_PROOF", "status": "EMPTY"}
    assert state["execution_gate"]["advance_allowed"] is False
    live_layer = "V59_FROZEN_PROJECTION"

elif controller_schema_now in {V60, V61}:
    # Historical successor compatibility: the immutable V38 receipt above has
    # already been replayed.  A V60/V61 tree must additionally carry its own V39
    # live-routing verifier; do not compare its live hashes to frozen V38 hashes.
    legacy = HERE / "verify_j2_post_v38_locator_first_construction_policy_v39.py"
    assert legacy.is_file(), "V39 compatibility verifier required on a V60/V61 tree"
    runpy.run_path(str(legacy), run_name="__main__")
    live_layer = "V39_SUCCESSOR_ROUTING"

elif controller_schema_now == V62:
    # Preserve the V38 frontier under the current controller without pretending
    # that V62 should equal the frozen V38 projection.
    assert controller["stage33_12"]["finite_v4_kummer_adapted_columns_materialized"] == 1
    assert controller["stage33_12"]["finite_v4_kummer_columns_materialized"] == 0
    assert state["current_exact_frontier"]["j2_adapted_columns_materialized"] == 1
    assert state["current_exact_frontier"]["original_standard_columns_materialized"] == 0
    assert state["current_exact_frontier"]["remaining_adapted_source_labels"] == REMAINING
    runpy.run_path(str(HERE / "verify_j2_post_v39_arsenal_first_bounded_search_policy_v41.py"), run_name="__main__")
    live_layer = "V41_ARSENAL_FIRST_ROUTING"

else:
    raise AssertionError(f"unsupported live controller schema for V38 replay: {controller_schema_now}")

print(json.dumps({
    "success": True,
    "canonical_sha256": EXPECTED,
    "immutable_v38_receipt_replayed": True,
    "historical_controller_projection_canonical_sha256": locks["controller_projection_canonical_sha256"],
    "historical_main_state_canonical_sha256": locks["main_state_canonical_sha256"],
    "live_controller_schema": controller_schema_now,
    "live_controller_projection_canonical_sha256": controller_sha,
    "live_main_state_canonical_sha256": state_sha,
    "live_layer": live_layer,
    "adapted_columns_materialized": 1,
    "standard_columns_materialized": 0,
    "mathematical_change": False,
    "marker": "PROOF_REPLAY_COMPLETE"
}, sort_keys=True))
