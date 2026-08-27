#!/usr/bin/env python3
"""Certify P1 tangent-cone coordinates on all 48 exceptional curves.

The retained side-coordinate artifact identifies every physical side/node
incidence. All corresponding node and first-order tangent coordinates lie in
Q(i), so this leaf reconstructs them with exact local Gaussian-rational linear
algebra; no numerical solver or remote CAS is used.

At every ordinary double point it verifies Jacobian rank three, forms the
three-dimensional projective tangent quotient, extracts the unique quadratic
relation with zero linear term, and checks that it is a nonsingular conic.
Each incident side parametrization is differentiated exactly and placed on
that conic. A deterministic projection-from-a-point then supplies a P1
coordinate for the exceptional curve.

This remains a coordinate certificate. It does not construct a global
Gersten lift, an L-squareclass tensor, delta_loc, or Hochschild--Serre d2.
"""
import hashlib
import json
import os
from collections import Counter, defaultdict
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
OUT = HERE / "exceptional-p1-tangent-coordinates.json"
SIDE_EXPECTED = "ae58f55d54fd00ba3b79b7bb51a6e668450643a11e60fd67f4f89475e4b6ad04"
I = sp.I
PARAMETERS = ["0", "infinity", "1", "-1", "i", "-i"]
UVS = [(0, 1), (1, 0), (1, 1), (-1, 1), (I, 1), (-I, 1)]


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def clean(x):
    return sp.cancel(sp.expand(x))


def is_zero(x):
    return clean(x) == 0


def projective_normalize(v):
    values = [clean(x) for x in list(v)]
    pivot = next((x for x in values if not is_zero(x)), None)
    if pivot is None:
        raise SystemExit("zero projective vector")
    return tuple(clean(x / pivot) for x in values)


def independent_columns(columns):
    out = []
    rank = 0
    for column in columns:
        candidate = sp.Matrix.hstack(*(out + [sp.Matrix(column)]))
        new_rank = candidate.rank()
        if new_rank > rank:
            out.append(sp.Matrix(column))
            rank = new_rank
    return out


def perpendicular_candidates(v):
    x, y, z = list(v)
    return [
        sp.Matrix([y, -x, 0]),
        sp.Matrix([z, 0, -x]),
        sp.Matrix([0, z, -y]),
    ]


def rational_pair(q):
    q = clean(q)
    if q.is_Rational is not True:
        raise SystemExit(f"expected rational coefficient, got {q}")
    return [int(sp.numer(q)), int(sp.denom(q))]


def encode_element(x):
    x = clean(x)
    xc = clean(sp.conjugate(x))
    a = clean((x + xc) / 2)
    b = clean((x - xc) / (2 * I))
    if clean(x - a - b * I) != 0:
        raise SystemExit(f"element escaped Q(i): {x}")
    ar, br = rational_pair(a), rational_pair(b)
    return [ar[0], ar[1], br[0], br[1]]


def encode_vector(v):
    return [encode_element(x) for x in list(v)]


def encode_matrix(m):
    return [[encode_element(m[r, c]) for c in range(m.cols)] for r in range(m.rows)]


