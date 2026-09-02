#!/usr/bin/env python3
"""Network-free replay of the v20 named-functional quotient."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-order4-named-functional-quotient-v20.json"
PRODUCER = HERE / "certify_j2_order4_named_functional_quotient_v20.py"

cert = json.loads(CERT.read_text())
body = dict(cert)
claimed = body.pop("canonical_sha256")
actual = hashlib.sha256(
    json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
assert claimed == actual
assert cert["schema"] == "STAGE33_12_J2_ORDER4_NAMED_FUNCTIONAL_QUOTIENT_V20"
assert cert["status"] == "PASS_EXACT_NAMED_COLUMN_GAP_REDUCED_TO_TWO_BITS"
q = cert["exact_quotient"]
assert q["integral_correction_torsor_dimension_f2"] == 14
assert q["integral_corrections_per_functional"] == 1024
assert q["named_column_relevant_quotient_dimension_f2"] == 2
assert q["named_column_relevant_quotient_count"] == 4
assert q["ten_correction_bits_are_invisible_to_the_proper_br2_source_column"] is True
assert [x["retained10_mask_decimal"] for x in q["affine_plane_records"]] == [4, 5, 6, 7]
s3 = cert["actual_s3_action_on_two_bit_quotient"]
assert s3["orbits"] == [[6], [4, 5, 7]]
assert s3["unique_joint_fixed_mask"] == 6
assert s3["joint_fixedness_of_named_order4_lift_source_locked"] is False
assert s3["named_mask_selected"] is False
assert cert["narrowed_missing_interface"]["previous_14_bit_selector_required_for_named_column"] is False
fw = cert["promotion_firewall"]
assert fw["named_j2_source_coordinate_materialized"] is False
assert fw["first_75D_matrix_column_materialized"] is False
assert fw["stage33_progress"] == "6/11"
assert fw["stage33_12_closed_exact"] is False

replay = subprocess.run(
    [sys.executable, str(PRODUCER), "--check"],
    check=True,
    text=True,
    capture_output=True,
)
receipt = json.loads(replay.stdout)
assert receipt["canonical_sha256"] == claimed
assert receipt["named_column_gap_bits"] == 2
assert receipt["named_selected"] is False
assert receipt["marker"] == "PROOF_REPLAY_COMPLETE"
print("PROOF_REPLAY_COMPLETE")
