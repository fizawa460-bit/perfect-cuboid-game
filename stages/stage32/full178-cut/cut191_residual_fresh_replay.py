#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from z3 import sat, unknown, unsat, get_version_string

import cut102_finite_ring_direct_completion_v2 as cut102
import cut191_bc218_parent_cover_scan as cover

SCHEMA = "STAGE32_FULL178_CUT191_RESIDUAL_FRESH_REPLAY_V1"
EXPECTED_COVER_BLOB = "d789e43a2440b4c1b4411e02b3f926b0653d8e8f"
EXPECTED_CUT102_BLOB = "fbdd1e65b509526d5198743208bff79bd2488673"
TARGET_D = 8


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parent", type=int, required=True)
    ap.add_argument("--timeout-ms", type=int, default=15000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if not (0 <= args.parent < cover.EXPECTED_PARENT_COUNT):
        raise ValueError("parent index out of range")
    if args.timeout_ms <= 0:
        raise ValueError("timeout must be positive")
    if cut102.git_blob_sha(Path(cover.__file__).resolve()) != EXPECTED_COVER_BLOB:
        raise ValueError("CUT191 cover implementation source lock moved")
    if cut102.git_blob_sha(Path(cut102.__file__).resolve()) != EXPECTED_CUT102_BLOB:
        raise ValueError("CUT102 implementation source lock moved")

    P, blocks, exceptional_labels, parents, fixed = cut102.load_interface()
    yE, _allowed = parents[args.parent]

    weak, weak_p = cover.make_exact_solver(P, blocks, fixed, False, args.timeout_ms)
    wr, wreason = cover.check_parent(weak, weak_p, exceptional_labels, yE)
    if wr == unsat:
        method = "fresh weak exact Picard64 UNSAT"
        final = "unsat"
        strong_result = None
        mod2_result = None
        branches = []
    else:
        strong, strong_p = cover.make_exact_solver(P, blocks, fixed, True, args.timeout_ms)
        sr, sreason = cover.check_parent(strong, strong_p, exceptional_labels, yE)
        strong_result = {"result": str(sr)}
        if sreason is not None:
            strong_result["reason_unknown"] = sreason
        if sr == unsat:
            method = "fresh strong exact Picard64 UNSAT"
            final = "unsat"
            mod2_result = None
            branches = []
        elif sr == sat:
            method = "fresh strong exact Picard64 SAT"
            final = "sat"
            mod2_result = None
            branches = []
        else:
            mod2, y, n1, meta = cut102.make_solver(P, blocks, fixed, 2, args.timeout_ms)
            mod2.push()
            for label, value in zip(exceptional_labels, yE):
                mod2.add(y[label - 1] == int(value))
            mr = mod2.check()
            mreason = mod2.reason_unknown() if mr == unknown else None
            mod2.pop()
            mod2_result = {
                "result": str(mr),
                "rank_mod_2": meta["rank_mod_p"],
                "left_kernel_dimension_mod_2": meta["left_kernel_dimension"],
            }
            if mreason is not None:
                mod2_result["reason_unknown"] = mreason
            branches = []
            if mr == unsat:
                method = "fresh whole-parent mod2 UNSAT"
                final = "unsat"
            elif mr == sat:
                method = "fresh whole-parent mod2 SAT"
                final = "sat_relaxation"
            else:
                saw_sat = False
                saw_unknown = False
                for degree in range(TARGET_D + 1):
                    bs, by, bn1, _bmeta = cut102.make_solver(P, blocks, fixed, 2, args.timeout_ms)
                    for label, value in zip(exceptional_labels, yE):
                        bs.add(by[label - 1] == int(value))
                    bs.add(bn1 == degree)
                    br = bs.check()
                    rec = {"n1": degree, "result": str(br)}
                    if br == unknown:
                        saw_unknown = True
                        rec["reason_unknown"] = bs.reason_unknown()
                    elif br == sat:
                        saw_sat = True
                    elif br != unsat:
                        raise ValueError("unexpected branch result")
                    branches.append(rec)
                if saw_sat:
                    method = "fresh n1 partition has mod2 SAT branch"
                    final = "sat_relaxation"
                elif saw_unknown:
                    method = "fresh n1 partition retains UNKNOWN branch"
                    final = "unknown"
                else:
                    method = "fresh exhaustive n1=0..8 mod2 UNSAT partition"
                    final = "unsat"

    weak_result = {"result": str(wr)}
    if wreason is not None:
        weak_result["reason_unknown"] = wreason
    status = "PASS_RESIDUAL_PARENT_UNSAT" if final == "unsat" else "BLOCKED_RESIDUAL_PARENT_NOT_UNSAT"
    body = {
        "schema": SCHEMA,
        "stage": "32",
        "surface": "full178-cut",
        "node": "CUT191",
        "status": status,
        "parent_index": args.parent,
        "source_locks": {
            "cut191_cover_implementation_blob": EXPECTED_COVER_BLOB,
            "cut102_implementation_blob": EXPECTED_CUT102_BLOB,
            "bc2_18_feasible_stream_sha256": cut102.EXPECTED_STREAM,
            "bc2_18_parent_count": cover.EXPECTED_PARENT_COUNT,
        },
        "solver": {
            "z3_version": get_version_string(),
            "timeout_ms_per_fresh_check": args.timeout_ms,
            "fresh_solver_per_partition_branch": True,
        },
        "result": {
            "final": final,
            "method": method,
            "weak_exact": weak_result,
            "strong_exact": strong_result,
            "mod2": mod2_result,
            "n1_partition_branches": branches,
        },
        "soundness": {
            "only_unsat_has_exclusion_credit": True,
            "timeouts_relabelled_unsat": False,
            "mod2_sat_relabelled_exact_sat": False,
        },
        "credit": {
            "parent_excluded": final == "unsat",
            "whole_bc2_18_parent_union_closed": False,
            "whole_first_block_unsat": False,
            "stage32_main_pruning_credit": False,
            "full178_complete": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
        "firewalls": {
            "bc2_25_identity_refinement_performed": False,
            "n356_candidate_assumed_consumed": False,
            "main_authority_mutated": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": status, "parent": args.parent, "final": final, "method": method}, sort_keys=True))


if __name__ == "__main__":
    main()
