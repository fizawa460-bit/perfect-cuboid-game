#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
EXC = S07 / "exceptional-p1-tangent-coordinates.json"
R5B2A = HERE / "e3-v91c1x-r5b2a-a2-02-target-side-incidence-closure.json"
OUT = HERE / "e3-v91c1x-r5b2b1-a2-02-full-closure-local-germs.json"
EXC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
R5B2A_SHA = "dc3c875eaa006f89386749e332e0e4559c2af0b0a4cb0fe9aa97aecbf0944534"
EXPECTED_CLOSURE = [
    "EXC_003", "EXC_004", "EXC_007", "EXC_008", "EXC_011", "EXC_012",
    "EXC_015", "EXC_016", "EXC_025", "EXC_026", "EXC_027", "EXC_028",
    "EXC_029", "EXC_030", "EXC_031", "EXC_032",
]
COORDS = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]
I = sp.I


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj["canonical_sha256"]
    body = dict(obj)
    body.pop("canonical_sha256")
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"source lock moved {path}: claimed={claimed} actual={actual} expected={expected}")
    return obj


def clean(x):
    return sp.cancel(sp.expand(x))


def decode_element(z):
    return sp.Rational(int(z[0]), int(z[1])) + I * sp.Rational(int(z[2]), int(z[3]))


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


def quadrics(v):
    a1, a2, a3, b1, b2, b3, c = list(v)
    return sp.Matrix([
        a1 * a1 + a2 * a2 - b3 * b3,
        a2 * a2 + a3 * a3 - b1 * b1,
        a1 * a1 + a3 * a3 - b2 * b2,
        a1 * a1 + a2 * a2 + a3 * a3 - c * c,
    ])


def independent_row_indices(M):
    chosen = []
    rank = 0
    for r in range(M.rows):
        candidate = M.extract(chosen + [r], range(M.cols))
        nr = candidate.rank()
        if nr > rank:
            chosen.append(r)
            rank = nr
    return chosen


def initial_degree(poly, variables):
    P = sp.Poly(sp.expand(poly), *variables, extension=I)
    return min(sum(mon) for mon, coeff in P.terms() if coeff != 0)


