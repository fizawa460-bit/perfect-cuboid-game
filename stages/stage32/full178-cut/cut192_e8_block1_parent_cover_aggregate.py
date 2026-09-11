#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

SCHEMA = "STAGE32_FULL178_CUT192_E8_BLOCK1_PARENT_COVER_AGGREGATE_V1"
SHARD_SCHEMA = "STAGE32_FULL178_CUT192_E8_BLOCK1_PARENT_COVER_SCAN_V1"
EXPECTED_PARENT_COUNT = 2360
EXPECTED_RANGES = [
    [0, 295], [295, 590], [590, 885], [885, 1180],
    [1180, 1475], [1475, 1770], [1770, 2065], [2065, 2360],
]
EXPECTED_PARENT_SCAN_BLOB = "4b9489fb88970039aa0d46dc4203395d45f55816"
EXPECTED_HANDOFF_BLOB = "011fe82cd97bfa192d4efbbafacb21b0ea724b44"
EXPECTED_HANDOFF_CANONICAL = "41405165f081554bf3089c0cb15f568d8515fe81202cf6c809914c9490479d1c"
EXPECTED_EX5_HEAD = "fd00531181228c9f367a49eb61ddc3af6ab84ab3"
EXPECTED_PARENT_STREAM = "4977be767465c69616288b54bc79e491b3f8ee29c94162ce089a6258b6fc00e0"
CURRENT_V12_REMAINING = 65396964990500233636101


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit("FAIL: " + msg)


