#!/usr/bin/env python3
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import pathlib

PROFILE_SCHEMA = "STAGE32_D8_MATERIALIZATION_SCHEDULE_PROFILE_V1"
TIER_SCHEMA = "STAGE32_D8_MATERIALIZED_PARENT_TIER_EXHAUSTIVE_V1"
CELL_SCHEMA = "STAGE32_D8_MATERIALIZED_CELL_EXHAUSTIVE_NUMERICAL_V1"
REPAIR_SCHEMA = "STAGE32_TIMEOUT_SHARD_AGGREGATE_V1"
GIANT_SCHEMA = "STAGE32_D8_E10_A30_GIANT_TAIL_AGGREGATE_V1"
OUT_SCHEMA = "STAGE32_D8_E10_A30_FULL_PARENT_NUMERICAL_CENSUS_V1"
PROFILE_SHA = "993d0005f60499b50b03b899153b60f93de757a74f53d942e5a2168830cc5123"
TIER_SHA = "09ebeb9994ce8f4f78a0639a9ed0b71d02d483070ba8dafd201b40e751c651fd"
REPAIR_SHA = "7550900e558a47d07c41164dcb1547901b2849ba53e72f4882b7d15d4ce62384"
CELL_INVENTORY_SHA = "c2e028af43afda9cce1e82139c09ba56be72c087b5d957b40e8bda70e3a96afd"
REPAIR_INDICES = {27, 37}
GIANT_INDICES = {43, 64, 100, 108}


