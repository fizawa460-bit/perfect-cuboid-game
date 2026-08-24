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
CERT_SCHEMA = "STAGE32_D8_E20_A0_MATERIALIZED_CELL_SHARD_COMPACT_CERT_V1"
OUT_SCHEMA = "STAGE32_D8_E20_A0_EXACT_TIER_LE16384_V1"
EXPECTED_PROFILE_SHA = "e2b1b47fea0076cde9d93399b04f0bf087175fafcc5cb384534d53fa1fee67c5"
EXPECTED_PREV_SHA = "88d3d7d12217626e8af80e3d6c3886b47a6416b498500de94bc1032c25407cb5"


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
    assert int(plan["target_threshold"]) == 16384
    assert int(plan["delta_cell_count"]) == 53
    assert int(plan["delta_branch_count"]) == 606768
    assert int(plan["cumulative_cell_count"]) == 69
    assert int(plan["cumulative_branch_count"]) == 655558

    target_rows = [r for r in profile["cells_sorted_by_branch_count"] if int(r["materialized_branch_count"]) <= 16384]
    delta_rows = [r for r in target_rows if int(r["materialized_branch_count"]) > 4096]
    delta = {(int(r["cell_index"]), str(r["cell_id"])): int(r["materialized_branch_count"]) for r in delta_rows}
    planned = {(int(c["cell_index"]), str(c["cell_id"])): int(c["total_branches"]) for c in plan["selected_delta_cells"]}
    assert delta == planned and len(delta) == 53

    expected = {(idx, shard): (cid, branches) for (idx, cid), branches in delta.items() for shard in range(2)}
    certs: dict[tuple[int, int], dict[str, Any]] = {}
    for path in sorted(args.input_dir.rglob("compact.json")):
        row = json.loads(path.read_text())
        assert row["schema"] == CERT_SCHEMA
        unsigned = dict(row)
        claimed = unsigned.pop("canonical_sha256_without_this_field")
        assert csha(unsigned) == claimed
        p = row["parameters"]
        key = (int(p["cell_index"]), int(p["shard_index"]))
        assert key in expected and key not in certs
        certs[key] = row
    assert set(certs) == set(expected), (len(certs), len(expected))

    delta_summaries: list[dict[str, Any]] = []
    delta_survivors: list[dict[str, Any]] = []
    delta_nodes = 0
    for (idx, cid), branches in sorted(delta.items()):
        survivors: list[dict[str, Any]] = []
        cell_nodes = executed = 0
        compact_shas: list[str] = []
        raw_shas: list[str] = []
        stream_shas: list[str] = []
        for shard in range(2):
            row = certs[(idx, shard)]
            p = row["parameters"]
            assert int(p["degree"]) == 8 and int(p["genus"]) == 0
            assert int(p["exceptional_mass"]) == 20 and int(p["curve_group_mass"]) == 0
            assert int(p["cell_index"]) == idx and str(p["cell_id"]) == cid
            assert int(p["shard_index"]) == shard and int(p["shard_count"]) == 2
            assert int(row["parent_cell_total_branch_count"]) == branches
            assert row["all_branch_indices_exact_mod_partition"] is True
            assert row["all_branches_complete"] is True
            assert int(row["unknown_branch_count"]) == 0
            assert row["compaction_is_post_verification_only"] is True
            assert row["raw_branch_rows_persisted"] is False
            assert row["theorem_credit"] is False and row["receiver_credit"] is False
            want = expected_mod_count(branches, 2, shard)
            assert int(row["executed_shard_branch_count"]) == want
            assert int(row["first_branch_index"]) == shard
            assert int(row["last_branch_index"]) == shard + (want - 1) * 2
            executed += want
            cell_nodes += int(row["total_search_nodes"])
            survivors.extend(row["numerical_survivors"])
            compact_shas.append(row["canonical_sha256_without_this_field"])
            raw_shas.append(row["source_raw_deterministic_sha256"])
            stream_shas.append(row["branch_exact_evidence_stream_sha256"])
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
            "shard_count": 2,
            "branch_partition_complete": True,
            "unknown_branch_count": 0,
            "solver_result": "SAT_EXHAUSTED" if survivors else "UNSAT",
            "exact_numerical_survivor_count": len(survivors),
            "search_nodes": cell_nodes,
            "compact_certificate_shas": compact_shas,
            "source_raw_deterministic_shas": raw_shas,
            "branch_evidence_stream_shas": stream_shas,
            "numerical_survivors": survivors,
        })

    prev_summaries = list(prev["cell_summaries"])
    prev_survivors = list(prev["numerical_survivors"])
    all_summaries = prev_summaries + delta_summaries
    all_summaries.sort(key=lambda c: int(c["cell_index"]))
    all_survivors = prev_survivors + delta_survivors
    all_survivors.sort(key=lambda r: tuple(r["basis_coordinates"]))
    keys = [tuple(r["basis_coordinates"]) for r in all_survivors]
    assert len(keys) == len(set(keys))

    target_keys = {(int(r["cell_index"]), str(r["cell_id"])) for r in target_rows}
    summary_keys = {(int(c["cell_index"]), str(c["cell_id"])) for c in all_summaries}
    assert summary_keys == target_keys and len(all_summaries) == 69
    total_branches = sum(int(c["total_branch_count"]) for c in all_summaries)
    assert total_branches == 655558

    report = {
        "schema": OUT_SCHEMA,
        "evidence_storage_mode": "POST_VERIFICATION_COMPACT_CERTIFICATES_ONLY",
        "profile_sha256": EXPECTED_PROFILE_SHA,
        "predecessor_sha256": EXPECTED_PREV_SHA,
        "delta_plan_sha256": plan_claimed,
        "parameters": {"degree": 8, "genus": 0, "exceptional_mass": 20, "curve_group_mass": 0},
        "chosen_cumulative_branch_threshold": 16384,
        "predecessor_cell_count": 16,
        "delta_cell_count": 53,
        "selected_cell_count": 69,
        "predecessor_materialized_branches": 48790,
        "delta_materialized_branches": 606768,
        "selected_total_materialized_branches": total_branches,
        "selected_cells_exactly_complete": True,
        "unknown_branch_count": 0,
        "predecessor_search_nodes": int(prev["total_search_nodes"]),
        "delta_search_nodes": delta_nodes,
        "total_search_nodes": int(prev["total_search_nodes"]) + delta_nodes,
        "exact_numerical_survivor_count": len(all_survivors),
        "numerical_survivors": all_survivors,
        "cell_summaries": all_summaries,
        "tier_scope": "ALL_E20_A0_SIGNATURE_CELLS_WITH_MATERIALIZED_BRANCH_COUNT_LE_16384",
        "parent_e20_a0_complete": False,
        "next_profile_wall": {"threshold": 65536, "cell_count": 301, "materialized_branches": 6834114},
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
        "cells": 69,
        "branches": total_branches,
        "delta_nodes": delta_nodes,
        "survivors": len(all_survivors),
        "next_wall_cells": 301,
        "next_wall_branches": 6834114,
        "sha": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
