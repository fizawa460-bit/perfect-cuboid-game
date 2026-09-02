#!/usr/bin/env python3
"""Network-free replay of the v23 H1 coordinate-41 trace."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-kummer-target-h1-coordinate41-trace-v23.json"
PRODUCER = HERE / "certify_j2_kummer_target_h1_coordinate41_trace_v23.py"

cert = json.loads(CERT.read_text())
body = dict(cert)
claimed = body.pop("canonical_sha256")
actual = hashlib.sha256(
    json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
assert claimed == actual
assert cert["status"] == "PASS_EXACT_TARGET_ADAPTER_GAP_TRACED_TO_H1_BASIS41"
sep = cert["separating_coordinate"]
assert sep["H1_coordinate_1based"] == 41
assert sep["H1_basis41_raw_pic2_cc_support_1based"] == []
assert sep["H1_basis41_raw_pic2_ct_support_1based"] == [9, 11, 19]
assert sep["annihilates_every_source_first_j2_reachable_extension_image"] is True
assert sep["value_on_locked_named_j2_target"] == 1
assert cert["locked_target_replay"]["H1_coordinate41"] == 1
assert cert["locked_target_replay"]["projection_reconstruction_exact"] is True
assert cert["narrowed_missing_interface"]["source_coordinate_or_label_in_blocker"] is False
assert cert["promotion_firewall"]["standard_columns_materialized"] == 0

replay = subprocess.run(
    [sys.executable, str(PRODUCER), "--check"],
    check=True,
    text=True,
    capture_output=True,
)
receipt = json.loads(replay.stdout)
assert receipt["canonical_sha256"] == claimed
assert receipt["basis41_ct_support"] == [9, 11, 19]
assert receipt["marker"] == "PROOF_REPLAY_COMPLETE"
print("PROOF_REPLAY_COMPLETE")
