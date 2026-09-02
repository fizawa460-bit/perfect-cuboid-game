#!/usr/bin/env python3
"""Network-free replay of the v22 source-first V4 incompatibility witness."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-kummer-source-target-module-source-first-v22.json"
PRODUCER = HERE / "replay_j2_kummer_source_target_module_source_first_v22.py"

cert = json.loads(CERT.read_text())
body = dict(cert)
claimed = body.pop("canonical_sha256")
actual = hashlib.sha256(
    json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
assert claimed == actual
assert cert["schema"] == "STAGE33_12_V4_KUMMER_EXTENSION_REACHABILITY_SOURCE_FIRST_V3"
assert cert["status"] == "FAIL_EXACT_SOURCE_FIRST_J2_TARGET_UNREACHABLE"
j2 = cert["locked_named_j2"]
assert j2["proper14_f2"] == [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert j2["retained10_support_1based"] == [2, 3]
assert j2["reachable_H1_subspace_dimension_f2"] == 13
assert j2["locked_target_reachable_from_locked_source"] is False
assert j2["separating_functional_annihilates_reachable_subspace"] is True
assert j2["separating_functional_value_on_locked_target"] == 1
assert len(j2["separating_functional_75D_f2"]) == 75
reach = cert["target_reachability_over_all_nonzero_retained_sources"]
assert reach["compatible_source_count"] + reach["incompatible_source_count"] == 1023
assert reach["all_nonzero_retained_sources_partitioned"] is True
assert reach["locked_j2_source_mask_decimal"] in reach["incompatible_source_masks_decimal"]
consequence = cert["exact_consequence"]
assert consequence["source_label_or_orientation_is_no_longer_in_the_blocker"] is True
assert consequence["remaining_interface"] == "TARGET_H1_PROJECTION_OR_KUMMER_BLOCK_EXTENSION_CONVENTION_ADAPTER"
assert consequence["historical_source_target_relation_restored"] is False
assert consequence["standard_columns_materialized"] == 0

replay = subprocess.run(
    [sys.executable, str(PRODUCER), "--check"],
    check=True,
    text=True,
    capture_output=True,
)
receipt = json.loads(replay.stdout)
assert receipt["canonical_sha256"] == claimed
assert receipt["target_reachable"] is False
assert receipt["marker"] == "PROOF_REPLAY_COMPLETE"
print("PROOF_REPLAY_COMPLETE")
