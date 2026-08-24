#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
from collections import Counter
from typing import Any

PROFILE_SCHEMA = "STAGE32_D8_MATERIALIZATION_SCHEDULE_PROFILE_V1"
PREV_SCHEMA = "STAGE32_D8_E20_A0_EXACT_TIER_LE16384_V1"
PLAN_SCHEMA = "STAGE32_D8_E20_A0_TIER65536_WORK_BALANCED_PLAN_V1"
EXPECTED_PROFILE_SHA = "e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384534d53fa1fee67c5"
EXPECTED_PREV_SHA = "593bb0fc5231222ab9ce79ae0bd5802d77311d02fd633152d665f869b095611f"
PREV_THRESHOLD = 16_384
TARGET_THRESHOLD = 65_536
EXPECTED_PREV_CELLS = 69
EXPECTED_PREV_BRANCHES = 655_558
EXPECTED_DELTA_CELLS = 232
EXPECTED_DELTA_BRANCHES = 6_178_556
EXPECTED_CUMULATIVE_CELLS = 301
EXPECTED_CUMULATIVE_BRANCHES = 6_834_114
MAX_BRANCHES_PER_WORK_ITEM = 32_768
BUNDLE_COUNT = 48
WAVE_COUNT = 4
MAX_COMPACT_BYTES_PER_ITEM = 20_000
MAX_RUNNER_LOCAL_RAW_BYTES = 1_000_000_000
MAX_PARALLEL_BUNDLES = 8


