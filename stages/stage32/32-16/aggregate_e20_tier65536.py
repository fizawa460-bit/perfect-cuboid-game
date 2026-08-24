#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import statistics
from typing import Any

PROFILE_SCHEMA = "STAGE32_D8_MATERIALIZATION_SCHEDULE_PROFILE_V1"
PREV_SCHEMA = "STAGE32_D8_E20_A0_EXACT_TIER_LE16384_V1"
PLAN_SCHEMA = "STAGE32_D8_E20_A0_TIER65536_WORK_BALANCED_PLAN_V1"
CERT_SCHEMA = "STAGE32_D8_E20_A0_DYNAMIC_SHARD_COMPACT_CERT_V1"
RECEIPT_SCHEMA = "STAGE32_D8_E20_A0_EXACT_WORK_BUNDLE_RECEIPT_V1"
OUT_SCHEMA = "STAGE32_D8_E20_A0_EXACT_TIER_LE65536_V1"
EXPECTED_PROFILE_SHA = "e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384534d53fa1fee67c5"
EXPECTED_PREV_SHA = "593bb0fc5231222ab9ce79ae0bd5802d77311d02fd633152d665f869b095611f"


def csha(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def expected_mod_count(total: int, shard_count: int, shard_index: int) -> int:
    return total // shard_count + (1 if shard_index < total % shard_count else 0)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", type=pathlib.Path, required=True)
    ap.add_argument("--predecessor", type=pathlib.Path, required=True)
    ap.add_argument("--plan", type=pathlib.Path, required=True)
    ap.add_argument("--input-dir", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    profile = json.loads(args.profile.read_text())
    prev = json.loads(args.predecessor.read_text())
    plan = json.loads(args.plan.read_text())
    assert profile["schema"] == PROFILE_SCHEMA
    assert profile["canonical_sha256_without_this_field"] == EXPECTED_PROFILE_SHA
    assert prev["schema"] == PREV_SCHEMA
    prev_unsigned = dict(prev)
    prev_claimed = prev_unsigned.pop("canonical_sha256_without_this_field")
    assert prev_claimed == EXPECTED_PREV_SHA and csha(prev_unsigned) == prev_claimed
    assert plan["schema"] == PLAN_SCHEMA
    plan_unsigned = dict(plan)
    plan_claimed = plan_unsigned.pop("canonical_sha256_without_this_field")
    assert csha(plan_unsigned) == plan_claimed
    assert plan["profile_sha256"] == EXPECTED_PROFILE_SHA
    assert plan["predecessor_sha256"] == EXPECTED_PREV_SHA
    assert int(plan["predecessor_threshold"]) == 16_384
    assert int(plan["target_threshold"]) == 65_536
    assert int(plan["delta_cell_count"]) == 232
    assert int(plan["delta_branch_count"]) == 6_178_556
    assert int(plan["cumulative_cell_count"]) == 301
    assert int(plan["cumulative_branch_count"]) == 6_834_114

    target_rows = [
        r
        for r in profile["cells_sorted_by_branch_count"]
        if int(r["materialized_branch_count"]) <= 65_536
    ]
    delta_rows = [
        r for r in target_rows if int(r["materialized_branch_count"]) > 16_384
    ]
    delta = {
        (int(r["cell_index"]), str(r["cell_id"])): int(
            r["materialized_branch_count"]
        )
        for r in delta_rows
    }
    planned = {
        (int(c["cell_index"]), str(c["cell_id"])): (
            int(c["total_branches"]),
            int(c["shard_count"]),
        )
        for c in plan["selected_delta_cells"]
    }
    assert len(delta) == 232 and len(planned) == 232
    assert all(delta[k] == planned[k][0] for k in delta)
    assert set(delta) == set(planned)

    expected_items: dict[tuple[int, int], dict[str, Any]] = {}
    expected_bundles: dict[str, dict[str, Any]] = {}
    for bundle in plan["bundles"]:
        bundle_id = str(bundle["bundle_id"])
        assert bundle_id not in expected_bundles
        expected_bundles[bundle_id] = bundle
        for item in bundle["items"]:
            key = (int(item["cell_index"]), int(item["shard_index"]))
            assert key not in expected_items
            expected_items[key] = {**item, "bundle_id": bundle_id}
    assert len(expected_items) == 287 and len(expected_bundles) == 48

    certs: dict[tuple[int, int], dict[str, Any]] = {}
    cert_paths = sorted(args.input_dir.rglob("*-compact.json"))
    for path in cert_paths:
        row = json.loads(path.read_text())
        assert row["schema"] == CERT_SCHEMA
        unsigned = dict(row)
        claimed = unsigned.pop("canonical_sha256_without_this_field")
        assert csha(unsigned) == claimed
        p = row["parameters"]
        key = (int(p["cell_index"]), int(p["shard_index"]))
        assert key in expected_items and key not in certs
        certs[key] = row
    assert set(certs) == set(expected_items), (len(certs), len(expected_items))

    receipts: dict[str, dict[str, Any]] = {}
    for path in sorted(args.input_dir.rglob("bundle-receipt.json")):
        row = json.loads(path.read_text())
        assert row["schema"] == RECEIPT_SCHEMA
        unsigned = dict(row)
        claimed = unsigned.pop("canonical_sha256_without_this_field")
        assert csha(unsigned) == claimed
        bundle_id = str(row["bundle_id"])
        assert bundle_id in expected_bundles and bundle_id not in receipts
        assert row["plan_sha256"] == plan_claimed
        deterministic = {
            k: v
            for k, v in row.items()
            if k
            not in {
                "environment",
                "runtime",
                "deterministic_sha256_without_environment_or_runtime",
                "canonical_sha256_without_this_field",
            }
        }
        assert csha(deterministic) == row[
            "deterministic_sha256_without_environment_or_runtime"
        ]
        assert row["all_items_complete"] is True
        assert int(row["unknown_branch_count"]) == 0
        assert row["runner_local_raw_evidence_deleted_after_verification"] is True
        assert row["raw_branch_rows_uploaded"] is False
        assert row["theorem_credit"] is False and row["receiver_credit"] is False
        receipts[bundle_id] = row
    assert set(receipts) == set(expected_bundles), (len(receipts), len(expected_bundles))

    for bundle_id, bundle in expected_bundles.items():
        receipt = receipts[bundle_id]
        expected_keys = [
            (int(i["cell_index"]), int(i["shard_index"])) for i in bundle["items"]
        ]
        got_keys = [
            (int(i["cell_index"]), int(i["shard_index"]))
            for i in receipt["certificates"]
        ]
        assert got_keys == expected_keys
        assert int(receipt["item_count"]) == len(expected_keys)
        assert int(receipt["planned_expected_branches"]) == int(
            bundle["expected_branches"]
        )
        assert int(receipt["executed_branches"]) == int(bundle["expected_branches"])
        for item_receipt in receipt["certificates"]:
            key = (
                int(item_receipt["cell_index"]),
                int(item_receipt["shard_index"]),
            )
            cert = certs[key]
            assert item_receipt["compact_canonical_sha256"] == cert[
                "canonical_sha256_without_this_field"
            ]
            assert item_receipt["raw_deterministic_sha256"] == cert[
                "source_raw_deterministic_sha256"
            ]
            assert item_receipt["branch_exact_evidence_stream_sha256"] == cert[
                "branch_exact_evidence_stream_sha256"
            ]

    delta_summaries: list[dict[str, Any]] = []
    delta_survivors: list[dict[str, Any]] = []
    delta_nodes = 0
    for (idx, cid), branches in sorted(delta.items()):
        shard_count = planned[(idx, cid)][1]
        survivors: list[dict[str, Any]] = []
        cell_nodes = executed = 0
        compact_shas: list[str] = []
        raw_shas: list[str] = []
        stream_shas: list[str] = []
        bundle_ids: list[str] = []
        for shard_index in range(shard_count):
            row = certs[(idx, shard_index)]
            p = row["parameters"]
            assert int(p["degree"]) == 8 and int(p["genus"]) == 0
            assert int(p["exceptional_mass"]) == 20
            assert int(p["curve_group_mass"]) == 0
            assert int(p["cell_index"]) == idx and str(p["cell_id"]) == cid
            assert int(p["shard_index"]) == shard_index
            assert int(p["shard_count"]) == shard_count
            assert int(p["node_limit_per_branch"]) == 1_000_000
            assert int(row["parent_cell_total_branch_count"]) == branches
            assert row["all_branch_indices_exact_mod_partition"] is True
            assert row["all_branches_complete"] is True
            assert int(row["unknown_branch_count"]) == 0
            assert row["compaction_is_post_verification_only"] is True
            assert row["raw_branch_rows_persisted"] is False
            assert row["theorem_credit"] is False and row["receiver_credit"] is False
            want = expected_mod_count(branches, shard_count, shard_index)
            assert int(row["executed_shard_branch_count"]) == want
            assert int(row["first_branch_index"]) == shard_index
            assert int(row["last_branch_index"]) == (
                shard_index + (want - 1) * shard_count
            )
            executed += want
            cell_nodes += int(row["total_search_nodes"])
            survivors.extend(row["numerical_survivors"])
            compact_shas.append(row["canonical_sha256_without_this_field"])
            raw_shas.append(row["source_raw_deterministic_sha256"])
            stream_shas.append(row["branch_exact_evidence_stream_sha256"])
            bundle_ids.append(expected_items[(idx, shard_index)]["bundle_id"])
        assert executed == branches
        survivors.sort(key=lambda r: tuple(r["basis_coordinates"]))
        keys = [tuple(r["basis_coordinates"]) for r in survivors]
        assert len(keys) == len(set(keys))
        delta_survivors.extend(survivors)
        delta_nodes += cell_nodes
        delta_summaries.append(
            {
                "cell_index": idx,
                "cell_id": cid,
                "total_branch_count": branches,
                "shard_count": shard_count,
                "branch_partition_complete": True,
                "unknown_branch_count": 0,
                "solver_result": "SAT_EXHAUSTED" if survivors else "UNSAT",
                "exact_numerical_survivor_count": len(survivors),
                "search_nodes": cell_nodes,
                "bundle_ids": bundle_ids,
                "compact_certificate_shas": compact_shas,
                "source_raw_deterministic_shas": raw_shas,
                "branch_evidence_stream_shas": stream_shas,
                "numerical_survivors": survivors,
            }
        )

    all_summaries = list(prev["cell_summaries"]) + delta_summaries
    all_summaries.sort(key=lambda c: int(c["cell_index"]))
    all_survivors = list(prev["numerical_survivors"]) + delta_survivors
    all_survivors.sort(key=lambda r: tuple(r["basis_coordinates"]))
    keys = [tuple(r["basis_coordinates"]) for r in all_survivors]
    assert len(keys) == len(set(keys))
    target_keys = {(int(r["cell_index"]), str(r["cell_id"])) for r in target_rows}
    summary_keys = {(int(c["cell_index"]), str(c["cell_id"])) for c in all_summaries}
    assert summary_keys == target_keys and len(all_summaries) == 301
    total_branches = sum(int(c["total_branch_count"]) for c in all_summaries)
    assert total_branches == 6_834_114

    bundle_seconds = [float(r["runtime"]["bundle_elapsed_seconds"]) for r in receipts.values()]
    context_seconds = [
        float(r["runtime"]["context_initialization_seconds"]) for r in receipts.values()
    ]
    total_compact_bytes = sum(
        int(r["runtime"]["total_compact_bytes"]) for r in receipts.values()
    )
    maximum_raw_bytes = max(
        int(r["runtime"]["maximum_runner_local_raw_bytes"]) for r in receipts.values()
    )
    baseline = plan["stage32_15_measured_baseline"]
    previous_exact_seconds_per_branch = float(baseline["bulk_exact_step_seconds"]) / int(
        baseline["measured_bulk_branches"]
    )
    new_bundle_seconds_per_branch = sum(bundle_seconds) / 6_178_556

    runtime_measurements = {
        "bundle_count": len(bundle_seconds),
        "work_item_count": len(certs),
        "bundle_runner_seconds_total": round(sum(bundle_seconds), 6),
        "bundle_runner_seconds_minimum": round(min(bundle_seconds), 6),
        "bundle_runner_seconds_median": round(statistics.median(bundle_seconds), 6),
        "bundle_runner_seconds_maximum": round(max(bundle_seconds), 6),
        "context_initialization_seconds_total": round(sum(context_seconds), 6),
        "maximum_runner_local_raw_bytes": maximum_raw_bytes,
        "uploaded_compact_bytes_total": total_compact_bytes,
        "fixed_two_shard_projected_job_count": int(
            baseline["fixed_two_shards_per_cell_projected_jobs_for_current_delta"]
        ),
        "actual_bundle_job_count": len(bundle_seconds),
        "job_count_reduction_numerator": int(
            baseline["fixed_two_shards_per_cell_projected_jobs_for_current_delta"]
        )
        - len(bundle_seconds),
        "job_count_reduction_denominator": int(
            baseline["fixed_two_shards_per_cell_projected_jobs_for_current_delta"]
        ),
        "stage32_15_measured_exact_seconds_per_branch": round(
            previous_exact_seconds_per_branch, 12
        ),
        "stage32_16_measured_bundle_seconds_per_branch": round(
            new_bundle_seconds_per_branch, 12
        ),
        "measured_runner_efficiency_ratio_stage32_15_over_stage32_16": round(
            previous_exact_seconds_per_branch / new_bundle_seconds_per_branch, 6
        ),
        "note": "Runner totals compare resource efficiency; parallel workflow wall time is recorded in the audit artifact from the Actions run timestamps.",
    }

    report = {
        "schema": OUT_SCHEMA,
        "evidence_storage_mode": "SEQUENTIAL_RUNNER_LOCAL_RAW_THEN_POST_VERIFICATION_COMPACT_CERTIFICATES",
        "profile_sha256": EXPECTED_PROFILE_SHA,
        "predecessor_sha256": EXPECTED_PREV_SHA,
        "delta_plan_sha256": plan_claimed,
        "parameters": {
            "degree": 8,
            "genus": 0,
            "exceptional_mass": 20,
            "curve_group_mass": 0,
            "node_limit_per_branch": 1_000_000,
        },
        "chosen_cumulative_branch_threshold": 65_536,
        "predecessor_cell_count": 69,
        "delta_cell_count": 232,
        "selected_cell_count": 301,
        "predecessor_materialized_branches": 655_558,
        "delta_materialized_branches": 6_178_556,
        "selected_total_materialized_branches": total_branches,
        "selected_cells_exactly_complete": True,
        "unknown_branch_count": 0,
        "predecessor_search_nodes": int(prev["total_search_nodes"]),
        "delta_search_nodes": delta_nodes,
        "total_search_nodes": int(prev["total_search_nodes"]) + delta_nodes,
        "exact_numerical_survivor_count": len(all_survivors),
        "numerical_survivors": all_survivors,
        "cell_summaries": all_summaries,
        "bundle_receipt_shas": {
            bundle_id: receipts[bundle_id]["canonical_sha256_without_this_field"]
            for bundle_id in sorted(receipts)
        },
        "runtime_and_architecture_measurements": runtime_measurements,
        "tier_scope": "ALL_E20_A0_SIGNATURE_CELLS_WITH_MATERIALIZED_BRANCH_COUNT_LE_65536",
        "parent_e20_a0_complete": False,
        "next_compute_wall": {
            "status": "NOT_EXECUTED_BY_SCOPE",
            "reason": "STOP_AT_DECLARED_CUMULATIVE_LE65536_AUDIT_BOUNDARY",
        },
        "effectivity_classification_complete": False,
        "actual_curve_existence_claim": False,
        "theorem_credit": False,
        "audit_status": "PENDING",
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
    print(
        json.dumps(
            {
                "cells": 301,
                "branches": total_branches,
                "delta_nodes": delta_nodes,
                "survivors": len(all_survivors),
                "unknown": 0,
                "bundles": len(bundle_seconds),
                "runner_efficiency_ratio": runtime_measurements[
                    "measured_runner_efficiency_ratio_stage32_15_over_stage32_16"
                ],
                "sha": report["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
