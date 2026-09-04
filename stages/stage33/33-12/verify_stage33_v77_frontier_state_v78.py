#!/usr/bin/env python3
"""Verify Stage33 V78 live startup/state/roadmap alignment at V77."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
STATE = STAGE / "MAIN-STATE.json"
START = STAGE / "MAIN-START-HERE.md"
ROADMAP = STAGE / "ROADMAP-33-12-V71-J1-TORSOR.md"
V77 = HERE / "e3-b1-c22-j1-xalpha-kernel-correction-v77.json"

STATE_SHA = "f13dca2b0e254eb1b8e5a4c72b495886718e019167b87bf4d5a2a7452f3cee37"
V77_SHA = "d2f803ab0cb394389c1fedf8f94e237ce82702743d0240a4f4b2fe73a44d5e98"
V77_BLOB = "bfc54650fdc7885664cdfcb1533cb9a1e711c5a5"


def csha(obj):
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


state = json.loads(STATE.read_text(encoding="utf-8"))
v77 = json.loads(V77.read_text(encoding="utf-8"))
assert state["canonical_sha256"] == STATE_SHA == csha(state)
assert blob_sha(V77) == V77_BLOB
assert v77["canonical_sha256"] == V77_SHA == csha(v77)

assert state["schema"] == "STAGE33_MAIN_COMPACT_STATE_V25_V77_J1_XALPHA_ZERO_COLUMN3_REPAIR_ACTIVE"
assert state["stage33_progress"] == "6/11"
assert state["authority_sync"]["frontier_authority"] == "V77_J1_XALPHA_KERNEL_CORRECTION"
assert state["branch_exact_frontier_authority"].endswith("e3-b1-c22-j1-xalpha-kernel-correction-v77.json")
assert state["current"]["active_missing_interface"] == "LAMBDA_A_LITERAL_TO_PROPER14_BRAUER_BINDING_AFTER_J1_XALPHA_ZERO"
assert state["current_exact_frontier"]["j1_E2_cocycle_nonzero"] is True
assert state["current_exact_frontier"]["j1_H1_E_class"] == "ZERO"
assert state["current_exact_frontier"]["j1_geometric_brauer_os_class"] == "ZERO"
assert state["current_exact_frontier"]["j1_xalpha_image_exact"] is True
assert state["current_exact_frontier"]["j1_xalpha_brauer_quotient_basis"] == ["J2", "q1"]
assert state["current_exact_frontier"]["j1_twisted_kernel_minimum_norm"] == 4
assert state["current_exact_frontier"]["j1_minimum_norm_4_selects_u2"] is False
assert state["current_exact_frontier"]["J1_marked_kc_candidate_gate_applicable"] is False
assert state["current_exact_frontier"]["contact_to_marked_transport_gate_applicable_to_J1_brauer_image"] is False
assert state["current_exact_frontier"]["e3_b1_column3_marked_coordinate_materialized"] is False
assert state["locked_facts"]["v77"]["sha256"] == V77_SHA
assert state["resolved_investigations"]["j1_xalpha_kernel"].startswith("CLOSED_EXACT_V77")
assert state["resolved_investigations"]["proper14_column3"].startswith("OPEN_REPAIR_AFTER_V77")
assert state["anti_loop_policy"]["do_not_revive_v65_nonzero_j1_marked_kc_gate_after_xalpha_kernel_correction"] is True
assert state["execution_gate"]["advance_allowed"] is True
assert state["firewalls"]["stage33_12_closed_exact"] is False
assert state["firewalls"]["stage33_13_released"] is False
assert state["firewalls"]["merge_allowed"] is False

assert v77["xalpha_repair_replay"]["J1_in_xalpha_image_exact"] is True
assert v77["cohomological_correction"]["J1_geometric_brauer_class"] == "ZERO"
assert v77["torsor_lattice_consequence"]["T_X_J1_minimum_norm"] == 4
assert v77["torsor_lattice_consequence"]["minimum_norm_4_means_u2_here"] is False
assert v77["supersession"]["v65_J1_candidates_u2_u1plusu2_valid_for_actual_Brauer_OS_class"] is False
assert v77["proper14_boundary"]["column3_marked_coordinate_materialized"] is False

start = START.read_text(encoding="utf-8")
roadmap = ROADMAP.read_text(encoding="utf-8")
assert "Current exact frontier: V77" in start
assert "zero in the geometric Brauer/Ogg-Shafarevich quotient" in start
assert "literal `lambda_A` -> proper14 column-3 binding" in start
assert "Do not reopen the 4/12 minimum-norm discriminator" in start
assert "CURRENT_LOCKED_FRONTIER=V61_THROUGH_V77_WITH_V65_V69_V75_HISTORICAL_SUPERSESSION" in roadmap
assert "CURRENT_LEAF=D4_REPAIR_LITERAL_LAMBDA_A_TO_PROPER14_COLUMN3_AFTER_J1_XALPHA_ZERO" in roadmap
assert "D2.2 — minimum-norm discriminator — RETIRED V77" in roadmap
assert "D4 — repair marked proper14 column 3 — CURRENT" in roadmap
assert "MERGE_ALLOWED=false" in roadmap

print(json.dumps({
    "success": True,
    "marker": "V78_STAGE33_V77_FRONTIER_STATE_ALIGNMENT_COMPLETE",
    "state_canonical_sha256": STATE_SHA,
    "v77_canonical_sha256": V77_SHA,
    "j1_geometric_brauer_os_class": "ZERO",
    "current_leaf": state["current"]["active_missing_interface"],
    "advance_allowed": True,
    "merge_allowed": False,
}, sort_keys=True))
