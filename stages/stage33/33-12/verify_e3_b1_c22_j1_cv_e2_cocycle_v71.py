#!/usr/bin/env python3
"""Verify Stage33 V71 J1-specific Creutz--Viray E[2] cocycle materialization."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
D05 = STAGE / "33-05"
CERT = HERE / "e3-b1-c22-j1-cv-e2-cocycle-v71.json"
V63 = HERE / "e3-b1-c22-kappa-a-literal-cech-lift-v63.json"
V64 = HERE / "e3-b1-c22-named-torsion-normalization-bridge-v64.json"
J2CV = D05 / "j2-corrected-cv-e2-cocycle.json"
LCE = D05 / "lce_filtered_quotient_skeleton.py"
NORM = D05 / "normalization_galois_skeleton.py"

EXPECTED = "3e9409ee7537ab4edb12e2416745bbd074f1cc1b02a4fc8a92be643075b8569a"
SOURCE_BLOBS = {
    V63: "3a966544378e2302f5a591e2162c30dbb5a3732e",
    V64: "cd112667605f7d73736827269bacff4de7ef0fde",
    J2CV: "5165ee50011382f6cbe34340d51538a35f9fc942",
    LCE: "ac8bb0096714d85e67efd55f8bb4730e1d1169ce",
    NORM: "139a309c52a6646e649d37bdb03c3bb535d29cf1",
}
SOURCE_CANONICAL = {
    V63: "7714c722f7f30cae1fac03edd34821d1e84372bf3d7663dc2c62a98fde6b186c",
    V64: "55679ba16710e3b78ab46ab699ea73ecc3fc56faab4cb7edc5a02e487df3de38",
    J2CV: "8440400fd7eff183830bb16e991a6fb6f253b1774a76384ed2a3dc8adc951312",
}

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def locked_json(path: Path, expected: str):
    assert git_blob_sha(path) == SOURCE_BLOBS[path], path
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj

for path, sha in SOURCE_BLOBS.items():
    assert git_blob_sha(path) == sha, path

cert = json.loads(CERT.read_text(encoding="utf-8"))
body = dict(cert)
claimed = body.pop("canonical_sha256")
assert claimed == EXPECTED == csha(body)

v63 = locked_json(V63, SOURCE_CANONICAL[V63])
v64 = locked_json(V64, SOURCE_CANONICAL[V64])
j2 = locked_json(J2CV, SOURCE_CANONICAL[J2CV])
lce = LCE.read_text(encoding="utf-8")
norm = NORM.read_text(encoding="utf-8")

# The retained quotient source itself names J1 by the first-component pair (f1,1).
assert 'f1 = sp.cancel((t-r1)/(t-r4))' in lce
assert '{"class":"J1","pair_in_L":"(f1,1)"' in lce
assert 'assert sp.cancel(f1*f2*f3 - q/(t-r4)**4) == 0' in lce
assert 'q = sp.expand(t**4 - 6*t**2 + 1)' in lce
assert 'common_normalization":"z^2=t^4-6*t^2+1"' in norm

# V63/V64 independently identify the literal branch class as the same J1.
assert v63["literal_symbol"]["f_A"] == "(t-r1)/(t-r4)"
assert v63["literal_symbol"]["branch_input"] == "kappa_A=[P_r1-P_r4]"
assert v64["exact_bridge"]["kappa_A"]["named_torsion"] == "J1"

j1 = cert["j1_full_l_representative"]
assert j1["pair_in_L"] == "(f1,1)"
assert j1["matches_v63_f_A"] is True
assert j1["named_branch_class"] == "kappa_A=J1"
assert j1["nonzero_square_test"]["f1_K_square"] is False
assert j1["nonzero_square_test"]["f1_over_q_identity"] == "f1/q=1/((t-r2)*(t-r3)*(t-r4)^2)"
assert j1["nonzero_square_test"]["f1_over_q_K_square"] is False
assert j1["nonzero_square_test"]["f1_square_in_F"] is False
assert j1["full_L_class_nonzero"] is True

# Reuse only the exact Bplus partition geometry from J2: the coefficient squareclass is now f1.
part = j2["partition_2torsion_identification"]
assert part["Bplus_partition_point"] == "Tr=(r,0)"
assert part["exact_square_identity"].startswith("(-1/(t*r))*Gplus/(X-r)=")
assert j2["cv_lemma_4_6"]["chi_tilde_on_four_branch_points"] == [1, 1, 0, 0]
assert j2["cv_lemma_4_6"]["g_ell_rho"] == 1
assert j2["cv_lemma_4_6"]["fixed_E2_basis"] == ["T0=(0,0)", "Tr=(r,0)"]

cv = cert["cv_cocycle"]
assert cv["splitting_field"] == "Kgeom(sqrt(f1))"
assert cv["component_character_support_on_four_branch_points"] == [1, 1, 0, 0]
assert cv["partition_2torsion_point"] == "Tr=(r,0)"
assert cv["xi_rho"] == "Tr"
assert cv["cocycle_bits_in_fixed_basis"] == [0, 1]
assert cv["cocycle_condition_verified"] is True
assert cv["cocycle_nonzero"] is True
assert cv["j2_cocycle_relabelled_as_j1"] is False

nxt = cert["next_translation_torsor_contract"]
assert nxt["translation_point"] == "Tr"
assert nxt["twisting_squareclass"] == "d=f1"
assert nxt["semilinear_action"] == "tilde_rho=tau_Tr o rho"
assert nxt["expected_quartic_to_materialize_next"] == "d*V^2=N^4-2*a*d*N^2*Z^2+d^2*q^2*Z^4"
assert nxt["torsor_materialized"] is False
assert nxt["twisted_kernel_minimum_norm_materialized"] is False

fw = cert["credit_firewall"]
for key in (
    "j1_marked_kc_coordinate_selected",
    "identity_vs_shear_selected",
    "j1_translation_torsor_materialized",
    "j1_twisted_kernel_minimum_norm_selected",
    "new_marked_proper14_gysin_column_materialized",
    "b1_14x4_matrix_materialized",
    "e3_mask20_membership_computed",
    "genuine_full_surface_H2_mu2_lift_for_e3",
    "e3_kummer_column_materialized",
    "D2_closed",
    "stage33_12_closed",
    "stage33_13_released",
    "perfect_cuboid_credit",
    "merge_allowed",
):
    assert fw[key] is False, key

print(json.dumps({
    "success": True,
    "marker": "V71_J1_SPECIFIC_CV_E2_COCYCLE_REPLAY_COMPLETE",
    "canonical_sha256": EXPECTED,
    "J1_pair_in_L": "(f1,1)",
    "splitting_field": "Kgeom(sqrt(f1))",
    "xi_rho": "Tr",
    "cocycle_bits": [0, 1],
    "torsor_materialized": False,
    "identity_vs_shear_selected": False,
    "merge_allowed": False,
}, sort_keys=True))