def csha(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def expected_mod_count(total: int, shard_count: int, shard_index: int) -> int:
    return total // shard_count + (1 if shard_index < total % shard_count else 0)


def quantile_nearest(values: list[int], fraction: float) -> int:
    assert values
    return values[min(len(values) - 1, round(fraction * (len(values) - 1)))]


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
    assert int(profile["exceptional_mass"]) == 20
    assert int(profile["curve_group_mass"]) == 0
    assert int(profile["signature_cell_count"]) == 1182
    assert int(profile["exceptional_assignment_count_after_qtail_quotient"]) == 1_032_477_716

    assert prev["schema"] == PREV_SCHEMA
    prev_unsigned = dict(prev)
    prev_claimed = prev_unsigned.pop("canonical_sha256_without_this_field")
    assert prev_claimed == EXPECTED_PREV_SHA and csha(prev_unsigned) == prev_claimed
    assert int(prev["chosen_cumulative_branch_threshold"]) == PREV_THRESHOLD
    assert int(prev["selected_cell_count"]) == EXPECTED_PREV_CELLS
    assert int(prev["selected_total_materialized_branches"]) == EXPECTED_PREV_BRANCHES
    assert prev["selected_cells_exactly_complete"] is True
    assert int(prev["unknown_branch_count"]) == 0
    assert int(prev["exact_numerical_survivor_count"]) == 0
    assert prev["theorem_credit"] is False and prev["receiver_credit"] is False

    rows = list(profile["cells_sorted_by_branch_count"])
    prev_rows = [r for r in rows if int(r["materialized_branch_count"]) <= PREV_THRESHOLD]
    target_rows = [r for r in rows if int(r["materialized_branch_count"]) <= TARGET_THRESHOLD]
    delta_rows = [
        r
        for r in target_rows
        if int(r["materialized_branch_count"]) > PREV_THRESHOLD
    ]
    assert len(prev_rows) == EXPECTED_PREV_CELLS
    assert sum(int(r["materialized_branch_count"]) for r in prev_rows) == EXPECTED_PREV_BRANCHES
    assert len(delta_rows) == EXPECTED_DELTA_CELLS
    assert sum(int(r["materialized_branch_count"]) for r in delta_rows) == EXPECTED_DELTA_BRANCHES
    assert len(target_rows) == EXPECTED_CUMULATIVE_CELLS
    assert sum(int(r["materialized_branch_count"]) for r in target_rows) == EXPECTED_CUMULATIVE_BRANCHES

    prev_keys = {(int(c["cell_index"]), str(c["cell_id"])) for c in prev["cell_summaries"]}
    expected_prev_keys = {(int(r["cell_index"]), str(r["cell_id"])) for r in prev_rows}
    assert prev_keys == expected_prev_keys
    regression_summary = next(
        c for c in prev["cell_summaries"] if int(c["cell_index"]) == 588
    )
    assert regression_summary["cell_id"] == "7c39ef960e984f06103f2957"
    assert int(regression_summary["total_branch_count"]) == 4896
    assert int(regression_summary["shard_count"]) == 2
    assert regression_summary["branch_partition_complete"] is True
    assert int(regression_summary["unknown_branch_count"]) == 0
    assert int(regression_summary["exact_numerical_survivor_count"]) == 0

    cells: list[dict[str, Any]] = []
    work_items: list[dict[str, Any]] = []
    for row in delta_rows:
        total = int(row["materialized_branch_count"])
        shard_count = math.ceil(total / MAX_BRANCHES_PER_WORK_ITEM)
        cell = {
            "cell_index": int(row["cell_index"]),
            "cell_id": str(row["cell_id"]),
            "total_branches": total,
            "shard_count": shard_count,
        }
        cells.append(cell)
        for shard_index in range(shard_count):
            branches = expected_mod_count(total, shard_count, shard_index)
            assert 0 < branches <= MAX_BRANCHES_PER_WORK_ITEM
            work_items.append(
                {
                    **cell,
                    "shard_index": shard_index,
                    "expected_shard_branches": branches,
                }
            )
    cells.sort(key=lambda r: (r["total_branches"], r["cell_id"]))
    assert len(cells) == EXPECTED_DELTA_CELLS
    assert len(work_items) == 287
    assert sum(int(i["expected_shard_branches"]) for i in work_items) == EXPECTED_DELTA_BRANCHES

    # Deterministic longest-processing-time packing. The declared branch count is the
    # exact materialized workload proxy; no mathematical or heuristic pruning changes.
    bundles: list[dict[str, Any]] = [
        {"bundle_id": f"b{i:03d}", "expected_branches": 0, "items": []}
        for i in range(BUNDLE_COUNT)
    ]
    ordered = sorted(
        work_items,
        key=lambda r: (
            -int(r["expected_shard_branches"]),
            int(r["cell_index"]),
            int(r["shard_index"]),
        ),
    )
    for item in ordered:
        target = min(
            bundles,
            key=lambda b: (
                int(b["expected_branches"]),
                len(b["items"]),
                str(b["bundle_id"]),
            ),
        )
        target["items"].append(item)
        target["expected_branches"] += int(item["expected_shard_branches"])
    for bundle in bundles:
        bundle["items"].sort(
            key=lambda r: (int(r["cell_index"]), int(r["shard_index"]))
        )
        bundle["item_count"] = len(bundle["items"])
        assert bundle["items"]

    assigned = [
        (int(i["cell_index"]), int(i["shard_index"]), int(i["shard_count"]))
        for b in bundles
        for i in b["items"]
    ]
    expected_assigned = [
        (int(i["cell_index"]), int(i["shard_index"]), int(i["shard_count"]))
        for i in work_items
    ]
    assert sorted(assigned) == sorted(expected_assigned)
    loads = sorted(int(b["expected_branches"]) for b in bundles)
    pilot = max(
        bundles,
        key=lambda b: (int(b["expected_branches"]), len(b["items"]), str(b["bundle_id"])),
    )
    bulk_matrix = [
        {"bundle_id": str(b["bundle_id"])}
        for b in bundles
        if b["bundle_id"] != pilot["bundle_id"]
    ]
    assert len(bulk_matrix) == BUNDLE_COUNT - 1
    waves: list[dict[str, Any]] = []
    wave_matrices: list[list[dict[str, str]]] = []
    for wave_index in range(WAVE_COUNT):
        wave_bundles = [b for i, b in enumerate(bundles) if i % WAVE_COUNT == wave_index]
        matrix = [
            {"bundle_id": str(b["bundle_id"])}
            for b in wave_bundles
            if b["bundle_id"] != pilot["bundle_id"]
        ]
        waves.append(
            {
                "wave_index": wave_index,
                "bundle_ids": [str(b["bundle_id"]) for b in wave_bundles],
                "bundle_count": len(wave_bundles),
                "bulk_bundle_count_after_pilot_exclusion": len(matrix),
                "expected_branches": sum(
                    int(b["expected_branches"]) for b in wave_bundles
                ),
            }
        )
        wave_matrices.append(matrix)
    assert [w["bundle_count"] for w in waves] == [12, 12, 12, 12]
    assert sum(int(w["expected_branches"]) for w in waves) == EXPECTED_DELTA_BRANCHES
    assert waves[0]["bulk_bundle_count_after_pilot_exclusion"] == 11
    assert all(w["bulk_bundle_count_after_pilot_exclusion"] == 12 for w in waves[1:])

    branch_counts = sorted(int(r["materialized_branch_count"]) for r in delta_rows)
    bins = Counter(
        f"{((v - 1) // 8192) * 8192 + 1}-{((v - 1) // 8192 + 1) * 8192}"
        for v in branch_counts
    )
    report = {
        "schema": PLAN_SCHEMA,
        "parameters": {
            "degree": 8,
            "genus": 0,
            "exceptional_mass": 20,
            "curve_group_mass": 0,
            "node_limit_per_branch": 1_000_000,
        },
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
        "selection_rule": "ALL_E20_A0_SIGNATURE_CELLS_WITH_16384_LT_BRANCH_COUNT_LE_65536",
        "selected_delta_cells": cells,
        "branch_count_distribution": {
            "minimum": branch_counts[0],
            "q10_nearest": quantile_nearest(branch_counts, 0.10),
            "q25_nearest": quantile_nearest(branch_counts, 0.25),
            "median_nearest": quantile_nearest(branch_counts, 0.50),
            "q75_nearest": quantile_nearest(branch_counts, 0.75),
            "q90_nearest": quantile_nearest(branch_counts, 0.90),
            "maximum": branch_counts[-1],
            "mean_numerator": EXPECTED_DELTA_BRANCHES,
            "mean_denominator": EXPECTED_DELTA_CELLS,
            "bins_width_8192": dict(sorted(bins.items())),
        },
        "execution_architecture": {
            "partition_rule": "DYNAMIC_GLOBAL_BRANCH_INDEX_MOD_CEIL_TOTAL_OVER_32768",
            "max_expected_branches_per_work_item": MAX_BRANCHES_PER_WORK_ITEM,
            "work_item_count": len(work_items),
            "bundle_packing": "DETERMINISTIC_LPT_BY_EXPECTED_MATERIALIZED_BRANCH_COUNT",
            "bundle_count": BUNDLE_COUNT,
            "bounded_wave_count": WAVE_COUNT,
            "max_parallel_bundles": MAX_PARALLEL_BUNDLES,
            "bundle_expected_branch_minimum": loads[0],
            "bundle_expected_branch_median": quantile_nearest(loads, 0.5),
            "bundle_expected_branch_maximum": loads[-1],
            "bundle_load_spread": loads[-1] - loads[0],
            "single_exact_context_initialization_per_bundle": True,
            "raw_items_verified_and_compacted_sequentially": True,
        },
        "pilot_bundle_id": pilot["bundle_id"],
        "representative_predecessor_regression": {
            "bundle_id": "predecessor-regression-cell588-s0of2",
            "purpose": "NARROW_EQUIVALENCE_CHECK_ONLY_NOT_PART_OF_DELTA",
            "item": {
                "cell_index": 588,
                "cell_id": "7c39ef960e984f06103f2957",
                "total_branches": 4896,
                "shard_count": 2,
                "shard_index": 0,
                "expected_shard_branches": 2448,
            },
            "expected_branch_exact_evidence_stream_sha256": regression_summary[
                "branch_evidence_stream_shas"
            ][0],
            "expected_exact_numerical_survivor_count": 0,
            "expected_signature_cell_sha256": "f01766288f110f465d0486593de8948898468c720eeeddcd943ffdd680538e40",
            "expected_shared_context_certificate_sha256": "5315b8188d36ca4ae35d3d943cd10b8783a3e602fd157b83a4bf6b1e725ab835",
        },
        "bundles": bundles,
        "bounded_waves": waves,
        "storage_safety": {
            "artifact_count": BUNDLE_COUNT,
            "compact_certificate_count": len(work_items),
            "max_compact_bytes_per_item": MAX_COMPACT_BYTES_PER_ITEM,
            "hard_compact_storage_upper_bound_bytes": len(work_items)
            * MAX_COMPACT_BYTES_PER_ITEM,
            "max_runner_local_raw_bytes_per_item": MAX_RUNNER_LOCAL_RAW_BYTES,
            "max_simultaneous_runner_local_raw_items": MAX_PARALLEL_BUNDLES,
            "raw_items_retained_after_post_verification_compaction": False,
            "transient_bundle_retention_days": 1,
        },
        "stage32_15_measured_baseline": {
            "workflow_run_id": 32726279718,
            "functional_commit": "649c7673256734cf9acbbf3e75616ebf72d5b1e9",
            "bulk_jobs_measured": 105,
            "bulk_runner_seconds": 11_524,
            "bulk_exact_step_seconds": 8_197,
            "bulk_non_exact_step_seconds": 3_327,
            "median_bulk_job_seconds": 109,
            "median_exact_step_seconds": 79,
            "median_non_exact_step_seconds": 31,
            "measured_bulk_branches": 604_320,
            "fixed_two_shards_per_cell_projected_jobs_for_current_delta": 464,
            "current_bundle_jobs": BUNDLE_COUNT,
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
        with args.github_output.open("a") as handle:
            handle.write(f"bulk_matrix={json.dumps(bulk_matrix, separators=(',', ':'))}\n")
            for wave_index, matrix in enumerate(wave_matrices):
                handle.write(
                    f"wave{wave_index}_matrix={json.dumps(matrix, separators=(',', ':'))}\n"
                )
            handle.write(f"pilot_bundle_id={pilot['bundle_id']}\n")
            handle.write(f"plan_sha={report['canonical_sha256_without_this_field']}\n")

    print(
        json.dumps(
            {
                "delta_cells": EXPECTED_DELTA_CELLS,
                "delta_branches": EXPECTED_DELTA_BRANCHES,
                "work_items": len(work_items),
                "bundles": BUNDLE_COUNT,
                "bundle_load_min": loads[0],
                "bundle_load_max": loads[-1],
                "pilot_bundle": pilot["bundle_id"],
                "plan_sha": report["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
