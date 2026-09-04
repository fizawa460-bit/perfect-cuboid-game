#!/usr/bin/env python3
"""Verify Stage33 V74 startup/state/roadmap alignment at the V73 J1 torsor frontier."""
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
V73 = HERE / "e3-b1-c22-j1-translation-torsor-v73.json"

STATE_SHA = "93e2403e49faa69e4c6e92499ae5164947a3626630f95e4d42b653f5446afba2"
V69_BLOB = "77638f2f3afb2dc6445f5130addcd52e88bc5767"
V73_BLOB = "277ec4bfd86a118b25e45632ce4a02fe3af87cc1"
V73_SHA = "b6a8dd83cd83547525e8ff328cccc1572791c52bea6061137c2bc59a134fa09d"

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
assert git_blob_sha(V73) == V73_BLOB
v73 = locked(V73, V73_SHA)

assert state["schema"] == "STAGE33_MAIN_COMPACT_STATE_V23_V73_J1_TRANSLATION_TORSOR_KERNEL_ACTIVE"
assert state["authority_sync"]["frontier_authority"] == "V73_J1_TRANSLATION_TORSOR"
assert state["branch_exact_frontier_authority"].endswith("e3-b1-c22-j1-translation-torsor-v73.json")
assert state["current"]["active_missing_interface"] == "J1_TWISTED_KERNEL_MINIMUM_NORM_4_OR_12"
assert state["current"]["next_exact_leaf"] == "D2_2_COMPUTE_J1_TORSOR_NS_COMPONENT_GLUE_OR_EQUIVALENT_INTEGRAL_TWISTED_KERNEL_FINGERPRINT"
assert state["current_exact_frontier"]["J1_marked_kc_coordinate_candidates_f2"] == [[0, 1], [1, 1]]
assert state["current_exact_frontier"]["J1_marked_kc_remaining_ambiguity_bits"] == 1
assert state["current_exact_frontier"]["contact_to_marked_transport_candidates"] == ["identity", "shear_fixing_u1"]
assert state["current_exact_frontier"]["j1_translation_torsor_materialized"] is True
assert state["current_exact_frontier"]["j1_translation_torsor_equation"].endswith("d=f1")
assert state["current_exact_frontier"]["j1_translation_torsor_splitting_field"] == "Kgeom(sqrt(f1))"
assert state["current_exact_frontier"]["j1_translation_torsor_bisection_branch_points"] == ["r1=1+sqrt(2)", "r4=1-sqrt(2)"]
assert state["current_exact_frontier"]["j1_translation_torsor_jacobian"] == "E: y^2=x*(x^2+a*x+b)"
assert state["current_exact_frontier"]["j1_twisted_kernel_minimum_norm_materialized"] is False
assert state["execution_gate"]["advance_allowed"] is True
assert state["firewalls"]["stage33_12_closed_exact"] is False
assert state["firewalls"]["stage33_13_released"] is False
assert state["firewalls"]["merge_allowed"] is False

assert v69["d2_verdict"] == "OPEN_ONE_BIT"
assert v73["translation_torsor"]["twisting_squareclass"] == "d=f1"
assert v73["translation_torsor"]["jacobian"] == "E: y^2=x*(x^2+a*x+b)"
assert v73["next_kernel_contract"]["allowed_minimum_norm_outcomes"] == [4, 12]
assert v73["credit_firewall"]["j1_translation_torsor_materialized"] is True
assert v73["credit_firewall"]["j1_twisted_kernel_minimum_norm_materialized"] is False
assert v73["credit_firewall"]["j1_marked_kc_coordinate_selected"] is False
assert v73["credit_firewall"]["identity_vs_shear_selected"] is False

start = START.read_text(encoding="utf-8")
roadmap = ROADMAP.read_text(encoding="utf-8")
assert "Current exact frontier: V73" in start
assert "D2.1 is PASS at V73" in start
assert "current constructive leaf is D2.2" in start
assert "S33-PW07" in start and "S33-PW04" in start
assert "CURRENT_LOCKED_FRONTIER=V61_THROUGH_V73_WITH_V68_V69_TRANSPORT_REDUCTION" in roadmap
assert "CURRENT_LEAF=D2_2_COMPUTE_J1_TWISTED_KERNEL_MINIMUM_NORM" in roadmap
assert "D2.1 — materialize the J1 translation torsor — PASS V73" in roadmap
assert "D2.2 — compute an independent J1 twisted-kernel fingerprint — CURRENT" in roadmap
assert "`4` => `J1 -> u2` => shear transport" in roadmap
assert "`12` => `J1 -> u1+u2` => identity transport" in roadmap
assert "MERGE_ALLOWED=false" in roadmap

print(json.dumps({
    "success": True,
    "marker": "V74_STAGE33_V73_FRONTIER_STATE_ALIGNMENT_COMPLETE",
    "state_canonical_sha256": STATE_SHA,
    "v73_canonical_sha256": V73_SHA,
    "remaining_transport_bits": 1,
    "current_leaf": "J1_TWISTED_KERNEL_MINIMUM_NORM_4_OR_12",
    "advance_allowed": True,
    "merge_allowed": False
}, sort_keys=True))
