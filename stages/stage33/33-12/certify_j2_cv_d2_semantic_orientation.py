#!/usr/bin/env python3
"""Certify the corrected named-J2 CV d=2 semantic Kc orientation.

This closes only the fixed-marking semantic orientation. It deliberately does
not identify Br[2] canonically with A_T[2], guess a full-surface proper-Br2
coordinate, or place a 75D Kummer matrix column.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
STATE = S33 / "33-05" / "j2-representative-repair-state.json"
R4 = S33 / "33-05" / "j2-r4-hostile-torsor-brauer-kernel-verification.json"
FP = HERE / "j2-brauer-kernel-lattice-fingerprints.json"
ISO = HERE / "j2-kc-transcendental-lattice-isometry.json"
SEM = HERE / "j2-semantic-kc-discriminant-2torsion-target.json"
RIG = HERE / "j2-named-transport-first-column-rigidity.json"
OUT = HERE / "j2-cv-d2-semantic-orientation.json"

LOCKS = {
    STATE: "612d5a9628084cb06cc722d40a1355a92926b742",
    R4: "32be9c1f272a4b12d032bbba00d9bbea1edf2622",
    FP: "572ad201ca859c5970507dbc598ac0489fdd90d10ee74ffc58f5e2f3fba7927e",
    ISO: "b7f2bcfa29c01731ea2f10d22db898ad57317f140b547f91e3d3a27a0faf1010",
    SEM: "0b5d7dfdefbb0f2b7c37396ada35c0bee462dfeb625eb18262be0e862205d8df",
}


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def verify_canonical(path, expected):
    obj = load(path)
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body)
    return obj


state = load(STATE)
r4 = load(R4)
fp = verify_canonical(FP, LOCKS[FP])
iso = verify_canonical(ISO, LOCKS[ISO])
sem = verify_canonical(SEM, LOCKS[SEM])
rig = load(RIG)

credit = state["retained_exact_geometric_credit"]
assert credit["marked_J2"] == [1, 0]
assert credit["minimum_norm"] == 8
assert credit["twisted_kernel_gram"] == [[8, 0], [0, 16]]
assert state["firewalls"]["stage33_05_reclosed"] is True

ilat = r4["integral_lattice_check"]
assert ilat["marked_brauer_coordinate"] == [1, 0]
assert ilat["minimum_norm"] == 8
assert ilat["T_X_J2_gram"] == [[8, 0], [0, 16]]
assert ilat["T_Kc_gram"] == [[4, 0], [0, 8]]

assert fp["source"]["brauer_marked_basis"] == ["beta1=t1/8", "beta2=t2/16"]
norm_map = fp["exact_conclusion"]["minimum_norm_to_functional"]
selected = norm_map[str(ilat["minimum_norm"])]
assert selected == [1, 0]

witness = iso["explicit_discriminant_anti_isometry_witness"]
assert witness["T_generators"] == ["t1/4", "t2/8"]
image_t1_quarter = [Fraction(x) for x in witness["NS_images_semantic_fractional_coordinates"][0]]
doubled = [(2 * x) % 1 for x in image_t1_quarter]
numerator_mod2 = [int(2 * x) & 1 for x in doubled]
u1 = sem["semantic_half_lattice_basis"][0]
assert u1["label"] == "u1"
assert numerator_mod2 == u1["numerator_mod2"]
assert sem["nonzero_semantic_2torsion_candidates"][0]["coordinate_f2"] == [1, 0]
assert rig["fixed_marked_kc_frame"]["basis_labels"] == ["u1", "u2"]
assert rig["named_cv_frame"]["named_J2_coordinate_f2"] == [1, 0]

out = load(OUT)
body = dict(out)
claimed = body.pop("canonical_sha256")
assert claimed == "0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e"
assert claimed == csha(body)
assert out["exact_conclusion"]["named_CV_J2_fixed_marked_Kc_coordinate_f2"] == selected
assert out["anti_isometry_check"]["doubled_image_mod_Z_half_lattice_numerator_mod2"] == numerator_mod2
assert out["exact_conclusion"]["named_CV_J2_semantic_discriminant_label"] == "u1"
assert out["exact_conclusion"]["retained_10D_full_surface_source_coordinate_materialized"] is False
assert out["exact_conclusion"]["locked_75D_target_placed_as_matrix_column"] is False
print(json.dumps({"success": True, "semantic_J2": "u1", "coordinate_f2": [1, 0], "canonical_sha256": claimed}, sort_keys=True))
