#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1x-r5b2a-a2-02-target-side-incidence-closure.json"
MAT = HERE / "materialize_e3_v91c1x_r5b2a_target_side_incidence_closure.py"
TARGET_SIDES = ["SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008"]
TARGET_EXC = ["EXC_003", "EXC_004", "EXC_011", "EXC_012"]
PARAMS = ["0", "infinity", "1", "-1", "i", "-i"]
EXPECTED_CLOSURE = [
    "EXC_003", "EXC_004", "EXC_007", "EXC_008", "EXC_011", "EXC_012",
    "EXC_015", "EXC_016", "EXC_025", "EXC_026", "EXC_027", "EXC_028",
    "EXC_029", "EXC_030", "EXC_031", "EXC_032",
]
EXPECTED_ADDITIONAL = [
    "EXC_007", "EXC_008", "EXC_015", "EXC_016", "EXC_025", "EXC_026",
    "EXC_027", "EXC_028", "EXC_029", "EXC_030", "EXC_031", "EXC_032",
]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


cert = json.loads(CERT.read_text(encoding="utf-8"))
claimed = cert["canonical_sha256"]
body = dict(cert)
body.pop("canonical_sha256")
assert claimed == csha(body)
assert cert["schema"] == "stage33.e3.v91c1x_r5b2a.a2_02_target_side_incidence_closure.v1"
assert cert["stage"] == "33-12"
assert cert["entry"]["authority"] == "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
assert cert["entry"]["stage33_progress"] == "6/11"
assert cert["target_side_components"] == TARGET_SIDES
assert cert["target_exceptional_components_from_a2_02_support"] == TARGET_EXC
assert cert["incidence_pair_count"] == 24
for row in cert["side_rows"]:
    assert row["crossing_count"] == 6
    assert row["crossing_parameters_in_frozen_order"] == PARAMS
    assert len(row["incident_exceptional_ids"]) == 6
    assert len(set(row["incident_exceptional_ids"])) == 6
assert cert["side_incident_exceptional_closure"] == EXPECTED_CLOSURE
assert cert["side_incident_exceptional_closure_count"] == 16
assert cert["additional_exceptionals_required_beyond_target4_for_full_target_side_crossing_cover"] == EXPECTED_ADDITIONAL
assert cert["additional_exceptionals_required_count"] == 12
assert cert["target4_exceptionals_not_incident_to_any_target_side"] == []
con = cert["exact_consequence"]
assert con["each_target_side_has_exactly_six_frozen_exceptional_crossings"] is True
assert con["each_target_side_crossing_parameter_set_is_0_inf_pm1_pmi"] is True
assert con["r5b1_component_cover_remains_valid_for_its_four_target_exceptionals"] is True
assert con["target4_exceptionals_cover_all_crossings_of_the_four_target_sides"] is False
assert con["surface_neighborhood_cover_may_ignore_additional_incident_exceptionals"] is False
for key, value in cert["credit_firewall"].items():
    assert value is False, key

replay = subprocess.run([sys.executable, str(MAT)], check=True, capture_output=True, text=True)
summary = json.loads(replay.stdout.strip().splitlines()[-1])
assert summary["success"] is True
assert summary["certificate_sha256"] == claimed
assert summary["incidence_pair_count"] == 24
assert summary["closure_count"] == 16
assert summary["additional_exceptional_count"] == 12
assert summary["target4_covers_all_target_side_crossings"] is False
print(json.dumps({
    "success": True,
    "marker": "V118_V91C1X_R5B2A_TARGET_SIDE_INCIDENCE_CLOSURE",
    "certificate_sha256": claimed,
    "incidence_pair_count": 24,
    "closure_count": 16,
    "additional_exceptional_count": 12,
    "stage33_progress": "6/11",
    "next_exact_leaf": cert["next_exact_leaf"],
}, sort_keys=True))
