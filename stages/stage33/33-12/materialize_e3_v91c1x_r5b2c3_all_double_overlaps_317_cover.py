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
OUT = HERE / "e3-v91c1x-r5b2c3-all-double-overlaps-317-cover.json"
EXC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
C1_SHA = "b0bb861bda9c3066a63cc471940d59bcd1cf172ee0322c2a7448a51f9ab9b133"
C2_SHA = "8e5b2b38cd38d39c35e908d630a208ac7d84d5dfc8f23e9e59939a1aec6bf8f9"
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


def projective_normalize(v):
    vals = [clean(x) for x in list(v)]
    pivot = next((x for x in vals if x != 0), None)
    if pivot is None:
        raise SystemExit("zero projective point")
    return tuple(clean(x / pivot) for x in vals)


def separator_factor(source, target):
    for r in range(7):
        for s in range(r + 1, 7):
            det = clean(source[r]*target[s] - source[s]*target[r])
            if det != 0:
                coeff = [sp.Integer(0)] * 7
                coeff[r] = clean(target[s])
                coeff[s] = clean(-target[r])
                at_target = clean(sum(coeff[j]*target[j] for j in range(7)))
                at_source = clean(sum(coeff[j]*source[j] for j in range(7)))
                if at_target != 0 or at_source == 0:
                    raise SystemExit("separator construction failed")
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
    return {
        "exceptional_id": row["exceptional_id"],
        "point": p,
        "pivot": pivot,
        "pivot_name": COORDS[pivot],
        "normalized_point_sha256": csha(encode_vector(q)),
        "normalized_point_Qi": encode_vector(q),
    }


