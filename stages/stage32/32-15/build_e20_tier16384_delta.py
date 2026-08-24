#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
from typing import Any

PROFILE_SCHEMA = "STAGE32_D8_MATERIALIZATION_SCHEDULE_PROFILE_V1"
PREV_SCHEMA = "STAGE32_D8_E20_A0_STORAGE_SAFE_EXACT_TIER_V1"
PLAN_SCHEMA = "STAGE32_D8_E20_A0_TIER16384_DELTA_PLAN_V1"
EXPECTED_PROFILE_SHA = "e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384534d53fa1fee67c5"
EXPECTED_PREV_SHA = "88d3d7d12217626e8af80e3d6c3886b47a6416b498500de94bc1032c25407cb5"
PREV_THRESHOLD = 4096
TARGET_THRESHOLD = 16384
EXPECTED_PREV_CELLS = 16
EXPECTED_PREV_BRANCHES = 48790
EXPECTED_CUMULATIVE_CELLS = 69
EXPECTED_CUMULATIVE_BRANCHES = 655558
EXPECTED_DELTA_CELLS = 53
EXPECTED_DELTA_BRANCHES = 606768
SHARD_COUNT = 2
MAX_COMPACT_BYTES = 100_000


def csha(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", type=pathlib.Path, required=True)
    ap.add_argument("--predecessor", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--github-output", type=pathlib.Path)
    args = ap.parse_args()

    profile = json.loads(args.profile.read_text())
    prev = json.loads(args.predecessor.read_text())
    assert profile["schema"] == PROFILE_SCHEMA
    assert profile["canonical_sha256_without_this_field"] == EXPECTED_PROFILE_SHA
    assert int(profile["degree"]) == 8 and int(profile["genus"]) == 0
    assert int(profile["exceptional_mass"]) == 20 and int(profile["curve_group_mass"]) == 0
    assert int(profile["signature_cell_count"]) == 1182
    assert int(profile["exceptional_assignment_count_after_qtail_quotient"]) == 1_032_477_716

    assert prev["schema"] == PREV_SCHEMA
    unsigned = dict(prev)
    claimed_prev = unsigned.pop("canonical_sha256_without_this_field")
    assert claimed_prev == EXPECTED_PREV_SHA and csha(unsigned) == claimed_prev
    assert int(prev["chosen_cumulative_branch_threshold"]) == PREV_THRESHOLD
    assert int(prev["selected_cell_count"]) == EXPECTED_PREV_CELLS
    assert int(prev["selected_total_materialized_branches"]) == EXPECTED_PREV_BRANCHES
    assert prev["selected_cells_exactly_complete"] is True
    assert int(prev["unknown_branch_count"]) == 0
    assert int(prev["exact_numerical_survivor_count"]) == 0
    assert prev["parent_e20_a0_complete"] is False
    assert prev["theorem_credit"] is False and prev["receiver_credit"] is False

    rows = list(profile["cells_sorted_by_branch_count"])
    prev_rows = [r for r in rows if int(r["materialized_branch_count"]) <= PREV_THRESHOLD]
    target_rows = [r for r in rows if int(r["materialized_branch_count"]) <= TARGET_THRESHOLD]
    delta_rows = [r for r in target_rows if int(r["materialized_branch_count"]) > PREV_THRESHOLD]

    assert len(prev_rows) == EXPECTED_PREV_CELLS
    assert sum(int(r["materialized_branch_count"]) for r in prev_rows) == EXPECTED_PREV_BRANCHES
    assert len(target_rows) == EXPECTED_CUMULATIVE_CELLS
    assert sum(int(r["materialized_branch_count"]) for r in target_rows) == EXPECTED_CUMULATIVE_BRANCHES
    assert len(delta_rows) == EXPECTED_DELTA_CELLS
    assert sum(int(r["materialized_branch_count"]) for r in delta_rows) == EXPECTED_DELTA_BRANCHES

    prev_keys = {(int(c["cell_index"]), str(c["cell_id"])) for c in prev["cell_summaries"]}
    expected_prev_keys = {(int(r["cell_index"]), str(r["cell_id"])) for r in prev_rows}
    assert prev_keys == expected_prev_keys

    cells = [{
        "cell_index": int(r["cell_index"]),
        "cell_id": str(r["cell_id"]),
        "total_branches": int(r["materialized_branch_count"]),
        "shard_count": SHARD_COUNT,
    } for r in delta_rows]
    cells.sort(key=lambda r: (r["total_branches"], r["cell_id"]))

    pilot = {
        "cell_index": cells[0]["cell_index"],
        "cell_id": cells[0]["cell_id"],
        "total_branches": cells[0]["total_branches"],
        "shard_index": 0,
        "shard_count": SHARD_COUNT,
    }
    bulk: list[dict[str, Any]] = []
    for cell in cells:
        for shard_index in range(SHARD_COUNT):
            item = {
                "cell_index": cell["cell_index"],
                "cell_id": cell["cell_id"],
                "total_branches": cell["total_branches"],
                "shard_index": shard_index,
                "shard_count": SHARD_COUNT,
            }
            if item != pilot:
                bulk.append(item)
    assert len(bulk) == EXPECTED_DELTA_CELLS * SHARD_COUNT - 1

    report = {
        "schema": PLAN_SCHEMA,
        "parameters": {"degree": 8, "genus": 0, "exceptional_mass": 20, "curve_group_mass": 0},
        "profile_sha256": EXPECTED_PROFILE_SHA,
        "predecessor_sha256": EXPECTED_PREV_SHA,
        "predecessor_threshold": PREV_THRESHOLD,
        "target_threshold": TARGET_THRESHOLD,
        "predecessor_cell_count": EXPECTED_PREV_CELLS,
        "predecessor_branch_count": EXPECTED_PREV_BRANCHES,
        "delta_cell_count": EXPECTED_DELTA_CELLS,
        "delta_branch_count": EXPECTED_DELTA_BRANCHES,
        "cumulative_cell_count": EXPECTED_CUMULATIVE_CELLS,
        "cumulative_branch_count": EXPECTED_CUMULATIVE_BRANCHES,
        "selected_delta_cells": cells,
        "pilot": pilot,
        "bulk_matrix": bulk,
        "selection_rule": "ALL_E20_A0_SIGNATURE_CELLS_WITH_4096_LT_BRANCH_COUNT_LE_16384",
        "storage_safety": {
            "compact_artifact_count": EXPECTED_DELTA_CELLS * SHARD_COUNT,
            "max_compact_bytes_per_artifact": MAX_COMPACT_BYTES,
            "hard_shard_storage_upper_bound_bytes": EXPECTED_DELTA_CELLS * SHARD_COUNT * MAX_COMPACT_BYTES,
            "observed_stage32_14_representative_artifact_bytes": 1281,
            "observed_projection_bytes_at_same_size": EXPECTED_DELTA_CELLS * SHARD_COUNT * 1281,
            "raw_branch_rows_persisted": False,
            "retention_days": 1,
        },
        "theorem_credit": False,
        "receiver_credit": False,
        "FULL_D8_G0_ROW_COMPLETE": False,
        "FULL_D176_D192_NUMERICAL_ORBIT_CENSUS": False,
        "R29_LG2_NUMERICAL_COMPONENT_COMPLETE": False,
        "R29_LG2": "NOT_DISCHARGED",
        "R29_LG2_EFF": "NOT_DISCHARGED",
        "R29_LG2_MB": "NOT_DISCHARGED",
        "G10_LOWGENUS_PICARD": "AMBER",
    }
    report["canonical_sha256_without_this_field"] = csha(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")

    if args.github_output:
        values = {
            "bulk_matrix": json.dumps(bulk, separators=(",", ":")),
            "pilot_cell_index": str(pilot["cell_index"]),
            "pilot_cell_id": pilot["cell_id"],
            "pilot_total_branches": str(pilot["total_branches"]),
        }
        with args.github_output.open("a") as h:
            for k, v in values.items():
                h.write(f"{k}={v}\n")

    print(json.dumps({
        "delta_cells": EXPECTED_DELTA_CELLS,
        "delta_branches": EXPECTED_DELTA_BRANCHES,
        "cumulative_cells": EXPECTED_CUMULATIVE_CELLS,
        "cumulative_branches": EXPECTED_CUMULATIVE_BRANCHES,
        "pilot": pilot,
        "bulk_jobs": len(bulk),
        "hard_storage_upper_bound_bytes": report["storage_safety"]["hard_shard_storage_upper_bound_bytes"],
        "plan_sha": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
