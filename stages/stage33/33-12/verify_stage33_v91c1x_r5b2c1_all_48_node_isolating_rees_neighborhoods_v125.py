#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
CERT = HERE / "e3-v91c1x-r5b2c1-all-48-node-isolating-rees-neighborhoods.json"
EXC = S07 / "exceptional-p1-tangent-coordinates.json"
EXC_CANONICAL = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canonical(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj["canonical_sha256"]
    body = dict(obj)
    body.pop("canonical_sha256")
    actual = csha(body)
    if claimed != actual:
        raise SystemExit(f"canonical hash mismatch {path}: claimed={claimed} actual={actual}")
    return obj


def main():
    src = load_canonical(EXC)
    if src["canonical_sha256"] != EXC_CANONICAL:
        raise SystemExit("exceptional P1 tangent source lock moved")

    cert = load_canonical(CERT)
    if cert["schema"] != "stage33.e3.v91c1x_r5b2c1.all_48_node_isolating_rees_neighborhoods.v1":
        raise SystemExit("R5B2C1 schema moved")
    if cert["candidate"] != "V91C1X_R5B2C1_ALL_48_NODE_ISOLATING_REES_NEIGHBORHOODS":
        raise SystemExit("R5B2C1 candidate moved")
    if cert["entry"]["authority"] != "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT":
        raise SystemExit("authority drift")
    if cert["entry"]["stage33_progress"] != "6/11":
        raise SystemExit("Stage33 progress drift")
    if cert["source_locks"]["exceptional_p1_tangent_coordinates_sha256"] != EXC_CANONICAL:
        raise SystemExit("certificate source lock drift")

    expected_counts = {
        "frozen_exceptional_node_count": 48,
        "node_isolating_principal_open_count": 48,
        "separator_vanishing_check_count": 48 * 47,
        "standard_rees_charts_per_node": 6,
        "total_standard_rees_chart_count": 48 * 6,
        "directed_internal_rees_overlap_transitions_per_node": 30,
        "total_directed_internal_rees_overlap_transition_count": 48 * 30,
        "t_saturation_exact_check_count": 48 * 6,
    }
    for key, value in expected_counts.items():
        if cert[key] != value:
            raise SystemExit(f"count moved {key}: {cert[key]} != {value}")

    rows = cert["node_rows"]
    expected_ids = [f"EXC_{i:03d}" for i in range(1, 49)]
    if [r["exceptional_id"] for r in rows] != expected_ids:
        raise SystemExit("node row order moved")
    for row in rows:
        op = row["node_isolating_principal_open"]
        if op["separator_factor_count"] != 47 or op["homogeneous_degree"] != 48:
            raise SystemExit(f"node isolator shape moved {row['exceptional_id']}")
        if not op["nonzero_at_own_node"] or not op["zero_at_all_other_47_frozen_nodes"]:
            raise SystemExit(f"node isolator exact property moved {row['exceptional_id']}")
        if row["standard_rees_chart_count"] != 6 or len(row["standard_rees_chart_commitment_sha256s"]) != 6:
            raise SystemExit(f"Rees commitment count moved {row['exceptional_id']}")
        if row["directed_internal_rees_overlap_transition_count"] != 30:
            raise SystemExit(f"internal overlap count moved {row['exceptional_id']}")

    exact = cert["exact_consequence"]
    required_true = [
        "all_48_frozen_nodes_are_distinct_projective_surface_points",
        "all_48_have_projective_jacobian_rank_3",
        "all_48_have_adapted_local_generator_orders_1_1_1_2",
        "all_48_have_nondegenerate_odp_tangent_quadratic",
        "all_48_have_source_bound_principal_opens_containing_that_node_and_excluding_the_other_47_frozen_nodes",
        "all_48_node_opens_have_six_exact_standard_rees_charts",
        "all_288_rees_chart_strict_transform_ideals_equal_t_saturation_of_pullback_ideals",
        "all_48_internal_rees_atlases_have_all_30_directed_standard_overlap_recipes",
        "all_48_exceptional_fibers_are_covered_by_their_six_standard_rees_charts",
    ]
    if any(exact[k] is not True for k in required_true):
        raise SystemExit("R5B2C1 exact consequence regressed")

    status = cert["construction_status"]
    if status["all_48_frozen_node_neighborhoods_globally_isolated_from_each_other"] is not True:
        raise SystemExit("global node isolation regressed")
    if status["all_48_exceptional_resolution_atlases_materialized"] is not True:
        raise SystemExit("all-48 resolution atlas regressed")
    for key in [
        "smooth_complement_principal_cover_materialized",
        "finite_whole_resolved_surface_cover_materialized",
        "all_whole_surface_double_overlaps_materialized",
        "swap23_cover_action_or_common_refinement_materialized",
        "literal_mu2_2_cocycle_materialized",
        "equivalent_unimodular_cech_glue_materialized",
    ]:
        if status[key] is not False:
            raise SystemExit(f"status firewall moved: {key}")

    expected_next = "V91C1X_R5B2C2_MATERIALIZE_JACOBIAN_MINOR_SMOOTH_COMPLEMENT_COVER_AND_GLUE_TO_ALL_48_NODE_REES_NEIGHBORHOODS"
    if cert["next_exact_leaf"] != expected_next:
        raise SystemExit("next leaf moved")
    if any(v is not False for v in cert["credit_firewall"].values()):
        raise SystemExit("credit firewall opened")

    print(json.dumps({
        "success": True,
        "marker": "V125_V91C1X_R5B2C1_ALL_48_NODE_ISOLATING_REES_NEIGHBORHOODS",
        "certificate_sha256": cert["canonical_sha256"],
        "frozen_nodes": 48,
        "node_isolating_opens": 48,
        "rees_charts": 288,
        "separator_checks": 2256,
        "stage33_progress": "6/11",
        "next_exact_leaf": expected_next,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
