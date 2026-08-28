#!/usr/bin/env python3
"""Strengthen intrinsic->retained A[2] transport by the mixed-order filtration.

In addition to seven named signs, named cc/ct, and the discriminant quadratic
form, require the transport to carry the canonical filtration
4A[8] subset 2A[4] subset A[2] to the retained Smith-coordinate filtration.
This is basis-independent information from the full mixed (2,4,8) discriminant
group and is strictly stronger than the previous A[2]-only marking.
"""
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

import z3

HERE = Path(__file__).resolve().parent
BASE_SCRIPT = HERE / "certify_intrinsic_to_retained_at2_swap_transport.py"
GALOIS_SCRIPT = HERE / "certify_actual_galois_at2_actions.py"
FILTRATION_SCRIPT = HERE / "certify_intrinsic_at2_divisibility_filtration.py"
OUT = HERE / "intrinsic-to-retained-at2-swap-transport-filtration.json"

base = runpy.run_path(str(BASE_SCRIPT))
gal = runpy.run_path(str(GALOIS_SCRIPT))
filt = runpy.run_path(str(FILTRATION_SCRIPT))

N = int(base["N"])
A12i, A13i = base["A12i"], base["A13i"]
signs_i, signs_r = base["signs_i"], base["signs_r"]
qdiag_i, polar_i = base["qdiag_i"], base["polar_i"]
qdiag_r, polar_r = base["qdiag_r"], base["polar_r"]
A_cc_r, A_ct_r = base["A_cc"], base["A_ct"]
A_cc_i, A_ct_i = gal["A_cc"], gal["A_ct"]
D2_basis = [int(x) for x in filt["D2_basis_masks"]]
D4_basis = [int(x) for x in filt["D4_basis_masks"]]

const_times_symbolic = base["const_times_symbolic"]
symbolic_times_const = base["symbolic_times_const"]
symbolic_times_symbolic = base["symbolic_times_symbolic"]
bool_matrix = base["bool_matrix"]
mm2 = base["mm2"]
q_expr = base["q_expr"]
b_expr = base["b_expr"]
xor_bool = base["xor_bool"]


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def symbolic_image_of_const_row(mask: int, S, j: int):
    return xor_bool(S[i][j] for i in range(N) if (int(mask) >> i) & 1)


S = [[z3.Bool(f"fs_{i}_{j}") for j in range(N)] for i in range(N)]
T = [[z3.Bool(f"ft_{i}_{j}") for j in range(N)] for i in range(N)]
X12 = [[z3.Bool(f"fx12_{i}_{j}") for j in range(N)] for i in range(N)]
X13 = [[z3.Bool(f"fx13_{i}_{j}") for j in range(N)] for i in range(N)]
solver = z3.Solver()
solver.set(timeout=300000)

# Seven named geometric signs and named arithmetic V4.
for Ai, Ar in zip(signs_i, signs_r):
    for i in range(N):
        for j in range(N):
            solver.add(const_times_symbolic(Ai, S, i, j) == symbolic_times_const(S, Ar, i, j))
for Gi, Gr in ((A_cc_i, A_cc_r), (A_ct_i, A_ct_r)):
    for i in range(N):
        for j in range(N):
            solver.add(const_times_symbolic(Gi, S, i, j) == symbolic_times_const(S, Gr, i, j))

# Invertible basis transport.
for i in range(N):
    for j in range(N):
        solver.add(symbolic_times_symbolic(S, T, i, j) == z3.BoolVal(i == j))
        solver.add(symbolic_times_symbolic(T, S, i, j) == z3.BoolVal(i == j))

# Quadratic isometry.
for i in range(N):
    solver.add(q_expr(S[i], qdiag_r, polar_r) == z3.BoolVal(bool(qdiag_i[i])))
for i in range(N):
    for j in range(i + 1, N):
        solver.add(b_expr(S[i], S[j], polar_r) == z3.BoolVal(bool(polar_i[i][j])))

# Canonical mixed-order divisibility filtration.  In the retained Smith model
# [2^4,4^6,8^4], 2A[4] is the last 10 coordinate span and 4A[8] the last 4.
# Dimensions agree intrinsically, so inclusion plus invertibility gives equality.
for row in D2_basis:
    for j in range(4):
        solver.add(symbolic_image_of_const_row(row, S, j) == z3.BoolVal(False))
