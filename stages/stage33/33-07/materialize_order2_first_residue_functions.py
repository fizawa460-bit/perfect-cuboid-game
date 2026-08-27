#!/usr/bin/env python3
"""Certify raw first-residue liftability for the 26 quotient A[2] sources.

This reconstructs the historical U44/R17/O12 crossing basis from retained
compact data.  In particular, it does not depend on the expired raw Stage33-04
artifact: the recovered twelve order-four doubles must reproduce the retained
12x17 coordinates modulo U44 exactly.  Their omitted U44 coordinates only
change the chosen residue representative by known unit-symbol functions.

For a raw order-two source vector and a boundary component C ~= P1, the selected
crossings have even cardinality.  With homogeneous coordinate [u:v] on C and
crossing point p=[a:b], use

    f_C(u,v) = product_p (b*u-a*v) / v^d,  d=#selected crossings.

The denominator has even exponent and therefore does not change the Kummer
squareclass.  Some elements of A[2] have only order-four representatives in
the raw ramified residue module: doubling them is a nonzero known U44
unit-symbol class.  Those elements cannot be silently represented by Kummer
squareclasses.  This leaf records that exact quotient-to-raw obstruction.
"""
import hashlib
import json
from itertools import combinations
from pathlib import Path

import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp


HERE = Path(__file__).resolve().parent
OUT = HERE / "order2-first-residue-function-liftability.json"
EXPECTED = {
    "br0b-boundary-raw-residue-map.json": "44f03877c524a817e41036d89cf20ea971cc95c3d52adf53c2af6317a83d2324",
    "br0g-finite-ramified-residue-presentation.json": "4ff7731ec06df0fbd676c7c310e29c50ef1898690530d7f7497ce832a1e0d71d",
    "two-primary-residue-invariant-basis.json": "f18a54717b2327f7abc8ee87859b5c0537bffc062a1d5c1e36a5763c46faa939",
    "exceptional-p1-tangent-coordinates.json": "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636",
}
PARAMETERS = ["0", "infinity", "1", "-1", "i", "-i"]
SIDE_POINTS = {
    "0": [[0, 1, 0, 1], [1, 1, 0, 1]],
    "infinity": [[1, 1, 0, 1], [0, 1, 0, 1]],
    "1": [[1, 1, 0, 1], [1, 1, 0, 1]],
    "-1": [[-1, 1, 0, 1], [1, 1, 0, 1]],
    "i": [[0, 1, 1, 1], [1, 1, 0, 1]],
    "-i": [[0, 1, -1, 1], [1, 1, 0, 1]],
}


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(name):
    x = json.loads((HERE / name).read_text(encoding="utf-8"))
    body = dict(x)
    claimed = body.pop("canonical_sha256")
    actual = canonical_sha256(body)
    if claimed != EXPECTED[name] or actual != EXPECTED[name]:
        raise SystemExit(f"source lock moved for {name}: {claimed} {actual}")
    return x


def rref2(rows, ncols=None):
    a = [[int(x) & 1 for x in row] for row in rows]
    if ncols is None:
        ncols = len(a[0]) if a else 0
    pivots = []
    r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    return a, pivots


def rank2(rows, ncols=None):
    return len(rref2(rows, ncols)[1])


def nullspace2(rows, ncols):
    rr, pivots = rref2(rows, ncols)
    free = [j for j in range(ncols) if j not in pivots]
    out = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        for i, p in enumerate(pivots):
            v[p] = rr[i][f]
        out.append(v)
    return out


def rowmul2(v, matrix):
    return [
        sum((int(v[k]) & 1) * (int(matrix[k][j]) & 1) for k in range(len(v))) & 1
        for j in range(len(matrix[0]))
    ]


def inv2(matrix):
    n = len(matrix)
    a = [
        [int(x) & 1 for x in matrix[i]] + [int(i == j) for j in range(n)]
        for i in range(n)
    ]
    for c in range(n):
        p = next((i for i in range(c, n) if a[i][c]), None)
        if p is None:
            raise SystemExit("singular GF2 pivot minor")
        a[c], a[p] = a[p], a[c]
        for i in range(n):
            if i != c and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[c])]
    return [row[n:] for row in a]


