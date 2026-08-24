#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
from typing import Any

PROFILE_SCHEMA = "STAGE32_D8_MATERIALIZATION_SCHEDULE_PROFILE_V1"
PREV_SCHEMA = "STAGE32_D8_E20_A0_EXACT_TIER_LE65536_V1"
PLAN_SCHEMA = "STAGE32_D8_E20_A0_TIER114186_WORK_BALANCED_PLAN_V1"
EXPECTED_PROFILE_SHA = "e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384534d53fa1fee67c5"
EXPECTED_PREV_SHA = "5e6a447f7df3a712d6b8c873bc7e912f58b74b44cf4f461dc4cecd800c9e516c"
PREV_THRESHOLD = 65_536
TARGET_THRESHOLD = 114_186
NEXT_PLATEAU_BRANCH_COUNT = 115_712
NEXT_PLATEAU_CELL_MULTIPLICITY = 128
EXPECTED_PREV_CELLS = 301
EXPECTED_PREV_BRANCHES = 6_834_114
EXPECTED_DELTA_CELLS = 116
EXPECTED_DELTA_BRANCHES = 9_890_148
EXPECTED_CUMULATIVE_CELLS = 417
EXPECTED_CUMULATIVE_BRANCHES = 16_724_262
EXPECTED_WORK_ITEMS = 364
MAX_BRANCHES_PER_WORK_ITEM = 32_768
BUNDLE_COUNT = 80
WAVE_COUNT = 4
MAX_PARALLEL_BUNDLES = 8


