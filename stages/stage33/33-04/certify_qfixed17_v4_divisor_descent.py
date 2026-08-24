#!/usr/bin/env python3
"""Certify the finite V4 divisor-parity descent skeleton for the Q-fixed17 residual.

This leaf is intentionally narrower than arithmetic Brauer descent.  It proves
that each of the 17 residual edge patterns is invariant under the two pinned V4
generators and gives an even parity divisor on every geometric boundary
component.  Hence there is no remaining *finite permutation/divisor-parity*
obstruction at the level already modeled by the Stage33-04 boundary complex.

It does NOT promote those geometric Kummer residues to Q-defined Brauer
classes.  Descent of the actual first-residue functions, including constants /
squareclasses and any nontrivial Q-form issue for the normalized components,
remains downstream.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sk = json.loads((ROOT / "boundary-residue-skeleton.json").read_text())
bg = json.loads((ROOT / "boundary-galois.json").read_text())
q17 = json.loads((ROOT / "qfixed17-graph-residual.json").read_text())

if sk["component_count"] != 72 or sk["codim2_crossing_count"] != 144:
    raise SystemExit("boundary inventory regression")
vecs = [[int(x) & 1 for x in v] for v in q17["qfixed_residual_basis_edge_vectors_144"]]
if len(vecs) != 17 or any(len(v) != 144 for v in vecs):
    raise SystemExit("Q-fixed17 basis regression")

cc = [int(x) - 1 for x in bg["boundary_perm_cc_1based"]]
ct = [int(x) - 1 for x in bg["boundary_perm_ct_1based"]]
if sorted(cc) != list(range(72)) or sorted(ct) != list(range(72)):
    raise SystemExit("boundary Galois permutation regression")

# Stable edge lookup from the SNC skeleton.
edges = []
edge_index = {}
for idx, e in enumerate(sk["codim2_crossings"]):
    a = int(e["side_vertex"]) - 1
    b = int(e["exceptional_vertex"]) - 1
    key = tuple(sorted((a, b)))
    if key in edge_index:
        raise SystemExit("duplicate crossing edge")
    edge_index[key] = idx
    edges.append((a, b))


def edge_perm(p):
    out = []
    for a, b in edges:
        key = tuple(sorted((p[a], p[b])))
        if key not in edge_index:
            raise SystemExit("Galois action does not preserve crossing graph")
        out.append(edge_index[key])
    if sorted(out) != list(range(144)):
        raise SystemExit("invalid induced edge permutation")
    return out


ecc = edge_perm(cc)
ect = edge_perm(ct)


def act_edge_vector(v, ep):
    w = [0] * len(v)
    for j, image in enumerate(ep):
        w[image] = v[j]
    return w


def component_parities(v):
    deg = [0] * 72
    for bit, (a, b) in zip(v, edges):
        if bit:
            deg[a] ^= 1
            deg[b] ^= 1
    return deg

for i, v in enumerate(vecs):
    if act_edge_vector(v, ecc) != v:
        raise SystemExit(f"residual vector {i} not fixed by complex conjugation")
    if act_edge_vector(v, ect) != v:
        raise SystemExit(f"residual vector {i} not fixed by sqrt(2)-conjugation")
    if any(component_parities(v)):
        raise SystemExit(f"residual vector {i} has odd component divisor parity")

# Record component orbits under the exact V4 permutation action.
unseen = set(range(72))
orbits = []
while unseen:
    s = min(unseen)
    orb = {s, cc[s], ct[s], cc[ct[s]], ct[cc[s]]}
    # close under generators defensively
    changed = True
    while changed:
        changed = False
        for x in list(orb):
            for p in (cc, ct):
                y = p[x]
                if y not in orb:
                    orb.add(y)
                    changed = True
    unseen -= orb
    orbits.append(sorted(x + 1 for x in orb))

cert = {
    "schema": "STAGE33_04_QFIXED17_V4_DIVISOR_DESCENT_V1",
    "source_locks": {
        "boundary_skeleton_sha256": sk["canonical_sha256"],
        "boundary_galois_sha256": bg["canonical_sha256"],
        "qfixed17_graph_residual_sha256": q17["canonical_sha256"],
    },
    "boundary_component_count": 72,
    "boundary_component_orbit_count_under_v4": len(orbits),
    "boundary_component_orbits_1based": orbits,
    "qfixed17_dimension_f2": 17,
    "all_17_edge_patterns_fixed_by_cc": True,
    "all_17_edge_patterns_fixed_by_ct": True,
    "all_17_edge_patterns_even_on_every_component": True,
    "finite_v4_permutation_descent_compatibility_complete": True,
    "finite_divisor_parity_descent_obstruction_zero": True,
    "actual_first_residue_function_descent_complete": False,
    "constant_squareclass_descent_complete": False,
    "q_defined_brauer_class_dimension_certified": False,
    "physical_open_unramified_kernel_complete": False,
    "br0g_discharged": False,
    "new_residual_kernel": "R33-BR0G-QFIXED17-FUNCTION-AND-CONSTANT-SQUARECLASS-DESCENT",
    "next_exact_leaf": "L33-04-DESCEND-FIRST-RESIDUE-FUNCTIONS-MOD-SQUARES-AND-CONSTANTS",
    "loop_guard": "Do not reopen graph invariance, component parity, geometric realizability, Ford pullback, or unit-symbol span; only function/constant arithmetic descent remains.",
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "qfixed17-v4-divisor-descent.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "component_orbits": len(orbits),
    "qfixed17_dimension": 17,
    "finite_divisor_parity_descent_obstruction_zero": True,
    "remaining_kernel": cert["new_residual_kernel"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
