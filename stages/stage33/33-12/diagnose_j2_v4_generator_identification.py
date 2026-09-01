#!/usr/bin/env python3
"""Diagnose whether the J2 binding failure is only a relative V4-generator labelling mismatch.

Keep the locked Pic(Sbar)/2 action and the locked raw/75D J2 target fixed.  On the
proper-Br2 side, test all six automorphisms of V4 by identifying the Pic-side
ordered generators (cc,ct) with each ordered pair of distinct nonidentity
proper-Br2 elements.  For each identification, enumerate the complete compatible
F2[V4]-module extension space and ask whether the locked J2 proper-Br2 source can
reach the locked 75D target.

This is a diagnostic only.  A positive row would narrow the missing adapter; it
would not identify the geometric Kummer extension or promote a matrix column.
"""
from __future__ import annotations

import json
from pathlib import Path

from v4_pic2_raw_cocycle_projection import expand_sparse, locked, projection_basis

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
PIC = S33 / "33-07" / "retained-picard-base-sparse.json"
PROPER = S33 / "33-07" / "proper-brauer2-from-discriminant.json"
ADJOINT = HERE / "j2-picard-adjoint-proper-br2.json"
J2_TARGET = HERE / "j2-named-v4-h1-target-before-source-orientation.json"

PIC_SHA = "e41df3f84760b941440035a388baac88602126c80140139ddf9c187bedf0bb49"
PROPER_SHA = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
ADJOINT_SHA = "066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8"
J2_TARGET_SHA = "4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3"

NP = 64
NB = 14
H1 = 75
PHI_SIZE = NB * NP
PHI_C_OFF = 0
PHI_T_OFF = PHI_SIZE
NVARS = 2 * PHI_SIZE
MASK64 = (1 << NP) - 1


def xor(a: list[int], b: list[int]) -> list[int]:
    return [x ^ y for x, y in zip(a, b)]


def rowmul(v: list[int], m: list[list[int]]) -> list[int]:
    return [sum(v[i] * m[i][j] for i in range(len(v))) & 1 for j in range(len(m[0]))]


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [rowmul(row, b) for row in a]


def identity(n: int) -> list[list[int]]:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def vindex(off: int, brow: int, pcol: int) -> int:
    return off + brow * NP + pcol


def insert_rank(echelon: dict[int, int], vector: int) -> bool:
    while vector:
        pivot = vector.bit_length() - 1
        if pivot in echelon:
            vector ^= echelon[pivot]
        else:
            echelon[pivot] = vector
            return True
    return False


def in_span(echelon: dict[int, int], vector: int) -> bool:
    while vector:
        pivot = vector.bit_length() - 1
        if pivot not in echelon:
            return False
        vector ^= echelon[pivot]
    return True


def insert_labelled(echelon: dict[int, tuple[int, int]], vector: int, label: int) -> bool:
    while vector:
        pivot = vector.bit_length() - 1
        if pivot in echelon:
            vector ^= echelon[pivot][0]
            label ^= echelon[pivot][1]
        else:
            echelon[pivot] = (vector, label)
            return True
    return False


def homogeneous_echelon(equations: list[int]) -> dict[int, int]:
    pivots: dict[int, int] = {}
    for coeff in equations:
        while coeff:
            pivot = coeff.bit_length() - 1
            if pivot in pivots:
                coeff ^= pivots[pivot]
            else:
                pivots[pivot] = coeff
                break
    return pivots


def null_vector_from_free(pivots: dict[int, int], free_var: int) -> int:
    x = 1 << free_var
    for pivot in sorted(pivots):
        lower = pivots[pivot] & ((1 << pivot) - 1)
        if (lower & x).bit_count() & 1:
            x |= 1 << pivot
    return x


def phi_rows(solution: int, off: int) -> list[int]:
    return [(solution >> (off + a * NP)) & MASK64 for a in range(NB)]


def source_raw_pair_int(solution: int, source: list[int]) -> int:
    crows = phi_rows(solution, PHI_C_OFF)
    trows = phi_rows(solution, PHI_T_OFF)
    cc = 0
    ct = 0
    for a, bit in enumerate(source):
        if bit:
            cc ^= crows[a]
            ct ^= trows[a]
    return cc | (ct << NP)


def make_h1_reducer() -> dict[int, tuple[int, int]]:
    nc, nt, h1_reps = projection_basis()
    echelon: dict[int, tuple[int, int]] = {}
    for i in range(NP):
        pair = sum((nc[i][j] & 1) << j for j in range(NP))
        pair |= sum((nt[i][j] & 1) << (NP + j) for j in range(NP))
        insert_labelled(echelon, pair, 1 << i)
    for j, rep in enumerate(h1_reps):
        pair = sum((rep[k] & 1) << k for k in range(2 * NP))
        if not insert_labelled(echelon, pair, 1 << (NP + j)):
            raise ValueError("locked H1 quotient basis lost independence")
    return echelon


def project_pair(pair: int, reducer: dict[int, tuple[int, int]]) -> int:
    label = 0
    remainder = pair
    while remainder:
        pivot = remainder.bit_length() - 1
        if pivot not in reducer:
            raise ValueError("extension defect is outside locked cocycle span")
        vector, basis_label = reducer[pivot]
        remainder ^= vector
        label ^= basis_label
    return (label >> NP) & ((1 << H1) - 1)


