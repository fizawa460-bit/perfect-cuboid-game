#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1x-r5b2b3a-a2-02-24-side-exceptional-crossing-uniformizer-charts.json"
MAT = HERE / "materialize_e3_v91c1x_r5b2b3a_24_side_exceptional_crossing_uniformizer_charts_v3.py"
TARGET_SIDES = [2, 4, 6, 8]
PARAMETERS = ["0", "infinity", "1", "-1", "i", "-i"]
ZERO_QI = [0, 1, 0, 1]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


cert = json.loads(CERT.read_text(encoding="utf-8"))
claimed = cert["canonical_sha256"]
body = dict(cert)
body.pop("canonical_sha256")
assert claimed == csha(body)
assert cert["schema"] == "stage33.e3.v91c1x_r5b2b3a.a2_02_24_side_exceptional_crossing_uniformizer_charts.v3"
assert cert["candidate"] == "V91C1X_R5B2B3A_A2_02_24_SIDE_EXCEPTIONAL_CROSSING_UNIFORMIZER_CHARTS"
assert cert["role"] == "EXACT_NONCREDIT_R5B2B3A_SOURCE_BOUND_SIDE_EXCEPTIONAL_CROSSING_NEIGHBORHOOD_CONSTRUCTION"
assert cert["entry"]["authority"] == "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
assert cert["entry"]["stage33_progress"] == "6/11"
assert cert["entry"]["r5b2a_canonical_sha256"] == "dc3c875eaa006f89386749e332e0e4559c2af0b0a4cb0fe9aa97aecbf0944534"
assert cert["entry"]["r5b2b1_canonical_sha256"] == "02f0362bce42716a18ff709e350587775cd7edbdcc99d71af39b49b01c63651d"
assert cert["entry"]["r5b2b2_canonical_sha256"] == "305841c0d906c4d65aa08d6acac5e821991dabc364bd7f5890fa75f06dbde98e"
assert cert["source_locks"]["side_parametrization_source_git_blob_sha1"] == "02682d9d7648e683b9d26fca86efba02118ba8a3"
assert cert["source_locks"]["side_parametrization_source_actual_git_blob_sha1"] == "02682d9d7648e683b9d26fca86efba02118ba8a3"
assert cert["target_side_components"] == [f"SIDE_{x:03d}" for x in TARGET_SIDES]
assert cert["target_side_count"] == 4
assert cert["side_exceptional_crossing_count"] == 24
assert len(cert["crossing_neighborhood_rows"]) == 4

seen = set()
for side_row, side in zip(cert["crossing_neighborhood_rows"], TARGET_SIDES):
    assert side_row["component_id"] == f"SIDE_{side:03d}"
    assert side_row["side_index_1based"] == side
    assert side_row["family"] == "A1"
    assert side_row["crossing_neighborhood_count"] == 6
    assert len(side_row["crossing_neighborhoods"]) == 6
    assert [x["side_parameter"] for x in side_row["crossing_neighborhoods"]] == PARAMETERS
    assert [x["side_parameter_index_1based"] for x in side_row["crossing_neighborhoods"]] == list(range(1, 7))
    assert len(side_row["homogeneous_side_ideal_generators"]) == 4
    for crossing in side_row["crossing_neighborhoods"]:
        key = (side, crossing["side_parameter"], crossing["exceptional_id"])
        assert key not in seen
        seen.add(key)
        assert crossing["canonical_rees_chart_pivot_displacement_index_0based"] in crossing["valid_standard_rees_chart_pivots_from_side_tangent"]
        assert len(crossing["side_tangent_displacement_direction_Qi"]) == 6
        assert len(crossing["crossing_rees_chart_point"]["u_Qi_in_chart_order"]) == 5
        assert crossing["crossing_rees_chart_point"]["e_Qi"] == ZERO_QI
        assert len(crossing["side_strict_transform_generators_Qi"]) == 4
        assert 0 <= crossing["selected_side_uniformizer_generator_index_0based"] < 4
        assert crossing["literal_exceptional_uniformizer"] == "e"
        assert crossing["surface_jacobian_rank_at_crossing"] == 4
        assert crossing["surface_plus_side_uniformizer_jacobian_rank_at_crossing"] == 5
        assert crossing["surface_plus_side_plus_exceptional_jacobian_rank_at_crossing"] == 6

        op = crossing["distinguished_open"]
        assert op["condition"] == "lambda != 0"
        assert op["lambda_construction"] == "crossing transversality determinant times one nonvanishing exact colon witness for each strict-side generator modulo (surface,s)"
        assert op["crossing_transversality_determinant_at_crossing_Qi"] != ZERO_QI
        witnesses = op["exact_colon_witnesses"]
        assert len(witnesses) == 4
        assert [w["strict_side_generator_index_0based"] for w in witnesses] == [0, 1, 2, 3]
        for witness in witnesses:
            assert isinstance(witness["already_in_surface_plus_s_ideal"], bool)
            assert witness["colon_witness_at_crossing_Qi"] != ZERO_QI
        assert op["lambda_at_crossing_Qi"] != ZERO_QI

        checks = crossing["exact_local_checks"]
        assert checks["parameterized_side_point_matches_b2b1_node"] is True
        assert checks["side_tangent_selects_canonical_rees_chart"] is True
        assert checks["all_four_side_linear_pullbacks_equal_e_times_strict_generators"] is True
        assert checks["combined_surface_plus_side_pullback_e_saturation_equals_strict_transform_ideal"] is True
        assert checks["each_colon_witness_times_its_strict_side_generator_lies_in_surface_plus_selected_s_ideal"] is True
        assert checks["all_colon_witnesses_are_nonzero_at_the_crossing"] is True
        assert checks["on_D_lambda_surface_plus_selected_s_equals_full_strict_side_ideal"] is True
        assert checks["lambda_is_nonzero_at_the_crossing"] is True
        assert checks["selected_s_is_literal_local_side_uniformizer"] is True
        assert checks["e_is_literal_local_exceptional_uniformizer"] is True
        assert checks["side_and_exceptional_are_transverse_regular_parameters_on_resolved_surface"] is True

        overlap = crossing["cross_overlap_map"]
        assert overlap["target"] == crossing["canonical_rees_chart_id"]
        assert overlap["open_embedding"] == "localize the same Rees chart at lambda"
        assert overlap["exceptional_uniformizer_transition"] == "e_target=e_source"
        assert overlap["ambient_chart_variable_map"] == {"e": "e", "u0": "u0", "u1": "u1", "u2": "u2", "u3": "u3", "u4": "u4"}
