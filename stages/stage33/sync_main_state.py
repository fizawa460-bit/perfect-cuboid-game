#!/usr/bin/env python3
"""Generate/check Stage33 MAIN compact state at the exact V80 outside-B1 Cech frontier."""
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

CONTROLLER_SCHEMA = "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V62_ARSENAL_FIRST_BOUNDED_SEARCH_ACTIVE"
CONTROLLER_SHA = "18d8aa4e0ab7a946f5ae5205de2cfddc4b55f867338e92242e5db7cac6f87554"
STATE_SHA = "bb0390d9df485722c24dbbd56168a917831adf13ef2565e8de98cd603acf7073"
V79_SHA = "29acced201721df4ad65bda071914bf71a4b5d7098dce86a541cdd41f2085921"
V80_SHA = "d75a7bbe14f5194b91a1411a372ce4b64982331d04da23d044591422fb37ccbf"


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
    assert v79["canonical_sha256"] == V79_SHA == csha(v79)
    assert v80["canonical_sha256"] == V80_SHA == csha(v80)
    assert v79["e3_membership"]["in_image"] is False
    assert v80["v79_promotion"]["b1_image_masks_decimal"] == [0, 25]
    assert v80["v79_promotion"]["e3_target_mask_decimal"] == 20
    assert v80["rewired_current_leaf"]["genuine_full_surface_H2_mu2_lift_for_e3"] is False

    state = json.loads(OUT.read_text(encoding="utf-8"))
    assert state["canonical_sha256"] == STATE_SHA == csha(state)
    assert state["controller_projection_canonical_sha256"] == CONTROLLER_SHA
    assert state["schema"] == "STAGE33_MAIN_COMPACT_STATE_V26_V80_B1_ROUTE_FROZEN_OUTSIDE_CECH_ACTIVE"
    assert state["authority_sync"]["frontier_authority"] == "V80_B1_ROUTE_FREEZE_OUTSIDE_CECH_REWIRE"
    assert state["branch_exact_frontier_authority"].endswith("e3-b1-route-freeze-and-outside-cech-rewire-v80.json")
    assert state["current"]["active_missing_interface"] == "SOURCE_SPECIFIC_FULL_SURFACE_CECH_H2_MU2_REALIZATION_FOR_E3_MASK20_OUTSIDE_B1_ROUTE"
    assert state["current_exact_frontier"]["e3_b1_matrix_column_masks_decimal"] == [0, 25, 0, 25]
    assert state["current_exact_frontier"]["e3_b1_image_masks_decimal"] == [0, 25]
    assert state["current_exact_frontier"]["e3_b1_membership"] is False
    assert state["current_exact_frontier"]["e3_b1_route_frozen"] is True
    assert state["current_exact_frontier"]["e3_global_H2_mu2_nonexistence_claim"] is False
    assert state["current_exact_frontier"]["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
    assert state["current_exact_frontier"]["j1_geometric_brauer_os_class"] == "ZERO"
    assert state["locked_facts"]["v79"]["sha256"] == V79_SHA
    assert state["locked_facts"]["v80"]["sha256"] == V80_SHA
    assert state["resolved_investigations"]["e3_b1_route_membership"].startswith("CLOSED_EXACT_V79")
    assert state["resolved_investigations"]["e3_full_surface_cech_realization"].startswith("OPEN_V80")
    assert state["anti_loop_policy"]["do_not_reopen_b1_gysin_membership_after_v79"] is True
    assert state["anti_loop_policy"]["do_not_promote_b1_nonmembership_to_global_H2_mu2_nonexistence"] is True
    assert state["execution_gate"]["advance_allowed"] is True
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
        "b1_route_frozen": True,
        "e3_mask20_in_b1_image": False,
        "advance_allowed": True,
        "merge_allowed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
