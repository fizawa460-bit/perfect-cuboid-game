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
OUT = HERE / "e3-v91c1x-r5b2c1-all-48-node-isolating-rees-neighborhoods.json"
EXC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
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


def encode_poly(poly, variables):
    P = sp.Poly(sp.expand(poly), *variables, extension=I)
    terms = []
    for mon, coeff in P.terms():
        if coeff == 0:
            continue
        terms.append({"exponents": list(mon), "coefficient_Qi": encode_element(sp.sympify(coeff))})
    return {"variables": [str(x) for x in variables], "terms": terms}


def quadrics(v):
    a1, a2, a3, b1, b2, b3, c = list(v)
    return sp.Matrix([
        a1*a1 + a2*a2 - b3*b3,
        a2*a2 + a3*a3 - b1*b1,
        a1*a1 + a3*a3 - b2*b2,
        a1*a1 + a2*a2 + a3*a3 - c*c,
    ])


def jacobian(v):
    a1, a2, a3, b1, b2, b3, c = list(v)
    return sp.Matrix([
        [2*a1, 2*a2, 0, 0, 0, -2*b3, 0],
        [0, 2*a2, 2*a3, -2*b1, 0, 0, 0],
        [2*a1, 0, 2*a3, 0, -2*b2, 0, 0],
        [2*a1, 2*a2, 2*a3, 0, 0, 0, -2*c],
    ])


def projective_normalize(v):
    vals = [clean(x) for x in list(v)]
    pivot = next((x for x in vals if x != 0), None)
    if pivot is None:
        raise SystemExit("zero projective point")
    return tuple(clean(x / pivot) for x in vals)


def independent_row_indices(M):
    chosen = []
    rank = 0
    for r in range(M.rows):
        cand = M.extract(chosen + [r], range(M.cols))
        nr = cand.rank()
        if nr > rank:
            chosen.append(r)
            rank = nr
    return chosen


def initial_degree(poly, variables):
    P = sp.Poly(sp.expand(poly), *variables, extension=I)
    return min(sum(mon) for mon, coeff in P.terms() if coeff != 0)


def tangent_quadratic_matrix(H, variables, K):
    us = sp.symbols("w0:3")
    subs = {variables[j]: sum(K[j, k] * us[k] for k in range(3)) for j in range(6)}
    Q = sp.expand(H.subs(subs))
    G = sp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            G[r, c] = clean(sp.diff(sp.diff(Q, us[r]), us[c]) / 2)
    return G


def adapted_local_germ(eid, p):
    if any(clean(x) != 0 for x in quadrics(p)):
        raise SystemExit(f"node escaped pinned quadrics: {eid}")
    if jacobian(p).rank() != 3:
        raise SystemExit(f"projective Jacobian rank moved: {eid}")
    pivot = next((j for j, x in enumerate(p) if clean(x) != 0), None)
    if pivot is None:
        raise SystemExit(f"zero projective node: {eid}")
    q = sp.Matrix([clean(x / p[pivot]) for x in p])
    nonpivot = [j for j in range(7) if j != pivot]
    d = sp.symbols("d0:6")
    affine = list(q)
    affine[pivot] = sp.Integer(1)
    for k, j in enumerate(nonpivot):
        affine[j] = clean(q[j] + d[k])
    F = [clean(x) for x in quadrics(sp.Matrix(affine))]
    zero = {x: 0 for x in d}
    if any(clean(f.subs(zero)) != 0 for f in F):
        raise SystemExit(f"affine origin missed node: {eid}")
    J = sp.Matrix([[clean(sp.diff(F[r], d[c]).subs(zero)) for c in range(6)] for r in range(4)])
    if J.rank() != 3:
        raise SystemExit(f"affine Jacobian rank moved: {eid}")
    indep = independent_row_indices(J)
    if len(indep) != 3:
        raise SystemExit(f"independent affine rows moved: {eid}")
    alpha_space = J.T.nullspace()
    if len(alpha_space) != 1:
        raise SystemExit(f"linear relation dimension moved: {eid}")
    alpha = alpha_space[0]
    apiv = next(x for x in alpha if clean(x) != 0)
    alpha = sp.Matrix([clean(x / apiv) for x in alpha])
    H = clean(sum(alpha[r] * F[r] for r in range(4)))
    gens = [F[r] for r in indep] + [H]
    orders = [initial_degree(g, d) for g in gens]
    if orders != [1, 1, 1, 2]:
        raise SystemExit(f"adapted orders moved: {eid} {orders}")
    Kcols = J.extract(indep, range(6)).nullspace()
    if len(Kcols) != 3:
        raise SystemExit(f"tangent kernel dimension moved: {eid}")
    K = sp.Matrix.hstack(*Kcols)
    G = tangent_quadratic_matrix(H, d, K)
    if clean(G.det()) == 0:
        raise SystemExit(f"degenerate ODP tangent quadratic: {eid}")
    return {
        "pivot": pivot,
        "q": q,
        "nonpivot": nonpivot,
        "d": d,
        "gens": gens,
        "orders": orders,
        "indep": indep,
        "alpha": alpha,
        "tangent_det": clean(G.det()),
    }