def extension_equations(Pc: list[list[int]], Pt: list[list[int]], Bc: list[list[int]], Bt: list[list[int]]) -> list[int]:
    equations: list[int] = []
    for a in range(NB):
        for p in range(NP):
            bits = 0
            for q in range(NP):
                if Pc[q][p]:
                    bits ^= 1 << vindex(PHI_C_OFF, a, q)
            for b in range(NB):
                if Bc[a][b]:
                    bits ^= 1 << vindex(PHI_C_OFF, b, p)
            equations.append(bits)

            bits = 0
            for q in range(NP):
                if Pt[q][p]:
                    bits ^= 1 << vindex(PHI_T_OFF, a, q)
            for b in range(NB):
                if Bt[a][b]:
                    bits ^= 1 << vindex(PHI_T_OFF, b, p)
            equations.append(bits)

    for a in range(NB):
        for p in range(NP):
            bits = 0
            for q in range(NP):
                if Pt[q][p]:
                    bits ^= 1 << vindex(PHI_C_OFF, a, q)
                if Pc[q][p]:
                    bits ^= 1 << vindex(PHI_T_OFF, a, q)
            for b in range(NB):
                if Bc[a][b]:
                    bits ^= 1 << vindex(PHI_T_OFF, b, p)
                if Bt[a][b]:
                    bits ^= 1 << vindex(PHI_C_OFF, b, p)
            equations.append(bits)
    return equations


pic = locked(PIC, PIC_SHA)
proper = locked(PROPER, PROPER_SHA)
adjoint = locked(ADJOINT, ADJOINT_SHA)
j2_target = locked(J2_TARGET, J2_TARGET_SHA)

Pc = expand_sparse(pic["objects"]["cc"])
Pt = expand_sparse(pic["objects"]["ct"])
Bc0 = proper["proper_Br2_cc_action_f2"]
Bt0 = proper["proper_Br2_ct_action_f2"]
Bct0 = matmul(Bc0, Bt0)
I64 = identity(NP)
I14 = identity(NB)
assert matmul(Pc, Pc) == I64 and matmul(Pt, Pt) == I64 and matmul(Pc, Pt) == matmul(Pt, Pc)
for B in (Bc0, Bt0, Bct0):
    assert matmul(B, B) == I14
assert matmul(Bc0, Bt0) == matmul(Bt0, Bc0)

j2 = adjoint["proper_brauer2_pullback"]["proper_Br2_14D_coordinate_f2"]
j2_h1_list = j2_target["retained_H1_projection"]["coordinates_f2"]
j2_h1 = sum((bit & 1) << i for i, bit in enumerate(j2_h1_list))
reducer = make_h1_reducer()

actions = {"cc": Bc0, "ct": Bt0, "ccct": Bct0}
ordered_generator_pairs = [
    ("cc", "ct"),
    ("cc", "ccct"),
    ("ct", "cc"),
    ("ct", "ccct"),
    ("ccct", "cc"),
    ("ccct", "ct"),
]

rows = []
for br_for_pic_cc, br_for_pic_ct in ordered_generator_pairs:
    Bc = actions[br_for_pic_cc]
    Bt = actions[br_for_pic_ct]
    assert rowmul(j2, Bc) == j2 and rowmul(j2, Bt) == j2
    equations = extension_equations(Pc, Pt, Bc, Bt)
    pivots = homogeneous_echelon(equations)
    free = [i for i in range(NVARS) if i not in pivots]
    reachable: dict[int, int] = {}
    for free_var in free:
        solution = null_vector_from_free(pivots, free_var)
        image = project_pair(source_raw_pair_int(solution, j2), reducer)
        insert_rank(reachable, image)
    rows.append({
        "proper_action_seen_by_pic_cc": br_for_pic_cc,
        "proper_action_seen_by_pic_ct": br_for_pic_ct,
        "equations": len(equations),
        "extension_constraint_rank_f2": len(pivots),
        "extension_nullity_f2": len(free),
        "j2_reachable_H1_dimension_f2": len(reachable),
        "locked_target_reachable_from_j2": in_span(reachable, j2_h1),
    })

result = {
    "success": True,
    "schema": "STAGE33_12_J2_V4_GENERATOR_IDENTIFICATION_DIAGNOSTIC_V1",
    "scope": "ALL_SIX_AUTOMORPHISMS_OF_V4_AS_RELATIVE_IDENTIFICATIONS_BETWEEN_LOCKED_PIC_AND_PROPER_BR2_ACTION_LABELS",
    "source_locks": {
        "retained_picard_base_sparse_canonical_sha256": PIC_SHA,
        "proper_brauer2_from_discriminant_canonical_sha256": PROPER_SHA,
        "j2_picard_adjoint_canonical_sha256": ADJOINT_SHA,
        "j2_named_75D_target_canonical_sha256": J2_TARGET_SHA,
    },
    "locked_j2_proper14_f2": j2,
    "locked_target_75D_weight": sum(j2_h1_list),
    "rows": rows,
    "compatible_relative_identification_count": sum(row["locked_target_reachable_from_j2"] for row in rows),
    "firewall": {
        "diagnostic_only": True,
        "actual_geometric_extension_identified": False,
        "source_coordinate_changed": False,
        "target_coordinate_changed": False,
        "named_kummer_relation_restored": False,
        "standard_kummer_column_materialized": False,
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
    },
}
print(json.dumps(result, indent=2, sort_keys=True))
