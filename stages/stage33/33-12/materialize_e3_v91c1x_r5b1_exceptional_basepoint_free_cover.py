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
OUT = HERE / "e3-v91c1x-r5b1-a2-02-exceptional-basepoint-free-cover.json"
EXPECTED_EXC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
TARGETS = ["EXC_003", "EXC_004", "EXC_011", "EXC_012"]
COORDS = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]
I = sp.I
PARAMETERS = ["0", "infinity", "1", "-1", "i", "-i"]
UVS = [(0, 1), (1, 0), (1, 1), (-1, 1), (I, 1), (-I, 1)]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def clean(x):
    return sp.cancel(sp.expand(x))


def is_zero(x):
    return clean(x) == 0


def projective_normalize(v):
    vals = [clean(x) for x in list(v)]
    pivot = next((x for x in vals if not is_zero(x)), None)
    if pivot is None:
        raise SystemExit("zero projective vector")
    return tuple(clean(x / pivot) for x in vals)


def independent_columns(columns):
    out = []
    rank = 0
    for column in columns:
        candidate = sp.Matrix.hstack(*(out + [sp.Matrix(column)]))
        new_rank = candidate.rank()
        if new_rank > rank:
            out.append(sp.Matrix(column))
            rank = new_rank
    return out


def perpendicular_candidates(v):
    x, y, z = list(v)
    return [sp.Matrix([y, -x, 0]), sp.Matrix([z, 0, -x]), sp.Matrix([0, z, -y])]


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


def decode_element(z):
    return sp.Rational(int(z[0]), int(z[1])) + I * sp.Rational(int(z[2]), int(z[3]))


def encode_vector(v):
    return [encode_element(x) for x in list(v)]


def encode_matrix(m):
    return [[encode_element(m[r, c]) for c in range(m.cols)] for r in range(m.rows)]


