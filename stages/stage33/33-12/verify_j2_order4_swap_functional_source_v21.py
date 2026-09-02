#!/usr/bin/env python3
"""Network-free replay of the v21 source-first named J2 functional."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-order4-swap-functional-source-v21.json"
PRODUCER = HERE / "certify_j2_order4_swap_functional_source_v21.py"

cert = json.loads(CERT.read_text())
body = dict(cert)
claimed = body.pop("canonical_sha256")
actual = hashlib.sha256(
    json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
assert claimed == actual
assert cert["schema"] == "STAGE33_12_J2_ORDER4_SWAP_FUNCTIONAL_SOURCE_V21"
assert cert["status"] == "PASS_EXACT_SOURCE_FIRST_NAMED_FUNCTIONAL_MATERIALIZED"
assert cert["pinned_upstream"]["git_blob_sha1"] == "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
assert cert["pinned_upstream"]["raw_sha256"] == "5dc3ae961d872ff96420385880edf0f4225a12d3f906c614e1ccd2220399ce89"
geo = cert["exact_geometric_equivariance"]
assert geo["pullback_naturality_applies"] is True
assert all(x["projection_commutes_exactly"] for x in geo["swaps"].values())
assert all(x["kc_automorphism_exact"] for x in geo["swaps"].values())
behavior = cert["named_order4_functional_behavior"]
assert behavior["order4_element_itself_claimed_fixed"] is False
assert behavior["named_binary_functional_fixed_under_swap12"] is True
assert behavior["named_binary_functional_fixed_under_swap13"] is True
source = cert["named_full_surface_source"]
assert source["proper14_mask_decimal"] == 25
assert source["retained10_mask_decimal"] == 6
assert source["retained10_f2"] == [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
assert source["two_bit_value_a_b"] == [0, 1]
assert source["source_coordinate_materialized"] is True
assert not any(cert["anti_inference"].values())
scope = cert["promotion_scope"]
assert scope["source_coordinate_only"] is True
assert scope["named_source_target_relation_materialized"] is False
assert scope["finite_v4_kummer_columns_materialized"] == 0
assert scope["stage33_progress"] == "6/11"
assert scope["stage33_12_closed_exact"] is False

replay = subprocess.run(
    [sys.executable, str(PRODUCER), "--check"],
    check=True,
    text=True,
    capture_output=True,
)
receipt = json.loads(replay.stdout)
assert receipt["canonical_sha256"] == claimed
assert receipt["retained10_mask"] == 6
assert receipt["two_bit_value_a_b"] == [0, 1]
assert receipt["source_coordinate_materialized"] is True
assert receipt["relation_materialized"] is False
assert receipt["marker"] == "PROOF_REPLAY_COMPLETE"
print("PROOF_REPLAY_COMPLETE")
