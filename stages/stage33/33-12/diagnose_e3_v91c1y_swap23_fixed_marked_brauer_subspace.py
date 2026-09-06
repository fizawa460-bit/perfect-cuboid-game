#!/usr/bin/env python3
"""V91C1Y NONCREDIT preflight: constrain the unknown A2_02 marked Brauer image.

V91C1X source-binds swap23-fixedness of the literal full-surface H2(mu2) seed.
By quotient naturality the unknown proper14 Brauer image must therefore be fixed
by cc, ct, and the exact swap23 word.  This diagnostic computes that exact
intersection and a minimal coordinate discriminator.  It does not compute any
source evaluation bit and grants no marked-image, theorem, receiver, endpoint,
or merge credit.
"""
from __future__ import annotations

import hashlib
import json
import os
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
X = HERE / "e3-v91c1x-a2-02-kummer-naturality-mask20-exclusion.json"
Q = HERE / "diagnose_e3_v91c1q_shortest_mask20_moving_stabilizer_word.py"
V84 = HERE / "diagnose_e3_coordinate_automorphism_orbit_v84.py"
BR = S33 / "33-07" / "proper-brauer2-from-discriminant.json"

X_SHA = "aca4d8929f9cc04b24da6e8a7ba0ec0b89be18ac1bc2bf3e6e1f870808bdf29f"
BR_SHA = "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
Q_BLOB = "1b83812cec6473f04de0e3cf7e2b70bfb47de409"
V84_BLOB = "e9c7e81cc59fb5203482071208d25ff1447edeb2"
WORD = ["swap12", "swap13", "swap12"]
N = 14


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def gitblob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


def rref(rows, n):
    a = [[int(x) & 1 for x in row] for row in rows if any(int(x) & 1 for x in row)]
    pivots = []
    rr = 0
    for col in range(n):
        pivot = next((i for i in range(rr, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rr], a[pivot] = a[pivot], a[rr]
        for i in range(len(a)):
            if i != rr and a[i][col]:
                a[i] = [x ^ y for x, y in zip(a[i], a[rr])]
        pivots.append(col)
        rr += 1
        if rr == len(a):
            break
    return a[:rr], pivots


def nullspace(equations, n):
    rr, pivots = rref(equations, n)
    free = [j for j in range(n) if j not in pivots]
    out = []
    for free_col in free:
        v = [0] * n
        v[free_col] = 1
        for row, pivot in zip(rr, pivots):
            v[pivot] = row[free_col]
        out.append(v)
    return out


def colact(matrix, vector):
    return tuple(
        sum(int(matrix[i][j]) * int(vector[j]) for j in range(len(vector))) & 1
        for i in range(len(vector))
    )


def apply_target(vector, word, generators):
    out = tuple(vector)
    for name in word:
        out = colact(generators[name], out)
    return out


def target_matrix(word, generators, n=N):
    # Columns are images of the standard column basis.
    cols = [
        apply_target([int(i == j) for i in range(n)], word, generators)
        for j in range(n)
    ]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def fixed_equations(matrix, n=N):
    # Column-vector convention: (M-I)v=0.
    return [
        [int(matrix[i][j]) ^ (1 if i == j else 0) for j in range(n)]
        for i in range(n)
    ]


x = load(X, X_SHA)
br = load(BR, BR_SHA)
assert gitblob(Q.read_bytes()) == Q_BLOB
assert gitblob(V84.read_bytes()) == V84_BLOB
assert x["exact_consequence"]["a2_02_swap23_seed_fixed_mod_pic2"] is True
assert x["exact_consequence"]["a2_02_marked_brauer_image_must_be_swap23_fixed"] is True
assert x["exact_consequence"]["a2_02_marked_brauer_image_excluded_from_mask20"] is True
assert x["exact_consequence"]["a2_02_marked_brauer_image_computed"] is False

q = runpy.run_path(str(Q))["result"]
assert q["word"] == WORD and q["source_a2_02_residue_fixed"] is True
assert q["mask20_moved"] is True and q["mask20_target_image_decimal"] == 22

ns = runpy.run_path(str(V84))
gens14 = ns["gens14"]
assert all(name in gens14 for name in WORD)
swap23 = target_matrix(WORD, gens14)
cc = br["proper_Br2_cc_action_f2"]
ct = br["proper_Br2_ct_action_f2"]

mask20 = tuple([0, 0, 1, 0, 1] + [0] * 9)
assert colact(cc, mask20) == mask20
assert colact(ct, mask20) == mask20
assert colact(swap23, mask20) != mask20
assert colact(swap23, mask20) == tuple([0, 1, 1, 0, 1] + [0] * 9)

v4_eq = fixed_equations(cc) + fixed_equations(ct)
v4_basis = nullspace(v4_eq, N)
assert len(v4_basis) == 10 == br["proper_Br2_joint_v4_fixed_dimension_f2"]

fixed_eq = v4_eq + fixed_equations(swap23)
fixed_basis = nullspace(fixed_eq, N)
fixed_dim = len(fixed_basis)
assert fixed_dim < 10
assert all(colact(cc, v) == tuple(v) for v in fixed_basis)
assert all(colact(ct, v) == tuple(v) for v in fixed_basis)
assert all(colact(swap23, v) == tuple(v) for v in fixed_basis)
assert mask20 not in [tuple(v) for v in fixed_basis]

# Pivot coordinate functionals on a basis matrix give a minimal injective
# coordinate projection on the fixed subspace.
_, coord_pivots = rref(fixed_basis, N)
assert len(coord_pivots) == fixed_dim
selected = [p + 1 for p in coord_pivots]
restriction = [[row[p] for p in coord_pivots] for row in fixed_basis]
assert len(rref(restriction, fixed_dim)[1]) == fixed_dim

result = {
    "success": True,
    "marker": "V91C1Y_SWAP23_FIXED_MARKED_BRAUER_SUBSPACE_PREFLIGHT",
    "source_bound_input": "V91C1X_SWAP23_LITERAL_H2_SEED_FIXEDNESS",
    "proper14_dimension_f2": N,
    "joint_cc_ct_fixed_dimension_f2": len(v4_basis),
    "joint_cc_ct_swap23_fixed_dimension_f2": fixed_dim,
    "joint_cc_ct_swap23_fixed_cardinality": 1 << fixed_dim,
    "dimension_drop_from_v4_fixed": len(v4_basis) - fixed_dim,
    "fixed_basis_f2": fixed_basis,
    "minimal_coordinate_discriminator_positions_one_based": selected,
    "minimal_coordinate_discriminator_bit_count": fixed_dim,
    "mask20_excluded": True,
    "mask20_swap23_image_decimal": 22,
    "source_bound_proper14_evaluation_bits_materialized": 0,
    "actual_marked_brauer_image_computed": False,
    "credit": False,
}
print(json.dumps(result, sort_keys=True))
annotation = json.dumps(result, sort_keys=True, separators=(",", ":"))
print(
    "::warning file=stages/stage33/33-12/diagnose_e3_v91c1y_swap23_fixed_marked_brauer_subspace.py,"
    "title=V91C1Y_SWAP23_FIXED_SUBSPACE::" + annotation
)
if os.environ.get("GITHUB_ENV"):
    with open(os.environ["GITHUB_ENV"], "a", encoding="utf-8") as out:
        out.write(f"V91C1Y_FIXED_DIM={fixed_dim}\n")
        out.write("V91C1Y_COORDS=" + ",".join(map(str, selected)) + "\n")
