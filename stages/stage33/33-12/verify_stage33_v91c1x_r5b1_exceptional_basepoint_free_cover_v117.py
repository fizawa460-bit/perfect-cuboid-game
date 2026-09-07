#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1x-r5b1-a2-02-exceptional-basepoint-free-cover.json"
MAT = HERE / "materialize_e3_v91c1x_r5b1_exceptional_basepoint_free_cover.py"
TARGETS = ["EXC_003", "EXC_004", "EXC_011", "EXC_012"]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


cert = json.loads(CERT.read_text(encoding="utf-8"))
claimed = cert["canonical_sha256"]
body = dict(cert)
body.pop("canonical_sha256")
assert claimed == csha(body)
assert cert["schema"] == "stage33.e3.v91c1x_r5b1.a2_02_exceptional_basepoint_free_projection_cover.v1"
assert cert["stage"] == "33-12"
assert cert["entry"]["authority"] == "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
assert cert["entry"]["stage33_progress"] == "6/11"
assert cert["target_exceptional_components"] == TARGETS
assert [r["component_id"] for r in cert["rows"]] == TARGETS
for row in cert["rows"]:
    assert row["physical_crossing_count"] >= 2
    assert row["two_distinct_projection_basepoints_verified"] is True
    assert len(row["projection_systems"]) == 2
    assert {x["base_crossing_index_0based"] for x in row["projection_systems"]} == {0, 1}
    assert all(x["common_zero_locus_on_projective_tangent_plane"] == "EXACTLY_THE_CHOSEN_BASEPOINT" for x in row["projection_systems"])
    assert row["transition_determinant_nonzero"] is True
    M = row["pgl2_transition_system0_to_system1"]
    assert len(M) == 2 and all(len(x) == 2 for x in M)

con = cert["exact_consequence"]
for key in [
    "all_four_target_exceptional_conics_have_two_source_bound_projection_systems",
    "each_projection_system_has_exactly_one_basepoint_on_the_exceptional_conic",
    "the_two_basepoints_are_distinct_for_each_component",
    "the_two_projection_domains_cover_each_target_exceptional_conic",
    "exact_pgl2_transition_between_projection_coordinates_materialized",
]:
    assert con[key] is True, key
assert con["naive_single_R0_R1_pair_treated_as_basepoint_free_cover"] is False
for key, value in cert["credit_firewall"].items():
    assert value is False, key

replay = subprocess.run([sys.executable, str(MAT)], check=True, capture_output=True, text=True)
summary = json.loads(replay.stdout.strip().splitlines()[-1])
assert summary["success"] is True
assert summary["certificate_sha256"] == claimed
assert summary["target_count"] == 4
assert summary["pgl2_transition_count"] == 4
print(json.dumps({
    "success": True,
    "marker": "V117_V91C1X_R5B1_EXCEPTIONAL_BASEPOINT_FREE_COVER",
    "certificate_sha256": claimed,
    "target_count": 4,
    "stage33_progress": "6/11",
    "next_exact_leaf": cert["next_exact_leaf"],
}, sort_keys=True))
