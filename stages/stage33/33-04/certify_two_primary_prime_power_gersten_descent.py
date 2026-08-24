#!/usr/bin/env python3
"""Exact full two-primary prime-power Gersten/character descent for Stage33-04.

The hostile re-audit accepted the odd-primary arithmetic descent but rejected
all-primary BR0G closure because the existing arithmetic two-primary proof was
only exponent two. This leaf computes the complete 2-primary residue-character
kernel supported on the arithmetic boundary crossing orbits.

For each arithmetic boundary normalization P^1_K, the curve localization
sequence gives
  0 -> H^1(K,Q_2/Z_2)
    -> H^1(K(t),Q_2/Z_2)_{ramified only at marked crossings}
    -> direct_sum_x H^0(k(x),Q_2/Z_2(-1))
    -> H^0(K,Q_2/Z_2(-1)).
The last map is the sum of corestrictions. Surface Gersten compatibility
identifies the two residues at each crossing with opposite signs.

Here K and k(x) are only Q or Q(i). Hence the crossing coefficient groups are
Z/2 at Q-points and Z/4 at Q(i)-points. Corestriction Q(i)->Q is zero on the
2-primary Tate-twist invariants because transfer is 1+cc and cc acts by -1 on
Z/4(-1) (and 2=0 on Z/2). Therefore all ramified higher-2-power structure is
finite and bounded by order 4; arbitrary higher 2-power orders occur only in
the constant-field character factors.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

sk = json.loads((ROOT / "boundary-residue-skeleton.json").read_text())
bg = json.loads((ROOT / "boundary-galois.json").read_text())
geo = json.loads((ROOT / "all-primary-geometric-cycle-invariants.json").read_text())
odd = json.loads((ROOT / "odd-primary-arithmetic-character-descent.json").read_text())
unit = json.loads((ROOT / "unit-symbol-residue-span.json").read_text())
q17 = json.loads((ROOT / "qfixed17-graph-residual.json").read_text())
audit = json.loads((ROOT / "audit-state.json").read_text())

EXPECTED_VERDICT = "PASS_ODD_PRIMARY_RESIDUAL_REJECT_ALL_PRIMARY_CLOSURE_ON_HIGHER_TWO_POWER_GERSTEN_DESCENT"
EXPECTED_KERNEL = "R33-BR0G-TWO-PRIMARY-PRIME-POWER-GERSTEN-CHARACTER-DESCENT"
if audit["audit_verdict"] != EXPECTED_VERDICT:
    raise SystemExit("hostile re-audit verdict regression")
if audit["unit_status"] != "BLOCKED_NEW_KERNEL" or audit["unit_closed"]:
    raise SystemExit("expected blocked hostile re-audit checkpoint")
if audit["new_kernel_id"] != EXPECTED_KERNEL or audit["unresolved_unknown_in_scope"] != 1:
    raise SystemExit("higher-two-power residual kernel regression")
if not audit["arithmetic_odd_character_descent_complete"]:
    raise SystemExit("odd-primary predecessor no longer closed")
if not odd["arithmetic_odd_character_descent_complete"]:
    raise SystemExit("odd-primary certificate regression")
if geo["two_primary_geometric_fixed_module"] != "(Q_2/Z_2)^61":
    raise SystemExit("geometric two-primary fixed module regression")
if sk["component_count"] != 72 or sk["codim2_crossing_count"] != 144:
    raise SystemExit("boundary inventory regression")

def gf2_bits(row):
    x = 0
    for i, b in enumerate(row):
        if int(b) & 1:
            x |= 1 << i
    return x

def gf2_rank(rows):
    piv = {}
    for row in rows:
        x = gf2_bits(row) if not isinstance(row, int) else row
        while x:
            p = x.bit_length() - 1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p] = x
                break
    return len(piv)

def gf2_coordinates(basis_rows, target):
    """Coordinates in an independent GF(2) row basis."""
    piv = {}
    for i, row in enumerate(basis_rows):
        x = gf2_bits(row)
        c = 1 << i
        while x:
            p = x.bit_length() - 1
            if p in piv:
                bx, bc = piv[p]
                x ^= bx
                c ^= bc
            else:
                piv[p] = (x, c)
                break
        if not x:
            raise SystemExit("coordinate basis is dependent")
    x = gf2_bits(target)
    c = 0
    while x:
        p = x.bit_length() - 1
        if p not in piv:
            raise SystemExit("target escaped certified Q-fixed basis")
        bx, bc = piv[p]
        x ^= bx
        c ^= bc
    return [(c >> i) & 1 for i in range(len(basis_rows))]

cc = [int(x) - 1 for x in bg["boundary_perm_cc_1based"]]
ct = [int(x) - 1 for x in bg["boundary_perm_ct_1based"]]
if ct != list(range(72)) or any(cc[cc[j]] != j for j in range(72)):
    raise SystemExit("boundary Galois action regression")

edges = []
edge_index = {}
for idx, e in enumerate(sk["codim2_crossings"]):
    a = int(e["side_vertex"]) - 1
    b = int(e["exceptional_vertex"]) - 1
    edges.append((a, b))
    edge_index[tuple(sorted((a, b)))] = idx
if len(edge_index) != 144:
    raise SystemExit("crossing uniqueness regression")

def induced_edge_perm(p):
    out = []
    for a, b in edges:
        key = tuple(sorted((p[a], p[b])))
        if key not in edge_index:
            raise SystemExit("Galois action escaped crossing graph")
        out.append(edge_index[key])
    return out

ecc = induced_edge_perm(cc)
if any(ecc[ecc[j]] != j for j in range(144)):
    raise SystemExit("crossing conjugation is not involutive")

component_orbits = []
seen = set()
for j in range(72):
    if j in seen:
        continue
    orb = sorted({j, cc[j]})
    component_orbits.append(orb)
    seen.update(orb)
component_orbit_of = {j: i for i, orb in enumerate(component_orbits) for j in orb}
q_vertices = [i for i, orb in enumerate(component_orbits) if len(orb) == 1]
qi_vertices = [i for i, orb in enumerate(component_orbits) if len(orb) == 2]
if (len(component_orbits), len(q_vertices), len(qi_vertices)) != (60, 48, 12):
    raise SystemExit("arithmetic component orbit regression")

edge_orbits = []
seen = set()
for j in range(144):
    if j in seen:
        continue
    orb = sorted({j, ecc[j]})
    edge_orbits.append(orb)
    seen.update(orb)
if len(edge_orbits) != 120:
    raise SystemExit("arithmetic crossing orbit count regression")

arith_edges = []
for i, orb in enumerate(edge_orbits):
    a, b = edges[orb[0]]
    va, vb = component_orbit_of[a], component_orbit_of[b]
    if va == vb:
        raise SystemExit("unexpected quotient-graph loop")
    field = "Q" if len(orb) == 1 else "Q(i)"
    arith_edges.append({
        "index": i,
        "geometric_edges_0based": orb,
        "vertices": (va, vb),
        "field": field,
    })

q_edges = [e for e in arith_edges if e["field"] == "Q"]
qi_edges = [e for e in arith_edges if e["field"] == "Q(i)"]
if (len(q_edges), len(qi_edges)) != (96, 24):
    raise SystemExit("arithmetic crossing field regression")
for e in q_edges:
    if any(v not in q_vertices for v in e["vertices"]):
        raise SystemExit("Q crossing touches non-Q arithmetic component")
for e in qi_edges:
    types = sorted(1 if v in qi_vertices else 0 for v in e["vertices"])
    if types != [0, 1]:
        raise SystemExit("Q(i) crossing is not Q--Q(i)")

q_adj = {v: [] for v in q_vertices}
q_incidence_rows = []
for v in q_vertices:
    row = [0] * len(q_edges)
    for j, e in enumerate(q_edges):
        if v in e["vertices"]:
            row[j] = 1
            q_adj[v].append(e["index"])
    q_incidence_rows.append(row)

todo = [q_vertices[0]]
seen_q = {q_vertices[0]}
while todo:
    v = todo.pop()
    for ei in q_adj[v]:
        e = arith_edges[ei]
        w = e["vertices"][0] if e["vertices"][1] == v else e["vertices"][1]
        if w not in seen_q:
            seen_q.add(w)
            todo.append(w)
if len(seen_q) != len(q_vertices):
    raise SystemExit("Q-crossing subgraph is not connected")
q_incidence_rank = gf2_rank(q_incidence_rows)
if q_incidence_rank != 47:
    raise SystemExit(f"Q-edge incidence rank regression: {q_incidence_rank}")
q_ramified_z2_rank = len(q_edges) - q_incidence_rank
if q_ramified_z2_rank != 49:
    raise SystemExit("Q-edge ramified kernel rank regression")

qi_incident = {}
for v in qi_vertices:
    inc = [e for e in qi_edges if v in e["vertices"]]
    if len(inc) != 2:
        raise SystemExit(f"Q(i) component degree regression at orbit {v}: {len(inc)}")
    qi_incident[v] = [e["index"] for e in inc]
if len({ei for xs in qi_incident.values() for ei in xs}) != 24:
    raise SystemExit("Q(i) crossing partition regression")
qi_ramified_z4_rank = len(qi_vertices)
if qi_ramified_z4_rank != 12:
    raise SystemExit("Q(i) order-4 ramified rank regression")

order4_double_vectors = []
order4_generators = []
for v in qi_vertices:
    e1, e2 = qi_incident[v]
    vec = [0] * 144
    for ae in (e1, e2):
        for ge in edge_orbits[ae]:
            vec[ge] = 1
    degree = [0] * 72
    for bit, (a, b) in zip(vec, edges):
        if bit:
            degree[a] += 1
            degree[b] += 1
    if any(d % 2 for d in degree):
        raise SystemExit("order-4 double is not an exponent-two graph cycle")
    if any(vec[ecc[j]] != vec[j] for j in range(144)):
        raise SystemExit("order-4 double is not Galois fixed")
    order4_double_vectors.append(vec)
    order4_generators.append({
        "qi_component_orbit_index_0based": v,
        "arithmetic_crossing_orbits_0based": [e1, e2],
        "coefficients_mod4": [1, 3],
        "double_support_geometric_edges_1based": [j + 1 for j, b in enumerate(vec) if b],
    })

U = [[int(x) & 1 for x in row] for row in unit["independent_secondary_residue_patterns"]]
R = [[int(x) & 1 for x in row] for row in q17["qfixed_residual_basis_edge_vectors_144"]]
if len(U) != 44 or len(R) != 17:
    raise SystemExit("accepted F2 decomposition regression")
if gf2_rank(U) != 44 or gf2_rank(R) != 17 or gf2_rank(U + R) != 61:
    raise SystemExit("accepted 61=44+17 basis regression")
if gf2_rank(order4_double_vectors) != 12:
    raise SystemExit("order-4 double subspace rank regression")
if gf2_rank(U + R + order4_double_vectors) != 61:
    raise SystemExit("order-4 doubles escaped accepted Q-fixed F2 module")
rank_u_plus_q4 = gf2_rank(U + order4_double_vectors)
q4_intersection_unit = 44 + 12 - rank_u_plus_q4
q4_image_mod_unit = rank_u_plus_q4 - 44
if (q4_intersection_unit, q4_image_mod_unit) != (9, 3):
    raise SystemExit("order-4/unit-symbol intersection regression")

basis61 = U + R
quotient_coords = []
for vec in order4_double_vectors:
    coords = gf2_coordinates(basis61, vec)
    quotient_coords.append(coords[44:])
if gf2_rank(quotient_coords) != 3:
    raise SystemExit("order-4 lift image in old 17D quotient is not rank 3")

pivot_rows = []
current = []
rank_now = 0
for i, row in enumerate(quotient_coords):
    nr = gf2_rank(current + [row])
    if nr > rank_now:
        pivot_rows.append(i)
        current.append(row)
        rank_now = nr
if rank_now != 3:
    raise SystemExit("failed to select three independent order-4 quotient images")

ramified_2torsion_dim = q_ramified_z2_rank + qi_ramified_z4_rank
if ramified_2torsion_dim != 61:
    raise SystemExit("full prime-power ramification does not reduce to F2 dimension 61")

diagnostic_z4_rank = 12 - q4_intersection_unit
diagnostic_log2_order = 49 + 2 * 12 - 44
diagnostic_z2_rank = diagnostic_log2_order - 2 * diagnostic_z4_rank
if (diagnostic_z2_rank, diagnostic_z4_rank) != (23, 3):
    raise SystemExit("finite quotient invariant-factor diagnostic regression")

two_primary_constant_module = (
    "Hom_cont(G_Q,Q_2/Z_2)^48 direct_sum "
    "Hom_cont(G_Q(i),Q_2/Z_2)^12"
)
two_primary_ramified_module = "(Z/2)^49 direct_sum (Z/4)^12"
all_primary_odd_module = odd["odd_primary_boundary_character_module"]

cert = {
    "schema": "STAGE33_04_TWO_PRIMARY_PRIME_POWER_GERSTEN_DESCENT_V1",
    "audited_residual_kernel": EXPECTED_KERNEL,
    "audited_exact_prefix_preserved": True,
    "source_locks": {
        "audit_state_sha256": hashlib.sha256((ROOT / "audit-state.json").read_bytes()).hexdigest(),
        "boundary_skeleton_sha256": sk["canonical_sha256"],
        "boundary_galois_sha256": bg["canonical_sha256"],
        "all_primary_geometric_cycle_sha256": geo["canonical_sha256"],
        "odd_primary_character_descent_sha256": odd["canonical_sha256"],
        "unit_symbol_residue_span_sha256": unit["canonical_sha256"],
        "qfixed17_graph_residual_sha256": q17["canonical_sha256"],
        "stage29_boundary_gersten_receiver": "stages/stage29/29-02f/boundary-gersten-receiver.md",
        "curve_residue_law": "localization/Faddeev exact sequence for H^1(K(P1),Q_2/Z_2) with residues in H^0(k(x),Q_2/Z_2(-1)) and sum of corestrictions",
    },
    "arithmetic_component_orbits_total": 60,
    "q_component_orbits": 48,
    "qi_component_orbits": 12,
    "arithmetic_crossing_orbits_total": 120,
    "q_crossing_orbits": 96,
    "qi_crossing_orbits": 24,
    "q_crossing_tate_twist_group": "Z/2",
    "qi_crossing_tate_twist_group": "Z/4",
    "qi_to_q_tate_twist_corestriction_zero": True,
    "qi_to_q_corestriction_reason": "transfer=1+cc; cc=-1 on Z/4(-1), and multiplication by 2 is zero on Z/2",
    "q_edge_subgraph_vertex_count": 48,
    "q_edge_subgraph_edge_count": 96,
    "q_edge_subgraph_connected_components": 1,
    "q_edge_incidence_rank_f2": q_incidence_rank,
    "q_edge_ramified_kernel_rank_f2": q_ramified_z2_rank,
    "qi_vertex_degree_in_qi_edges": 2,
    "qi_order4_ramified_generator_rank": qi_ramified_z4_rank,
    "two_primary_constant_character_module": two_primary_constant_module,
    "two_primary_ramified_crossing_module": two_primary_ramified_module,
    "two_primary_boundary_character_kernel_exact_sequence": (
        "0 -> " + two_primary_constant_module +
        " -> BR0G_boundary[2^infinity] -> " + two_primary_ramified_module + " -> 0"
    ),
    "ramified_exponent_at_most": 4,
    "order8_or_higher_ramified_crossing_classes": 0,
    "higher_two_power_orders_only_in_constant_character_factors": True,
    "ramified_two_torsion_dimension_f2": ramified_2torsion_dim,
    "matches_audited_exponent_two_dimension_61": True,
    "order4_generator_count": 12,
    "order4_generators": order4_generators,
    "order4_double_subspace_rank_f2": 12,
    "order4_double_intersection_unit_symbol_span_rank_f2": q4_intersection_unit,
    "order4_double_image_mod_unit_symbol_span_rank_f2": q4_image_mod_unit,
    "order4_double_coordinates_in_old_qfixed17_quotient": quotient_coords,
    "independent_order4_images_in_old_qfixed17_indices_1based": [i + 1 for i in pivot_rows],
    "diagnostic_only_finite_ramified_quotient_by_known_exponent_two_unit_symbol_image": {
        "group": "(Z/2)^23 direct_sum (Z/4)^3",
        "z2_rank": diagnostic_z2_rank,
        "z4_rank": diagnostic_z4_rank,
        "firewall": "not a Stage33-04 closure quotient; duplicate/class integration belongs to Stage33-07",
    },
    "proper_brauer_boundary_residue_image_zero": True,
    "proper_residue_quotient_changes_boundary_kernel": False,
    "full_two_primary_prime_power_gersten_character_descent_complete": True,
    "arithmetic_odd_character_descent_complete": True,
    "all_primary_boundary_residue_kernel_exact_candidate": True,
    "all_primary_odd_boundary_character_module": all_primary_odd_module,
    "unramified_physical_open_kernel_exact_candidate": True,
    "br0g_discharged_candidate_pending_hostile_audit": True,
    "unresolved_unknown_in_scope_candidate": 0,
    "new_kernel_id_candidate": None,
    "unit_status_candidate": "AUDIT_REQUIRED",
    "unit_closed": False,
    "downstream_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
    "next_expected_command_if_ci_green": "Stage33-audit",
    "firewall": "exact BR0G boundary-residue kernel is not yet the downstream complete Q-defined Brauer-class list and is not a Brauer-Manin obstruction",
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "two-primary-prime-power-gersten-descent.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n"
)
print(json.dumps({
    "success": True,
    "two_primary_ramified_crossing_module": two_primary_ramified_module,
    "two_primary_constant_character_module": two_primary_constant_module,
    "ramified_two_torsion_dimension_f2": ramified_2torsion_dim,
    "order4_generator_count": 12,
    "order4_double_intersection_unit_span_rank_f2": q4_intersection_unit,
    "order4_double_image_mod_unit_span_rank_f2": q4_image_mod_unit,
    "diagnostic_finite_quotient_by_unit_image": "(Z/2)^23 direct_sum (Z/4)^3",
    "full_two_primary_prime_power_gersten_character_descent_complete": True,
    "next": "Stage33-audit",
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
