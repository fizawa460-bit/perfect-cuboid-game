#!/usr/bin/env python3
from __future__ import annotations

import json

POINTS = ["0", "inf", "1", "-1", "i", "-i"]
IDX = {name: i for i, name in enumerate(POINTS)}
ALL = (1 << 6) - 1

# Cecotti Appendix B on y^2=x^5-x:
# B.7: x -> -(x+i)/(1+i*x)
# B.8: x -> i*(x-1)/(x+1)
B7 = {"0": "-i", "inf": "i", "1": "-1", "-1": "1", "i": "inf", "-i": "0"}
B8 = {"0": "-i", "inf": "i", "1": "0", "-1": "inf", "i": "-1", "-i": "1"}

# J[2] = even subsets of the six Weierstrass points modulo complements.
# Basis: delta_0inf, delta_1inf, delta_-1inf, delta_iinf.
BASIS_MASKS = [
    (1 << IDX["0"]) | (1 << IDX["inf"]),
    (1 << IDX["1"]) | (1 << IDX["inf"]),
    (1 << IDX["-1"]) | (1 << IDX["inf"]),
    (1 << IDX["i"]) | (1 << IDX["inf"]),
]


def qcanon(mask: int) -> int:
    mask &= ALL
    return min(mask, mask ^ ALL)


SPAN: dict[int, tuple[int, int, int, int]] = {}
for bits in range(16):
    mask = 0
    for j, bm in enumerate(BASIS_MASKS):
        if (bits >> j) & 1:
            mask ^= bm
    SPAN[qcanon(mask)] = tuple((bits >> j) & 1 for j in range(4))
assert len(SPAN) == 16


def act_mask(mask: int, perm: dict[str, str]) -> int:
    out = 0
    for name in POINTS:
        if (mask >> IDX[name]) & 1:
            out ^= 1 << IDX[perm[name]]
    return out


def rep_matrix(perm: dict[str, str]) -> list[list[int]]:
    cols = []
    for bm in BASIS_MASKS:
        cols.append(SPAN[qcanon(act_mask(bm, perm))])
    return [[cols[c][r] for c in range(4)] for r in range(4)]


def mm(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(4)) & 1 for j in range(4)]
        for i in range(4)
    ]


def mv(A, v):
    return [sum(A[i][k] * v[k] for k in range(4)) & 1 for i in range(4)]


def rank4(A):
    rows = [sum((A[i][j] & 1) << j for j in range(4)) for i in range(4)]
    rank = 0
    for c in range(4):
        pivot = next((i for i in range(rank, 4) if (rows[i] >> c) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(4):
            if i != rank and ((rows[i] >> c) & 1):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def mat_from_bits(bits: int):
    return [[(bits >> (4 * i + j)) & 1 for j in range(4)] for i in range(4)]


A7 = rep_matrix(B7)
A8 = rep_matrix(B8)

# Retained lattice basis (e1,e2,r*e1,r*e2), r^2=-2.
# Mod 2, S=b4 and T=-b3=b3 act as below.
S = [
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
]
T = [
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
]

solutions = []
for bits in range(1 << 16):
    P = mat_from_bits(bits)
    if rank4(P) != 4:
        continue
    if mm(P, A7) == mm(S, P) and mm(P, A8) == mm(T, P):
        solutions.append(P)


def pair_vec(a, b):
    return list(SPAN[qcanon((1 << IDX[a]) | (1 << IDX[b]))])


Z = {
    "Z1": pair_vec("1", "-1"),
    "Z2": pair_vec("i", "-i"),
    "Z3": pair_vec("0", "inf"),
}
L = {
    "L1": [0, 0, 1, 0],
    "L2": [0, 0, 0, 1],
    "L3": [0, 0, 1, 1],
}

images = []
for P in solutions:
    images.append({z: mv(P, vec) for z, vec in Z.items()})

assert len(solutions) == 2
assert all(im["Z1"] == L["L1"] for im in images)
assert all(im["Z2"] == L["L2"] for im in images)
assert all(im["Z3"] == L["L3"] for im in images)

out = {
    "schema": "STAGE32_SCRATCH_B7_B8_J2_RETAINED_W_INTERTWINER_V1",
    "source_J2_basis": ["delta_0inf", "delta_1inf", "delta_-1inf", "delta_iinf"],
    "B7_J2_matrix": A7,
    "B8_J2_matrix": A8,
    "retained_mod2_S_equals_b4": S,
    "retained_mod2_T_equals_minus_b3": T,
    "invertible_F2_intertwiner_count": len(solutions),
    "intertwiners": solutions,
    "pair_vectors": Z,
    "images_under_every_intertwiner": images,
    "forced_pair_line_map": {"Z1": "L1", "Z2": "L2", "Z3": "L3"},
    "forced_delta_0inf_line_if_ordered_generator_pair_is_source_bound": "L3",
    "forced_q602_residue_if_ordered_generator_pair_is_source_bound": 235,
    "absolute_identification_promoted_now": False,
}
print(json.dumps(out, sort_keys=True, indent=2))
