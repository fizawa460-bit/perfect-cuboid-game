#!/usr/bin/env python3
"""Verify post-V36 startup authority in transition or synchronized mode.

V37 remains an immutable operational receipt. This verifier is a compatibility
entrypoint for CI; synchronized heads dispatch to the V38 verifier.
"""
from __future__ import annotations
import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
V38_VERIFY = HERE / "verify_j2_post_v36_controller_generator_sync_v38.py"
LOCKS = {
    "v25": (HERE / "j2-genuine-h2-mu2-kummer-adapter-v25.json", "d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"),
    "v33": (HERE / "j2-current-hs-d2-nonzero-v33.json", "59385430d2806fd600006b8bee1e02170f28d0a598912555d1e905e556c84b8f"),
    "v34": (HERE / "j2-adapted-first-kummer-column-v34.json", "eb53bd545626efe3b32d407eccd2788e991494203acd718d88100ee7233b909e"),
    "v35": (HERE / "j2-post-v34-main-handoff-v35.json", "4837ebeb0dd4ea97f196f6e4a405923eede73b53f663f9e0acac66aaf4e5f8e9"),
    "v36": (HERE / "j2-post-v35-evidence-locator-handoff-v36.json", "065c0ca8a92ad0994a88b2a62337a0ceb33af9823e746590e7de590676d6db7c"),
    "v37": (HERE / "j2-post-v36-startup-authority-repair-v37.json", "8b3da6a1b747a39a54f329959d3cac0073ec1bc57c21acf9a71f979194de8dcf")
}

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def load_locked(path, expected):
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj

state = json.loads((STAGE33 / "MAIN-STATE.json").read_text())
status = state.get("authority_sync", {}).get("status")
if status == "SYNCHRONIZED_POST_V36":
    assert V38_VERIFY.exists()
    runpy.run_path(str(V38_VERIFY), run_name="__main__")
    raise SystemExit(0)
assert status == "ACTIVE_POST_V36_OVERRIDE"
z = {name: load_locked(path, digest) for name, (path, digest) in LOCKS.items()}
assert z["v25"]["genuine_h2_mu2_adapter"]["full_surface_named_j2_h2_mu2_lift_materialized"] is True
assert z["v33"]["exact_information_boundary"]["current_hs_d2_nonzero_proved"] is True
assert z["v34"]["exact_information_boundary"]["adapted_kummer_columns_materialized"] == 1
assert z["v34"]["exact_information_boundary"]["original_standard_kummer_columns_materialized"] == 0
assert z["v36"]["bounded_reuse_first_search"]["positive_asset_match_materialized"] is False
assert z["v36"]["bounded_reuse_first_search"]["old_origin_search_restarted"] is False
assert z["v37"]["bounded_local_check"]["broad_historical_search_performed"] is False
assert z["v37"]["bounded_local_check"]["synthetic_split_permitted"] is False
assert state["work_checkpoint"]["status"] == "ACTIVE_UNPROMOTED"
assert not any(state["firewalls"].values())
print(json.dumps({"success": True, "authority_sync": "ACTIVE_POST_V36_OVERRIDE", "v25_v37_source_locks": "PASS", "marker": "PROOF_REPLAY_COMPLETE"}, sort_keys=True))