def side_metadata(side_index):
    j = side_index - 1
    family = j // 8
    r = j % 8
    e1 = [1, -1][r // 4]
    e2 = [1, -1][(r // 2) % 2]
    e3 = [1, -1][r % 2]
    return family, e1, e2, e3


def side_param_and_tangent(side_index, parameter_index):
    family, e1, e2, e3 = side_metadata(side_index)
    u, v = UVS[parameter_index - 1]
    X, Y, Z = u * u - v * v, 2 * u * v, u * u + v * v
    # Choose a projectively transverse parameter variation.  The tempting
    # (-v,u) becomes radial at u/v=+/-i, so use an affine-chart basis instead.
    du, dv = (1, 0) if v != 0 else (0, 1)
    dX = 2 * u * du - 2 * v * dv
    dY = 2 * (du * v + u * dv)
    dZ = 2 * u * du + 2 * v * dv
    if family == 0:
        q = [0, -e1 * X, -e2 * Y, -e3 * Z, Y, X, Z]
        d = [0, -e1 * dX, -e2 * dY, -e3 * dZ, dY, dX, dZ]
    elif family == 1:
        q = [-e2 * Y, 0, -e1 * X, X, -e3 * Z, Y, Z]
        d = [-e2 * dY, 0, -e1 * dX, dX, -e3 * dZ, dY, dZ]
    else:
        q = [-e1 * X, -e2 * Y, 0, Y, X, -e3 * Z, Z]
        d = [-e1 * dX, -e2 * dY, 0, dY, dX, -e3 * dZ, dZ]
    return sp.Matrix([clean(x) for x in q]), sp.Matrix([clean(x) for x in d])


def quadrics(v):
    a1, a2, a3, b1, b2, b3, c = list(v)
    return sp.Matrix([
        a1 * a1 + a2 * a2 - b3 * b3,
        a2 * a2 + a3 * a3 - b1 * b1,
        a1 * a1 + a3 * a3 - b2 * b2,
        a1 * a1 + a2 * a2 + a3 * a3 - c * c,
    ])


def jacobian(v):
    a1, a2, a3, b1, b2, b3, c = list(v)
    return sp.Matrix([
        [2 * a1, 2 * a2, 0, 0, 0, -2 * b3, 0],
        [0, 2 * a2, 2 * a3, -2 * b1, 0, 0, 0],
        [2 * a1, 0, 2 * a3, 0, -2 * b2, 0, 0],
        [2 * a1, 2 * a2, 2 * a3, 0, 0, 0, -2 * c],
    ])


side_path = Path(os.environ.get(
    "STAGE33_SIDE_COORDINATE_CERTIFICATE",
    HERE / "boundary-side-p1-crossing-coordinates.json",
))
if not side_path.exists():
    raise SystemExit(
        "missing retained side-coordinate certificate; set "
        "STAGE33_SIDE_COORDINATE_CERTIFICATE"
    )
side = json.loads(side_path.read_text(encoding="utf-8"))
side_claimed = side["canonical_sha256"]
side_body = dict(side)
side_body.pop("canonical_sha256")
if side_claimed != SIDE_EXPECTED or canonical_sha256(side_body) != SIDE_EXPECTED:
    raise SystemExit("retained side-coordinate source lock moved")
if side["parameter_support"] != PARAMETERS or side["side_exceptional_crossing_count"] != 144:
    raise SystemExit("retained side-coordinate shape regression")

expected_incidence = {}
pair_to_exceptional = {}
for record in side["exceptional_incidence"]:
    point = int(record["exceptional_id"][4:])
    pairs = sorted(
        (int(x["side_index_1based"]), PARAMETERS.index(x["parameter"]) + 1)
        for x in record["incident_side_parameter_pairs"]
    )
    expected_incidence[point] = pairs
    for pair in pairs:
        if pair in pair_to_exceptional:
            raise SystemExit(f"duplicate retained incidence pair {pair}")
        pair_to_exceptional[pair] = point
if len(pair_to_exceptional) != 144:
    raise SystemExit("retained side incidence did not contain 144 unique pairs")

# Reconstruct and cross-check every pinned node solely from its incident side
# parametrizations. The retained artifact supplies the upstream exceptional
# numbering; the equations below independently certify the actual point.
node_vectors = {}
incident_tangents = defaultdict(list)
for point in range(1, 49):
    normalized = []
    for side_index, z in expected_incidence[point]:
        q, d = side_param_and_tangent(side_index, z)
        if any(not is_zero(x) for x in quadrics(q)):
            raise SystemExit(f"side parameter escaped surface at {(side_index, z)}")
        normalized.append(projective_normalize(q))
        incident_tangents[point].append((side_index, z, d))
    if any(x != normalized[0] for x in normalized[1:]):
        raise SystemExit(f"incident sides disagree on exceptional node {point}")
    node_vectors[point] = sp.Matrix(normalized[0])
if len({projective_normalize(v) for v in node_vectors.values()}) != 48:
    raise SystemExit("reconstructed exceptional nodes are not 48 distinct points")

# Verify retained complex conjugation directly. sqrt(2) fixes Q(i).
point_by_normalized = {projective_normalize(v): p for p, v in node_vectors.items()}
for point, p in node_vectors.items():
    image = point_by_normalized[projective_normalize(p.applyfunc(sp.conjugate))]
    claimed = int(side["exceptional_incidence"][point - 1][
        "complex_conjugate_exceptional_id"
    ][4:])
    if image != claimed:
        raise SystemExit(f"complex conjugation mismatch at exceptional {point}")

records = []
degree_histogram = Counter()
for point in range(1, 49):
    p = node_vectors[point]
    J = jacobian(p)
    if J.rank() != 3:
        raise SystemExit(f"node Jacobian rank regression at {point}")
    W = J.nullspace()
    if len(W) != 4:
        raise SystemExit(f"affine tangent dimension regression at {point}")
    Bcols = independent_columns([p] + W)
    if len(Bcols) != 4 or Bcols[0] != p:
        raise SystemExit(f"radial-first tangent basis regression at {point}")
    B = sp.Matrix.hstack(*Bcols)

    alpha_space = J.T.nullspace()
    if len(alpha_space) != 1:
        raise SystemExit(f"node quadratic relation not unique at {point}")
    alpha = alpha_space[0]

    def qeval(v):
        return clean((alpha.T * quadrics(v))[0])

    U = B[:, 1:4]
    G = sp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            G[r, c] = clean(
                (qeval(U[:, r] + U[:, c]) - qeval(U[:, r]) - qeval(U[:, c])) / 2
            )
    if G != G.T or is_zero(G.det()):
        raise SystemExit(f"exceptional tangent conic degenerated at {point}")

    tangent_rows = []
    ys = []
    for side_index, z, d in incident_tangents[point]:
        solution, parameters = B.gauss_jordan_solve(d)
        if parameters.rows:
            raise SystemExit(f"nonunique tangent coordinates at {point}")
        if B * solution != d:
            raise SystemExit(f"tangent basis solve failed at {point}")
        y = solution[1:4, 0]
        conic_value = clean((y.T * G * y)[0])
        if y == sp.zeros(3, 1) or not is_zero(conic_value):
            raise SystemExit(
                f"side tangent missed exceptional conic at {point} "
                f"side={side_index} z={z} value={conic_value} "
                f"p={list(p)} d={list(d)} y={list(y)} alpha={list(alpha)} G={G}"
            )
        ys.append(y)
        tangent_rows.append((side_index, z, d, y))
    if len(ys) not in {2, 4}:
        raise SystemExit(f"physical exceptional degree regression at {point}")
    if len({projective_normalize(y) for y in ys}) != len(ys):
        raise SystemExit(f"coincident physical tangent points at exceptional {point}")
    if len(ys) == 4 and sp.Matrix.hstack(*ys).rank() != 3:
        raise SystemExit(f"four tangent points fail to span exceptional conic at {point}")

    p0 = ys[0]
    forms = independent_columns([
        v for v in perpendicular_candidates(p0) if v != sp.zeros(3, 1)
    ])
    if len(forms) != 2 or any(not is_zero(f.dot(p0)) for f in forms):
        raise SystemExit(f"projection forms failed at exceptional {point}")
    grad = G * p0
    tangent_kernel = independent_columns([
        v for v in perpendicular_candidates(grad) if v != sp.zeros(3, 1)
    ])
    w = next(
        (v for v in tangent_kernel if sp.Matrix.hstack(p0, v).rank() == 2),
        None,
    )
    if w is None or not is_zero(grad.dot(w)):
        raise SystemExit(f"projection base tangent failed at exceptional {point}")

    crossing_records = []
    full_crossing_commitments = []
    for k, (side_index, z, d, y) in enumerate(tangent_rows):
        source = w if k == 0 else y
        pair = sp.Matrix([clean(forms[0].dot(source)), clean(forms[1].dot(source))])
        if pair == sp.zeros(2, 1):
            raise SystemExit(f"zero P1 coordinate at exceptional {point}")
        pair = sp.Matrix(projective_normalize(pair))
        full_crossing = {
            "side_index_1based": side_index,
            "side_parameter": PARAMETERS[z - 1],
            "side_parameter_index_1based": z,
            "ambient_tangent_vector_L_basis": encode_vector(d),
            "exceptional_conic_point_L_basis": encode_vector(y),
            "exceptional_P1_homogeneous_coordinate_L_basis": encode_vector(pair),
        }
        full_crossing_commitments.append(full_crossing)
        crossing_records.append({
            "side_index_1based": side_index,
            "side_parameter": PARAMETERS[z - 1],
            "side_parameter_index_1based": z,
            "exceptional_P1_homogeneous_coordinate_L_basis": (
                full_crossing["exceptional_P1_homogeneous_coordinate_L_basis"]
            ),
            "ambient_and_conic_tangent_sha256": canonical_sha256({
                "ambient": full_crossing["ambient_tangent_vector_L_basis"],
                "conic": full_crossing["exceptional_conic_point_L_basis"],
            }),
        })

    crossing_records.sort(
        key=lambda x: (x["side_index_1based"], x["side_parameter_index_1based"])
    )
    got_pairs = [
        (x["side_index_1based"], x["side_parameter_index_1based"])
        for x in crossing_records
    ]
    if got_pairs != expected_incidence[point]:
        raise SystemExit(f"tangent/source incidence mismatch at exceptional {point}")

    degree_histogram[len(crossing_records)] += 1
    node_encoded = encode_vector(p)
    tangent_model_commitment = {
        "node": node_encoded,
        "affine_tangent_basis_radial_first": encode_matrix(B),
        "exceptional_conic_gram": encode_matrix(G),
        "projection_forms": encode_matrix(sp.Matrix.hstack(*forms).T),
        "projection_base_tangent": encode_vector(w),
        "full_crossings": sorted(
            full_crossing_commitments,
            key=lambda x: (x["side_index_1based"], x["side_parameter_index_1based"]),
        ),
    }
    records.append({
        "exceptional_id": f"EXC_{point:03d}",
        "node_point_ambient_P6_L_basis": node_encoded,
        "full_tangent_conic_coordinate_model_sha256": canonical_sha256(
            tangent_model_commitment
        ),
        "physical_crossing_tangent_coordinates": crossing_records,
        "complex_conjugate_exceptional_id": side["exceptional_incidence"][point - 1][
            "complex_conjugate_exceptional_id"
        ],
        "sqrt2_conjugate_exceptional_id": f"EXC_{point:03d}",
    })

if degree_histogram != Counter({2: 24, 4: 24}):
    raise SystemExit(f"exceptional degree histogram regression {degree_histogram}")

cert = {
    "schema": "STAGE33_07_EXCEPTIONAL_P1_TANGENT_COORDINATES_V1",
    "source_locks": {
        "boundary_side_p1_crossing_coordinates_sha256": side_claimed,
        "boundary_side_p1_artifact_run": 33046734567,
        "boundary_side_p1_artifact_id": 9635988498,
        "boundary_side_p1_artifact_zip_sha256": (
            "1b5efeb443d5de38dd3b80608aeebbee552b4bc7ba1a3cfb9dded6ee33968f28"
        ),
        "testa_stoll_commit": "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
        "testa_stoll_cuboids_magma_blob_sha1": (
            "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
        ),
    },
    "field": "L=Q(i,sqrt(2)); all materialized coordinates lie in Q(i)",
    "field_element_encoding": (
        "[real_numerator,real_denominator,i_numerator,i_denominator]; "
        "sqrt2 and i*sqrt2 coefficients are exactly zero"
    ),
    "exceptional_count": 48,
    "physical_crossing_tangent_count": 144,
    "exceptional_physical_incidence_degree_histogram": {
        str(k): v for k, v in sorted(degree_histogram.items())
    },
    "coordinate_construction": (
        "unique node quadratic relation on tangent quotient, then deterministic "
        "projection from first physical tangent point"
    ),
    "exceptional_models": records,
    "exact_checks": {
        "all_48_nodes_reconstructed_from_retained_side_parametrizations": True,
        "all_nodes_satisfy_pinned_surface_quadrics": True,
        "all_nodes_have_jacobian_rank_3": True,
        "all_affine_tangent_spaces_have_dimension_4": True,
        "all_exceptional_tangent_conics_nonsingular": True,
        "all_144_side_derivatives_lie_on_claimed_exceptional_conics": True,
        "all_incidence_pairs_match_retained_side_coordinate_certificate": True,
        "complex_conjugation_matches_retained_exceptional_permutation": True,
        "every_exceptional_P1_coordinate_map_is_nonconstant": True,
        "exceptional_incidence_histogram_matches_24_degree2_plus_24_degree4": True,
    },
    "constructive_progress": {
        "physical_side_P1_coordinates_materialized": True,
        "exceptional_P1_tangent_coordinates_materialized": True,
        "order2_source_first_residue_functions_materialized": False,
        "chosen_global_geometric_lifts_materialized": False,
        "project_14x26_L_squareclass_tensor_materialized": False,
        "absolute_delta_loc_computed": False,
    },
    "next_exact_leaf": (
        "L33-07-MATERIALIZE-26-FIRST-RESIDUE-FUNCTIONS-ON-72-BOUNDARY-P1-MODELS"
    ),
    "new_smallest_exact_kernel": (
        "R33-BR2A-EXPLICIT-26-FIRST-RESIDUE-FUNCTIONS-AND-GLOBAL-GERSTEN-LIFTS"
    ),
    "arithmetic_hs_closed": False,
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
    "execution": {
        "engine": "sympy exact QQ(i) linear algebra",
        "network_or_remote_cas_required": False,
    },
}
cert["canonical_sha256"] = canonical_sha256(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "exceptional_count": 48,
    "tangent_crossing_count": 144,
    "degree_histogram": cert["exceptional_physical_incidence_degree_histogram"],
    "first_residue_functions_materialized": False,
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
