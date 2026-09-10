#!/usr/bin/env python3
"""Exact F2 ambiguity audit for the Stage33 finite-V4 75x10 Kummer matrix.

Scratch/noncredit lane-e tool.  It deliberately excludes the revoked named-J2
target relation.  The only constraints are the locked Pic/2 and proper-Br2 V4
actions, the retained 10 invariant proper-Br2 sources, and the locked 75D H1
quotient projection.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parents[3]
S3312 = S33 / "33-12"
sys.path.insert(0, str(S3312))
from v4_pic2_raw_cocycle_projection import expand_sparse, locked, projection_basis  # noqa: E402

PIC = S33 / "33-07" / "retained-picard-base-sparse.json"
PROPER = S33 / "33-07" / "proper-brauer2-from-discriminant.json"
TARGET = S3312 / "full-surface-pic2-kummer-target.json"

PIC_SHA = "e41df3f84760b941440035a388baac88602126c80140139ddf9c187bedf0bb49"
PROPER_SHA = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
TARGET_SHA = "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890"

NP = 64
NB = 14
H1 = 75
NSRC = 10
PHI_SIZE = NB * NP
PHI_C_OFF = 0
PHI_T_OFF = PHI_SIZE
NVARS = 2 * PHI_SIZE
MASK64 = (1 << NP) - 1
MASK75 = (1 << H1) - 1


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


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


def homogeneous_echelon(equations: list[int]) -> dict[int, int]:
    pivots: dict[int, int] = {}
    for coeff in equations:
        insert_rank(pivots, coeff)
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
    return (label >> NP) & MASK75


def decode_coordinate(bit: int) -> dict[str, int]:
    return {
        "global_zero_based": bit,
        "source_zero_based": bit // H1,
        "source_one_based": bit // H1 + 1,
        "h1_zero_based": bit % H1,
        "h1_one_based": bit % H1 + 1,
    }


pic = locked(PIC, PIC_SHA)
proper = locked(PROPER, PROPER_SHA)
target = locked(TARGET, TARGET_SHA)
Pc = expand_sparse(pic["objects"]["cc"])
Pt = expand_sparse(pic["objects"]["ct"])
Bc = proper["proper_Br2_cc_action_f2"]
Bt = proper["proper_Br2_ct_action_f2"]
I64 = identity(NP)
I14 = identity(NB)
assert matmul(Pc, Pc) == I64 and matmul(Pt, Pt) == I64 and matmul(Pc, Pt) == matmul(Pt, Pc)
assert matmul(Bc, Bc) == I14 and matmul(Bt, Bt) == I14 and matmul(Bc, Bt) == matmul(Bt, Bc)
retained = target["proper_invariant_domain"]["basis_rows_original_proper_br2_coordinates_f2"]
assert len(retained) == NSRC
for source in retained:
    assert len(source) == NB
    assert rowmul(source, Bc) == source and rowmul(source, Bt) == source

# Homogeneous V4-module extension constraints for Phi_cc and Phi_ct.
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

pivots = homogeneous_echelon(equations)
free = [i for i in range(NVARS) if i not in pivots]
reducer = make_h1_reducer()

# Image D <= F2^(75*10) of the complete compatible extension solution space.
matrix_image_basis: dict[int, int] = {}
column_bases: list[dict[int, int]] = [dict() for _ in range(NSRC)]
for free_var in free:
    solution = null_vector_from_free(pivots, free_var)
    assert all(((eq & solution).bit_count() & 1) == 0 for eq in equations)
    images = [project_pair(source_raw_pair_int(solution, source), reducer) for source in retained]
    combined = 0
    for j, image in enumerate(images):
        combined |= image << (H1 * j)
        insert_rank(column_bases[j], image)
    insert_rank(matrix_image_basis, combined)

ambiguity_dim = len(matrix_image_basis)
column_dims = [len(b) for b in column_bases]
forced_columns = [j + 1 for j, d in enumerate(column_dims) if d == 0]
variable_support = 0
for vector in matrix_image_basis.values():
    variable_support |= vector
forced_bits = [bit for bit in range(H1 * NSRC) if ((variable_support >> bit) & 1) == 0]
measurement_pivots = sorted(matrix_image_basis.keys(), reverse=True)
assert len(measurement_pivots) == ambiguity_dim

result = {
    "success": True,
    "schema": "STAGE33_KUMMER_E_75X10_ABSTRACT_V4_AMBIGUITY_V1",
    "scope": "ALL_F2_V4_MODULE_EXTENSIONS_COMPATIBLE_WITH_LOCKED_PIC_AND_PROPER_BR2_ACTIONS",
    "source_locks": {
        "parent_exact_head": "fa7949deee5e134eddc45aff7bc1d6e608e1f286",
        "retained_picard_base_sparse_canonical_sha256": PIC_SHA,
        "proper_brauer2_from_discriminant_canonical_sha256": PROPER_SHA,
        "full_surface_pic2_kummer_target_canonical_sha256": TARGET_SHA,
    },
    "revoked_relation_firewall": {
        "named_j2_target_used": False,
        "named_j2_source_target_relation_used": False,
    },
    "extension_solution_space": {
        "variables_phi_cc_phi_ct": NVARS,
        "equations": len(equations),
        "rank_f2": len(pivots),
        "nullity_f2": len(free),
        "zero_extension_present": True,
    },
    "matrix": {
        "rows_h1": H1,
        "columns_retained_sources": NSRC,
        "scalar_entries": H1 * NSRC,
        "residual_ambiguity_dimension_f2": ambiguity_dim,
        "residual_candidate_count": 1 << ambiguity_dim,
        "column_ambiguity_dimensions_f2": column_dims,
        "forced_columns_one_based": forced_columns,
        "forced_entry_count": len(forced_bits),
        "forced_entries_all_zero": True,
        "forced_entries": [decode_coordinate(bit) for bit in forced_bits],
    },
    "minimal_coordinate_measurement_plan": {
        "minimum_scalar_entry_measurements": ambiguity_dim,
        "reason": "pivot-coordinate projection is injective on the ambiguity subspace; fewer than dim(D) F2 scalar measurements cannot distinguish all 2^dim(D) states",
        "entries": [decode_coordinate(bit) for bit in measurement_pivots],
    },
    "firewall": {
        "abstract_module_extension_only": True,
        "actual_geometric_extension_identified": False,
        "geometric_existence_credit": False,
        "Q_defined_descent_credit_added": False,
        "authority_or_stage_progress_promoted": False,
    },
}
body = dict(result)
result["canonical_sha256"] = csha(body)
print(json.dumps(result, sort_keys=True))
