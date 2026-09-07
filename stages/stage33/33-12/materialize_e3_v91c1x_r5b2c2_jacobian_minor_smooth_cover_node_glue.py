#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
EXC = S07 / "exceptional-p1-tangent-coordinates.json"
C1 = HERE / "e3-v91c1x-r5b2c1-all-48-node-isolating-rees-neighborhoods.json"
OUT = HERE / "e3-v91c1x-r5b2c2-jacobian-minor-smooth-cover-node-glue.json"
EXC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
C1_SHA = "b0bb861bda9c3066a63cc471940d59bcd1cf172ee0322c2a7448a51f9ab9b133"
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
        a1*a1 + a2*a2 - b3*b3,
        a2*a2 + a3*a3 - b1*b1,
        a1*a1 + a3*a3 - b2*b2,
        a1*a1 + a2*a2 + a3*a3 - c*c,
    ])


def reduced_jacobian(v):
    a1, a2, a3, b1, b2, b3, c = list(v)
    return sp.Matrix([
        [a1, a2, 0, 0, 0, -b3, 0],
        [0, a2, a3, -b1, 0, 0, 0],
        [a1, 0, a3, 0, -b2, 0, 0],
        [a1, a2, a3, 0, 0, 0, -c],
    ])


def projective_normalize(v):
    vals = [clean(x) for x in list(v)]
    pivot = next((x for x in vals if x != 0), None)
    if pivot is None:
        raise SystemExit("zero projective point")
    return tuple(clean(x / pivot) for x in vals)


def support_rank(pattern):
    return int(reduced_jacobian(sp.Matrix(pattern)).rank())


def square_forms():
    x, y, z = sp.symbols("x y z")
    return (x, y, z), [x, y, z, y+z, x+z, x+y, x+y+z]


def feasible_support(pattern):
    xyz, forms = square_forms()
    zero_forms = [forms[i] for i, bit in enumerate(pattern) if bit == 0]
    nonzero_forms = [forms[i] for i, bit in enumerate(pattern) if bit == 1]
    if zero_forms:
        A, _ = sp.linear_eq_to_matrix(zero_forms, xyz)
    else:
        A = sp.zeros(0, 3)
    ns = A.nullspace()
    if not ns:
        return None
    # Over Q(i), finitely many proper hyperplanes cannot cover a vector space.
    # Thus a support is feasible exactly when no requested-nonzero square form
    # vanishes identically on the zero-constraint nullspace.
    for f in nonzero_forms:
        coeff = sp.Matrix([sp.diff(f, q) for q in xyz])
        if all(clean(coeff.dot(v)) == 0 for v in ns):
            return None
    return ns


def qi_roots(q):
    q = clean(q)
    if q == 0:
        return [sp.Integer(0)]
    if q == 1:
        return [sp.Integer(1), sp.Integer(-1)]
    if q == -1:
        return [I, -I]
    raise SystemExit(f"unexpected normalized square value {q}")


def enumerate_pattern_points(pattern, ns):
    if len(ns) != 1:
        raise SystemExit(f"singular support nullity not one: {pattern} dim={len(ns)}")
    xyz, forms = square_forms()
    q = [clean(x) for x in ns[0]]
    ai_pivot = next((j for j in range(3) if pattern[j]), None)
    if ai_pivot is None or q[ai_pivot] == 0:
        raise SystemExit(f"singular support has no valid a-pivot: {pattern}")
    q = [clean(v / q[ai_pivot]) for v in q]
    vals = {xyz[0]: q[0], xyz[1]: q[1], xyz[2]: q[2]}
    sq = [clean(f.subs(vals)) for f in forms]
    if any((sq[j] == 0) != (pattern[j] == 0) for j in range(7)):
        raise SystemExit(f"support/square mismatch: {pattern} squares={sq}")

    choices = []
    for j, s in enumerate(sq):
        roots = qi_roots(s)
        if j == ai_pivot:
            roots = [sp.Integer(1)]
        choices.append(roots)

    out = []
    for tuple_values in itertools.product(*choices):
        p = sp.Matrix(tuple_values)
        if any(clean(x) != 0 for x in quadrics(p)):
            raise SystemExit(f"enumerated singular point escaped surface: {pattern} {tuple_values}")
        if reduced_jacobian(p).rank() >= 4:
            raise SystemExit(f"enumerated support point not singular: {pattern} {tuple_values}")
        out.append(projective_normalize(p))
    return sorted(set(out), key=lambda t: tuple(str(x) for x in t))


