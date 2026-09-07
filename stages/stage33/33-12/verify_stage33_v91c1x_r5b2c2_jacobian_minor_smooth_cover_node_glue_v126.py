#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1x-r5b2c2-jacobian-minor-smooth-cover-node-glue.json"
MAT = HERE / "materialize_e3_v91c1x_r5b2c2_jacobian_minor_smooth_cover_node_glue.py"


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
    cert = load_canonical(CERT)
    if cert["schema"] != "stage33.e3.v91c1x_r5b2c2.jacobian_minor_smooth_cover_node_glue.v1":
        raise SystemExit("R5B2C2 schema moved")
    if cert["candidate"] != "V91C1X_R5B2C2_JACOBIAN_MINOR_SMOOTH_COMPLEMENT_COVER_AND_48_NODE_REES_GLUE":
        raise SystemExit("R5B2C2 candidate moved")
    if cert["entry"]["stage33_progress"] != "6/11":
        raise SystemExit("Stage33 progress changed inside noncredit R5B2C2")

    sing = cert["singular_locus_exact_enumeration"]
    if sing["nonzero_coordinate_support_patterns_examined"] != 127:
        raise SystemExit("support enumeration count moved")
    if sing["rank_deficient_surface_compatible_support_pattern_count"] != 6:
        raise SystemExit("singular support pattern count moved")
    if sing["enumerated_projective_singular_point_count"] != 48:
        raise SystemExit("singular point count moved")
    if not sing["equals_frozen_48_node_inventory_exactly"]:
        raise SystemExit("singular locus no longer equals frozen node inventory")
    if len(sing["support_rows"]) != 6 or any(x["projective_point_count"] != 8 for x in sing["support_rows"]):
        raise SystemExit("6x8 singular-family partition moved")

    smooth = cert["smooth_complement_cover"]
    if smooth["all_4x4_column_subsets"] != 35 or smooth["identically_zero_reduced_minor_count"] != 6:
        raise SystemExit("Jacobian minor inventory moved")
    if smooth["nonzero_reduced_minor_count"] != 29 or len(smooth["minor_rows"]) != 29:
        raise SystemExit("nonzero Jacobian minor count moved")
    if not smooth["smooth_complement_is_union_of_29_principal_minor_opens"]:
        raise SystemExit("smooth complement cover flag false")
    if smooth["directed_smooth_smooth_identity_overlap_transition_count"] != 29*28:
        raise SystemExit("smooth/smooth overlap count moved")

    glue = cert["node_rees_glue"]
    if glue["node_count"] != 48 or glue["rees_chart_count"] != 288:
        raise SystemExit("node/Rees count moved")
    if glue["smooth_rees_overlap_count"] != 288*29:
        raise SystemExit("smooth/Rees overlap count moved")
    if glue["directed_smooth_rees_transition_count"] != 2*288*29:
        raise SystemExit("directed smooth/Rees transition count moved")
    if not glue["all_288_blowdown_inverse_roundtrips_verified"]:
        raise SystemExit("Rees blowdown/inverse roundtrip flag false")
    if glue["prior_same_node_directed_internal_rees_transition_count"] != 1440:
        raise SystemExit("prior internal Rees overlap count moved")

    cover = cert["finite_cover"]
    if cover["smooth_minor_chart_count"] != 29 or cover["node_rees_chart_count"] != 288:
        raise SystemExit("finite cover partition moved")
    if cover["total_cover_chart_count"] != 317 or not cover["whole_resolved_surface_is_covered"]:
        raise SystemExit("finite whole-surface cover not materialized")

    status = cert["construction_status"]
    required_true = [
        "smooth_complement_principal_cover_materialized",
        "exact_singular_locus_equals_frozen_48_nodes",
        "smooth_to_rees_glue_materialized",
        "finite_whole_resolved_surface_cover_materialized",
    ]
    if any(not status[k] for k in required_true):
        raise SystemExit("R5B2C2 constructive status regressed")
    required_false = [
        "all_whole_surface_double_overlaps_materialized",
        "cross_node_rees_to_rees_overlap_transitions_materialized",
        "swap23_cover_action_or_common_refinement_materialized",
        "literal_mu2_2_cocycle_materialized",
        "equivalent_unimodular_cech_glue_materialized",
    ]
    if any(status[k] for k in required_false):
        raise SystemExit("R5B2C2 overclaimed later construction")
    if any(cert["credit_firewall"].values()):
        raise SystemExit("R5B2C2 credit firewall opened")

    replay = subprocess.check_output([sys.executable, str(MAT)], text=True)
    replay_obj = json.loads(replay)
    if not replay_obj.get("success"):
        raise SystemExit("R5B2C2 replay failed")
    if replay_obj["certificate_sha256"] != cert["canonical_sha256"]:
        raise SystemExit("R5B2C2 replay canonical SHA mismatch")
    if replay_obj["finite_cover_charts"] != 317 or replay_obj["singular_points"] != 48:
        raise SystemExit("R5B2C2 replay counts moved")

    print(json.dumps({
        "success": True,
        "marker": "V126_V91C1X_R5B2C2_JACOBIAN_MINOR_SMOOTH_COMPLEMENT_COVER_AND_48_NODE_REES_GLUE",
        "singular_support_patterns": 6,
        "singular_points": 48,
        "smooth_minor_charts": 29,
        "node_rees_charts": 288,
        "finite_cover_charts": 317,
        "smooth_rees_overlaps": 288*29,
        "certificate_sha256": cert["canonical_sha256"],
        "stage33_progress": "6/11",
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
