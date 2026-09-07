#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1x-r5b2b1-a2-02-full-closure-local-germs.json"
MAT = HERE / "materialize_e3_v91c1x_r5b2b1_full_closure_local_germs.py"
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
assert cert["schema"] == "stage33.e3.v91c1x_r5b2b1.a2_02_full_closure_local_germs.v1"
assert cert["entry"]["authority"] == "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
assert cert["entry"]["stage33_progress"] == "6/11"
assert cert["closure_exceptionals"] == EXPECTED
assert cert["closure_count"] == 16
assert len(cert["local_germ_rows"]) == 16
assert [r["exceptional_id"] for r in cert["local_germ_rows"]] == EXPECTED
for row in cert["local_germ_rows"]:
    assert row["adapted_generator_initial_degrees"] == [1, 1, 1, 2]
    assert row["tangent_kernel_dimension"] == 3
    assert row["rees_input_ready"] is True
    assert len(row["independent_surface_equation_indices_0based"]) == 3
    assert len(row["unique_linear_relation_alpha_Qi"]) == 4
    assert len(row["normalized_affine_node_nonpivot_Qi"]) == 6
con = cert["exact_consequence"]
assert con["all_16_nodes_satisfy_pinned_surface_quadrics"] is True
assert con["all_16_affine_jacobians_have_rank_3"] is True
assert con["all_16_actual_affine_surface_germs_materialized_by_exact_dehomogenize_translate_recipe"] is True
assert con["all_16_have_adapted_generator_orders_1_1_1_2"] is True
assert con["all_16_have_nondegenerate_quadratic_on_three_dimensional_tangent_kernel"] is True
assert con["all_16_are_ready_for_exact_rees_substitution"] is True
assert con["tangent_model_only_source_gap_remains_for_the_16_exceptionals"] is False
status = cert["construction_status"]
assert status["actual_local_surface_equations_materialized"] is True
assert status["full_16_exceptional_rees_charts_materialized"] is False
assert status["four_target_side_strict_transform_neighborhoods_materialized"] is False
assert status["surface_uniformizers_materialized"] is False
assert status["cross_overlap_maps_materialized"] is False
for key, value in cert["credit_firewall"].items():
    assert value is False, key

replay = subprocess.run([sys.executable, str(MAT)], check=True, capture_output=True, text=True)
summary = json.loads(replay.stdout.strip().splitlines()[-1])
assert summary["success"] is True
assert summary["certificate_sha256"] == claimed
assert summary["closure_count"] == 16
assert summary["all_rees_input_ready"] is True
assert summary["next_exact_leaf"] == cert["next_exact_leaf"]
print(json.dumps({
    "success": True,
    "marker": "V119_V91C1X_R5B2B1_FULL_CLOSURE_LOCAL_GERMS",
    "certificate_sha256": claimed,
    "closure_count": 16,
    "stage33_progress": "6/11",
    "next_exact_leaf": cert["next_exact_leaf"],
}, sort_keys=True))