for row in D4_basis:
    for j in range(10):
        solver.add(symbolic_image_of_const_row(row, S, j) == z3.BoolVal(False))

# Transport actual coordinate swaps.
for Ai, X in ((A12i, X12), (A13i, X13)):
    for i in range(N):
        for j in range(N):
            solver.add(const_times_symbolic(Ai, S, i, j) == symbolic_times_symbolic(S, X, i, j))

# Q-defined swaps commute with arithmetic V4 in retained coordinates.
for X in (X12, X13):
    for G in (A_cc_r, A_ct_r):
        for i in range(N):
            for j in range(N):
                solver.add(symbolic_times_const(X, G, i, j) == const_times_symbolic(G, X, i, j))

status = solver.check()
if status != z3.sat:
    raise SystemExit(f"no filtration-preserving intrinsic-to-retained transport: {status} {solver.reason_unknown()}")
model = solver.model()
S0, T0 = bool_matrix(model, S), bool_matrix(model, T)
X120, X130 = bool_matrix(model, X12), bool_matrix(model, X13)
I = [[int(i == j) for j in range(N)] for i in range(N)]
if mm2(S0, T0) != I or mm2(T0, S0) != I:
    raise SystemExit("filtration transport is not invertible")
if mm2(X120, X120) != I or mm2(X130, X130) != I:
    raise SystemExit("filtration-transported swaps lost involutivity")
if mm2(mm2(X120, X130), X120) != mm2(mm2(X130, X120), X130):
    raise SystemExit("filtration-transported swaps lost S3 braid")

# Check the concrete model really carries both intrinsic filtration pieces to
# the intended retained coordinate spans.
def image_row(mask: int, M: list[list[int]]) -> list[int]:
    return [sum(((mask >> i) & 1) * int(M[i][j]) for i in range(N)) & 1 for j in range(N)]
for row in D2_basis:
    if any(image_row(row, S0)[:4]):
        raise SystemExit("2A[4] concrete transport regression")
for row in D4_basis:
    if any(image_row(row, S0)[:10]):
        raise SystemExit("4A[8] concrete transport regression")

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
    raise SystemExit("filtration swap-pair uniqueness SAT returned unknown: " + solver.reason_unknown())
unique_pair = second == z3.unsat
solver.pop()

out = {
    "schema": "STAGE33_07_INTRINSIC_TO_RETAINED_AT2_SWAP_TRANSPORT_FILTRATION_V1",
    "source_locks": {
        "base_transport_certificate_sha256": base["out"]["canonical_sha256"],
        "actual_galois_at2_certificate_sha256": gal["out"]["canonical_sha256"],
        "intrinsic_divisibility_filtration_sha256": filt["out"]["canonical_sha256"],
    },
    "transport": {
        "one_exact_basis_isomorphism_14x14": S0,
        "inverse_14x14": T0,
        "seven_named_sign_actions_intertwined": True,
        "named_cc_ct_actions_intertwined": True,
        "quadratic_form_isometry": True,
        "two_A4_filtration_preserved": True,
        "four_A8_filtration_preserved": True,
    },
    "actual_swaps_in_retained_at2_basis": {
        "swap12_action_14x14": X120,
        "swap13_action_14x14": X130,
        "both_commute_with_retained_cc_ct": True,
        "s3_relations_exact": True,
        "pair_unique_after_mixed_order_filtration": unique_pair,
    },
    "exact_consequence": {
        "basis_independent_mixed_order_marking_used": True,
        "actual_geometric_swap_pair_materialized_in_retained_at2_basis": True,
        "actual_pair_uniquely_identified_in_retained_basis": unique_pair,
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
        "induce the unique actual swaps on finite H1(V4,Br[2]) and impose exact source/receiver naturality on the 26x16 extension map"
        if unique_pair else
        "mixed-order filtration still leaves swap ambiguity; classify the residual filtration-preserving transport centralizer before using swap naturality"
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
    "mixed_order_filtration_marking": True,
    "retained_basis_swap_pair_unique": unique_pair,
    "certificate_sha256": out["canonical_sha256"],
    "next": out["next_exact_leaf"],
}, indent=2, sort_keys=True))
