#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
from typing import Any

SCHEMA = "STAGE32_TIMEOUT_SHARD_AGGREGATE_V1"
SHARD_SCHEMA = "STAGE32_D8_MATERIALIZED_CELL_BRANCH_SHARD_V1"
SHARD_COUNT = 4
EXPECTED = {
    (8, 36, 39, "ceb88a2b425fb743669aa33e"): 529480,
    (10, 30, 27, "2719e0ba39bfa79944906bf5"): 639840,
    (10, 30, 37, "3af4cf3d535a93607ef8b5bb"): 605120,
}


def canonical_sha256(value: Any) -> str:
    payload = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    return hashlib.sha256(payload).hexdigest()


def expected_mod_count(total: int, shard_count: int, shard_index: int) -> int:
    return total // shard_count + (1 if shard_index < total % shard_count else 0)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    paths = sorted(args.input_dir.rglob("*.json"))
    reports = []
    for path in paths:
        row = json.loads(path.read_text())
        if row.get("schema") == SHARD_SCHEMA:
            reports.append(row)
    assert len(reports) == len(EXPECTED) * SHARD_COUNT, len(reports)

    grouped: dict[tuple[int, int, int, str], list[dict[str, Any]]] = {}
    for row in reports:
        p = row["parameters"]
        key = (
            int(p["exceptional_mass"]),
            int(p["curve_group_mass"]),
            int(p["cell_index"]),
            str(p["cell_id"]),
        )
        assert key in EXPECTED, key
        grouped.setdefault(key, []).append(row)

    assert set(grouped) == set(EXPECTED)
    cell_summaries = []
    total_nodes = 0
    total_survivors = 0

    for key, total_branches in EXPECTED.items():
        rows = grouped[key]
        rows.sort(key=lambda r: int(r["parameters"]["shard_index"]))
        assert [int(r["parameters"]["shard_index"]) for r in rows] == list(
            range(SHARD_COUNT)
        )
        assert all(int(r["parameters"]["shard_count"]) == SHARD_COUNT for r in rows)
        assert all(
            int(r["materialization"]["total_parent_cell_branch_count"])
            == total_branches
            for r in rows
        )
        assert all(r["complete_shard_numerical_enumeration"] is True for r in rows)
        assert all(r["theorem_credit"] is False for r in rows)
        assert all(r["receiver_credit"] is False for r in rows)
        assert all(r["FULL_D8_G0_ROW_COMPLETE"] is False for r in rows)
        assert all(r["R29_LG2"] == "NOT_DISCHARGED" for r in rows)
        assert all(r["G10_LOWGENUS_PICARD"] == "AMBER" for r in rows)

        seen_branch_indices: set[int] = set()
        survivors = []
        cell_nodes = 0
        for row in rows:
            shard_index = int(row["parameters"]["shard_index"])
            expected_count = expected_mod_count(
                total_branches, SHARD_COUNT, shard_index
            )
            branch_rows = row["branches"]
            assert len(branch_rows) == expected_count
            assert (
                int(row["materialization"]["expected_shard_branch_count"])
                == expected_count
            )
            assert (
                int(row["materialization"]["executed_shard_branch_count"])
                == expected_count
            )
            for branch in branch_rows:
                idx = int(branch["branch_index"])
                assert 0 <= idx < total_branches
                assert idx % SHARD_COUNT == shard_index
                assert idx not in seen_branch_indices
                seen_branch_indices.add(idx)
                search = branch["search"]
                assert search["complete_numerical_enumeration"] is True
                assert search["node_budget_exhausted"] is False
                cell_nodes += int(search["enumeration_node_count"])
            survivors.extend(row["numerical_survivors"])

        assert len(seen_branch_indices) == total_branches
        assert seen_branch_indices == set(range(total_branches))

        survivors.sort(key=lambda r: tuple(r["basis_coordinates"]))
        survivor_keys = [tuple(r["basis_coordinates"]) for r in survivors]
        assert len(survivor_keys) == len(set(survivor_keys))
        result = "SAT_EXHAUSTED" if survivors else "UNSAT"

        shard_shas = [r["deterministic_sha256_without_runtime"] for r in rows]
        cell_summary = {
            "exceptional_mass": key[0],
            "curve_group_mass": key[1],
            "cell_index": key[2],
            "cell_id": key[3],
            "total_branch_count": total_branches,
            "shard_count": SHARD_COUNT,
            "branch_partition_complete": True,
            "unknown_branch_count": 0,
            "solver_result": result,
            "exact_numerical_survivor_count": len(survivors),
            "search_nodes": cell_nodes,
            "shard_deterministic_shas": shard_shas,
            "shard_set_sha256": canonical_sha256(shard_shas),
            "numerical_survivors": survivors,
        }
        cell_summaries.append(cell_summary)
        total_nodes += cell_nodes
        total_survivors += len(survivors)

    report = {
        "schema": SCHEMA,
        "source_timeout_run": 32689063120,
        "timeout_cells": 3,
        "shard_count_per_cell": SHARD_COUNT,
        "total_repaired_branch_count": sum(EXPECTED.values()),
        "cell_summaries": cell_summaries,
        "all_timeout_cells_exactly_partitioned_and_complete": True,
        "total_search_nodes": total_nodes,
        "total_numerical_survivors_in_repaired_cells": total_survivors,
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
    report["canonical_sha256_without_this_field"] = canonical_sha256(report)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "cells": len(cell_summaries),
                "branches": report["total_repaired_branch_count"],
                "nodes": total_nodes,
                "survivors": total_survivors,
                "complete": True,
                "sha": report["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
