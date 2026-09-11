#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from z3 import get_version_string, unknown, unsat

import cut102_finite_ring_direct_completion_v2 as core

HERE = Path(__file__).resolve().parent
SCHEMA = "STAGE32_FULL178_CUT102_RESIDUAL3_BRANCH_REPLAY_V1"
TARGET_BRANCHES = {
    1000: [3, 5],
    1030: [3, 5],
    1056: [2, 3, 5],
}


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-branch-timeout-ms", type=int, default=15000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.per_branch_timeout_ms <= 0:
        raise ValueError("positive timeout required")

    P, blocks, exceptional_labels, parents, fixed = core.load_interface()
    records = []
    for parent_index, degrees in TARGET_BRANCHES.items():
        yE, _ = parents[parent_index]
        for degree in degrees:
            # Fresh solver per branch: no incremental search-state dependence.
            s, y, n1, linear = core.make_solver(P, blocks, fixed, 2, args.per_branch_timeout_ms)
            for label, value in zip(exceptional_labels, yE):
                s.add(y[label - 1] == value)
            s.add(n1 == degree)
            r = s.check()
            rec = {
                "parent_index": parent_index,
                "n1": degree,
                "n2": core.TARGET_D - degree,
                "result": str(r),
                "prime": 2,
                "rank_mod_p": linear["rank_mod_p"],
                "left_kernel_dimension": linear["left_kernel_dimension"],
            }
            if r == unknown:
                rec["reason_unknown"] = s.reason_unknown()
            elif r != unsat:
                rec["note"] = "finite-ring SAT is nonexcluding and has no exact feasibility credit"
            records.append(rec)

    unresolved = [r for r in records if r["result"] != "unsat"]
    status = "PASS_ALL_SEVEN_RESIDUAL_MOD2_BRANCHES_UNSAT" if not unresolved else "BLOCKED_RESIDUAL_MOD2_BRANCHES_REMAIN"
    body = {
        "schema": SCHEMA,
        "stage": "32",
        "surface": "full178-cut",
        "node": "CUT102",
        "status": status,
        "z3_version": get_version_string(),
        "source_locks": {
            "bc2_24_checkpoint_blob_sha1": core.EXPECTED_BC224_BLOB,
            "bc2_24_checkpoint_canonical_sha256": core.EXPECTED_BC224_CANONICAL,
            "bc2_18_enumerator_blob_sha1": core.EXPECTED_D18_BLOB,
            "retained_picard_bundle_blob_sha1": core.EXPECTED_RETAINED_BLOB,
            "retained_marking_blob_sha1": core.EXPECTED_MARKING_BLOB,
            "bc2_18_feasible_stream_sha256": core.EXPECTED_STREAM,
        },
        "target_branches": {str(k): v for k, v in TARGET_BRANCHES.items()},
        "method": {
            "prime": 2,
            "fresh_solver_per_branch": True,
            "per_branch_timeout_ms": args.per_branch_timeout_ms,
            "reason": "remove incremental solver search-state dependence observed when parent 1224 replayed after deeper residual checks",
        },
        "records": records,
        "unresolved_records": unresolved,
        "credit": {
            "cut103_scope_certificate_complete": False,
            "stage32_main_pruning_credit": False,
            "full178_complete": False,
            "merge_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": status, "unsat": len(records) - len(unresolved), "unresolved": len(unresolved)}))


if __name__ == "__main__":
    main()
