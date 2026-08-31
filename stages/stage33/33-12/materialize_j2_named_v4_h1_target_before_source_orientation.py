#!/usr/bin/env python3
"""Project the corrected named-J2 defect to the retained 75D V4 H1 basis.

This fixes the target image of named J2 but does not guess which retained
10D proper-Brauer source basis vector represents J2.  Hence it is not yet a
column of the 75x10 matrix.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
S33 = HERE.parent
PIC = S33 / "33-07" / "retained-picard-base-sparse.json"
TARGET = HERE / "full-surface-pic2-kummer-target.json"
CT = HERE / "j2-ct-six-kc-support-fullpic64-pullbacks.json"
CC = HERE / "j2-cc-actual-cech-global-square-overlap.json"
OUT = HERE / "j2-named-v4-h1-target-before-source-orientation.json"

LOCKS = {
    PIC: "e41df3f84760b941440035a388baac88602126c80140139ddf9c187bedf0bb49",
    TARGET: "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890",
    CT: "592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d",
    CC: "82ac2b6fe8d023c915e9cf3bb8ff38d4782dbec47f98e2593f964ea020ccc6fd",
}


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def locked(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == LOCKS[path] == csha(body)
    return obj


def expand_sparse(obj, n=64):
    answer = []
    for row in obj["matrix_64x64_sparse_rows_1based"]:
        dense = [0] * n
        for column, value in row:
            assert 1 <= column <= n and dense[column - 1] == 0
            dense[column - 1] = value & 1
        answer.append(dense)
    assert len(answer) == n
    return answer


def xor(left, right):
    return [a ^ b for a, b in zip(left, right)]


def rowmul(vector, matrix):
    return [sum(vector[i] * matrix[i][j] for i in range(len(vector))) & 1
            for j in range(len(matrix[0]))]


def bits(vector):
    return sum((value & 1) << i for i, value in enumerate(vector))


def insert(echelon, vector, label):
    while vector:
        pivot = vector.bit_length() - 1
        if pivot in echelon:
            vector ^= echelon[pivot][0]
            label ^= echelon[pivot][1]
        else:
            echelon[pivot] = (vector, label)
            return True
    return False


pic = locked(PIC)
target = locked(TARGET)
ct_cert = locked(CT)
cc_cert = locked(CC)
n = 64
identity = [[int(i == j) for j in range(n)] for i in range(n)]
cc_action = expand_sparse(pic["objects"]["cc"])
ct_action = expand_sparse(pic["objects"]["ct"])
nc = [xor(row, eye) for row, eye in zip(cc_action, identity)]
nt = [xor(row, eye) for row, eye in zip(ct_action, identity)]

# The retained Picard action uses the historical Magma Pic64 basis.
raw_cc = cc_cert["actual_cc_defect"][
    "full_surface_Pic64_historical_Magma_mod2_coordinates"
]
raw_ct = ct_cert["ct_sum_fullPic64_historical_Magma_coordinates_mod2"]
assert raw_cc == [0] * n
assert len(raw_ct) == n and sum(raw_ct) == 8

# Row-vector normalized V4 cocycle equations.
assert rowmul(raw_cc, nc) == [0] * n
assert rowmul(raw_ct, nt) == [0] * n
assert rowmul(raw_cc, nt) == rowmul(raw_ct, nc)

coboundaries = [nc[i] + nt[i] for i in range(n)]
h1_pairs = target["finite_v4_pic2_cohomology"][
    "H1_quotient_basis_cc_ct_pairs_original_pic2_coordinates_f2"
]
h1_representatives = [row["cc"] + row["ct"] for row in h1_pairs]
assert len(h1_representatives) == 75

# Express the raw cocycle in the ordered independent basis
# (64 displayed coboundary generators, then the 75 retained H1 generators).
# Dependent coboundary generators are harmless: insertion records the first
# independent presentation and quotient coordinates remain unique.
echelon = {}
for i, vector in enumerate(coboundaries):
    insert(echelon, bits(vector), 1 << i)
for j, vector in enumerate(h1_representatives):
    assert insert(echelon, bits(vector), 1 << (n + j))

remainder = bits(raw_cc + raw_ct)
label = 0
while remainder:
    pivot = remainder.bit_length() - 1
    assert pivot in echelon
    remainder ^= echelon[pivot][0]
    label ^= echelon[pivot][1]
assert remainder == 0

coboundary_coefficients = [(label >> i) & 1 for i in range(n)]
h1_coordinates = [(label >> (n + j)) & 1 for j in range(75)]
assert sum(h1_coordinates) == 15
reconstructed = [0] * (2 * n)
for coefficient, vector in zip(coboundary_coefficients, coboundaries):
    if coefficient:
        reconstructed = xor(reconstructed, vector)
for coefficient, vector in zip(h1_coordinates, h1_representatives):
    if coefficient:
        reconstructed = xor(reconstructed, vector)
assert reconstructed == raw_cc + raw_ct

out = {
    "schema": "STAGE33_12_J2_NAMED_V4_H1_TARGET_BEFORE_SOURCE_ORIENTATION_V1",
    "stage": "33-12",
    "status": "PASS_EXACT_NAMED_J2_TARGET_IMAGE_NONZERO_SOURCE_PLACEMENT_OPEN",
    "source_locks": {
        "retained_picard_base_sparse_canonical_sha256": LOCKS[PIC],
        "full_surface_pic2_kummer_target_canonical_sha256": LOCKS[TARGET],
        "j2_ct_six_fullPic64_pullbacks_canonical_sha256": LOCKS[CT],
        "j2_cc_actual_cech_overlap_canonical_sha256": LOCKS[CC],
    },
    "raw_named_J2_cocycle_historical_Magma_Pic64_mod2": {
        "cc": raw_cc,
        "ct": raw_ct,
        "ct_weight": sum(raw_ct),
        "cc_involution_equation": True,
        "ct_involution_equation": True,
        "cc_ct_commutation_equation": True,
    },
    "retained_H1_projection": {
        "group": "V4=<cc,ct>",
        "module": "Pic(Sbar)/2",
        "retained_H1_dimension_f2": 75,
        "coordinates_f2": h1_coordinates,
        "coordinate_weight": sum(h1_coordinates),
        "nonzero": any(h1_coordinates),
        "reconstruction_with_retained_H1_basis_and_coboundaries_exact": True,
        "one_coboundary_coefficient_witness_f2": coboundary_coefficients,
    },
    "exact_information_boundary": {
        "named_J2_V4_H1_target_image_materialized": True,
        "named_J2_V4_H1_target_image_nonzero": True,
        "named_J2_retained_10D_source_coordinate_materialized": False,
        "named_J2_target_placed_as_75x10_matrix_column": False,
        "finite_v4_kummer_columns_materialized": 0,
        "first_exact_75D_kummer_column_materialized": False,
    },
    "remaining_interface": "NAMED_CV_d2_TO_SEMANTIC_DISCRIMINANT_ORIENTATION_AND_RETAINED_10D_SOURCE_PLACEMENT",
    "next_exact_leaf": "MATCH_CV_d2_TO_SEMANTIC_u1_u2_OR_u1_PLUS_u2_THEN_PLACE_THE_LOCKED_NAMED_J2_TARGET_AS_THE_FIRST_75x10_COLUMN",
    "prohibited_promotions": {
        "d2_single_quotient_coordinate_used_as_full_surface_orientation": False,
        "historical_J2_zero_column_reused": False,
        "fake_source_basis_column_created": False,
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "named_J2_H1_target_weight": sum(h1_coordinates),
    "named_J2_H1_target_nonzero": any(h1_coordinates),
    "matrix_columns_materialized": 0,
    "certificate_sha256": out["canonical_sha256"],
}, sort_keys=True))