def load_canonical(path: Path) -> dict:
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    req(isinstance(claimed, str) and csha(body) == claimed, f"canonical replay drift: {path}")
    return obj


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    files = sorted(args.input_dir.glob("*.json"))
    req(len(files) == len(EXPECTED_RANGES), f"expected {len(EXPECTED_RANGES)} shard files, got {len(files)}")

    shards = []
    counts = {
        "weak_exact_unsat": 0,
        "strong_exact_unsat": 0,
        "mod2_unsat": 0,
        "residual_strong_sat": 0,
        "residual_mod2_sat": 0,
        "residual_unknown": 0,
    }
    residual_indices = []
    residual_kinds = {}
    covered = 0
    checked = 0

    by_range = {}
    for path in files:
        obj = load_canonical(path)
        req(obj.get("schema") == SHARD_SCHEMA, f"shard schema drift: {path}")
        scope = obj["scope"]
        r = [int(scope["parent_index_start_inclusive"]), int(scope["parent_index_end_exclusive"])]
        req(r not in by_range, f"duplicate shard range {r}")
        by_range[tuple(r)] = (path, obj)

    for expected in EXPECTED_RANGES:
        key = tuple(expected)
        req(key in by_range, f"missing shard range {expected}")
        path, obj = by_range[key]
        locks = obj["source_locks"]
        req(locks["cut192_ex5_handoff_blob"] == EXPECTED_HANDOFF_BLOB, f"handoff blob drift in {path}")
        req(locks["cut192_ex5_handoff_canonical"] == EXPECTED_HANDOFF_CANONICAL, f"handoff canonical drift in {path}")
        req(locks["ex5_exact_head"] == EXPECTED_EX5_HEAD, f"EX5 head drift in {path}")
        req(locks["ex5_adapter_blob"] == "6026d2c8b4a2eb69c453a2bd38c5923f46d6d74f", f"EX5 adapter drift in {path}")
        req(locks["block1_hnf_parent_stream_sha256"] == EXPECTED_PARENT_STREAM, f"parent stream drift in {path}")
        solver = obj["solver"]
        req(solver["weak_timeout_ms"] == 300 and solver["strong_timeout_ms"] == 600 and solver["mod2_timeout_ms"] == 500, f"solver timeout contract drift in {path}")
        result = obj["result"]
        local_checked = expected[1] - expected[0]
        local_covered = int(result["covered_parent_count"])
        local_residual = int(result["residual_parent_count"])
        req(local_covered + local_residual == local_checked, f"coverage accounting drift in {path}")
        for k in counts:
            counts[k] += int(result["counts"][k])
        for rec in result["residual_records"]:
            idx = int(rec["parent_index"])
            req(expected[0] <= idx < expected[1], f"residual index outside shard in {path}: {idx}")
            residual_indices.append(idx)
            if rec["strong_exact"] == "sat":
                kind = "strong_sat"
            elif rec["mod2"] == "sat":
                kind = "mod2_sat"
            else:
                kind = "unknown"
            residual_kinds[str(idx)] = kind
        checked += local_checked
        covered += local_covered
        shards.append({
            "range": expected,
            "canonical_sha256": obj["canonical_sha256_without_this_field"],
            "covered_parent_count": local_covered,
            "residual_parent_count": local_residual,
            "status_stream_sha256": result["status_stream_sha256"],
        })

    req(checked == EXPECTED_PARENT_COUNT, "aggregate parent coverage count drift")
    req(covered + len(residual_indices) == EXPECTED_PARENT_COUNT, "aggregate covered+residual drift")
    req(len(set(residual_indices)) == len(residual_indices), "duplicate aggregate residual parent")
    residual_indices.sort()
    closed = not residual_indices
    candidate = 113 if closed else 0
    body = {
        "schema": SCHEMA,
        "stage": "32",
        "surface": "full178-cut",
        "node": "CUT192",
        "status": "CANDIDATE_BLOCK1_113_TERMINALS_PARENT_UNION_CLOSED_AUDIT_REQUIRED" if closed else "BLOCKED_BLOCK1_RESIDUAL_HNF_PARENTS_REMAIN",
        "source_locks": {
            "parent_scan_implementation_blob": EXPECTED_PARENT_SCAN_BLOB,
            "cut192_ex5_handoff_blob": EXPECTED_HANDOFF_BLOB,
            "cut192_ex5_handoff_canonical": EXPECTED_HANDOFF_CANONICAL,
            "ex5_exact_head": EXPECTED_EX5_HEAD,
            "block1_hnf_parent_stream_sha256": EXPECTED_PARENT_STREAM,
        },
        "scope": {
            "block_index": 1,
            "terminal_rank_range": [113, 225],
            "terminal_count": 113,
            "hnf_parent_count": EXPECTED_PARENT_COUNT,
            "shard_ranges": EXPECTED_RANGES,
            "all_parent_indices_covered_exactly": "0..2359",
        },
        "result": {
            "counts": counts,
            "covered_parent_count": covered,
            "residual_parent_count": len(residual_indices),
            "residual_parent_indices": residual_indices,
            "residual_kinds": residual_kinds,
            "shards": shards,
            "sat_parent_count_lower_bound": counts["residual_strong_sat"] + counts["residual_mod2_sat"],
            "unknown_parent_count": counts["residual_unknown"],
        },
        "credit": {
            "whole_block_parent_union_closed": closed,
            "cut192_pruning_candidate_terminals": candidate,
            "hostile_audit_passed": False,
            "stage32_main_pruning_credit": False,
            "candidate_remaining_terminals_if_later_audited_and_consumed": CURRENT_V12_REMAINING - candidate,
            "whole_stratum_closed": False,
            "full178_complete": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
        "next": {
            "if_residual": "fresh longer exact/modular replay only on retained residual parent indices",
            "if_closed": "freeze retained CUT192 checkpoint then external stage32cut-audit before MAIN consumption",
        },
        "firewalls": {
            "sat_promoted_to_exact_feasibility": False,
            "unknown_promoted_to_unsat": False,
            "main_authority_mutated": False,
            "whole_block_promoted_to_whole_stratum": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": body["status"],
        "covered": covered,
        "residual": len(residual_indices),
        "counts": counts,
        "candidate": candidate,
        "output": str(args.output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
