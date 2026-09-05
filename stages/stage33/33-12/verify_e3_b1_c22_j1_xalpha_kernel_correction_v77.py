#!/usr/bin/env python3
"""Verify V77: exact x-alpha kernel correction for named source J1."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
R05 = STAGE / "33-05"
CERT = HERE / "e3-b1-c22-j1-xalpha-kernel-correction-v77.json"
XALPHA = R05 / "xalpha_pair_galois_repair.py"
V65 = HERE / "e3-b1-j1-marked-kc-discriminator-gate-v65.json"
V71 = HERE / "e3-b1-c22-j1-cv-e2-cocycle-v71.json"
V73 = HERE / "e3-b1-c22-j1-translation-torsor-v73.json"
V75 = HERE / "e3-b1-c22-j1-generic-quotient-discriminator-rejection-v75.json"
HOSTILE = R05 / "j2-r4-hostile-torsor-brauer-kernel-verification.json"
FINGERPRINTS = HERE / "j2-brauer-kernel-lattice-fingerprints.json"

EXPECTED = "d2f803ab0cb394389c1fedf8f94e237ce82702743d0240a4f4b2fe73a44d5e98"
LOCKS = {
    XALPHA: "b7f37df50a123ef6c972aa210e7efb5f16535f76",
    V65: "e3634d9c8ed0f4f58ff4132f7bd5822f60fa23c3",
    V71: "5073a38366aa8715b5ce27115a1d055386a0869a",
    V73: "277ec4bfd86a118b25e45632ce4a02fe3af87cc1",
    V75: "6d316b60c933b446004297d9d32d0a7ef6c1c357",
    HOSTILE: "32be9c1f272a4b12d032bbba00d9bbea1edf2622",
    FINGERPRINTS: "ba48b42a2af3afeaf03d031f8ee6e11fa73df832",
}
CANONICALS = {
    V65: "7ebef9a6182522f772f198d8c1572acc48cd8441f6158312d1f3f3f2c7fcc01c",
    V71: "3e9409ee7537ab4edb12e2416745bbd074f1cc1b02a4fc8a92be643075b8569a",
    V73: "b6a8dd83cd83547525e8ff328cccc1572791c52bea6061137c2bc59a134fa09d",
    V75: "22b166d44d516a5e0cb57bf582a21144d40b0035489a29036f86dc0944ce1192",
    FINGERPRINTS: "572ad201ca859c5970507dbc598ac0489fdd90d10ee74ffc58f5e2f3fba7927e",
}


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def locked(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    expected = CANONICALS[path]
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


def det2(g):
    return g[0][0] * g[1][1] - g[0][1] * g[1][0]


# The exact algebraic x-alpha repair is immutable by blob.  It computes an
# explicit square witness for the Mobius-section / s=1 difference and proves
# that difference is J1, then identifies {J2,q1} as a basis of the geometric
# Brauer quotient.  V77 consumes that already-certified exact asset rather than
# re-running its SymPy producer in ordinary CI.
for path, expected in LOCKS.items():
    assert blob_sha(path) == expected, path
xtext = XALPHA.read_text(encoding="utf-8")
for needle in [
    'square_witness = p + qcoef*z',
    'assert reduce_z2(square_witness**2-u/f1) == 0',
    'J1_relation = [1,0,0,0,0]',
    '"J1_in_xalpha_image_exact": True',
    'quotient_basis = ["J2", "q1"]',
    '"brauer_quotient_dimension": 2',
    '"xalpha_image_spanned_exactly": True',
]:
    assert needle in xtext, needle

v65, v71, v73, v75, fp = map(locked, [V65, V71, V73, V75, FINGERPRINTS])
hostile = json.loads(HOSTILE.read_text(encoding="utf-8"))

# Retain the literal E[2] cocycle and explicit quartic, but distinguish the
# Kummer E[2] class from its image in H^1(E).
assert v71["j1_full_l_representative"]["pair_in_L"] == "(f1,1)"
assert v71["cv_cocycle"]["cocycle_nonzero"] is True
assert v71["cv_cocycle"]["cocycle_bits_in_fixed_basis"] == [0, 1]
assert v71["cv_cocycle"]["xi_rho"] == "Tr"
assert v73["translation_torsor"]["twisting_squareclass"] == "d=f1"
assert v73["translation_torsor"]["jacobian"] == "E: y^2=x*(x^2+a*x+b)"
assert v75["generic_quotient_replay"]["d_survives_in_quotient_equation"] is False
assert v75["generic_quotient_replay"]["same_generic_target_as_j2"] is True

# V65 had excluded the zero class before the x-alpha kernel fact was wired into
# this frontier.  Record exactly what is being superseded.
assert v65["locked_frontier"]["J1_marked_kc_coordinate_candidates_f2"] == [[0, 1], [1, 1]]
assert v65["target_discriminator_fingerprints"]["u2"]["minimum_norm"] == 4
assert v65["target_discriminator_fingerprints"]["u1_plus_u2"]["minimum_norm"] == 12

# Reuse the already-hostile-audited Ogg-Shafarevich/Caldararu integral-kernel
# dictionary.  A zero Brauer/OS class has kernel all of T(Kc), determinant 32.
cald = hostile["external_theorems"]["caldararu"]
assert "Ogg-Shafarevich" in cald["elliptic_torsor_dictionary_sections_1_15_1_16"]
assert "ker alpha" in cald["elliptic_torsor_dictionary_sections_1_15_1_16"]
tkc = hostile["integral_lattice_check"]["T_Kc_gram"]
assert tkc == [[4, 0], [0, 8]] and det2(tkc) == 32
pull = [[2*x for x in row] for row in tkc]
assert pull == [[8, 0], [0, 16]] and det2(pull) == 128
assert det2(pull) // det2(tkc) == 4  # index^2=4, hence index=2
assert fp["kernel_lattices"]["0,1"]["minimum_norm"] == 4
assert fp["kernel_lattices"]["1,0"]["minimum_norm"] == 8
assert fp["kernel_lattices"]["1,1"]["minimum_norm"] == 12

cert = json.loads(CERT.read_text(encoding="utf-8"))
body = dict(cert)
claimed = body.pop("canonical_sha256")
assert claimed == EXPECTED == csha(body)
assert cert["xalpha_repair_replay"]["J1_in_xalpha_image_exact"] is True
assert cert["xalpha_repair_replay"]["explicit_brauer_quotient_basis"] == ["J2", "q1"]
assert cert["cohomological_correction"]["J1_geometric_brauer_class"] == "ZERO"
assert cert["cohomological_correction"]["J1_image_in_H1_E"] == "ZERO"
assert cert["cohomological_correction"]["J1_ogg_shafarevich_class"] == "ZERO"
assert cert["cohomological_correction"]["E2_nonzero_implies_H1_E_nonzero"] is False
assert cert["torsor_lattice_consequence"]["T_X_J1_gram"] == tkc
assert cert["torsor_lattice_consequence"]["T_X_J1_minimum_norm"] == 4
assert cert["torsor_lattice_consequence"]["minimum_norm_4_means_u2_here"] is False
assert cert["torsor_lattice_consequence"]["pullback_index_in_T_X_J1"] == 2
assert cert["supersession"]["v65_J1_candidates_u2_u1plusu2_valid_for_actual_Brauer_OS_class"] is False
assert cert["supersession"]["v75_4_or_12_next_kernel_contract_valid"] is False
assert cert["supersession"]["J2_u1_authority_revoked"] is False
assert cert["supersession"]["v71_literal_E2_cocycle_revoked"] is False
assert cert["supersession"]["v73_quartic_revoked"] is False
assert cert["proper14_boundary"]["zero_Brauer_OS_image_automatically_sets_proper14_column3_to_zero"] is False
assert cert["proper14_boundary"]["column3_marked_coordinate_materialized"] is False
assert cert["credit_firewall"]["stage33_progress"] == "6/11"
for key in [
    "j1_nonzero_marked_kc_coordinate_selected", "identity_vs_shear_selected",
    "new_marked_proper14_gysin_column_materialized", "b1_14x4_matrix_materialized",
    "e3_mask20_membership_computed", "genuine_full_surface_H2_mu2_lift_for_e3",
    "e3_kummer_column_materialized", "stage33_12_closed_exact",
    "stage33_13_released", "receiver_credit", "theorem_credit",
    "endpoint_credit", "perfect_cuboid_credit", "merge_allowed",
]:
    assert cert["credit_firewall"][key] is False, key

print(json.dumps({
    "success": True,
    "marker": "V77_J1_XALPHA_KERNEL_CORRECTION_COMPLETE",
    "canonical_sha256": EXPECTED,
    "J1_geometric_brauer_OS_class": "ZERO",
    "J1_E2_cocycle_nonzero": True,
    "J1_H1_E_class": "ZERO",
    "T_X_J1_gram": tkc,
    "minimum_norm": 4,
    "minimum_norm_does_not_select_u2": True,
    "old_4_12_gate_retired": True,
    "proper14_column3": None,
    "merge_allowed": False,
}, sort_keys=True))
