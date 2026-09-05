#!/usr/bin/env python3
"""Verify V86: live Stage33 startup/state/roadmap alignment at the V85 frontier."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
STATE = STAGE / "MAIN-STATE.json"
START = STAGE / "MAIN-START-HERE.md"
ROADMAP = HERE / "ROADMAP-V71-J1-TORSOR.md"
V85 = HERE / "e3-coordinate-conjugate-sign-quotient-route-freeze-v85.json"

STATE_SHA = "353a1e27f667d2f5a70e5ff1dbee23ec3c007e1a1176fdddd8eb58c97014879f"
V85_SHA = "6f63d8814d87d1e9ae4810fb9a5a3d09c9f37f0d3bd2875ddf7f4dce43c82159"
V85_BLOB = "2b667e699448d2f910e16c5a4c93532fe390f893"
NEXT = "CONSTRUCT_NON_COORDINATE_CONJUGATE_FULL_SURFACE_CECH_OR_ACTUAL_GERSTEN_DATUM_WITH_EXACT_PROPER14_BRAUER_IMAGE_MASK20"
ACTIVE = "NON_COORDINATE_CONJUGATE_FULL_SURFACE_CECH_OR_ACTUAL_GERSTEN_DATUM_WITH_EXACT_PROPER14_BRAUER_IMAGE_MASK20"


def csha(obj):
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha(path: Path):
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


state = json.loads(STATE.read_text(encoding="utf-8"))
v85 = json.loads(V85.read_text(encoding="utf-8"))
assert state["canonical_sha256"] == STATE_SHA == csha(state)
assert v85["canonical_sha256"] == V85_SHA == csha(v85)
assert blob_sha(V85) == V85_BLOB
assert v85["next_exact_leaf"] == NEXT
assert v85["finite_group_replay"]["generator_count"] == 9
assert v85["finite_group_replay"]["mask25_orbit_masks_decimal"] == [25]
assert v85["sign_quotient_consequence"]["coordinate_conjugate_B1_B2_B3_image_masks_decimal"] == [0, 25]
assert v85["sign_quotient_consequence"]["e3_target_mask_decimal"] == 20
assert v85["sign_quotient_consequence"]["e3_in_any_coordinate_conjugate_sign_quotient_image"] is False
assert v85["exact_boundary"]["global_H2_mu2_nonexistence_claim"] is False

assert state["schema"] == "STAGE33_MAIN_COMPACT_STATE_V27_V85_COORDINATE_CONJUGATE_GYSIN_FAMILY_FROZEN_NONCOORDINATE_CECH_GERSTEN_ACTIVE"
assert state["stage33_progress"] == "6/11"
assert state["authority_sync"]["frontier_authority"] == "V85_COORDINATE_CONJUGATE_SIGN_QUOTIENT_ROUTE_FREEZE"
assert state["branch_exact_frontier_authority"].endswith("e3-coordinate-conjugate-sign-quotient-route-freeze-v85.json")
assert state["current"]["active_missing_interface"] == ACTIVE
assert state["current"]["next_exact_leaf"] == NEXT

f = state["current_exact_frontier"]
assert f["e3_b1_image_masks_decimal"] == [0, 25]
assert f["e3_b1_route_frozen"] is True
assert f["e3_coordinate_automorphism_generator_count"] == 9
assert f["e3_coordinate_conjugate_mask25_orbit_size"] == 1
assert f["e3_coordinate_conjugate_mask25_orbit_masks_decimal"] == [25]
assert f["e3_coordinate_conjugate_sign_quotient_image_masks_decimal"] == [0, 25]
assert f["e3_coordinate_conjugate_sign_quotient_routes_frozen"] is True
assert f["e3_in_any_coordinate_conjugate_sign_quotient_image"] is False
assert f["e3_proper14_mask_decimal"] == 20
assert f["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
assert f["e3_global_H2_mu2_nonexistence_claim"] is False

assert state["locked_facts"]["v85"]["sha256"] == V85_SHA
assert state["locked_facts"]["v85"]["blob_sha1"] == V85_BLOB
assert state["resolved_investigations"]["e3_coordinate_conjugate_sign_quotient_family"].startswith("CLOSED_EXACT_V85")
assert state["resolved_investigations"]["e3_full_surface_cech_realization"].startswith("OPEN_V85")
assert state["anti_loop_policy"]["do_not_reopen_coordinate_conjugate_sign_quotient_gysin_after_v85"] is True
assert state["anti_loop_policy"]["do_not_promote_coordinate_conjugate_route_family_failure_to_global_H2_mu2_nonexistence"] is True
assert state["discovery_policy"]["current_arsenal_cards"] == ["S33-PW04", "S33-PW07", "S33-PW08"]
assert state["execution_gate"]["advance_allowed"] is True
assert state["firewalls"]["stage33_12_closed_exact"] is False
assert state["firewalls"]["stage33_13_released"] is False
assert state["firewalls"]["merge_allowed"] is False

start = START.read_text(encoding="utf-8")
roadmap = ROADMAP.read_text(encoding="utf-8")
assert "Current exact frontier: V85" in start
assert "orbit(mask25)={25}" in start
assert ACTIVE in start
assert NEXT in start
assert "S33-PW04" in start and "S33-PW07" in start and "S33-PW08" in start
assert "CURRENT_LOCKED_FRONTIER=V61_THROUGH_V85" in roadmap
assert "CURRENT_LEAF=E3_NON_COORDINATE_CONJUGATE_FULL_SURFACE_CECH_OR_ACTUAL_GERSTEN_MASK20" in roadmap
assert "D6 — coordinate-conjugate sign-quotient family — PASS/NEGATIVE V85" in roadmap
assert "E3-A2.4C — non-coordinate-conjugate full-surface Cech/Gersten realization — CURRENT V85" in roadmap
assert NEXT in roadmap
assert "MERGE_ALLOWED=false" in roadmap

print(json.dumps({
    "success": True,
    "marker": "V86_STAGE33_V85_FRONTIER_STATE_ALIGNMENT_COMPLETE",
    "state_canonical_sha256": STATE_SHA,
    "v85_canonical_sha256": V85_SHA,
    "coordinate_conjugate_sign_quotient_routes_frozen": True,
    "coordinate_automorphism_orbit_masks": [25],
    "e3_target_mask": 20,
    "global_H2_mu2_nonexistence_claim": False,
    "current_leaf": ACTIVE,
    "advance_allowed": True,
    "merge_allowed": False,
}, sort_keys=True))
