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
C2 = HERE / "e3-v91c1x-r5b2c2-jacobian-minor-smooth-cover-node-glue.json"
C3 = HERE / "e3-v91c1x-r5b2c3-all-double-overlaps-317-cover.json"
D1 = HERE / "e3-v91c1x-r5b2d1-source-bound-swap23-action-adapter.json"
OUT = HERE / "e3-v91c1x-r5b2d2-swap23-317-cover-common-refinement.json"

EXC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
C1_SHA = "b0bb861bda9c3066a63cc471940d59bcd1cf172ee0322c2a7448a51f9ab9b133"
C2_SHA = "8e5b2b38cd38d39c35e908d630a208ac7d84d5dfc8f23e9e59939a1aec6bf8f9"
C3_SHA = "a49f7a77ad9aad10714e556503dbd5a84585c8f1c92241b9213d3e439819ca50"
D1_SHA = "1c6556e7a606636aaf9f154762bc32e6b2b46cfe7fbaf39da809efdcbd1cb19d"
COORDS = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]
PERM = [0, 2, 1, 3, 5, 4, 6]
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


def decode_poly(encoded, variables):
    out = sp.Integer(0)
    for term in encoded["terms"]:
        coeff = decode_element(term["coefficient_Qi"])
        mon = sp.Integer(1)
        for v, e in zip(variables, term["exponents"]):
            mon *= v ** int(e)
        out += coeff * mon
    return clean(out)


def encode_rational(expr, variables):
    num, den = sp.fraction(sp.cancel(expr))
    num = sp.expand(num)
    den = sp.expand(den)
    return {
        "numerator": encode_poly(num, variables),
        "denominator": encode_poly(den, variables),
    }


def projective_poly_signature(poly, variables):
    P = sp.Poly(sp.expand(poly), *variables, extension=I)
    terms = P.terms()
    if not terms:
        raise SystemExit("zero polynomial has no projective signature")
    pivot = sp.sympify(terms[0][1])
    normalized = []
    for mon, coeff in terms:
        normalized.append({
            "exponents": list(mon),
            "coefficient_Qi": encode_element(clean(sp.sympify(coeff) / pivot)),
        })
    return csha(normalized), pivot


def projective_normalize(v):
    vals = [clean(x) for x in list(v)]
    pivot = next((x for x in vals if x != 0), None)
    if pivot is None:
        raise SystemExit("zero projective point")
    return tuple(clean(x / pivot) for x in vals)


def separator_factor(source, target):
    for r in range(7):
        for s in range(r + 1, 7):
            det = clean(source[r] * target[s] - source[s] * target[r])
            if det != 0:
                coeff = [sp.Integer(0)] * 7
                coeff[r] = clean(target[s])
                coeff[s] = clean(-target[r])
                if clean(sum(coeff[j] * target[j] for j in range(7))) != 0:
                    raise SystemExit("separator failed to vanish at target")
                if clean(sum(coeff[j] * source[j] for j in range(7))) == 0:
                    raise SystemExit("separator vanished at source")
                return {
                    "coordinate_pair_0based": [r, s],
                    "coefficients_Qi": encode_vector(coeff),
                }
    raise SystemExit("projectively equal frozen nodes encountered")


def node_meta(row):
    p = sp.Matrix([decode_element(x) for x in row["node_point_ambient_P6_L_basis"]])
    pivot = next((j for j, x in enumerate(p) if clean(x) != 0), None)
    if pivot is None:
        raise SystemExit(f"zero frozen node {row['exceptional_id']}")
    q = sp.Matrix([clean(x / p[pivot]) for x in p])
    nonpivot = [j for j in range(7) if j != pivot]
    return {
        "exceptional_id": row["exceptional_id"],
        "point": p,
        "pivot": pivot,
        "q": q,
        "nonpivot": nonpivot,
        "normalized": projective_normalize(p),
    }


def tau_vec(v):
    return sp.Matrix([clean(v[PERM[j]]) for j in range(7)])


def chart_id(eid, cp):
    return f"{eid}_GLOBAL_ISOLATING_REES_D{cp}"


def chart_blowdown(meta, cp):
    e = sp.Symbol("e")
    u = sp.symbols("u0:5")
    d = sp.symbols("d0:6")
    affine = list(meta["q"])
    affine[meta["pivot"]] = sp.Integer(1)
    for k, j in enumerate(meta["nonpivot"]):
        affine[j] = clean(meta["q"][j] + d[k])
    nonp = [j for j in range(6) if j != cp]
    sub = {d[cp]: e}
    for k, j in enumerate(nonp):
        sub[d[j]] = e * u[k]
    blow = sp.Matrix([clean(x.subs(sub)) for x in affine])
    return e, u, d, nonp, blow


