#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S07 = HERE.parent / "33-07"
SRC = S07 / "exceptional-p1-tangent-coordinates.json"
R5B1 = HERE / "e3-v91c1x-r5b1-a2-02-exceptional-basepoint-free-cover.json"
OUT = HERE / "e3-v91c1x-r5b2a-a2-02-target-side-incidence-closure.json"
SRC_SHA = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
R5B1_SHA = "b5398d05f7f7799da3edb87aa5e81ab03cb30734dda0a3763222c468d812f54d"
TARGET_SIDES = [2, 4, 6, 8]
TARGET_EXC = ["EXC_003", "EXC_004", "EXC_011", "EXC_012"]
EXPECTED_PARAMETERS = ["0", "infinity", "1", "-1", "i", "-i"]


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    src = load_locked(SRC, SRC_SHA)
    r5b1 = load_locked(R5B1, R5B1_SHA)
    assert r5b1["target_exceptional_components"] == TARGET_EXC

    side_rows = []
    incidence_pairs = []
    closure = set()
    for side in TARGET_SIDES:
        rows = []
        for er in src["exceptional_models"]:
            eid = er["exceptional_id"]
            for cr in er["physical_crossing_tangent_coordinates"]:
                if int(cr["side_index_1based"]) != side:
                    continue
                rec = {
                    "exceptional_id": eid,
                    "side_parameter": cr["side_parameter"],
                    "side_parameter_index_1based": int(cr["side_parameter_index_1based"]),
                    "exceptional_P1_homogeneous_coordinate_L_basis": cr["exceptional_P1_homogeneous_coordinate_L_basis"],
                    "exceptional_tangent_model_sha256": er["full_tangent_conic_coordinate_model_sha256"],
                }
                rows.append(rec)
                incidence_pairs.append({"side_index_1based": side, **rec})
                closure.add(eid)
        rows.sort(key=lambda x: x["side_parameter_index_1based"])
        params = [x["side_parameter"] for x in rows]
        if len(rows) != 6 or params != EXPECTED_PARAMETERS:
            raise SystemExit(f"side crossing inventory moved SIDE_{side:03d}: count={len(rows)} params={params}")
        side_rows.append({
            "component_id": f"SIDE_{side:03d}",
            "side_index_1based": side,
            "crossing_count": len(rows),
            "crossing_parameters_in_frozen_order": params,
            "incident_exceptional_ids": [x["exceptional_id"] for x in rows],
            "crossings": rows,
        })

    closure_sorted = sorted(closure, key=lambda x: int(x.split("_")[1]))
    target_set = set(TARGET_EXC)
    missing_from_target4 = [x for x in closure_sorted if x not in target_set]
    target4_not_incident = [x for x in TARGET_EXC if x not in closure]
    target4_covers_all_target_side_crossings = len(missing_from_target4) == 0

    cert = {
        "schema": "stage33.e3.v91c1x_r5b2a.a2_02_target_side_incidence_closure.v1",
        "stage": "33-12",
        "candidate": "V91C1X_R5B2A_A2_02_TARGET_SIDE_EXCEPTIONAL_INCIDENCE_CLOSURE",
        "role": "EXACT_NONCREDIT_R5B2A_SURFACE_COVER_SCOPE_DIAGNOSTIC",
        "entry": {
            "pr": 1684,
            "authority": "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT",
            "stage33_progress": "6/11",
            "r5b1_canonical_sha256": R5B1_SHA,
        },
        "source_locks": {
            "exceptional_p1_tangent_coordinates_path": "stages/stage33/33-07/exceptional-p1-tangent-coordinates.json",
            "exceptional_p1_tangent_coordinates_sha256": SRC_SHA,
        },
        "target_side_components": [f"SIDE_{x:03d}" for x in TARGET_SIDES],
        "target_exceptional_components_from_a2_02_support": TARGET_EXC,
        "side_rows": side_rows,
        "incidence_pair_count": len(incidence_pairs),
        "side_incident_exceptional_closure": closure_sorted,
        "side_incident_exceptional_closure_count": len(closure_sorted),
        "additional_exceptionals_required_beyond_target4_for_full_target_side_crossing_cover": missing_from_target4,
        "additional_exceptionals_required_count": len(missing_from_target4),
        "target4_exceptionals_not_incident_to_any_target_side": target4_not_incident,
        "exact_consequence": {
            "each_target_side_has_exactly_six_frozen_exceptional_crossings": True,
            "each_target_side_crossing_parameter_set_is_0_inf_pm1_pmi": True,
            "target4_exceptionals_cover_all_crossings_of_the_four_target_sides": target4_covers_all_target_side_crossings,
            "surface_neighborhood_cover_may_ignore_additional_incident_exceptionals": target4_covers_all_target_side_crossings,
            "r5b1_component_cover_remains_valid_for_its_four_target_exceptionals": True,
        },
        "next_missing_object": (
            "SOURCE_BOUND_REES_BLOWUP_NEIGHBORHOOD_CHARTS_FOR_THE_FULL_TARGET_SIDE_INCIDENT_EXCEPTIONAL_CLOSURE_"
            "PLUS_FOUR_TARGET_SIDE_STRICT_TRANSFORM_NEIGHBORHOODS_WITH_UNIFORMIZER_AND_CROSS_OVERLAP_MAPS"
        ),
        "next_exact_leaf": "V91C1X_R5B2B_BUILD_REES_NEIGHBORHOOD_CHARTS_FOR_TARGET_SIDE_INCIDENCE_CLOSURE_THEN_ATTACH_SIDE_STRICT_TRANSFORM_UNIFORMIZERS",
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
        "marker": "V91C1X_R5B2A_TARGET_SIDE_INCIDENCE_CLOSURE",
        "side_count": 4,
        "incidence_pair_count": len(incidence_pairs),
        "closure_count": len(closure_sorted),
        "additional_exceptional_count": len(missing_from_target4),
        "target4_covers_all_target_side_crossings": target4_covers_all_target_side_crossings,
        "certificate_sha256": cert["canonical_sha256"],
        "next_exact_leaf": cert["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
