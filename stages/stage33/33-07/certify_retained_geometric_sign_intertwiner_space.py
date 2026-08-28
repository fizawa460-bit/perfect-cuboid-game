#!/usr/bin/env python3
"""Constrain the 26x16 finite localization ambiguity by seven retained Q-signs.

This is a fully local/exact replacement for the public-Magma-heavy sign part of
the Q-automorphism scout.  The endpoint action of the seven coordinate signs is
source-locked from the successful q256 artifact retained in this branch.  Their
boundary action is reconstructed independently from the 48 exact Q(i) node
coordinates and side-incidence data already committed in the exceptional-P1
certificate.  The finite H^1(V4,Br[2]) receiver is rebuilt in the retained
endpoint Smith basis, so no comparison with a different Smith basis is needed.

The result is only a naturality constraint on the unknown middle-Gersten
extension class.  No connecting-map column is selected or materialized.
"""
import hashlib
import json
import runpy
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
BASE_SCRIPT = HERE / "materialize_order2_first_residue_functions.py"
IB_PATH = HERE / "two-primary-residue-invariant-basis.json"
RECEIVER_PATH = HERE / "order2-localization-receiver.json"
EXC_PATH = HERE / "exceptional-p1-tangent-coordinates.json"
SIGN_PATH = HERE / "retained-q256-geometric-sign-endpoint.json"
OUT = HERE / "retained-geometric-sign-delta-loc-intertwiner-space.json"

EXPECTED_IB = "f18a54717b2327f7abc8ee87859b5c0537bffc062a1d5c1e36a5763c46faa939"
EXPECTED_RECEIVER = "9280846c6e7ae8a043e36c7b5498f11476901567b229b94e953b79afab891bda"
EXPECTED_EXC = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
EXPECTED_SIGN = "19d59e89b87d49681ae8b1b165085d529bef64b40c2d5ab6fe692a6b899fb061"
SIGN_NAMES = ["sign_a1", "sign_a2", "sign_a3", "sign_b1", "sign_b2", "sign_b3", "sign_c"]
N = 14
QDIM = 26
H1DIM = 16
I = sp.I


def canonical_sha256(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj.get("canonical_sha256")
    body = dict(obj); body.pop("canonical_sha256", None)
    actual = canonical_sha256(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"source lock moved for {path.name}: {claimed} {actual}")
    return obj


def xor(a, b):
    return [int(x) ^ int(y) for x, y in zip(a, b)]


def row_basis(rows, ncols):
    a = [[int(x) & 1 for x in row] for row in rows if any(int(x) & 1 for x in row)]
    if any(len(row) != ncols for row in a):
        raise SystemExit("GF2 row width regression")
    r = 0; pivots = []
    for c in range(ncols):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][c]:
                a[i] = xor(a[i], a[r])
        pivots.append(c); r += 1
        if r == len(a): break
    return a[:r], pivots


def rank2(rows, ncols=None):
    if ncols is None:
        ncols = len(rows[0]) if rows else 0
    return len(row_basis(rows, ncols)[0])


def nullspace2(rows, ncols):
    rr, pivots = row_basis(rows, ncols)
    free = [j for j in range(ncols) if j not in pivots]
    out = []
    for f in free:
        v = [0] * ncols; v[f] = 1
        for row, p in reversed(list(zip(rr, pivots))):
            v[p] = sum((row[j] & v[j]) for j in range(p + 1, ncols)) & 1
        out.append(v)
    if any(any(sum(r[j] * v[j] for j in range(ncols)) & 1 for r in rows) for v in out):
        raise SystemExit("GF2 nullspace verification failed")
    return out


def build_solver(basis):
    pivots = {}
    for i, row in enumerate(basis):
        x = sum((int(b) & 1) << j for j, b in enumerate(row)); coord = 1 << i
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                bx, bc = pivots[p]; x ^= bx; coord ^= bc
            else:
                pivots[p] = (x, coord); break
        if not x:
            raise SystemExit("coordinate basis is dependent")
    def solve(row):
        x = sum((int(b) & 1) << j for j, b in enumerate(row)); coord = 0
        while x:
            p = x.bit_length() - 1
            if p not in pivots:
                raise SystemExit("target escaped coordinate span")
            bx, bc = pivots[p]; x ^= bx; coord ^= bc
        return [(coord >> i) & 1 for i in range(len(basis))]
    return solve