def side_metadata(side_index):
    j = side_index - 1
    family = j // 8
    r = j % 8
    e1 = [1, -1][r // 4]
    e2 = [1, -1][(r // 2) % 2]
    e3 = [1, -1][r % 2]
    return family, e1, e2, e3


def side_param_and_tangent(side_index, parameter_index):
    family, e1, e2, e3 = side_metadata(side_index)
    u, v = UVS[parameter_index - 1]
    X, Y, Z = u * u - v * v, 2 * u * v, u * u + v * v
    du, dv = (1, 0) if v != 0 else (0, 1)
    dX = 2 * u * du - 2 * v * dv
    dY = 2 * (du * v + u * dv)
    dZ = 2 * u * du + 2 * v * dv
    if family == 0:
        q = [0, -e1 * X, -e2 * Y, -e3 * Z, Y, X, Z]
        d = [0, -e1 * dX, -e2 * dY, -e3 * dZ, dY, dX, dZ]
    elif family == 1:
        q = [-e2 * Y, 0, -e1 * X, X, -e3 * Z, Y, Z]
        d = [-e2 * dY, 0, -e1 * dX, dX, -e3 * dZ, dY, dZ]
    else:
        q = [-e1 * X, -e2 * Y, 0, Y, X, -e3 * Z, Z]
        d = [-e1 * dX, -e2 * dY, 0, dY, dX, -e3 * dZ, dZ]
    return sp.Matrix([clean(x) for x in q]), sp.Matrix([clean(x) for x in d])


def quadrics(v):
    a1, a2, a3, b1, b2, b3, c = list(v)
    return sp.Matrix([
        a1 * a1 + a2 * a2 - b3 * b3,
        a2 * a2 + a3 * a3 - b1 * b1,
        a1 * a1 + a3 * a3 - b2 * b2,
        a1 * a1 + a2 * a2 + a3 * a3 - c * c,
    ])


def jacobian(v):
    a1, a2, a3, b1, b2, b3, c = list(v)
    return sp.Matrix([
        [2 * a1, 2 * a2, 0, 0, 0, -2 * b3, 0],
        [0, 2 * a2, 2 * a3, -2 * b1, 0, 0, 0],
        [2 * a1, 0, 2 * a3, 0, -2 * b2, 0, 0],
        [2 * a1, 2 * a2, 2 * a3, 0, 0, 0, -2 * c],
    ])


def deterministic_left_inverse(B):
    rows = list(B.T.rref()[1])
    if len(rows) != 4:
        raise SystemExit("tangent basis did not expose four pivot rows")
    M = B.extract(rows, range(4))
    if is_zero(M.det()):
        raise SystemExit("pivot tangent minor singular")
    Minv = M.inv()
    L = sp.zeros(4, 7)
    for j, row in enumerate(rows):
        for i in range(4):
            L[i, row] = clean(Minv[i, j])
    if L * B != sp.eye(4):
        raise SystemExit("left inverse failure")
    return L


def projection_system(base, G, Y, p):
    forms = independent_columns([v for v in perpendicular_candidates(base) if v != sp.zeros(3, 1)])
    if len(forms) != 2:
        raise SystemExit("projection form rank failure")
    F = sp.Matrix.hstack(*forms).T
    if F.rank() != 2:
        raise SystemExit("projection form matrix rank failure")
    ker = F.nullspace()
    if len(ker) != 1 or projective_normalize(ker[0]) != projective_normalize(base):
        raise SystemExit("projection common zero is not exactly the chosen basepoint")
    grad = G * base
    tangent_kernel = independent_columns([v for v in perpendicular_candidates(grad) if v != sp.zeros(3, 1)])
    w = next((v for v in tangent_kernel if sp.Matrix.hstack(base, v).rank() == 2), None)
    if w is None or not is_zero(grad.dot(w)):
        raise SystemExit("base tangent extension failure")
    R = (F * Y).applyfunc(clean)
    if R.shape != (2, 7) or R * p != sp.zeros(2, 1):
        raise SystemExit("ambient projection pair does not vanish at node")
    if F * w == sp.zeros(2, 1):
        raise SystemExit("extended basepoint coordinate vanished")
    return F, R, w


def transition_matrix(pairs_a, pairs_b):
    rows = []
    for A, B in zip(pairs_a, pairs_b):
        a0, a1 = list(A)
        b0, b1 = list(B)
        rows.append([clean(b1 * a0), clean(b1 * a1), clean(-b0 * a0), clean(-b0 * a1)])
    Msys = sp.Matrix(rows)
    ns = Msys.nullspace()
    if len(ns) != 1:
        raise SystemExit(f"PGL2 transition not unique, nullity={len(ns)}")
    q = sp.Matrix(projective_normalize(ns[0]))
    M = sp.Matrix([[q[0], q[1]], [q[2], q[3]]])
    if is_zero(M.det()):
        raise SystemExit("PGL2 transition singular")
    for A, B in zip(pairs_a, pairs_b):
        if projective_normalize(M * A) != projective_normalize(B):
            raise SystemExit("PGL2 transition failed on crossing")
    return M


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    exc = json.loads(EXC.read_text(encoding="utf-8"))
    claimed = exc["canonical_sha256"]
    body = dict(exc)
    body.pop("canonical_sha256")
    actual = csha(body)
    if claimed != EXPECTED_EXC_SHA or actual != EXPECTED_EXC_SHA:
        raise SystemExit(f"exceptional tangent source lock moved: {claimed} {actual}")

    rows = []
    for eid in TARGETS:
        er = next(x for x in exc["exceptional_models"] if x["exceptional_id"] == eid)
        p = sp.Matrix([decode_element(x) for x in er["node_point_ambient_P6_L_basis"]])
        if any(not is_zero(x) for x in quadrics(p)):
            raise SystemExit(f"node escaped surface {eid}")
        J = jacobian(p)
        if J.rank() != 3:
            raise SystemExit(f"node rank regression {eid}")
        W = J.nullspace()
        Bcols = independent_columns([p] + W)
        if len(Bcols) != 4 or Bcols[0] != p:
            raise SystemExit(f"tangent basis regression {eid}")
        B = sp.Matrix.hstack(*Bcols)
        alpha_space = J.T.nullspace()
        if len(alpha_space) != 1:
            raise SystemExit(f"quadratic relation regression {eid}")
        alpha = alpha_space[0]

        def qeval(v):
            return clean((alpha.T * quadrics(v))[0])

        U = B[:, 1:4]
        G = sp.zeros(3, 3)
        for r in range(3):
            for c in range(3):
                G[r, c] = clean((qeval(U[:, r] + U[:, c]) - qeval(U[:, r]) - qeval(U[:, c])) / 2)
        if G != G.T or is_zero(G.det()):
            raise SystemExit(f"tangent conic degenerate {eid}")

        tangent_rows = []
        ys = []
        for cr in er["physical_crossing_tangent_coordinates"]:
            side = int(cr["side_index_1based"])
            z = int(cr["side_parameter_index_1based"])
            q, d = side_param_and_tangent(side, z)
            if projective_normalize(q) != projective_normalize(p):
                raise SystemExit(f"node/side incidence moved {eid} side={side}")
            solution, parameters = B.gauss_jordan_solve(d)
            if parameters.rows or B * solution != d:
                raise SystemExit(f"tangent solve failed {eid}")
            y = solution[1:4, 0]
            if y == sp.zeros(3, 1) or not is_zero((y.T * G * y)[0]):
                raise SystemExit(f"crossing tangent missed conic {eid}")
            tangent_rows.append(cr)
            ys.append(y)

        if len(ys) < 2 or projective_normalize(ys[0]) == projective_normalize(ys[1]):
            raise SystemExit(f"need two distinct projection bases {eid}")

        L = deterministic_left_inverse(B)
        Y = L[1:4, :]
        systems = []
        all_pairs = []
        for base_index in (0, 1):
            F, R, w = projection_system(ys[base_index], G, Y, p)
            pairs = []
            for k, y in enumerate(ys):
                pair = F * (w if k == base_index else y)
                if pair == sp.zeros(2, 1):
                    raise SystemExit(f"zero extended coordinate {eid} base={base_index} k={k}")
                pairs.append(sp.Matrix(projective_normalize(pair)))
            all_pairs.append(pairs)
            systems.append({
                "base_crossing_index_0based": base_index,
                "base_crossing_side_index_1based": int(tangent_rows[base_index]["side_index_1based"]),
                "base_crossing_parameter": tangent_rows[base_index]["side_parameter"],
                "ambient_projection_R0_R1_coefficients_L_basis": encode_matrix(R),
                "extended_crossing_coordinates_P1_L_basis": [encode_vector(x) for x in pairs],
                "common_zero_locus_on_projective_tangent_plane": "EXACTLY_THE_CHOSEN_BASEPOINT",
            })

        M = transition_matrix(all_pairs[0], all_pairs[1])
        rows.append({
            "component_id": eid,
            "physical_crossing_count": len(ys),
            "two_distinct_projection_basepoints_verified": True,
            "projection_systems": systems,
            "pgl2_transition_system0_to_system1": encode_matrix(M),
            "transition_determinant_nonzero": True,
            "coverage_statement": "domain(system0) union domain(system1) covers the exceptional conic because each system has exactly one basepoint and the two basepoints are distinct",
            "frozen_tangent_model_sha256": er["full_tangent_conic_coordinate_model_sha256"],
        })

    cert = {
        "schema": "stage33.e3.v91c1x_r5b1.a2_02_exceptional_basepoint_free_projection_cover.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B1_A2_02_EXCEPTIONAL_BASEPOINT_FREE_PROJECTION_COVER",
        "role": "EXACT_NONCREDIT_R5B1_EXCEPTIONAL_COMPONENT_COVER_AND_TRANSITION",
        "entry": {
            "pr": 1684,
            "authority": "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT",
            "stage33_progress": "6/11",
            "r5a_canonical_sha256": "76e63baad22a88f7c2b93d31930785c3b4eafe785fdc6de950756b169be7c9ce",
        },
        "source_locks": {
            "exceptional_p1_tangent_coordinates_path": "stages/stage33/33-07/exceptional-p1-tangent-coordinates.json",
            "exceptional_p1_tangent_coordinates_sha256": EXPECTED_EXC_SHA,
            "construction_method": "reconstruct the exact tangent conic, choose two distinct physical crossings as projection bases, build deterministic projection forms and ambient lifts, then solve the unique PGL2 transition on the three physical crossings",
        },
        "target_exceptional_components": TARGETS,
        "rows": rows,
        "exact_consequence": {
            "all_four_target_exceptional_conics_have_two_source_bound_projection_systems": True,
            "each_projection_system_has_exactly_one_basepoint_on_the_exceptional_conic": True,
            "the_two_basepoints_are_distinct_for_each_component": True,
            "the_two_projection_domains_cover_each_target_exceptional_conic": True,
            "exact_pgl2_transition_between_projection_coordinates_materialized": True,
            "naive_single_R0_R1_pair_treated_as_basepoint_free_cover": False,
        },
        "next_missing_object": "SOURCE_BOUND_REES_BLOWUP_NEIGHBORHOOD_THICKENING_OF_THE_FOUR_EXCEPTIONAL_COVERS_PLUS_STRICT_TRANSFORM_NEIGHBORHOOD_CHARTS_FOR_SIDE_002_004_006_008_WITH_SURFACE_UNIFORMIZERS_AND_DOUBLE_OVERLAP_MAPS",
        "next_exact_leaf": "V91C1X_R5B2_THICKEN_EXCEPTIONAL_COMPONENT_COVERS_TO_REES_BLOWUP_NEIGHBORHOODS_AND_ATTACH_FOUR_SIDE_STRICT_TRANSFORM_CHARTS",
        "credit_firewall": {
            "finite_surface_cover_materialized": False,
            "literal_local_surface_equations_materialized": False,
            "component_uniformizers_materialized": False,
            "surface_double_overlap_transitions_materialized": False,
            "swap23_common_refinement_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "equivalent_unimodular_cech_glue_materialized": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "triple_overlap_identity_verified": False,
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
        "marker": "V91C1X_R5B1_EXCEPTIONAL_BASEPOINT_FREE_COVER",
        "target_count": len(rows),
        "pgl2_transition_count": len(rows),
        "certificate_sha256": cert["canonical_sha256"],
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
