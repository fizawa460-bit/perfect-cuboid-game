#!/usr/bin/env python3
"""Verify Stage33 V72 startup/state/roadmap alignment at the V71 J1 torsor frontier."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
STATE = STAGE / "MAIN-STATE.json"
START = STAGE / "MAIN-START-HERE.md"
ROADMAP = STAGE / "ROADMAP-33-12-V71-J1-TORSOR.md"
V69 = HERE / "e3-b1-c22-j1-marked-kc-one-bit-transport-gate-v69.json"
V71 = HERE / "e3-b1-c22-j1-cv-e2-cocycle-v71.json"

STATE_SHA = "bc57b431eec982d1a9dd95f39f8777351425485ac266fc60c45198b9b79e7c06"
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

state = locked(STATE, STATE_SHA)
assert git_blob_sha(V69) == V69_BLOB
v69 = json.loads(V69.read_text(encoding="utf-8"))
v71 = locked(V71, V71_SHA)

assert state["schema"] == "STAGE33_MAIN_COMPACT_STATE_V22_V71_J1_CV_COCYCLE_TORSOR_ACTIVE"
assert state["authority_sync"]["frontier_authority"] == "V71_J1_SPECIFIC_CV_E2_COCYCLE"
assert state["branch_exact_frontier_authority"].endswith("e3-b1-c22-j1-cv-e2-cocycle-v71.json")
assert state["current"]["active_missing_interface"] == "J1_TRANSLATION_TORSOR_AND_TWISTED_KERNEL_FINGERPRINT"
assert state["current"]["next_exact_leaf"] == "D2_MATERIALIZE_J1_TRANSLATION_TORSOR_WITH_d_f1_THEN_COMPUTE_INDEPENDENT_MINIMUM_NORM_4_OR_12"
assert state["current_exact_frontier"]["J1_marked_kc_coordinate_candidates_f2"] == [[0, 1], [1, 1]]
assert state["current_exact_frontier"]["J1_marked_kc_remaining_ambiguity_bits"] == 1
assert state["current_exact_frontier"]["contact_to_marked_transport_candidates"] == ["identity", "shear_fixing_u1"]
assert state["current_exact_frontier"]["j1_cv_full_L_pair"] == "(f1,1)"
assert state["current_exact_frontier"]["j1_cv_cocycle_bits_in_fixed_E2_basis"] == [0, 1]
assert state["current_exact_frontier"]["j1_cv_translation_point"] == "Tr=(r,0)"
assert state["current_exact_frontier"]["j1_translation_torsor_materialized"] is False
assert state["current_exact_frontier"]["j1_twisted_kernel_minimum_norm_materialized"] is False
assert state["execution_gate"]["advance_allowed"] is True
assert state["execution_gate"]["stop_semantics"] == "LEAF_GATE_ONLY_NOT_ALGORITHM_EXHAUSTION"
assert state["firewalls"]["stage33_12_closed_exact"] is False
assert state["firewalls"]["stage33_13_released"] is False
assert state["firewalls"]["merge_allowed"] is False

assert v69["d2_verdict"] == "OPEN_ONE_BIT"
assert len(v69["transport_reduction"]["candidate_transports_contact_to_marked"]) == 2
assert v71["cv_cocycle"]["xi_rho"] == "Tr"
assert v71["cv_cocycle"]["cocycle_bits_in_fixed_basis"] == [0, 1]
assert v71["credit_firewall"]["identity_vs_shear_selected"] is False
assert v71["credit_firewall"]["j1_translation_torsor_materialized"] is False

start = START.read_text(encoding="utf-8")
roadmap = ROADMAP.read_text(encoding="utf-8")
assert "Current exact frontier: V71" in start
assert "ROADMAP-33-12-V71-J1-TORSOR.md" in start
assert "J1 translation torsor" in start
assert "S33-PW07" in start and "S33-PW04" in start
assert "CURRENT_LOCKED_FRONTIER=V61_THROUGH_V71_WITH_V68_V69_TRANSPORT_REDUCTION" in roadmap
assert "CURRENT_LEAF=D2_MATERIALIZE_J1_TRANSLATION_TORSOR_THEN_KERNEL_MINIMUM_NORM" in roadmap
assert "D2.1 — materialize the J1 translation torsor (current)" in roadmap
assert "D2.2 — compute an independent J1 twisted-kernel fingerprint" in roadmap
assert "`4` => `J1 -> u2` => shear transport" in roadmap
assert "`12` => `J1 -> u1+u2` => identity transport" in roadmap
assert "MERGE_ALLOWED=false" in roadmap

print(json.dumps({
    "success": True,
    "marker": "V72_STAGE33_V71_FRONTIER_STATE_ALIGNMENT_COMPLETE",
    "state_canonical_sha256": STATE_SHA,
    "v71_canonical_sha256": V71_SHA,
    "remaining_transport_bits": 1,
    "current_leaf": "J1_TRANSLATION_TORSOR_AND_TWISTED_KERNEL_FINGERPRINT",
    "advance_allowed": True,
    "merge_allowed": False,
}, sort_keys=True))
