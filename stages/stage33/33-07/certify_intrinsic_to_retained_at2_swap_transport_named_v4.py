#!/usr/bin/env python3
"""Strengthen intrinsic->retained A[2] transport by named Galois V4 equivariance.

The V1 transport used seven Q-geometric sign actions plus the quadratic form.
This V2 leaf additionally reconstructs the actual cc/ct actions intrinsically
from the retained 140-class source lock and requires the basis transport to
intertwine those named Galois generators themselves, not merely require the
transported coordinate swaps to commute with the retained V4.
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
OUT = HERE / "intrinsic-to-retained-at2-swap-transport-named-v4.json"

base = runpy.run_path(str(BASE_SCRIPT))
gal = runpy.run_path(str(GALOIS_SCRIPT))

N = int(base["N"])
A12i = base["A12i"]
A13i = base["A13i"]
signs_i = base["signs_i"]
signs_r = base["signs_r"]
qdiag_i = base["qdiag_i"]
polar_i = base["polar_i"]
qdiag_r = base["qdiag_r"]
polar_r = base["polar_r"]
A_cc_r = base["A_cc"]
A_ct_r = base["A_ct"]
A_cc_i = gal["A_cc"]
A_ct_i = gal["A_ct"]

const_times_symbolic = base["const_times_symbolic"]
symbolic_times_const = base["symbolic_times_const"]
symbolic_times_symbolic = base["symbolic_times_symbolic"]
bool_matrix = base["bool_matrix"]
mm2 = base["mm2"]
q_expr = base["q_expr"]
b_expr = base["b_expr"]


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


S = [[z3.Bool(f"v4s_{i}_{j}") for j in range(N)] for i in range(N)]
T = [[z3.Bool(f"v4t_{i}_{j}") for j in range(N)] for i in range(N)]
X12 = [[z3.Bool(f"v4x12_{i}_{j}") for j in range(N)] for i in range(N)]
X13 = [[z3.Bool(f"v4x13_{i}_{j}") for j in range(N)] for i in range(N)]
solver = z3.Solver()
solver.set(timeout=300000)

for Ai, Ar in zip(signs_i, signs_r):
    for i in range(N):
        for j in range(N):
            solver.add(
                const_times_symbolic(Ai, S, i, j)
                == symbolic_times_const(S, Ar, i, j)
            )

for Gi, Gr in ((A_cc_i, A_cc_r), (A_ct_i, A_ct_r)):
    for i in range(N):
        for j in range(N):
            solver.add(
                const_times_symbolic(Gi, S, i, j)
                == symbolic_times_const(S, Gr, i, j)
            )

for i in range(N):
    for j in range(N):
        solver.add(
            symbolic_times_symbolic(S, T, i, j) == z3.BoolVal(i == j)
        )
        solver.add(
            symbolic_times_symbolic(T, S, i, j) == z3.BoolVal(i == j)
        )

for i in range(N):
    solver.add(
        q_expr(S[i], qdiag_r, polar_r) == z3.BoolVal(bool(qdiag_i[i]))
    )
for i in range(N):
    for j in range(i + 1, N):
        solver.add(
            b_expr(S[i], S[j], polar_r)
            == z3.BoolVal(bool(polar_i[i][j]))
        )

for Ai, X in ((A12i, X12), (A13i, X13)):
    for i in range(N):
        for j in range(N):
            solver.add(
                const_times_symbolic(Ai, S, i, j)
                == symbolic_times_symbolic(S, X, i, j)
            )

for X in (X12, X13):
    for G in (A_cc_r, A_ct_r):
        for i in range(N):
            for j in range(N):
                solver.add(
                    symbolic_times_const(X, G, i, j)
                    == const_times_symbolic(G, X, i, j)
                )

status = solver.check()
if status != z3.sat:
    raise SystemExit(
        f"no named-V4 intrinsic-to-retained transport: {status} "
        f"{solver.reason_unknown()}"
    )

model = solver.model()
S0 = bool_matrix(model, S)
T0 = bool_matrix(model, T)
X120 = bool_matrix(model, X12)
X130 = bool_matrix(model, X13)
I = [[int(i == j) for j in range(N)] for i in range(N)]

if mm2(S0, T0) != I or mm2(T0, S0) != I:
    raise SystemExit("named-V4 transport is not invertible")
if mm2(X120, X120) != I or mm2(X130, X130) != I:
    raise SystemExit("named-V4 transported swaps lost involutivity")
if mm2(mm2(X120, X130), X120) != mm2(mm2(X130, X120), X130):
    raise SystemExit("named-V4 transported swaps lost S3 braid")
for Gi, Gr in ((A_cc_i, A_cc_r), (A_ct_i, A_ct_r)):
    if mm2(Gi, S0) != mm2(S0, Gr):
        raise SystemExit("named Galois intertwining regression")
for X in (X120, X130):
    if mm2(X, A_cc_r) != mm2(A_cc_r, X):
        raise SystemExit("swap lost retained cc commutation")
    if mm2(X, A_ct_r) != mm2(A_ct_r, X):
        raise SystemExit("swap lost retained ct commutation")

solver.push()
solver.add(
    z3.Or(
        *[
            X12[i][j] != z3.BoolVal(bool(X120[i][j]))
            for i in range(N)
            for j in range(N)
        ],
        *[
            X13[i][j] != z3.BoolVal(bool(X130[i][j]))
            for i in range(N)
            for j in range(N)
        ],
    )
)
second = solver.check()
if second == z3.unknown:
    raise SystemExit(
        "named-V4 swap-pair uniqueness SAT returned unknown: "
        + solver.reason_unknown()
    )
unique_pair = second == z3.unsat
solver.pop()

out = {
    "schema": "STAGE33_07_INTRINSIC_TO_RETAINED_AT2_SWAP_TRANSPORT_NAMED_V4_V1",
    "source_locks": {
        "galois_known_class_permutation_sha256": gal["perm_obj"]["canonical_sha256"],
        "actual_galois_at2_certificate_sha256": gal["out"]["canonical_sha256"],
        "base_transport_certificate_sha256": base["out"]["canonical_sha256"],
    },
    "transport": {
        "one_exact_basis_isomorphism_14x14": S0,
        "inverse_14x14": T0,
        "seven_named_sign_actions_intertwined": True,
        "named_cc_ct_actions_intertwined": True,
        "quadratic_form_isometry": True,
    },
    "actual_swaps_in_retained_at2_basis": {
        "swap12_action_14x14": X120,
        "swap13_action_14x14": X130,
        "both_commute_with_retained_cc_ct": True,
        "s3_relations_exact": True,
        "pair_unique_after_named_v4_marking": unique_pair,
    },
    "exact_consequence": {
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
        "actual_galois_picard_action_reconstructed_from_retained_140_class_marking": True,
    },
    "next_exact_leaf": (
        "induce the now-unique actual swaps on finite H1(V4,Br[2]) and impose exact source/receiver naturality on the 26x16 extension map"
        if unique_pair
        else
        "named cc/ct plus seven signs still leave transport ambiguity; add a further exact Picard marking invariant before using swap naturality"
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
    "named_v4_marking": True,
    "retained_basis_swap_pair_unique": unique_pair,
    "certificate_sha256": out["canonical_sha256"],
    "next": out["next_exact_leaf"],
}, indent=2, sort_keys=True))
