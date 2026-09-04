#!/usr/bin/env python3
"""Verify transfer of the V61 C22 basis to C21 and the full ordered B1 H1 basis."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
V61 = HERE / "e3-b1-c22-pic0-2-basis-v61.json"
V57 = HERE / "e3-mask20-b1-gysin-image-gate-v57.json"
ADP = HERE / "j2-corrected-branch-surface-mu2-adapter.json"
PRE = HERE.parent / "33-05" / "j2-corrected-pre-kummer-descent-cochain.json"
ART = HERE / "e3-b1-full-domain-basis-v62.json"


def canonical(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_canonical(path: Path, digest: str, blob: str):
    assert git_blob_sha1(path) == blob
    obj = json.loads(path.read_text())
    assert obj["canonical_sha256"] == digest
    body = dict(obj); body.pop("canonical_sha256")
    assert canonical(body) == digest
    return obj

v61 = load_canonical(V61, "48ec6b2ffb91d549041ff5ec667ff88d493becf01d89e1bb5974134b3b0a53f6", "e50bde0bd88f29ce4bbe16f8d48fe89a8c3ab4d9")
adp = load_canonical(ADP, "edb98c634c79c97c09b0ea4a14402f32d9c5900c63dd9584eca5ea91b91d6875", "6d0bdebdc1ec5466517caace8191b2968747d2f5")
pre = load_canonical(PRE, "940df53040c6f5245914effbfb7d752a08c61b6d593586952b322e4069415106", "bb50257bd1cf51639ae53012d8189dda2367b851")
assert git_blob_sha1(V57) == "3d7b6ad6b4355a0ed379553c4d5fa97fb3209e6e"
v57 = json.loads(V57.read_text())

geom = v57["exact_b1_route_geometry"]
assert geom["quotient_branch"] == "C21_tilde disjoint_union C22_tilde"
assert geom["C21_relation_to_C22"] == "complex-conjugate branch component under i -> -i"
assert geom["C21_genus"] == geom["C22_genus"] == 1
assert geom["H1_dimension_per_genus1_component_f2"] == 2
assert geom["branch_H1_total_dimension_f2"] == 4
assert adp["double_cover_geometry"]["branch_over_Qi"] == ["C21: A3+i*A2=0", "C22: A3-i*A2=0"]
assert pre["full_split_pair"]["cc_action"] == "component swap; cc(ell)=(1,f2)"
assert v61["basis_proof"]["ordered_basis_complete_for_c22"] is True
assert v61["domain_progress"]["c22_basis_dimension_materialized"] == 2

art = json.loads(ART.read_text())
claimed = art["canonical_sha256"]
body = dict(art); body.pop("canonical_sha256")
assert claimed == "353e68438334a0da71dfdbc09a8bf60e7e511598cf54a173338735686f1c3f4c"
assert canonical(body) == claimed
cc = art["conjugate_branch_identification"]
assert cc["C21_equation"] == "A3+i*A2=0"
assert cc["C22_equation"] == "A3-i*A2=0"
assert cc["component_action"] == "cc(C22_tilde)=C21_tilde and cc(C21_tilde)=C22_tilde"
assert cc["C21_genus"] == cc["C22_genus"] == 1
proof = art["basis_transfer_proof"]
assert proof["cc_is_curve_isomorphism"] is True
assert proof["cc_induces_pic0_2_isomorphism"] is True
assert proof["v61_ordered_basis_transfers_to_ordered_basis"] is True
assert proof["c21_pic0_2_dimension_f2"] == 2

c21 = art["ordered_c21_pic0_2_basis"]
assert [x["class_name"] for x in c21] == ["cc(kappa_A)", "cc(kappa_D)"]
assert c21[0]["kummer_function_on_conjugate_normalization"] == "cc(f_A)=f_A=(t-r1)/(t-r4)"
assert c21[1]["kummer_function_on_conjugate_normalization"] == "cc(f2)=f2=(t-r2)/(t-r4)"
ordered = art["ordered_b1_h1_basis"]
assert [(x["column_index"], x["component"], x["class"]) for x in ordered] == [
    (1, "C21_tilde", "cc(kappa_A)"),
    (2, "C21_tilde", "cc(kappa_D)"),
    (3, "C22_tilde", "kappa_A"),
    (4, "C22_tilde", "kappa_D"),
]
prog = art["domain_progress"]
assert prog["c21_basis_dimension_materialized"] == 2
assert prog["c22_basis_dimension_materialized"] == 2
assert prog["b1_total_domain_dimension"] == 4
assert prog["b1_ordered_basis_complete"] is True
assert prog["required_proper14_matrix_shape"] == [14, 4]
assert prog["known_exact_image_columns"]["column4"]["proper14_mask_decimal"] == 25
assert prog["unknown_image_columns"] == [1, 2, 3]
assert v57["existing_exact_j2_point_in_route"]["proper14_brauer_image_mask_decimal"] == 25

fw = art["credit_firewall"]
assert fw["new_proper14_gysin_columns_materialized"] == 0
for key in ["b1_14x4_matrix_materialized", "e3_mask20_membership_computed", "literal_e3_cech_geometry_materialized", "genuine_full_surface_h2_mu2_lift_for_e3", "e3_kummer_column_materialized", "stage33_12_closed_exact", "stage33_13_released", "merge_allowed"]:
    assert fw[key] is False, key
assert fw["stage33_progress"] == "6/11"
assert art["status"] == "PASS_EXACT_FULL_B1_ORDERED_H1_DOMAIN_BASIS_MATERIALIZED_ONLY_COLUMN4_IMAGE_KNOWN"
print(json.dumps({"success": True, "schema": art["schema"], "ordered_domain_dimension": 4, "known_image_columns": [4], "unknown_image_columns": [1,2,3], "matrix_materialized": False, "e3_membership_computed": False, "stage33_progress": "6/11", "merge_allowed": False}, sort_keys=True))
