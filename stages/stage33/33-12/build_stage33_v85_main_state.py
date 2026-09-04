#!/usr/bin/env python3
"""Build the minimal V85 successor of the exact V80 Stage33 MAIN state.

This is a deterministic migration helper.  It preserves every historical V80
field unless V85 materially supersedes that field, then prints the complete
canonical V85 state for review/application.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

H = Path(__file__).resolve().parent.parent
D = H / "33-12"
STATE = H / "MAIN-STATE.json"
V85 = D / "e3-coordinate-conjugate-sign-quotient-route-freeze-v85.json"

OLD_STATE_SHA = "bb0390d9df485722c24dbbd56168a917831adf13ef2565e8de98cd603acf7073"
V85_SHA = "6f63d8814d87d1e9ae4810fb9a5a3d09c9f37f0d3bd2875ddf7f4dce43c82159"
V85_BLOB = "2b667e699448d2f910e16c5a4c93532fe390f893"
V84_BLOB = "e9c7e81cc59fb5203482071208d25ff1447edeb2"


def csha(obj):
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


state = json.loads(STATE.read_text(encoding="utf-8"))
assert state["canonical_sha256"] == OLD_STATE_SHA == csha(state)
v85 = json.loads(V85.read_text(encoding="utf-8"))
assert v85["canonical_sha256"] == V85_SHA == csha(v85)
assert v85["finite_group_replay"]["generator_count"] == 9
assert v85["finite_group_replay"]["mask25_orbit_masks_decimal"] == [25]
assert v85["sign_quotient_consequence"]["coordinate_conjugate_B1_B2_B3_image_masks_decimal"] == [0, 25]
assert v85["sign_quotient_consequence"]["e3_target_mask_decimal"] == 20
assert v85["sign_quotient_consequence"]["e3_in_any_coordinate_conjugate_sign_quotient_image"] is False
assert v85["exact_boundary"]["global_H2_mu2_nonexistence_claim"] is False
assert v85["exact_boundary"]["non_coordinate_conjugate_full_surface_realization_still_open"] is True

state["schema"] = "STAGE33_MAIN_COMPACT_STATE_V27_V85_COORDINATE_CONJUGATE_GYSIN_FAMILY_FROZEN_NONCOORDINATE_CECH_GERSTEN_ACTIVE"
a = state["authority_sync"]
a["frontier_authority"] = "V85_COORDINATE_CONJUGATE_SIGN_QUOTIENT_ROUTE_FREEZE"
a["mathematical_authority"] = "V25_V36_EXACT_CERTIFICATE_CHAIN_PLUS_BRANCH_E3_V41_V57_V61_V71_V73_V75_V77_V79_V80_V85"
a["status"] = "V85_BRANCH_EXACT_FRONTIER_PROJECTED_CONTROLLER_GLOBAL_FIREWALLS_LOCKED"
state["branch_exact_frontier_authority"] = "stages/stage33/33-12/e3-coordinate-conjugate-sign-quotient-route-freeze-v85.json"

cur = state["current"]
cur["active_missing_interface"] = "NON_COORDINATE_CONJUGATE_FULL_SURFACE_CECH_OR_ACTUAL_GERSTEN_DATUM_WITH_EXACT_PROPER14_BRAUER_IMAGE_MASK20"
cur["next_exact_leaf"] = v85["next_exact_leaf"]
cur["substep"] = "E3_A2_4C_NON_COORDINATE_CONJUGATE_CECH_OR_ACTUAL_GERSTEN"

f = state["current_exact_frontier"]
f["e3_coordinate_automorphism_generator_count"] = 9
f["e3_coordinate_conjugate_mask25_orbit_size"] = 1
f["e3_coordinate_conjugate_mask25_orbit_masks_decimal"] = [25]
f["e3_coordinate_conjugate_sign_quotient_image_masks_decimal"] = [0, 25]
f["e3_coordinate_conjugate_sign_quotient_routes_frozen"] = True
f["e3_in_any_coordinate_conjugate_sign_quotient_image"] = False
f["e3_global_H2_mu2_nonexistence_claim"] = False
f["e3_genuine_full_surface_h2_mu2_lift_materialized"] = False

anti = state["anti_loop_policy"]
anti["do_not_reopen_coordinate_conjugate_sign_quotient_gysin_after_v85"] = True
anti["do_not_promote_coordinate_conjugate_route_family_failure_to_global_H2_mu2_nonexistence"] = True

state["locked_facts"]["v84"] = {
    "blob_sha1": V84_BLOB,
    "status": "EXACT_COORDINATE_AUTOMORPHISM_ORBIT_REPLAY_INPUT_TO_V85",
}
state["locked_facts"]["v85"] = {
    "sha256": V85_SHA,
    "blob_sha1": V85_BLOB,
    "status": "ALL_COORDINATE_CONJUGATE_SIGN_QUOTIENT_GYSIN_ROUTES_FROZEN_MASK20_OUTSIDE",
}

ri = state["resolved_investigations"]
ri["e3_coordinate_conjugate_sign_quotient_family"] = "CLOSED_EXACT_V85_MASK25_ORBIT_SINGLETON_DO_NOT_REOPEN"
ri["e3_full_surface_cech_realization"] = "OPEN_V85_NON_COORDINATE_CONJUGATE_CECH_OR_ACTUAL_GERSTEN_MASK20"

state["current_leaf_working_set"] = [
    "docs/research-os/policies/repository-asset-discovery.md",
    "docs/arsenal/index.json",
    "docs/arsenal/cards/provisional/S33-PW04.md",
    "docs/arsenal/cards/provisional/S33-PW07.md",
    "docs/arsenal/cards/provisional/S33-PW08.md",
    "stages/stage33/ROADMAP-33-12-V71-J1-TORSOR.md",
    "stages/stage33/33-12/e3-coordinate-conjugate-sign-quotient-route-freeze-v85.json",
    "stages/stage33/33-12/diagnose_e3_coordinate_automorphism_orbit_v84.py",
    "stages/stage33/33-12/e3-b1-route-freeze-and-outside-cech-rewire-v80.json",
    "stages/stage33/33-12/e3-b1-full-gysin-matrix-xalpha-correction-v79.json",
    "stages/stage33/33-12/e3-mask20-literal-cech-preimage-gap-v52.json",
    "stages/stage33/33-12/e3-mask20-picard-adjoint-candidate-v53.json",
    "stages/stage33/33-12/e3-mask20-marked-picard-to-literal-geometry-bridge-gap-v56.json",
    "stages/stage33/33-12/j2-corrected-explicit-cech-mu2-lift.json",
]
state["discovery_policy"]["current_arsenal_cards"] = ["S33-PW04", "S33-PW07", "S33-PW08"]

ex = state["execution_gate"]
ex["advance_scope"] = "A2_4C_NON_COORDINATE_CONJUGATE_FULL_SURFACE_CECH_OR_ACTUAL_GERSTEN_MASK20"
ex["next_expected_command"] = "CONSTRUCT_NON_COORDINATE_CONJUGATE_FULL_SURFACE_CECH_OR_ACTUAL_GERSTEN_DATUM_WITH_EXACT_PROPER14_BRAUER_IMAGE_MASK20; DO_NOT_REOPEN_COORDINATE_CONJUGATE_SIGN_QUOTIENT_GYSIN_FAMILY"

state["canonical_sha256"] = csha(state)
print("V85_STATE_CANONICAL_SHA256=" + state["canonical_sha256"])
print(json.dumps(state, sort_keys=True, separators=(",", ":")))
