#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
from typing import Any

CERT_SCHEMA = "STAGE32_D8_MATERIALIZED_CELL_BRANCH_SHARD_COMPACT_CERT_V1"
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
    expected = {
        (int(c["cell_index"]), s): c
        for c in plan["cells"]
        for s in range(int(c["shard_count"]))
    }

    certs: dict[tuple[int, int], dict[str, Any]] = {}
    for path in sorted(args.input_dir.rglob("compact.json")):
        row = json.loads(path.read_text())
        assert row["schema"] == CERT_SCHEMA
        p = row["parameters"]
        key = (int(p["cell_index"]), int(p["shard_index"]))
        assert key in expected and key not in certs
        certs[key] = row
    assert set(certs) == set(expected), (len(certs), len(expected))

    cell_summaries = []
    total_nodes = total_survivors = total_branches = 0

    for cell in sorted(plan["cells"], key=lambda c: int(c["cell_index"])):
        idx = int(cell["cell_index"])
        cid = str(cell["cell_id"])
        parent_branches = int(cell["total_branches"])
        shard_count = int(cell["shard_count"])
        survivors: list[dict[str, Any]] = []
        compact_shas: list[str] = []
        raw_shas: list[str] = []
        stream_shas: list[str] = []
        cell_nodes = 0
        executed_total = 0

        for shard_index in range(shard_count):
            row = certs[(idx, shard_index)]
            p = row["parameters"]
            assert int(p["exceptional_mass"]) == int(plan["exceptional_mass"]) == 10
            assert int(p["curve_group_mass"]) == int(plan["curve_group_mass"]) == 30
            assert int(p["cell_index"]) == idx and str(p["cell_id"]) == cid
            assert int(p["shard_index"]) == shard_index
            assert int(p["shard_count"]) == shard_count
            assert row["parent_cell_total_branch_count"] == parent_branches
            assert row["all_branch_indices_exact_mod_partition"] is True
            assert row["all_branches_complete"] is True
            assert int(row["unknown_branch_count"]) == 0
            assert row["compaction_is_post_verification_only"] is True
            assert row["raw_branch_rows_persisted"] is False
            assert row["theorem_credit"] is False and row["receiver_credit"] is False
            assert row["R29_LG2"] == "NOT_DISCHARGED"
            assert row["G10_LOWGENUS_PICARD"] == "AMBER"

            want = expected_mod_count(parent_branches, shard_count, shard_index)
            assert int(row["executed_shard_branch_count"]) == want
            assert int(row["first_branch_index"]) == shard_index
            assert int(row["last_branch_index"]) == shard_index + (want - 1) * shard_count
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
        result = "SAT_EXHAUSTED" if survivors else "UNSAT"
        cell_summaries.append({
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
            "compact_certificate_shas": compact_shas,
            "source_raw_deterministic_shas": raw_shas,
            "branch_evidence_stream_shas": stream_shas,
            "compact_certificate_set_sha256": csha(compact_shas),
            "source_raw_set_sha256": csha(raw_shas),
            "branch_evidence_stream_set_sha256": csha(stream_shas),
            "numerical_survivors": survivors,
        })
        total_nodes += cell_nodes
        total_survivors += len(survivors)
        total_branches += parent_branches

    assert total_branches == sum(int(c["total_branches"]) for c in plan["cells"])
    report = {
        "schema": OUT_SCHEMA,
        "evidence_storage_mode": "POST_VERIFICATION_COMPACT_CERTIFICATES_ONLY",
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
    print(json.dumps({
        "cells": len(cell_summaries),
        "branches": total_branches,
        "nodes": total_nodes,
        "survivors": total_survivors,
        "sha": report["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
