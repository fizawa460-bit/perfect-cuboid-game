#!/usr/bin/env python3
"""Verify Stage33 V68-V69 J1 transport-gap reduction and exact remaining shear bit."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
V63 = HERE / "e3-b1-c22-kappa-a-literal-cech-lift-v63.json"
V64 = HERE / "e3-b1-c22-named-torsion-normalization-bridge-v64.json"
V65 = HERE / "e3-b1-j1-marked-kc-discriminator-gate-v65.json"
V68 = HERE / "e3-b1-c22-j1-kummer-to-kc-transport-gap-v68.json"
V69 = HERE / "e3-b1-c22-j1-marked-kc-one-bit-transport-gate-v69.json"
J2 = HERE / "j2-cv-d2-semantic-orientation.json"

BLOBS = {
    V63: "3a966544378e2302f5a591e2162c30dbb5a3732e",
    V64: "cd112667605f7d73736827269bacff4de7ef0fde",
    V65: "e3634d9c8ed0f4f58ff4132f7bd5822f60fa23c3",
    V68: "9453000948593f21198ecfdff0ccce64d1c8ffd9",
    V69: "77638f2f3afb2dc6445f5130addcd52e88bc5767",
    J2: "140acdc9896d1d87a82a1807fd92ce276a620d75",
}

def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def load(path: Path):
    assert git_blob_sha(path) == BLOBS[path], path
    return json.loads(path.read_text(encoding="utf-8"))

v63, v64, v65, v68, v69, j2 = [load(p) for p in (V63, V64, V65, V68, V69, J2)]

# Retained source-side literal class and named torsion bridge.
assert v63["literal_symbol"]["branch_input"] == "kappa_A=[P_r1-P_r4]"
assert v63["surface_mu2_lift"]["class"] == "lambda_A=alpha(e_A), represented generically by {f_A,g22}"
assert v64["exact_bridge"]["kappa_A"]["named_torsion"] == "J1"
assert v64["exact_bridge"]["kappa_D"]["named_torsion"] == "J2"
assert v64["marked_kc_interface"]["kappa_D"]["coordinate_f2"] == [1, 0]
assert v65["locked_frontier"]["J1_marked_kc_coordinate_candidates_f2"] == [[0, 1], [1, 1]]
assert v65["locked_frontier"]["remaining_ambiguity_bits"] == 1

# V68 closes only the unconstrained-transport interpretation; D2 itself stays open.
assert v68["version"] == 68
assert v68["status"] == "D2_OPEN_TRANSPORT_BRIDGE_REQUIRED"
assert v68["scope"]["source_class"] == "kappa_A = P_r1 - P_r4 = J1"
assert v68["scope"]["source_lift"] == "lambda_A = {f_A, g_22}"
assert v68["targeted_repository_check"]["result"] == "NO_EXPLICIT_TRANSPORT_AUTHORITY_FOUND"
assert v68["result"]["d2_verdict"] == "OPEN"
assert "Do not relabel or reuse the J2" in v68["result"]["forbidden_shortcut"]
assert v68["credit_firewall"]["D2_closed"] is False

# V69 reduces the missing transport to exactly identity vs the unique shear fixing u1.
assert v69["version"] == 69
assert v69["status"] == "D2_OPEN_EXACT_ONE_BIT_MARKING_AMBIGUITY"
frame = v69["source_side_exact_character_frame"]
assert frame["class_coordinates"] == {
    "0": [0, 0], "J1": [1, 1], "J2": [1, 0], "J1+J2": [0, 1]
}
assert frame["cycle_basis"] == {"L": "D_L=J1+J2", "R": "D_R=J2"}
assert frame["bijection"] is True

tr = v69["transport_reduction"]
assert tr["identified_source_classes"] == {"eL": "J2", "eR": "J1+J2", "J1": "eL+eR"}
assert tr["forced_first_column"]["coordinate_f2"] == [1, 0]
cs = tr["candidate_transports_contact_to_marked"]
assert len(cs) == 2
assert cs[0] == {
    "name": "identity",
    "matrix_columns": [[1, 0], [0, 1]],
    "image_of_eR": "u2",
    "image_of_J1_eL_plus_eR": "u1+u2",
    "J1_coordinate_f2": [1, 1],
    "expected_twisted_kernel_minimum_norm_if_selected": 12,
}
assert cs[1] == {
    "name": "shear_fixing_u1",
    "matrix_columns": [[1, 0], [1, 1]],
    "image_of_eR": "u1+u2",
    "image_of_J1_eL_plus_eR": "u2",
    "J1_coordinate_f2": [0, 1],
    "expected_twisted_kernel_minimum_norm_if_selected": 4,
}
assert v69["d2_verdict"] == "OPEN_ONE_BIT"
assert v69["translation_torsor_scope_check"]["j1_independent_fingerprint_available"] is False

# Cross-check the two target fingerprints against the independently retained marked Kc authority.
mn = j2["kernel_fingerprint_identification"]["minimum_norm_to_functional"]
assert mn["4"] == [0, 1]
assert mn["12"] == [1, 1]
assert v69["translation_torsor_scope_check"]["j2_kernel_fingerprints"] == {
    "u2": 4, "u1": 8, "u1+u2": 12
}

fw = v69["credit_firewall"]
for key in (
    "j1_marked_kc_coordinate_selected",
    "new_marked_proper14_gysin_column_materialized",
    "b1_14x4_matrix_materialized",
    "e3_mask20_membership_computed",
    "genuine_full_surface_H2_mu2_lift",
    "e3_kummer_column",
    "D2_closed",
    "stage33_12_closed",
    "stage33_13_released",
    "perfect_cuboid_credit",
    "merge_allowed",
):
    assert fw[key] is False, key

assert v69["next_exact_leaf"].startswith("SOURCE_LOCK_ONE_SECOND_AXIS_DATUM_SELECTING_IDENTITY_VS_SHEAR")

print(json.dumps({
    "success": True,
    "marker": "V70_V68_V69_J1_TRANSPORT_GATE_REPLAY_COMPLETE",
    "v68_blob_sha1": BLOBS[V68],
    "v69_blob_sha1": BLOBS[V69],
    "remaining_transport_bits": 1,
    "candidate_transports": ["identity", "shear_fixing_u1"],
    "J1_selected": False,
    "D2_closed": False,
    "merge_allowed": False,
}, sort_keys=True))
