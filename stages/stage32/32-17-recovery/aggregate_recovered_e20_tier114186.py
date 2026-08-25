#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import statistics
from typing import Any

PROFILE_SCHEMA = "STAGE32_D8_MATERIALIZATION_SCHEDULE_PROFILE_V1"
PLAN_SCHEMA = "STAGE32_D8_E20_A0_TIER114186_WORK_BALANCED_PLAN_V1"
CERT_SCHEMA = "STAGE32_D8_E20_A0_DYNAMIC_SHARD_COMPACT_CERT_V1"
RECEIPT_SCHEMA = "STAGE32_D8_E20_A0_EXACT_WORK_BUNDLE_RECEIPT_V1"
AUDIT_SCHEMA = "STAGE32_16_E20_A0_LE65536_EXECUTION_STATE_V1"
OUT_SCHEMA = "STAGE32_D8_E20_A0_EXACT_TIER_LE114186_AUDIT_IMPORT_V2"
EXPECTED_PROFILE_SHA = "e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384534d53fa1fee67c5"
EXPECTED_PREV_SHA = "5e6a447f7df3a712d6b8c873bc7e912f58b74b44cf4f461dc4cecd800c9e516c"
EXPECTED_SHARED_CONTEXT_SHA = "5315b8188d36ca4ae35d3d943cd10b8783a3e602fd157b83a4bf6b1e725ab835"
PREV_THRESHOLD = 65_536
TARGET_THRESHOLD = 114_186
EXPECTED_PREV_CELLS = 301
EXPECTED_PREV_BRANCHES = 6_834_114
EXPECTED_PREV_NODES = 1_881_870
EXPECTED_DELTA_CELLS = 116
EXPECTED_DELTA_BRANCHES = 9_890_148
EXPECTED_CUMULATIVE_CELLS = 417
EXPECTED_CUMULATIVE_BRANCHES = 16_724_262
EXPECTED_WORK_ITEMS = 364
EXPECTED_BUNDLES = 80


