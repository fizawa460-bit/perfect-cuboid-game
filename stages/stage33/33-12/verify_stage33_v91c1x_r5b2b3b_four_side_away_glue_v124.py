#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1x-r5b2b3b-a2-02-four-side-away-from-exceptional-glue.json"
MAT = HERE / "materialize_e3_v91c1x_r5b2b3b_four_side_away_glue.py"
TARGET_SIDES = [2, 4, 6, 8]
PARAMETERS = ["0", "infinity", "1", "-1", "i", "-i"]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


cert = json.loads(CERT.read_text(encoding="utf-8"))
claimed = cert["canonical_sha256"]
body = dict(cert)
body.pop("canonical_sha256")
assert claimed == csha(body)
assert cert["schema"] == "stage33.e3.v91c1x_r5b2b3b.a2_02_four_side_away_from_exceptional_glue.v1"
assert cert["candidate"] == "V91C1X_R5B2B3B_A2_02_FOUR_SIDE_AWAY_FROM_EXCEPTIONAL_GLUE"
assert cert["role"] == "EXACT_NONCREDIT_R5B2B3B_SOURCE_BOUND_FOUR_TARGET_SIDE_STRICT_TRANSFORM_COVER_AND_CROSSING_GLUE"
assert cert["entry"]["authority"] == "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
assert cert["entry"]["stage33_progress"] == "6/11"
assert cert["entry"]["r5a_canonical_sha256"] == "76e63baad22a88f7c2b93d31930785c3b4eafe785fdc6de950756b169be7c9ce"
assert cert["entry"]["r5b2a_canonical_sha256"] == "dc3c875eaa006f89386749e332e0e4559c2af0b0a4cb0fe9aa97aecbf0944534"
assert cert["entry"]["r5b2b1_canonical_sha256"] == "02f0362bce42716a18ff709e350587775cd7edbdcc99d71af39b49b01c63651d"
assert cert["entry"]["r5b2b3a_canonical_sha256"] == "2b4a9e291a9413f03fce9216ee94674d0f6802d0f61dc493784809fb75c1f693"
assert cert["source_locks"]["side_ambient_lift_source_sha256"] == "00075c19b97260cbfd51d508d5bfe649724e0333d133e0b8d71c0ec8d6cea797"
assert cert["source_locks"]["side_ambient_lift_source_actual_sha256"] == cert["source_locks"]["side_ambient_lift_source_sha256"]
assert cert["target_side_components"] == [f"SIDE_{x:03d}" for x in TARGET_SIDES]
assert cert["away_side_chart_count"] == 4
assert cert["crossing_glue_overlap_count"] == 24
assert len(cert["away_side_charts"]) == 4
assert len(cert["crossing_glue_overlaps"]) == 24

for row, side in zip(cert["away_side_charts"], TARGET_SIDES):
    assert row["component_id"] == f"SIDE_{side:03d}"
    assert row["side_index_1based"] == side
    assert row["family"] == "A1"
    patch = row["projective_patch"]
    assert patch["condition"] == "D=c-b3 != 0"
    assert patch["normalization"] == "D=c-b3=1"
    assert patch["affine_coordinate_order"] == ["a1", "a2", "a3", "b1", "b2", "b3"]
    assert patch["eliminated_coordinate"] == "c=b3+1"
    assert len(row["surface_equations"]) == 4
    assert len(row["side_ideal_generators"]) == 4
    assert row["literal_side_uniformizer"] == "a1"
    assert len(row["opposite_branch_unit_factors"]) == 3
    assert len(row["principalization_identities"]) == 3
    assert row["localized_principalization_consequence"] == "on D(rho), the full selected-side ideal on the surface equals the principal Cartier ideal (a1)"
    par = row["side_parameter"]
    assert par["parameter"] == "t=b2=N/D=u/v"
    assert par["parameter_variable"] == "t"
    assert len(par["affine_embedding_in_coordinate_order"]) == 6
    assert par["finite_crossing_parameters"] == ["0", "1", "-1", "i", "-i"]
    assert par["infinity_crossing_removed_by_D_patch"] is True
    jac = row["jacobian_coverage"]
    assert jac["both_degeneracy_sets_equal_the_five_finite_crossings"] is True
    assert jac["surface_smooth_on_D_times_rho_nonzero_side_locus"] is True
    assert jac["a1_is_regular_parameter_on_D_times_rho_nonzero_side_locus"] is True
    assert row["coverage_consequence"] == "this single affine principal neighborhood covers SIDE minus its six exceptional crossing points"

