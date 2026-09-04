#!/usr/bin/env python3
"""Verify Stage33 V65 exact V64-frontier integration and one-bit J1 discriminator gate."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-b1-j1-marked-kc-discriminator-gate-v65.json"

LOCKS = {
    "v61_c22_basis": ("e3-b1-c22-pic0-2-basis-v61.json", "48ec6b2ffb91d549041ff5ec667ff88d493becf01d89e1bb5974134b3b0a53f6"),
    "v62_full_b1_domain_basis": ("e3-b1-full-domain-basis-v62.json", "353e68438334a0da71dfdbc09a8bf60e7e511598cf54a173338735686f1c3f4c"),
    "v63_kappa_a_literal_cech_lift": ("e3-b1-c22-kappa-a-literal-cech-lift-v63.json", "7714c722f7f30cae1fac03edd34821d1e84372bf3d7663dc2c62a98fde6b186c"),
    "v64_named_torsion_bridge": ("e3-b1-c22-named-torsion-normalization-bridge-v64.json", "55679ba16710e3b78ab46ab699ea73ecc3fc56faab4cb7edc5a02e487df3de38"),
}
J2 = HERE / "j2-cv-d2-semantic-orientation.json"
J2_SHA = "0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e"
EXPECTED = "7ebef9a6182522f772f198d8c1572acc48cd8441f6158312d1f3f3f2c7fcc01c"

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def locked(path, expected):
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj

cert = locked(CERT, EXPECTED)
loaded = {name: locked(HERE / path, digest) for name, (path, digest) in LOCKS.items()}
j2 = locked(J2, J2_SHA)

assert loaded["v61_c22_basis"]["ordered_c22_pic0_2_basis"][0]["class_name"] == "kappa_A"
assert loaded["v61_c22_basis"]["ordered_c22_pic0_2_basis"][1]["class_name"] == "kappa_D"
assert [x["class"] for x in loaded["v62_full_b1_domain_basis"]["ordered_b1_h1_basis"]] == [
    "cc(kappa_A)", "cc(kappa_D)", "kappa_A", "kappa_D"
]
assert loaded["v63_kappa_a_literal_cech_lift"]["surface_mu2_lift"]["surface_mu2_lift_materialized"] is True
assert loaded["v63_kappa_a_literal_cech_lift"]["proper14_coordinate_interface"]["column_index"] == 3
assert loaded["v63_kappa_a_literal_cech_lift"]["proper14_coordinate_interface"]["marked_proper14_14bit_coordinate_materialized"] is False

v64 = loaded["v64_named_torsion_bridge"]
assert v64["exact_bridge"]["kappa_A"]["named_torsion"] == "J1"
assert v64["exact_bridge"]["kappa_D"]["named_torsion"] == "J2"
assert v64["marked_kc_interface"]["kappa_D"]["coordinate_f2"] == [1, 0]
assert v64["marked_kc_interface"]["kappa_A"]["coordinate_candidates_f2"] == [[0, 1], [1, 1]]
assert v64["marked_kc_interface"]["remaining_ambiguity_bits"] == 1
assert v64["marked_kc_interface"]["kappa_A"]["selected"] is None

mn = j2["kernel_fingerprint_identification"]["minimum_norm_to_functional"]
assert mn["4"] == [0, 1]
assert mn["12"] == [1, 1]
assert cert["target_discriminator_fingerprints"]["u2"]["minimum_norm"] == 4
assert cert["target_discriminator_fingerprints"]["u1_plus_u2"]["minimum_norm"] == 12

assert cert["bounded_search_receipt"]["direct_exact_j1_discriminator_found"] is False
assert cert["bounded_search_receipt"]["repository_absence_claimed"] is False
assert cert["bounded_search_receipt"]["mathematical_nonexistence_claimed"] is False
assert all(v is False for v in cert["rejected_shortcuts"].values())
assert cert["credit_firewall"]["j1_marked_kc_coordinate_selected"] is False
assert cert["credit_firewall"]["new_marked_proper14_gysin_column_materialized"] is False
assert cert["credit_firewall"]["b1_14x4_matrix_materialized"] is False
assert cert["credit_firewall"]["e3_mask20_membership_computed"] is False
assert cert["credit_firewall"]["stage33_12_closed_exact"] is False
assert cert["credit_firewall"]["stage33_13_released"] is False
assert cert["credit_firewall"]["merge_allowed"] is False

print(json.dumps({
    "success": True,
    "marker": "V65_J1_ONE_BIT_DISCRIMINATOR_GATE_REPLAY_COMPLETE",
    "canonical_sha256": EXPECTED,
    "J1_candidates": [[0, 1], [1, 1]],
    "target_minimum_norms": {"u2": 4, "u1+u2": 12},
    "selected": None,
    "merge_allowed": False
}, sort_keys=True))