def build_solver(basis):
    pivots = {}
    for i, row in enumerate(basis):
        x = sum((int(b) & 1) << j for j, b in enumerate(row))
        coord = 1 << i
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                bx, bc = pivots[p]
                x ^= bx
                coord ^= bc
            else:
                pivots[p] = (x, coord)
                break
        if not x:
            raise SystemExit("coordinate basis is dependent")

    def solve(row):
        x = sum((int(b) & 1) << j for j, b in enumerate(row))
        coord = 0
        while x:
            p = x.bit_length() - 1
            if p not in pivots:
                raise SystemExit("target escaped retained U44/R17 span")
            bx, bc = pivots[p]
            x ^= bx
            coord ^= bc
        return [(coord >> i) & 1 for i in range(len(basis))]

    return solve


def negate_element(x):
    return [-int(x[0]), int(x[1]), -int(x[2]), int(x[3])]


br0b = load_locked("br0b-boundary-raw-residue-map.json")
br0g = load_locked("br0g-finite-ramified-residue-presentation.json")
ib = load_locked("two-primary-residue-invariant-basis.json")
exc = load_locked("exceptional-p1-tangent-coordinates.json")

if exc["exceptional_count"] != 48 or exc["physical_crossing_tangent_count"] != 144:
    raise SystemExit("exceptional coordinate shape regression")

# Stable edge order from the historical boundary skeleton: side first, then
# exceptional.  Attach the two exact local P1 coordinates to every edge.
raw_edges = []
cc_exc = {}
for er in exc["exceptional_models"]:
    e = int(er["exceptional_id"][4:]) - 1
    cc_exc[e] = int(er["complex_conjugate_exceptional_id"][4:]) - 1
    for crossing in er["physical_crossing_tangent_coordinates"]:
        raw_edges.append({
            "side": int(crossing["side_index_1based"]) - 1,
            "exceptional": 24 + e,
            "parameter": crossing["side_parameter"],
            "side_point": SIDE_POINTS[crossing["side_parameter"]],
            "exceptional_point": crossing["exceptional_P1_homogeneous_coordinate_L_basis"],
        })
edges_data = sorted(raw_edges, key=lambda x: (x["side"], x["exceptional"]))
if len(edges_data) != 144 or len({(x["side"], x["exceptional"]) for x in edges_data}) != 144:
    raise SystemExit("crossing inventory is not 144 unique side/exceptional pairs")
edges = [(x["side"], x["exceptional"]) for x in edges_data]
edge_index = {edge: i for i, edge in enumerate(edges)}

cc_vertices = list(range(24)) + [24 + cc_exc[i] for i in range(48)]
if any(cc_vertices[cc_vertices[i]] != i for i in range(72)):
    raise SystemExit("boundary complex conjugation is not involutive")
cc_edges = [edge_index[(cc_vertices[a], cc_vertices[b])] for a, b in edges]
if any(cc_edges[cc_edges[i]] != i for i in range(144)):
    raise SystemExit("crossing complex conjugation is not involutive")

# Reconstruct the exact historical saturated cycle basis.
B = sp.zeros(72, 144)
for k, (a, b) in enumerate(edges):
    B[a, k] = -1
    B[b, k] = 1
D, S, T = smith_normal_decomp(B, domain=ZZ)
if D != S * B * T or B.rank() != 71:
    raise SystemExit("boundary incidence Smith decomposition regression")
Kmat = T[:, 71:].T
K = [[int(Kmat[i, j]) for j in range(144)] for i in range(73)]
if Kmat.shape != (73, 144) or Kmat * B.T != sp.zeros(73, 72):
    raise SystemExit("historical integral cycle basis reconstruction failed")

# Vertex and edge conjugation actions, then the 61-dimensional F2 fixed space.
Pcc = sp.zeros(144)
for j, image in enumerate(cc_edges):
    Pcc[j, image] = 1
pivot_cols = list(Kmat.rref()[1])
minor = Kmat[:, pivot_cols]
Ccc = Kmat * Pcc
Ccc = Ccc[:, pivot_cols] * minor.inv()
if any(sp.Rational(Ccc[i, j]).q != 1 for i in range(73) for j in range(73)):
    raise SystemExit("cycle conjugation escaped integral lattice")
Ccc = [[int(Ccc[i, j]) for j in range(73)] for i in range(73)]
fixed_coords = nullspace2(
    [[Ccc[i][j] ^ int(i == j) for i in range(73)] for j in range(73)],
    73,
)
if len(fixed_coords) != 61:
    raise SystemExit(f"fixed cycle dimension regression: {len(fixed_coords)}")

# Expand the retained 14x60 arithmetic-orbit unit valuation matrix back to
# the 14x72 geometric boundary matrix in the original orbit order.
orbits = []
seen = set()
for i in range(72):
    if i in seen:
        continue
    orbit = sorted({i, cc_vertices[i]})
    orbits.append(orbit)
    seen.update(orbit)
