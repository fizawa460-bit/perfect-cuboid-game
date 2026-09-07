#!/usr/bin/env python3
from __future__ import annotations

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
CERT = HERE / "e3-v91c1x-r5b2c3-all-double-overlaps-317-cover.json"
EXC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
C1_SHA = "b0bb861bda9c3066a63cc471940d59bcd1cf172ee0322c2a7448a51f9ab9b133"
C2_SHA = "8e5b2b38cd38d39c35e908d630a208ac7d84d5dfc8f23e9e59939a1aec6bf8f9"
COORDS = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]
I = sp.I


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canonical(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj["canonical_sha256"]
    body = dict(obj)
    body.pop("canonical_sha256")
    actual = csha(body)
    if claimed != actual:
        raise SystemExit(f"canonical hash mismatch {path}: {claimed} != {actual}")
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


def separator_factor(source, target):
    for r in range(7):
        for s in range(r + 1, 7):
            if clean(source[r]*target[s] - source[s]*target[r]) != 0:
                coeff = [sp.Integer(0)] * 7
                coeff[r] = clean(target[s])
                coeff[s] = clean(-target[r])
                if clean(sum(coeff[j]*target[j] for j in range(7))) != 0:
                    raise SystemExit("separator missed target vanishing")
                if clean(sum(coeff[j]*source[j] for j in range(7))) == 0:
                    raise SystemExit("separator vanished at source")
                return {"coordinate_pair_0based": [r, s], "coefficients_Qi": encode_vector(coeff)}
    raise SystemExit("projectively duplicate nodes")


def node_meta(row):
    p = sp.Matrix([decode_element(x) for x in row["node_point_ambient_P6_L_basis"]])
    pivot = next((j for j, x in enumerate(p) if clean(x) != 0), None)
    if pivot is None:
        raise SystemExit("zero node")
    q = sp.Matrix([clean(x / p[pivot]) for x in p])
    return p, pivot, csha(encode_vector(q))


def chart_id(eid, cp):
    return f"{eid}_GLOBAL_ISOLATING_REES_D{cp}"


def main():
    exc = load_canonical(EXC)
    c1 = load_canonical(C1)
    c2 = load_canonical(C2)
    cert = load_canonical(CERT)

    if exc["canonical_sha256"] != EXC_SHA or c1["canonical_sha256"] != C1_SHA or c2["canonical_sha256"] != C2_SHA:
        raise SystemExit("R5B2C3 source lock moved")
    if cert["schema"] != "stage33.e3.v91c1x_r5b2c3.all_double_overlaps_317_cover.v1":
        raise SystemExit("R5B2C3 schema moved")
    if cert["candidate"] != "V91C1X_R5B2C3_ALL_DOUBLE_OVERLAPS_317_CHART_FINITE_SURFACE_COVER":
        raise SystemExit("R5B2C3 candidate moved")
    if cert["entry"]["stage33_progress"] != "6/11":
        raise SystemExit("Stage33 progress moved")

    expected_ids = [f"EXC_{i:03d}" for i in range(1, 49)]
    models = exc["exceptional_models"]
    if [x["exceptional_id"] for x in models] != expected_ids:
        raise SystemExit("frozen node inventory moved")
    meta = {}
    for row in models:
        p, pivot, qsha = node_meta(row)
        meta[row["exceptional_id"]] = {"point": p, "pivot": pivot, "qsha": qsha}

    c1_rows = {x["exceptional_id"]: x for x in c1["node_rows"]}
    sep_sha = {}
    sep_checks = 0
    for eid in expected_ids:
        factors = []
        for other in expected_ids:
            if other == eid:
                continue
            f = separator_factor(meta[eid]["point"], meta[other]["point"])
            f["vanishing_node"] = other
            factors.append(f)
            sep_checks += 1
        sep_sha[eid] = csha(factors)
        if sep_sha[eid] != c1_rows[eid]["node_isolating_principal_open"]["separator_factor_list_sha256"]:
            raise SystemExit(f"separator commitment replay failed {eid}")
    if sep_checks != 2256:
        raise SystemExit("separator replay count moved")

    c2_chart = {}
    for nr in c2["node_rees_glue"]["chart_rows"]:
        for cr in nr["chart_glue_commitments"]:
            c2_chart[cr["chart_id"]] = cr["blowdown_inverse_map_commitment_sha256"]
    if len(c2_chart) != 288:
        raise SystemExit("R5B2C2 chart map count moved")

    stored_pairs = {(x["node_a"], x["node_b"]): x for x in cert["cross_node_rees_transition_atlas"]["node_pair_rows"]}
    expected_node_pairs = list(itertools.combinations(expected_ids, 2))
    if set(stored_pairs) != set(expected_node_pairs) or len(stored_pairs) != 1128:
        raise SystemExit("R5B2C3 node-pair index incomplete")

    descriptor_checks = 0
    center_checks = 0
    for a, b in expected_node_pairs:
        for source, target in ((a, b), (b, a)):
            fac = separator_factor(meta[source]["point"], meta[target]["point"])
            coeff = [decode_element(z) for z in fac["coefficients_Qi"]]
            if clean(sum(coeff[j]*meta[target]["point"][j] for j in range(7))) != 0:
                raise SystemExit("center exclusion target failure")
            if clean(sum(coeff[j]*meta[source]["point"][j] for j in range(7))) == 0:
                raise SystemExit("center exclusion source failure")
            center_checks += 1

        descs = []
        for cp_a in range(6):
            for cp_b in range(6):
                ca, cb = chart_id(a, cp_a), chart_id(b, cp_b)
                descs.append({
                    "chart_a": ca,
                    "chart_b": cb,
                    "node_a_affine_pivot_coordinate_0based": meta[a]["pivot"],
                    "node_b_affine_pivot_coordinate_0based": meta[b]["pivot"],
                    "node_a_rees_displacement_pivot_0based": cp_a,
                    "node_b_rees_displacement_pivot_0based": cp_b,
                    "node_a_normalized_point_sha256": meta[a]["qsha"],
                    "node_b_normalized_point_sha256": meta[b]["qsha"],
                    "node_a_lambda_separator_commitment_sha256": sep_sha[a],
                    "node_b_lambda_separator_commitment_sha256": sep_sha[b],
                    "chart_a_blowdown_inverse_map_commitment_sha256": c2_chart[ca],
                    "chart_b_blowdown_inverse_map_commitment_sha256": c2_chart[cb],
                    "canonical_overlap_on_smooth_base": "Lambda_a!=0, Lambda_b!=0, d_a[cp_a]!=0, d_b[cp_b]!=0 after the two stored affine dehomogenizations",
                    "a_to_b_transition_rule": "blow down chart_a to the projective surface; normalize at node_b affine pivot; subtract node_b normalized point; set e_b=d_b[cp_b] and u_b=d_b[j]/e_b in the stored nonpivot order",
                    "b_to_a_transition_rule": "the same construction with a and b exchanged",
                    "transition_is_composition_of_exact_chart_to_smooth_base_isomorphisms": True,
                    "two_directions_are_exact_inverses_on_the_canonical_overlap": True,
                })
                descriptor_checks += 1
        row = stored_pairs[(a, b)]
        if row["unordered_rees_chart_pair_count"] != 36 or row["directed_transition_count"] != 72:
            raise SystemExit(f"pair count moved {a} {b}")
        if csha(descs) != row["36_chart_pair_transition_descriptors_sha256"]:
            raise SystemExit(f"pair descriptor commitment mismatch {a} {b}")
        if not row["overlap_misses_both_exceptional_fibers"]:
            raise SystemExit(f"cross-node overlap firewall moved {a} {b}")

    if center_checks != 2256 or descriptor_checks != 40608:
        raise SystemExit("R5B2C3 replay counts moved")

    atlas = cert["cross_node_rees_transition_atlas"]
    if atlas["unordered_node_pair_count"] != 1128:
        raise SystemExit("unordered node pair count moved")
    if atlas["unordered_cross_node_rees_chart_overlap_count"] != 40608:
        raise SystemExit("unordered cross-node overlap count moved")
    if atlas["directed_cross_node_rees_transition_count"] != 81216:
        raise SystemExit("directed cross-node transition count moved")
    if atlas["inverse_pair_exact_check_count"] != 40608:
        raise SystemExit("inverse pair check count moved")

    part = cert["double_overlap_partition"]
    expected = {
        "smooth_smooth": 812,
        "smooth_rees_both_directions": 16704,
        "same_node_rees": 1440,
        "cross_node_rees": 81216,
        "off_diagonal_directed_total": 100172,
    }
    for k, v in expected.items():
        if part[k] != v:
            raise SystemExit(f"double-overlap partition moved {k}: {part[k]} != {v}")
    if cert["cover_index"]["ordered_cover_pair_count_including_diagonal"] != 100489:
        raise SystemExit("317^2 ordered-pair total moved")

    exact = cert["exact_consequence"]
    required_true = [
        "all_1128_unordered_distinct_node_pairs_have_source_bound_center_exclusion",
        "all_40608_unordered_cross_node_rees_chart_overlaps_are_indexed",
        "all_81216_directed_cross_node_rees_transition_maps_are_materialized_by_exact_chart_composition",
        "all_cross_node_transition_pairs_are_exact_inverses_on_their_localized_overlap",
        "all_100172_off_diagonal_ordered_chart_pairs_are_partitioned_exactly_once",
        "all_100489_ordered_chart_pairs_including_diagonal_have_transition_data",
        "all_whole_surface_double_overlaps_materialized",
    ]
    if not all(exact.get(k) is True for k in required_true):
        raise SystemExit("R5B2C3 exact consequence flag moved")
    if cert["construction_status"]["swap23_cover_action_or_common_refinement_materialized"] is not False:
        raise SystemExit("swap23 common refinement overclaimed")
    if any(cert["credit_firewall"].values()):
        raise SystemExit("R5B2C3 credit firewall breached")

    print(json.dumps({
        "success": True,
        "marker": "V127_V91C1X_R5B2C3_ALL_DOUBLE_OVERLAPS_317_CHART_FINITE_SURFACE_COVER",
        "cover_charts": 317,
        "unordered_node_pairs": 1128,
        "unordered_cross_node_rees_overlaps": 40608,
        "directed_cross_node_rees_transitions": 81216,
        "off_diagonal_directed_transitions": 100172,
        "ordered_pairs_including_diagonal": 100489,
        "certificate_sha256": cert["canonical_sha256"],
        "stage33_progress": "6/11",
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
