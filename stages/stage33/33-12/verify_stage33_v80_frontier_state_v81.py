#!/usr/bin/env python3
"""Verify V81: live startup/state/roadmap alignment at the V80 outside-B1 frontier."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
STATE = STAGE / "MAIN-STATE.json"
START = STAGE / "MAIN-START-HERE.md"
ROADMAP = STAGE / "ROADMAP-33-12-V71-J1-TORSOR.md"
V79 = HERE / "e3-b1-full-gysin-matrix-xalpha-correction-v79.json"
V80 = HERE / "e3-b1-route-freeze-and-outside-cech-rewire-v80.json"

STATE_SHA = "bb0390d9df485722c24dbbd56168a917831adf13ef2565e8de98cd603acf7073"
V79_SHA = "29acced201721df4ad65bda071914bf71a4b5d7098dce86a541cdd41f2085921"
V80_SHA = "d75a7bbe14f5194b91a1411a372ce4b64982331d04da23d044591422fb37ccbf"
V80_BLOB = "978828a81d11c00e9a53244e2ee2334b4e527250"


def csha(obj):
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha(path: Path):
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


state = json.loads(STATE.read_text())
v79 = json.loads(V79.read_text())
v80 = json.loads(V80.read_text())
assert state["canonical_sha256"] == STATE_SHA == csha(state)
assert v79["canonical_sha256"] == V79_SHA == csha(v79)
assert blob_sha(V80) == V80_BLOB
assert v80["canonical_sha256"] == V80_SHA == csha(v80)

assert state["schema"] == "STAGE33_MAIN_COMPACT_STATE_V26_V80_B1_ROUTE_FROZEN_OUTSIDE_CECH_ACTIVE"
assert state["stage33_progress"] == "6/11"
assert state["authority_sync"]["frontier_authority"] == "V80_B1_ROUTE_FREEZE_OUTSIDE_CECH_REWIRE"
assert state["branch_exact_frontier_authority"].endswith("e3-b1-route-freeze-and-outside-cech-rewire-v80.json")
assert state["current"]["active_missing_interface"] == "SOURCE_SPECIFIC_FULL_SURFACE_CECH_H2_MU2_REALIZATION_FOR_E3_MASK20_OUTSIDE_B1_ROUTE"
assert state["current"]["next_exact_leaf"] == v80["rewired_current_leaf"]["next_exact_leaf"]

f = state["current_exact_frontier"]
assert f["e3_b1_matrix_materialized"] is True
assert f["e3_b1_matrix_shape"] == [14, 4]
assert f["e3_b1_matrix_column_masks_decimal"] == [0, 25, 0, 25]
assert f["e3_b1_matrix_rank_f2"] == 1
assert f["e3_b1_image_masks_decimal"] == [0, 25]
assert f["e3_b1_membership"] is False
assert f["e3_b1_route_frozen"] is True
assert f["e3_proper14_mask_decimal"] == 20
assert f["e3_b1_column3_proper14_mask_decimal"] == 0
assert f["e3_b1_column3_proper14_brauer_image_materialized"] is True
assert f["e3_marked_picard_adjoint_candidate_materialized"] is True
assert f["e3_literal_cech_preimage_materialized"] is False
assert f["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
assert f["e3_global_H2_mu2_nonexistence_claim"] is False

assert state["locked_facts"]["v79"]["sha256"] == V79_SHA
assert state["locked_facts"]["v80"]["sha256"] == V80_SHA
assert state["resolved_investigations"]["b1_full_14x4_gysin_matrix"].startswith("CLOSED_EXACT_V79")
assert state["resolved_investigations"]["e3_b1_route_membership"].startswith("CLOSED_EXACT_V79")
assert state["resolved_investigations"]["e3_full_surface_cech_realization"].startswith("OPEN_V80")
assert state["anti_loop_policy"]["do_not_reopen_b1_gysin_membership_after_v79"] is True
assert state["anti_loop_policy"]["do_not_promote_b1_nonmembership_to_global_H2_mu2_nonexistence"] is True
assert state["anti_loop_policy"]["do_not_relabel_j2_literal_cech_as_e3"] is True
assert state["execution_gate"]["advance_allowed"] is True
assert state["firewalls"]["stage33_12_closed_exact"] is False
assert state["firewalls"]["stage33_13_released"] is False
assert state["firewalls"]["merge_allowed"] is False

start = START.read_text()
roadmap = ROADMAP.read_text()
assert "Current exact frontier: V80" in start
assert "B1 branch-Gysin route is **exactly frozen for e3**" in start
assert "SOURCE_SPECIFIC_FULL_SURFACE_CECH_H2_MU2_REALIZATION_FOR_E3_MASK20_OUTSIDE_B1_ROUTE" in start
assert "S33-PW04" in start and "S33-PW07" in start and "S33-PW08" in start
assert "CURRENT_LOCKED_FRONTIER=V61_THROUGH_V80_WITH_V65_V69_V75_HISTORICAL_SUPERSESSION_AND_V79_B1_FREEZE" in roadmap
assert "CURRENT_LEAF=E3_SOURCE_SPECIFIC_FULL_SURFACE_CECH_H2_MU2_OUTSIDE_FROZEN_B1_ROUTE" in roadmap
assert "D5 — B1 14x4 and mask20 solve — PASS/NEGATIVE V79" in roadmap
assert "E3-A2.4C — source-specific full-surface Cech/Gersten realization — CURRENT V80" in roadmap
assert "MERGE_ALLOWED=false" in roadmap

print(json.dumps({
    "success": True,
    "marker": "V81_STAGE33_V80_FRONTIER_STATE_ALIGNMENT_COMPLETE",
    "state_canonical_sha256": STATE_SHA,
    "v80_canonical_sha256": V80_SHA,
    "b1_route_frozen": True,
    "e3_mask20_in_b1_image": False,
    "current_leaf": state["current"]["active_missing_interface"],
    "advance_allowed": True,
    "merge_allowed": False,
}, sort_keys=True))
