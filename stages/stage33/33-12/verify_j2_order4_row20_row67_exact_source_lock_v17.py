#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-order4-row20-row67-exact-source-lock-v17.json"

EXPECTED_CANONICAL = "04b47064db73e02068aa51301c94ab0576d927c0b71b2d3df093012028f061d2"
EXPECTED_RESULT_CANONICAL = "9bf2fe321557c3e8c76ab693dbbd6bec055095f4fec95b84b29db61c4f22e9e8"
EXPECTED_ROWS = {
    "20": [[32,2],[117,1],[122,1],[125,1],[130,1],[133,1],[138,1]],
    "67": [[110,1],[115,1]],
}

data = json.loads(CERT.read_text())
body = dict(data)
claimed = body.pop("canonical_sha256")
actual = hashlib.sha256(
    json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
assert claimed == EXPECTED_CANONICAL == actual
assert data["schema"] == "STAGE33_12_J2_ORDER4_ROW20_ROW67_EXACT_SOURCE_LOCK_V17"
assert data["status"] == "EXACT_TWO_ROW_SOURCE_LOCKED_NO_CLAIM_PROMOTION"
assert data["workflow"]["run_id"] == 33590282972
assert data["workflow"]["run_conclusion"] == "success"
assert data["workflow"]["extract_runner_count"] == 1
assert data["workflow"]["final_fail_closed_step_conclusion"] == "success"
assert data["workflow"]["final_fail_closed_step_locked_marker"] == "PROOF_REPLAY_COMPLETE"
assert data["authorization_gate"]["cold_generation"] == 5
assert data["authorization_gate"]["cold_armed"] is False
assert data["authorization_gate"]["armed_generation"] == 6
assert data["authorization_gate"]["armed"] is True
assert data["authorization_gate"]["transition_scope"] == "dedicated_run_key_only"
assert data["artifact"]["result_status"] == "EXACT_ROWS_EXTRACTED"
assert data["artifact"]["result_canonical_sha256"] == EXPECTED_RESULT_CANONICAL
assert data["dimensions"] == {"bdimK": 74, "bdim_full_surface": 140}
assert data["rows"] == EXPECTED_ROWS
assert all(1 <= idx <= 140 and mult > 0 for row in EXPECTED_ROWS.values() for idx, mult in row)
fw = data["firewalls"]
assert fw["qpic_smith_s3_reopened"] is False
assert fw["target_compatibility_inference_used"] is False
assert fw["claim_promotion_performed"] is False
assert fw["stage33_progress"] == "6/11"
assert fw["stage33_12_closed_exact"] is False
assert fw["kummer_standard_columns_materialized"] == 0
assert fw["named_j2_source_coordinate_materialized"] is False
print("PROOF_REPLAY_COMPLETE")
