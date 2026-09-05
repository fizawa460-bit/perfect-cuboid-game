#!/usr/bin/env python3
"""Replay historical V72/V71 frontier under V71 or any later exact successor frontier."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
V69 = HERE / "e3-b1-c22-j1-marked-kc-one-bit-transport-gate-v69.json"
V71 = HERE / "e3-b1-c22-j1-cv-e2-cocycle-v71.json"

V69_BLOB = "77638f2f3afb2dc6445f5130addcd52e88bc5767"
V71_SHA = "3e9409ee7537ab4edb12e2416745bbd074f1cc1b02a4fc8a92be643075b8569a"

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def locked(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj

assert git_blob_sha(V69) == V69_BLOB
v69 = json.loads(V69.read_text(encoding="utf-8"))
v71 = locked(V71, V71_SHA)
state = json.loads((STAGE / "MAIN-STATE.json").read_text(encoding="utf-8"))
start = (STAGE / "MAIN-START-HERE.md").read_text(encoding="utf-8")
roadmap = (HERE / "ROADMAP-V71-J1-TORSOR.md").read_text(encoding="utf-8")

assert v69["d2_verdict"] == "OPEN_ONE_BIT"
assert len(v69["transport_reduction"]["candidate_transports_contact_to_marked"]) == 2
assert v71["cv_cocycle"]["xi_rho"] == "Tr"
assert v71["cv_cocycle"]["cocycle_bits_in_fixed_basis"] == [0, 1]
assert v71["credit_firewall"]["identity_vs_shear_selected"] is False
assert v71["credit_firewall"]["j1_translation_torsor_materialized"] is False

# Successor-safe historical replay: live state may have advanced to V73+,
# but the V71 one-bit boundary and global credit firewalls must remain preserved.
assert state["stage33_progress"] == "6/11"
assert state["current_exact_frontier"]["J1_marked_kc_coordinate_candidates_f2"] == [[0, 1], [1, 1]]
assert state["current_exact_frontier"]["J1_marked_kc_remaining_ambiguity_bits"] == 1
assert state["current_exact_frontier"]["contact_to_marked_transport_candidates"] == ["identity", "shear_fixing_u1"]
assert state["firewalls"]["stage33_12_closed_exact"] is False
assert state["firewalls"]["stage33_13_released"] is False
assert state["firewalls"]["merge_allowed"] is False
assert "V71" in start and "V71" in roadmap
assert "S33-PW07" in start and "S33-PW04" in start
assert "MERGE_ALLOWED=false" in roadmap

print(json.dumps({
    "success": True,
    "marker": "V72_HISTORICAL_V71_FRONTIER_REPLAY_SUCCESSOR_SAFE",
    "v71_canonical_sha256": V71_SHA,
    "remaining_transport_bits": 1,
    "live_frontier": state["authority_sync"]["frontier_authority"],
    "merge_allowed": False
}, sort_keys=True))
