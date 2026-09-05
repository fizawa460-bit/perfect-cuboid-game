#!/usr/bin/env python3
"""Verify V79: x-alpha correction closes the exact B1 14x4 Gysin matrix."""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
R05 = STAGE / "33-05"
CERT = HERE / "e3-b1-full-gysin-matrix-xalpha-correction-v79.json"
V57 = HERE / "e3-mask20-b1-gysin-image-gate-v57.json"
V62 = HERE / "e3-b1-full-domain-basis-v62.json"
V63 = HERE / "e3-b1-c22-kappa-a-literal-cech-lift-v63.json"
V77 = HERE / "e3-b1-c22-j1-xalpha-kernel-correction-v77.json"
XALPHA = R05 / "xalpha_pair_galois_repair.py"
ADAPTER = HERE / "j2-corrected-branch-surface-mu2-adapter.json"
J2CECH = HERE / "j2-corrected-explicit-cech-mu2-lift.json"

EXPECTED = "29acced201721df4ad65bda071914bf71a4b5d7098dce86a541cdd41f2085921"
LOCKS = {
    V57: "3d7b6ad6b4355a0ed379553c4d5fa97fb3209e6e",
    V62: "781549b869dbb0e143d982c9b67523f2336225e4",
    V63: "3a966544378e2302f5a591e2162c30dbb5a3732e",
    V77: "bfc54650fdc7885664cdfcb1533cb9a1e711c5a5",
    XALPHA: "b7f37df50a123ef6c972aa210e7efb5f16535f76",
    ADAPTER: "6d0bdebdc1ec5466517caace8191b2968747d2f5",
    J2CECH: "97261735968c07903f87370eb483df8d6475b67c",
}
CANONICALS = {
    V62: "353e68438334a0da71dfdbc09a8bf60e7e511598cf54a173338735686f1c3f4c",
    V63: "7714c722f7f30cae1fac03edd34821d1e84372bf3d7663dc2c62a98fde6b186c",
    V77: "d2f803ab0cb394389c1fedf8f94e237ce82702743d0240a4f4b2fe73a44d5e98",
    ADAPTER: "edb98c634c79c97c09b0ea4a14402f32d9c5900c63dd9584eca5ea91b91d6875",
    J2CECH: "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b",
}


def csha(obj):
    body = dict(obj)
    body.pop("canonical_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def load(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    if path in CANONICALS:
        assert obj["canonical_sha256"] == CANONICALS[path] == csha(obj), path
    return obj


def mask_vec(mask: int, n=14):
    return [(mask >> i) & 1 for i in range(n)]


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]


for p, h in LOCKS.items():
    assert blob_sha(p) == h, p
v57, v62, v63, v77, adapter, j2 = map(load, [V57, V62, V63, V77, ADAPTER, J2CECH])
xtext = XALPHA.read_text(encoding="utf-8")

# Same source generator: V61/V63 kappa_A uses exactly the x-alpha J1 function.
assert v63["literal_symbol"]["f_A"] == "(t-r1)/(t-r4)"
assert v63["literal_symbol"]["branch_input"] == "kappa_A=[P_r1-P_r4]"
assert v63["surface_mu2_lift"]["class"] == "lambda_A=alpha(e_A), represented generically by {f_A,g22}"
assert v63["surface_mu2_lift"]["maps_to_branch_input"] == "C22:kappa_A"
assert "f1 = sp.cancel((t-r1)/(t-r4))  # J1" in xtext
assert '"J1_in_xalpha_image_exact": True' in xtext
assert 'quotient_basis = ["J2", "q1"]' in xtext
assert v77["cohomological_correction"]["J1_geometric_brauer_class"] == "ZERO"

# Same Brauer layer.  V57 defines the B1 route into Br(Kc_tilde_bar)[2]; the
# exact double-cover adapter identifies its C22 generator with the CV pair, and
# the explicit Cech producer records the corestriction/symbol projection.
assert v57["exact_b1_route_geometry"]["canonical_route_map"].startswith("Phi_B1:H1(")
assert v57["exact_b1_route_geometry"]["canonical_route_map"].endswith("Br(Kc_tilde_bar)[2]")
assert adapter["kummer_gysin_adapter"]["brauer_image"] == "Phi(0,kappa_D)=corrected geometric J2=(f2,1)"
assert j2["surface_mu2_lift"]["brauer_image"] == "corrected nonzero J2=(f2,1)"
assert j2["surface_mu2_lift"]["cv_projection_formula"] == "Cor_{K(C22)(s)/K(t,s)}{f2,s-alpha22}={f2,Norm(s-alpha22)}={f2,g22}"
# The formal projection identity applies to any base-field Kummer function f;
# V63 uses the identical alpha/g22 construction with f=f_A=f1.  Since V77
# proves that CV quotient class J1=(f1,1) is zero, column 3 is zero.
zero = [0] * 14
col25 = mask_vec(25)
assert col25 == [1,0,0,1,1,0,0,0,0,0,0,0,0,0]
assert v57["existing_exact_j2_point_in_route"]["proper14_brauer_image_mask_decimal"] == 25

