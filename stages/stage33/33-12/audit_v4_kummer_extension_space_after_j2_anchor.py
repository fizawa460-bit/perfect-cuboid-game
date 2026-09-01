#!/usr/bin/env python3
"""Audit the named-J2 Kummer relation against all compatible V4 module extensions.

Over F2, every V4-module extension

    0 -> Pic(Sbar)/2 -> E -> Br(Sbar)[2] -> 0

can, after choosing a linear section, be written with row-action blocks

    E_g = [[P_g, 0], [Phi_g, B_g]].

The involution and commutation laws give a homogeneous linear system for the
14x64 matrices Phi_cc and Phi_ct.  For an invariant Brauer source s, its
connecting cocycle is (s Phi_cc, s Phi_ct), modulo Picard coboundaries.

This script enumerates the full solution space of those module-extension
constraints, projects every resulting invariant-source defect through the
locked 75D H1 quotient, and asks whether the independently locked named-J2
75D target is reachable from the independently locked J2 proper-Br2 source.

If it is not reachable, then the current source and target certificates cannot
simultaneously be the Kummer connecting pair under the locked V4 actions; this
is a coordinate/semantic compatibility blocker, not permission to guess a new
column or promote historical glue.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from v4_pic2_raw_cocycle_projection import expand_sparse, locked, projection_basis

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
PIC = S33 / "33-07" / "retained-picard-base-sparse.json"
PROPER = S33 / "33-07" / "proper-brauer2-from-discriminant.json"
TARGET = HERE / "full-surface-pic2-kummer-target.json"
ADJOINT = HERE / "j2-picard-adjoint-proper-br2.json"
J2_TARGET = HERE / "j2-named-v4-h1-target-before-source-orientation.json"
J2_CT = HERE / "j2-ct-six-kc-support-fullpic64-pullbacks.json"
J2_CC = HERE / "j2-cc-actual-cech-global-square-overlap.json"

PIC_SHA = "e41df3f84760b941440035a388baac88602126c80140139ddf9c187bedf0bb49"
PROPER_SHA = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
TARGET_SHA = "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890"
ADJOINT_SHA = "066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8"
J2_TARGET_SHA = "4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3"
J2_CT_SHA = "592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d"
J2_CC_SHA = "82ac2b6fe8d023c915e9cf3bb8ff38d4782dbec47f98e2593f964ea020ccc6fd"

NP = 64
NB = 14
H1 = 75
PHI_SIZE = NB * NP
PHI_C_OFF = 0
PHI_T_OFF = PHI_SIZE
NVARS = 2 * PHI_SIZE
MASK64 = (1 << NP) - 1


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


def support_1based(mask: int, n: int = 10) -> list[int]:
    return [i + 1 for i in range(n) if (mask >> i) & 1]


pic = locked(PIC, PIC_SHA)
proper = locked(PROPER, PROPER_SHA)
target = locked(TARGET, TARGET_SHA)
adjoint = locked(ADJOINT, ADJOINT_SHA)
j2_target = locked(J2_TARGET, J2_TARGET_SHA)
j2_ct = locked(J2_CT, J2_CT_SHA)
j2_cc = locked(J2_CC, J2_CC_SHA)

Pc = expand_sparse(pic["objects"]["cc"])
Pt = expand_sparse(pic["objects"]["ct"])
Bc = proper["proper_Br2_cc_action_f2"]
Bt = proper["proper_Br2_ct_action_f2"]
I64 = identity(NP)
I14 = identity(NB)
assert matmul(Pc, Pc) == I64 and matmul(Pt, Pt) == I64 and matmul(Pc, Pt) == matmul(Pt, Pc)
assert matmul(Bc, Bc) == I14 and matmul(Bt, Bt) == I14 and matmul(Bc, Bt) == matmul(Bt, Bc)

retained = target["proper_invariant_domain"]["basis_rows_original_proper_br2_coordinates_f2"]
assert len(retained) == 10
for source in retained:
    assert rowmul(source, Bc) == source and rowmul(source, Bt) == source

j2 = adjoint["proper_brauer2_pullback"]["proper_Br2_14D_coordinate_f2"]
assert rowmul(j2, Bc) == j2 and rowmul(j2, Bt) == j2
assert xor(retained[1], retained[2]) == j2
j2_retained_mask = (1 << 1) | (1 << 2)

raw_j2_cc = j2_cc["actual_cc_defect"]["full_surface_Pic64_historical_Magma_mod2_coordinates"]
raw_j2_ct = j2_ct["ct_sum_fullPic64_historical_Magma_coordinates_mod2"]
j2_h1_list = j2_target["retained_H1_projection"]["coordinates_f2"]
j2_h1 = sum((bit & 1) << i for i, bit in enumerate(j2_h1_list))
reducer = make_h1_reducer()
raw_j2_pair = sum((bit & 1) << i for i, bit in enumerate(raw_j2_cc))
raw_j2_pair |= sum((bit & 1) << (NP + i) for i, bit in enumerate(raw_j2_ct))
assert project_pair(raw_j2_pair, reducer) == j2_h1

# All homogeneous block-extension constraints.
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

# For each basis direction in the complete extension solution space, record the
# H1 image of each retained standard source.
null_standard_images: list[list[int]] = []
for free_var in free:
    solution = null_vector_from_free(pivots, free_var)
    for eq in equations:
        assert ((eq & solution).bit_count() & 1) == 0
    images = [project_pair(source_raw_pair_int(solution, source), reducer) for source in retained]
    null_standard_images.append(images)

# Exact reachable H1 subspace for the independently fixed J2 proper-Br2 source.
j2_reachable: dict[int, int] = {}
for images in null_standard_images:
    insert_rank(j2_reachable, images[1] ^ images[2])
j2_target_reachable = in_span(j2_reachable, j2_h1)

# Diagnose whether a different retained source could, at the level of abstract
# module extensions, carry the locked target.  This does NOT rename J2; it only
# narrows whether the incompatibility is source-specific or target-global.
compatible_masks: list[int] = []
for mask in range(1, 1 << 10):
    span: dict[int, int] = {}
    for images in null_standard_images:
        out = 0
        for i in range(10):
            if (mask >> i) & 1:
                out ^= images[i]
        insert_rank(span, out)
    if in_span(span, j2_h1):
        compatible_masks.append(mask)

result = {
    "success": True,
    "schema": "STAGE33_12_V4_KUMMER_EXTENSION_REACHABILITY_AUDIT_V2",
    "scope": "ALL_F2_V4_MODULE_EXTENSIONS_COMPATIBLE_WITH_LOCKED_PIC_AND_PROPER_BR2_ACTIONS",
    "source_locks": {
        "retained_picard_base_sparse_canonical_sha256": PIC_SHA,
        "proper_brauer2_from_discriminant_canonical_sha256": PROPER_SHA,
        "full_surface_pic2_kummer_target_canonical_sha256": TARGET_SHA,
        "j2_picard_adjoint_canonical_sha256": ADJOINT_SHA,
        "j2_named_75D_target_canonical_sha256": J2_TARGET_SHA,
        "j2_ct_raw_cocycle_canonical_sha256": J2_CT_SHA,
        "j2_cc_raw_cocycle_canonical_sha256": J2_CC_SHA,
    },
    "extension_solution_space": {
        "variables_phi_cc_phi_ct": NVARS,
        "equations": len(equations),
        "rank_f2": len(pivots),
        "nullity_f2": len(free),
        "zero_extension_present": True,
    },
    "locked_named_j2": {
        "proper14_f2": j2,
        "retained10_support_1based": [2, 3],
        "target_75D_weight": sum(j2_h1_list),
        "reachable_H1_subspace_dimension_f2": len(j2_reachable),
        "locked_target_reachable_from_locked_source": j2_target_reachable,
    },
    "target_reachability_over_all_nonzero_retained_sources": {
        "compatible_source_count": len(compatible_masks),
        "locked_j2_source_mask_decimal": j2_retained_mask,
        "locked_j2_source_is_compatible": j2_retained_mask in compatible_masks,
        "compatible_source_masks_decimal": compatible_masks,
        "compatible_source_supports_1based": [support_1based(mask) for mask in compatible_masks],
    },
    "interpretation": (
        "LOCKED_J2_SOURCE_TARGET_RELATION_IS_COMPATIBLE_WITH_SOME_V4_MODULE_EXTENSION"
        if j2_target_reachable
        else "LOCKED_J2_SOURCE_TARGET_RELATION_IS_NOT_REALIZABLE_BY_ANY_V4_MODULE_EXTENSION_WITH_THE_LOCKED_ACTIONS"
    ),
    "firewall": {
        "actual_geometric_extension_identified": False,
        "historical_rep88_promoted": False,
        "standard_kummer_columns_materialized": 0,
        "Q_defined_descent_credit_added": False,
        "if_incompatible": "do not use C2+C3=h_J2 as a Kummer-matrix relation until the source/target/action convention mismatch is repaired",
    },
}
result["canonical_sha256"] = csha(result)
print(json.dumps(result, sort_keys=True))