def singular_support_enumeration():
    rows = []
    points = []
    examined = 0
    for pattern in itertools.product([0, 1], repeat=7):
        if not any(pattern):
            continue
        examined += 1
        rank = support_rank(pattern)
        if rank >= 4:
            continue
        ns = feasible_support(pattern)
        if ns is None:
            continue
        pat_points = enumerate_pattern_points(pattern, ns)
        rows.append({
            "support_bits_coordinate_order": list(pattern),
            "support_coordinate_names": [COORDS[j] for j, bit in enumerate(pattern) if bit],
            "reduced_jacobian_rank": rank,
            "square_constraint_nullity": len(ns),
            "projective_point_count": len(pat_points),
            "projective_points_commitment_sha256": csha([[str(x) for x in p] for p in pat_points]),
        })
        points.extend(pat_points)
    points = sorted(set(points), key=lambda t: tuple(str(x) for x in t))
    return examined, rows, points


def nonzero_jacobian_minors():
    X = sp.symbols("a1 a2 a3 b1 b2 b3 c")
    J = reduced_jacobian(sp.Matrix(X))
    rows = []
    polys = []
    for cols in itertools.combinations(range(7), 4):
        det = clean(J[:, list(cols)].det())
        if det == 0:
            continue
        mid = "M_" + "_".join(str(j) for j in cols)
        row = {
            "minor_id": mid,
            "column_indices_0based": list(cols),
            "column_names": [COORDS[j] for j in cols],
            "reduced_minor_Q": encode_poly(det, X),
            "principal_open": f"D_+({mid})",
        }
        rows.append(row)
        polys.append((mid, det))
    return X, rows, polys


def node_chart_data(node):
    p = sp.Matrix([decode_element(x) for x in node["node_point_ambient_P6_L_basis"]])
    pivot = next((j for j, x in enumerate(p) if clean(x) != 0), None)
    if pivot is None:
        raise SystemExit(f"zero node {node['exceptional_id']}")
    q = sp.Matrix([clean(x / p[pivot]) for x in p])
    nonpivot = [j for j in range(7) if j != pivot]
    d = sp.symbols("d0:6")
    affine = list(q)
    affine[pivot] = sp.Integer(1)
    for k, j in enumerate(nonpivot):
        affine[j] = clean(q[j] + d[k])
    return pivot, q, nonpivot, d, sp.Matrix(affine)


