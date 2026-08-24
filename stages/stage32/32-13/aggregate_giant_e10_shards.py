#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
from typing import Any

SHARD_SCHEMA = "STAGE32_D8_MATERIALIZED_CELL_BRANCH_SHARD_V1"
PLAN_SCHEMA = "STAGE32_E10_A30_GIANT_TAIL_SHARD_PLAN_V1"
OUT_SCHEMA = "STAGE32_D8_E10_A30_GIANT_TAIL_AGGREGATE_V1"


def csha(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def expected_mod_count(total: int, shard_count: int, shard_index: int) -> int:
    return total // shard_count + (1 if shard_index < total % shard_count else 0)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", type=pathlib.Path, required=True)
    ap.add_argument("--input-dir", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    plan = json.loads(args.plan.read_text())
    assert plan["schema"] == PLAN_SCHEMA
    expected_files = {
        f"cell-{int(cell['cell_index'])}-s{s}.json"
        for cell in plan["cells"]
        for s in range(int(cell["shard_count"]))
    }
    actual_files = {p.name for p in args.input_dir.glob("cell-*-s*.json")}
    assert actual_files == expected_files, (len(actual_files), len(expected_files))

    cell_summaries = []
    total_nodes = total_survivors = total_branches = 0

    for cell in sorted(plan["cells"], key=lambda c: int(c["cell_index"])):
        idx = int(cell["cell_index"])
        cid = str(cell["cell_id"])
        parent_branches = int(cell["total_branches"])
        shard_count = int(cell["shard_count"])
        survivors = []
        shard_shas = []
        cell_nodes = 0

        for shard_index in range(shard_count):
            path = args.input_dir / f"cell-{idx}-s{shard_index}.json"
            row = json.loads(path.read_text())
            assert row["schema"] == SHARD_SCHEMA
            p = row["parameters"]
            assert int(p["exceptional_mass"]) == int(plan["exceptional_mass"]) == 10
            assert int(p["curve_group_mass"]) == int(plan["curve_group_mass"]) == 30
            assert int(p["cell_index"]) == idx and str(p["cell_id"]) == cid
            assert int(p["shard_index"]) == shard_index
            assert int(p["shard_count"]) == shard_count
            assert int(row["materialization"]["total_parent_cell_branch_count"]) == parent_branches
            assert row["complete_shard_numerical_enumeration"] is True
            assert row["theorem_credit"] is False and row["receiver_credit"] is False
            assert row["FULL_D8_G0_ROW_COMPLETE"] is False
            assert row["R29_LG2"] == "NOT_DISCHARGED"
            assert row["G10_LOWGENUS_PICARD"] == "AMBER"

            want = expected_mod_count(parent_branches, shard_count, shard_index)
            branch_rows = row["branches"]
            assert len(branch_rows) == want
            assert int(row["materialization"]["expected_shard_branch_count"]) == want
            assert int(row["materialization"]["executed_shard_branch_count"]) == want

            expected_index = shard_index
            for branch in branch_rows:
                branch_index = int(branch["branch_index"])
                assert branch_index == expected_index
                expected_index += shard_count
                search = branch["search"]
                assert search["complete_numerical_enumeration"] is True
                assert search["node_budget_exhausted"] is False
                cell_nodes += int(search["enumeration_node_count"])
            assert expected_index >= parent_branches
            survivors.extend(row["numerical_survivors"])
            shard_shas.append(row["deterministic_sha256_without_runtime"])
            del row

        survivors.sort(key=lambda r: tuple(r["basis_coordinates"]))
        keys = [tuple(r["basis_coordinates"]) for r in survivors]
        assert len(keys) == len(set(keys))
        result = "SAT_EXHAUSTED" if survivors else "UNSAT"
        cell_summaries.append(
            {
                "exceptional_mass": 10,
                "curve_group_mass": 30,
                "cell_index": idx,
                "cell_id": cid,
                "total_branch_count": parent_branches,
                "shard_count": shard_count,
                "branch_partition_complete": True,
                "unknown_branch_count": 0,
                "solver_result": result,
                "exact_numerical_survivor_count": len(survivors),
                "search_nodes": cell_nodes,
                "shard_deterministic_shas": shard_shas,
                "shard_set_sha256": csha(shard_shas),
                "numerical_survivors": survivors,
            }
        )
        total_nodes += cell_nodes
        total_survivors += len(survivors)
        total_branches += parent_branches

    assert total_branches == sum(int(c["total_branches"]) for c in plan["cells"])
    report = {
        "schema": OUT_SCHEMA,
        "plan": plan,
        "giant_cell_count": len(cell_summaries),
        "total_giant_branch_count": total_branches,
        "cell_summaries": cell_summaries,
        "all_giant_cells_exactly_partitioned_and_complete": True,
        "total_search_nodes": total_nodes,
        "total_numerical_survivors_in_giant_cells": total_survivors,
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
                "cells": len(cell_summaries),
                "branches": total_branches,
                "nodes": total_nodes,
                "survivors": total_survivors,
                "sha": report["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
