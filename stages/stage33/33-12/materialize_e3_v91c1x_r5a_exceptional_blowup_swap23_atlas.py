#!/usr/bin/env python3
"""Materialize a bounded R5A exceptional blowup atlas for the A2_02 support.

This leaf is deliberately partial. It reconstructs deterministic tangent
coordinates at the four exceptional support components, turns those coordinates
into the three standard blowup charts and their exact overlap units, and records
the ambient swap23 action on those tangent charts. It does not manufacture a
side-component isolation open, a full eight-component finite cover, a literal
mu2 Cech cocycle, or a source-bound full-surface H2 representative.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
EXC = S33 / "33-07" / "exceptional-p1-tangent-coordinates.json"
R4 = HERE / "e3-v91c1x-r4-a2-02-local-chart-inventory.json"
OUT = HERE / "e3-v91c1x-r5a-a2-02-exceptional-blowup-swap23-atlas.json"

EXC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
R4_SHA = "68f61b79b07027e97b4822c4f074cd52f65cf05473475fe964fd0b6785e8c53d"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
TARGET_EXC = ("EXC_003", "EXC_004", "EXC_011", "EXC_012")
TARGET_SIDE = ("SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008")
COORDS = ("a1", "a2", "a3", "b1", "b2", "b3", "c")
I = sp.I


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"source lock moved: {path}: {claimed} {actual}")
    return obj


def clean(x):
    return sp.cancel(sp.expand(x))


def is_zero(x):
    return clean(x) == 0


def rational_pair(q):
    q = clean(q)
    if q.is_Rational is not True:
        raise SystemExit(f"expected rational coefficient: {q}")
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


def projective_normalize(v):
    vals = [clean(x) for x in list(v)]
    pivot = next((x for x in vals if not is_zero(x)), None)
    if pivot is None:
        raise SystemExit("zero projective vector")
    return tuple(clean(x / pivot) for x in vals)


def pkey(v):
    return tuple(str(x) for x in projective_normalize(v))


def independent_columns(columns):
    out = []
    rank = 0
    for column in columns:
        cand = sp.Matrix.hstack(*(out + [sp.Matrix(column)]))
        nr = cand.rank()
        if nr > rank:
            out.append(sp.Matrix(column))
            rank = nr
    return out


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


def deterministic_left_inverse(B):
    rows = list(B.T.rref()[1])
    if len(rows) != 4:
        raise SystemExit("tangent basis did not expose four pivot rows")
    M = B.extract(rows, range(4))
    if is_zero(M.det()):
        raise SystemExit("pivot-row tangent minor singular")
    Minv = M.inv()
    L = sp.zeros(4, 7)
    for j, row in enumerate(rows):
        for i in range(4):
            L[i, row] = clean(Minv[i, j])
    if L * B != sp.eye(4):
        raise SystemExit("deterministic tangent left inverse failed")
    return L, rows


def tangent_model(er):
    eid = er["exceptional_id"]
    p = sp.Matrix([decode_element(x) for x in er["node_point_ambient_P6_L_basis"]])
    if any(not is_zero(x) for x in quadrics(p)):
        raise SystemExit(f"node escaped surface: {eid}")
    J = jacobian(p)
    if J.rank() != 3:
        raise SystemExit(f"node Jacobian rank moved: {eid}")
    W = J.nullspace()
    Bcols = independent_columns([p] + W)
    if len(Bcols) != 4 or Bcols[0] != p:
        raise SystemExit(f"tangent basis regression: {eid}")
    B = sp.Matrix.hstack(*Bcols)
    L, pivots = deterministic_left_inverse(B)
    Y = L[1:4, :]
    U = B[:, 1:4]
    if Y * p != sp.zeros(3, 1) or Y * U != sp.eye(3):
        raise SystemExit(f"tangent quotient coordinates failed: {eid}")
    if Y.rank() != 3:
        raise SystemExit(f"tangent quotient coordinate rank failed: {eid}")
    return p, B, Y, pivots


def sigma_matrix():
    S = sp.eye(7)
    S[1, 1] = S[2, 2] = 0
    S[1, 2] = S[2, 1] = 1
    S[4, 4] = S[5, 5] = 0
    S[4, 5] = S[5, 4] = 1
    return S


def verify_sigma_quadrics(S):
    xs = sp.symbols("a1 a2 a3 b1 b2 b3 c")
    x = sp.Matrix(xs)
    q = quadrics(x)
    qs = quadrics(S*x)
    expected = sp.Matrix([q[2], q[1], q[0], q[3]])
    if any(not is_zero(qs[i] - expected[i]) for i in range(4)):
        raise SystemExit("swap23 does not permute pinned quadrics as expected")


def build_certificate():
    exc = load_locked(EXC, EXC_SHA)
    r4 = load_locked(R4, R4_SHA)
    if tuple(r4["components"]) != TARGET_EXC + TARGET_SIDE:
        raise SystemExit("A2_02 R4 support inventory moved")

    models = {er["exceptional_id"]: er for er in exc["exceptional_models"]}
    if not all(e in models for e in TARGET_EXC):
        raise SystemExit("target exceptional support missing")

    tangent = {}
    node_lookup = {}
    for eid, er in models.items():
        p = sp.Matrix([decode_element(x) for x in er["node_point_ambient_P6_L_basis"]])
        node_lookup[pkey(p)] = eid
    if len(node_lookup) != len(models):
        raise SystemExit("exceptional node projective keys are not unique")

    S = sigma_matrix()
    if S*S != sp.eye(7):
        raise SystemExit("swap23 ambient action is not involutive")
    verify_sigma_quadrics(S)

    rows = []
    sigma_perm = {}
    for eid in TARGET_EXC:
        p, B, Y, pivots = tangent_model(models[eid])
        target_id = node_lookup.get(pkey(S*p))
        if target_id is None:
            raise SystemExit(f"swap23 target node not found: {eid}")
        if target_id not in TARGET_EXC:
            raise SystemExit(f"A2_02 exceptional support not swap23-stable: {eid}->{target_id}")
        sigma_perm[eid] = target_id
        tangent[eid] = (p, B, Y, pivots)

    for eid in TARGET_EXC:
        p, B, Y, pivots = tangent[eid]
        target_id = sigma_perm[eid]
        tp, tB, tY, _ = tangent[target_id]
        acted = (Y*S).applyfunc(clean)
        A = (acted * tB[:, 1:4]).applyfunc(clean)
        if is_zero(A.det()):
            raise SystemExit(f"swap23 tangent action singular: {eid}")
        if acted * tB[:, 1:4] != A:
            raise SystemExit("internal tangent restriction mismatch")
        if A * (tY * tB[:, 1:4]) != A:
            raise SystemExit("target tangent-coordinate identity moved")

        charts = []
        overlaps = []
        for j in range(3):
            charts.append({
                "chart_id": f"{eid}:Y{j+1}_NONZERO",
                "exceptional_id": eid,
                "direction_open_condition": f"Y{j+1} != 0",
                "exceptional_local_parameter": f"lambda_{j+1}",
                "pullback_identity": f"Y{j+1} = lambda_{j+1}",
                "Yj_coefficients_L_basis": encode_vector(Y[j, :]),
                "coverage_role": "STANDARD_BLOWUP_DIRECTION_CHART",
            })
            for k in range(3):
                if j == k:
                    continue
                overlaps.append({
                    "from_chart": f"{eid}:Y{j+1}_NONZERO",
                    "to_chart": f"{eid}:Y{k+1}_NONZERO",
                    "overlap_conditions": [f"Y{j+1} != 0", f"Y{k+1} != 0"],
                    "unit": f"Y{k+1}/Y{j+1}",
                    "transition_identity": f"lambda_{k+1} = lambda_{j+1} * (Y{k+1}/Y{j+1})",
                    "inverse_unit": f"Y{j+1}/Y{k+1}",
                    "unit_inverse_product_exact": "1",
                })
        rows.append({
            "exceptional_id": eid,
            "node_point_ambient_P6_L_basis": encode_vector(p),
            "tangent_basis_left_inverse_pivot_rows_0based": pivots,
            "tangent_coordinate_linear_forms_Y1_Y2_Y3_L_basis": encode_matrix(Y),
            "standard_blowup_charts": charts,
            "ordered_overlap_transitions": overlaps,
            "standard_chart_cover_exact_on_exceptional_directions": True,
            "cover_reason": "Y*U=I3, so every nonzero projective tangent direction has at least one nonzero Yj",
            "swap23_target_exceptional_id": target_id,
            "swap23_restricted_tangent_coordinate_matrix_L_basis": encode_matrix(A),
            "swap23_restricted_tangent_matrix_invertible": True,
            "swap23_common_refinement_skeleton": {
                "source_standard_charts": [c["chart_id"] for c in charts],
                "target_standard_charts": [f"{target_id}:Y{k+1}_NONZERO" for k in range(3)],
                "refinement_rule": "intersect a source Yj-nonzero chart with the pullback of each target Yk-nonzero chart under swap23",
                "all_pairwise_nonemptiness_claimed": False,
                "full_overlap_transition_functions_materialized": False,
            },
        })

    if set(sigma_perm) != set(TARGET_EXC) or set(sigma_perm.values()) != set(TARGET_EXC):
        raise SystemExit("swap23 exceptional permutation is not a permutation")
    if any(sigma_perm[sigma_perm[e]] != e for e in TARGET_EXC):
        raise SystemExit("swap23 exceptional permutation is not involutive")

    side_rows = []
    r4_side = {r["component_id"]: r for r in r4["side_rows"]}
    if set(r4_side) != set(TARGET_SIDE):
        raise SystemExit("R4 side-row support moved")
    for sid in TARGET_SIDE:
        row = r4_side[sid]
        side_rows.append({
            "component_id": sid,
            "retained_r4_inventory_row": row,
            "retained_D_promoted_to_component_uniformizer": False,
            "side_isolation_open_materialized": False,
            "component_local_equation_materialized": False,
            "reason": "R4 exposes exact retained side residue/function inventory but not an isolation open or a proved local defining equation for the individual side component",
        })

    cert = {
        "schema": "stage33.e3.v91c1x.r5a.a2_02_exceptional_blowup_swap23_atlas.v1",
        "candidate": "V91C1X_R5A_A2_02_EXCEPTIONAL_STANDARD_BLOWUP_CHARTS_AND_SWAP23_REFINEMENT_SKELETON",
        "role": "EXACT_NONCREDIT_PARTIAL_COVER_CONSTRUCTION",
        "entry": {"authority": AUTH, "stage33_progress": "6/11", "pr": 1722},
        "source_locks": {
            "exceptional_p1_tangent_coordinates_sha256": EXC_SHA,
            "r4_a2_02_local_chart_inventory_sha256": R4_SHA,
        },
        "a2_02_support": {"exceptional": list(TARGET_EXC), "side": list(TARGET_SIDE), "total": 8},
        "ambient_swap23": {
            "coordinate_order": list(COORDS),
            "coordinate_permutation": {"a1":"a1", "a2":"a3", "a3":"a2", "b1":"b1", "b2":"b3", "b3":"b2", "c":"c"},
            "matrix": [[int(S[r,c]) for c in range(7)] for r in range(7)],
            "involution_exact": True,
            "surface_quadric_permutation": {"q1":"q3", "q2":"q2", "q3":"q1", "q4":"q4"},
            "exceptional_support_permutation": sigma_perm,
        },
        "exceptional_rows": rows,
        "side_rows": side_rows,
        "summary": {
            "exceptional_support_components": 4,
            "standard_blowup_charts_materialized": 12,
            "ordered_exceptional_overlap_transitions_materialized": 24,
            "exceptional_standard_chart_cover_exact": True,
            "exceptional_local_parameters_materialized": True,
            "exceptional_overlap_units_materialized": True,
            "swap23_exceptional_tangent_action_materialized": True,
            "swap23_common_refinement_skeleton_materialized": True,
            "side_support_components": 4,
            "side_isolation_opens_materialized": 0,
            "full_eight_component_finite_cover_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "source_bound_full_surface_h2_representative_materialized": False,
        },
        "exact_consequence": {
            "r5_constructive_progress": "FOUR_EXCEPTIONAL_SUPPORT_COMPONENTS_NOW_HAVE_EXPLICIT_STANDARD_BLOWUP_CHARTS_UNIFORMIZERS_AND_OVERLAP_UNITS_WITH_EXACT_SWAP23_TANGENT_REFINEMENT_SKELETON",
            "historical_r4_insufficiency_partially_reduced": True,
            "side_component_isolation_and_local_equations_still_missing": True,
            "full_cover_overlap_transition_package_still_missing": True,
            "source_bound_cech_or_equivalent_h2_anchor_still_missing": True,
            "no_repository_wide_absence_claim": True,
            "no_mathematical_nonexistence_claim": True,
            "authority_unchanged": True,
            "stage33_progress_unchanged": True,
            "stage33_12_closed_exact": False,
            "next_exact_leaf": "V91C1X_R5A_A2_02_EXCEPTIONAL_STANDARD_BLOWUP_CHARTS_AND_SWAP23_REFINEMENT_SKELETON_HOSTILE_AUDIT",
        },
        "credit_firewall": {
            "h2_fixedness_credit": False,
            "marked_brauer_credit": False,
            "stage33_12_close_credit": False,
            "stage33_13_release_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_credit": False,
            "merge_credit": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def write():
    cert = build_certificate()
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("R5A_EXCEPTIONAL_BLOWUP_SWAP23_ATLAS=WROTE")
    print("CERT_SHA256=" + cert["canonical_sha256"])


def check():
    expected = build_certificate()
    if not OUT.exists():
        raise SystemExit("R5A certificate missing")
    actual = json.loads(OUT.read_text(encoding="utf-8"))
    body = dict(actual)
    claimed = body.pop("canonical_sha256")
    if csha(body) != claimed or actual != expected:
        raise SystemExit("R5A recorded certificate drift")
    print("R5A_EXCEPTIONAL_BLOWUP_SWAP23_ATLAS=PASS")
    print("CERT_SHA256=" + claimed)


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--write", action="store_true")
    g.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if args.write:
        write()
    check()


if __name__ == "__main__":
    main()
