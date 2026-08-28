#!/usr/bin/env python3
"""Identify the actual coordinate swaps in the retained A_T[2] Smith basis.

The intrinsic leaf knows the actual swap and seven coordinate-sign actions on
A_Pic[2]=ker(G mod 2).  The retained finite receiver uses a different Smith
basis of the same 14-dimensional quadratic space.  We solve exactly for an
invertible quadratic isometry S intertwining the seven named sign actions and
transport both actual swaps through S.  We then ask a second SAT question to
determine whether the transported swap pair is unique among all such S.
"""
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

import z3

HERE = Path(__file__).resolve().parent
INTRINSIC_SCRIPT = HERE / "certify_actual_coordinate_swap_at2_actions.py"
RETAINED_SCRIPT = HERE / "certify_retained_geometric_sign_intertwiner_space.py"
QUADRATIC_PATH = HERE / "retained-q256-geometric-sign-quadratic.json"
OUT = HERE / "intrinsic-to-retained-at2-swap-transport.json"
N = 14
EXPECTED_QUADRATIC = "5fa065e1781da27f92983749cd782635839251e93b191e7ee4e6063f1fb3843c"


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def xor_bool(xs):
    xs = list(xs)
    if not xs:
        return z3.BoolVal(False)
    out = xs[0]
    for x in xs[1:]:
        out = z3.Xor(out, x)
    return out


def const_times_symbolic(A, X, i, j):
    return xor_bool(X[k][j] for k in range(N) if int(A[i][k]) & 1)


def symbolic_times_const(X, A, i, j):
    return xor_bool(X[i][k] for k in range(N) if int(A[k][j]) & 1)


def symbolic_times_symbolic(A, B, i, j):
    return xor_bool(z3.And(A[i][k], B[k][j]) for k in range(N))


def bool_matrix(model, M):
    return [
        [1 if z3.is_true(model.eval(M[i][j], model_completion=True)) else 0 for j in range(N)]
        for i in range(N)
    ]


def mm2(a, b):
    bt = list(zip(*b))
    return [
        [sum((int(x)&1)*(int(y)&1) for x,y in zip(row,col)) & 1 for col in bt]
        for row in a
    ]


def transpose(a):
    return [list(x) for x in zip(*a)]


def q_expr(row, diag, polar):
    terms = [row[k] for k in range(N) if diag[k]]
    for k in range(N):
        for ell in range(k + 1, N):
            if polar[k][ell]:
                terms.append(z3.And(row[k], row[ell]))
    return xor_bool(terms)


def b_expr(a, b, polar):
    return xor_bool(
        z3.And(a[k], b[ell])
        for k in range(N)
        for ell in range(N)
        if polar[k][ell]
    )


intr = runpy.run_path(str(INTRINSIC_SCRIPT))
ret = runpy.run_path(str(RETAINED_SCRIPT))
A12i = intr["A12"]
A13i = intr["A13"]
signs_i = intr["signs7"]
qdiag_i = intr["qdiag"]
polar_i = intr["polar"]
signs_r = ret["A_signs"]
A_cc = ret["A_cc"]
A_ct = ret["A_ct"]
if len(signs_i) != 7 or len(signs_r) != 7:
    raise SystemExit("seven-sign representation count regression")

quad = json.loads(QUADRATIC_PATH.read_text(encoding="utf-8"))
body = dict(quad); claimed = body.pop("canonical_sha256", None)
if claimed != EXPECTED_QUADRATIC or csha(body) != EXPECTED_QUADRATIC:
    raise SystemExit("retained quadratic source lock moved")
mods = [int(x) for x in quad["discriminant_moduli"]]
b8 = [[int(x) for x in row] for row in quad["discriminant_bilinear_numerator_over_8_reduced"]]
if mods != [2]*4 + [4]*6 + [8]*4:
    raise SystemExit("retained discriminant moduli regression")
