#!/usr/bin/env python3
"""Independent network-free replay of the named-J2 75D target image."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
S33 = HERE.parent
CERT = HERE / "j2-named-v4-h1-target-before-source-orientation.json"
PIC = S33 / "33-07" / "retained-picard-base-sparse.json"
TARGET = HERE / "full-surface-pic2-kummer-target.json"
CT = HERE / "j2-ct-six-kc-support-fullpic64-pullbacks.json"
CC = HERE / "j2-cc-actual-cech-global-square-overlap.json"
EXPECTED = "4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3"


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


cert = locked(CERT, EXPECTED)
pic = locked(PIC, "e41df3f84760b941440035a388baac88602126c80140139ddf9c187bedf0bb49")
target = locked(TARGET, "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890")
ct_cert = locked(CT, "592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d")
cc_cert = locked(CC, "82ac2b6fe8d023c915e9cf3bb8ff38d4782dbec47f98e2593f964ea020ccc6fd")


def expand(obj):
    answer = []
    for row in obj["matrix_64x64_sparse_rows_1based"]:
        dense = [0] * 64
        for column, value in row:
            dense[column - 1] = value & 1
        answer.append(dense)
    return answer


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]


def rowmul(vector, matrix):
    return [sum(vector[i] * matrix[i][j] for i in range(64)) & 1 for j in range(64)]


identity = [[int(i == j) for j in range(64)] for i in range(64)]
nc = [xor(row, eye) for row, eye in zip(expand(pic["objects"]["cc"]), identity)]
nt = [xor(row, eye) for row, eye in zip(expand(pic["objects"]["ct"]), identity)]
raw_cc = cc_cert["actual_cc_defect"]["full_surface_Pic64_historical_Magma_mod2_coordinates"]
raw_ct = ct_cert["ct_sum_fullPic64_historical_Magma_coordinates_mod2"]
assert rowmul(raw_cc, nc) == [0] * 64
assert rowmul(raw_ct, nt) == [0] * 64
assert rowmul(raw_cc, nt) == rowmul(raw_ct, nc)

stored = cert["retained_H1_projection"]
coordinates = stored["coordinates_f2"]
cob_coefficients = stored["one_coboundary_coefficient_witness_f2"]
h1 = target["finite_v4_pic2_cohomology"]["H1_quotient_basis_cc_ct_pairs_original_pic2_coordinates_f2"]
reconstructed = [0] * 128
for coefficient, cc_row, ct_row in zip(cob_coefficients, nc, nt):
    if coefficient:
        reconstructed = xor(reconstructed, cc_row + ct_row)
for coefficient, representative in zip(coordinates, h1):
    if coefficient:
        reconstructed = xor(reconstructed, representative["cc"] + representative["ct"])
assert reconstructed == raw_cc + raw_ct
assert len(coordinates) == 75 and sum(coordinates) == 15
assert stored["nonzero"] is True
boundary = cert["exact_information_boundary"]
assert boundary["named_J2_V4_H1_target_image_materialized"] is True
assert boundary["named_J2_retained_10D_source_coordinate_materialized"] is False
assert boundary["named_J2_target_placed_as_75x10_matrix_column"] is False
assert boundary["finite_v4_kummer_columns_materialized"] == 0
assert not any(cert["prohibited_promotions"].values())

print(json.dumps({
    "success": True,
    "certificate_sha256": EXPECTED,
    "named_J2_H1_target_weight": sum(coordinates),
    "named_J2_H1_target_nonzero": True,
    "matrix_columns_materialized": 0,
}, sort_keys=True))