def csha(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def add_survivors(target, source, idx, cid):
    for survivor in source:
        row = dict(survivor)
        row["source_cell_index"] = idx
        row["source_cell_id"] = cid
        target.append(row)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", type=pathlib.Path, required=True)
    ap.add_argument("--profile", type=pathlib.Path, required=True)
    ap.add_argument("--repair", type=pathlib.Path, required=True)
    ap.add_argument("--direct-dir", type=pathlib.Path, required=True)
    ap.add_argument("--giant", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    tier = json.loads(args.tier.read_text())
    prof = json.loads(args.profile.read_text())
    repair = json.loads(args.repair.read_text())
    giant = json.loads(args.giant.read_text())

    assert prof["schema"] == PROFILE_SCHEMA
    assert prof["canonical_sha256_without_this_field"] == PROFILE_SHA
    assert prof["degree"] == 8 and prof["genus"] == 0
    assert prof["exceptional_mass"] == 10 and prof["curve_group_mass"] == 30
    assert prof["signature_cell_count"] == 134
    rows = {int(r["cell_index"]): r for r in prof["cells_sorted_by_branch_count"]}
    assert len(rows) == 134 and set(rows) == set(range(134))

    assert tier["schema"] == TIER_SCHEMA
    assert tier["deterministic_sha256_without_runtime"] == TIER_SHA
    assert tier["parameters"] == {
        "branch_threshold": 4096,
        "curve_group_mass": 30,
        "degree": 8,
        "exceptional_mass": 10,
        "genus": 0,
        "node_limit_per_branch": 1000000,
    }
    assert tier["tier_complete_numerical_enumeration"] is True
    assert tier["unknown_cell_count"] == 0
    assert tier["tier_inventory"]["selected_cell_count"] == 102
    assert tier["parent_inventory"]["signature_cell_count"] == 134
    assert tier["parent_inventory"]["cell_inventory_sha256"] == CELL_INVENTORY_SHA
    tier_idx = set(map(int, tier["tier_inventory"]["selected_cell_indices"]))
    assert tier_idx == {
        i for i, r in rows.items() if int(r["materialized_branch_count"]) <= 4096
    }

    assert repair["schema"] == REPAIR_SCHEMA
    assert repair["canonical_sha256_without_this_field"] == REPAIR_SHA
    assert repair["all_timeout_cells_exactly_partitioned_and_complete"] is True

    assert giant["schema"] == GIANT_SCHEMA
    assert giant["all_giant_cells_exactly_partitioned_and_complete"] is True
    assert {int(c["cell_index"]) for c in giant["cell_summaries"]} == GIANT_INDICES

    tail_idx = set(rows) - tier_idx
    direct_idx = tail_idx - REPAIR_INDICES - GIANT_INDICES
    assert len(tail_idx) == 32
    assert direct_idx == {
        5, 25, 28, 29, 32, 34, 45, 47, 58, 59, 68, 71, 72,
        75, 83, 88, 89, 91, 98, 102, 112, 114, 119, 120, 125, 127,
    }

    cell_summaries = []
    survivors = []
    total_branches = 0

    for c in tier["cells"]:
        idx = int(c["cell_index"])
        assert idx in tier_idx
        assert c["cell_id"] == rows[idx]["cell_id"]
        assert c["complete_numerical_enumeration"] is True
        assert int(c["executed_branch_count"]) == int(c["materialized_branch_count"])
        assert int(c["executed_branch_count"]) == int(rows[idx]["materialized_branch_count"])
        total_branches += int(c["executed_branch_count"])
        cell_summaries.append(
            {
                "cell_index": idx,
                "cell_id": c["cell_id"],
                "branch_count": int(c["executed_branch_count"]),
                "solver_result": c["solver_result"],
                "exact_numerical_survivor_count": int(c["exact_numerical_survivor_count"]),
                "source": "stage32-10-e10-tier4096-run32686185075",
            }
        )
    for s in tier["confirmed_numerical_survivors"]:
        add_survivors(
            survivors,
            [s],
            int(s["source_cell_index"]),
            s["source_cell_id"],
        )

    seen_direct = set()
    for path in sorted(args.direct_dir.rglob("cell.json")):
        d = json.loads(path.read_text())
        if d.get("schema") != CELL_SCHEMA:
            continue
        p = d["parameters"]
        if int(p["exceptional_mass"]) != 10 or int(p["curve_group_mass"]) != 30:
            continue
        idx = int(p["cell_index"])
        assert idx in direct_idx and idx not in seen_direct
        seen_direct.add(idx)
        assert p["degree"] == 8 and p["genus"] == 0
        assert p["cell_id"] == rows[idx]["cell_id"]
        assert d["complete_numerical_enumeration"] is True
        assert d["solver_result"] in ("UNSAT", "SAT_EXHAUSTED")
        assert int(d["executed_branch_count"]) == int(rows[idx]["materialized_branch_count"])
        assert len(d["branches"]) == int(d["executed_branch_count"])
        assert all(
            b["search"]["complete_numerical_enumeration"]
            and not b["search"]["node_budget_exhausted"]
            for b in d["branches"]
        )
        total_branches += int(d["executed_branch_count"])
        cell_summaries.append(
            {
                "cell_index": idx,
                "cell_id": p["cell_id"],
                "branch_count": int(d["executed_branch_count"]),
                "solver_result": d["solver_result"],
                "exact_numerical_survivor_count": int(d["exact_numerical_survivor_count"]),
                "source": "stage32-11-run32689063120",
                "deterministic_sha256_without_runtime": d["deterministic_sha256_without_runtime"],
            }
        )
        add_survivors(survivors, d["numerical_survivors"], idx, p["cell_id"])
    assert seen_direct == direct_idx

    seen_repair = set()
    for rc in repair["cell_summaries"]:
        if int(rc["exceptional_mass"]) != 10 or int(rc["curve_group_mass"]) != 30:
            continue
        idx = int(rc["cell_index"])
        if idx not in REPAIR_INDICES:
            continue
        assert idx not in seen_repair
        seen_repair.add(idx)
        assert rc["branch_partition_complete"] is True
        assert int(rc["unknown_branch_count"]) == 0
        assert rc["cell_id"] == rows[idx]["cell_id"]
        assert int(rc["total_branch_count"]) == int(rows[idx]["materialized_branch_count"])
        total_branches += int(rc["total_branch_count"])
        cell_summaries.append(
            {
                "cell_index": idx,
                "cell_id": rc["cell_id"],
                "branch_count": int(rc["total_branch_count"]),
                "solver_result": rc["solver_result"],
                "exact_numerical_survivor_count": int(rc["exact_numerical_survivor_count"]),
                "source": "stage32-11r-run32694939071",
                "shard_set_sha256": rc["shard_set_sha256"],
            }
        )
        add_survivors(survivors, rc["numerical_survivors"], idx, rc["cell_id"])
    assert seen_repair == REPAIR_INDICES

    seen_giant = set()
    for gc in giant["cell_summaries"]:
        idx = int(gc["cell_index"])
        assert idx in GIANT_INDICES and idx not in seen_giant
        seen_giant.add(idx)
        assert gc["branch_partition_complete"] is True
        assert int(gc["unknown_branch_count"]) == 0
        assert gc["cell_id"] == rows[idx]["cell_id"]
        assert int(gc["total_branch_count"]) == int(rows[idx]["materialized_branch_count"])
        total_branches += int(gc["total_branch_count"])
        cell_summaries.append(
            {
                "cell_index": idx,
                "cell_id": gc["cell_id"],
                "branch_count": int(gc["total_branch_count"]),
                "solver_result": gc["solver_result"],
                "exact_numerical_survivor_count": int(gc["exact_numerical_survivor_count"]),
                "source": "stage32-13-giant-tail",
                "shard_count": int(gc["shard_count"]),
                "shard_set_sha256": gc["shard_set_sha256"],
            }
        )
        add_survivors(survivors, gc["numerical_survivors"], idx, gc["cell_id"])
    assert seen_giant == GIANT_INDICES

    assert len(cell_summaries) == 134
    assert {x["cell_index"] for x in cell_summaries} == set(range(134))
    assert total_branches == int(prof["total_materialized_branch_count"]) == 11205888
    cell_summaries.sort(key=lambda x: x["cell_index"])
    survivors.sort(key=lambda x: tuple(x["basis_coordinates"]))
    keys = [tuple(s["basis_coordinates"]) for s in survivors]
    assert len(keys) == len(set(keys))
    assert all(
        s["degree"] == 8 and s["exceptional_mass"] == 10 and s["curve_group_mass"] == 30
        for s in survivors
    )
    squares = collections.Counter(int(s["self_intersection"]) for s in survivors)

    report = {
        "schema": OUT_SCHEMA,
        "source_locks": {
            "profile_sha": PROFILE_SHA,
            "tier4096_sha": TIER_SHA,
            "timeout_repair_sha": REPAIR_SHA,
            "giant_tail_sha": giant["canonical_sha256_without_this_field"],
            "stage32_10_run": 32686185075,
            "stage32_11_run": 32689063120,
            "stage32_11r_run": 32694939071,
        },
        "parameters": {
            "degree": 8,
            "genus": 0,
            "exceptional_mass": 10,
            "curve_group_mass": 30,
            "node_limit_per_branch": 1000000,
        },
        "parent_inventory": {
            "signature_cell_count": 134,
            "total_materialized_branch_count": total_branches,
            "cell_inventory_sha256": CELL_INVENTORY_SHA,
        },
        "cell_summaries": cell_summaries,
        "exact_numerical_survivor_count": len(survivors),
        "self_intersection_distribution": {
            str(k): v for k, v in sorted(squares.items())
        },
        "numerical_survivors": survivors,
        "e10_a30_parent_complete": True,
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
                "cells": 134,
                "branches": total_branches,
                "survivors": len(survivors),
                "squares": report["self_intersection_distribution"],
                "sha": report["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