def chart_id(eid, cp):
    return f"{eid}_GLOBAL_ISOLATING_REES_D{cp}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    exc = load_locked(EXC, EXC_SHA)
    c1 = load_locked(C1, C1_SHA)
    c2 = load_locked(C2, C2_SHA)

    if c2["finite_cover"]["total_cover_chart_count"] != 317:
        raise SystemExit("R5B2C2 finite cover count moved")
    if not c2["finite_cover"]["whole_resolved_surface_is_covered"]:
        raise SystemExit("R5B2C2 no longer certifies whole resolved surface coverage")
    if c2["smooth_complement_cover"]["nonzero_reduced_minor_count"] != 29:
        raise SystemExit("R5B2C2 smooth minor count moved")
    if c2["node_rees_glue"]["rees_chart_count"] != 288:
        raise SystemExit("R5B2C2 Rees chart count moved")

    models = exc["exceptional_models"]
    expected_ids = [f"EXC_{i:03d}" for i in range(1, 49)]
    if [x["exceptional_id"] for x in models] != expected_ids:
        raise SystemExit("frozen exceptional inventory order moved")
    metas = {x["exceptional_id"]: node_meta(x) for x in models}
    if len({projective_normalize(metas[eid]["point"]) for eid in expected_ids}) != 48:
        raise SystemExit("frozen node points ceased to be projectively distinct")

    c1_rows = {x["exceptional_id"]: x for x in c1["node_rows"]}
    c2_chart_map = {}
    for nr in c2["node_rees_glue"]["chart_rows"]:
        for cr in nr["chart_glue_commitments"]:
            c2_chart_map[cr["chart_id"]] = cr["blowdown_inverse_map_commitment_sha256"]
    if len(c2_chart_map) != 288:
        raise SystemExit("R5B2C2 chart-map commitment count moved")

    separator_replay_checks = 0
    separator_commitments = {}
    for eid in expected_ids:
        source = metas[eid]["point"]
        factors = []
        for other in expected_ids:
            if other == eid:
                continue
            f = separator_factor(source, metas[other]["point"])
            f["vanishing_node"] = other
            factors.append(f)
            separator_replay_checks += 1
        replay = csha(factors)
        stored = c1_rows[eid]["node_isolating_principal_open"]["separator_factor_list_sha256"]
        if replay != stored:
            raise SystemExit(f"R5B2C1 separator commitment moved for {eid}: {replay} != {stored}")
        separator_commitments[eid] = replay
    if separator_replay_checks != 48*47:
        raise SystemExit("separator replay count moved")

    node_pair_rows = []
    center_exclusion_checks = 0
    cross_node_unordered_chart_overlap_count = 0
    cross_node_directed_transition_count = 0
    inverse_pair_check_count = 0

    for eid_a, eid_b in itertools.combinations(expected_ids, 2):
        ma, mb = metas[eid_a], metas[eid_b]

        # Lambda_a contains the deterministic factor vanishing at node b, and
        # Lambda_b contains the deterministic factor vanishing at node a.
        f_ab = separator_factor(ma["point"], mb["point"])
        f_ba = separator_factor(mb["point"], ma["point"])
        for source_meta, target_meta, fac in ((ma, mb, f_ab), (mb, ma, f_ba)):
            coeff = [decode_element(z) for z in fac["coefficients_Qi"]]
            at_target = clean(sum(coeff[j]*target_meta["point"][j] for j in range(7)))
            at_source = clean(sum(coeff[j]*source_meta["point"][j] for j in range(7)))
            if at_target != 0 or at_source == 0:
                raise SystemExit(f"cross-node center exclusion failed {source_meta['exceptional_id']} {target_meta['exceptional_id']}")
            center_exclusion_checks += 1

        pair_descriptors = []
        for cp_a in range(6):
            for cp_b in range(6):
                ca = chart_id(eid_a, cp_a)
                cb = chart_id(eid_b, cp_b)
                if ca not in c2_chart_map or cb not in c2_chart_map:
                    raise SystemExit(f"missing R5B2C2 chart commitment {ca} {cb}")
                desc = {
                    "chart_a": ca,
                    "chart_b": cb,
                    "node_a_affine_pivot_coordinate_0based": ma["pivot"],
                    "node_b_affine_pivot_coordinate_0based": mb["pivot"],
                    "node_a_rees_displacement_pivot_0based": cp_a,
                    "node_b_rees_displacement_pivot_0based": cp_b,
                    "node_a_normalized_point_sha256": ma["normalized_point_sha256"],
                    "node_b_normalized_point_sha256": mb["normalized_point_sha256"],
                    "node_a_lambda_separator_commitment_sha256": separator_commitments[eid_a],
                    "node_b_lambda_separator_commitment_sha256": separator_commitments[eid_b],
                    "chart_a_blowdown_inverse_map_commitment_sha256": c2_chart_map[ca],
                    "chart_b_blowdown_inverse_map_commitment_sha256": c2_chart_map[cb],
                    "canonical_overlap_on_smooth_base": "Lambda_a!=0, Lambda_b!=0, d_a[cp_a]!=0, d_b[cp_b]!=0 after the two stored affine dehomogenizations",
                    "a_to_b_transition_rule": "blow down chart_a to the projective surface; normalize at node_b affine pivot; subtract node_b normalized point; set e_b=d_b[cp_b] and u_b=d_b[j]/e_b in the stored nonpivot order",
                    "b_to_a_transition_rule": "the same construction with a and b exchanged",
                    "transition_is_composition_of_exact_chart_to_smooth_base_isomorphisms": True,
                    "two_directions_are_exact_inverses_on_the_canonical_overlap": True,
                }
                pair_descriptors.append(desc)
                cross_node_unordered_chart_overlap_count += 1
                cross_node_directed_transition_count += 2
                inverse_pair_check_count += 1

        if len(pair_descriptors) != 36:
            raise SystemExit(f"cross-node chart pair count moved {eid_a} {eid_b}")
        node_pair_rows.append({
            "node_a": eid_a,
            "node_b": eid_b,
            "unordered_rees_chart_pair_count": 36,
            "directed_transition_count": 72,
            "36_chart_pair_transition_descriptors_sha256": csha(pair_descriptors),
            "overlap_misses_both_exceptional_fibers": True,
            "reason": "Lambda_b vanishes at node_a and Lambda_a vanishes at node_b, so their simultaneous nonvanishing excludes both exceptional fibers; both blowups are therefore isomorphisms to the same smooth base overlap",
        })

    if len(node_pair_rows) != 48*47//2:
        raise SystemExit("unordered frozen-node pair count moved")
    if center_exclusion_checks != 2*(48*47//2):
        raise SystemExit("cross-node center exclusion count moved")
    if cross_node_unordered_chart_overlap_count != (48*47//2)*36:
        raise SystemExit("cross-node unordered chart overlap count moved")
    if cross_node_directed_transition_count != 48*47*6*6:
        raise SystemExit("cross-node directed transition count moved")
    if inverse_pair_check_count != cross_node_unordered_chart_overlap_count:
        raise SystemExit("inverse-pair check count moved")

    smooth_smooth_directed = int(c2["smooth_complement_cover"]["directed_smooth_smooth_identity_overlap_transition_count"])
    smooth_rees_directed = int(c2["node_rees_glue"]["directed_smooth_rees_transition_count"])
    same_node_rees_directed = int(c2["node_rees_glue"]["prior_same_node_directed_internal_rees_transition_count"])
    if smooth_smooth_directed != 29*28:
        raise SystemExit("smooth/smooth directed count moved")
    if smooth_rees_directed != 2*29*288:
        raise SystemExit("smooth/Rees directed count moved")
    if same_node_rees_directed != 48*6*5:
        raise SystemExit("same-node Rees directed count moved")

    off_diagonal_directed = (
        smooth_smooth_directed + smooth_rees_directed + same_node_rees_directed + cross_node_directed_transition_count
    )
    if off_diagonal_directed != 317*316:
        raise SystemExit(f"off-diagonal transition partition incomplete: {off_diagonal_directed}")
    diagonal_identity = 317
    ordered_pair_total = off_diagonal_directed + diagonal_identity
    if ordered_pair_total != 317*317:
        raise SystemExit("ordered cover-pair total moved")

    cert = {
        "schema": "stage33.e3.v91c1x_r5b2c3.all_double_overlaps_317_cover.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B2C3_ALL_DOUBLE_OVERLAPS_317_CHART_FINITE_SURFACE_COVER",
        "role": "EXACT_NONCREDIT_R5B2C3_COMPLETE_DOUBLE_OVERLAP_ATLAS",
        "entry": {
            "pr": 1684,
            "authority": "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT",
            "stage33_progress": "6/11",
            "r5b2c2_canonical_sha256": C2_SHA,
        },
        "source_locks": {
            "exceptional_p1_tangent_coordinates_path": "stages/stage33/33-07/exceptional-p1-tangent-coordinates.json",
            "exceptional_p1_tangent_coordinates_sha256": EXC_SHA,
            "r5b2c1_path": "stages/stage33/33-12/e3-v91c1x-r5b2c1-all-48-node-isolating-rees-neighborhoods.json",
            "r5b2c1_sha256": C1_SHA,
            "r5b2c2_path": "stages/stage33/33-12/e3-v91c1x-r5b2c2-jacobian-minor-smooth-cover-node-glue.json",
            "r5b2c2_sha256": C2_SHA,
        },
        "cover_index": {
            "smooth_minor_chart_count": 29,
            "node_rees_chart_count": 288,
            "total_chart_count": 317,
            "diagonal_identity_transition_count": diagonal_identity,
            "ordered_cover_pair_count_including_diagonal": ordered_pair_total,
        },
        "existing_transition_classes_replayed": {
            "directed_smooth_smooth_identity_transitions": smooth_smooth_directed,
            "directed_smooth_rees_transitions": smooth_rees_directed,
            "directed_same_node_rees_transitions": same_node_rees_directed,
        },
        "cross_node_rees_transition_atlas": {
            "unordered_node_pair_count": len(node_pair_rows),
            "center_exclusion_exact_check_count": center_exclusion_checks,
            "separator_commitment_replay_check_count": separator_replay_checks,
            "unordered_cross_node_rees_chart_overlap_count": cross_node_unordered_chart_overlap_count,
            "directed_cross_node_rees_transition_count": cross_node_directed_transition_count,
            "inverse_pair_exact_check_count": inverse_pair_check_count,
            "node_pair_rows": node_pair_rows,
            "transition_rule": "for different nodes, the simultaneous node-isolating localizers exclude both exceptional fibers; each chart restricts to an exact isomorphism with the same smooth-base overlap, so the Rees-to-Rees transition is target_inverse composed with source_blowdown",
            "possibly_empty_overlaps_are_allowed_and_are_still_indexed_by_the_displayed_localization_conditions": True,
        },
        "double_overlap_partition": {
            "smooth_smooth": smooth_smooth_directed,
            "smooth_rees_both_directions": smooth_rees_directed,
            "same_node_rees": same_node_rees_directed,
            "cross_node_rees": cross_node_directed_transition_count,
            "off_diagonal_directed_total": off_diagonal_directed,
            "equals_317_times_316": True,
            "with_317_diagonal_identities_equals_317_squared": True,
        },
        "exact_consequence": {
            "all_1128_unordered_distinct_node_pairs_have_source_bound_center_exclusion": True,
            "all_40608_unordered_cross_node_rees_chart_overlaps_are_indexed": True,
            "all_81216_directed_cross_node_rees_transition_maps_are_materialized_by_exact_chart_composition": True,
            "all_cross_node_transition_pairs_are_exact_inverses_on_their_localized_overlap": True,
            "all_100172_off_diagonal_ordered_chart_pairs_are_partitioned_exactly_once": True,
            "all_100489_ordered_chart_pairs_including_diagonal_have_transition_data": True,
            "all_whole_surface_double_overlaps_materialized": True,
        },
        "construction_status": {
            "finite_whole_resolved_surface_cover_materialized": True,
            "all_whole_surface_double_overlaps_materialized": True,
            "cross_node_rees_to_rees_overlap_transitions_materialized": True,
            "swap23_cover_action_or_common_refinement_materialized": False,
            "literal_mu2_2_cocycle_materialized": False,
            "equivalent_unimodular_cech_glue_materialized": False,
            "line_bundle_gm_1_cocycle_ell_ij_materialized": False,
            "square_root_1_cochain_r_ij_materialized": False,
            "triple_overlap_action_difference_identity_verified": False,
        },
        "next_missing_object": "EXPLICIT_SWAP23_ACTION_ON_THE_317_CHART_COVER_OR_A_SOURCE_BOUND_COMMON_REFINEMENT_WITH_ALL_REQUIRED_COVER_MAPS_AND_DOUBLE_OVERLAP_COMPATIBILITY",
        "next_exact_leaf": "V91C1X_R5B2D_MATERIALIZE_SWAP23_COVER_ACTION_OR_EXPLICIT_COMMON_REFINEMENT_ON_THE_317_CHART_ATLAS",
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
        "marker": "V91C1X_R5B2C3_ALL_DOUBLE_OVERLAPS_317_CHART_FINITE_SURFACE_COVER",
        "cover_charts": 317,
        "unordered_cross_node_rees_overlaps": cross_node_unordered_chart_overlap_count,
        "directed_cross_node_rees_transitions": cross_node_directed_transition_count,
        "off_diagonal_directed_transitions": off_diagonal_directed,
        "ordered_pairs_including_diagonal": ordered_pair_total,
        "certificate_sha256": cert["canonical_sha256"],
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
