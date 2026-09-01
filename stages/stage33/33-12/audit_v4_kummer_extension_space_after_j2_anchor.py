#!/usr/bin/env python3
"""Exact GF(2) audit of V4 Kummer extension ambiguity after the J2 anchor.

We range over every F2[V4]-module extension

    0 -> Pic(Sbar)/2 -> E -> Br(Sbar)[2] -> 0

compatible with the already-certified Picard and proper-Br2 actions.  In a
row-vector section the two actions on E have lower-left blocks Phi_cc and
Phi_ct (14 x 64).  The V4 relations give linear equations on those blocks.
We additionally impose the exact named-J2 boundary class, modulo Picard
coboundary (section change), and ask which retained 10D source images are
forced in H^1(V4,Pic/2).

This is deliberately an *all-module-extensions* audit.  If a column varies
inside this superset, the current module actions plus the J2 anchor alone do
not determine that geometric Kummer column.  No historical finite-glue
candidate is promoted to actual geometry here.
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
W_OFF = 2 * PHI_SIZE
NVARS = W_OFF + NP
MASK64 = (1 << NP) - 1


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


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


def add_bit(bits: int, index: int) -> int:
    return bits ^ (1 << index)


def insert_rank(echelon: dict[int, int], vector: int) -> bool:
    while vector:
        pivot = vector.bit_length() - 1
        if pivot in echelon:
            vector ^= echelon[pivot]
        else:
            echelon[pivot] = vector
            return True
    return False


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


def affine_echelon(equations: list[tuple[int, int]]) -> dict[int, tuple[int, int]]:
    """Highest-pivot echelon: pivot row contains only lower-index variables."""
    pivots: dict[int, tuple[int, int]] = {}
    for coeff, rhs in equations:
        rhs &= 1
        while coeff:
            pivot = coeff.bit_length() - 1
            if pivot in pivots:
                pc, pr = pivots[pivot]
                coeff ^= pc
                rhs ^= pr
            else:
                pivots[pivot] = (coeff, rhs)
                break
        else:
            if rhs:
                raise ValueError("inconsistent anchored V4 extension system")
    return pivots


def solve_from_free(pivots: dict[int, tuple[int, int]], free_seed: int, affine: bool) -> int:
    x = free_seed
    for pivot in sorted(pivots):
        coeff, rhs = pivots[pivot]
        lower = coeff & ((1 << pivot) - 1)
        value = ((lower & x).bit_count() & 1) ^ (rhs if affine else 0)
        if value:
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


def make_h1_reducer() -> tuple[dict[int, tuple[int, int]], list[list[int]], list[list[int]]]:
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
    return echelon, nc, nt


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


def bits_to_list(x: int, n: int) -> list[int]:
    return [(x >> i) & 1 for i in range(n)]


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
Nc = [xor(row, eye) for row, eye in zip(Pc, I64)]
Nt = [xor(row, eye) for row, eye in zip(Pt, I64)]

assert len(Bc) == len(Bt) == NB and all(len(row) == NB for row in Bc + Bt)
assert matmul(Pc, Pc) == I64 and matmul(Pt, Pt) == I64 and matmul(Pc, Pt) == matmul(Pt, Pc)
assert matmul(Bc, Bc) == I14 and matmul(Bt, Bt) == I14 and matmul(Bc, Bt) == matmul(Bt, Bc)

retained = target["proper_invariant_domain"]["basis_rows_original_proper_br2_coordinates_f2"]
assert len(retained) == 10
for source in retained:
    assert rowmul(source, Bc) == source
    assert rowmul(source, Bt) == source

j2 = adjoint["proper_brauer2_pullback"]["proper_Br2_14D_coordinate_f2"]
assert rowmul(j2, Bc) == j2 and rowmul(j2, Bt) == j2
assert xor(retained[1], retained[2]) == j2  # retained10 e2+e3

raw_j2_cc = j2_cc["actual_cc_defect"]["full_surface_Pic64_historical_Magma_mod2_coordinates"]
raw_j2_ct = j2_ct["ct_sum_fullPic64_historical_Magma_coordinates_mod2"]
assert len(raw_j2_cc) == len(raw_j2_ct) == NP
j2_h1_list = j2_target["retained_H1_projection"]["coordinates_f2"]
j2_h1 = sum((bit & 1) << i for i, bit in enumerate(j2_h1_list))

reducer, _, _ = make_h1_reducer()
raw_j2_pair = sum((bit & 1) << i for i, bit in enumerate(raw_j2_cc))
raw_j2_pair |= sum((bit & 1) << (NP + i) for i, bit in enumerate(raw_j2_ct))
assert project_pair(raw_j2_pair, reducer) == j2_h1

# Build all module-extension equations.
equations: list[tuple[int, int]] = []

# Phi_c Pc + Bc Phi_c = 0 and Phi_t Pt + Bt Phi_t = 0.
for a in range(NB):
    for p in range(NP):
        bits = 0
        for q in range(NP):
            if Pc[q][p]:
                bits = add_bit(bits, vindex(PHI_C_OFF, a, q))
        for b in range(NB):
            if Bc[a][b]:
                bits = add_bit(bits, vindex(PHI_C_OFF, b, p))
        equations.append((bits, 0))

        bits = 0
        for q in range(NP):
            if Pt[q][p]:
                bits = add_bit(bits, vindex(PHI_T_OFF, a, q))
        for b in range(NB):
            if Bt[a][b]:
                bits = add_bit(bits, vindex(PHI_T_OFF, b, p))
        equations.append((bits, 0))

# Phi_c Pt + Bc Phi_t = Phi_t Pc + Bt Phi_c.
for a in range(NB):
    for p in range(NP):
        bits = 0
        for q in range(NP):
            if Pt[q][p]:
                bits = add_bit(bits, vindex(PHI_C_OFF, a, q))
            if Pc[q][p]:
                bits = add_bit(bits, vindex(PHI_T_OFF, a, q))
        for b in range(NB):
            if Bc[a][b]:
                bits = add_bit(bits, vindex(PHI_T_OFF, b, p))
            if Bt[a][b]:
                bits = add_bit(bits, vindex(PHI_C_OFF, b, p))
        equations.append((bits, 0))

# Exact J2 anchor modulo a Picard coboundary from one section-change vector w.
for p in range(NP):
    bits = 0
    for a, bit in enumerate(j2):
        if bit:
            bits = add_bit(bits, vindex(PHI_C_OFF, a, p))
    for q in range(NP):
        if Nc[q][p]:
            bits = add_bit(bits, W_OFF + q)
    equations.append((bits, raw_j2_cc[p]))

    bits = 0
    for a, bit in enumerate(j2):
        if bit:
            bits = add_bit(bits, vindex(PHI_T_OFF, a, p))
    for q in range(NP):
        if Nt[q][p]:
            bits = add_bit(bits, W_OFF + q)
    equations.append((bits, raw_j2_ct[p]))

pivots = affine_echelon(equations)
rank = len(pivots)
free = [i for i in range(NVARS) if i not in pivots]
particular = solve_from_free(pivots, 0, affine=True)

# Verify the particular solution satisfies every equation exactly.
for coeff, rhs in equations:
    assert ((coeff & particular).bit_count() & 1) == rhs

particular_images = [project_pair(source_raw_pair_int(particular, s), reducer) for s in retained]
assert particular_images[1] ^ particular_images[2] == j2_h1

ambiguity_spaces: list[dict[int, int]] = [dict() for _ in retained]
nonzero_null_images = 0
for free_var in free:
    null_solution = solve_from_free(pivots, 1 << free_var, affine=False)
    # The anchored J2 boundary must be zero in every homogeneous direction.
    j2_delta = project_pair(source_raw_pair_int(null_solution, j2), reducer)
    assert j2_delta == 0
    any_nonzero = False
    for i, source in enumerate(retained):
        delta = project_pair(source_raw_pair_int(null_solution, source), reducer)
        if delta:
            any_nonzero = True
            insert_rank(ambiguity_spaces[i], delta)
    if any_nonzero:
        nonzero_null_images += 1

ambiguity_ranks = [len(space) for space in ambiguity_spaces]
forced = [rank_i == 0 for rank_i in ambiguity_ranks]
forced_coordinates = [bits_to_list(particular_images[i], H1) if forced[i] else None for i in range(10)]

result = {
    "success": True,
    "schema": "STAGE33_12_V4_KUMMER_EXTENSION_SPACE_AFTER_J2_ANCHOR_AUDIT_V1",
    "scope": "ALL_F2_V4_MODULE_EXTENSIONS_COMPATIBLE_WITH_LOCKED_PIC_AND_PROPER_BR2_ACTIONS_PLUS_EXACT_J2_BOUNDARY_ANCHOR",
    "source_locks": {
        "retained_picard_base_sparse_canonical_sha256": PIC_SHA,
        "proper_brauer2_from_discriminant_canonical_sha256": PROPER_SHA,
        "full_surface_pic2_kummer_target_canonical_sha256": TARGET_SHA,
        "j2_picard_adjoint_canonical_sha256": ADJOINT_SHA,
        "j2_named_75D_target_canonical_sha256": J2_TARGET_SHA,
        "j2_ct_raw_cocycle_canonical_sha256": J2_CT_SHA,
        "j2_cc_raw_cocycle_canonical_sha256": J2_CC_SHA,
    },
    "linear_system": {
        "variables": NVARS,
        "phi_variables": 2 * PHI_SIZE,
        "j2_anchor_coboundary_witness_variables": NP,
        "equations": len(equations),
        "rank_f2": rank,
        "nullity_f2": len(free),
        "consistent": True,
    },
    "j2_anchor": {
        "proper14_f2": j2,
        "retained_equation": "e2 + e3",
        "locked_75D_weight": sum(j2_h1_list),
        "homogeneous_boundary_ambiguity_rank_f2": 0,
    },
    "retained_standard_columns": [
        {
            "column_1based": i + 1,
            "source_proper14_f2": retained[i],
            "ambiguity_rank_in_H1_f2": ambiguity_ranks[i],
            "forced_by_module_actions_plus_j2_anchor": forced[i],
            "forced_75D_coordinate_f2": forced_coordinates[i],
        }
        for i in range(10)
    ],
    "e2_e3_split": {
        "C2_ambiguity_rank_f2": ambiguity_ranks[1],
        "C3_ambiguity_rank_f2": ambiguity_ranks[2],
        "C2_forced": forced[1],
        "C3_forced": forced[2],
        "C2_plus_C3_fixed_to_named_J2": True,
    },
    "nullspace_directions_with_nonzero_retained_H1_effect": nonzero_null_images,
    "interpretation_firewall": {
        "actual_geometric_extension_identified": False,
        "historical_rep88_promoted": False,
        "Q_defined_descent_credit_added": False,
        "standard_column_materialized_only_if_forced": True,
        "if_ambiguity_positive": "module actions plus the J2 anchor alone are insufficient to infer that column; an additional geometric mu2-lift/glue datum is still required",
    },
}
result["canonical_sha256"] = csha(result)
print(json.dumps(result, sort_keys=True))