if len(orbits) != 60 or [len(x) for x in orbits].count(2) != 12:
    raise SystemExit("arithmetic boundary orbit reconstruction failed")
V60 = br0b["unit_to_arithmetic_boundary_valuation_matrix_14x60"]
if len(V60) != 14 or any(len(row) != 60 for row in V60):
    raise SystemExit("retained unit valuation shape regression")
Uvertex = [[0] * 72 for _ in range(14)]
for r in range(14):
    for oi, orbit in enumerate(orbits):
        for v in orbit:
            Uvertex[r][v] = int(V60[r][oi])

unit_candidates = []
for i, j in combinations(range(14), 2):
    vi, vj = Uvertex[i], Uvertex[j]
    unit_candidates.append([
        (vi[a] * vj[b] - vi[b] * vj[a]) & 1 for a, b in edges
    ])
U44 = []
rank_now = 0
for row in unit_candidates:
    new_rank = rank2(U44 + [row], 144)
    if new_rank > rank_now:
        U44.append(row)
        rank_now = new_rank
if len(U44) != 44:
    raise SystemExit("reconstructed unit-symbol rank is not 44")

# Match the historical cycle-coordinate algorithm and extend U44 to R17.
_, kpiv = rref2(K, 144)
Kminor = [[K[i][j] & 1 for j in kpiv] for i in range(73)]
Kminor_inv = inv2(Kminor)


def cycle_coords(row):
    coords = rowmul2([row[j] for j in kpiv], Kminor_inv)
    if rowmul2(coords, K) != [int(x) & 1 for x in row]:
        raise SystemExit("cycle coordinate reconstruction failed")
    return coords


unit_coords = [cycle_coords(row) for row in U44]
basis_coords = list(unit_coords)
Rcoords = []
rank_now = rank2(basis_coords, 73)
for row in fixed_coords:
    new_rank = rank2(basis_coords + [row], 73)
    if new_rank > rank_now:
        Rcoords.append(row)
        basis_coords.append(row)
        rank_now = new_rank
R17 = [rowmul2(row, K) for row in Rcoords]
if len(R17) != 17 or rank_now != 61:
    raise SystemExit("historical R17 complement reconstruction failed")

# Reconstruct the twelve Q(i)-component order-four generators, including their
# signed geometric mod-4 residues, and source-lock their retained doubles.
edge_orbits = []
seen = set()
for i in range(144):
    if i in seen:
        continue
    orbit = sorted({i, cc_edges[i]})
    edge_orbits.append(orbit)
    seen.update(orbit)
component_orbit_of = {v: i for i, orbit in enumerate(orbits) for v in orbit}
arith_edges = []
for orbit in edge_orbits:
    a, b = edges[orbit[0]]
    arith_edges.append((orbit, (component_orbit_of[a], component_orbit_of[b])))
qi_vertices = {i for i, orbit in enumerate(orbits) if len(orbit) == 2}
qi_edges = [i for i, (orbit, _) in enumerate(arith_edges) if len(orbit) == 2]
qi_incident = {
    v: [ei for ei in qi_edges if v in arith_edges[ei][1]] for v in sorted(qi_vertices)
}
if len(qi_incident) != 12 or any(len(x) != 2 for x in qi_incident.values()):
    raise SystemExit("Q(i) order-four incidence regression")

