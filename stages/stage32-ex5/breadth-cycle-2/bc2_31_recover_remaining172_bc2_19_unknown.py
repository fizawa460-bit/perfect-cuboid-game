#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import linecache
import sys
import tempfile
from pathlib import Path

import bc2_18_n354_survivor_exceptional_mod8_decomposition as d18
import bc2_19_n354_survivor_normal_positivity_mass_replay as b19

HERE = Path(__file__).resolve().parent
BC2_19_CHECKPOINT = HERE / "bc2-19-n354-survivor-normal-positivity-mass-checkpoint.json"
BC2_21_PREFLIGHT = HERE / "bc2-21-first64-unknown-parent-slice-preflight.json"
BC2_30_CHECKPOINT = HERE / "bc2-30-boundary42-partition-checkpoint.json"
PREFLIGHT = HERE / "bc2-31-recover-remaining172-preflight.json"

EXPECTED_BC2_19_SOURCE_BLOB = "b2899aa228e7a3ee97526e3787ffbefa483530b4"
EXPECTED_BC2_18_SOURCE_BLOB = "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
EXPECTED_BC2_19_CHECKPOINT = "62e97cdb8bd6a8d14c0ac176576bd2cf2ec51020295f8703cbefc3bc85f001eb"
EXPECTED_BC2_21_PREFLIGHT = "7af1bad407a8bfebdbbe1048a6d309092a16fcae818fd7ba1e26b996e5845c47"
EXPECTED_BC2_30_CHECKPOINT = "2bbb85361d29331957b0d6f6916ae18a18a4bb04bad4846a7144f94546a32c7a"
EXPECTED_PREFLIGHT = "edd1bf6198d054277f828795f4e7a9d5372bc3094886e7afea420484bd899328"
EXPECTED_BC2_19_RAW = "fcfecfc4dbd3592095c1c0302991c2b29bee22b6f3652d73612deea7775d7755"
EXPECTED_STATUS_STREAM = "7a551339ab56ef34ed346b7586fd3d1f1ab81de042a3be9c1a9af2bc1d9ab18a"
EXPECTED_BC2_19_COMPUTE_HEAD = "f28112e30c0863e359c375813219196131ec6a06"
EXPECTED_BC2_19_WORKFLOW_RUN = 34467246133
EXPECTED_BC2_19_COMPUTE_JOB = 102838819035
EXPECTED_BC2_19_ARTIFACT = 10148676265
BC2_30_AUDIT_HEAD = "38b60be7d0390ad5fa89ddb4dcd9511cfe36c57f"
BC2_30_AUDIT_REVIEW = 5184226057


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def checked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    if obj.get("canonical_sha256_without_this_field") != expected:
        raise ValueError(f"canonical field drift: {path.name}")
    replay = dict(obj)
    replay.pop("canonical_sha256_without_this_field", None)
    if csha(replay) != expected:
        raise ValueError(f"canonical replay drift: {path.name}")
    return obj


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-parent-timeout-ms", type=int, default=2000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.per_parent_timeout_ms != 2000:
        raise ValueError("BC2-31 recovery requires the exact historical BC2-19 2000 ms timeout")

    if git_blob_sha(Path(b19.__file__).resolve()) != EXPECTED_BC2_19_SOURCE_BLOB:
        raise ValueError("BC2-19 replay source blob regression")
    if git_blob_sha(Path(d18.__file__).resolve()) != EXPECTED_BC2_18_SOURCE_BLOB:
        raise ValueError("BC2-18 enumerator source blob regression")

    c19 = checked(BC2_19_CHECKPOINT, EXPECTED_BC2_19_CHECKPOINT)
    c21 = checked(BC2_21_PREFLIGHT, EXPECTED_BC2_21_PREFLIGHT)
    c30 = checked(BC2_30_CHECKPOINT, EXPECTED_BC2_30_CHECKPOINT)
    pf = checked(PREFLIGHT, EXPECTED_PREFLIGHT)

    if (c19["result"]["parents_checked"], c19["result"]["unsat_count"], c19["result"]["unknown_count"], c19["result"]["sat_count"]) != (7336, 7100, 236, 0):
        raise ValueError("BC2-19 historical partition regression")
    if c19["result"]["status_stream_sha256"] != EXPECTED_STATUS_STREAM:
        raise ValueError("BC2-19 status-stream regression")
    selected64 = [int(v) for v in c21["slice"]["indices"]]
    if len(selected64) != 64 or len(set(selected64)) != 64 or selected64 != sorted(selected64):
        raise ValueError("BC2-21 selected64 identity regression")
    if c21["slice"]["other_bc2_19_unknown_count"] != 172:
        raise ValueError("BC2-21 remaining-count regression")
    if (pf["recovery"]["historical_unknown_count"], pf["recovery"]["retained_first64_count"], pf["recovery"]["expected_remaining_count"]) != (236, 64, 172):
        raise ValueError("BC2-31 preflight count regression")
    if c30["interpretation"]["known_parent_unsat_count_lower_bound"] != 7164:
        raise ValueError("BC2-30 lower-bound regression")
    if c30["interpretation"]["unretained_unknown_identity_count"] != 172:
        raise ValueError("BC2-30 unretained count regression")

    captured_unknown: list[int] = []

    def tracer(frame, event, arg):
        if frame.f_code is b19.main.__code__ and event == "line":
            text = linecache.getline(frame.f_code.co_filename, frame.f_lineno).strip()
            if text == "unknown_count += 1":
                captured_unknown.append(int(frame.f_locals["parent_index"]))
        return tracer

    old_argv = sys.argv[:]
    old_trace = sys.gettrace()
    try:
        with tempfile.TemporaryDirectory() as td:
            raw_path = Path(td) / "bc2-19-replay.json"
            sys.argv = [str(Path(b19.__file__).resolve()), "--per-parent-timeout-ms", "2000", "--max-parents", "0", "--output", str(raw_path)]
            sys.settrace(tracer)
            b19.main()
            raw = json.loads(raw_path.read_text(encoding="utf-8"))
    finally:
        sys.settrace(old_trace)
        sys.argv = old_argv

    if raw.get("canonical_sha256_without_this_field") != EXPECTED_BC2_19_RAW:
        raise ValueError("BC2-19 replay canonical mismatch; identity recovery refused")
    pr = raw["parent_replay"]
    if (pr["parents_checked"], pr["unsat_count"], pr["unknown_count"], pr["sat_found"]) != (7336, 7100, 236, False):
        raise ValueError("BC2-19 replay partition mismatch")
    if pr["status_stream_sha256"] != EXPECTED_STATUS_STREAM:
        raise ValueError("BC2-19 replay status stream mismatch")
    if pr["unknown_parent_indices_first64"] != selected64:
        raise ValueError("BC2-19 replay first64 mismatch")

    if len(captured_unknown) != 236 or len(set(captured_unknown)) != 236 or captured_unknown != sorted(captured_unknown):
        raise ValueError("captured BC2-19 UNKNOWN identity set regression")
    if captured_unknown[:64] != selected64:
        raise ValueError("captured UNKNOWN prefix differs from retained selected64")

    remaining = captured_unknown[64:]
    if len(remaining) != 172 or len(set(remaining)) != 172 or remaining != sorted(remaining) or set(remaining) & set(selected64):
        raise ValueError("remaining172 exact complement regression")
    if set(captured_unknown) != set(selected64) | set(remaining):
        raise ValueError("236 = 64 + 172 partition regression")

    body = {
        "schema": "STAGE32EX5_BC2_31_RECOVER_REMAINING_172_BC2_19_UNKNOWN_IDENTITIES_V1",
        "stage": "32EX5",
        "unit": "BC2_31_EXACT_RECOVERY_OF_UNRETAINED_BC2_19_UNKNOWN_IDENTITIES",
        "status": "PASS_EXACT_172_IDENTITIES_RECOVERED_NO_STATUS_INFERENCE",
        "audit_consumption": {
            "bc2_30_hostile_audit_status": "PASS",
            "bc2_30_hostile_audit_exact_head": BC2_30_AUDIT_HEAD,
            "bc2_30_hostile_audit_review_id": BC2_30_AUDIT_REVIEW
        },
        "source_locks": {
            "bc2_19_replay_source_git_blob_sha": EXPECTED_BC2_19_SOURCE_BLOB,
            "bc2_18_enumerator_source_git_blob_sha": EXPECTED_BC2_18_SOURCE_BLOB,
            "bc2_19_checkpoint_canonical": EXPECTED_BC2_19_CHECKPOINT,
            "bc2_21_first64_preflight_canonical": EXPECTED_BC2_21_PREFLIGHT,
            "bc2_30_checkpoint_canonical": EXPECTED_BC2_30_CHECKPOINT,
            "bc2_31_preflight_canonical": EXPECTED_PREFLIGHT,
            "historical_bc2_19_raw_result_canonical": EXPECTED_BC2_19_RAW,
            "historical_bc2_19_status_stream_sha256": EXPECTED_STATUS_STREAM,
            "historical_bc2_19_compute_head": EXPECTED_BC2_19_COMPUTE_HEAD,
            "historical_bc2_19_workflow_run_id": EXPECTED_BC2_19_WORKFLOW_RUN,
            "historical_bc2_19_compute_job_id": EXPECTED_BC2_19_COMPUTE_JOB,
            "historical_bc2_19_artifact_id": EXPECTED_BC2_19_ARTIFACT
        },
        "recovery_certificate": {
            "method": "EXECUTE_EXACT_BC2_19_SOURCE_AND_TRACE_EACH_UNKNOWN_EVENT",
            "exact_historical_replay_required": True,
            "historical_raw_canonical_matched": True,
            "historical_status_stream_matched": True,
            "historical_unknown_count": 236,
            "retained_first64_count": 64,
            "recovered_remaining_count": 172,
            "partition_exact": True,
            "partition_disjoint": True,
            "selected64_are_prefix_of_historical_unknown_stream": True,
            "all236_parent_indices": captured_unknown,
            "all236_parent_indices_sha256": csha(captured_unknown),
            "retained_first64_parent_indices": selected64,
            "retained_first64_parent_indices_sha256": csha(selected64),
            "recovered_remaining172_parent_indices": remaining,
            "recovered_remaining172_parent_indices_sha256": csha(remaining)
        },
        "interpretation": {
            "identity_recovery_only": True,
            "new_status_inference_applied": False,
            "recovered_172_are_still_unknown_at_historical_bc2_19_boundary": True,
            "known_parent_unsat_count_lower_bound": 7164,
            "whole_first_block_unsat_proved": False
        },
        "credit": {
            "exact_remaining172_identity_set_recovered": True,
            "new_parent_unsat_count": 0,
            "known_parent_unsat_count_lower_bound": 7164,
            "whole_first_block_unsat": False,
            "whole_stratum_closed": False,
            "full178_complete": False,
            "stage32_main_credit": False,
            "effectivity_or_actual_curve_existence_proved": False,
            "theorem_credit": False,
            "endpoint_credit": False
        },
        "firewalls": {
            "recovered_unknown_relabelled_unsat": False,
            "unknown_dropped": False,
            "sat_relabelled_actual_curve": False,
            "main_promotion": False,
            "merge_authorized": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False
        },
        "next_exact_unit": {
            "id": "BC2_32_REPLAY_RECOVERED_172_BC2_19_UNKNOWN_IDENTITIES",
            "goal": "Replay the exact recovered 172 parent identities under a separately audited bounded solver plan; identity recovery alone grants no status inference.",
            "heavy_scaleout_authorized": False,
            "main_promotion_authorized": False
        }
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "canonical": body["canonical_sha256_without_this_field"],
        "all_unknown": len(captured_unknown),
        "selected64": len(selected64),
        "remaining172": len(remaining),
        "remaining172_sha256": body["recovery_certificate"]["recovered_remaining172_parent_indices_sha256"],
        "known_unsat_lower_bound": 7164,
        "next": body["next_exact_unit"]["id"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