def tangent_quadratic_matrix(H, variables, K):
    subs = {variables[j]: sum(K[j, k] * sp.Symbol(f"u{k}") for k in range(3)) for j in range(6)}
    us = [sp.Symbol(f"u{k}") for k in range(3)]
    Q = sp.expand(H.subs(subs))
    G = sp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            G[r, c] = clean(sp.diff(sp.diff(Q, us[r]), us[c]) / 2)
    return G


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    exc = load_locked(EXC, EXC_SHA)
    r5b2a = load_locked(R5B2A, R5B2A_SHA)
    closure = r5b2a["side_incident_exceptional_closure"]
    if closure != EXPECTED_CLOSURE:
        raise SystemExit(f"R5B2A closure moved: {closure}")

    d = sp.symbols("d0:6")
    rows = []
    models = {x["exceptional_id"]: x for x in exc["exceptional_models"]}
    for eid in closure:
        er = models[eid]
        p = sp.Matrix([decode_element(x) for x in er["node_point_ambient_P6_L_basis"]])
        vals = quadrics(p)
        if any(clean(x) != 0 for x in vals):
            raise SystemExit(f"node escaped pinned quadrics: {eid}")
        pivot = next((j for j, x in enumerate(p) if clean(x) != 0), None)
        if pivot is None:
            raise SystemExit(f"zero projective node: {eid}")
        q = sp.Matrix([clean(x / p[pivot]) for x in p])
        nonpivot = [j for j in range(7) if j != pivot]
        affine = list(q)
        affine[pivot] = sp.Integer(1)
        for k, j in enumerate(nonpivot):
            affine[j] = clean(q[j] + d[k])
        F = [clean(x) for x in quadrics(sp.Matrix(affine))]
        if any(clean(f.subs({x: 0 for x in d})) != 0 for f in F):
            raise SystemExit(f"affine origin missed node: {eid}")
        J = sp.Matrix([[clean(sp.diff(F[r], d[c]).subs({x: 0 for x in d})) for c in range(6)] for r in range(4)])
        if J.rank() != 3:
            raise SystemExit(f"affine Jacobian rank regression {eid}: {J.rank()}")
        indep = independent_row_indices(J)
        if len(indep) != 3:
            raise SystemExit(f"failed to choose three independent linear generators: {eid}")
        alpha_space = J.T.nullspace()
        if len(alpha_space) != 1:
            raise SystemExit(f"unique linear relation failed: {eid}")
        alpha = alpha_space[0]
        alpha_pivot = next(x for x in alpha if clean(x) != 0)
        alpha = sp.Matrix([clean(x / alpha_pivot) for x in alpha])
        H = clean(sum(alpha[r] * F[r] for r in range(4)))
        orders = [initial_degree(F[r], d) for r in indep] + [initial_degree(H, d)]
        if orders != [1, 1, 1, 2]:
            raise SystemExit(f"adapted generator orders moved {eid}: {orders}")
        Kcols = J.extract(indep, range(6)).nullspace()
        if len(Kcols) != 3:
            raise SystemExit(f"tangent kernel dimension moved {eid}")
        K = sp.Matrix.hstack(*Kcols)
        G = tangent_quadratic_matrix(H, d, K)
        detG = clean(G.det())
        if detG == 0:
            raise SystemExit(f"ODP tangent quadratic degenerate {eid}")
        rows.append({
            "exceptional_id": eid,
            "node_point_ambient_P6_L_basis": er["node_point_ambient_P6_L_basis"],
            "source_tangent_model_sha256": er["full_tangent_conic_coordinate_model_sha256"],
            "affine_patch_pivot_coordinate_0based": pivot,
            "affine_patch_pivot_name": COORDS[pivot],
            "affine_nonpivot_coordinates_in_displacement_order": [COORDS[j] for j in nonpivot],
            "normalized_affine_node_nonpivot_Qi": encode_vector([q[j] for j in nonpivot]),
            "independent_surface_equation_indices_0based": indep,
            "unique_linear_relation_alpha_Qi": encode_vector(alpha),
            "adapted_generator_initial_degrees": orders,
            "tangent_kernel_dimension": 3,
            "adapted_quadratic_tangent_det_Qi": encode_element(detG),
            "actual_affine_surface_germ_recipe": {
                "dehomogenize": f"set {COORDS[pivot]}=1",
                "translate": "for the six nonpivot coordinates set x_j=q_j+d_j",
                "equations": ["F0=a1^2+a2^2-b3^2", "F1=a2^2+a3^2-b1^2", "F2=a1^2+a3^2-b2^2", "F3=a1^2+a2^2+a3^2-c^2"],
                "adapted_generators": "the three indexed F_i plus H=sum(alpha_i F_i)",
            },
            "rees_input_ready": True,
        })

    cert = {
        "schema": "stage33.e3.v91c1x_r5b2b1.a2_02_full_closure_local_germs.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B2B1_A2_02_FULL_CLOSURE_ACTUAL_LOCAL_SURFACE_GERMS",
        "role": "EXACT_NONCREDIT_R5B2B1_SOURCE_BOUND_LOCAL_GERM_CONSTRUCTION",
        "entry": {
            "pr": 1684,
            "authority": "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT",
            "stage33_progress": "6/11",
            "r5b2a_canonical_sha256": R5B2A_SHA,
        },
        "source_locks": {
            "exceptional_p1_tangent_coordinates_path": "stages/stage33/33-07/exceptional-p1-tangent-coordinates.json",
            "exceptional_p1_tangent_coordinates_sha256": EXC_SHA,
            "pinned_global_surface_quadrics": [
                "a1^2+a2^2-b3^2", "a2^2+a3^2-b1^2",
                "a1^2+a3^2-b2^2", "a1^2+a2^2+a3^2-c^2",
            ],
        },
        "closure_exceptionals": closure,
        "closure_count": len(closure),
        "local_germ_rows": rows,
        "exact_consequence": {
            "all_16_nodes_satisfy_pinned_surface_quadrics": True,
            "all_16_affine_jacobians_have_rank_3": True,
            "all_16_actual_affine_surface_germs_materialized_by_exact_dehomogenize_translate_recipe": True,
            "all_16_have_adapted_generator_orders_1_1_1_2": True,
            "all_16_have_nondegenerate_quadratic_on_three_dimensional_tangent_kernel": True,
            "all_16_are_ready_for_exact_rees_substitution": True,
            "tangent_model_only_source_gap_remains_for_the_16_exceptionals": False,
        },
        "construction_status": {
            "actual_local_surface_equations_materialized": True,
            "full_16_exceptional_rees_charts_materialized": False,
            "four_target_side_strict_transform_neighborhoods_materialized": False,
            "surface_uniformizers_materialized": False,
            "cross_overlap_maps_materialized": False,
        },
        "next_missing_object": "EXACT_REES_SUBSTITUTION_CHARTS_FOR_THE_16_ADAPTED_LOCAL_GERMS_WITH_EXCEPTIONAL_UNIFORMIZERS_THEN_FOUR_TARGET_SIDE_STRICT_TRANSFORM_NEIGHBORHOODS_AND_CROSS_OVERLAP_MAPS",
        "next_exact_leaf": "V91C1X_R5B2B2_MATERIALIZE_FULL_16_EXCEPTIONAL_REES_CHARTS_FROM_ADAPTED_LOCAL_GENERATORS",
        "credit_firewall": {
            "finite_surface_cover_credit": False,
            "h2_fixedness_credit": False,
            "mask20_credit": False,
            "source_bound_dim5_credit": False,
            "marked_brauer_image_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B2B1_FULL_CLOSURE_LOCAL_GERMS",
        "closure_count": len(rows),
        "all_rees_input_ready": all(x["rees_input_ready"] for x in rows),
        "certificate_sha256": cert["canonical_sha256"],
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
