#!/usr/bin/env python3
"""Exact conservative naturality envelope for the two Q coordinate swaps.

The public Magma calculator is not used.  We start from the already retained
finite 2-primary endpoint module and enumerate *every* pair of F2 actions that
could be the restrictions of the two geometric coordinate swaps under the
following necessary exact conditions:

* commute with the retained V4 Galois action;
* conjugate the seven coordinate signs exactly as S3 permutes coordinates;
* preserve the retained quadratic form on A_T[2];
* each swap is an involution and the two satisfy the S3 braid relation.

The actual geometric pair is therefore contained in this finite candidate set.
For each candidate pair we independently impose naturality on the unknown
26x16 finite localization connecting map.  If every candidate gives the same
constraint row-space (or in particular forces zero), no choice of a Picard
Smith basis or remote CAS computation is needed.

This leaf is deliberately conservative: it never identifies a candidate with
the actual integral Picard action unless the finite conditions themselves make
that identification unique.
"""
import hashlib
import json
import runpy
from collections import Counter
from pathlib import Path

import z3

HERE = Path(__file__).resolve().parent
SIGN_SCRIPT = HERE / "certify_retained_geometric_sign_intertwiner_space.py"
OUT = HERE / "finite-swap-candidate-naturality-envelope.json"
QDIM = 26
H1DIM = 16
N = 14
MAX_MODELS = 4096


