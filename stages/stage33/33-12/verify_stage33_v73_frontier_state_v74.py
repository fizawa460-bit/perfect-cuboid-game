#!/usr/bin/env python3
"""Replay historical V74 while allowing successor live frontiers after V73."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
STATE = STAGE / "MAIN-STATE.json"
V69 = HERE / "e3-b1-c22-j1-marked-kc-one-bit-transport-gate-v69.json"
V73 = HERE / "e3-b1-c22-j1-translation-torsor-v73.json"

V69_BLOB = "77638f2f3afb2dc6445f5130addcd52e88bc5767"
V73_BLOB = "277ec4bfd86a118b25e45632ce4a02fe3af87cc1"
V73_SHA = "b6a8dd83cd83547525e8ff328cccc1572791c52bea6061137c2bc59a134fa09d"

def csha(obj):
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def locked(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    assert obj.get("canonical_sha256") == expected == csha(obj), path
    return obj

state = json.loads(STATE.read_text(encoding="utf-8"))
assert state.get("canonical_sha256") == csha(state)
assert git_blob_sha(V69) == V69_BLOB
v69 = json.loads(V69.read_text(encoding="utf-8"))
assert git_blob_sha(V73) == V73_BLOB
v73 = locked(V73, V73_SHA)

# Immutable historical V73/V74 mathematical boundary.
assert v69["d2_verdict"] == "OPEN_ONE_BIT"
assert v73["translation_torsor"]["twisting_squareclass"] == "d=f1"
assert v73["translation_torsor"]["jacobian"] == "E: y^2=x*(x^2+a*x+b)"
assert v73["next_kernel_contract"]["allowed_minimum_norm_outcomes"] == [4, 12]
assert v73["credit_firewall"]["j1_translation_torsor_materialized"] is True
assert v73["credit_firewall"]["j1_twisted_kernel_minimum_norm_materialized"] is False
assert v73["credit_firewall"]["j1_marked_kc_coordinate_selected"] is False
assert v73["credit_firewall"]["identity_vs_shear_selected"] is False

# Successor-safe live-state checks: later exact frontiers may supersede V73,
# but they must preserve the V73 credit and the global firewalls until the
# independent J1 fingerprint is actually materialized.
assert state["stage33_progress"] == "6/11"
assert state["authority_sync"]["controller_global_authority_locked"] is True
assert state["authority_sync"]["operational_routing_authority"] == "V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP"
assert state["current_exact_frontier"]["J1_marked_kc_coordinate_candidates_f2"] == [[0, 1], [1, 1]]
assert state["current_exact_frontier"]["J1_marked_kc_remaining_ambiguity_bits"] == 1
assert state["current_exact_frontier"]["j1_translation_torsor_materialized"] is True
assert state["current_exact_frontier"]["j1_translation_torsor_equation"].endswith("d=f1")
assert state["current_exact_frontier"]["j1_translation_torsor_splitting_field"] == "Kgeom(sqrt(f1))"
assert state["current_exact_frontier"]["j1_twisted_kernel_minimum_norm_materialized"] is False
assert state["execution_gate"]["advance_allowed"] is True
assert state["firewalls"]["stage33_12_closed_exact"] is False
assert state["firewalls"]["stage33_13_released"] is False
assert state["firewalls"]["merge_allowed"] is False

print(json.dumps({
    "success": True,
    "marker": "V74_HISTORICAL_V73_FRONTIER_SUCCESSOR_SAFE_REPLAY",
    "v73_canonical_sha256": V73_SHA,
    "live_frontier": state["authority_sync"]["frontier_authority"],
    "remaining_transport_bits": 1,
    "j1_translation_torsor_materialized": True,
    "j1_twisted_kernel_minimum_norm_materialized": False,
    "merge_allowed": False
}, sort_keys=True))