# Ordered domain and conjugate columns.
order = [x["class"] for x in v62["ordered_b1_h1_basis"]]
assert order == ["cc(kappa_A)", "cc(kappa_D)", "kappa_A", "kappa_D"]
assert v62["conjugate_branch_identification"]["component_action"].startswith("cc(C22_tilde)=C21_tilde")
assert v62["ordered_c21_pic0_2_basis"][0]["kummer_function_on_conjugate_normalization"] == "cc(f_A)=f_A=(t-r1)/(t-r4)"
# J2's exact Cech defect is algebraic/generically zero under cc, hence its
# Brauer class is fixed.  Zero is fixed automatically for J1.
assert j2["galois_defect_generic_splittings"]["cc"]["generic_symbol_zero"] is True
assert "g21*g22" in j2["galois_defect_generic_splittings"]["cc"]["formula"]
assert "(B1/(2*t))^2" in j2["galois_defect_generic_splittings"]["cc"]["formula"]

columns = [zero, col25, zero, col25]
rows = [[columns[j][i] for j in range(4)] for i in range(14)]
assert rows == [[0,1,0,1],[0,0,0,0],[0,0,0,0],[0,1,0,1],[0,1,0,1]] + [[0,0,0,0]] * 9

# Exhaustive F2^4 membership solve.
target = mask_vec(20)
assert target == v57["e3_membership_gate"]["proper14_coordinate_f2"]
solutions = []
images = set()
for bits in itertools.product((0, 1), repeat=4):
    out = [0] * 14
    for bit, col in zip(bits, columns):
        if bit:
            out = xor(out, col)
    mask = sum(bit << i for i, bit in enumerate(out))
    images.add(mask)
    if out == target:
        solutions.append(list(bits))
assert images == {0, 25}
assert solutions == []

cert = json.loads(CERT.read_text(encoding="utf-8"))
assert cert["canonical_sha256"] == EXPECTED == csha(cert)
assert cert["column3"]["proper14_coordinate_f2"] == zero
assert cert["column3"]["proper14_mask_decimal"] == 0
assert cert["column3"]["zero_brauer_does_not_mean_zero_H2_mu2_lift"] is True
assert cert["b1_matrix"]["column_masks_decimal"] == [0, 25, 0, 25]
assert cert["b1_matrix"]["columns_f2"] == columns
assert cert["b1_matrix"]["rows_f2"] == rows
assert cert["b1_matrix"]["rank_f2"] == 1
assert cert["b1_matrix"]["image_masks_decimal"] == [0, 25]
assert cert["e3_membership"]["target_mask_decimal"] == 20
assert cert["e3_membership"]["in_image"] is False
assert cert["e3_membership"]["solution_vectors_f2"] == []
assert cert["credit_firewall"]["b1_14x4_matrix_materialized"] is True
assert cert["credit_firewall"]["e3_b1_route_membership_computed"] is True
assert cert["credit_firewall"]["e3_b1_route_membership"] is False
assert cert["credit_firewall"]["global_H2_mu2_nonexistence_claim"] is False
for key in [
    "e3_literal_cech_preimage_materialized", "genuine_full_surface_H2_mu2_lift_for_e3",
    "e3_kummer_column_materialized", "stage33_12_closed_exact", "stage33_13_released",
    "merge_allowed", "receiver_credit", "endpoint_credit", "theorem_credit",
    "perfect_cuboid_credit",
]:
    assert cert["credit_firewall"][key] is False, key

print(json.dumps({
    "success": True,
    "marker": "V79_B1_FULL_GYSIN_MATRIX_AND_MASK20_NONMEMBERSHIP_COMPLETE",
    "canonical_sha256": EXPECTED,
    "column_masks": [0, 25, 0, 25],
    "rank_f2": 1,
    "image_masks": [0, 25],
    "target_mask": 20,
    "target_in_image": False,
    "b1_route_frozen_only": True,
    "global_H2_mu2_nonexistence_claim": False,
    "merge_allowed": False,
}, sort_keys=True))
