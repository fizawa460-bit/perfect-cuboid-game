#!/usr/bin/env python3
"""Network-free replay of the v24 raw-H1/Kummer-target scope firewall."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-raw-h1-not-kummer-target-v24.json"
PRODUCER = HERE / "certify_j2_raw_h1_not_kummer_target_v24.py"
cert = json.loads(CERT.read_text())
body = dict(cert)
claimed = body.pop("canonical_sha256")
assert claimed == hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
assert cert["status"] == "PASS_EXACT_RAW_H1_SCOPE_SEPARATED_FROM_MISSING_KUMMER_ADAPTER"
scope = cert["exact_scope_separation"]
assert scope["named_source_coordinate_exact"] is True
assert scope["named_source_retained10_mask_decimal"] == 6
assert scope["raw_cech_H1_weight"] == 15
assert scope["raw_cech_H1_may_be_used_as_named_kummer_boundary"] is False
assert cert["supersession"]["old_weight15_vector_retained_as_raw_H1_evidence"] is True
assert cert["supersession"]["old_weight15_vector_revoked_as_named_kummer_matrix_target"] is True
assert cert["basis_and_gauge_independence"]["failure_is_not_a_choice_of_H1_basis"] is True
assert cert["basis_and_gauge_independence"]["failure_is_not_removed_by_pic2_coboundary_gauge"] is True
assert cert["promotion_firewall"]["standard_columns_materialized"] == 0

r = subprocess.run([sys.executable, str(PRODUCER), "--check"], check=True, text=True, capture_output=True)
receipt = json.loads(r.stdout)
assert receipt["canonical_sha256"] == claimed
assert receipt["raw_h1_is_named_kummer_target"] is False
assert receipt["marker"] == "PROOF_REPLAY_COMPLETE"
print("PROOF_REPLAY_COMPLETE")