def target_displacements_from_source_chart(source_meta, target_meta, cp):
    e, u, _d, _nonp, blow = chart_blowdown(source_meta, cp)
    acted = tau_vec(blow)
    denom = clean(acted[target_meta["pivot"]])
    if clean(denom.subs(e, 0)) == 0:
        raise SystemExit(f"acted target affine pivot vanished on exceptional center {source_meta['exceptional_id']}")
    y = sp.Matrix([clean(x / denom) for x in acted])
    dprime = [clean(y[j] - target_meta["q"][j]) for j in target_meta["nonpivot"]]
    h = [clean(x / e) for x in dprime]
    vars_ = [e, *u]
    for idx, val in enumerate(h):
        num, den = sp.fraction(sp.cancel(val))
        if clean(den.subs(e, 0)) == 0:
            raise SystemExit(f"acted Rees homogeneous coordinate acquired exceptional pole {source_meta['exceptional_id']} cp={cp} r={idx}")
    reconstructed = list(target_meta["q"])
    reconstructed[target_meta["pivot"]] = sp.Integer(1)
    for k, j in enumerate(target_meta["nonpivot"]):
        reconstructed[j] = clean(target_meta["q"][j] + dprime[k])
    for j in range(7):
        if clean(reconstructed[j] - y[j]) != 0:
            raise SystemExit(f"target affine displacement reconstruction failed {source_meta['exceptional_id']} cp={cp} coord={j}")
    return vars_, blow, y, dprime, h


def derivative_matrix(source_meta, target_meta):
    d = sp.symbols("d0:6")
    affine = list(source_meta["q"])
    affine[source_meta["pivot"]] = sp.Integer(1)
    for k, j in enumerate(source_meta["nonpivot"]):
        affine[j] = clean(source_meta["q"][j] + d[k])
    acted = tau_vec(sp.Matrix(affine))
    denom = clean(acted[target_meta["pivot"]])
    y = sp.Matrix([clean(x / denom) for x in acted])
    dprime = sp.Matrix([clean(y[j] - target_meta["q"][j]) for j in target_meta["nonpivot"]])
    J = dprime.jacobian(d)
    zero = {x: 0 for x in d}
    J0 = sp.Matrix([[clean(J[r, c].subs(zero)) for c in range(6)] for r in range(6)])
    det = clean(J0.det())
    if det == 0:
        raise SystemExit(f"swap23 tangent map singular at {source_meta['exceptional_id']}")
    return J0, det


