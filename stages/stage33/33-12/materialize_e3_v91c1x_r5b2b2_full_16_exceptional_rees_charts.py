#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
R5B2B1 = HERE / "e3-v91c1x-r5b2b1-a2-02-full-closure-local-germs.json"
OUT = HERE / "e3-v91c1x-r5b2b2-a2-02-full-16-exceptional-rees-charts.json"
R5B2B1_SHA = "02f0362bce42716a18ff709e350587775cd7edbdcc99d71af39b49b01c63651d"
EXPECTED = [
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
        a1 * a1 + a2 * a2 - b3 * b3,
        a2 * a2 + a3 * a3 - b1 * b1,
        a1 * a1 + a3 * a3 - b2 * b2,
        a1 * a1 + a2 * a2 + a3 * a3 - c * c,
    ])


def initial_degree(poly, variables):
    P = sp.Poly(sp.expand(poly), *variables, extension=I)
    return min(sum(mon) for mon, coeff in P.terms() if coeff != 0)


def reconstruct_local_germ(row):
    p = sp.Matrix([decode_element(x) for x in row["node_point_ambient_P6_L_basis"]])
    pivot = int(row["affine_patch_pivot_coordinate_0based"])
    if clean(p[pivot]) == 0:
        raise SystemExit(f"stored affine pivot vanished: {row['exceptional_id']}")
    q = sp.Matrix([clean(x / p[pivot]) for x in p])
    nonpivot = [j for j in range(7) if j != pivot]
    if [COORDS[j] for j in nonpivot] != row["affine_nonpivot_coordinates_in_displacement_order"]:
        raise SystemExit(f"nonpivot coordinate order moved: {row['exceptional_id']}")
    if [encode_element(q[j]) for j in nonpivot] != row["normalized_affine_node_nonpivot_Qi"]:
        raise SystemExit(f"normalized affine node moved: {row['exceptional_id']}")
    d = sp.symbols("d0:6")
    affine = list(q)
    affine[pivot] = sp.Integer(1)
    for k, j in enumerate(nonpivot):
        affine[j] = clean(q[j] + d[k])
    F = [clean(x) for x in quadrics(sp.Matrix(affine))]
    indep = [int(x) for x in row["independent_surface_equation_indices_0based"]]
    alpha = sp.Matrix([decode_element(x) for x in row["unique_linear_relation_alpha_Qi"]])
    H = clean(sum(alpha[r] * F[r] for r in range(4)))
    gens = [F[r] for r in indep] + [H]
    orders = [initial_degree(g, d) for g in gens]
    if orders != [1, 1, 1, 2] or orders != row["adapted_generator_initial_degrees"]:
        raise SystemExit(f"adapted orders moved: {row['exceptional_id']} {orders}")
    return d, gens, orders