def csha(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def expected_mod_count(total: int, shard_count: int, shard_index: int) -> int:
    return total // shard_count + (1 if shard_index < total % shard_count else 0)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", type=pathlib.Path, required=True)
    ap.add_argument("--predecessor-audit-state", type=pathlib.Path, required=True)
    ap.add_argument("--plan", type=pathlib.Path, required=True)
    ap.add_argument("--input-dir", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    profile = json.loads(args.profile.read_text())
    audit = json.loads(args.predecessor_audit_state.read_text())
    plan = json.loads(args.plan.read_text())

    assert profile["schema"] == PROFILE_SCHEMA
    profile_unsigned = dict(profile)
    profile_claimed = profile_unsigned.pop("canonical_sha256_without_this_field")
    assert profile_claimed == EXPECTED_PROFILE_SHA and csha(profile_unsigned) == profile_claimed
    assert int(profile["signature_cell_count"]) == 1182

    # Import only a repository-committed, hostile-audited predecessor. The old
    # transient Actions artifact may expire; the committed audit state records
    # both its canonical digest and an independent full reaggregation.
    assert audit["schema"] == AUDIT_SCHEMA
    assert audit["execution_verdict"] == "PASS_EXACT_E20_A0_DELTA_AND_CUMULATIVE_LE65536_ZERO_TIER"
    assert audit["audit_final_verdict"] == "PASS_EXACT_E20_A0_DELTA_AND_CUMULATIVE_LE65536_ZERO_TIER"
    assert audit["hostile_audit_required"] is False
    assert audit["profile_sha256"] == EXPECTED_PROFILE_SHA
    prev = audit["cumulative_tier"]
    assert int(prev["threshold"]) == PREV_THRESHOLD
    assert int(prev["cells"]) == EXPECTED_PREV_CELLS
    assert int(prev["materialized_branches"]) == EXPECTED_PREV_BRANCHES
    assert int(prev["search_nodes"]) == EXPECTED_PREV_NODES
    assert int(prev["unknown_branches"]) == 0
    assert int(prev["numerical_survivors"]) == 0
    assert prev["all_selected_cells_unsat"] is True
    assert prev["canonical_sha256"] == EXPECTED_PREV_SHA
    independent = audit["independent_reaggregation"]
    assert int(independent["all_bundle_artifacts_downloaded"]) == 48
    assert int(independent["all_compact_certificates_verified"]) == 287
    assert independent["parsed_aggregate_equal"] is True
    assert independent["canonical_sha256"] == EXPECTED_PREV_SHA

    assert plan["schema"] == PLAN_SCHEMA
    plan_unsigned = dict(plan)
    plan_claimed = plan_unsigned.pop("canonical_sha256_without_this_field")
    assert csha(plan_unsigned) == plan_claimed
    assert plan["profile_sha256"] == EXPECTED_PROFILE_SHA
    assert plan["predecessor_sha256"] == EXPECTED_PREV_SHA
    assert int(plan["predecessor_threshold"]) == PREV_THRESHOLD
    assert int(plan["target_threshold"]) == TARGET_THRESHOLD
    assert int(plan["predecessor_cell_count"]) == EXPECTED_PREV_CELLS
    assert int(plan["predecessor_branch_count"]) == EXPECTED_PREV_BRANCHES
    assert int(plan["delta_cell_count"]) == EXPECTED_DELTA_CELLS
    assert int(plan["delta_branch_count"]) == EXPECTED_DELTA_BRANCHES
    assert int(plan["cumulative_cell_count"]) == EXPECTED_CUMULATIVE_CELLS
    assert int(plan["cumulative_branch_count"]) == EXPECTED_CUMULATIVE_BRANCHES

    target_rows = [r for r in profile["cells_sorted_by_branch_count"] if int(r["materialized_branch_count"]) <= TARGET_THRESHOLD]
    prev_rows = [r for r in profile["cells_sorted_by_branch_count"] if int(r["materialized_branch_count"]) <= PREV_THRESHOLD]
    delta_rows = [r for r in target_rows if int(r["materialized_branch_count"]) > PREV_THRESHOLD]
    assert len(prev_rows) == EXPECTED_PREV_CELLS
    assert sum(int(r["materialized_branch_count"]) for r in prev_rows) == EXPECTED_PREV_BRANCHES
    assert len(target_rows) == EXPECTED_CUMULATIVE_CELLS
    assert sum(int(r["materialized_branch_count"]) for r in target_rows) == EXPECTED_CUMULATIVE_BRANCHES

    delta = {(int(r["cell_index"]), str(r["cell_id"])): int(r["materialized_branch_count"]) for r in delta_rows}
    planned = {
        (int(c["cell_index"]), str(c["cell_id"])): (int(c["total_branches"]), int(c["shard_count"]))
        for c in plan["selected_delta_cells"]
    }
    assert len(delta) == EXPECTED_DELTA_CELLS and len(planned) == EXPECTED_DELTA_CELLS
    assert set(delta) == set(planned)
    assert all(delta[k] == planned[k][0] for k in delta)
    assert sum(delta.values()) == EXPECTED_DELTA_BRANCHES

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
    assert len(expected_items) == EXPECTED_WORK_ITEMS
    assert len(expected_bundles) == EXPECTED_BUNDLES

    certs: dict[tuple[int, int], dict[str, Any]] = {}
    for path in sorted(args.input_dir.rglob("*-compact.json")):
        row = json.loads(path.read_text())
        if row.get("schema") != CERT_SCHEMA:
            continue
        unsigned = dict(row)
        claimed = unsigned.pop("canonical_sha256_without_this_field")
        assert csha(unsigned) == claimed
        assert row["shared_context_certificate_sha256"] == EXPECTED_SHARED_CONTEXT_SHA
        p = row["parameters"]
        key = (int(p["cell_index"]), int(p["shard_index"]))
        assert key in expected_items and key not in certs, (key, path)
        certs[key] = row
    assert set(certs) == set(expected_items), (len(certs), len(expected_items))

    receipts: dict[str, dict[str, Any]] = {}
    for path in sorted(args.input_dir.rglob("bundle-receipt.json")):
        row = json.loads(path.read_text())
        if row.get("schema") != RECEIPT_SCHEMA:
            continue
        unsigned = dict(row)
        claimed = unsigned.pop("canonical_sha256_without_this_field")
        assert csha(unsigned) == claimed
        bundle_id = str(row["bundle_id"])
        assert bundle_id in expected_bundles and bundle_id not in receipts, (bundle_id, path)
        assert row["plan_sha256"] == plan_claimed
        deterministic = {
            k: v for k, v in row.items()
            if k not in {"environment", "runtime", "deterministic_sha256_without_environment_or_runtime", "canonical_sha256_without_this_field"}
        }
        assert csha(deterministic) == row["deterministic_sha256_without_environment_or_runtime"]
        assert row["all_items_complete"] is True
        assert int(row["unknown_branch_count"]) == 0
        assert row["runner_local_raw_evidence_deleted_after_verification"] is True
        assert row["raw_branch_rows_uploaded"] is False
        assert row["theorem_credit"] is False and row["receiver_credit"] is False
        receipts[bundle_id] = row
    assert set(receipts) == set(expected_bundles), (len(receipts), len(expected_bundles))

    for bundle_id, bundle in expected_bundles.items():
        receipt = receipts[bundle_id]
        expected_keys = [(int(i["cell_index"]), int(i["shard_index"])) for i in bundle["items"]]
        got_keys = [(int(i["cell_index"]), int(i["shard_index"])) for i in receipt["certificates"]]
        assert got_keys == expected_keys
        assert int(receipt["item_count"]) == len(expected_keys)
        assert int(receipt["planned_expected_branches"]) == int(bundle["expected_branches"])
        assert int(receipt["executed_branches"]) == int(bundle["expected_branches"])
        for item_receipt in receipt["certificates"]:
            key = (int(item_receipt["cell_index"]), int(item_receipt["shard_index"]))
            cert = certs[key]
            assert item_receipt["compact_canonical_sha256"] == cert["canonical_sha256_without_this_field"]
            assert item_receipt["raw_deterministic_sha256"] == cert["source_raw_deterministic_sha256"]
            assert item_receipt["branch_exact_evidence_stream_sha256"] == cert["branch_exact_evidence_stream_sha256"]

    delta_summaries: list[dict[str, Any]] = []
    delta_survivors: list[dict[str, Any]] = []
    delta_nodes = 0
    for (idx, cid), branches in sorted(delta.items()):
        shard_count = planned[(idx, cid)][1]
        survivors: list[dict[str, Any]] = []
        cell_nodes = 0
        executed = 0
        compact_shas: list[str] = []
        raw_shas: list[str] = []
        stream_shas: list[str] = []
        bundle_ids: list[str] = []
        for shard_index in range(shard_count):
            row = certs[(idx, shard_index)]
            p = row["parameters"]
            assert int(p["degree"]) == 8 and int(p["genus"]) == 0
            assert int(p["exceptional_mass"]) == 20 and int(p["curve_group_mass"]) == 0
            assert int(p["cell_index"]) == idx and str(p["cell_id"]) == cid
            assert int(p["shard_index"]) == shard_index and int(p["shard_count"]) == shard_count
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
            assert int(row["last_branch_index"]) == shard_index + (want - 1) * shard_count
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
        delta_summaries.append({
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
        })

    delta_survivors.sort(key=lambda r: tuple(r["basis_coordinates"]))
    dkeys = [tuple(r["basis_coordinates"]) for r in delta_survivors]
    assert len(dkeys) == len(set(dkeys))
    # Main-stage credit is exact only when the imported audited prefix and the
    # newly reassembled delta are both survivor-free.
    assert not delta_survivors

    inventory = [
        {
            "cell_index": int(r["cell_index"]),
            "cell_id": str(r["cell_id"]),
            "materialized_branch_count": int(r["materialized_branch_count"]),
        }
        for r in target_rows
    ]
    assert len(inventory) == EXPECTED_CUMULATIVE_CELLS
    inventory_sha = csha(inventory)

    bundle_seconds = [float(r["runtime"]["bundle_elapsed_seconds"]) for r in receipts.values()]
    context_seconds = [float(r["runtime"]["context_initialization_seconds"]) for r in receipts.values()]
    total_compact_bytes = sum(int(r["runtime"]["total_compact_bytes"]) for r in receipts.values())
    maximum_raw_bytes = max(int(r["runtime"]["maximum_runner_local_raw_bytes"]) for r in receipts.values())

    report = {
        "schema": OUT_SCHEMA,
        "recovery_reason": "TRANSIENT_ANCESTOR_ACTIONS_ARTIFACTS_EXPIRED_AFTER_WAVE2; NO_SOLVER_FAILURE",
        "evidence_storage_mode": "AUDITED_PREDECESSOR_IMPORT_PLUS_EXACT_DELTA_COMPACT_CERTIFICATES",
        "profile_sha256": EXPECTED_PROFILE_SHA,
        "predecessor_sha256": EXPECTED_PREV_SHA,
        "delta_plan_sha256": plan_claimed,
        "parameters": {"degree": 8, "genus": 0, "exceptional_mass": 20, "curve_group_mass": 0, "node_limit_per_branch": 1_000_000},
        "chosen_cumulative_branch_threshold": TARGET_THRESHOLD,
        "predecessor_cell_count": EXPECTED_PREV_CELLS,
        "delta_cell_count": EXPECTED_DELTA_CELLS,
        "selected_cell_count": EXPECTED_CUMULATIVE_CELLS,
        "predecessor_materialized_branches": EXPECTED_PREV_BRANCHES,
        "delta_materialized_branches": EXPECTED_DELTA_BRANCHES,
        "selected_total_materialized_branches": EXPECTED_CUMULATIVE_BRANCHES,
        "selected_cells_exactly_complete": True,
        "unknown_branch_count": 0,
        "predecessor_search_nodes": EXPECTED_PREV_NODES,
        "delta_search_nodes": delta_nodes,
        "total_search_nodes": EXPECTED_PREV_NODES + delta_nodes,
        "exact_numerical_survivor_count": 0,
        "numerical_survivors": [],
        "predecessor_import": {
            "audit_state_path": "stages/stage32/32-16/execution-state.json",
            "audit_final_verdict": audit["audit_final_verdict"],
            "canonical_sha256": EXPECTED_PREV_SHA,
            "cells": EXPECTED_PREV_CELLS,
            "materialized_branches": EXPECTED_PREV_BRANCHES,
            "search_nodes": EXPECTED_PREV_NODES,
            "unknown_branches": 0,
            "numerical_survivors": 0,
            "independent_reaggregation": independent,
            "expired_transient_artifact_metadata": audit["final_artifact"],
        },
        "selected_cell_inventory": inventory,
        "selected_cell_inventory_sha256": inventory_sha,
        "delta_cell_summaries": delta_summaries,
        "bundle_receipt_shas": {bundle_id: receipts[bundle_id]["canonical_sha256_without_this_field"] for bundle_id in sorted(receipts)},
        "runtime_and_architecture_measurements": {
            "bundle_count": len(bundle_seconds),
            "work_item_count": len(certs),
            "bundle_runner_seconds_total": round(sum(bundle_seconds), 6),
            "bundle_runner_seconds_minimum": round(min(bundle_seconds), 6),
            "bundle_runner_seconds_median": round(statistics.median(bundle_seconds), 6),
            "bundle_runner_seconds_maximum": round(max(bundle_seconds), 6),
            "context_initialization_seconds_total": round(sum(context_seconds), 6),
            "maximum_runner_local_raw_bytes": maximum_raw_bytes,
            "uploaded_compact_bytes_total": total_compact_bytes,
        },
        "recovery_integrity": {
            "profile_rederived_and_exact_sha_matched": True,
            "predecessor_import_is_hostile_audited": True,
            "predecessor_independent_reaggregation_was_recorded_before_artifact_expiry": True,
            "all_364_delta_work_items_verified": True,
            "all_80_bundle_receipts_verified": True,
            "shared_context_certificate_sha256": EXPECTED_SHARED_CONTEXT_SHA,
            "source_expiry_changes_no_mathematical_credit": True,
        },
        "tier_scope": "ALL_E20_A0_SIGNATURE_CELLS_WITH_MATERIALIZED_BRANCH_COUNT_LE_114186",
        "next_profile_wall": plan["next_profile_wall"],
        "parent_e20_a0_complete": False,
        "e20_a0_profile_cell_count": 1182,
        "remaining_e20_a0_cells": 1182 - EXPECTED_CUMULATIVE_CELLS,
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
    print(json.dumps({
        "cells": EXPECTED_CUMULATIVE_CELLS,
        "branches": EXPECTED_CUMULATIVE_BRANCHES,
        "delta_nodes": delta_nodes,
        "total_nodes": report["total_search_nodes"],
        "survivors": 0,
        "unknown": 0,
        "bundles": len(bundle_seconds),
        "sha": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
