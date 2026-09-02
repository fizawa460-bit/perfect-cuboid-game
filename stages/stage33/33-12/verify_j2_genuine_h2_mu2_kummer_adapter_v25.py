#!/usr/bin/env python3
"""Network-free replay of V25 current named-J2 genuine H2(mu2) adapter."""
from __future__ import annotations
import hashlib
import json
import subprocess
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-genuine-h2-mu2-kummer-adapter-v25.json"
PRODUCER = HERE / "certify_j2_genuine_h2_mu2_kummer_adapter_v25.py"
cert = json.loads(CERT.read_text())
body = dict(cert)
claimed = body.pop("canonical_sha256")
actual = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
assert claimed == actual
assert cert["schema"] == "STAGE33_12_J2_GENUINE_H2_MU2_KUMMER_ADAPTER_V25"
assert cert["status"] == "PASS_EXACT_CURRENT_NAMED_J2_GENUINE_H2_MU2_LIFT_ADAPTER_MATERIALIZED_CONNECTING_COCYCLE_OPEN"
assert cert["current_named_source"]["retained10_mask_decimal"] == 6
assert cert["current_named_source"]["marked_brauer_coordinate_f2"] == [1, 0]
adapter = cert["genuine_h2_mu2_adapter"]
assert adapter["named_source_and_cech_lift_identified_by_same_marked_brauer_coordinate"] is True
assert adapter["explicit_cech_preimage_e_D_materialized"] is True
assert adapter["genuine_kc_surface_h2_mu2_lift_materialized"] is True
assert adapter["full_surface_named_j2_h2_mu2_lift_materialized"] is True
assert adapter["historical_kummer_glue_used"] is False
assert adapter["raw_weight15_h1_used_as_kummer_boundary"] is False
assert cert["supersession"]["v24_old_weight15_target_remains_revoked"] is True
assert cert["supersession"]["standard_kummer_column_materialized"] is False
remain = cert["remaining_interface"]
assert remain["v4_connecting_cocycle_materialized"] is False
assert remain["standard_kummer_columns_materialized"] == 0
assert cert["promotion_firewall"]["stage33_progress"] == "6/11"
assert cert["promotion_firewall"]["stage33_12_closed_exact"] is False
assert cert["promotion_firewall"]["merge_allowed"] is False
replay = subprocess.run([sys.executable, str(PRODUCER), "--check"], check=True, text=True, capture_output=True)
receipt = json.loads(replay.stdout)
assert receipt["canonical_sha256"] == claimed
assert receipt["genuine_h2_mu2_lift_adapter_materialized"] is True
assert receipt["v4_connecting_cocycle_materialized"] is False
assert receipt["standard_kummer_columns_materialized"] == 0
assert receipt["marker"] == "PROOF_REPLAY_COMPLETE"
print("PROOF_REPLAY_COMPLETE")