assert len(seen) == 24

counts = cert["exact_check_counts"]
assert counts["combined_pullback_e_saturation_pass_count"] == 24
assert counts["exact_colon_localizer_pass_count"] == 24
assert counts["localized_principal_side_uniformizer_pass_count"] == 24
assert counts["side_exceptional_transversality_pass_count"] == 24

con = cert["exact_consequence"]
assert con["all_24_target_side_exceptional_crossings_have_source_bound_rees_neighborhoods"] is True
assert con["all_24_crossings_have_exact_colon_localizers"] is True
assert con["all_24_crossings_have_literal_local_side_uniformizers"] is True
assert con["all_24_crossings_have_literal_exceptional_uniformizer_e"] is True
assert con["all_24_crossings_have_exact_side_to_exceptional_cross_overlap_open_embeddings"] is True
assert con["all_24_side_strict_transform_ideals_are_verified_by_combined_e_saturation"] is True
assert con["all_24_side_exceptional_pairs_are_transverse_regular_parameters_on_the_resolved_surface"] is True
assert con["four_target_side_full_strict_transform_neighborhoods_are_covered_away_from_exceptional_crossings"] is False

status = cert["construction_status"]
assert status["full_16_exceptional_rees_atlases_materialized"] is True
assert status["four_target_side_crossing_neighborhood_atlases_materialized"] is True
assert status["side_component_uniformizers_at_all_24_side_exceptional_crossings_materialized"] is True
assert status["side_to_exceptional_cross_overlap_maps_at_all_24_crossings_materialized"] is True
assert status["four_target_side_away_from_exceptional_neighborhoods_materialized"] is False
assert status["four_target_side_full_strict_transform_neighborhoods_materialized"] is False
assert status["finite_surface_cover_materialized"] is False
assert status["surface_all_double_overlap_transitions_materialized"] is False
assert cert["next_missing_object"] == "SOURCE_BOUND_AWAY_FROM_EXCEPTIONAL_NEIGHBORHOODS_COVERING_THE_FOUR_TARGET_SIDE_STRICT_TRANSFORMS_PLUS_OVERLAP_MAPS_TO_THE_24_CROSSING_OPENS"
assert cert["next_exact_leaf"] == "V91C1X_R5B2B3B_COVER_FOUR_TARGET_SIDE_STRICT_TRANSFORMS_AWAY_FROM_EXCEPTIONAL_CROSSINGS_AND_GLUE_TO_24_CROSSING_OPENS"
for key, value in cert["credit_firewall"].items():
    assert value is False, key

replay = subprocess.run([sys.executable, str(MAT)], check=True, capture_output=True, text=True)
summary = json.loads(replay.stdout.strip().splitlines()[-1])
assert summary["success"] is True
assert summary["certificate_sha256"] == claimed
assert summary["side_count"] == 4
assert summary["crossing_count"] == 24
assert summary["combined_saturation_pass_count"] == 24
assert summary["exact_colon_localizer_pass_count"] == 24
assert summary["localized_principal_pass_count"] == 24
assert summary["transversality_pass_count"] == 24
assert summary["next_exact_leaf"] == cert["next_exact_leaf"]

print(json.dumps({
    "success": True,
    "marker": "V123_V91C1X_R5B2B3A_24_SIDE_EXCEPTIONAL_CROSSING_UNIFORMIZER_CHARTS_COLON_LOCALIZED",
    "certificate_sha256": claimed,
    "side_count": 4,
    "crossing_count": 24,
    "combined_saturation_pass_count": 24,
    "exact_colon_localizer_pass_count": 24,
    "localized_principal_pass_count": 24,
    "transversality_pass_count": 24,
    "stage33_progress": "6/11",
    "next_exact_leaf": cert["next_exact_leaf"],
}, sort_keys=True))