scales = [m // 2 for m in mods]

def qret_bits(bits):
    vec = [scales[i] * ((bits >> i) & 1) for i in range(N)]
    val = sum(vec[i] * b8[i][j] * vec[j] for i in range(N) for j in range(N)) % 16
    if val not in (0, 8):
        raise SystemExit("retained A_T[2] quadratic restriction escaped F2")
    return val // 8
qdiag_r = [qret_bits(1 << i) for i in range(N)]
polar_r = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        polar_r[i][j] = qret_bits((1 << i) ^ (1 << j)) ^ qdiag_r[i] ^ qdiag_r[j]

S = [[z3.Bool(f"s_{i}_{j}") for j in range(N)] for i in range(N)]
T = [[z3.Bool(f"t_{i}_{j}") for j in range(N)] for i in range(N)]
X12 = [[z3.Bool(f"x12_{i}_{j}") for j in range(N)] for i in range(N)]
X13 = [[z3.Bool(f"x13_{i}_{j}") for j in range(N)] for i in range(N)]
solver = z3.Solver(); solver.set(timeout=300000)

# Named seven-sign equivariance: A_intrinsic * S = S * A_retained.
for Ai, Ar in zip(signs_i, signs_r):
    for i in range(N):
        for j in range(N):
            solver.add(const_times_symbolic(Ai, S, i, j) == symbolic_times_const(S, Ar, i, j))

# S is a genuine basis isomorphism.
for i in range(N):
    for j in range(N):
        solver.add(symbolic_times_symbolic(S, T, i, j) == z3.BoolVal(i == j))
        solver.add(symbolic_times_symbolic(T, S, i, j) == z3.BoolVal(i == j))

# S preserves the discriminant quadratic form. It is enough to check basis
# values and polar pairings.
for i in range(N):
    solver.add(q_expr(S[i], qdiag_r, polar_r) == z3.BoolVal(bool(qdiag_i[i])))
for i in range(N):
    for j in range(i + 1, N):
        solver.add(b_expr(S[i], S[j], polar_r) == z3.BoolVal(bool(polar_i[i][j])))

# Transport the actual swaps: A_intrinsic*S = S*X_retained.
for Ai, X in ((A12i, X12), (A13i, X13)):
    for i in range(N):
        for j in range(N):
            solver.add(const_times_symbolic(Ai, S, i, j) == symbolic_times_symbolic(S, X, i, j))

# Q-defined geometric swaps commute with the retained finite V4 Galois action.
for X in (X12, X13):
    for G in (A_cc, A_ct):
        for i in range(N):
            for j in range(N):
                left = symbolic_times_const(X, G, i, j)
                right = const_times_symbolic(G, X, i, j)
                solver.add(left == right)

status = solver.check()
if status != z3.sat:
    raise SystemExit(f"no exact intrinsic-to-retained A_T[2] transport: {status} {solver.reason_unknown()}")
model = solver.model()
S0 = bool_matrix(model, S)
T0 = bool_matrix(model, T)
X120 = bool_matrix(model, X12)
X130 = bool_matrix(model, X13)
I = [[int(i == j) for j in range(N)] for i in range(N)]
if mm2(S0, T0) != I or mm2(T0, S0) != I:
    raise SystemExit("model transport is not invertible")
if mm2(X120, X120) != I or mm2(X130, X130) != I:
    raise SystemExit("transported swap involution regression")
if mm2(mm2(X120, X130), X120) != mm2(mm2(X130, X120), X130):
    raise SystemExit("transported swap S3 braid regression")
for X in (X120, X130):
    if mm2(X, A_cc) != mm2(A_cc, X) or mm2(X, A_ct) != mm2(A_ct, X):
        raise SystemExit("transported Q-swap lost V4 commutation")

# Is the retained-basis swap pair independent of the possible sign/quadratic
# identification S? Ask for any second model with a different X12 or X13.
solver.push()
solver.add(z3.Or(*[
    X12[i][j] != z3.BoolVal(bool(X120[i][j]))
    for i in range(N) for j in range(N)
] + [
    X13[i][j] != z3.BoolVal(bool(X130[i][j]))
    for i in range(N) for j in range(N)
]))
second = solver.check()
if second == z3.unknown:
    raise SystemExit("swap-pair uniqueness SAT returned unknown: " + solver.reason_unknown())
unique_pair = second == z3.unsat
solver.pop()

out = {
    "schema": "STAGE33_07_INTRINSIC_TO_RETAINED_AT2_SWAP_TRANSPORT_V1",
    "transport": {
        "one_exact_quadratic_sign_equivariant_basis_isomorphism_14x14": S0,
        "inverse_14x14": T0,
        "seven_named_sign_actions_intertwined": True,
        "quadratic_form_isometry": True,
    },
    "actual_swaps_in_retained_at2_basis": {
        "swap12_action_14x14": X120,
        "swap13_action_14x14": X130,
        "both_commute_with_retained_cc_ct": True,
        "s3_relations_exact": True,
        "pair_unique_over_all_exact_sign_quadratic_transports": unique_pair,
    },
    "exact_consequence": {
        "actual_geometric_swap_pair_materialized_in_retained_at2_basis": True,
        "actual_pair_uniquely_identified_in_retained_basis": unique_pair,
        "finite_candidate_envelope_replaced_for_this_pair": unique_pair,
        "connecting_matrix_columns_explicitly_materialized": 0,
        "middle_gersten_module_action_materialized": False,
        "absolute_delta_loc_computed": False,
        "arithmetic_hs_closed": False,
    },
    "execution": {
        "z3_exact_boolean_solver_used": True,
        "remote_cas_used": False,
        "smith_recomputation_used": False,
    },
    "next_exact_leaf": (
        "induce the two retained-basis actual swaps on finite H1(V4,Br[2]) and impose their exact source/receiver naturality on the 26x16 extension map"
        if unique_pair else
        "add an exact marking invariant that distinguishes the remaining retained-basis transports before using swap naturality"
    ),
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "retained_basis_swap_pair_materialized": True,
    "retained_basis_swap_pair_unique": unique_pair,
    "certificate_sha256": out["canonical_sha256"],
    "next": out["next_exact_leaf"],
}, indent=2, sort_keys=True))