def chart_blowdown_and_inverse(node, cp, minor_polys):
    pivot, q, nonpivot, d, affine = node_chart_data(node)
    e = sp.Symbol("e")
    u = sp.symbols("u0:5")
    nonp = [j for j in range(6) if j != cp]
    sub = {d[cp]: e}
    for k, j in enumerate(nonp):
        sub[d[j]] = e*u[k]
    blow = sp.Matrix([clean(x.subs(sub)) for x in affine])

    d_from_blow = [clean(blow[nonpivot[k]] - q[nonpivot[k]]) for k in range(6)]
    if clean(d_from_blow[cp] - e) != 0:
        raise SystemExit(f"blowdown inverse e roundtrip failed {node['exceptional_id']} cp={cp}")
    for k, j in enumerate(nonp):
        if clean(d_from_blow[j] / e - u[k]) != 0:
            raise SystemExit(f"blowdown inverse u roundtrip failed {node['exceptional_id']} cp={cp} u={k}")

    X = sp.symbols("a1 a2 a3 b1 b2 b3 c")
    pullbacks = []
    for mid, poly in minor_polys:
        val = clean(poly.subs({X[j]: blow[j] for j in range(7)}))
        if val == 0:
            raise SystemExit(f"Jacobian minor pullback vanished identically {node['exceptional_id']} cp={cp} {mid}")
        pullbacks.append({
            "minor_id": mid,
            "pullback_Qi": encode_poly(val, [e, *u]),
            "overlap_condition": f"e!=0 and pullback({mid})!=0",
        })

    inverse_recipe = {
        "node_affine_pivot_coordinate_0based": pivot,
        "node_affine_pivot_name": COORDS[pivot],
        "rees_displacement_pivot_0based": cp,
        "blowdown_affine_coordinates_Qi": [encode_poly(x, [e, *u]) for x in blow],
        "inverse_on_e_nonzero": {
            "d_k": "x_nonpivot[k]-q_nonpivot[k]",
            "e": f"d{cp}",
            "u_order_displacement_indices": nonp,
            "u_k": "d_j/e in the displayed displacement order",
        },
        "exact_roundtrip_verified": True,
    }
    return csha(inverse_recipe), csha(pullbacks)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    exc = load_locked(EXC, EXC_SHA)
    c1 = load_locked(C1, C1_SHA)
    models = exc["exceptional_models"]
    if len(models) != 48:
        raise SystemExit("frozen exceptional inventory moved")
    if c1["frozen_exceptional_node_count"] != 48 or c1["total_standard_rees_chart_count"] != 288:
        raise SystemExit("R5B2C1 count lock moved")

    examined, singular_rows, singular_points = singular_support_enumeration()
    if examined != 127:
        raise SystemExit(f"support enumeration count moved: {examined}")
    if len(singular_rows) != 6:
        raise SystemExit(f"singular support family count moved: {len(singular_rows)}")
    if [r["projective_point_count"] for r in singular_rows] != [8]*6:
        raise SystemExit("singular support point counts moved")
    if len(singular_points) != 48:
        raise SystemExit(f"singular point count moved: {len(singular_points)}")

    frozen_points = sorted(
        {
            projective_normalize(sp.Matrix([decode_element(x) for x in row["node_point_ambient_P6_L_basis"]]))
            for row in models
        },
        key=lambda t: tuple(str(x) for x in t),
    )
    if singular_points != frozen_points:
        raise SystemExit("exact singular-locus enumeration does not equal frozen 48-node inventory")

    X, minor_rows, minor_polys = nonzero_jacobian_minors()
    if len(minor_rows) != 29:
        raise SystemExit(f"nonzero 4x4 Jacobian minor count moved: {len(minor_rows)}")
    for p in frozen_points:
        subs = {X[j]: p[j] for j in range(7)}
        if any(clean(poly.subs(subs)) != 0 for _mid, poly in minor_polys):
            raise SystemExit("Jacobian-minor cover leaked onto a frozen singular point")

    chart_rows = []
    cross_overlap_count = 0
    directed_cross_transition_count = 0
    for node in models:
        chart_commitments = []
        for cp in range(6):
            map_sha, pullback_sha = chart_blowdown_and_inverse(node, cp, minor_polys)
            chart_commitments.append({
                "chart_id": f"{node['exceptional_id']}_GLOBAL_ISOLATING_REES_D{cp}",
                "blowdown_inverse_map_commitment_sha256": map_sha,
                "29_smooth_minor_pullbacks_commitment_sha256": pullback_sha,
                "smooth_minor_overlap_count": 29,
                "directed_smooth_rees_transition_count": 58,
            })
            cross_overlap_count += 29
            directed_cross_transition_count += 58
        chart_rows.append({
            "exceptional_id": node["exceptional_id"],
            "standard_rees_chart_count": 6,
            "chart_glue_commitments": chart_commitments,
        })

    if cross_overlap_count != 288*29 or directed_cross_transition_count != 2*288*29:
        raise SystemExit("smooth/Rees cross-overlap count moved")

    smooth_directed_overlap_count = 29*28
    prior_internal_rees_directed = int(c1["total_directed_internal_rees_overlap_transition_count"])

    cert = {
        "schema": "stage33.e3.v91c1x_r5b2c2.jacobian_minor_smooth_cover_node_glue.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B2C2_JACOBIAN_MINOR_SMOOTH_COMPLEMENT_COVER_AND_48_NODE_REES_GLUE",
        "role": "EXACT_NONCREDIT_R5B2C2_FINITE_WHOLE_RESOLVED_SURFACE_COVER_CONSTRUCTION",
        "entry": {
            "pr": 1684,
            "authority": "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT",
            "stage33_progress": "6/11",
            "r5b2c1_canonical_sha256": C1_SHA,
        },
        "source_locks": {
            "exceptional_p1_tangent_coordinates_path": "stages/stage33/33-07/exceptional-p1-tangent-coordinates.json",
            "exceptional_p1_tangent_coordinates_sha256": EXC_SHA,
            "r5b2c1_path": "stages/stage33/33-12/e3-v91c1x-r5b2c1-all-48-node-isolating-rees-neighborhoods.json",
            "r5b2c1_sha256": C1_SHA,
            "pinned_global_surface_quadrics": [
                "a1^2+a2^2-b3^2", "a2^2+a3^2-b1^2",
                "a1^2+a3^2-b2^2", "a1^2+a2^2+a3^2-c^2",
            ],
            "reduced_jacobian": [
                ["a1","a2","0","0","0","-b3","0"],
                ["0","a2","a3","-b1","0","0","0"],
                ["a1","0","a3","0","-b2","0","0"],
                ["a1","a2","a3","0","0","0","-c"],
            ],
        },
        "singular_locus_exact_enumeration": {
            "nonzero_coordinate_support_patterns_examined": examined,
            "rank_deficient_surface_compatible_support_pattern_count": len(singular_rows),
            "support_rows": singular_rows,
            "enumerated_projective_singular_point_count": len(singular_points),
            "enumerated_singular_points_commitment_sha256": csha([[str(x) for x in p] for p in singular_points]),
            "equals_frozen_48_node_inventory_exactly": True,
        },
        "smooth_complement_cover": {
            "all_4x4_column_subsets": 35,
            "identically_zero_reduced_minor_count": 6,
            "nonzero_reduced_minor_count": 29,
            "minor_rows": minor_rows,
            "smooth_complement_is_union_of_29_principal_minor_opens": True,
            "directed_smooth_smooth_identity_overlap_transition_count": smooth_directed_overlap_count,
            "smooth_smooth_transition_rule": "identity on the original projective surface, restricted to D_+(M_i M_j)",
        },
        "node_rees_glue": {
            "node_count": 48,
            "rees_chart_count": 288,
            "chart_rows": chart_rows,
            "smooth_rees_overlap_count": cross_overlap_count,
            "directed_smooth_rees_transition_count": directed_cross_transition_count,
            "overlap_rule": "on each standard Rees chart, restrict to e!=0 and pullback(M)!=0; blow down by the exact affine Rees substitution and invert by d=x-q, e=d_p, u=d/e",
            "all_288_blowdown_inverse_roundtrips_verified": True,
            "prior_same_node_directed_internal_rees_transition_count": prior_internal_rees_directed,
        },
        "finite_cover": {
            "smooth_minor_chart_count": 29,
            "node_rees_chart_count": 288,
            "total_cover_chart_count": 317,
            "whole_resolved_surface_is_covered": True,
            "reason": "away from the exceptional fibers the blowup is isomorphic to the original surface minus its exact 48-point singular locus, covered by the 29 Jacobian-minor opens; the 48 exceptional fibers are covered by the 288 R5B2C1 standard Rees charts",
        },
        "construction_status": {
            "smooth_complement_principal_cover_materialized": True,
            "exact_singular_locus_equals_frozen_48_nodes": True,
            "smooth_to_rees_glue_materialized": True,
            "finite_whole_resolved_surface_cover_materialized": True,
            "all_whole_surface_double_overlaps_materialized": False,
            "cross_node_rees_to_rees_overlap_transitions_materialized": False,
            "swap23_cover_action_or_common_refinement_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "equivalent_unimodular_cech_glue_materialized": False,
        },
        "next_missing_object": "COMPLETE_COVER_INDEXED_ALL_DOUBLE_OVERLAP_TRANSITION_ATLAS_FOR_THE_317_CHART_FINITE_RESOLVED_SURFACE_COVER_INCLUDING_CROSS_NODE_REES_TO_REES_OVERLAPS_THEN_SWAP23_COMMON_REFINEMENT",
        "next_exact_leaf": "V91C1X_R5B2C3_MATERIALIZE_ALL_DOUBLE_OVERLAPS_FOR_THE_317_CHART_FINITE_SURFACE_COVER",
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
        "marker": "V91C1X_R5B2C2_JACOBIAN_MINOR_SMOOTH_COMPLEMENT_COVER_AND_48_NODE_REES_GLUE",
        "singular_support_patterns": len(singular_rows),
        "singular_points": len(singular_points),
        "smooth_minor_charts": len(minor_rows),
        "node_rees_charts": 288,
        "finite_cover_charts": 317,
        "smooth_rees_overlaps": cross_overlap_count,
        "directed_smooth_rees_transitions": directed_cross_transition_count,
        "certificate_sha256": cert["canonical_sha256"],
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
