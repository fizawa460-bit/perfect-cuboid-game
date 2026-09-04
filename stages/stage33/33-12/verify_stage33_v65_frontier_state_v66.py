#!/usr/bin/env python3
"""Verify Stage33 current startup/state/roadmap projection at the V65 one-bit frontier."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
STATE = STAGE / "MAIN-STATE.json"
START = STAGE / "MAIN-START-HERE.md"
ROADMAP = STAGE / "ROADMAP-33-12-V65-J1-DISCRIMINATOR.md"
V65 = HERE / "e3-b1-j1-marked-kc-discriminator-gate-v65.json"

STATE_SHA = "006a23e3cd06b842c65361a9804e1e088e7114c33a07f6faf6f0f2b469a4ed3c"
V65_SHA = "7ebef9a6182522f772f198d8c1572acc48cd8441f6158312d1f3f3f2c7fcc01c"

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

state = json.loads(STATE.read_text())
body = dict(state)
claimed = body.pop("canonical_sha256")
assert claimed == STATE_SHA == csha(body)

v65 = json.loads(V65.read_text())
vb = dict(v65)
vclaimed = vb.pop("canonical_sha256")
assert vclaimed == V65_SHA == csha(vb)

assert state["schema"] == "STAGE33_MAIN_COMPACT_STATE_V21_V65_J1_ONE_BIT_DISCRIMINATOR_ACTIVE"
assert state["current"]["active_missing_interface"] == "J1_MARKED_KC_IMAGE_ONE_BIT_DISCRIMINATOR"
assert state["current_exact_frontier"]["J1_marked_kc_coordinate_candidates_f2"] == [[0, 1], [1, 1]]
assert state["current_exact_frontier"]["J1_marked_kc_remaining_ambiguity_bits"] == 1
assert state["authority_sync"]["controller_current_leaf_projection_synchronized"] is False
assert state["authority_sync"]["frontier_authority"] == "V65_J1_ONE_BIT_DISCRIMINATOR_GATE"
assert state["execution_gate"]["advance_allowed"] is True
assert state["execution_gate"]["stop_semantics"] == "LEAF_GATE_ONLY_NOT_ALGORITHM_EXHAUSTION"
assert state["firewalls"]["stage33_12_closed_exact"] is False
assert state["firewalls"]["stage33_13_released"] is False
assert state["firewalls"]["merge_allowed"] is False

start = START.read_text()
roadmap = ROADMAP.read_text()
assert "STOP` at V65 means **leaf gate only, not algorithm exhaustion**" in start
assert "ROADMAP-33-12-V65-J1-DISCRIMINATOR.md" in start
assert "S33-PW04" in start and "S33-PW07" in start
assert "CURRENT_LOCKED_FRONTIER=V61_THROUGH_V65" in roadmap
assert "CURRENT_LEAF=RESOLVE_J1_MARKED_KC_ONE_BIT" in roadmap
assert "u2 -> 4" in roadmap and "u1+u2 -> 12" in roadmap
assert "D1 — exact second transport column" in roadmap
assert "D2 — independent J1 source fingerprint" in roadmap
assert "D3 — automorphism-equivariant discriminator" in roadmap
assert "MERGE_ALLOWED=false" in roadmap

print(json.dumps({
    "success": True,
    "marker": "V66_STAGE33_V65_FRONTIER_STATE_ALIGNMENT_COMPLETE",
    "state_canonical_sha256": STATE_SHA,
    "v65_canonical_sha256": V65_SHA,
    "advance_allowed": True,
    "stop_semantics": "LEAF_GATE_ONLY_NOT_ALGORITHM_EXHAUSTION",
    "merge_allowed": False
}, sort_keys=True))
