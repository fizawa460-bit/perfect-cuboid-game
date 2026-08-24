#!/usr/bin/env python3
"""Close the geometric first-residue realizability part of the Q-fixed17 wall.

Loop guard: this leaf does exactly one thing.  It does NOT attempt arithmetic
G_Q descent.  On each geometric boundary component D_j ~= P^1 over Qbar,
Kummer theory identifies H^1(Qbar(D_j), Z/2) with k(D_j)^*/k(D_j)^{*2}.
The divisor sequence on P^1 shows that a finite parity prescription at closed
points is realizable iff its total degree is even.  For the SNC boundary, that
condition at every vertex is exactly the dual-graph cycle condition already
certified by qfixed17-graph-residual.json.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sk = json.loads((ROOT / "boundary-residue-skeleton.json").read_text())
q17 = json.loads((ROOT / "qfixed17-graph-residual.json").read_text())

if sk["component_count"] != 72 or sk["codim2_crossing_count"] != 144:
    raise SystemExit("boundary inventory regression")
vecs = q17["qfixed_residual_basis_edge_vectors_144"]
if len(vecs) != 17 or any(len(v) != 144 for v in vecs):
    raise SystemExit("Q-fixed17 basis regression")

edges = [(int(e["side_vertex"]) - 1, int(e["exceptional_vertex"]) - 1)
         for e in sk["codim2_crossings"]]
vertex_parities = []
for idx, v in enumerate(vecs):
    deg = [0] * 72
    for bit, (a, b) in zip(v, edges):
        if int(bit) & 1:
            deg[a] ^= 1
            deg[b] ^= 1
    if any(deg):
        raise SystemExit(f"residual basis vector {idx} violates even divisor parity")
    vertex_parities.append(deg)

# Self-contained theorem adapter used here:
# 0 -> k^* -> k(P1)^* -> Div(P1) -> Pic(P1) -> 0,
# with k=Qbar and Pic(P1)=Z.  Modulo squares, a finite divisor-parity vector is
# therefore in the image of k(P1)^*/k(P1)^{*2} iff its total degree is even.
# The Stage29 Gersten receiver then identifies the second-residue compatibility
# condition with the graph boundary condition.  Proper Brauer classes have zero
# boundary residue, so quotienting by Br(Sbar) does not alter a nonzero residue
# vector/coset.  None of this supplies arithmetic G_Q descent.

cert = {
    "schema": "STAGE33_04_QFIXED17_FIRST_RESIDUE_REALIZABILITY_V1",
    "source_locks": {
        "boundary_skeleton_sha256": sk["canonical_sha256"],
        "qfixed17_graph_residual_sha256": q17["canonical_sha256"],
        "stage29_gersten_receiver": "stages/stage29/29-02f/boundary-gersten-receiver.md",
        "divisor_sequence_adapter": "0->k*->k(P1)*->Div(P1)->Pic(P1)->0; Pic(P1)=Z; reduce valuations mod 2",
    },
    "boundary_component_count": 72,
    "boundary_components_geometric_genus_zero": True,
    "qfixed_residual_dimension_f2": 17,
    "all_17_vectors_even_at_every_boundary_component": True,
    "kummer_first_residue_realizability_over_qbar_complete": True,
    "gersten_second_residue_compatibility_complete": True,
    "proper_brauer_classes_have_zero_boundary_residue": True,
    "proper_brauer_residue_quotient_changes_residual_vectors": False,
    "geometric_qfixed17_residue_cosets_realizable": True,
    "arithmetic_gq_descent_complete": False,
    "q_defined_brauer_class_dimension_certified": False,
    "physical_open_unramified_kernel_complete": False,
    "br0g_discharged": False,
    "new_residual_kernel": "R33-BR0G-QFIXED17-GALOIS-DESCENT",
    "next_exact_leaf": "STOP_AND_AUDIT_OR_ATTACK_R33-BR0G-QFIXED17-GALOIS-DESCENT",
    "loop_guard": "Do not reopen geometric realizability or search more unit functions; only arithmetic descent remains for this 17D quotient.",
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "qfixed17-first-residue-realizability.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "qfixed17_geometric_realizability": True,
    "remaining_kernel": cert["new_residual_kernel"],
    "loop_guard": cert["loop_guard"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
