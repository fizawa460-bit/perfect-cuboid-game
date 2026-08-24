#!/usr/bin/env python3
import hashlib
import json
import pathlib

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parent
skel = json.loads((ROOT / "boundary-residue-skeleton.json").read_text(encoding="utf-8"))
gal = json.loads((ROOT / "boundary-galois.json").read_text(encoding="utf-8"))

if skel["component_count"] != 72 or skel["codim2_crossing_count"] != 144 or skel["dual_graph_cycle_rank"] != 73:
    raise SystemExit("unexpected boundary skeleton dimensions")


def perm_matrix(perm_1based):
    n = len(perm_1based)
    P = sp.zeros(n)
    for j, image in enumerate(perm_1based):
        P[j, image - 1] = 1
    return P


def basis_action_on_row_lattice(K, P):
    pivots = list(K.rref()[1])
    if len(pivots) != K.rows:
        raise SystemExit("cycle basis lost rank")
    minor = K[:, pivots]
    acted = K * P
    A = acted[:, pivots] * minor.inv()
    if any(sp.Rational(A[i, j]).q != 1 for i in range(A.rows) for j in range(A.cols)):
        raise SystemExit("cycle Galois action not integral in saturated basis")
    A = sp.Matrix([[int(A[i, j]) for j in range(A.cols)] for i in range(A.rows)])
    if A * K != acted:
        raise SystemExit("cycle action reconstruction failed")
    return A, pivots


def rank_mod2_matrix(M):
    a = [[int(M[i, j]) & 1 for j in range(M.cols)] for i in range(M.rows)]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((u for u in range(r, m) if a[u][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        for u in range(m):
            if u != r and a[u][c]:
                a[u] = [x ^ y for x, y in zip(a[u], a[r])]
        r += 1
        if r == m:
            break
    return r


def int_rows(M):
    return [[int(M[i, j]) for j in range(M.cols)] for i in range(M.rows)]


cc_v = gal["boundary_perm_cc_1based"]
ct_v = gal["boundary_perm_ct_1based"]
if len(cc_v) != 72 or len(ct_v) != 72:
    raise SystemExit("bad vertex permutation size")

edges = [(e["side_vertex"], e["exceptional_vertex"]) for e in skel["codim2_crossings"]]
if len(edges) != 144 or len(set(edges)) != 144:
    raise SystemExit("edge inventory not unique")
edge_index = {edge: i + 1 for i, edge in enumerate(edges)}


def induced_edge_perm(vperm):
    out = []
    for a, b in edges:
        image = (vperm[a - 1], vperm[b - 1])
        if image not in edge_index:
            raise SystemExit(f"Galois image of crossing missing: {(a,b)} -> {image}")
        out.append(edge_index[image])
    return out

cc_e = induced_edge_perm(cc_v)
ct_e = induced_edge_perm(ct_v)
Pcc = perm_matrix(cc_e)
Pct = perm_matrix(ct_e)
I144 = sp.eye(144)
if Pcc * Pcc != I144 or Pct * Pct != I144 or Pcc * Pct != Pct * Pcc:
    raise SystemExit("edge actions do not realize V4")

K = sp.Matrix(skel["integral_cycle_basis"])
if K.shape != (73, 144) or K.rank() != 73:
    raise SystemExit("unexpected saturated cycle basis")
Ccc, pivots = basis_action_on_row_lattice(K, Pcc)
Cct, pivots2 = basis_action_on_row_lattice(K, Pct)
if pivots != pivots2:
    raise SystemExit("cycle pivot basis mismatch")
I73 = sp.eye(73)
if Ccc * Ccc != I73 or Cct * Cct != I73 or Ccc * Cct != Cct * Ccc:
    raise SystemExit("cycle-lattice V4 relation failed")

traces = {
    "id": 73,
    "cc": int(sp.trace(Ccc)),
    "ct": int(sp.trace(Cct)),
    "cct": int(sp.trace(Ccc * Cct)),
}
mult = {}
for ea in (1, -1):
    for eb in (1, -1):
        num = 73 + ea * traces["cc"] + eb * traces["ct"] + ea * eb * traces["cct"]
        if num % 4:
            raise SystemExit(f"nonintegral V4 character multiplicity numerator {num}")
        mult[f"cc{ea:+d}_ct{eb:+d}"] = num // 4
if sum(mult.values()) != 73 or any(v < 0 for v in mult.values()):
    raise SystemExit(f"bad cycle V4 multiplicities {mult}")

# For odd primes, |V4| is invertible and the residue cycle coefficient module
# splits into these sign-character pieces.  Q-invariant odd-primary cycles are
# exactly the (+,+) piece.  For 2-torsion the action is not semisimple; record
# exact fixed-space dimensions over F2 instead of reusing the odd-prime count.
cc_fixed_f2 = 73 - rank_mod2_matrix(Ccc - I73)
ct_fixed_f2 = 73 - rank_mod2_matrix(Cct - I73)
joint = (Ccc - I73).col_join(Cct - I73)
joint_fixed_f2 = 73 - rank_mod2_matrix(joint)

certificate = {
    "schema": "STAGE33_04_BOUNDARY_CYCLE_GALOIS_V1",
    "source_locks": {
        "boundary_skeleton_sha256": skel["canonical_sha256"],
        "boundary_galois_sha256": gal["canonical_sha256"],
    },
    "vertex_action": {
        "cc_fixed": sum(j == x for j, x in enumerate(cc_v, 1)),
        "ct_fixed": sum(j == x for j, x in enumerate(ct_v, 1)),
    },
    "edge_action": {
        "edge_count": 144,
        "cc_fixed": sum(j == x for j, x in enumerate(cc_e, 1)),
        "ct_fixed": sum(j == x for j, x in enumerate(ct_e, 1)),
        "cc_perm_1based": cc_e,
        "ct_perm_1based": ct_e,
    },
    "cycle_lattice": {
        "rank": 73,
        "basis_pivot_edges_1based": [x + 1 for x in pivots],
        "cc_matrix": int_rows(Ccc),
        "ct_matrix": int_rows(Cct),
        "character_traces": traces,
        "v4_rational_character_multiplicities": mult,
        "odd_primary_q_invariant_cycle_rank": mult["cc+1_ct+1"],
        "f2_fixed_dimension_cc": cc_fixed_f2,
        "f2_fixed_dimension_ct": ct_fixed_f2,
        "f2_joint_fixed_dimension": joint_fixed_f2,
    },
    "exact_checks": {
        "all_144_crossings_galois_stable": True,
        "edge_v4_relations": True,
        "cycle_lattice_integrally_stable": True,
        "cycle_v4_relations": True,
        "odd_primary_semisimple_character_decomposition_exact": True,
        "two_primary_fixed_space_computed_separately": True,
    },
    "multiquadratic_pullback_accounted": False,
    "physical_open_unramified_kernel_complete": False,
    "br0g_discharged": False,
    "unit_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
certificate["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "boundary-cycle-galois.json").write_text(
    json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "cycle_rank": 73,
    "cycle_character_multiplicities": mult,
    "odd_primary_q_invariant_cycle_rank": certificate["cycle_lattice"]["odd_primary_q_invariant_cycle_rank"],
    "f2_joint_fixed_dimension": joint_fixed_f2,
    "certificate_sha256": certificate["canonical_sha256"],
}, indent=2, sort_keys=True))
