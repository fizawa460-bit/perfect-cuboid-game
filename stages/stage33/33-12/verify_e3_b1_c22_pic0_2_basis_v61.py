#!/usr/bin/env python3
"""Verify the exact ordered C22 Pic0[2] basis used by Stage33 e3 A2.4B."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ART = HERE / "e3-b1-c22-pic0-2-basis-v61.json"
PRE = HERE.parent / "33-05" / "j2-corrected-pre-kummer-descent-cochain.json"
SUP = HERE / "j2-corrected-kc-branch-support.json"
ADP = HERE / "j2-corrected-branch-surface-mu2-adapter.json"
V57 = HERE / "e3-mask20-b1-gysin-image-gate-v57.json"


def canonical(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_locked(path: Path, expected_canonical: str, expected_blob: str):
    assert git_blob_sha1(path) == expected_blob, (path, git_blob_sha1(path), expected_blob)
    obj = json.loads(path.read_text())
    claimed = obj.get("canonical_sha256")
    assert claimed == expected_canonical, (path, claimed, expected_canonical)
    body = dict(obj)
    body.pop("canonical_sha256")
    assert canonical(body) == claimed, path
    return obj

# Q(sqrt(2)) represented as a+b*s, s^2=2.
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def neg(x): return (-x[0], -x[1])
def mul(x, y): return (x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def scale(n, x): return (n*x[0], n*x[1])
def power(x, n):
    y = (1, 0)
    for _ in range(n): y = mul(y, x)
    return y

def q(x): return add(add(power(x, 4), scale(-6, power(x, 2))), (1, 0))
def dq(x): return add(scale(4, power(x, 3)), scale(-12, x))

pre = load_locked(PRE, "940df53040c6f5245914effbfb7d752a08c61b6d593586952b322e4069415106", "bb50257bd1cf51639ae53012d8189dda2367b851")
sup = load_locked(SUP, "a9eb7d4d3868581d88ff7ce88c23a42b7010c79c959ead1579738e4a0c56961a", "60bf21201d8ca42857568edbfec0cb9092a2da5d")
adp = load_locked(ADP, "edb98c634c79c97c09b0ea4a14402f32d9c5900c63dd9584eca5ea91b91d6875", "6d0bdebdc1ec5466517caace8191b2968747d2f5")
assert git_blob_sha1(V57) == "3d7b6ad6b4355a0ed379553c4d5fa97fb3209e6e"
v57 = json.loads(V57.read_text())

roots_src = pre["normalization"]["roots"]
assert roots_src == {"r1":"1+sqrt(2)", "r2":"-(1+sqrt(2))", "r3":"sqrt(2)-1", "r4":"1-sqrt(2)"}
assert pre["normalization"]["equation"] == "z^2=q=t^4-6*t^2+1"
assert pre["normalization"]["half_divisor_D"] == "P_r2-P_r4"
assert pre["normalization"]["f2"] == "(t-r2)/(t-r4)"
assert sup["corrected_normalization"]["equation"] == "z^2=t^4-6*t^2+1"
assert sup["corrected_normalization"]["div_f2"] == "2*(P_r2-P_r4)"
assert sup["corrected_normalization"]["f2"] == "(t-r2)/(t-r4)"
assert adp["corrected_pic0_2torsion"]["component_smooth_genus"] == 1
assert adp["corrected_pic0_2torsion"]["class"] == "kappa_D in H^1(C22_bar,mu_2)"

roots = {
    "r1": (1, 1),
    "r2": (-1, -1),
    "r3": (-1, 1),
    "r4": (1, -1),
}
assert len(set(roots.values())) == 4
for name, r in roots.items():
    assert q(r) == (0, 0), (name, q(r))
    assert dq(r) != (0, 0), (name, dq(r))

art = json.loads(ART.read_text())
claimed = art["canonical_sha256"]
body = dict(art)
body.pop("canonical_sha256")
assert claimed == "48ec6b2ffb91d549041ff5ec667ff88d493becf01d89e1bb5974134b3b0a53f6"
assert canonical(body) == claimed
assert art["component"]["roots"] == roots_src
assert art["component"]["smooth_genus"] == 1
assert art["component"]["base_point"] == "P_r4"

basis = art["ordered_c22_pic0_2_basis"]
assert [x["basis_index"] for x in basis] == [1, 2]
assert basis[0]["class_name"] == "kappa_A"
assert basis[0]["half_divisor"] == "D_A=P_r1-P_r4"
assert basis[0]["kummer_function"] == "f_A=(t-r1)/(t-r4)"
assert basis[0]["divisor"] == "div(f_A)=2*D_A"
assert basis[0]["two_torsion"] is True
assert basis[1]["class_name"] == "kappa_D"
assert basis[1]["half_divisor"] == "D=P_r2-P_r4"
assert basis[1]["kummer_function"] == "f2=(t-r2)/(t-r4)"
assert basis[1]["divisor"] == "div(f2)=2*D"
assert basis[1]["two_torsion"] is True

proof = art["basis_proof"]
assert "isomorphism C22_tilde -> Pic0(C22_tilde)" in proof["abel_jacobi_fact"]
assert proof["distinct_points_imply_distinct_classes"] is True
assert proof["pic0_2_dimension_f2"] == 2
assert proof["ordered_basis_complete_for_c22"] is True
assert proof["nonzero_classes"] == ["kappa_A", "kappa_D"]

prog = art["domain_progress"]
assert prog["c22_basis_dimension_materialized"] == 2
assert prog["c21_basis_dimension_materialized"] == 0
assert prog["b1_total_domain_dimension"] == 4
assert prog["b1_ordered_basis_complete"] is False
assert prog["proper14_image_columns_materialized"] == 1
assert v57["exact_b1_route_geometry"]["branch_H1_total_dimension_f2"] == 4
assert v57["exact_b1_route_geometry"]["required_marked_matrix_shape"] == [14, 4]
assert v57["e3_membership_gate"]["proper14_mask_decimal"] == 20
assert v57["e3_membership_gate"]["membership_in_im_Phi_B1"] == "OPEN_NOT_COMPUTED"

fw = art["credit_firewall"]
for key in ["c21_basis_materialized", "full_b1_domain_basis_materialized", "new_proper14_gysin_column_for_kappa_A_materialized", "b1_14x4_matrix_materialized", "e3_mask20_membership_computed", "literal_e3_cech_geometry_materialized", "genuine_full_surface_h2_mu2_lift_for_e3", "e3_kummer_column_materialized", "stage33_12_closed_exact", "stage33_13_released", "merge_allowed"]:
    assert fw[key] is False, key
assert fw["stage33_progress"] == "6/11"
assert art["status"] == "PASS_EXACT_C22_PIC0_2_ORDERED_BASIS_MATERIALIZED_C21_AND_PROPER14_IMAGES_OPEN"
print(json.dumps({"success": True, "schema": art["schema"], "c22_basis_dimension": 2, "c21_basis_dimension": 0, "b1_matrix_materialized": False, "e3_membership_computed": False, "stage33_progress": "6/11", "merge_allowed": False}, sort_keys=True))
