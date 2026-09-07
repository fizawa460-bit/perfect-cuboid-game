#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1x-r5b2b2-a2-02-full-16-exceptional-rees-charts.json"
MAT = HERE / "materialize_e3_v91c1x_r5b2b2_full_16_exceptional_rees_charts.py"
EXPECTED = [
    "EXC_003", "EXC_004", "EXC_007", "EXC_008", "EXC_011", "EXC_012",
    "EXC_015", "EXC_016", "EXC_025", "EXC_026", "EXC_027", "EXC_028",
    "EXC_029", "EXC_030", "EXC_031", "EXC_032",
]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


cert = json.loads(CERT.read_text(encoding="utf-8"))
claimed = cert["canonical_sha256"]
body = dict(cert)
body.pop("canonical_sha256")
assert claimed == csha(body)
assert cert["schema"] == "stage33.e3.v91c1x_r5b2b2.a2_02_full_16_exceptional_rees_charts.v1"
assert cert["entry"]["authority"] == "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
assert cert["entry"]["stage33_progress"] == "6/11"
assert cert["entry"]["r5b2b1_canonical_sha256"] == "02f0362bce42716a18ff709e350587775cd7edbdcc99d71af39b49b01c63651d"
assert cert["closure_exceptionals"] == EXPECTED
assert cert["closure_count"] == 16
assert cert["standard_rees_charts_per_exceptional"] == 6
assert cert["total_standard_rees_chart_count"] == 96
assert cert["directed_internal_overlap_transitions_per_exceptional"] == 30
assert cert["total_directed_internal_overlap_transition_count"] == 480
assert cert["t_saturation_exact_check_count"] == 96
assert len(cert["exceptional_rows"]) == 16
assert [x["exceptional_id"] for x in cert["exceptional_rows"]] == EXPECTED

chart_count = 0
transition_count = 0
for row in cert["exceptional_rows"]:
    assert row["standard_rees_chart_count"] == 6
    assert len(row["charts"]) == 6
    assert row["directed_internal_overlap_transition_count"] == 30
    assert len(row["directed_internal_overlap_transitions"]) == 30
    assert [x["pivot_displacement_index_0based"] for x in row["charts"]] == list(range(6))
    for chart in row["charts"]:
        assert chart["exceptional_uniformizer"] == "e"
        assert chart["strict_transform_division_orders"] == [1, 1, 1, 2]
        assert len(chart["strict_transform_generators_Qi"]) == 4
        assert len(chart["exceptional_fiber_generators_Qi"]) == 4
        assert chart["pullback_equals_e_power_times_strict_generator"] is True
        assert chart["pullback_ideal_t_saturation_equals_strict_transform_ideal"] is True
        chart_count += 1
    seen = {(x["source_chart_pivot_0based"], x["target_chart_pivot_0based"]) for x in row["directed_internal_overlap_transitions"]}
    assert seen == {(p, q) for p in range(6) for q in range(6) if p != q}
    for tr in row["directed_internal_overlap_transitions"]:
        assert tr["strict_generator_transition_weights"] == [1, 1, 1, 2]
        assert tr["strict_generator_rule"] == "G_target = G_source / overlap_unit^order"
        transition_count += 1
assert chart_count == 96
assert transition_count == 480

con = cert["exact_consequence"]
assert con["all_16_exceptional_local_germs_have_full_six_standard_rees_charts"] is True
assert con["all_96_pullback_equations_divide_exactly_by_the_adapted_orders_1_1_1_2"] is True
assert con["all_96_strict_transform_ideals_equal_the_t_saturation_of_the_pullback_ideals"] is True
assert con["all_16_internal_standard_rees_atlases_have_all_30_directed_pairwise_overlap_transition_recipes"] is True
assert con["exceptional_uniformizer_e_is_literal_on_every_standard_rees_chart"] is True
assert con["internal_rees_chart_overlap_maps_are_materialized"] is True
assert con["side_to_exceptional_cross_overlap_maps_are_materialized"] is False
status = cert["construction_status"]
assert status["actual_local_surface_equations_materialized"] is True
assert status["full_16_exceptional_rees_charts_materialized"] is True
assert status["exceptional_chart_uniformizers_materialized"] is True
assert status["internal_rees_overlap_maps_materialized"] is True
assert status["four_target_side_strict_transform_neighborhoods_materialized"] is False
assert status["side_component_uniformizers_materialized"] is False
assert status["side_to_exceptional_cross_overlap_maps_materialized"] is False
assert status["finite_surface_cover_materialized"] is False
for key, value in cert["credit_firewall"].items():
    assert value is False, key

# Full exact replay: the materializer independently reconstructs the local equations,
# performs all 96 Rees substitutions and all 96 t-saturation ideal-equality checks,
# then recomputes the canonical certificate hash without rewriting the certificate.
replay = subprocess.run([sys.executable, str(MAT)], check=True, capture_output=True, text=True)
summary = json.loads(replay.stdout.strip().splitlines()[-1])
assert summary["success"] is True
assert summary["certificate_sha256"] == claimed
assert summary["closure_count"] == 16
assert summary["standard_rees_chart_count"] == 96
assert summary["internal_overlap_transition_count"] == 480
assert summary["saturation_pass_count"] == 96
assert summary["next_exact_leaf"] == cert["next_exact_leaf"]
print(json.dumps({
    "success": True,
    "marker": "V120_V91C1X_R5B2B2_FULL_16_EXCEPTIONAL_REES_CHARTS",
    "certificate_sha256": claimed,
    "closure_count": 16,
    "standard_rees_chart_count": 96,
    "saturation_pass_count": 96,
    "stage33_progress": "6/11",
    "next_exact_leaf": cert["next_exact_leaf"],
}, sort_keys=True))
