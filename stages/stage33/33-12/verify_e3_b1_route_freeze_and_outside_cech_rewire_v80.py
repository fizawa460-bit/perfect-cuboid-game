#!/usr/bin/env python3
"""Verify V80: V79 freezes B1 and rewires e3 to outside-B1 literal Cech/Gersten realization."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-b1-route-freeze-and-outside-cech-rewire-v80.json"
V79 = HERE / "e3-b1-full-gysin-matrix-xalpha-correction-v79.json"
V52 = HERE / "e3-mask20-literal-cech-preimage-gap-v52.json"
V53 = HERE / "e3-mask20-picard-adjoint-candidate-v53.json"
V56 = HERE / "e3-mask20-marked-picard-to-literal-geometry-bridge-gap-v56.json"
J2 = HERE / "j2-corrected-explicit-cech-mu2-lift.json"

EXPECTED = "d75a7bbe14f5194b91a1411a372ce4b64982331d04da23d044591422fb37ccbf"
LOCKS = {
    V79: "3d9ca5dc8c659cb6281f27d91825d85ad3ef8966",
    V52: "15ae7ebf8ddaf9d8771d48bc93caa0705e4ebf67",
    V53: "011c6ac6db793e2458622355f031e369f176973e",
    V56: "251a5940672758c33eecff9656e7d57f4422f38b",
    J2: "97261735968c07903f87370eb483df8d6475b67c",
}


def csha(obj):
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha(path: Path):
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


for path, expected in LOCKS.items():
    assert blob_sha(path) == expected, path

v79 = json.loads(V79.read_text())
v52 = json.loads(V52.read_text())
v53 = json.loads(V53.read_text())
v56 = json.loads(V56.read_text())
j2 = json.loads(J2.read_text())
cert = json.loads(CERT.read_text())

assert v79["canonical_sha256"] == "29acced201721df4ad65bda071914bf71a4b5d7098dce86a541cdd41f2085921" == csha(v79)
assert j2["canonical_sha256"] == "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b" == csha(j2)
assert cert["canonical_sha256"] == EXPECTED == csha(cert)

# V79 closes exactly the B1 branch-Gysin route.
assert v79["b1_matrix"]["shape"] == [14, 4]
assert v79["b1_matrix"]["column_masks_decimal"] == [0, 25, 0, 25]
assert v79["b1_matrix"]["rank_f2"] == 1
assert v79["b1_matrix"]["image_masks_decimal"] == [0, 25]
assert v79["e3_membership"]["target_mask_decimal"] == 20
assert v79["e3_membership"]["in_image"] is False
assert v79["credit_firewall"]["global_H2_mu2_nonexistence_claim"] is False

# The outside-B1 target is the pre-existing exact literal-geometry gap, not a
# reopened B1 search and not J2 relabelling.
assert v52["bounded_inspection"]["e3_source"]["proper14_mask_decimal"] == 20
assert v52["bounded_inspection"]["mask20_literal_preimage_materialized"] is False
assert v52["exact_blocker"]["name"] == "SOURCE_SPECIFIC_MARKED_GEOMETRIC_CECH_PREIMAGE_FOR_E3_PROPER14_MASK20"
assert v53["exact_computation"]["input_proper14_mask_decimal"] == 20
assert v53["geometric_realization_boundary"]["source_specific_cech_h2_mu2_preimage_materialized"] is False
assert v56["interface_gap"]["name"] == "MASK20_MARKED_PICARD_ADJOINT_TO_LITERAL_FULL_SURFACE_CECH_GEOMETRY"
assert v56["exact_chain_localization"]["locked_chain_materializes_required_geometry_output"] is False
assert j2["surface_mu2_lift"]["genuine_surface_H2_mu2_lift_materialized"] is True
assert v52["bounded_inspection"]["available_literal_cech_example"]["reusable_as_e3_by_relabelling"] is False

p = cert["v79_promotion"]
assert p["b1_column_masks_decimal"] == [0, 25, 0, 25]
assert p["b1_image_masks_decimal"] == [0, 25]
assert p["e3_target_mask_decimal"] == 20
assert p["e3_in_b1_image"] is False
assert p["global_H2_mu2_nonexistence_claim"] is False
assert p["proper14_column3_mask_decimal"] == 0

leaf = cert["rewired_current_leaf"]
assert leaf["name"] == "SOURCE_SPECIFIC_FULL_SURFACE_CECH_H2_MU2_REALIZATION_FOR_E3_MASK20_OUTSIDE_B1_ROUTE"
assert leaf["input_proper14_mask_decimal"] == 20
assert leaf["literal_function_divisor_transition_datum_materialized"] is False
assert leaf["genuine_full_surface_H2_mu2_lift_for_e3"] is False
assert leaf["arsenal_routing"]["marked_source_binding"] == "S33-PW04"
assert leaf["arsenal_routing"]["literal_geometric_realization"] == "S33-PW07"
assert leaf["arsenal_routing"]["gersten_adapter"].startswith("S33-PW08_CONDITIONAL")

assert cert["anti_loop"]["do_not_reopen_b1_gysin_membership_after_v79"] is True
assert cert["anti_loop"]["do_not_promote_b1_nonmembership_to_global_H2_mu2_nonexistence"] is True
assert cert["anti_loop"]["do_not_relabel_j2_literal_cech_as_e3"] is True
assert cert["credit_firewall"]["stage33_progress"] == "6/11"
assert cert["credit_firewall"]["stage33_12_closed_exact"] is False
assert cert["credit_firewall"]["stage33_13_released"] is False
assert cert["credit_firewall"]["genuine_full_surface_H2_mu2_lift_for_e3"] is False
assert cert["credit_firewall"]["merge_allowed"] is False

print(json.dumps({
    "success": True,
    "marker": "V80_B1_ROUTE_FROZEN_OUTSIDE_CECH_REWIRE_COMPLETE",
    "canonical_sha256": EXPECTED,
    "b1_image_masks": [0, 25],
    "e3_mask20_in_b1_image": False,
    "global_H2_mu2_nonexistence_claim": False,
    "next_leaf": leaf["name"],
    "merge_allowed": False,
}, sort_keys=True))