def rowmul2(v, M):
    return [sum((int(v[k]) & 1) * (int(M[k][j]) & 1) for k in range(len(v))) & 1 for j in range(len(M[0]))]


def rowmul_z(v, M):
    return [sum(int(v[k]) * int(M[k][j]) for k in range(len(v))) for j in range(len(M[0]))]


def matmul2(A, B):
    return [rowmul2(row, B) for row in A]


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def transpose(A):
    return [list(col) for col in zip(*A)]


def sub2(A, B):
    return [[int(A[i][j]) ^ int(B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def permute_vector(row, perm, modulus):
    out = [0] * len(row)
    for i, value in enumerate(row):
        out[perm[i]] = int(value) % modulus
    return out


def rank_bitmasks(rows):
    pivots = {}
    for raw in rows:
        x = int(raw)
        while x:
            p = x.bit_length() - 1
            if p in pivots: x ^= pivots[p]
            else: pivots[p] = x; break
    return len(pivots)


def decode_qi(e):
    if len(e) != 4:
        raise SystemExit("Q(i) encoding width regression")
    return sp.Rational(int(e[0]), int(e[1])) + sp.Rational(int(e[2]), int(e[3])) * I


def clean(x):
    return sp.cancel(sp.expand(x))


def projective_normalize(v):
    values = [clean(x) for x in v]
    pivot = next((x for x in values if clean(x) != 0), None)
    if pivot is None:
        raise SystemExit("zero exceptional projective vector")
    return tuple(clean(x / pivot) for x in values)


def restrict_two(M, mods):
    scales = [m // 2 for m in mods]
    out = []
    for i in range(N):
        row = []
        for j in range(N):
            num = scales[i] * int(M[i][j])
            if num % scales[j]:
                raise SystemExit("retained A_T[2] restriction integrality failed")
            row.append((num // scales[j]) & 1)
        out.append(row)
    return out


# Exact source-side residue algebra.
ns = runpy.run_path(str(BASE_SCRIPT))
edges = ns["edges"]
edge_index = ns["edge_index"]
U44 = ns["U44"]
R17 = ns["R17"]
O4 = ns["O4"]
solve61 = ns["solve61"]
br0g = ns["br0g"]
if (len(edges), len(U44), len(R17), len(O4)) != (144, 44, 17, 12):
    raise SystemExit("boundary raw basis shape regression")

ib = load_locked(IB_PATH, EXPECTED_IB)
receiver = load_locked(RECEIVER_PATH, EXPECTED_RECEIVER)
exc = load_locked(EXC_PATH, EXPECTED_EXC)
signs = load_locked(SIGN_PATH, EXPECTED_SIGN)
if receiver["finite_source_order2_dimension_f2"] != QDIM:
    raise SystemExit("source dimension regression")

# Reconstruct exact exceptional-node permutations under each coordinate sign.
models = exc["exceptional_models"]
if len(models) != 48:
    raise SystemExit("exceptional model count regression")
node_vectors = {}
side_incidence = {j: set() for j in range(1, 25)}
for rec in models:
    p = int(rec["exceptional_id"][4:])
    node_vectors[p] = [decode_qi(e) for e in rec["node_point_ambient_P6_L_basis"]]
    for cross in rec["physical_crossing_tangent_coordinates"]:
        side_incidence[int(cross["side_index_1based"])].add(p)
if any(len(v) != 6 for v in side_incidence.values()):
    raise SystemExit("physical side exceptional incidence regression")
point_lookup = {projective_normalize(v): p for p, v in node_vectors.items()}
if len(point_lookup) != 48:
    raise SystemExit("exceptional node coordinates are not 48 distinct points")
side_lookup = {frozenset(v): j for j, v in side_incidence.items()}
if len(side_lookup) != 24:
    raise SystemExit("physical side incidence sets are not distinct")

boundary_perms = []
for coord in range(7):
    pointp = []
    for p in range(1, 49):
        v = list(node_vectors[p]); v[coord] = -v[coord]
        key = projective_normalize(v)
        if key not in point_lookup:
            raise SystemExit(f"{SIGN_NAMES[coord]}: node image escaped retained 48 points")
        pointp.append(point_lookup[key] - 1)
    if sorted(pointp) != list(range(48)):
        raise SystemExit(f"{SIGN_NAMES[coord]}: exceptional permutation regression")
    sidep = []
    for side in range(1, 25):
        image_set = frozenset(pointp[p - 1] + 1 for p in side_incidence[side])
        if image_set not in side_lookup:
            raise SystemExit(f"{SIGN_NAMES[coord]}: side image escaped retained incidence sets")
        sidep.append(side_lookup[image_set] - 1)
    if sorted(sidep) != list(range(24)):
        raise SystemExit(f"{SIGN_NAMES[coord]}: physical-side permutation regression")
    boundary_perms.append((sidep, pointp))

# The seven coordinate signs multiply to global projective -1, hence identity.
def compose_perm(p, q):
    return [q[p[i]] for i in range(len(p))]
side_prod = list(range(24)); point_prod = list(range(48))
for sidep, pointp in boundary_perms:
    side_prod = compose_perm(side_prod, sidep)
    point_prod = compose_perm(point_prod, pointp)
if side_prod != list(range(24)) or point_prod != list(range(48)):
    raise SystemExit("seven boundary sign permutations do not multiply to projective identity")

# Rebuild the retained endpoint proper-Br2 V4 module and H1 quotient basis.
mods = [int(x) for x in signs["discriminant_moduli"]]
if mods != [2] * 4 + [4] * 6 + [8] * 4:
    raise SystemExit("retained sign discriminant moduli regression")
A_cc = restrict_two(signs["cc_action_mixed_moduli"], mods)
A_ct = restrict_two(signs["ct_action_mixed_moduli"], mods)
A_signs = [restrict_two(M, mods) for M in signs["sign_actions_mixed_moduli"]]
B_cc = transpose(A_cc); B_ct = transpose(A_ct); B_signs = [transpose(A) for A in A_signs]
I14 = eye(N)
if matmul2(B_cc, B_cc) != I14 or matmul2(B_ct, B_ct) != I14 or matmul2(B_cc, B_ct) != matmul2(B_ct, B_cc):
    raise SystemExit("retained proper Br2 V4 action regression")
for name, B in zip(SIGN_NAMES, B_signs):
    if matmul2(B, B) != I14 or matmul2(B, B_cc) != matmul2(B_cc, B) or matmul2(B, B_ct) != matmul2(B_ct, B):
        raise SystemExit(f"{name}: retained proper action regression")

Ng = sub2(B_cc, I14); Nh = sub2(B_ct, I14)
eq = []
for j in range(N): eq.append([Ng[i][j] for i in range(N)] + [0] * N)
for j in range(N): eq.append([0] * N + [Nh[i][j] for i in range(N)])
for j in range(N): eq.append([Nh[i][j] for i in range(N)] + [Ng[i][j] for i in range(N)])
z1 = nullspace2(eq, 28)
b1, _ = row_basis([Ng[i] + Nh[i] for i in range(N)], 28)
if (len(z1), len(b1)) != (20, 4):
    raise SystemExit(f"retained H1 dimensions moved: Z1={len(z1)} B1={len(b1)}")
frame = list(b1); h1 = []
for z in z1:
    if rank2(frame + [z], 28) > len(frame):
        frame.append(z); h1.append(z)
if len(h1) != H1DIM or rank2(frame, 28) != 20:
    raise SystemExit("retained H1 quotient complement regression")
solve_h1 = build_solver(frame)

# Exact A[2] Smith source basis data.
T = [[int(x) for x in row] for row in ib["smith_right_unimodular_T"]]
diag29 = [int(x) for x in ib["smith_diagonal"]]
if diag29 != [1] * 3 + [2] * 23 + [4] * 3:
    raise SystemExit("A source Smith diagonal regression")
source_basis = receiver["finite_source_basis"]
support_to_source = {}
for source_index, rec in enumerate(source_basis):
    smith = [int(x) for x in rec["smith_coordinates_Z29"]]
    support = [j for j, x in enumerate(smith) if x]
    if len(support) != 1:
        raise SystemExit("A2 Smith basis support regression")
    support_to_source[support[0]] = (source_index, smith[support[0]])
if len(support_to_source) != QDIM:
    raise SystemExit("A2 Smith supports not distinct")
relation29 = [[int(x) for x in row] for row in br0g["diagnostic_quotient_by_U44_relation_matrix_29x29"]]

records = []
constraints = []
progressive = []
source_sign_actions = []
h1_sign_actions = []
for sign_index, name in enumerate(SIGN_NAMES):
    sidep, pointp = boundary_perms[sign_index]
    vertex_perm = sidep + [24 + x for x in pointp]
    edge_perm = [edge_index[(vertex_perm[a], vertex_perm[b])] for a, b in edges]
    if sorted(edge_perm) != list(range(144)):
        raise SystemExit(f"{name}: crossing permutation regression")

    for u in U44:
        coords = solve61(permute_vector(u, edge_perm, 2))
        if any(coords[44:]):
            raise SystemExit(f"{name}: U44 escaped itself")

    r_action = []
    for row in R17:
        coords = solve61(permute_vector(row, edge_perm, 2))
        r_action.append([int(x) & 1 for x in coords[44:]])

    o_action = []
    for j, row in enumerate(O4):
        image = permute_vector(row, edge_perm, 4); matches = []
        for k, target in enumerate(O4):
            if image == target: matches.append((k, 1))
            if image == [(-int(x)) % 4 for x in target]: matches.append((k, -1))
        if len(matches) != 1:
            raise SystemExit(f"{name}: O4_{j+1} not a unique signed generator: {matches}")
        o_action.append(matches[0])

    A29 = []
    for i in range(17): A29.append(r_action[i] + [0] * 12)
    for j in range(12):
        row = [0] * 29; target, sgn = o_action[j]; row[17 + target] = sgn; A29.append(row)
    for rel in relation29:
        smith_rel = rowmul_z(rowmul_z(rel, A29), T)
        if any(smith_rel[j] % diag29[j] for j in range(29)):
            raise SystemExit(f"{name}: exact relation lattice not preserved")

    source_action = []
    for rec in source_basis:
        original = [int(x) for x in rec["original_R17_O12_coordinates_Z29"]]
        smith = rowmul_z(rowmul_z(original, A29), T)
        out = [0] * QDIM
        for j, d in enumerate(diag29):
            value = smith[j] % d
            if not value: continue
            if j not in support_to_source:
                raise SystemExit(f"{name}: source image hit trivial Smith coordinate {j}")
            source_index, basis_value = support_to_source[j]
            if value != basis_value % d:
                raise SystemExit(f"{name}: source image not A2 basis-valued at Smith {j}")
            out[source_index] ^= 1
        source_action.append(out)
    if rank2(source_action, QDIM) != QDIM or matmul2(source_action, source_action) != eye(QDIM):
        raise SystemExit(f"{name}: source A2 action not involutive automorphism")
    source_sign_actions.append(source_action)

    proper = B_signs[sign_index]
    h1_action = []
    for z in h1:
        transformed = rowmul2(z[:N], proper) + rowmul2(z[N:], proper)
        coeff = solve_h1(transformed)
        h1_action.append(coeff[4:])
    if rank2(h1_action, H1DIM) != H1DIM or matmul2(h1_action, h1_action) != eye(H1DIM):
        raise SystemExit(f"{name}: induced H1 action regression")
    h1_sign_actions.append(h1_action)

    local = []
    for i in range(QDIM):
        for j in range(H1DIM):
            mask = 0
            for k in range(QDIM):
                if source_action[i][k]: mask ^= 1 << (k * H1DIM + j)
            for ell in range(H1DIM):
                if h1_action[ell][j]: mask ^= 1 << (i * H1DIM + ell)
            if mask: local.append(mask)
    constraints.extend(local)
    rk = rank_bitmasks(constraints); rem = QDIM * H1DIM - rk
    progressive.append({"after_generator": name, "constraint_rank_f2": rk, "intertwiner_dimension_f2": rem})
    records.append({
        "name": name,
        "boundary_side_permutation_1based": [x + 1 for x in sidep],
        "boundary_exceptional_permutation_1based": [x + 1 for x in pointp],
        "source_A2_action_f2": source_action,
        "proper_Br2_action_f2": proper,
        "finite_H1_action_f2": h1_action,
        "O4_signed_permutation": [
            {"source_1based": j + 1, "target_1based": t + 1, "sign": s}
            for j, (t, s) in enumerate(o_action)
        ],
    })

# Verify the projective product relation also after descent to source and H1.
def product_actions(actions, n):
    out = eye(n)
    for A in actions: out = matmul2(out, A)
    return out
if product_actions(source_sign_actions, QDIM) != eye(QDIM):
    raise SystemExit("seven source sign actions do not multiply to identity")
if product_actions(h1_sign_actions, H1DIM) != eye(H1DIM):
    raise SystemExit("seven H1 sign actions do not multiply to identity")

final_rank = rank_bitmasks(constraints)
remaining = QDIM * H1DIM - final_rank
forced_zero = remaining == 0
cert = {
    "schema": "STAGE33_07_RETAINED_GEOMETRIC_SIGN_DELTA_LOC_INTERTWINER_V1",
    "source_locks": {
        "retained_q256_geometric_sign_endpoint_sha256": EXPECTED_SIGN,
        "exceptional_p1_tangent_coordinates_sha256": EXPECTED_EXC,
        "two_primary_residue_invariant_basis_sha256": EXPECTED_IB,
        "order2_localization_receiver_sha256": EXPECTED_RECEIVER,
    },
    "execution": {"remote_cas_used": False, "all_linear_algebra_exact": True},
    "naturality_statement": {
        "q_defined_coordinate_sign_generators": SIGN_NAMES,
        "generator_count": 7,
        "independent_generator_rank": 6,
        "seven_sign_product_is_projective_identity": True,
        "boundary_permutations_reconstructed_from_exact_qi_node_coordinates": True,
        "all_signs_preserve_U44_and_exact_29_generator_source_quotient": True,
        "all_signs_commute_with_V4_on_proper_Br2": True,
        "connecting_map_equivariance_equation": "S_phi * D = D * R_phi for D in Mat_{26x16}(F2)",
    },
    "retained_receiver_reconstruction": {
        "proper_Br2_dimension_f2": 14,
        "finite_Z1_dimension_f2": len(z1),
        "finite_B1_dimension_f2": len(b1),
        "finite_H1_dimension_f2": len(h1),
    },
    "progressive_intertwiner_reduction": progressive,
    "final_intertwiner": {
        "ambient_matrix_space_dimension_f2": 416,
        "naturality_constraint_rank_f2": final_rank,
        "intertwiner_dimension_f2": remaining,
        "compatible_connecting_map_count": "1" if forced_zero else f"2^{remaining}",
        "finite_v4_delta_loc_forced_zero_by_seven_sign_naturality": forced_zero,
    },
    "automorphism_records": records,
    "exact_consequence": {
        "all_26_source_columns_treated_uniformly": True,
        "remaining_extension_ambiguity_dimension_f2_after_seven_sign_naturality": remaining,
        "connecting_matrix_columns_explicitly_materialized": 0,
        "middle_gersten_module_action_materialized": False,
        "finite_v4_delta_loc_computed_without_explicit_middle_module": forced_zero,
        "absolute_delta_loc_computed": False,
        "project_14x26_L_squareclass_tensor_materialized": False,
        "arithmetic_HS_closed": False,
    },
    "next_exact_leaf": (
        "L33-07-PROMOTE-FINITE-V4-DELTA-LOC-ZERO-THEN-ATTACK-14x26-GL-SQUARECLASS-TENSOR"
        if forced_zero else
        "L33-07-ADD-TWO-COORDINATE-SWAPS-TO-SEVEN-SIGN-NATURALITY-OR-MATERIALIZE-MIDDLE-GERSTEN-DATA"
    ),
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
    "remote_cas_used": False,
    "geometric_sign_generators": 7,
    "ambient_extension_dimension_f2": 416,
    "naturality_constraint_rank_f2": final_rank,
    "remaining_intertwiner_dimension_f2": remaining,
    "finite_v4_delta_loc_forced_zero": forced_zero,
    "certificate_sha256": cert["canonical_sha256"],
    "next": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