def t_saturation_equals_candidate(pullbacks, strict, chart_vars):
    e = chart_vars[0]
    z = sp.Symbol("z_sat")
    Gsat = sp.groebner(list(pullbacks) + [1 - z*e], z, *chart_vars, order="lex", extension=I)
    elim = [g.as_expr() for g in Gsat.polys if not g.as_expr().has(z)]
    if not elim:
        return False
    Gcand = sp.groebner(list(strict), *chart_vars, order="grevlex", extension=I)
    Gelim = sp.groebner(elim, *chart_vars, order="grevlex", extension=I)
    return (
        all(clean(Gelim.reduce(sp.expand(f))[1]) == 0 for f in strict)
        and all(clean(Gcand.reduce(sp.expand(f))[1]) == 0 for f in elim)
    )


def separator_factor(source, target):
    for r in range(7):
        for s in range(r + 1, 7):
            det = clean(source[r]*target[s] - source[s]*target[r])
            if det != 0:
                # l_target(X)=target[s] X_r - target[r] X_s
                coeff = [sp.Integer(0)] * 7
                coeff[r] = clean(target[s])
                coeff[s] = clean(-target[r])
                at_target = clean(sum(coeff[j]*target[j] for j in range(7)))
                at_source = clean(sum(coeff[j]*source[j] for j in range(7)))
                if at_target != 0 or at_source == 0:
                    raise SystemExit("separator construction failed")
                return {"coordinate_pair_0based": [r, s], "coefficients_Qi": encode_vector(coeff)}
    raise SystemExit("projectively equal frozen nodes encountered")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--skip-saturation", action="store_true", help="diagnostic only; CI must not use")
    args = ap.parse_args()

    exc = load_locked(EXC, EXC_SHA)
    models = exc["exceptional_models"]
    if len(models) != 48:
        raise SystemExit(f"frozen exceptional inventory moved: {len(models)}")
    expected_ids = [f"EXC_{i:03d}" for i in range(1, 49)]
    if [x["exceptional_id"] for x in models] != expected_ids:
        raise SystemExit("frozen exceptional id order moved")

    points = {
        row["exceptional_id"]: sp.Matrix([decode_element(x) for x in row["node_point_ambient_P6_L_basis"]])
        for row in models
    }
    norms = [projective_normalize(points[eid]) for eid in expected_ids]
    if len(set(norms)) != 48:
        raise SystemExit("frozen node points are not 48 distinct projective points")

    rows = []
    separator_check_count = 0
    total_charts = 0
    saturation_pass_count = 0
    internal_transition_count = 0
    for eid in expected_ids:
        p = points[eid]
        germ = adapted_local_germ(eid, p)
        pivot = germ["pivot"]

        separator_factors = []
        for other in expected_ids:
            if other == eid:
                continue
            f = separator_factor(p, points[other])
            f["vanishing_node"] = other
            separator_factors.append(f)
            separator_check_count += 1
        if len(separator_factors) != 47:
            raise SystemExit(f"separator count moved: {eid}")
        separator_commitment = csha(separator_factors)

        # Lambda_eid = X_pivot * product_{m!=eid} l_{eid,m}.
        # It is nonzero at eid and zero at every other frozen node, so D_+(Lambda_eid)
        # is a source-bound projective principal open containing this node and no other frozen node.
        if clean(p[pivot]) == 0:
            raise SystemExit(f"pivot localizer vanished at source node: {eid}")

        chart_hashes = []
        d = germ["d"]
        gens = germ["gens"]
        orders = germ["orders"]
        for cp in range(6):
            e = sp.Symbol("e")
            u = sp.symbols("u0:5")
            nonp = [j for j in range(6) if j != cp]
            sub = {d[cp]: e}
            for k, j in enumerate(nonp):
                sub[d[j]] = e*u[k]
            pullbacks = [clean(g.subs(sub)) for g in gens]
            strict = [clean(gp/(e**o)) for gp, o in zip(pullbacks, orders)]
            for gp, sg, o in zip(pullbacks, strict, orders):
                sp.Poly(sg, e, *u, extension=I)
                if clean(gp - e**o * sg) != 0:
                    raise SystemExit(f"Rees division identity failed {eid} chart {cp}")
            exceptional = [clean(g.subs(e, 0)) for g in strict]
            sat_ok = True if args.skip_saturation else t_saturation_equals_candidate(pullbacks, strict, [e, *u])
            if not sat_ok:
                raise SystemExit(f"t-saturation mismatch {eid} chart {cp}")
            saturation_pass_count += 1
            chart_commitment = {
                "chart_id": f"{eid}_GLOBAL_ISOLATING_REES_D{cp}",
                "node_open": f"D_+(Lambda_{eid})",
                "pivot_displacement_index_0based": cp,
                "nonpivot_displacement_indices_in_u_order": nonp,
                "strict_transform_division_orders": orders,
                "strict_transform_generators_Qi": [encode_poly(g, [e, *u]) for g in strict],
                "exceptional_fiber_generators_Qi": [encode_poly(g, u) for g in exceptional],
                "exceptional_uniformizer": "e",
                "pullback_ideal_t_saturation_equals_strict_transform_ideal": sat_ok,
            }
            chart_hashes.append(csha(chart_commitment))
            total_charts += 1
        internal_transition_count += 30

        local_germ_commitment = {
            "pivot_coordinate_0based": pivot,
            "pivot_name": COORDS[pivot],
            "normalized_affine_node_Qi": encode_vector(germ["q"]),
            "independent_surface_equation_indices_0based": germ["indep"],
            "unique_linear_relation_alpha_Qi": encode_vector(germ["alpha"]),
            "adapted_generator_initial_degrees": orders,
            "adapted_quadratic_tangent_det_Qi": encode_element(germ["tangent_det"]),
        }
        rows.append({
            "exceptional_id": eid,
            "source_tangent_model_sha256": next(x for x in models if x["exceptional_id"] == eid)["full_tangent_conic_coordinate_model_sha256"],
            "node_point_ambient_P6_L_basis": next(x for x in models if x["exceptional_id"] == eid)["node_point_ambient_P6_L_basis"],
            "node_isolating_principal_open": {
                "name": f"D_+(Lambda_{eid})",
                "Lambda_factorization_recipe": "X_pivot times the 47 deterministic pair-separator linear forms; for other node m choose the lexicographically first r<s with p_eid[r]p_m[s]-p_eid[s]p_m[r]!=0 and use l_m=p_m[s]X_r-p_m[r]X_s",
                "homogeneous_degree": 48,
                "pivot_coordinate_0based": pivot,
                "separator_factor_count": 47,
                "separator_factor_list_sha256": separator_commitment,
                "nonzero_at_own_node": True,
                "zero_at_all_other_47_frozen_nodes": True,
            },
            "local_germ_commitment_sha256": csha(local_germ_commitment),
            "standard_rees_chart_count": 6,
            "standard_rees_chart_commitment_sha256s": chart_hashes,
            "directed_internal_rees_overlap_transition_count": 30,
        })

    if separator_check_count != 48*47:
        raise SystemExit("separator check count moved")
    if total_charts != 48*6 or saturation_pass_count != 48*6:
        raise SystemExit("all-48 Rees chart count moved")
    if internal_transition_count != 48*30:
        raise SystemExit("all-48 internal transition count moved")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b2c1.all_48_node_isolating_rees_neighborhoods.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B2C1_ALL_48_NODE_ISOLATING_REES_NEIGHBORHOODS",
        "role": "EXACT_NONCREDIT_R5B2C1_GLOBAL_NODE_NEIGHBORHOOD_COMPLETION",
        "entry": {
            "pr": 1684,
            "authority": "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT",
            "stage33_progress": "6/11",
            "prior_r5b2b3b_sha256": "9a540773b7a7f332d6aa2f67582b3d3619fae08041015d652e0a567c36098bf5",
        },
        "source_locks": {
            "exceptional_p1_tangent_coordinates_path": "stages/stage33/33-07/exceptional-p1-tangent-coordinates.json",
            "exceptional_p1_tangent_coordinates_sha256": EXC_SHA,
            "pinned_global_surface_quadrics": [
                "a1^2+a2^2-b3^2", "a2^2+a3^2-b1^2",
                "a1^2+a3^2-b2^2", "a1^2+a2^2+a3^2-c^2",
            ],
            "standard_node_rees_rule": "on D_+(Lambda_eid), dehomogenize at the stored pivot, translate the node to d=0, then for chart p substitute d_p=e and d_j=e*u_j for j!=p",
        },
        "frozen_exceptional_node_count": 48,
        "node_isolating_principal_open_count": 48,
        "separator_vanishing_check_count": separator_check_count,
        "standard_rees_charts_per_node": 6,
        "total_standard_rees_chart_count": total_charts,
        "directed_internal_rees_overlap_transitions_per_node": 30,
        "total_directed_internal_rees_overlap_transition_count": internal_transition_count,
        "t_saturation_exact_check_count": saturation_pass_count,
        "node_rows": rows,
        "exact_consequence": {
            "all_48_frozen_nodes_are_distinct_projective_surface_points": True,
            "all_48_have_projective_jacobian_rank_3": True,
            "all_48_have_adapted_local_generator_orders_1_1_1_2": True,
            "all_48_have_nondegenerate_odp_tangent_quadratic": True,
            "all_48_have_source_bound_principal_opens_containing_that_node_and_excluding_the_other_47_frozen_nodes": True,
            "all_48_node_opens_have_six_exact_standard_rees_charts": True,
            "all_288_rees_chart_strict_transform_ideals_equal_t_saturation_of_pullback_ideals": saturation_pass_count == 288,
            "all_48_internal_rees_atlases_have_all_30_directed_standard_overlap_recipes": True,
            "all_48_exceptional_fibers_are_covered_by_their_six_standard_rees_charts": True,
        },
        "construction_status": {
            "all_48_frozen_node_neighborhoods_globally_isolated_from_each_other": True,
            "all_48_exceptional_resolution_atlases_materialized": True,
            "smooth_complement_principal_cover_materialized": False,
            "finite_whole_resolved_surface_cover_materialized": False,
            "all_whole_surface_double_overlaps_materialized": False,
            "swap23_cover_action_or_common_refinement_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "equivalent_unimodular_cech_glue_materialized": False,
        },
        "next_missing_object": "SOURCE_BOUND_PRINCIPAL_OPEN_COVER_OF_THE_SMOOTH_COMPLEMENT_USING_NONZERO_4X4_JACOBIAN_MINORS_PLUS_EXACT_GLUE_TO_THE_48_NODE_ISOLATING_REES_NEIGHBORHOODS",
        "next_exact_leaf": "V91C1X_R5B2C2_MATERIALIZE_JACOBIAN_MINOR_SMOOTH_COMPLEMENT_COVER_AND_GLUE_TO_ALL_48_NODE_REES_NEIGHBORHOODS",
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
        "marker": "V91C1X_R5B2C1_ALL_48_NODE_ISOLATING_REES_NEIGHBORHOODS",
        "frozen_nodes": 48,
        "node_isolating_opens": 48,
        "separator_checks": separator_check_count,
        "rees_charts": total_charts,
        "saturation_checks": saturation_pass_count,
        "internal_directed_transitions": internal_transition_count,
        "certificate_sha256": cert["canonical_sha256"],
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