def canonical_sha256(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def xor_bool(xs):
    xs = list(xs)
    if not xs:
        return z3.BoolVal(False)
    if len(xs) == 1:
        return xs[0]
    return z3.Xor(*xs)


def gf2_rref_masks(rows):
    piv = {}
    for raw in rows:
        x = int(raw)
        while x:
            p = x.bit_length() - 1
            if p in piv:
                x ^= piv[p]
            else:
                for q in list(piv):
                    if (piv[q] >> p) & 1:
                        piv[q] ^= x
                piv[p] = x
                break
    return piv


def null_basis_masks(rows, ncols):
    piv = gf2_rref_masks(rows)
    free = [j for j in range(ncols) if j not in piv]
    out = []
    for f in free:
        v = 1 << f
        for p in sorted(piv):
            if (piv[p] & v).bit_count() & 1:
                v ^= 1 << p
        if any((int(r) & v).bit_count() & 1 for r in rows):
            raise SystemExit("GF2 null-basis verification failed")
        out.append(v)
    return out


def linear_intertwiner_constraints(A, B):
    """Rows for X*A=B*X in row convention, X has N*N bit variables."""
    rows = []
    for i in range(N):
        for j in range(N):
            mask = 0
            for k in range(N):
                if A[k][j]:
                    mask ^= 1 << (i * N + k)
                if B[i][k]:
                    mask ^= 1 << (k * N + j)
            if mask:
                rows.append(mask)
    return rows


def matrix_from_linear_basis(basis, coeffs):
    M = []
    for i in range(N):
        row = []
        for j in range(N):
            bit = i * N + j
            row.append(xor_bool(coeffs[t] for t, v in enumerate(basis) if (v >> bit) & 1))
        M.append(row)
    return M


def mul_entry(A, B, i, j):
    return xor_bool(z3.And(A[i][k], B[k][j]) for k in range(N))


def bool_matrix_from_model(model, M):
    rows = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(1 if z3.is_true(model.eval(M[i][j], model_completion=True)) else 0)
        rows.append(row)
    return rows


def rowspace_sha256(rows):
    piv = gf2_rref_masks(rows)
    canonical = [piv[p] for p in sorted(piv, reverse=True)]
    raw = ",".join(str(x) for x in canonical).encode()
    return hashlib.sha256(raw).hexdigest()


# Reuse the already-passing seven-sign exact leaf.  This reconstructs the
# source quotient, exact Q(i) boundary geometry, retained endpoint receiver,
# and the 270 sign-naturality constraints without remote CAS.
ns = runpy.run_path(str(SIGN_SCRIPT))
A_cc = ns["A_cc"]
A_ct = ns["A_ct"]
A_signs = ns["A_signs"]
mods = ns["mods"]
signs = ns["signs"]
constraints7 = list(ns["constraints"])
if ns["rank_bitmasks"](constraints7) != 270:
    raise SystemExit("seven-sign constraint-rank regression")

# The two swaps act on coordinate-sign labels as (a1 a2)(b1 b2) and
# (a1 a3)(b1 b3), fixing c.
perm12 = [1, 0, 2, 4, 3, 5, 6]
perm13 = [2, 1, 0, 5, 4, 3, 6]


def intertwiner_basis_for_sign_permutation(perm):
    rows = []
    for A, B in [(A_cc, A_cc), (A_ct, A_ct)]:
        rows.extend(linear_intertwiner_constraints(A, B))
    for i in range(7):
        rows.extend(linear_intertwiner_constraints(A_signs[i], A_signs[perm[i]]))
    basis = null_basis_masks(rows, N * N)
    return basis, len(rows), N * N - len(basis)


basis12, linear_eq12, linear_rank12 = intertwiner_basis_for_sign_permutation(perm12)
basis13, linear_eq13, linear_rank13 = intertwiner_basis_for_sign_permutation(perm13)
if len(basis12) != 33 or len(basis13) != 33 or linear_rank12 != 163 or linear_rank13 != 163:
    raise SystemExit("finite swap linear-intertwiner dimension regression")

u = [z3.Bool(f"u_{j}") for j in range(len(basis12))]
v = [z3.Bool(f"v_{j}") for j in range(len(basis13))]
X12 = matrix_from_linear_basis(basis12, u)
X13 = matrix_from_linear_basis(basis13, v)
solver = z3.Solver()
solver.set(timeout=300000)

# Involutions.
for X in (X12, X13):
    for i in range(N):
        for j in range(N):
            solver.add(mul_entry(X, X, i, j) == z3.BoolVal(i == j))

# Restriction of the retained finite quadratic form to A_T[2].  It takes only
# values 0 or 1 after dividing its numerator by 8.  Build its polar form.
b8 = [[int(x) for x in row] for row in signs["discriminant_bilinear_numerator_over_8_reduced"]]
scales = [int(m) // 2 for m in mods]


def q2_bits(bits):
    vec = [scales[i] * ((bits >> i) & 1) for i in range(N)]
    val = sum(vec[i] * b8[i][j] * vec[j] for i in range(N) for j in range(N)) % 16
    if val not in (0, 8):
        raise SystemExit("A_T[2] quadratic restriction escaped F2")
    return val // 8


qdiag = [q2_bits(1 << i) for i in range(N)]
polar = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        polar[i][j] = q2_bits((1 << i) ^ (1 << j)) ^ qdiag[i] ^ qdiag[j]
if any(polar[i][i] for i in range(N)) or any(polar[i][j] != polar[j][i] for i in range(N) for j in range(N)):
    raise SystemExit("A_T[2] polar-form regression")


def q_expr(row):
    terms = [row[k] for k in range(N) if qdiag[k]]
    for k in range(N):
        for ell in range(k + 1, N):
            if polar[k][ell]:
                terms.append(z3.And(row[k], row[ell]))
    return xor_bool(terms)


def b_expr(a, b):
    return xor_bool(
        z3.And(a[k], b[ell])
        for k in range(N)
        for ell in range(N)
        if polar[k][ell]
    )


for X in (X12, X13):
    for i in range(N):
        solver.add(q_expr(X[i]) == z3.BoolVal(bool(qdiag[i])))
    for i in range(N):
        for j in range(i + 1, N):
            solver.add(b_expr(X[i], X[j]) == z3.BoolVal(bool(polar[i][j])))

# S3 braid relation.  Introduce exact intermediate product matrices so the SAT
# instance remains quadratic rather than cubic.
Y = [[z3.Bool(f"y_{i}_{j}") for j in range(N)] for i in range(N)]
Z = [[z3.Bool(f"z_{i}_{j}") for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        solver.add(Y[i][j] == mul_entry(X12, X13, i, j))
        solver.add(Z[i][j] == mul_entry(X13, X12, i, j))
for i in range(N):
    for j in range(N):
        solver.add(mul_entry(Y, X12, i, j) == mul_entry(Z, X13, i, j))

# Reconstruct the two exact source-side swap actions purely from the retained
# Q(i) node coordinates and boundary incidence.  No point ordering is guessed.
node_vectors = ns["node_vectors"]
point_lookup = ns["point_lookup"]
side_incidence = ns["side_incidence"]
side_lookup = ns["side_lookup"]
projective_normalize = ns["projective_normalize"]
edges = ns["edges"]
edge_index = ns["edge_index"]
U44 = ns["U44"]
R17 = ns["R17"]
O4 = ns["O4"]
solve61 = ns["solve61"]
permute_vector = ns["permute_vector"]
rowmul_z = ns["rowmul_z"]
T = ns["T"]
diag29 = ns["diag29"]
relation29 = ns["relation29"]
source_basis = ns["source_basis"]
support_to_source = ns["support_to_source"]
rank2 = ns["rank2"]
matmul2 = ns["matmul2"]
eye = ns["eye"]
rowmul2 = ns["rowmul2"]
transpose = ns["transpose"]
h1 = ns["h1"]
solve_h1 = ns["solve_h1"]
rank_bitmasks = ns["rank_bitmasks"]

def boundary_swap(coord_perm):
    pointp = []
    for p in range(1, 49):
        old = node_vectors[p]
        image = [old[coord_perm[j]] for j in range(7)]
        key = projective_normalize(image)
        if key not in point_lookup:
            raise SystemExit("coordinate swap escaped retained 48 nodes")
        pointp.append(point_lookup[key] - 1)
    if sorted(pointp) != list(range(48)):
        raise SystemExit("coordinate-swap point permutation regression")
    sidep = []
    for side in range(1, 25):
        image_set = frozenset(pointp[p - 1] + 1 for p in side_incidence[side])
        if image_set not in side_lookup:
            raise SystemExit("coordinate swap escaped retained 24 physical sides")
        sidep.append(side_lookup[image_set] - 1)
    if sorted(sidep) != list(range(24)):
        raise SystemExit("coordinate-swap side permutation regression")
    return sidep, pointp


def source_action_from_boundary(sidep, pointp, name):
    vertex_perm = sidep + [24 + x for x in pointp]
    edge_perm = [edge_index[(vertex_perm[a], vertex_perm[b])] for a, b in edges]
    if sorted(edge_perm) != list(range(144)):
        raise SystemExit(f"{name}: crossing permutation regression")
    for urow in U44:
        coords = solve61(permute_vector(urow, edge_perm, 2))
        if any(coords[44:]):
            raise SystemExit(f"{name}: U44 escaped itself")
    r_action = []
    for row in R17:
        coords = solve61(permute_vector(row, edge_perm, 2))
        r_action.append([int(x) & 1 for x in coords[44:]])
    o_action = []
    for j, row in enumerate(O4):
        image = permute_vector(row, edge_perm, 4)
        matches = []
        for k, target in enumerate(O4):
            if image == target:
                matches.append((k, 1))
            if image == [(-int(x)) % 4 for x in target]:
                matches.append((k, -1))
        if len(matches) != 1:
            raise SystemExit(f"{name}: O4_{j+1} signed-generator regression {matches}")
        o_action.append(matches[0])
    A29 = []
    for i in range(17):
        A29.append(r_action[i] + [0] * 12)
    for j in range(12):
        row = [0] * 29
        target, sgn = o_action[j]
        row[17 + target] = sgn
        A29.append(row)
    for rel in relation29:
        smith_rel = rowmul_z(rowmul_z(rel, A29), T)
        if any(smith_rel[j] % diag29[j] for j in range(29)):
            raise SystemExit(f"{name}: exact source relation lattice not preserved")
    source_action = []
    for rec in source_basis:
        original = [int(x) for x in rec["original_R17_O12_coordinates_Z29"]]
        smith = rowmul_z(rowmul_z(original, A29), T)
        out = [0] * QDIM
        for j, d in enumerate(diag29):
            value = smith[j] % d
            if not value:
                continue
            if j not in support_to_source:
                raise SystemExit(f"{name}: source image hit trivial Smith coordinate")
            source_index, basis_value = support_to_source[j]
            if value != basis_value % d:
                raise SystemExit(f"{name}: source image not A2-basis-valued")
            out[source_index] ^= 1
        source_action.append(out)
    if rank2(source_action, QDIM) != QDIM or matmul2(source_action, source_action) != eye(QDIM):
        raise SystemExit(f"{name}: source action is not an involutive automorphism")
    return source_action, o_action


swap12_boundary = boundary_swap([1, 0, 2, 4, 3, 5, 6])
swap13_boundary = boundary_swap([2, 1, 0, 5, 4, 3, 6])
source12, o12 = source_action_from_boundary(*swap12_boundary, "swap12")
source13, o13 = source_action_from_boundary(*swap13_boundary, "swap13")
# S3 must already hold on the source quotient.
if matmul2(matmul2(source12, source13), source12) != matmul2(matmul2(source13, source12), source13):
    raise SystemExit("source swap actions fail S3 braid relation")


def h1_action_from_AT2(A):
    proper = transpose(A)
    out = []
    for z in h1:
        transformed = rowmul2(z[:N], proper) + rowmul2(z[N:], proper)
        coeff = solve_h1(transformed)
        out.append(coeff[4:])
    if rank2(out, H1DIM) != H1DIM:
        raise SystemExit("candidate receiver H1 action lost rank")
    return out


def naturality_rows(source_action, h1_action):
    out = []
    for i in range(QDIM):
        for j in range(H1DIM):
            mask = 0
            for k in range(QDIM):
                if source_action[i][k]:
                    mask ^= 1 << (k * H1DIM + j)
            for ell in range(H1DIM):
                if h1_action[ell][j]:
                    mask ^= 1 << (i * H1DIM + ell)
            if mask:
                out.append(mask)
    return out


candidate_records = []
rowspace_counter = Counter()
dimension_counter = Counter()
complete = False
for model_index in range(MAX_MODELS + 1):
    status = solver.check()
    if status == z3.unsat:
        complete = True
        break
    if status == z3.unknown:
        raise SystemExit(f"finite swap SAT returned unknown: {solver.reason_unknown()}")
    if model_index == MAX_MODELS:
        break
    model = solver.model()
    M12 = bool_matrix_from_model(model, X12)
    M13 = bool_matrix_from_model(model, X13)
    h12 = h1_action_from_AT2(M12)
    h13 = h1_action_from_AT2(M13)
    if matmul2(h12, h12) != eye(H1DIM) or matmul2(h13, h13) != eye(H1DIM):
        raise SystemExit("candidate H1 involution regression")
    if matmul2(matmul2(h12, h13), h12) != matmul2(matmul2(h13, h12), h13):
        raise SystemExit("candidate H1 braid regression")
    rows = constraints7 + naturality_rows(source12, h12) + naturality_rows(source13, h13)
    rk = rank_bitmasks(rows)
    rem = QDIM * H1DIM - rk
    rsha = rowspace_sha256(rows)
    dimension_counter[rem] += 1
    rowspace_counter[rsha] += 1
    candidate_records.append({
        "candidate_index": model_index,
        "swap12_A_T2_action_rows_as_bitints": [sum((int(b) & 1) << j for j, b in enumerate(row)) for row in M12],
        "swap13_A_T2_action_rows_as_bitints": [sum((int(b) & 1) << j for j, b in enumerate(row)) for row in M13],
        "naturality_constraint_rank_f2": rk,
        "remaining_intertwiner_dimension_f2": rem,
        "constraint_rowspace_sha256": rsha,
    })
    # Block this exact pair of free-coordinate assignments.
    vals = []
    for var in u + v:
        val = z3.is_true(model.eval(var, model_completion=True))
        vals.append(var != z3.BoolVal(val))
    solver.add(z3.Or(*vals))

if not complete:
    raise SystemExit(f"finite swap candidate enumeration exceeded cap {MAX_MODELS}")
if not candidate_records:
    raise SystemExit("finite swap candidate set unexpectedly empty")

unique_rowspaces = len(rowspace_counter)
unique_dimensions = len(dimension_counter)
max_remaining = max(dimension_counter)
min_remaining = min(dimension_counter)
robust_zero = max_remaining == 0
rowspace_independent = unique_rowspaces == 1

cert = {
    "schema": "STAGE33_07_FINITE_SWAP_CANDIDATE_NATURALITY_ENVELOPE_V1",
    "execution": {
        "remote_cas_used": False,
        "z3_exact_boolean_solver_used": True,
        "candidate_enumeration_complete": complete,
        "candidate_cap": MAX_MODELS,
    },
    "finite_receiver_problem": {
        "A_T2_dimension_f2": N,
        "swap12_linear_intertwiner_dimension_f2": len(basis12),
        "swap13_linear_intertwiner_dimension_f2": len(basis13),
        "necessary_conditions_enforced": [
            "commute_with_cc_ct",
            "conjugate_seven_coordinate_signs_by_coordinate_permutation",
            "preserve_restricted_finite_quadratic_form",
            "each_swap_involution",
            "S3_braid_relation",
        ],
        "actual_integral_picard_swap_identified": len(candidate_records) == 1,
        "candidate_pair_count": len(candidate_records),
    },
    "source_geometry": {
        "boundary_permutations_reconstructed_from_exact_qi_nodes": True,
        "swap12_side_permutation_1based": [x + 1 for x in swap12_boundary[0]],
        "swap12_exceptional_permutation_1based": [x + 1 for x in swap12_boundary[1]],
        "swap13_side_permutation_1based": [x + 1 for x in swap13_boundary[0]],
        "swap13_exceptional_permutation_1based": [x + 1 for x in swap13_boundary[1]],
        "source_swap_actions_satisfy_S3": True,
    },
    "naturality_envelope": {
        "ambient_matrix_space_dimension_f2": QDIM * H1DIM,
        "seven_sign_only_constraint_rank_f2": 270,
        "seven_sign_only_remaining_dimension_f2": 146,
        "remaining_dimension_histogram": {str(k): v for k, v in sorted(dimension_counter.items())},
        "minimum_remaining_dimension_f2": min_remaining,
        "maximum_remaining_dimension_f2": max_remaining,
        "unique_constraint_rowspace_count": unique_rowspaces,
        "constraint_rowspace_independent_of_finite_swap_candidate": rowspace_independent,
        "finite_v4_delta_loc_forced_zero_for_every_admissible_candidate": robust_zero,
    },
    "candidate_records": candidate_records,
    "exact_consequence": {
        "actual_geometric_finite_swap_pair_is_contained_in_candidate_set": True,
        "all_26_source_columns_treated_uniformly": True,
        "connecting_matrix_columns_explicitly_materialized": 0,
        "middle_gersten_module_action_materialized": False,
        "absolute_delta_loc_computed": False,
        "project_14x26_L_squareclass_tensor_materialized": False,
        "arithmetic_HS_closed": False,
    },
    "next_exact_leaf": (
        "L33-07-PROMOTE-FINITE-V4-DELTA-LOC-ZERO-THEN-ATTACK-14x26-GL-SQUARECLASS-TENSOR"
        if robust_zero else
        "L33-07-DISTINGUISH-FINITE-SWAP-CANDIDATES-OR-MATERIALIZE-MIDDLE-GERSTEN-EXTENSION-DATA"
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
    "candidate_pair_count": len(candidate_records),
    "candidate_enumeration_complete": complete,
    "remaining_dimension_histogram": cert["naturality_envelope"]["remaining_dimension_histogram"],
    "unique_constraint_rowspace_count": unique_rowspaces,
    "finite_v4_delta_loc_forced_zero_for_every_candidate": robust_zero,
    "certificate_sha256": cert["canonical_sha256"],
    "next": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
