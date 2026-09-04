#!/usr/bin/env python3
"""Replay historical V76/V75 facts without pinning the later live frontier."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
STATE = STAGE / "MAIN-STATE.json"
V75 = HERE / "e3-b1-c22-j1-generic-quotient-discriminator-rejection-v75.json"

V75_BLOB = "6d316b60c933b446004297d9d32d0a7ef6c1c357"
V75_SHA = "22b166d44d516a5e0cb57bf582a21144d40b0035489a29036f86dc0944ce1192"


def csha(obj):
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


state = json.loads(STATE.read_text(encoding="utf-8"))
assert state["canonical_sha256"] == csha(state)
assert git_blob_sha(V75) == V75_BLOB
v75 = json.loads(V75.read_text(encoding="utf-8"))
assert v75["canonical_sha256"] == V75_SHA == csha(v75)

# Historical V75 result remains immutable even though V77 supersedes its
# interpretation of the old V65 nonzero-candidate gate.
assert v75["generic_quotient_replay"]["d_survives_in_quotient_equation"] is False
assert v75["generic_quotient_replay"]["same_generic_target_as_j2"] is True
assert v75["nonportable_j2_lattice_step"]["j2_exact_result"]["minimum_norm"] == 8
assert v75["nonportable_j2_lattice_step"]["v65_exact_j1_gate"]["allowed_minimum_norms"] == [4, 12]
assert v75["exact_missing_interface"]["generic_function_field_quotient_alone_sufficient"] is False
assert v75["next_kernel_contract"]["minimum_norm_materialized"] is False
assert v75["next_kernel_contract"]["marked_kc_coordinate_selected"] is False

# Later live frontiers are valid provided the global controller/firewalls and
# the historical lock are retained.  Do not pin this historical replay to V75.
assert state["stage33_progress"] == "6/11"
assert state["authority_sync"]["controller_global_authority_locked"] is True
assert state["authority_sync"]["operational_routing_authority"] == "V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP"
assert state["locked_facts"]["v75"]["sha256"] == V75_SHA
assert state["firewalls"]["stage33_12_closed_exact"] is False
assert state["firewalls"]["stage33_13_released"] is False
assert state["firewalls"]["merge_allowed"] is False

print(json.dumps({
    "success": True,
    "marker": "V76_HISTORICAL_V75_REPLAY_COMPLETE_LIVE_FRONTIER_UNPINNED",
    "v75_canonical_sha256": V75_SHA,
    "live_frontier": state["authority_sync"]["frontier_authority"],
    "merge_allowed": False,
}, sort_keys=True))
