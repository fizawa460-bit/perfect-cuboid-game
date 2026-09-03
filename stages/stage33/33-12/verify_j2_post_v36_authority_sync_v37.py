#!/usr/bin/env python3
"""Verify the post-V36 Stage33 startup authority gate without changing math.

This verifier source-locks the exact V25/V33/V34 frontier and the V35/V36/V37
handoff chain. It also checks that the compact MAIN projection cannot promote
closure/credit or synthesize a missing Kummer column.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent

LOCKS = {
    "v25": (HERE / "j2-genuine-h2-mu2-kummer-adapter-v25.json", "d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"),
    "v33": (HERE / "j2-current-hs-d2-nonzero-v33.json", "59385430d2806fd600006b8bee1e02170f28d0a598912555d1e905e556c84b8f"),
    "v34": (HERE / "j2-adapted-first-kummer-column-v34.json", "eb53bd545626efe3b32d407eccd2788e991494203acd718d88100ee7233b909e"),
    "v35": (HERE / "j2-post-v34-main-handoff-v35.json", "4837ebeb0dd4ea97f196f6e4a405923eede73b53f663f9e0acac66aaf4e5f8e9"),
    "v36": (HERE / "j2-post-v35-evidence-locator-handoff-v36.json", "065c0ca8a92ad0994a88b2a62337a0ceb33af9823e746590e7de590676d6db7c"),
    "v37": (HERE / "j2-post-v36-startup-authority-repair-v37.json", "8b3da6a1b747a39a54f329959d3cac0073ec1bc57c21acf9a71f979194de8dcf"),
}


def canonical_sha(obj: dict) -> str:
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    digest = hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    assert claimed == digest
    return digest


def load_locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text())
    assert canonical_sha(obj) == expected, path
    return obj


z = {name: load_locked(path, digest) for name, (path, digest) in LOCKS.items()}

assert z["v25"]["genuine_h2_mu2_adapter"]["full_surface_named_j2_h2_mu2_lift_materialized"] is True
assert z["v25"]["remaining_interface"]["standard_kummer_columns_materialized"] == 0
assert z["v33"]["exact_information_boundary"]["current_hs_d2_nonzero_proved"] is True
assert z["v33"]["kummer_hs_conclusion"]["named_J2_HS_d2_zero"] is False
assert z["v34"]["exact_information_boundary"]["adapted_kummer_columns_materialized"] == 1
assert z["v34"]["exact_information_boundary"]["original_standard_kummer_columns_materialized"] == 0
assert z["v34"]["original_standard_basis_relation"]["no_individual_standard_column_inferred"] is True

assert z["v35"]["current_exact_frontier"]["j2_adapted_columns_materialized"] == 1
assert z["v35"]["current_exact_frontier"]["original_standard_columns_materialized"] == 0
assert z["v35"]["anti_loop"]["do_not_split_standard_col2_col3_from_xor_relation"] is True

assert z["v36"]["bounded_reuse_first_search"]["positive_asset_match_materialized"] is False
assert z["v36"]["bounded_reuse_first_search"]["old_origin_search_restarted"] is False
assert z["v36"]["current_exact_frontier"]["new_mathematical_column_materialized_in_v36"] is False
assert z["v36"]["next_exact_leaf"]["action"] == "STOP_REUSE_FIRST_SEARCH"

assert z["v37"]["bounded_local_check"]["result"] == "NO_STANDALONE_E3_LIFT_IN_CURRENT_V34_V36_FRONTIER"
assert z["v37"]["bounded_local_check"]["broad_historical_search_performed"] is False
assert z["v37"]["bounded_local_check"]["synthetic_split_permitted"] is False
assert z["v37"]["current_exact_frontier"]["new_mathematical_column_materialized_in_v37"] is False
assert z["v37"]["next_exact_leaf"]["no_new_asset_means_stop"] is True

for name in ("v35", "v36", "v37"):
    fw = z[name]["promotion_firewall"]
    assert fw["merge_allowed"] is False
    assert fw["theorem_credit"] is False
    assert fw["receiver_credit"] is False
    assert fw["endpoint_credit"] is False
    assert fw["stage33_12_closed_exact"] is False

state = json.loads((STAGE33 / "MAIN-STATE.json").read_text())
assert state["authority_sync"]["status"] == "ACTIVE_POST_V36_OVERRIDE"
assert state["authority_sync"]["clear_only_after_controller_and_generator_are_synchronized_together"] is True
assert state["current_exact_frontier"]["j2_adapted_columns_materialized"] == 1
assert state["current_exact_frontier"]["original_standard_columns_materialized"] == 0
assert state["current_exact_frontier"]["remaining_adapted_source_labels"] == ["e3", "e1", "e4", "e5", "e6", "e7", "e8", "e9", "e10"]
assert state["work_checkpoint"]["status"] == "ACTIVE_UNPROMOTED"
for key in (
    "merge_allowed",
    "theorem_credit",
    "receiver_credit",
    "endpoint_credit",
    "stage33_12_closed_exact",
    "stage33_13_released",
):
    assert state["firewalls"][key] is False

print(json.dumps({
    "success": True,
    "authority_sync": "ACTIVE_POST_V36_OVERRIDE",
    "v25_v37_source_locks": "PASS",
    "adapted_columns_materialized": 1,
    "standard_columns_materialized": 0,
    "next_action": "STOP_UNLESS_NEW_GENUINE_LIFT_OR_REGISTERED_POSITIVE_ASSET",
    "marker": "PROOF_REPLAY_COMPLETE",
}, sort_keys=True))
