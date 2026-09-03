#!/usr/bin/env python3
"""Network-free hostile replay for the V41 independent e3 source lock."""
from __future__ import annotations
import hashlib, json, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"e3-independent-proper14-source-v41.json"
PRODUCER=HERE/"certify_e3_independent_proper14_source_v41.py"
EXPECTED="04c6ead2226c87defff085fc641ee80867e1fdf4b07baa28c5e97d2c5e534ac6"

def csha(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

cert=json.loads(CERT.read_text(encoding="utf-8")); body=dict(cert); claimed=body.pop("canonical_sha256")
assert claimed==EXPECTED==csha(body)
assert cert["schema"]=="STAGE33_12_E3_INDEPENDENT_PROPER14_SOURCE_V41"
assert cert["status"]=="PASS_EXACT_E3_INDEPENDENT_PROPER14_SOURCE_MATERIALIZED_H2_MU2_LIFT_OPEN"
src=cert["e3_source"]
assert src["adapted_basis_label"]=="e3"
assert src["retained10_standard_mask_decimal"]==4
assert src["retained10_standard_coordinate_f2"]==[0,0,1,0,0,0,0,0,0,0]
assert src["proper14_mask_decimal"]==20
assert src["proper14_coordinate_f2"]==[0,0,1,0,1,0,0,0,0,0,0,0,0,0]
assert src["derived_from_j2_xor_split"] is False
assert cert["basis_replay"]["proper_invariant_dimension_f2"]==10
assert cert["basis_replay"]["basis_rank_f2"]==10
assert cert["construction_boundary"]["genuine_full_surface_h2_mu2_lift_materialized"] is False
assert cert["construction_boundary"]["kummer_column_for_e3_materialized"] is False
anti=cert["anti_inference"]
assert anti["j2_equals_e2_plus_e3_used_to_derive_e3"] is False
assert anti["standard_col2_col3_split_from_xor"] is False
assert anti["remaining_kummer_column_guessed"] is False
assert anti["broad_history_or_origin_search_restarted"] is False
assert cert["promotion_firewall"]["merge_allowed"] is False
replay=subprocess.run([sys.executable,str(PRODUCER),"--check"],check=True,text=True,capture_output=True)
receipt=json.loads(replay.stdout)
assert receipt["canonical_sha256"]==EXPECTED
assert receipt["retained10_mask"]==4 and receipt["proper14_mask"]==20
assert receipt["genuine_h2_mu2_lift_materialized"] is False
assert receipt["marker"]=="PROOF_REPLAY_COMPLETE"
print("PROOF_REPLAY_COMPLETE")
