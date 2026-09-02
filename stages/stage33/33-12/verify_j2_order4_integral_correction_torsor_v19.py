#!/usr/bin/env python3
"""Network-free replay of the v19 J2 order-4 correction torsor."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-order4-integral-correction-torsor-v19.json"
PRODUCER = HERE / "materialize_j2_order4_integral_correction_torsor_v19.py"
EXPECTED = "3ee11e0ecdc855083a4260c2ae4f24ef4c160a7e26a48fd3872369d117118576"

cert = json.loads(CERT.read_text())
body = dict(cert)
claimed = body.pop("canonical_sha256")
actual = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
assert claimed == EXPECTED == actual
assert cert["schema"] == "STAGE33_12_J2_ORDER4_INTEGRAL_CORRECTION_TORSOR_V19"
assert cert["status"] == "PASS_EXACT_CORRECTION_TORSOR_MATERIALIZED_NAMED_ELEMENT_UNLABELED"
eq = cert["integrality_equation"]
assert eq["coefficient_rank_f2"] == 50
assert eq["solution_affine_dimension_f2"] == 14
assert eq["solution_count"] == 16384
assert len(eq["kernel_basis_f2_14x64"]) == 14
assert all(len(row) == 64 for row in eq["kernel_basis_f2_14x64"])
enum = cert["exact_enumeration"]
assert enum["corrected_integral_order4_lifts"] == 16384
assert enum["distinct_mixed_smith_half_lifts"] == 16384
assert enum["every_lift_doubles_to_locked_semantic_u1"] is True
assert enum["distinct_proper14_functionals"] == 16
assert enum["preimages_per_proper14_functional"] == 1024
assert enum["joint_cc_ct_fixed_retained10_masks"] == [4, 5, 6, 7]
assert enum["unique_named_element_selected"] is False
assert cert["anti_inference"] == {
    "historical_mask6_assumed": False,
    "rep88_used_as_actual_integral_glue": False,
    "s3_fixedness_used_to_select_label": False,
    "target_compatibility_used": False,
}
fw = cert["promotion_firewall"]
assert fw["named_j2_source_coordinate_materialized"] is False
assert fw["finite_v4_kummer_columns_materialized"] == 0
assert fw["stage33_progress"] == "6/11"
assert fw["stage33_12_closed_exact"] is False

replay = subprocess.run(
    [sys.executable, str(PRODUCER), "--check"],
    check=True,
    text=True,
    capture_output=True,
)
receipt = json.loads(replay.stdout)
assert receipt["canonical_sha256"] == EXPECTED
assert receipt["marker"] == "PROOF_REPLAY_COMPLETE"
assert receipt["named_selected"] is False
print("PROOF_REPLAY_COMPLETE")
