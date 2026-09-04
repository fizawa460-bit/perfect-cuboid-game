#!/usr/bin/env python3
"""Verify Stage33 V67 #1529 new-signal scope gate for the J1 discriminator leaf."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-b1-j1-post1529-equivariance-scope-gate-v67.json"
V65 = HERE / "e3-b1-j1-marked-kc-discriminator-gate-v65.json"
V63 = HERE / "e3-b1-c22-kappa-a-literal-cech-lift-v63.json"

EXPECTED = "8b52ab2f2bf57c068fb084035e36fc066806560fac6814c8d9bce9b26e7345de"
V65_SHA = "7ebef9a6182522f772f198d8c1572acc48cd8441f6158312d1f3f3f2c7fcc01c"
V63_SHA = "7714c722f7f30cae1fac03edd34821d1e84372bf3d7663dc2c62a98fde6b186c"

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def locked(path, expected):
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj

cert = locked(CERT, EXPECTED)
v65 = locked(V65, V65_SHA)
v63 = locked(V63, V63_SHA)

assert v65["locked_frontier"]["kappa_A_named_torsion"] == "J1"
assert v65["locked_frontier"]["J1_marked_kc_coordinate_candidates_f2"] == [[0, 1], [1, 1]]
assert v65["locked_frontier"]["remaining_ambiguity_bits"] == 1
assert v65["credit_firewall"]["j1_marked_kc_coordinate_selected"] is False

assert v63["surface_mu2_lift"]["class"] == "lambda_A=alpha(e_A), represented generically by {f_A,g22}"
assert v63["proper14_coordinate_interface"]["marked_proper14_14bit_coordinate_materialized"] is False

lock = cert["source_locks"]["post1529_fsm_stoll_adapter"]
assert lock["commit"] == "ea51d06f3fe46b134e98a065332e9c70fcec57f0"
assert lock["merged_pr"] == 1529
assert lock["blob_sha1"] == "809d7096cf98cf94b37455b6281cb23cbdcc6b41"
assert lock["canonical_sha256_without_this_field"] == "5726289d8948beaaf3ed4e2dc260f49d1b3b3054642f3460b6b1e53c77ea23bc"

signal = cert["materially_new_signal"]
assert signal["adapter_scope"] == "ONLY_U_S_TO_STOLL_WORD_PROVENANCE"
assert signal["U_matrix"] == [[1, 2], [0, 1]]
assert signal["U_stoll_word"] == "g4*g5*g9"
assert signal["S_matrix"] == [[0, -1], [1, 0]]
assert signal["S_stoll_word"] == "g2*g5"
assert signal["verification_contract_no_other_fsm_claims"] is True

scope = cert["exact_scope_test"]
supplies = scope["post1529_adapter_supplies"]
assert supplies["U_S_to_stoll_word_provenance"] is True
assert supplies["named_J1_J2_action"] is False
assert supplies["fixed_marked_kc_action"] is False
assert supplies["second_transport_column"] is False
assert supplies["named_CV_to_fixed_marked_kc_equivariance"] is False
assert scope["D1_satisfied_by_post1529_signal"] is False
assert scope["D3_satisfied_by_post1529_signal"] is False

receipt = cert["bounded_search_receipt"]
assert receipt["route_scope_closed"] == "POST1529_SIGNAL_ONLY"
assert receipt["search_miss_proves_repository_absence"] is False
assert receipt["search_miss_proves_mathematical_nonexistence"] is False

nxt = cert["next_construction"]
assert nxt["roadmap_leaf"] == "D2_INDEPENDENT_J1_SOURCE_FINGERPRINT"
assert nxt["preferred_witness"] == "J1_TWISTED_KERNEL_MINIMUM_NORM"
assert nxt["literal_seed"]["named_torsion"] == "J1"
assert nxt["j2_template_use"] == "METHOD_TEMPLATE_ONLY_NOT_A_J1_IDENTIFICATION"

fw = cert["credit_firewall"]
assert fw["j1_marked_kc_coordinate_selected"] is False
assert fw["j1_cocycle_materialized"] is False
assert fw["j1_torsor_materialized"] is False
assert fw["j1_twisted_kernel_minimum_norm_selected"] is False
assert fw["new_marked_proper14_gysin_column_materialized"] is False
assert fw["stage33_12_closed_exact"] is False
assert fw["stage33_13_released"] is False
assert fw["merge_allowed"] is False

print(json.dumps({
    "success": True,
    "marker": "V67_POST1529_J1_EQUIVARIANCE_SCOPE_GATE_REPLAY_COMPLETE",
    "canonical_sha256": EXPECTED,
    "post1529_D1_satisfied": False,
    "post1529_D3_satisfied": False,
    "next_leaf": nxt["roadmap_leaf"],
    "J1_selected": False,
    "merge_allowed": False
}, sort_keys=True))
