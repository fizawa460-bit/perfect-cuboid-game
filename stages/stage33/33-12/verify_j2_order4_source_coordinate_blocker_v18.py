#!/usr/bin/env python3
"""Network-free replay of the exact v18 order-4 normalization blocker."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-order4-source-coordinate-v18.json"
PRODUCER = HERE / "materialize_j2_order4_source_coordinate_v18.py"
EXPECTED = "a0378a7d7191d537347435d11002faa3692f91781dd15f53fe3063443e9d50d1"

cert = json.loads(CERT.read_text())
body = dict(cert)
claimed = body.pop("canonical_sha256")
actual = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
assert claimed == EXPECTED == actual
assert cert["schema"] == "STAGE33_12_J2_ORDER4_SOURCE_COORDINATE_BLOCKER_V18"
assert cert["status"] == "PASS_EXACT_ALL_REQUIRED_ROWS_MATERIALIZED_BLOCKED_AT_ORDER4_DUAL_INTEGRALITY"
assert sorted(map(int, cert["required_rows"])) == [2, 4, 9, 10, 20, 35, 39, 47, 49, 67]
assert cert["rows20_67_reconstruction"]["20"]["full_surface_known_preimage_indices_1based"] == [32, 117, 122, 125, 130, 133, 138]
assert cert["rows20_67_reconstruction"]["20"]["full_surface_known_preimage_multiplicities"] == [2, 1, 1, 1, 1, 1, 1]
assert cert["rows20_67_reconstruction"]["67"]["full_surface_known_preimage_indices_1based"] == [110, 115]
assert cert["semantic_order4_numerator"]["divisible_by_2"] is True
assert cert["semantic_order4_numerator"]["divisible_by_4"] is False
assert cert["semantic_order4_numerator"]["nondivisible_positions_1based"] == [3, 4, 10, 12, 55]
assert cert["named_j2_source_coordinate"]["materialized"] is False
fw = cert["promotion_firewall"]
assert fw["mathematical_state_promotion_performed"] is False
assert fw["finite_v4_kummer_columns_materialized"] == 0
assert fw["stage33_progress"] == "6/11"
assert fw["stage33_12_closed_exact"] is False

replay = subprocess.run(
    [sys.executable, str(PRODUCER), "--check"],
    cwd=HERE.parents[2],
    check=True,
    text=True,
    capture_output=True,
)
receipt = json.loads(replay.stdout)
assert receipt["canonical_sha256"] == EXPECTED
assert receipt["marker"] == "PROOF_REPLAY_COMPLETE"
print("PROOF_REPLAY_COMPLETE")
