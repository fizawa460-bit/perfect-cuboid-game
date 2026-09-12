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
BC2_30 = HERE / "bc2-30-boundary42-partition-checkpoint.json"
EXPECTED_B19_BLOB = "b2899aa228e7a3ee97526e3787ffbefa483530b4"
EXPECTED_D18_BLOB = "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
EXPECTED_BC2_30_CANONICAL = "2bbb85361d29331957b0d6f6916ae18a18a4bb04bad4846a7144f94546a32c7a"
BC2_30_AUDIT_HEAD = "38b60be7d0390ad5fa89ddb4dcd9511cfe36c57f"
BC2_30_AUDIT_REVIEW = 5184226057
PRIOR_AUDITED_LOWER_BOUND = 7164

def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-parent-timeout-ms", type=int, default=10000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.per_parent_timeout_ms != 10000:
        raise ValueError("BC2-31 fresh replay is locked to 10000 ms per parent")

    if git_blob_sha(Path(b19.__file__).resolve()) != EXPECTED_B19_BLOB:
        raise ValueError("BC2-19 source blob drift")
    if git_blob_sha(Path(d18.__file__).resolve()) != EXPECTED_D18_BLOB:
        raise ValueError("BC2-18 enumerator source blob drift")
    c30 = json.loads(BC2_30.read_text())
    replay = dict(c30)
    expected = replay.pop("canonical_sha256_without_this_field", None)
    if expected != EXPECTED_BC2_30_CANONICAL or csha(replay) != expected:
        raise ValueError("BC2-30 retained checkpoint drift")

    unknown_indices: list[int] = []
    def tracer(frame, event, arg):
        if frame.f_code is b19.main.__code__ and event == "line":
            text = linecache.getline(frame.f_code.co_filename, frame.f_lineno).strip()
            if text == "unknown_count += 1":
                unknown_indices.append(int(frame.f_locals["parent_index"]))
        return tracer

    old_argv = sys.argv[:]
    old_trace = sys.gettrace()
    try:
        with tempfile.TemporaryDirectory() as td:
            raw_path = Path(td) / "fresh-bc2-19.json"
            sys.argv = [
                str(Path(b19.__file__).resolve()),
                "--per-parent-timeout-ms", "10000",
                "--max-parents", "0",
                "--output", str(raw_path),
            ]
            sys.settrace(tracer)
            b19.main()
            raw = json.loads(raw_path.read_text())
    finally:
        sys.settrace(old_trace)
        sys.argv = old_argv

    pr = raw["parent_replay"]
    checked = int(pr["parents_checked"])
    unsat_count = int(pr["unsat_count"])
    unknown_count = int(pr["unknown_count"])
    sat_found = bool(pr["sat_found"])

    if checked != 7336 and not sat_found:
        raise ValueError("fresh replay did not cover all 7336 parents")
    if len(unknown_indices) != unknown_count:
        raise ValueError("UNKNOWN trace count differs from raw result")
    if len(set(unknown_indices)) != len(unknown_indices) or unknown_indices != sorted(unknown_indices):
        raise ValueError("UNKNOWN identity stream is not unique/sorted")
    if unknown_indices[:64] != pr.get("unknown_parent_indices_first64", []):
        raise ValueError("UNKNOWN trace first64 differs from raw result")
    if unsat_count + unknown_count + (1 if sat_found else 0) != checked:
        raise ValueError("fresh replay status partition regression")

    direct_lower_bound = unsat_count
    combined_lower_bound = max(PRIOR_AUDITED_LOWER_BOUND, direct_lower_bound)
    body = {
        "schema": "STAGE32EX5_BC2_31_FRESH_ALL7336_REPLAY_V1",
        "stage": "32EX5",
        "unit": "BC2_31_FRESH_ALL7336_REPLAY_WITH_EXPLICIT_UNKNOWN_IDENTITIES",
        "status": "PASS_FRESH_REPLAY_RETAINED" if not sat_found else "PASS_PICARD64_PAIRING_FEASIBLE_WITNESS_FOUND_NO_CURVE_CREDIT",
        "audit_consumption": {
            "bc2_30_hostile_audit_status": "PASS",
            "bc2_30_hostile_audit_exact_head": BC2_30_AUDIT_HEAD,
            "bc2_30_hostile_audit_review_id": BC2_30_AUDIT_REVIEW,
        },
        "archival_diagnosis": {
            "historical_bc2_19_unknown_count": 236,
            "historical_artifact_id": 10148676265,
            "historical_artifact_expired_410": True,
            "historical_raw_retained_only_first64_unknown_ids": True,
            "generation2_same_source_replay_unsat_unknown_sat": [7113, 223, 0],
            "generation2_raw_canonical": "f5ef75a81dcb3a952689a0bad14fcf8b122d2b321b4b63a469b3e761910d7f13",
            "historical_timeout_dependent_identity_set_not_recoverable_from_hash_alone": True,
            "historical_remaining172_status_inference_applied": False,
        },
        "source_locks": {
            "bc2_19_replay_source_git_blob_sha": EXPECTED_B19_BLOB,
            "bc2_18_enumerator_source_git_blob_sha": EXPECTED_D18_BLOB,
            "bc2_30_checkpoint_canonical": EXPECTED_BC2_30_CANONICAL,
            "python_version": "3.10.6",
            "sympy_version": "1.14.0",
            "z3_solver_version": "4.15.4.0",
        },
        "fresh_replay": {
            "per_parent_timeout_ms": args.per_parent_timeout_ms,
            "parents_checked": checked,
            "unsat_count": unsat_count,
            "unknown_count": unknown_count,
            "sat_found": sat_found,
            "raw_result_canonical": raw["canonical_sha256_without_this_field"],
            "raw_status_stream_sha256": pr["status_stream_sha256"],
            "unknown_parent_indices_all": unknown_indices,
            "unknown_parent_indices_all_sha256": csha(unknown_indices),
            "all_unknown_identities_explicitly_retained": len(unknown_indices) == unknown_count,
            "sat_witness": raw.get("sat_witness"),
        },
        "interpretation": {
            "fresh_run_statuses_are_run_specific_but_each_unsat_result_is_exact": True,
            "fresh_direct_unsat_lower_bound": direct_lower_bound,
            "prior_audited_lower_bound": PRIOR_AUDITED_LOWER_BOUND,
            "combined_known_parent_unsat_lower_bound": combined_lower_bound,
            "whole_first_block_unsat_proved": (not sat_found and checked == 7336 and unknown_count == 0),
            "historical_remaining172_exact_identity_recovery_claim": False,
        },
        "credit": {
            "fresh_parent_unsat_count": direct_lower_bound,
            "known_parent_unsat_count_lower_bound": combined_lower_bound,
            "whole_first_block_unsat": (not sat_found and checked == 7336 and unknown_count == 0),
            "whole_stratum_closed": False,
            "full178_complete": False,
            "stage32_main_credit": False,
            "effectivity_or_actual_curve_existence_proved": False,
            "theorem_credit": False,
            "endpoint_credit": False,
        },
        "firewalls": {
            "timeout_unknown_relabelled_unsat": False,
            "unknown_dropped": False,
            "sat_relabelled_actual_curve": False,
            "main_promotion": False,
            "merge_authorized": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
        "next_exact_unit": {
            "id": "BC2_32_REPLAY_EXPLICIT_FRESH_UNKNOWN_SET" if unknown_count else "HOSTILE_AUDIT_BC2_31_FRESH_CLOSURE",
            "goal": "Use the explicitly retained fresh UNKNOWN identity list only after hostile audit of this replay receipt.",
            "heavy_scaleout_authorized": False,
            "main_promotion_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "canonical": body["canonical_sha256_without_this_field"],
        "checked": checked,
        "unsat": unsat_count,
        "unknown": unknown_count,
        "sat": sat_found,
        "unknown_sha256": body["fresh_replay"]["unknown_parent_indices_all_sha256"],
        "known_unsat_lower_bound": combined_lower_bound,
        "next": body["next_exact_unit"]["id"],
    }, sort_keys=True))

if __name__ == "__main__":
    main()