def csha(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def mod_count(total: int, count: int, index: int) -> int:
    return total // count + (1 if index < total % count else 0)


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
    assert int(profile["signature_cell_count"]) == 1182

    assert prev["schema"] == PREV_SCHEMA
    unsigned = dict(prev)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    assert claimed == EXPECTED_PREV_SHA and csha(unsigned) == claimed
    assert int(prev["chosen_cumulative_branch_threshold"]) == PREV_THRESHOLD
    assert int(prev["selected_cell_count"]) == EXPECTED_PREV_CELLS
    assert int(prev["selected_total_materialized_branches"]) == EXPECTED_PREV_BRANCHES
    assert prev["selected_cells_exactly_complete"] is True
    assert int(prev["unknown_branch_count"]) == 0
    assert int(prev["exact_numerical_survivor_count"]) == 0

    rows = list(profile["cells_sorted_by_branch_count"])
    prev_rows = [r for r in rows if int(r["materialized_branch_count"]) <= PREV_THRESHOLD]
    target_rows = [r for r in rows if int(r["materialized_branch_count"]) <= TARGET_THRESHOLD]
    delta_rows = [r for r in target_rows if int(r["materialized_branch_count"]) > PREV_THRESHOLD]
    above = sorted(int(r["materialized_branch_count"]) for r in rows if int(r["materialized_branch_count"]) > TARGET_THRESHOLD)

    assert len(prev_rows) == EXPECTED_PREV_CELLS
    assert sum(int(r["materialized_branch_count"]) for r in prev_rows) == EXPECTED_PREV_BRANCHES
    assert len(delta_rows) == EXPECTED_DELTA_CELLS
    assert sum(int(r["materialized_branch_count"]) for r in delta_rows) == EXPECTED_DELTA_BRANCHES
    assert len(target_rows) == EXPECTED_CUMULATIVE_CELLS
    assert sum(int(r["materialized_branch_count"]) for r in target_rows) == EXPECTED_CUMULATIVE_BRANCHES
    assert above[0] == NEXT_PLATEAU_BRANCH_COUNT
    assert sum(v == NEXT_PLATEAU_BRANCH_COUNT for v in above) == NEXT_PLATEAU_CELL_MULTIPLICITY

    prev_keys = {(int(c["cell_index"]), str(c["cell_id"])) for c in prev["cell_summaries"]}
    profile_prev_keys = {(int(r["cell_index"]), str(r["cell_id"])) for r in prev_rows}
    assert prev_keys == profile_prev_keys

    cells: list[dict[str, Any]] = []
    items: list[dict[str, Any]] = []
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
            n = mod_count(total, shard_count, shard_index)
            assert 0 < n <= MAX_BRANCHES_PER_WORK_ITEM
            items.append({**cell, "shard_index": shard_index, "expected_shard_branches": n})
    cells.sort(key=lambda r: (r["total_branches"], r["cell_id"]))
    assert len(items) == EXPECTED_WORK_ITEMS
    assert sum(int(i["expected_shard_branches"]) for i in items) == EXPECTED_DELTA_BRANCHES

    bundles = [
        {"bundle_id": f"b{i:03d}", "expected_branches": 0, "items": []}
        for i in range(BUNDLE_COUNT)
    ]
    for item in sorted(items, key=lambda r: (-int(r["expected_shard_branches"]), int(r["cell_index"]), int(r["shard_index"]))):
        target = min(bundles, key=lambda b: (int(b["expected_branches"]), len(b["items"]), str(b["bundle_id"])))
        target["items"].append(item)
        target["expected_branches"] += int(item["expected_shard_branches"])
    for b in bundles:
        b["items"].sort(key=lambda r: (int(r["cell_index"]), int(r["shard_index"])))
        b["item_count"] = len(b["items"])
        assert b["items"]

    loads = sorted(int(b["expected_branches"]) for b in bundles)
    assert loads[0] == 109_826 and loads[-1] == 134_565
    pilot = max(bundles, key=lambda b: (int(b["expected_branches"]), len(b["items"]), str(b["bundle_id"])))
    assert pilot["bundle_id"] == "b066" and int(pilot["expected_branches"]) == 134_565

    waves = []
    matrices = []
    for wi in range(WAVE_COUNT):
        wave_bundles = [b for i, b in enumerate(bundles) if i % WAVE_COUNT == wi]
        matrix = [{"bundle_id": str(b["bundle_id"])} for b in wave_bundles if b["bundle_id"] != pilot["bundle_id"]]
        waves.append({
            "wave_index": wi,
            "bundle_ids": [str(b["bundle_id"]) for b in wave_bundles],
            "bundle_count": len(wave_bundles),
            "bulk_bundle_count_after_pilot_exclusion": len(matrix),
            "expected_branches": sum(int(b["expected_branches"]) for b in wave_bundles),
        })
        matrices.append(matrix)
    assert [w["bundle_count"] for w in waves] == [20, 20, 20, 20]
    assert sum(w["bulk_bundle_count_after_pilot_exclusion"] for w in waves) == 79

    regression = next(c for c in prev["cell_summaries"] if int(c["cell_index"]) == 48)
    assert regression["cell_id"] == "09d0449f1e53b0a4e6c5e115"
    assert int(regression["total_branch_count"]) == 52_992
    assert int(regression["shard_count"]) == 2
    assert regression["branch_evidence_stream_shas"][0] == "b6d30e4f6d73d6e545d9594c29cebcbc4394f854d493b49b6c6aaa91233534b0"

    report = {
        "schema": PLAN_SCHEMA,
        "parameters": {"degree": 8, "genus": 0, "exceptional_mass": 20, "curve_group_mass": 0, "node_limit_per_branch": 1_000_000},
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
        "selection_rule": "ALL_E20_A0_SIGNATURE_CELLS_WITH_65536_LT_BRANCH_COUNT_LE_114186",
        "selected_delta_cells": cells,
        "next_profile_wall": {
            "branch_count": NEXT_PLATEAU_BRANCH_COUNT,
            "cell_multiplicity": NEXT_PLATEAU_CELL_MULTIPLICITY,
            "reason_for_stop": "STOP_IMMEDIATELY_BEFORE_128_CELL_EQUAL_BRANCH_COUNT_PLATEAU",
        },
        "execution_architecture": {
            "partition_rule": "DYNAMIC_GLOBAL_BRANCH_INDEX_MOD_CEIL_TOTAL_OVER_32768",
            "max_expected_branches_per_work_item": MAX_BRANCHES_PER_WORK_ITEM,
            "work_item_count": EXPECTED_WORK_ITEMS,
            "bundle_packing": "DETERMINISTIC_LPT_BY_EXPECTED_MATERIALIZED_BRANCH_COUNT",
            "bundle_count": BUNDLE_COUNT,
            "bounded_wave_count": WAVE_COUNT,
            "max_parallel_bundles": MAX_PARALLEL_BUNDLES,
            "bundle_expected_branch_minimum": loads[0],
            "bundle_expected_branch_maximum": loads[-1],
            "single_exact_context_initialization_per_bundle": True,
            "raw_items_verified_and_compacted_sequentially": True,
            "stage32_16_runner_reused_without_solver_semantic_change": True,
        },
        "pilot_bundle_id": pilot["bundle_id"],
        "representative_predecessor_regression": {
            "bundle_id": "predecessor-regression-cell48-s0of2",
            "purpose": "NARROW_EQUIVALENCE_CHECK_AGAINST_AUDITED_LE65536_PREDECESSOR",
            "item": {"cell_index": 48, "cell_id": "09d0449f1e53b0a4e6c5e115", "total_branches": 52_992, "shard_count": 2, "shard_index": 0, "expected_shard_branches": 26_496},
            "expected_branch_exact_evidence_stream_sha256": "b6d30e4f6d73d6e545d9594c29cebcbc4394f854d493b49b6c6aaa91233534b0",
            "expected_exact_numerical_survivor_count": 0,
            "expected_signature_cell_sha256": "35e8236d4545cbb7506c217db10654cf5aa0b4f534ea41537afbf4c5bb0cb72c",
            "expected_shared_context_certificate_sha256": "5315b8188d36ca4ae35d3d943cd10b8783a3e602fd157b83a4bf6b1e725ab835",
        },
        "bundles": bundles,
        "bounded_waves": waves,
        "storage_safety": {
            "artifact_count": BUNDLE_COUNT,
            "compact_certificate_count": EXPECTED_WORK_ITEMS,
            "max_compact_bytes_per_item": 20_000,
            "hard_compact_storage_upper_bound_bytes": EXPECTED_WORK_ITEMS * 20_000,
            "max_runner_local_raw_bytes_per_item": 1_000_000_000,
            "max_simultaneous_runners": MAX_PARALLEL_BUNDLES,
            "raw_items_retained_after_post_verification_compaction": False,
            "transient_bundle_retention_days": 1,
        },
        "stage32_16_measured_baseline": {
            "workflow_run_id": 32733420941,
            "measured_bundle_seconds_per_branch": 0.008521564114,
            "measured_workflow_throughput_branches_per_wall_second": 588.265828810816,
            "previous_bundle_count": 48,
            "current_bundle_count": BUNDLE_COUNT,
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
        with args.github_output.open("a") as fh:
            for i, matrix in enumerate(matrices):
                fh.write(f"wave{i}_matrix={json.dumps({'include': matrix}, separators=(',', ':'))}\n")
            fh.write(f"pilot_bundle_id={pilot['bundle_id']}\n")
            fh.write(f"plan_sha={report['canonical_sha256_without_this_field']}\n")

    print(json.dumps({
        "delta_cells": EXPECTED_DELTA_CELLS,
        "delta_branches": EXPECTED_DELTA_BRANCHES,
        "work_items": EXPECTED_WORK_ITEMS,
        "bundles": BUNDLE_COUNT,
        "load_min": loads[0],
        "load_max": loads[-1],
        "next_plateau": NEXT_PLATEAU_BRANCH_COUNT,
        "next_plateau_cells": NEXT_PLATEAU_CELL_MULTIPLICITY,
        "sha": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
