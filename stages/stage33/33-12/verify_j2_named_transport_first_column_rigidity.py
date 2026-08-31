#!/usr/bin/env python3
"""Network-free replay of the named-J2 first-column orientation reduction."""
from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-named-transport-first-column-rigidity.json"
PAIRING = HERE / "j2-named-cv-special-brauer-pairing-orbit.json"
AUT = HERE / "j2-kc-automorphism-mod2-marking-rejection.json"
SEM = HERE / "j2-semantic-kc-discriminant-2torsion-target.json"
TARGET = HERE / "j2-named-v4-h1-target-before-source-orientation.json"
EXPECTED = "3c6842cde33d43a0466431c901899f5c730d3790edb1786ab13f4cf8722d1d2c"


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body)
    return obj


def git_blob_sha1(path):
    payload = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(payload)).encode() + b"\0" + payload).hexdigest()


def det2(m):
    return (m[0][0] * m[1][1] - m[0][1] * m[1][0]) & 1


parser = argparse.ArgumentParser()
parser.add_argument(
    "--logic-only",
    action="store_true",
    help="Replay the certificate algebra without opening upstream source files.",
)
args = parser.parse_args()

cert = locked(CERT, EXPECTED)
locks = cert["source_locks"]
assert locks == {
    "named_cv_special_brauer_pairing_orbit_git_blob_sha1": "5ef1d0549cd0c2e48ae4ffd2af99b6b6577e5b27",
    "kc_automorphism_mod2_marking_rejection_canonical_sha256": "dfbd85c56c3c9c29238e1da633baec2ed2bd8cc58021c8137e95fb1cf9cd74fb",
    "semantic_kc_discriminant_2torsion_target_canonical_sha256": "0b5d7dfdefbb0f2b7c37396ada35c0bee462dfeb625eb18262be0e862205d8df",
    "named_v4_h1_target_before_source_orientation_canonical_sha256": "4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3",
}

# Replay GL(2,F2) exhaustively rather than trusting the stored list.
gl2 = []
for a, b, c, d in product((0, 1), repeat=4):
    m = [[a, b], [c, d]]
    if det2(m) == 1:
        gl2.append(m)
gl2.sort()
stored_gl2 = sorted(cert["linear_transport_reduction"]["all_gl2_f2_matrices_row_major"])
assert gl2 == stored_gl2
assert len(gl2) == cert["linear_transport_reduction"]["gl2_f2_order"] == 6

first_columns = [(m[0][0], m[1][0]) for m in gl2]
counts = {v: first_columns.count(v) for v in set(first_columns)}
expected_candidates = {(1, 0), (0, 1), (1, 1)}
assert set(first_columns) == expected_candidates
assert set(map(tuple, cert["fixed_marked_kc_frame"]["nonzero_candidate_coordinates_f2"])) == expected_candidates
assert set(map(tuple, cert["linear_transport_reduction"]["possible_first_columns_f2"])) == expected_candidates
assert counts == {v: 2 for v in expected_candidates}
assert cert["linear_transport_reduction"]["number_of_gl2_completions_per_first_column"] == 2

assert cert["named_cv_frame"]["named_J2_coordinate_f2"] == [1, 0]
assert cert["named_cv_frame"]["marked_kc_identification_asserted"] is False
assert cert["fixed_marked_kc_frame"]["transcendental_lattice_gram"] == [[4, 0], [0, 8]]
assert cert["fixed_marked_kc_frame"]["integral_isometry_mod2_image"] == "identity_only"
assert cert["fixed_marked_kc_frame"]["candidate_vectors_are_absolute_in_the_fixed_marking"] is True
assert cert["selected_marked_kc_coordinate_f2"] is None
assert cert["remaining_interface"] == "IMAGE_OF_NAMED_CV_J2_IN_FIXED_MARKED_KC_BR2_F2_2"

locked_target = cert["locked_named_target"]
assert locked_target == {
    "retained_H1_dimension_f2": 75,
    "coordinate_weight": 15,
    "nonzero": True,
    "packed_coordinate_hex": "0000004800194b018a00",
    "target_image_materialized": True,
    "retained_10D_source_coordinate_materialized": False,
    "target_placed_as_75x10_matrix_column": False,
    "finite_v4_kummer_columns_materialized": 0,
}
assert not any(cert["firewalls"].values())

if not args.logic_only:
    assert git_blob_sha1(PAIRING) == locks["named_cv_special_brauer_pairing_orbit_git_blob_sha1"]
    pairing = json.loads(PAIRING.read_text(encoding="utf-8"))
    aut = locked(AUT, locks["kc_automorphism_mod2_marking_rejection_canonical_sha256"])
    sem = locked(SEM, locks["semantic_kc_discriminant_2torsion_target_canonical_sha256"])
    target = locked(TARGET, locks["named_v4_h1_target_before_source_orientation_canonical_sha256"])

    assert pairing["weil_pairing_evaluation"]["selected_orbit_invariant"] == [1, 0]
    assert pairing["firewalls"]["pairing_orbit_bits_equal_marked_brauer_bits"] is False
    assert pairing["firewalls"]["j2_marked_coordinate_selected"] is False
    assert aut["all_integral_isometries_reduce_to_identity_mod2"] is True
    assert aut["j2_coordinate_materialized"] is False
    sem_candidates = [x["coordinate_f2"] for x in sem["nonzero_semantic_2torsion_candidates"]]
    assert set(map(tuple, sem_candidates)) == expected_candidates
    assert sem["j2_coordinate_materialized"] is False
    boundary = target["exact_information_boundary"]
    assert boundary["named_J2_V4_H1_target_image_materialized"] is True
    assert boundary["named_J2_V4_H1_target_image_nonzero"] is True
    assert boundary["named_J2_retained_10D_source_coordinate_materialized"] is False
    assert boundary["named_J2_target_placed_as_75x10_matrix_column"] is False
    assert boundary["finite_v4_kummer_columns_materialized"] == 0
    assert target["retained_H1_projection"]["coordinate_weight"] == 15

print(json.dumps({
    "success": True,
    "certificate_sha256": EXPECTED,
    "mode": "logic-only" if args.logic_only else "full-source-replay",
    "gl2_f2_order": len(gl2),
    "possible_named_images": [list(v) for v in sorted(expected_candidates)],
    "completions_per_image": 2,
    "candidate_selected": False,
    "matrix_columns_materialized": 0,
}, sort_keys=True))