seen = set()
for row in cert["crossing_glue_overlaps"]:
    key = (row["side_component_id"], row["side_parameter"], row["exceptional_id"])
    assert key not in seen
    seen.add(key)
    assert row["side_component_id"] in cert["target_side_components"]
    assert row["side_parameter"] in PARAMETERS
    assert row["crossing_source_condition"] == "lambda != 0"
    assert row["overlap_subopen_condition"] == "lambda != 0 AND e != 0 AND D_cross != 0 AND rho_cross != 0"
    assert row["crossing_variables"] == ["e", "u0", "u1", "u2", "u3", "u4"]
    forward = row["cross_to_away_map"]
    assert forward["away_coordinate_order"] == ["a1", "a2", "a3", "b1", "b2", "b3"]
    assert len(forward["numerators_Qi"]) == 6
    assert forward["c_is_reconstructed_as_b3_plus_1"] is True
    inverse = row["away_to_cross_inverse_template"]
    assert 0 <= inverse["node_affine_pivot_coordinate_0based"] <= 6
    assert len(inverse["rees_u_numerators_in_u_order"]) == 5
    trans = row["side_uniformizer_transition"]
    assert trans["away_uniformizer"] == "a1/D"
    assert trans["crossing_uniformizer"] == "a1_aff/e"
    assert trans["unit_multiplier_cross_to_away"] == "e/D_cross"
    assert all(v is True for v in row["exact_checks"].values())
assert len(seen) == 24

counts = cert["exact_check_counts"]
assert counts["away_chart_principalization_count"] == 4
assert counts["away_chart_smoothness_and_cartier_rank_coverage_count"] == 4
assert counts["crossing_selected_strict_a1_uniformizer_count"] == 24
assert counts["crossing_away_rational_roundtrip_count"] == 24
assert counts["explicit_side_uniformizer_unit_transition_count"] == 24

con = cert["exact_consequence"]
assert con["four_target_side_away_from_exceptional_neighborhoods_materialized"] is True
assert con["each_away_neighborhood_is_one_source_bound_affine_principal_chart"] is True
assert con["each_away_chart_covers_exactly_the_side_minus_its_six_exceptional_crossings"] is True
assert con["all_24_crossing_open_to_away_chart_overlap_maps_materialized"] is True
assert con["all_24_overlap_maps_have_exact_rational_inverses"] is True
assert con["all_24_overlap_uniformizer_transitions_are_explicit_units"] is True
assert con["four_target_side_full_strict_transform_neighborhood_covers_materialized"] is True
assert con["finite_surface_cover_materialized"] is False
assert con["surface_all_double_overlap_transitions_materialized"] is False
assert con["swap23_cover_action_or_common_refinement_materialized"] is False

status = cert["construction_status"]
assert status["full_16_exceptional_rees_atlases_materialized"] is True
assert status["four_target_side_crossing_neighborhood_atlases_materialized"] is True
assert status["four_target_side_away_from_exceptional_neighborhoods_materialized"] is True
assert status["four_target_side_full_strict_transform_neighborhoods_materialized"] is True
assert status["side_to_exceptional_cross_overlap_maps_at_all_24_crossings_materialized"] is True
assert status["finite_surface_cover_materialized"] is False
assert status["surface_all_double_overlap_transitions_materialized"] is False
assert status["swap23_cover_action_or_common_refinement_materialized"] is False
assert cert["next_exact_leaf"] == "V91C1X_R5B2C_EXTEND_BOUNDARY_NEIGHBORHOODS_TO_A_FINITE_SURFACE_COVER_AND_MATERIALIZE_ALL_DOUBLE_OVERLAPS"
for key, value in cert["credit_firewall"].items():
    assert value is False, key

replay = subprocess.run([sys.executable, str(MAT)], check=True, capture_output=True, text=True)
summary = json.loads(replay.stdout.strip().splitlines()[-1])
assert summary["success"] is True
assert summary["certificate_sha256"] == claimed
assert summary["away_side_chart_count"] == 4
assert summary["crossing_glue_overlap_count"] == 24
assert summary["crossing_selected_strict_a1_uniformizer_count"] == 24
assert summary["crossing_away_rational_roundtrip_count"] == 24
assert summary["explicit_side_uniformizer_unit_transition_count"] == 24
assert summary["next_exact_leaf"] == cert["next_exact_leaf"]

print(json.dumps({
    "success": True,
    "marker": "V124_V91C1X_R5B2B3B_FOUR_SIDE_AWAY_FROM_EXCEPTIONAL_GLUE",
    "certificate_sha256": claimed,
    "away_side_chart_count": 4,
    "crossing_glue_overlap_count": 24,
    "stage33_progress": "6/11",
    "next_exact_leaf": cert["next_exact_leaf"],
}, sort_keys=True))
