#!/usr/bin/env python3
"""V91C1Z NONCREDIT target preflight after V91C1Y.

Starting from the source-bound cc/ct/swap23-fixed proper14 subspace computed by
V91C1Y, enumerate exact Schreier generators of the A2_02 *residue* stabilizer
and greedily select target actions that further reduce that 7D subspace.

This is conditional target routing only.  A residue-stabilizer word is NOT
promoted to literal H2(mu2)-seed fixedness here.  Each selected word must later
be tested on the literal Cech-Cartier seed and reduced through Pic/2 exactly.
"""
from __future__ import annotations

import hashlib
import json
import os
import runpy
from collections import deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
SRC = S33 / "33-11f" / "stage33-11f-source-lock.json"
V84 = HERE / "diagnose_e3_coordinate_automorphism_orbit_v84.py"
Y = HERE / "diagnose_e3_v91c1y_swap23_fixed_marked_brauer_subspace.py"

SRC_SHA = "3c493c5863a1506e48622ec9180119b6b80f5ee0642fe20515916749b3138957"
V84_BLOB = "e9c7e81cc59fb5203482071208d25ff1447edeb2"
Y_BLOB = "0a6626e368d2ee573a998a66b6f821350533debe"
N = 14


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def gitblob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


def rref(rows, n):
    a = [[int(x) & 1 for x in row] for row in rows if any(int(x) & 1 for x in row)]
    pivots = []; rr = 0
    for col in range(n):
        pivot = next((i for i in range(rr, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rr], a[pivot] = a[pivot], a[rr]
        for i in range(len(a)):
            if i != rr and a[i][col]:
                a[i] = [x ^ y for x, y in zip(a[i], a[rr])]
        pivots.append(col); rr += 1
        if rr == len(a):
            break
    return a[:rr], pivots


def nullspace(equations, n):
    rr, pivots = rref(equations, n)
    free = [j for j in range(n) if j not in pivots]
    out = []
    for f in free:
        v = [0] * n; v[f] = 1
        for row, pivot in zip(rr, pivots):
            v[pivot] = row[f]
        out.append(v)
    return out


def rowmul(v, matrix):
    return tuple(
        sum(int(v[i]) * int(matrix[i][j]) for i in range(len(v))) & 1
        for j in range(len(v))
    )


def colact(matrix, v):
    return tuple(
        sum(int(matrix[i][j]) * int(v[j]) for j in range(len(v))) & 1
        for i in range(len(v))
    )


def apply_target(v, word, generators):
    out = tuple(v)
    for name in word:
        out = colact(generators[name], out)
    return out


def target_matrix(word, generators, n=N):
    cols = [
        apply_target([int(i == j) for i in range(n)], word, generators)
        for j in range(n)
    ]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def intersect_basis_with_fixed_action(basis, matrix):
    """Return a basis of span(basis) intersect Fix(matrix), column convention."""
    d = len(basis)
    if d == 0:
        return []
    defects = []
    for b in basis:
        image = colact(matrix, b)
        defects.append([x ^ y for x, y in zip(image, b)])
    equations = [[defects[k][i] for k in range(d)] for i in range(N)]
    coeff_basis = nullspace(equations, d)
    out = []
    for coeffs in coeff_basis:
        v = [0] * N
        for c, b in zip(coeffs, basis):
            if c:
                v = [x ^ y for x, y in zip(v, b)]
        out.append(v)
    return out


src = load(SRC, SRC_SHA)
assert gitblob(V84.read_bytes()) == V84_BLOB
assert gitblob(Y.read_bytes()) == Y_BLOB
yns = runpy.run_path(str(Y))
y = yns["result"]
assert y["success"] is True
assert y["joint_cc_ct_swap23_fixed_dimension_f2"] == 7
base_basis = [list(v) for v in y["fixed_basis_f2"]]

v84 = runpy.run_path(str(V84))
gens14 = v84["gens14"]
names = src["exact_source_actions"]["action_names"]
acts = src["exact_source_actions"]["matrices"]
assert set(names) == set(gens14)

# Exact A2_02 residue orbit and Schreier stabilizer words, matching V91C1P.
start = tuple([0, 1] + [0] * 24)
representatives = {start: []}
queue = deque([start])
while queue:
    v = queue.popleft()
    for name, matrix in zip(names, acts):
        w = rowmul(v, matrix)
        if w not in representatives:
            representatives[w] = representatives[v] + [name]
            queue.append(w)

seen_target = set()
actions = []
for v, rep_v in representatives.items():
    for name, matrix in zip(names, acts):
        w = rowmul(v, matrix)
        word = rep_v + [name] + list(reversed(representatives[w]))
        z = start
        for nm in word:
            z = rowmul(z, acts[names.index(nm)])
        assert z == start
        target = target_matrix(word, gens14)
        key = tuple(tuple(row) for row in target)
        if key in seen_target:
            continue
        seen_target.add(key)
        actions.append((word, target))

# Greedily pick the shortest/lexicographically first action among those giving
# the maximum dimension drop at each step.  This is deterministic routing only.
current = base_basis
selected = []
dimension_path = [len(current)]
remaining = list(actions)
while True:
    candidates = []
    for word, matrix in remaining:
        new_basis = intersect_basis_with_fixed_action(current, matrix)
        new_dim = len(new_basis)
        if new_dim < len(current):
            candidates.append((new_dim, len(word), tuple(word), word, matrix, new_basis))
    if not candidates:
        break
    candidates.sort(key=lambda item: (item[0], item[1], item[2]))
    new_dim, _length, _lex, word, matrix, new_basis = candidates[0]
    selected.append({
        "word": word,
        "word_length": len(word),
        "dimension_before": len(current),
        "dimension_after_if_literal_seed_fixed": new_dim,
    })
    current = new_basis
    dimension_path.append(len(current))
    # Keep all distinct actions: later actions can still reduce the new space.

result = {
    "success": True,
    "marker": "V91C1Z_NEXT_RESIDUE_STABILIZER_REDUCERS",
    "source_orbit_size": len(representatives),
    "distinct_target_residue_stabilizer_actions": len(actions),
    "entry_source_bound_fixed_dimension_f2": len(base_basis),
    "greedy_selected_reducer_count": len(selected),
    "greedy_selected_reducers": selected,
    "conditional_dimension_path_if_all_selected_words_fix_literal_seed": dimension_path,
    "conditional_final_dimension_f2": len(current),
    "conditional_final_cardinality": 1 << len(current),
    "selected_words_literal_h2_seed_fixedness_materialized": False,
    "selected_words_pic2_differences_computed": False,
    "actual_marked_brauer_image_computed": False,
    "credit": False,
}
print(json.dumps(result, sort_keys=True))
print(
    "::warning file=stages/stage33/33-12/diagnose_e3_v91c1z_next_stabilizer_reducers.py,"
    "title=V91C1Z_REDUCERS::"
    + json.dumps(result, sort_keys=True, separators=(",", ":"))
)
if os.environ.get("GITHUB_ENV"):
    with open(os.environ["GITHUB_ENV"], "a", encoding="utf-8") as out:
        out.write(f"V91C1Z_FINAL_DIM={len(current)}\n")
        out.write(f"V91C1Z_REDUCER_COUNT={len(selected)}\n")
