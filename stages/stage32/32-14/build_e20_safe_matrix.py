#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
from typing import Any

PROFILE_SCHEMA = "STAGE32_D8_MATERIALIZATION_SCHEDULE_PROFILE_V1"
PLAN_SCHEMA = "STAGE32_D8_E20_A0_STORAGE_SAFE_TIER_PLAN_V1"
EXPECTED_CELLS = 1182
EXPECTED_ASSIGNMENTS = 1_032_477_716
SHARD_COUNT = 2
MAX_SELECTED_CELLS = 24
MAX_TOTAL_BRANCHES = 1_000_000
MAX_CELL_BRANCHES = 65_536
MAX_COMPACT_BYTES = 100_000
MAX_PROFILE_BYTES = 2_000_000
MAX_FINAL_BYTES = 5_000_000


def csha(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--github-output", type=pathlib.Path)
    args = ap.parse_args()

    profile_bytes = args.profile.stat().st_size
    assert profile_bytes <= MAX_PROFILE_BYTES, profile_bytes
    profile = json.loads(args.profile.read_text())
    assert profile["schema"] == PROFILE_SCHEMA
    assert int(profile["degree"]) == 8 and int(profile["genus"]) == 0
    assert int(profile["exceptional_mass"]) == 20
    assert int(profile["curve_group_mass"]) == 0
    assert int(profile["signature_cell_count"]) == EXPECTED_CELLS
    assert int(profile["exceptional_assignment_count_after_qtail_quotient"]) == EXPECTED_ASSIGNMENTS
    assert profile["profile_only"] is True
    assert profile["theorem_credit"] is False and profile["receiver_credit"] is False
    assert profile["FULL_D8_G0_ROW_COMPLETE"] is False
    assert profile["FULL_D176_D192_NUMERICAL_ORBIT_CENSUS"] is False
    assert profile["R29_LG2"] == "NOT_DISCHARGED"
    assert profile["G10_LOWGENUS_PICARD"] == "AMBER"

    rows = list(profile["cells_sorted_by_branch_count"])
    assert len(rows) == EXPECTED_CELLS
    assert rows == sorted(rows, key=lambda r: (int(r["materialized_branch_count"]), str(r["cell_id"])))

    eligible: list[tuple[int, list[dict[str, Any]], int]] = []
    for entry in profile["branch_count_cumulative_profile"]:
        threshold = int(entry["branch_threshold"])
        selected = [r for r in rows if int(r["materialized_branch_count"]) <= threshold]
        total = sum(int(r["materialized_branch_count"]) for r in selected)
        assert len(selected) == int(entry["covered_cell_count"])
        assert total == int(entry["scheduled_materialized_branch_count"])
        if (
            selected
            and threshold <= MAX_CELL_BRANCHES
            and len(selected) <= MAX_SELECTED_CELLS
            and total <= MAX_TOTAL_BRANCHES
            and max(int(r["materialized_branch_count"]) for r in selected) <= MAX_CELL_BRANCHES
        ):
            eligible.append((threshold, selected, total))

    safe = bool(eligible)
    threshold = selected_total = 0
    selected_rows: list[dict[str, Any]] = []
    if safe:
        threshold, selected_rows, selected_total = max(eligible, key=lambda x: x[0])

    cells = [
        {
            "cell_index": int(r["cell_index"]),
            "cell_id": str(r["cell_id"]),
            "total_branches": int(r["materialized_branch_count"]),
            "shard_count": SHARD_COUNT,
        }
        for r in selected_rows
    ]
    cells.sort(key=lambda r: (r["total_branches"], r["cell_id"]))

    pilot: dict[str, Any] | None = None
    bulk: list[dict[str, Any]] = []
    if cells:
        first = cells[0]
        pilot = {
            "cell_index": first["cell_index"],
            "cell_id": first["cell_id"],
            "total_branches": first["total_branches"],
            "shard_index": 0,
            "shard_count": SHARD_COUNT,
        }
        for cell in cells:
            for shard_index in range(SHARD_COUNT):
                item = {
                    "cell_index": cell["cell_index"],
                    "cell_id": cell["cell_id"],
                    "total_branches": cell["total_branches"],
                    "shard_index": shard_index,
                    "shard_count": SHARD_COUNT,
                }
                if item == pilot:
                    continue
                bulk.append(item)

    assert len(bulk) == max(0, len(cells) * SHARD_COUNT - (1 if pilot else 0))
    compact_artifact_count = len(cells) * SHARD_COUNT
    shard_storage_upper_bound = compact_artifact_count * MAX_COMPACT_BYTES
    assert compact_artifact_count <= MAX_SELECTED_CELLS * SHARD_COUNT

    report = {
        "schema": PLAN_SCHEMA,
        "parameters": {"degree": 8, "genus": 0, "exceptional_mass": 20, "curve_group_mass": 0},
        "profile_sha256": profile["canonical_sha256_without_this_field"],
        "profile_bytes": profile_bytes,
        "expected_signature_cells": EXPECTED_CELLS,
        "expected_exceptional_assignments": EXPECTED_ASSIGNMENTS,
        "safety_envelope": {
            "max_selected_cells": MAX_SELECTED_CELLS,
            "max_total_materialized_branches": MAX_TOTAL_BRANCHES,
            "max_cell_materialized_branches": MAX_CELL_BRANCHES,
            "shard_count_per_cell": SHARD_COUNT,
            "max_compact_bytes_per_shard_artifact": MAX_COMPACT_BYTES,
            "max_profile_bytes": MAX_PROFILE_BYTES,
            "max_final_aggregate_bytes": MAX_FINAL_BYTES,
            "max_compact_artifact_count": MAX_SELECTED_CELLS * SHARD_COUNT,
            "shard_artifact_storage_upper_bound_bytes": MAX_SELECTED_CELLS * SHARD_COUNT * MAX_COMPACT_BYTES,
            "bulk_max_parallel": 8,
        },
        "safe_to_fanout": safe,
        "chosen_cumulative_branch_threshold": threshold if safe else None,
        "selected_cell_count": len(cells),
        "selected_total_materialized_branches": selected_total,
        "compact_artifact_count": compact_artifact_count,
        "shard_artifact_storage_upper_bound_bytes": shard_storage_upper_bound,
        "selected_cells": cells,
        "pilot": pilot,
        "bulk_matrix": bulk,
        "selection_rule": "ALL_SIGNATURE_CELLS_WITH_MATERIALIZED_BRANCH_COUNT_LE_CHOSEN_THRESHOLD",
        "profile_only_when_safe_to_fanout_false": not safe,
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
        outputs = {
            "safe_to_fanout": "true" if safe else "false",
            "chosen_threshold": str(threshold if safe else 0),
            "selected_cell_count": str(len(cells)),
            "selected_total_branches": str(selected_total),
            "bulk_matrix": json.dumps(bulk, separators=(",", ":")),
            "pilot_cell_index": str(pilot["cell_index"] if pilot else -1),
            "pilot_cell_id": str(pilot["cell_id"] if pilot else "NONE"),
            "pilot_total_branches": str(pilot["total_branches"] if pilot else 0),
        }
        with args.github_output.open("a") as handle:
            for key, value in outputs.items():
                handle.write(f"{key}={value}\n")

    print(json.dumps({
        "safe": safe,
        "threshold": threshold if safe else None,
        "cells": len(cells),
        "branches": selected_total,
        "compact_artifacts": compact_artifact_count,
        "shard_storage_upper_bound_bytes": shard_storage_upper_bound,
        "plan_sha": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
