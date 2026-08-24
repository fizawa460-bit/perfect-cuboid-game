#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
from typing import Any

PROFILE_SCHEMA = "STAGE32_D8_MATERIALIZATION_SCHEDULE_PROFILE_V1"
PLAN_SCHEMA = "STAGE32_D8_E20_A0_STORAGE_SAFE_TIER_PLAN_V1"
CERT_SCHEMA = "STAGE32_D8_E20_A0_MATERIALIZED_CELL_SHARD_COMPACT_CERT_V1"
OUT_SCHEMA = "STAGE32_D8_E20_A0_STORAGE_SAFE_EXACT_TIER_V1"


def csha(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def expected_mod_count(total: int, shard_count: int, shard_index: int) -> int:
    return total // shard_count + (1 if shard_index < total % shard_count else 0)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", type=pathlib.Path, required=True)
    ap.add_argument("--plan", type=pathlib.Path, required=True)
    ap.add_argument("--input-dir", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    profile = json.loads(args.profile.read_text())
    plan = json.loads(args.plan.read_text())
    assert profile["schema"] == PROFILE_SCHEMA
    assert plan["schema"] == PLAN_SCHEMA
    assert plan["safe_to_fanout"] is True
    assert int(profile["exceptional_mass"]) == 20 and int(profile["curve_group_mass"]) == 0
    assert int(profile["degree"]) == 8 and int(profile["genus"]) == 0
    assert plan["profile_sha256"] == profile["canonical_sha256_without_this_field"]
    assert plan["selection_rule"] == "ALL_SIGNATURE_CELLS_WITH_MATERIALIZED_BRANCH_COUNT_LE_CHOSEN_THRESHOLD"

    threshold = int(plan["chosen_cumulative_branch_threshold"])
    expected_rows = [
        r for r in profile["cells_sorted_by_branch_count"]
        if int(r["materialized_branch_count"]) <= threshold
    ]
    expected_cells_from_profile = {
        (int(r["cell_index"]), str(r["cell_id"])): int(r["materialized_branch_count"])
        for r in expected_rows
    }
    planned_cells = {
        (int(c["cell_index"]), str(c["cell_id"])): int(c["total_branches"])
        for c in plan["selected_cells"]
    }
    assert planned_cells == expected_cells_from_profile
    assert len(planned_cells) == int(plan["selected_cell_count"])
    assert sum(planned_cells.values()) == int(plan["selected_total_materialized_branches"])

    expected = {
        (idx, shard): (cid, branches)
        for (idx, cid), branches in planned_cells.items()
        for shard in range(2)
    }
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

    cell_summaries: list[dict[str, Any]] = []
    all_survivors: list[dict[str, Any]] = []
    total_nodes = total_branches = 0

    for (idx, cid), parent_branches in sorted(planned_cells.items()):
        survivors: list[dict[str, Any]] = []
        compact_shas: list[str] = []
        raw_shas: list[str] = []
        stream_shas: list[str] = []
        cell_nodes = executed_total = 0
        for shard_index in range(2):
            row = certs[(idx, shard_index)]
            p = row["parameters"]
            assert int(p["degree"]) == 8 and int(p["genus"]) == 0
            assert int(p["exceptional_mass"]) == 20 and int(p["curve_group_mass"]) == 0
            assert int(p["cell_index"]) == idx and str(p["cell_id"]) == cid
            assert int(p["shard_index"]) == shard_index and int(p["shard_count"]) == 2
            assert int(row["parent_cell_total_branch_count"]) == parent_branches
            assert row["all_branch_indices_exact_mod_partition"] is True
            assert row["all_branches_complete"] is True
            assert int(row["unknown_branch_count"]) == 0
            assert row["compaction_is_post_verification_only"] is True
            assert row["raw_branch_rows_persisted"] is False
            assert row["theorem_credit"] is False and row["receiver_credit"] is False
            assert row["FULL_D8_G0_ROW_COMPLETE"] is False
            assert row["FULL_D176_D192_NUMERICAL_ORBIT_CENSUS"] is False
            assert row["R29_LG2"] == "NOT_DISCHARGED"
            assert row["G10_LOWGENUS_PICARD"] == "AMBER"

            want = expected_mod_count(parent_branches, 2, shard_index)
            assert int(row["executed_shard_branch_count"]) == want
            assert int(row["first_branch_index"]) == shard_index
            assert int(row["last_branch_index"]) == shard_index + (want - 1) * 2
            assert int(row["last_branch_index"]) < parent_branches
            executed_total += want
            cell_nodes += int(row["total_search_nodes"])
            survivors.extend(row["numerical_survivors"])
            compact_shas.append(row["canonical_sha256_without_this_field"])
            raw_shas.append(row["source_raw_deterministic_sha256"])
            stream_shas.append(row["branch_exact_evidence_stream_sha256"])

        assert executed_total == parent_branches
        survivors.sort(key=lambda r: tuple(r["basis_coordinates"]))
        keys = [tuple(r["basis_coordinates"]) for r in survivors]
        assert len(keys) == len(set(keys))
        all_survivors.extend(survivors)
        cell_summaries.append({
            "cell_index": idx,
            "cell_id": cid,
            "total_branch_count": parent_branches,
            "shard_count": 2,
            "branch_partition_complete": True,
            "unknown_branch_count": 0,
            "solver_result": "SAT_EXHAUSTED" if survivors else "UNSAT",
            "exact_numerical_survivor_count": len(survivors),
            "search_nodes": cell_nodes,
            "compact_certificate_shas": compact_shas,
            "source_raw_deterministic_shas": raw_shas,
            "branch_evidence_stream_shas": stream_shas,
            "compact_certificate_set_sha256": csha(compact_shas),
            "source_raw_set_sha256": csha(raw_shas),
            "branch_evidence_stream_set_sha256": csha(stream_shas),
            "numerical_survivors": survivors,
        })
        total_nodes += cell_nodes
        total_branches += parent_branches

    all_survivors.sort(key=lambda r: tuple(r["basis_coordinates"]))
    all_keys = [tuple(r["basis_coordinates"]) for r in all_survivors]
    assert len(all_keys) == len(set(all_keys))
    assert total_branches == int(plan["selected_total_materialized_branches"])

    report = {
        "schema": OUT_SCHEMA,
        "evidence_storage_mode": "POST_VERIFICATION_COMPACT_CERTIFICATES_ONLY",
        "profile_sha256": profile["canonical_sha256_without_this_field"],
        "plan_sha256": plan["canonical_sha256_without_this_field"],
        "parameters": {"degree": 8, "genus": 0, "exceptional_mass": 20, "curve_group_mass": 0},
        "chosen_cumulative_branch_threshold": threshold,
        "selected_cell_count": len(cell_summaries),
        "selected_total_materialized_branches": total_branches,
        "selected_cells_exactly_complete": True,
        "unknown_branch_count": 0,
        "total_search_nodes": total_nodes,
        "exact_numerical_survivor_count": len(all_survivors),
        "numerical_survivors": all_survivors,
        "cell_summaries": cell_summaries,
        "tier_scope": "ALL_E20_A0_SIGNATURE_CELLS_AT_OR_BELOW_CHOSEN_MATERIALIZED_BRANCH_THRESHOLD_ONLY",
        "parent_e20_a0_complete": len(cell_summaries) == int(profile["signature_cell_count"]),
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
        "threshold": threshold,
        "cells": len(cell_summaries),
        "branches": total_branches,
        "nodes": total_nodes,
        "survivors": len(all_survivors),
        "parent_complete": report["parent_e20_a0_complete"],
        "sha": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
