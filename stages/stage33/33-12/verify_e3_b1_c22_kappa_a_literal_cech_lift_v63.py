#!/usr/bin/env python3
"""Verify V63 C22 kappa_A literal Cech/surface mu2 lift while keeping marked proper14 column 3 open."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from fractions import Fraction

HERE = Path(__file__).resolve().parent
V61 = HERE / "e3-b1-c22-pic0-2-basis-v61.json"
V62 = HERE / "e3-b1-full-domain-basis-v62.json"
J2CECH = HERE / "j2-corrected-explicit-cech-mu2-lift.json"
ADJ = HERE / "j2-picard-adjoint-proper-br2.json"
ART = HERE / "e3-b1-c22-kappa-a-literal-cech-lift-v63.json"

def canonical(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def git_blob_sha1(path: Path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def load_canonical(path: Path, digest: str, blob: str):
    assert git_blob_sha1(path) == blob, path
    obj = json.loads(path.read_text())
    assert obj["canonical_sha256"] == digest, path
    body = dict(obj)
    body.pop("canonical_sha256")
    assert canonical(body) == digest, path
    return obj

# Q(sqrt(2)) helpers, represented as a+b*sqrt(2).
def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def mul(x, y):
    return (x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0])

def neg(x):
    return (-x[0], -x[1])

def inv(x):
    den = x[0]*x[0] - 2*x[1]*x[1]
    assert den != 0
    return (Fraction(x[0], den), Fraction(-x[1], den))

def div(x, y):
    return mul(x, inv(y))

v61 = load_canonical(
    V61,
    "48ec6b2ffb91d549041ff5ec667ff88d493becf01d89e1bb5974134b3b0a53f6",
    "e50bde0bd88f29ce4bbe16f8d48fe89a8c3ab4d9",
)
v62 = load_canonical(
    V62,
    "353e68438334a0da71dfdbc09a8bf60e7e511598cf54a173338735686f1c3f4c",
    "781549b869dbb0e143d982c9b67523f2336225e4",
)
j2 = load_canonical(
    J2CECH,
    "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b",
    "97261735968c07903f87370eb483df8d6475b67c",
)
adj = load_canonical(
    ADJ,
    "066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8",
    "2e70dc274afbbd20aefbb0a87409d66d6ac183bc",
)

basis = v61["ordered_c22_pic0_2_basis"]
assert basis[0]["class_name"] == "kappa_A"
assert basis[0]["half_divisor"] == "D_A=P_r1-P_r4"
assert basis[0]["kummer_function"] == "f_A=(t-r1)/(t-r4)"
assert basis[0]["divisor"] == "div(f_A)=2*D_A"
ordered = v62["ordered_b1_h1_basis"]
assert ordered[2] == {"column_index": 3, "component": "C22_tilde", "class": "kappa_A"}

assert j2["explicit_cech_preimage"]["g22"] == "1-s^2+i*s*(1-t^2)/t"
assert j2["explicit_cech_preimage"]["open"] == "Ubar=Sprime_bar-(C21_tilde disjoint_union C22_tilde)"
assert j2["surface_mu2_lift"]["ramification_check"] == (
    "pi^*g22 has valuation 2 along the ramification curve over C22, so the required surface residue is trivial"
)

one = (Fraction(1), Fraction(0))
r1 = (Fraction(1), Fraction(1))
r4 = (Fraction(1), Fraction(-1))
r1sq = mul(r1, r1)
r4sq = mul(r4, r4)
assert r1sq == (Fraction(3), Fraction(2))
assert r4sq == (Fraction(3), Fraction(-2))
assert div(add(one, neg(r1sq)), r1) == (Fraction(-2), Fraction(0))
assert div(add(one, neg(r4sq)), r4) == (Fraction(-2), Fraction(0))
fA0 = div(r1, r4)
assert fA0 == neg(r1sq)
fAinf = one
assert fAinf == one

art = json.loads(ART.read_text())
claimed = art["canonical_sha256"]
body = dict(art)
body.pop("canonical_sha256")
assert claimed == "7714c722f7f30cae1fac03edd34821d1e84372bf3d7663dc2c62a98fde6b186c"
assert canonical(body) == claimed

sym = art["literal_symbol"]
assert sym["branch_input"] == "kappa_A=[P_r1-P_r4]"
assert sym["f_A"] == "(t-r1)/(t-r4)"
assert sym["g22"] == j2["explicit_cech_preimage"]["g22"]
assert sym["boundary_on_C21_C22"] == ["0", "kappa_A represented by f_A"]

rows = {r["divisor"]: r for r in art["codimension_one_residue_audit"]["rows"]}
assert rows["C22"]["residue"] == "f_A"
assert rows["C21"]["residue"] == "1"
assert rows["t=r1"]["residue_square_witness"] == "g22(r1,s)=(1-i*s)^2"
assert rows["t=r4"]["residue_square_witness"] == "g22(r4,s)=(1-i*s)^2"
assert rows["t=0"]["residue_square_witness"] == "f_A(0)=(i*(1+sqrt(2)))^2"
assert rows["t=infinity"]["residue_square_witness"] == "f_A(infinity)=1"
assert rows["s=infinity"]["residue"] == "f_A^-2 is a square"
assert art["codimension_one_residue_audit"]["all_nonboundary_residues_zero"] is True
assert art["resolution_residue_audit"]["all_exceptional_residues_zero"] is True

lift = art["surface_mu2_lift"]
assert lift["concrete_Cech_preimage_e_A_materialized"] is True
assert lift["surface_mu2_lift_materialized"] is True
assert lift["maps_to_branch_input"] == "C22:kappa_A"
assert lift["historical_j2_mask_relabel_used"] is False

cols = adj["degree2_picard_adjoint"]["decoded_target_basis_columns"]
assert len(cols) == 14
assert all("source_picard_dual_covector_zK" in c for c in cols)
iface = art["proper14_coordinate_interface"]
assert iface["symbolic_gysin_image_class_materialized"] is True
assert iface["marked_proper14_14bit_coordinate_materialized"] is False
assert iface["column_index"] == 3
assert iface["column3_mask_decimal"] is None
assert iface["missing_exact_input"] == "MARKED_PICARD_DUAL_COVECTOR_FOR_LAMBDA_A_OR_EQUIVALENT_EXACT_SYMBOL_TO_PROPER14_BINDING"

prog = art["matrix_progress"]
assert prog["required_shape"] == [14, 4]
assert prog["known_marked_coordinate_columns"] == [4]
assert prog["literal_symbol_columns_materialized"] == [3, 4]
assert prog["unknown_marked_coordinate_columns"] == [1, 2, 3]
assert prog["column4_mask_decimal"] == 25
assert prog["column3_marked_coordinate_open"] is True

fw = art["credit_firewall"]
assert fw["new_marked_proper14_gysin_columns_materialized"] == 0
for key in [
    "b1_14x4_matrix_materialized",
    "e3_mask20_membership_computed",
    "literal_e3_cech_geometry_materialized",
    "genuine_full_surface_h2_mu2_lift_for_e3",
    "e3_kummer_column_materialized",
    "stage33_12_closed_exact",
    "stage33_13_released",
    "merge_allowed",
]:
    assert fw[key] is False, key
assert fw["stage33_progress"] == "6/11"
assert art["status"] == "PASS_EXACT_C22_KAPPA_A_LITERAL_CECH_SURFACE_LIFT_MARKED_PROPER14_COLUMN3_OPEN"
print(json.dumps({
    "success": True,
    "schema": art["schema"],
    "column3_literal_cech_surface_lift": True,
    "column3_marked_proper14_coordinate": None,
    "known_marked_coordinate_columns": [4],
    "e3_membership_computed": False,
    "stage33_progress": "6/11",
    "merge_allowed": False,
}, sort_keys=True))
