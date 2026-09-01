#!/usr/bin/env python3
"""Project an exact raw V4 Pic/2 cocycle to the locked 75D H1 basis.

This is a reusable linear-algebra adapter only.  It does not construct a
mu_2 lift, prove Q-descent, or choose a proper-Brauer source class.  Callers
must provide exact historical-Magma Pic64 mod-2 cocycle components
``raw_cc`` and ``raw_ct``.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
S33 = HERE.parent
PIC = S33 / "33-07" / "retained-picard-base-sparse.json"
TARGET = HERE / "full-surface-pic2-kummer-target.json"
PIC_SHA = "e41df3f84760b941440035a388baac88602126c80140139ddf9c187bedf0bb49"
TARGET_SHA = "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890"
N = 64
H1_DIM = 75


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if claimed != expected or csha(body) != expected:
        raise ValueError(f"canonical lock moved: {path}")
    return obj


def expand_sparse(obj: dict, n: int = N) -> list[list[int]]:
    answer = []
    for row in obj["matrix_64x64_sparse_rows_1based"]:
        dense = [0] * n
        for column, value in row:
            if not 1 <= column <= n or dense[column - 1] != 0:
                raise ValueError("invalid sparse Picard action row")
            dense[column - 1] = int(value) & 1
        answer.append(dense)
    if len(answer) != n:
        raise ValueError("Picard action shape moved")
    return answer


def xor(left: list[int], right: list[int]) -> list[int]:
    if len(left) != len(right):
        raise ValueError("xor length mismatch")
    return [a ^ b for a, b in zip(left, right)]


def rowmul(vector: list[int], matrix: list[list[int]]) -> list[int]:
    return [
        sum(vector[i] * matrix[i][j] for i in range(len(vector))) & 1
        for j in range(len(matrix[0]))
    ]


def bits(vector: list[int]) -> int:
    return sum((value & 1) << i for i, value in enumerate(vector))


def insert(echelon: dict[int, tuple[int, int]], vector: int, label: int) -> bool:
    while vector:
        pivot = vector.bit_length() - 1
        if pivot in echelon:
            vector ^= echelon[pivot][0]
            label ^= echelon[pivot][1]
        else:
            echelon[pivot] = (vector, label)
            return True
    return False


def projection_basis() -> tuple[list[list[int]], list[list[int]], list[list[int]]]:
    pic = locked(PIC, PIC_SHA)
    target = locked(TARGET, TARGET_SHA)
    identity = [[int(i == j) for j in range(N)] for i in range(N)]
    cc_action = expand_sparse(pic["objects"]["cc"])
    ct_action = expand_sparse(pic["objects"]["ct"])
    nc = [xor(row, eye) for row, eye in zip(cc_action, identity)]
    nt = [xor(row, eye) for row, eye in zip(ct_action, identity)]
    h1_pairs = target["finite_v4_pic2_cohomology"][
        "H1_quotient_basis_cc_ct_pairs_original_pic2_coordinates_f2"
    ]
    h1_representatives = [row["cc"] + row["ct"] for row in h1_pairs]
    if len(h1_representatives) != H1_DIM:
        raise ValueError("retained H1 dimension moved")
    return nc, nt, h1_representatives


def project_raw_cocycle(raw_cc: list[int], raw_ct: list[int]) -> dict:
    raw_cc = [int(x) for x in raw_cc]
    raw_ct = [int(x) for x in raw_ct]
    if len(raw_cc) != N or len(raw_ct) != N:
        raise ValueError("raw cocycle components must each have length 64")
    if any(x not in (0, 1) for x in raw_cc + raw_ct):
        raise ValueError("raw cocycle must be F2-valued")

    nc, nt, h1_representatives = projection_basis()
    zero = [0] * N
    if rowmul(raw_cc, nc) != zero:
        raise ValueError("cc involution cocycle equation failed")
    if rowmul(raw_ct, nt) != zero:
        raise ValueError("ct involution cocycle equation failed")
    if rowmul(raw_cc, nt) != rowmul(raw_ct, nc):
        raise ValueError("cc/ct commutation cocycle equation failed")

    coboundaries = [nc[i] + nt[i] for i in range(N)]
    echelon: dict[int, tuple[int, int]] = {}
    for i, vector in enumerate(coboundaries):
        insert(echelon, bits(vector), 1 << i)
    for j, vector in enumerate(h1_representatives):
        if not insert(echelon, bits(vector), 1 << (N + j)):
            raise ValueError("retained H1 quotient basis lost independence")

    remainder = bits(raw_cc + raw_ct)
    label = 0
    while remainder:
        pivot = remainder.bit_length() - 1
        if pivot not in echelon:
            raise ValueError("raw cocycle outside certified cocycle span")
        remainder ^= echelon[pivot][0]
        label ^= echelon[pivot][1]

    coboundary_coefficients = [(label >> i) & 1 for i in range(N)]
    h1_coordinates = [(label >> (N + j)) & 1 for j in range(H1_DIM)]

    reconstructed = [0] * (2 * N)
    for coefficient, vector in zip(coboundary_coefficients, coboundaries):
        if coefficient:
            reconstructed = xor(reconstructed, vector)
    for coefficient, vector in zip(h1_coordinates, h1_representatives):
        if coefficient:
            reconstructed = xor(reconstructed, vector)
    if reconstructed != raw_cc + raw_ct:
        raise ValueError("projection reconstruction failed")

    return {
        "coordinates_f2": h1_coordinates,
        "coordinate_weight": sum(h1_coordinates),
        "nonzero": any(h1_coordinates),
        "one_coboundary_coefficient_witness_f2": coboundary_coefficients,
        "reconstruction_exact": True,
        "source_locks": {
            "retained_picard_base_sparse_canonical_sha256": PIC_SHA,
            "full_surface_pic2_kummer_target_canonical_sha256": TARGET_SHA,
        },
    }
