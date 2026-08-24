#!/usr/bin/env python3
"""Materialize the exact 17D Q-fixed graph-residue quotient left after unit-symbol footprints.

This is a graph-level Gersten certificate only.  The 17 quotient directions are
NOT promoted to Brauer classes: realizability by first-residue data on the
normalized boundary components, proper-Brauer quotienting, and arithmetic
descent remain explicit downstream conditions.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sk = json.loads((ROOT / "boundary-residue-skeleton.json").read_text())
cg = json.loads((ROOT / "boundary-cycle-galois.json").read_text())
us = json.loads((ROOT / "unit-symbol-residue-span.json").read_text())


def rref2(A):
    A = [[int(x) & 1 for x in row] for row in A]
    if not A:
        return A, []
    m, n = len(A), len(A[0])
    piv = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c]), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        for i in range(m):
            if i != r and A[i][c]:
                A[i] = [x ^ y for x, y in zip(A[i], A[r])]
        piv.append(c)
        r += 1
        if r == m:
            break
    return A, piv


def rank2(A):
    return len(rref2(A)[1])


def nullspace2(M):
    R, piv = rref2(M)
    n = len(M[0]) if M else 0
    free = [j for j in range(n) if j not in piv]
    out = []
    for f in free:
        x = [0] * n
        x[f] = 1
        for ri, p in enumerate(piv):
            x[p] = R[ri][f]
        out.append(x)
    return out


def rowmul2(v, M):
    return [sum((int(v[k]) & 1) * (int(M[k][j]) & 1) for k in range(len(v))) & 1
            for j in range(len(M[0]))]


def transpose(M):
    return [list(x) for x in zip(*M)]


def inv2(A):
    n = len(A)
    aug = [[int(x) & 1 for x in A[i]] + [int(i == j) for j in range(n)] for i in range(n)]
    r = 0
    for c in range(n):
        p = next((i for i in range(r, n) if aug[i][c]), None)
        if p is None:
            raise SystemExit("pivot minor is singular mod 2")
        aug[r], aug[p] = aug[p], aug[r]
        for i in range(n):
            if i != r and aug[i][c]:
                aug[i] = [x ^ y for x, y in zip(aug[i], aug[r])]
        r += 1
    return [row[n:] for row in aug]


K = [[int(x) & 1 for x in row] for row in sk["integral_cycle_basis"]]
if len(K) != 73 or any(len(r) != 144 for r in K) or rank2(K) != 73:
    raise SystemExit("boundary cycle basis mod-2 rank regression")

Ccc = [[int(x) & 1 for x in row] for row in cg["cycle_lattice"]["cc_matrix"]]
Cct = [[int(x) & 1 for x in row] for row in cg["cycle_lattice"]["ct_matrix"]]
I = [[int(i == j) for j in range(73)] for i in range(73)]
eqs = []
for C in (Ccc, Cct):
    D = [[C[i][j] ^ I[i][j] for j in range(73)] for i in range(73)]
    eqs.extend(transpose(D))  # row coordinates x satisfy x(C-I)=0
fixed_coords = nullspace2(eqs)
if len(fixed_coords) != 61:
    raise SystemExit(f"Q-fixed cycle dimension regression: {len(fixed_coords)}")

# Convert 144-edge cycle vectors to coordinates in the stable 73-row cycle basis.
_, pivot_cols = rref2(K)
if len(pivot_cols) != 73:
    raise SystemExit("failed to choose mod-2 cycle pivot minor")
A = [[K[i][j] for j in pivot_cols] for i in range(73)]
Ainv = inv2(A)


def cycle_coords(edge_vector):
    y = [int(edge_vector[j]) & 1 for j in pivot_cols]
    x = rowmul2(y, Ainv)
    if rowmul2(x, K) != [int(q) & 1 for q in edge_vector]:
        raise SystemExit("cycle coordinate reconstruction failed")
    return x


unit_coords = [cycle_coords(v) for v in us["independent_secondary_residue_patterns"]]
if rank2(unit_coords) != 44:
    raise SystemExit("unit-symbol image rank regression")
for x in unit_coords:
    if rowmul2(x, Ccc) != x or rowmul2(x, Cct) != x:
        raise SystemExit("unit-symbol image escaped Q-fixed cycle space")

# Extend the exact 44D unit-symbol image to the complete 61D fixed cycle space.
basis = unit_coords[:]
r = rank2(basis)
complement_coords = []
for x in fixed_coords:
    nr = rank2(basis + [x])
    if nr > r:
        complement_coords.append(x)
        basis.append(x)
        r = nr
if len(complement_coords) != 17 or r != 61:
    raise SystemExit(f"Q-fixed quotient dimension regression: complement={len(complement_coords)}, rank={r}")
complement_edges = [rowmul2(x, K) for x in complement_coords]

# Every explicit residual vector is a graph cycle and Q-fixed by construction.
edges = [(int(e["side_vertex"]) - 1, int(e["exceptional_vertex"]) - 1)
         for e in sk["codim2_crossings"]]
for v in complement_edges:
    bd = [0] * 72
    for bit, (a, b) in zip(v, edges):
        if bit:
            bd[a] ^= 1
            bd[b] ^= 1
    if any(bd):
        raise SystemExit("residual vector is not a graph cycle")

cert = {
    "schema": "STAGE33_04_QFIXED17_GRAPH_RESIDUAL_V1",
    "source_locks": {
        "boundary_skeleton_sha256": sk["canonical_sha256"],
        "cycle_galois_sha256": cg["canonical_sha256"],
        "unit_symbol_residue_span_sha256": us["canonical_sha256"],
    },
    "boundary_cycle_dimension_f2": 73,
    "qfixed_boundary_cycle_dimension_f2": 61,
    "unit_symbol_secondary_residue_image_dimension_f2": 44,
    "qfixed_quotient_after_unit_symbol_image_dimension_f2": 17,
    "cycle_basis_pivot_edges_1based": [j + 1 for j in pivot_cols],
    "qfixed_residual_basis_cycle_coordinates_73": complement_coords,
    "qfixed_residual_basis_edge_vectors_144": complement_edges,
    "qfixed_residual_basis_edge_weights": [sum(v) for v in complement_edges],
    "all_residual_basis_vectors_are_graph_cycles": True,
    "all_residual_basis_vectors_are_qfixed": True,
    "quotient_basis_exact": True,
    "brauer_class_realizability_certified": False,
    "proper_brauer_quotient_complete": False,
    "boundary_component_h1_realization_complete": False,
    "cyclotomic_coefficient_descent_complete": False,
    "physical_open_unramified_kernel_complete": False,
    "br0g_discharged": False,
    "new_residual_kernel": "R33-BR0G-QFIXED17-FIRST-RESIDUE-REALIZABILITY-AND-DESCENT",
    "next_exact_leaf": "L33-04-REALIZE-OR-KILL-QFIXED17-IN-BOUNDARY-H1-THEN-QUOTIENT-PROPER-BRAUER",
    "firewall": "17D is a quotient of graph-level compatible secondary residues, not a certified 17D Brauer group",
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "qfixed17-graph-residual.json").write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "qfixed_cycle_dim": 61,
    "unit_symbol_image_dim": 44,
    "qfixed_residual_dim": 17,
    "new_residual_kernel": cert["new_residual_kernel"],
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
