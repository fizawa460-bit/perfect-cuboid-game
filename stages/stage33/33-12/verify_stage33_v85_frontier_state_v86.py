#!/usr/bin/env python3
"""Historical V86 replay of immutable V85 evidence only.

This verifier must never inspect mutable Stage33 startup/state.  Its sole role is
to replay the exact V85 route-freeze certificate and the immutable V79/V84
inputs named by that certificate.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
V79 = HERE / "e3-b1-full-gysin-matrix-xalpha-correction-v79.json"
V84 = HERE / "diagnose_e3_coordinate_automorphism_orbit_v84.py"
V85 = HERE / "e3-coordinate-conjugate-sign-quotient-route-freeze-v85.json"

V79_SHA = "29acced201721df4ad65bda071914bf71a4b5d7098dce86a541cdd41f2085921"
V79_BLOB = "3d9ca5dc8c659cb6281f27d91825d85ad3ef8966"
V84_BLOB = "e9c7e81cc59fb5203482071208d25ff1447edeb2"
V85_SHA = "6f63d8814d87d1e9ae4810fb9a5a3d09c9f37f0d3bd2875ddf7f4dce43c82159"
V85_BLOB = "2b667e699448d2f910e16c5a4c93532fe390f893"
NEXT = (
    "CONSTRUCT_NON_COORDINATE_CONJUGATE_FULL_SURFACE_CECH_OR_ACTUAL_GERSTEN_"
    "DATUM_WITH_EXACT_PROPER14_BRAUER_IMAGE_MASK20"
)


def csha(obj):
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def blob_sha(path: Path):
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


v79 = json.loads(V79.read_text(encoding="utf-8"))
v85 = json.loads(V85.read_text(encoding="utf-8"))

# Immutable certificate/source locks only.  Do not read MAIN-STATE.json,
# MAIN-START-HERE.md, controller.json, or any mutable roadmap here.
assert v79["canonical_sha256"] == V79_SHA == csha(v79)
assert blob_sha(V79) == V79_BLOB
assert blob_sha(V84) == V84_BLOB
assert v85["canonical_sha256"] == V85_SHA == csha(v85)
assert blob_sha(V85) == V85_BLOB

locks = v85["source_locks"]
assert locks["v79_b1_matrix"]["canonical_sha256"] == V79_SHA
assert locks["v79_b1_matrix"]["blob_sha1"] == V79_BLOB
assert locks["v84_orbit_replay"]["blob_sha1"] == V84_BLOB

assert v79["b1_matrix"]["column_masks_decimal"] == [0, 25, 0, 25]
assert v79["b1_matrix"]["image_masks_decimal"] == [0, 25]
assert v79["b1_matrix"]["rank_f2"] == 1
assert v79["e3_membership"]["target_mask_decimal"] == 20
assert v79["e3_membership"]["in_image"] is False

replay = v85["finite_group_replay"]
assert replay["generator_count"] == 9
assert replay["mask25_orbit_size"] == 1
assert replay["mask25_orbit_masks_decimal"] == [25]
assert replay["mask25_fixed_by_full_generated_coordinate_automorphism_group"] is True

sq = v85["sign_quotient_consequence"]
assert sq["b1_exact_image_masks_decimal"] == [0, 25]
assert sq["coordinate_conjugate_B1_B2_B3_image_masks_decimal"] == [0, 25]
assert sq["e3_target_mask_decimal"] == 20
assert sq["e3_in_any_coordinate_conjugate_sign_quotient_image"] is False
assert set(sq["routes_frozen"]) == {
    "B1_BRANCH_GYSIN",
    "B2_COORDINATE_CONJUGATE_BRANCH_GYSIN",
    "B3_COORDINATE_CONJUGATE_BRANCH_GYSIN",
}

boundary = v85["exact_boundary"]
assert boundary["global_H2_mu2_nonexistence_claim"] is False
assert boundary["all_literal_cech_routes_exhausted"] is False
assert boundary["all_gersten_routes_exhausted"] is False
assert boundary["non_coordinate_conjugate_full_surface_realization_still_open"] is True

fw = v85["credit_firewall"]
assert fw["stage33_progress"] == "6/11"
for key in (
    "stage33_12_closed_exact",
    "stage33_13_released",
    "genuine_full_surface_H2_mu2_lift_for_e3",
    "e3_kummer_column_materialized",
    "receiver_credit",
    "theorem_credit",
    "endpoint_credit",
    "perfect_cuboid_credit",
    "merge_allowed",
):
    assert fw[key] is False

assert v85["next_exact_leaf"] == NEXT

print(json.dumps({
    "success": True,
    "marker": "V86_HISTORICAL_V85_IMMUTABLE_EVIDENCE_REPLAY_COMPLETE",
    "historical_frontier": "V85",
    "reads_live_main_state": False,
    "reads_live_startup": False,
    "coordinate_automorphism_orbit_masks": [25],
    "coordinate_conjugate_sign_quotient_image_masks": [0, 25],
    "e3_target_mask": 20,
    "global_H2_mu2_nonexistence_claim": False,
    "historical_next_leaf": NEXT,
    "merge_allowed": False,
}, sort_keys=True))