O4 = []
Odoubles = []
for v in sorted(qi_vertices):
    row = [0] * 144
    for arithmetic_edge, coefficient in zip(qi_incident[v], (1, 3)):
        orbit = arith_edges[arithmetic_edge][0]
        if len(orbit) != 2:
            raise SystemExit("order-four generator touched rational crossing")
        row[orbit[0]] = coefficient
        row[orbit[1]] = (-coefficient) % 4
    O4.append(row)
    Odoubles.append([(2 * x // 2) & 1 for x in row])

solve61 = build_solver(U44 + R17)
recovered_ocoords = [solve61(row) for row in Odoubles]
relation29 = br0g["diagnostic_quotient_by_U44_relation_matrix_29x29"]
if len(relation29) != 29 or any(len(row) != 29 for row in relation29):
    raise SystemExit("retained diagnostic relation matrix shape regression")
retained_o_r17 = []
for k, row in enumerate(relation29[17:]):
    if row[17 + k] != 2 or any(row[17 + j] for j in range(12) if j != k):
        raise SystemExit("retained O12 relation block regression")
    retained_o_r17.append([(-int(x)) & 1 for x in row[:17]])
if [row[44:] for row in recovered_ocoords] != retained_o_r17:
    raise SystemExit("reconstructed O12 doubles moved in the retained R17 quotient")

# Convert the explicit Smith A[2] basis back to order-two crossing vectors.
source_records = []
source_edge_vectors = []
double_obstructions = []
for index, generator in enumerate(ib["invariant_factor_generators"], 1):
    multiplier = 1 if int(generator["order"]) == 2 else 2
    original = [
        multiplier * int(x) for x in generator["original_R17_O12_coordinates"]
    ]
    mod4 = [0] * 144
    for coefficient, row in zip(original[:17], R17):
        for e, bit in enumerate(row):
            mod4[e] = (mod4[e] + 2 * coefficient * bit) % 4
    for coefficient, row in zip(original[17:], O4):
        for e, value in enumerate(row):
            mod4[e] = (mod4[e] + coefficient * value) % 4
    double_vector = [0] * 144
    for coefficient, row in zip(original[17:], Odoubles):
        if coefficient & 1:
            double_vector = [x ^ y for x, y in zip(double_vector, row)]
    double_coordinates = solve61(double_vector)
    if any(double_coordinates[44:]):
        raise SystemExit(f"A2_{index:02d} double escaped the retained U44 span")
    obstruction = double_coordinates[:44]
    double_obstructions.append(obstruction)
    raw_order2 = not any(obstruction)
    if raw_order2 != all(x in (0, 2) for x in mod4):
        raise SystemExit(f"A2_{index:02d} raw-order test disagrees with U44 obstruction")
    if not raw_order2:
        obstruction_bits = sum(bit << j for j, bit in enumerate(obstruction))
        source_records.append({
            "source_basis_name": f"A2_{index:02d}",
            "from_invariant_factor": generator["name"],
            "parent_order": int(generator["order"]),
            "parent_multiplier": multiplier,
            "raw_order2_first_residue_function_liftable": False,
            "raw_representative_has_order4_crossing_entries": True,
            "double_obstruction_U44_f2_hex_le": f"{obstruction_bits:011x}",
            "quotient_order2_reason": "doubling is a nonzero known U44 unit-symbol residue",
        })
        continue
    vector = [x // 2 for x in mod4]
    degrees = [0] * 72
    for bit, (a, b) in zip(vector, edges):
        if bit:
            degrees[a] += 1
            degrees[b] += 1
    if any(d & 1 for d in degrees):
        raise SystemExit(f"A2_{index:02d} violates componentwise even parity")
    if [vector[cc_edges[e]] for e in range(144)] != vector:
        raise SystemExit(f"A2_{index:02d} lost complex-conjugation invariance")

    component_functions = []
    full_function_models = []
    for component in range(72):
        selected = [
            e for e, (a, b) in enumerate(edges)
            if vector[e] and component in (a, b)
        ]
        if not selected:
            continue
        factors = []
        for e in selected:
            point = (
                edges_data[e]["side_point"]
                if component < 24
                else edges_data[e]["exceptional_point"]
            )
            a, b = point
            factors.append({
                "edge_id": f"X_{e + 1:04d}",
                "point_P1_L_basis": point,
                "linear_factor_bu_minus_av_L_basis": [b, negate_element(a)],
            })
        full = {
            "component_id": (
                f"SIDE_{component + 1:03d}"
                if component < 24
                else f"EXC_{component - 23:03d}"
            ),
            "selected_crossing_factors": factors,
            "denominator": "v^d",
            "denominator_exponent_d": len(selected),
        }
        full_function_models.append(full)
        component_functions.append({
            "component_id": full["component_id"],
            "selected_edge_ids": [x["edge_id"] for x in factors],
            "even_degree": len(selected),
            "function_model_sha256": canonical_sha256(full),
        })

    bitset = sum(bit << e for e, bit in enumerate(vector))
    source_records.append({
        "source_basis_name": f"A2_{index:02d}",
        "from_invariant_factor": generator["name"],
        "parent_order": int(generator["order"]),
        "parent_multiplier": multiplier,
        "raw_order2_first_residue_function_liftable": True,
        "raw_representative_has_order4_crossing_entries": False,
        "double_obstruction_U44_f2_hex_le": "00000000000",
        "crossing_vector_f2_144_hex_le": f"{bitset:036x}",
        "selected_crossing_count": sum(vector),
        "nontrivial_component_function_count": len(component_functions),
        "component_first_residue_functions": component_functions,
        "full_72_component_function_model_sha256": canonical_sha256({
            "source_basis_name": f"A2_{index:02d}",
            "models": full_function_models,
            "trivial_components_have_function": "1",
        }),
    })
    source_edge_vectors.append(vector)

if len(source_records) != 26:
    raise SystemExit("order-two source basis dimension regression")
obstruction_rank = rank2(double_obstructions, 44)
raw_liftable_count = sum(not any(row) for row in double_obstructions)
if obstruction_rank != 9 or raw_liftable_count != 17:
    raise SystemExit(
        f"quotient-to-raw obstruction regression rank={obstruction_rank} "
        f"raw_liftable={raw_liftable_count}"
    )
if rank2(U44 + source_edge_vectors, 144) - rank2(U44, 144) != 17:
    raise SystemExit("the 17 raw-order2 source vectors are not independent modulo U44")

cert = {
    "schema": "STAGE33_07_ORDER2_FIRST_RESIDUE_FUNCTION_LIFTABILITY_V1",
    "source_locks": {
        name.replace(".json", "_sha256"): value for name, value in EXPECTED.items()
    },
    "boundary_model": {
        "component_count": 72,
        "side_P1_count": 24,
        "exceptional_P1_count": 48,
        "crossing_count": 144,
        "crossing_order": "side index, then exceptional index",
        "coordinate_fields": "Q on sides; Q(i) on exceptional tangent models",
    },
    "historical_basis_reconstruction": {
        "unit_symbol_rank_f2": 44,
        "qfixed_complement_rank_f2": 17,
        "order4_generator_count": 12,
        "retained_order4_double_quotient_coordinate_matrix_shape": [12, 17],
        "retained_12x17_mod_U44_matrix_reproduced_exactly": True,
        "omitted_U44_coordinates_scope": "choice of representative by known unit-symbol functions",
    },
    "function_convention": {
        "crossing_point": "p=[a:b]",
        "homogeneous_boundary_coordinate": "[u:v]",
        "linear_factor": "b*u-a*v",
        "component_function": "product selected linear factors / v^d",
        "denominator_exponent_d_is_even": True,
        "zero_selected_crossings_function": "1",
    },
    "source_order2_dimension_f2": 26,
    "raw_order2_first_residue_function_liftable_basis_count": 17,
    "quotient_only_order2_basis_count": 9,
    "quotient_to_raw_double_obstruction_rank_f2": 9,
    "source_basis": source_records,
    "exact_checks": {
        "all_144_crossings_reconstructed_once": True,
        "historical_U44_R17_O12_basis_reconstructed_from_compact_sources": True,
        "retained_order4_double_12x17_mod_U44_coordinates_reproduced_exactly": True,
        "exactly_17_sources_have_raw_order_two_crossing_residues": True,
        "the_other_9_sources_double_to_nonzero_U44_unit_symbol_residues": True,
        "quotient_to_raw_double_obstruction_has_rank_9": True,
        "all_17_raw_order2_sources_even_on_every_boundary_component": True,
        "all_17_raw_order2_sources_complex_conjugation_invariant_as_crossing_divisors": True,
        "all_17_raw_order2_sources_independent_modulo_U44": True,
        "all_17_raw_order2_component_functions_deterministically_materialized": True,
    },
    "constructive_progress": {
        "physical_side_P1_coordinates_materialized": True,
        "exceptional_P1_tangent_coordinates_materialized": True,
        "raw_order2_first_residue_functions_materialized": 17,
        "all_26_order2_quotient_source_first_residue_functions_materialized": False,
        "nine_quotient_only_order2_double_obstructions_materialized": True,
        "chosen_global_geometric_lifts_materialized": False,
        "project_14x26_L_squareclass_tensor_materialized": False,
        "absolute_delta_loc_computed": False,
    },
    "new_smallest_exact_kernel": "R33-BR2A-9-QUOTIENT-ORDER2-RAW-ORDER4-EXTENSION-BOCKSTEIN",
    "next_exact_leaf": "L33-07-RESOLVE-9-U44-DOUBLE-OBSTRUCTIONS-BEFORE-ANY-14x26-SQUARECLASS-TENSOR",
    "arithmetic_hs_closed": False,
    "actual_index512_glue_identified": False,
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
cert["canonical_sha256"] = canonical_sha256(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "quotient_source_dimension_f2": 26,
    "raw_order2_function_liftable_count": 17,
    "quotient_only_order2_count": 9,
    "double_obstruction_rank_f2": 9,
    "boundary_P1_count": 72,
    "crossing_count": 144,
    "retained_12x17_mod_U44_lock_reproduced": True,
    "all_26_first_residue_functions_materialized": False,
    "certificate_sha256": cert["canonical_sha256"],
    "next_exact_leaf": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