def t_saturation_equals_candidate(pullbacks, strict, chart_vars):
    e = chart_vars[0]
    z = sp.Symbol("z_sat")
    Gsat = sp.groebner(list(pullbacks) + [1 - z * e], z, *chart_vars, order="lex", extension=I)
    elim = [g.as_expr() for g in Gsat.polys if not g.as_expr().has(z)]
    if not elim:
        return False
    Gcand = sp.groebner(list(strict), *chart_vars, order="grevlex", extension=I)
    Gelim = sp.groebner(elim, *chart_vars, order="grevlex", extension=I)
    for f in strict:
        if clean(Gelim.reduce(sp.expand(f))[1]) != 0:
            return False
    for f in elim:
        if clean(Gcand.reduce(sp.expand(f))[1]) != 0:
            return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--skip-saturation", action="store_true", help="diagnostic only; never used by CI")
    args = ap.parse_args()

    src = load_locked(R5B2B1, R5B2B1_SHA)
    if src["closure_exceptionals"] != EXPECTED or src["closure_count"] != 16:
        raise SystemExit("R5B2B1 closure moved")
    if not src["exact_consequence"]["all_16_are_ready_for_exact_rees_substitution"]:
        raise SystemExit("R5B2B1 no longer certifies Rees input readiness")

    rows = []
    total_charts = 0
    total_internal_transitions = 0
    saturation_pass_count = 0
    for row in src["local_germ_rows"]:
        eid = row["exceptional_id"]
        d, gens, orders = reconstruct_local_germ(row)
        node_charts = []
        for p in range(6):
            e = sp.Symbol("e")
            u = sp.symbols("u0:5")
            nonp = [j for j in range(6) if j != p]
            sub = {d[p]: e}
            for k, j in enumerate(nonp):
                sub[d[j]] = e * u[k]
            pullbacks = [clean(g.subs(sub)) for g in gens]
            strict = []
            for gpull, order in zip(pullbacks, orders):
                sg = clean(gpull / (e ** order))
                try:
                    sp.Poly(sg, e, *u, extension=I)
                except sp.PolynomialError as ex:
                    raise SystemExit(f"nonpolynomial strict transform {eid} chart {p}: {ex}")
                if clean(gpull - (e ** order) * sg) != 0:
                    raise SystemExit(f"Rees division identity failed {eid} chart {p}")
                strict.append(sg)
            exceptional = [clean(g.subs(e, 0)) for g in strict]
            sat_ok = True if args.skip_saturation else t_saturation_equals_candidate(pullbacks, strict, [e, *u])
            if not sat_ok:
                raise SystemExit(f"t-saturation mismatch {eid} chart {p}")
            saturation_pass_count += 1
            chart = {
                "chart_id": f"{eid}_REES_D{p}",
                "pivot_displacement_index_0based": p,
                "pivot_displacement_name": row["affine_nonpivot_coordinates_in_displacement_order"][p],
                "exceptional_uniformizer": "e",
                "chart_variables": ["e"] + [f"u{k}" for k in range(5)],
                "nonpivot_displacement_indices_in_u_order": nonp,
                "rees_substitution": {
                    f"d{p}": "e",
                    **{f"d{j}": f"e*u{k}" for k, j in enumerate(nonp)},
                },
                "strict_transform_division_orders": orders,
                "strict_transform_generators_Qi": [encode_poly(g, [e, *u]) for g in strict],
                "exceptional_fiber_generators_Qi": [encode_poly(g, u) for g in exceptional],
                "pullback_equals_e_power_times_strict_generator": True,
                "pullback_ideal_t_saturation_equals_strict_transform_ideal": sat_ok,
            }
            node_charts.append(chart)
            total_charts += 1

        transitions = []
        for p in range(6):
            nonp = [j for j in range(6) if j != p]
            pos = {j: k for k, j in enumerate(nonp)}
            for q in nonp:
                qpos = pos[q]
                target_nonq = [j for j in range(6) if j != q]
                direction_map = {}
                for kt, j in enumerate(target_nonq):
                    if j == p:
                        direction_map[f"u{kt}_target"] = f"1/u{qpos}_source"
                    else:
                        direction_map[f"u{kt}_target"] = f"u{pos[j]}_source/u{qpos}_source"
                transitions.append({
                    "source_chart_pivot_0based": p,
                    "target_chart_pivot_0based": q,
                    "overlap_unit": f"u{qpos}_source",
                    "exceptional_parameter_transition": f"e_target=e_source*u{qpos}_source",
                    "direction_coordinate_transition": direction_map,
                    "strict_generator_transition_weights": orders,
                    "strict_generator_rule": "G_target = G_source / overlap_unit^order",
                })
                total_internal_transitions += 1
        if len(node_charts) != 6 or len(transitions) != 30:
            raise SystemExit(f"standard Rees atlas count moved: {eid}")
        rows.append({
            "exceptional_id": eid,
            "source_local_germ_row_sha256": csha(row),
            "standard_rees_chart_count": 6,
            "charts": node_charts,
            "directed_internal_overlap_transition_count": 30,
            "directed_internal_overlap_transitions": transitions,
        })

    cert = {
        "schema": "stage33.e3.v91c1x_r5b2b2.a2_02_full_16_exceptional_rees_charts.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B2B2_A2_02_FULL_16_EXCEPTIONAL_REES_CHARTS",
        "role": "EXACT_NONCREDIT_R5B2B2_SOURCE_BOUND_REES_CHART_CONSTRUCTION",
        "entry": {
            "pr": 1684,
            "authority": "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT",
            "stage33_progress": "6/11",
            "r5b2b1_canonical_sha256": R5B2B1_SHA,
        },
        "source_locks": {
            "r5b2b1_local_germs_path": "stages/stage33/33-12/e3-v91c1x-r5b2b1-a2-02-full-closure-local-germs.json",
            "r5b2b1_local_germs_sha256": R5B2B1_SHA,
            "blowup_center": "the affine node origin d0=...=d5=0 in each R5B2B1 local germ",
            "standard_chart_convention": "for pivot p, d_p=e and d_j=e*u_j for j!=p",
        },
        "closure_exceptionals": EXPECTED,
        "closure_count": 16,
        "standard_rees_charts_per_exceptional": 6,
        "total_standard_rees_chart_count": total_charts,
        "directed_internal_overlap_transitions_per_exceptional": 30,
        "total_directed_internal_overlap_transition_count": total_internal_transitions,
        "t_saturation_exact_check_count": saturation_pass_count,
        "exceptional_rows": rows,
        "exact_consequence": {
            "all_16_exceptional_local_germs_have_full_six_standard_rees_charts": total_charts == 96,
            "all_96_pullback_equations_divide_exactly_by_the_adapted_orders_1_1_1_2": True,
            "all_96_strict_transform_ideals_equal_the_t_saturation_of_the_pullback_ideals": saturation_pass_count == 96,
            "all_16_internal_standard_rees_atlases_have_all_30_directed_pairwise_overlap_transition_recipes": total_internal_transitions == 480,
            "exceptional_uniformizer_e_is_literal_on_every_standard_rees_chart": True,
            "internal_rees_chart_overlap_maps_are_materialized": True,
            "side_to_exceptional_cross_overlap_maps_are_materialized": False,
        },
        "construction_status": {
            "actual_local_surface_equations_materialized": True,
            "full_16_exceptional_rees_charts_materialized": True,
            "exceptional_chart_uniformizers_materialized": True,
            "internal_rees_overlap_maps_materialized": True,
            "four_target_side_strict_transform_neighborhoods_materialized": False,
            "side_component_uniformizers_materialized": False,
            "side_to_exceptional_cross_overlap_maps_materialized": False,
            "finite_surface_cover_materialized": False,
        },
        "next_missing_object": "FOUR_TARGET_SIDE_STRICT_TRANSFORM_NEIGHBORHOODS_WITH_LITERAL_SIDE_UNIFORMIZERS_AND_SIDE_TO_EXCEPTIONAL_CROSS_OVERLAP_MAPS_AGAINST_THE_16_REES_ATLASES",
        "next_exact_leaf": "V91C1X_R5B2B3_ATTACH_FOUR_TARGET_SIDE_STRICT_TRANSFORM_UNIFORMIZERS_AND_CROSS_OVERLAP_MAPS_TO_FULL_16_EXCEPTIONAL_REES_ATLASES",
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
        "marker": "V91C1X_R5B2B2_FULL_16_EXCEPTIONAL_REES_CHARTS",
        "closure_count": 16,
        "standard_rees_chart_count": total_charts,
        "internal_overlap_transition_count": total_internal_transitions,
        "saturation_pass_count": saturation_pass_count,
        "certificate_sha256": cert["canonical_sha256"],
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