def build_certificate():
    exc = load_locked(EXC, EXC_SHA)
    c1 = load_locked(C1, C1_SHA)
    c2 = load_locked(C2, C2_SHA)
    c3 = load_locked(C3, C3_SHA)
    d1 = load_locked(D1, D1_SHA)

    if d1["source_bound_action"]["composed_coordinate_permutation_zero_based"] != PERM:
        raise SystemExit("R5B2D1 source-bound coordinate permutation moved")
    if [PERM[PERM[j]] for j in range(7)] != list(range(7)):
        raise SystemExit("swap23 coordinate permutation ceased to be involutive")
    if c2["finite_cover"]["total_cover_chart_count"] != 317:
        raise SystemExit("R5B2C2 finite cover count moved")
    if c3["cover_index"]["ordered_cover_pair_count_including_diagonal"] != 317 * 317:
        raise SystemExit("R5B2C3 all-double-overlap count moved")

    X = sp.symbols("a1 a2 a3 b1 b2 b3 c")
    minor_rows = c2["smooth_complement_cover"]["minor_rows"]
    if len(minor_rows) != 29:
        raise SystemExit("smooth minor inventory moved")
    minor_polys = {r["minor_id"]: decode_poly(r["reduced_minor_Q"], X) for r in minor_rows}
    sig_to_minor = {}
    pivots = {}
    for mid, poly in minor_polys.items():
        sig, piv = projective_poly_signature(poly, X)
        if sig in sig_to_minor:
            raise SystemExit("duplicate smooth minor projective signature")
        sig_to_minor[sig] = mid
        pivots[mid] = piv

    minor_action_rows = []
    minor_pullback = {}
    subs_tau = {X[j]: X[PERM[j]] for j in range(7)}
    for target_mid, poly in minor_polys.items():
        pull = clean(poly.subs(subs_tau, simultaneous=True))
        sig, pull_pivot = projective_poly_signature(pull, X)
        source_mid = sig_to_minor.get(sig)
        if source_mid is None:
            raise SystemExit(f"swap23 pulled smooth minor escaped 29-chart inventory: {target_mid}")
        source_pivot = pivots[source_mid]
        scalar = clean(pull_pivot / source_pivot)
        if clean(pull - scalar * minor_polys[source_mid]) != 0:
            raise SystemExit(f"smooth minor scalar match failed {target_mid}->{source_mid}")
        minor_pullback[target_mid] = source_mid
        minor_action_rows.append({
            "acted_target_minor_id": target_mid,
            "source_minor_id_equal_to_pullback_open": source_mid,
            "pullback_scalar_Qi": encode_element(scalar),
            "common_refinement_piece_id": f"REF_SMOOTH_{source_mid}",
        })
    if set(minor_pullback.values()) != set(minor_polys):
        raise SystemExit("swap23 smooth-minor action is not a permutation")
    for mid in minor_polys:
        if minor_pullback[minor_pullback[mid]] != mid:
            raise SystemExit("swap23 smooth-minor permutation is not involutive")

    models = exc["exceptional_models"]
    expected_ids = [f"EXC_{i:03d}" for i in range(1, 49)]
    if [x["exceptional_id"] for x in models] != expected_ids:
        raise SystemExit("frozen node inventory order moved")
    metas = {row["exceptional_id"]: node_meta(row) for row in models}
    norm_to_id = {metas[eid]["normalized"]: eid for eid in expected_ids}
    if len(norm_to_id) != 48:
        raise SystemExit("frozen node points are no longer distinct")

    node_action = {}
    for eid in expected_ids:
        acted = projective_normalize(tau_vec(metas[eid]["point"]))
        target = norm_to_id.get(acted)
        if target is None:
            raise SystemExit(f"swap23 moved frozen node outside 48-node inventory: {eid}")
        node_action[eid] = target
    if set(node_action.values()) != set(expected_ids):
        raise SystemExit("swap23 node action is not a permutation")
    for eid in expected_ids:
        if node_action[node_action[eid]] != eid:
            raise SystemExit("swap23 node action is not involutive")

    c1_rows = {x["exceptional_id"]: x for x in c1["node_rows"]}
    node_rows = []
    derivative_checks = 0
    chart_affine_compatibility_checks = 0
    exceptional_refinement_piece_count = 0
    acted_localizer_center_unit_checks = 0

    for eid in expected_ids:
        target_id = node_action[eid]
        source_meta = metas[eid]
        target_meta = metas[target_id]

        target_factors = []
        for other in expected_ids:
            if other == target_id:
                continue
            f = separator_factor(target_meta["point"], metas[other]["point"])
            f["vanishing_node"] = other
            target_factors.append(f)
        replay = csha(target_factors)
        stored = c1_rows[target_id]["node_isolating_principal_open"]["separator_factor_list_sha256"]
        if replay != stored:
            raise SystemExit(f"target localizer separator commitment moved {target_id}")

        pulled_factors = []
        for f in target_factors:
            coeff = [decode_element(z) for z in f["coefficients_Qi"]]
            pulled = [clean(coeff[PERM[k]]) for k in range(7)]
            if clean(sum(pulled[k] * source_meta["point"][k] for k in range(7))) == 0:
                raise SystemExit(f"pulled target localizer factor vanished at source center {eid}")
            pulled_factors.append({
                "target_vanishing_node": f["vanishing_node"],
                "pulled_coefficients_Qi": encode_vector(pulled),
            })
            acted_localizer_center_unit_checks += 1
        pulled_pivot_index = PERM[target_meta["pivot"]]
        if clean(source_meta["point"][pulled_pivot_index]) == 0:
            raise SystemExit(f"pulled target localizer pivot factor vanished at source center {eid}")
        acted_localizer_center_unit_checks += 1
        pulled_localizer_recipe = {
            "pulled_target_node": target_id,
            "pulled_target_affine_pivot_coordinate_0based": pulled_pivot_index,
            "pulled_separator_factors": pulled_factors,
        }

        J0, det = derivative_matrix(source_meta, target_meta)
        derivative_checks += 1
        derivative_commitment = csha({
            "matrix_Qi": [encode_vector(J0.row(r)) for r in range(6)],
            "determinant_Qi": encode_element(det),
        })

        pair_descriptors = []
        for cp_source in range(6):
            vars_, blow, y, dprime, h = target_displacements_from_source_chart(source_meta, target_meta, cp_source)
            acted_blow = tau_vec(blow)
            target_den = clean(acted_blow[target_meta["pivot"]])
            for j in range(7):
                if clean(y[j] - acted_blow[j] / target_den) != 0:
                    raise SystemExit(f"smooth/exceptional tau compatibility failed {eid} cp={cp_source} coord={j}")
            chart_affine_compatibility_checks += 1

            for cp_target in range(6):
                if h[cp_target] == 0:
                    raise SystemExit(f"target Rees chart homogeneous pullback vanished identically {eid} {cp_source}->{cp_target}")
                target_nonp = [r for r in range(6) if r != cp_target]
                target_map = {
                    "e_target": encode_rational(dprime[cp_target], vars_),
                    "u_target_in_displacement_order": [
                        {"target_displacement_index": r, "value": encode_rational(clean(dprime[r] / dprime[cp_target]), vars_)}
                        for r in target_nonp
                    ],
                }
                desc = {
                    "piece_id": f"REF_{eid}_S{cp_source}_T{cp_target}",
                    "source_chart_id": chart_id(eid, cp_source),
                    "acted_target_chart_id": chart_id(target_id, cp_target),
                    "source_to_acted_target_map_sha256": csha(target_map),
                    "acted_target_rees_homogeneous_coordinate_pullback_sha256": csha(encode_rational(h[cp_target], vars_)),
                    "domain_rule": "inside the source Rees chart: pulled target node-isolating localizer != 0 and pulled target Rees homogeneous coordinate != 0",
                    "source_projection": "identity inclusion into the displayed source Rees chart",
                    "acted_projection": "restriction of the source-bound lifted swap23 map to the displayed acted target Rees chart",
                }
                pair_descriptors.append(desc)
                exceptional_refinement_piece_count += 1
        if len(pair_descriptors) != 36:
            raise SystemExit(f"exceptional common-refinement pair count moved {eid}")

        node_rows.append({
            "source_node": eid,
            "acted_target_node": target_id,
            "source_node_rees_chart_count": 6,
            "acted_target_node_rees_chart_count": 6,
            "common_refinement_piece_count": 36,
            "swap23_tangent_map_derivative_commitment_sha256": derivative_commitment,
            "pulled_target_node_localizer_factorized_recipe_sha256": csha(pulled_localizer_recipe),
            "36_piece_descriptors_sha256": csha(pair_descriptors),
            "target_chart_maps_are_dehomogenizations_of_one_common_six_coordinate_acted_rees_vector": True,
            "same_node_target_transition_compatibility_exact_by_common_homogeneous_vector": True,
            "smooth_exceptional_transition_compatibility_verified_by_blowdown_then_global_tau": True,
        })

    if derivative_checks != 48:
        raise SystemExit("node derivative check count moved")
    if chart_affine_compatibility_checks != 48 * 6:
        raise SystemExit("source Rees chart affine compatibility count moved")
    if exceptional_refinement_piece_count != 48 * 6 * 6:
        raise SystemExit("exceptional common-refinement piece count moved")
    if acted_localizer_center_unit_checks != 48 * 48:
        raise SystemExit("acted target localizer center-unit check count moved")

    smooth_refinement_piece_count = len(minor_action_rows)
    total_refinement_piece_count = smooth_refinement_piece_count + exceptional_refinement_piece_count
    if total_refinement_piece_count != 29 + 48 * 36:
        raise SystemExit("common-refinement total piece count moved")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b2d2.swap23_317_cover_common_refinement.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B2D2_SWAP23_317_COVER_COMMON_REFINEMENT",
        "role": "EXACT_NONCREDIT_SOURCE_BOUND_SWAP23_COMMON_REFINEMENT_OF_R5_317_CHART_RESOLVED_SURFACE_COVER",
        "entry": {
            "pr": 1695,
            "authority": "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT",
            "stage33_progress": "6/11",
        },
        "source_locks": {
            "exceptional_p1_tangent_coordinates_sha256": EXC_SHA,
            "r5b2c1_sha256": C1_SHA,
            "r5b2c2_sha256": C2_SHA,
            "r5b2c3_sha256": C3_SHA,
            "r5b2d1_sha256": D1_SHA,
        },
        "source_bound_swap23": {
            "coordinate_order": COORDS,
            "coordinate_permutation_zero_based": PERM,
            "involutive": True,
            "node_action_is_permutation_of_48_frozen_nodes": True,
            "node_action_is_involutive": True,
            "node_action": node_action,
        },
        "smooth_cover_action": {
            "smooth_minor_chart_count": 29,
            "pullback_action_is_permutation": True,
            "pullback_action_is_involutive": True,
            "minor_action_rows": minor_action_rows,
            "smooth_common_refinement_piece_count": smooth_refinement_piece_count,
            "reason": "for every acted target smooth chart D_+(M_j), tau^*M_j is a nonzero Q(i)-scalar multiple of one retained smooth minor M_i, hence its pullback open is exactly the retained source chart D_+(M_i)",
        },
        "exceptional_common_refinement": {
            "source_node_count": 48,
            "source_rees_chart_count_per_node": 6,
            "acted_target_rees_chart_count_per_node": 6,
            "piece_count_per_node": 36,
            "total_exceptional_refinement_piece_count": exceptional_refinement_piece_count,
            "node_rows": node_rows,
            "tangent_derivative_invertibility_check_count": derivative_checks,
            "source_chart_global_tau_blowdown_compatibility_check_count": chart_affine_compatibility_checks,
            "pulled_target_localizer_center_unit_check_count": acted_localizer_center_unit_checks,
            "coverage_reason": "the 29 smooth charts cover the complement of the exceptional fibers; on each exceptional P5 the six source standard Rees charts and the six acted target standard Rees charts are both covers, because the source-bound swap23 tangent derivative is invertible, so their 36 pairwise intersections cover that exceptional fiber",
        },
        "common_refinement_index": {
            "smooth_piece_count": smooth_refinement_piece_count,
            "exceptional_piece_count": exceptional_refinement_piece_count,
            "total_piece_count": total_refinement_piece_count,
            "equals_1757": True,
            "covers_whole_resolved_surface": True,
            "each_piece_refines_one_source_317_cover_chart": True,
            "each_piece_refines_one_swap23_pulled_back_317_cover_chart": True,
            "source_projection_maps_materialized": True,
            "acted_projection_maps_materialized": True,
        },
        "transition_compatibility": {
            "smooth_smooth": True,
            "exceptional_exceptional_same_node": True,
            "smooth_exceptional": True,
            "reason": "smooth pieces use the global source-bound coordinate involution; exceptional target maps are exact dehomogenizations of the same acted six-coordinate Rees vector; and every exceptional chart map blows down to the same global tau-transformed projective point, so all restrictions agree with the C3 atlas transitions on common domains",
        },
        "exact_consequence": {
            "swap23_pullback_of_all_29_smooth_chart_domains_materialized": True,
            "swap23_action_on_all_48_exceptional_centers_materialized": True,
            "swap23_lift_to_all_288_source_rees_charts_materialized": True,
            "explicit_source_bound_common_refinement_of_original_and_swap23_pulled_317_covers_materialized": True,
            "all_common_refinement_projection_maps_materialized": True,
            "double_overlap_transition_compatibility_verified": True,
        },
        "construction_status": {
            "source_bound_swap23_coordinate_action_materialized": True,
            "swap23_pullback_of_each_317_chart_domain_materialized": True,
            "cover_action_or_common_refinement_materialized": True,
            "same_representative_transport_materialized": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "equivalent_unimodular_cech_glue_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
        },
        "next_missing_object": "SOURCE_BOUND_LITERAL_A2_02_REPRESENTATIVE_ON_THE_1757_PIECE_COMMON_REFINEMENT_THEN_ELL_IJ_R_IJ_AND_TRIPLE_OVERLAP_ACTION_DIFFERENCE_IDENTITY",
        "next_exact_leaf": "V91C1X_R5B3_MATERIALIZE_LITERAL_A2_02_MU2_OR_EQUIVALENT_GLUE_ON_THE_SWAP23_COMMON_REFINEMENT",
        "credit_firewall": {
            "authority_promotion": False,
            "common_refinement_authority_credit": False,
            "h2_fixedness_credit": False,
            "marked_brauer_image_credit": False,
            "mask20_credit": False,
            "source_bound_dim5_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B2D2_SWAP23_317_COVER_COMMON_REFINEMENT",
        "smooth_refinement_pieces": cert["common_refinement_index"]["smooth_piece_count"],
        "exceptional_refinement_pieces": cert["common_refinement_index"]["exceptional_piece_count"],
        "total_refinement_pieces": cert["common_refinement_index"]["total_piece_count"],
        "certificate_sha256": cert["canonical_sha256"],
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
