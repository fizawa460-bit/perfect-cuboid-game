#!/usr/bin/env python3
"""Generate/check Stage33 MAIN compact state at the exact V85 frontier."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parent
D = H / "33-12"
OUT = H / "MAIN-STATE.json"
CONTROLLER = H / "controller.json"
V79 = D / "e3-b1-full-gysin-matrix-xalpha-correction-v79.json"
V80 = D / "e3-b1-route-freeze-and-outside-cech-rewire-v80.json"
V85 = D / "e3-coordinate-conjugate-sign-quotient-route-freeze-v85.json"

CONTROLLER_SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE"
CONTROLLER_SHA = "02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773"
STATE_SHA = "8e4289aa08a83ea4f6ef5624803d2c5049daf8248efd03f1408844b162e96c0b"
V79_SHA = "29acced201721df4ad65bda071914bf71a4b5d7098dce86a541cdd41f2085921"
V80_SHA = "d75a7bbe14f5194b91a1411a372ce4b64982331d04da23d044591422fb37ccbf"
V85_SHA = "6f63d8814d87d1e9ae4810fb9a5a3d09c9f37f0d3bd2875ddf7f4dce43c82159"
NEXT = "CONSTRUCT_NON_COORDINATE_CONJUGATE_FULL_SURFACE_CECH_OR_ACTUAL_GERSTEN_DATUM_WITH_EXACT_PROPER14_BRAUER_IMAGE_MASK20"
ACTIVE = "NON_COORDINATE_CONJUGATE_FULL_SURFACE_CECH_OR_ACTUAL_GERSTEN_DATUM_WITH_EXACT_PROPER14_BRAUER_IMAGE_MASK20"


def csha(obj):
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    controller = json.loads(CONTROLLER.read_text(encoding="utf-8"))
    cb = dict(controller)
    claimed_controller = cb.pop("projection_canonical_sha256")
    assert controller["schema"] == CONTROLLER_SCHEMA
    assert claimed_controller == CONTROLLER_SHA == hashlib.sha256(
        json.dumps(cb, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    assert controller["merge_allowed"] is False
    assert controller["execution"]["merge_allowed"] is False

    v79 = json.loads(V79.read_text(encoding="utf-8"))
    v80 = json.loads(V80.read_text(encoding="utf-8"))
    v85 = json.loads(V85.read_text(encoding="utf-8"))
    assert v79["canonical_sha256"] == V79_SHA == csha(v79)
    assert v80["canonical_sha256"] == V80_SHA == csha(v80)
    assert v85["canonical_sha256"] == V85_SHA == csha(v85)
    assert v85["finite_group_replay"]["generator_count"] == 9
    assert v85["finite_group_replay"]["mask25_orbit_masks_decimal"] == [25]
    assert v85["sign_quotient_consequence"]["coordinate_conjugate_B1_B2_B3_image_masks_decimal"] == [0, 25]
    assert v85["sign_quotient_consequence"]["e3_target_mask_decimal"] == 20
    assert v85["sign_quotient_consequence"]["e3_in_any_coordinate_conjugate_sign_quotient_image"] is False
    assert v85["exact_boundary"]["global_H2_mu2_nonexistence_claim"] is False
    assert v85["next_exact_leaf"] == NEXT

    state = json.loads(OUT.read_text(encoding="utf-8"))
    assert state["canonical_sha256"] == STATE_SHA == csha(state)
    assert state["controller_projection_canonical_sha256"] == CONTROLLER_SHA
    assert state["schema"] == "STAGE33_MAIN_COMPACT_STATE_V27_V85_COORDINATE_CONJUGATE_GYSIN_FAMILY_FROZEN_NONCOORDINATE_CECH_GERSTEN_ACTIVE"
    assert state["authority_sync"]["frontier_authority"] == "V85_COORDINATE_CONJUGATE_SIGN_QUOTIENT_ROUTE_FREEZE"
    assert state["branch_exact_frontier_authority"].endswith("e3-coordinate-conjugate-sign-quotient-route-freeze-v85.json")
    assert state["current"]["active_missing_interface"] == ACTIVE
    assert state["current"]["next_exact_leaf"] == NEXT
    f = state["current_exact_frontier"]
    assert f["e3_b1_image_masks_decimal"] == [0, 25]
    assert f["e3_b1_membership"] is False
    assert f["e3_b1_route_frozen"] is True
    assert f["e3_coordinate_automorphism_generator_count"] == 9
    assert f["e3_coordinate_conjugate_mask25_orbit_size"] == 1
    assert f["e3_coordinate_conjugate_mask25_orbit_masks_decimal"] == [25]
    assert f["e3_coordinate_conjugate_sign_quotient_image_masks_decimal"] == [0, 25]
    assert f["e3_coordinate_conjugate_sign_quotient_routes_frozen"] is True
    assert f["e3_in_any_coordinate_conjugate_sign_quotient_image"] is False
    assert f["e3_global_H2_mu2_nonexistence_claim"] is False
    assert f["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
    assert f["j1_geometric_brauer_os_class"] == "ZERO"
    assert state["locked_facts"]["v79"]["sha256"] == V79_SHA
    assert state["locked_facts"]["v80"]["sha256"] == V80_SHA
    assert state["locked_facts"]["v85"]["sha256"] == V85_SHA
    assert state["resolved_investigations"]["e3_coordinate_conjugate_sign_quotient_family"].startswith("CLOSED_EXACT_V85")
    assert state["resolved_investigations"]["e3_full_surface_cech_realization"].startswith("OPEN_V85")
    assert state["anti_loop_policy"]["do_not_reopen_coordinate_conjugate_sign_quotient_gysin_after_v85"] is True
    assert state["anti_loop_policy"]["do_not_promote_coordinate_conjugate_route_family_failure_to_global_H2_mu2_nonexistence"] is True
    assert state["discovery_policy"]["current_arsenal_cards"] == ["S33-PW04", "S33-PW07", "S33-PW08"]
    assert state["execution_gate"]["advance_allowed"] is True
    assert state["firewalls"]["stage33_12_closed_exact"] is False
    assert state["firewalls"]["stage33_13_released"] is False
    assert state["firewalls"]["merge_allowed"] is False
    assert state["stage33_progress"] == "6/11"

    if not args.check:
        OUT.write_text(json.dumps(state, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")

    print(json.dumps({
        "success": True,
        "mode": "check" if args.check else "write",
        "canonical_sha256": STATE_SHA,
        "frontier": state["authority_sync"]["frontier_authority"],
        "current_leaf": state["current"]["active_missing_interface"],
        "coordinate_conjugate_sign_quotient_routes_frozen": True,
        "e3_target_mask": 20,
        "global_H2_mu2_nonexistence_claim": False,
        "advance_allowed": True,
        "merge_allowed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
