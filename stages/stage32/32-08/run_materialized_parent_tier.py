#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import pathlib
import sys
import time
from typing import Any

HERE = pathlib.Path(__file__).resolve().parent
S32 = HERE.parent
S32_05 = S32 / "32-05"
S32_07 = S32 / "32-07"
sys.path.insert(0, str(S32_05))


def load_module(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


pilot = load_module("stage32_07_parent_tier", S32_07 / "run_d8_bounded_signature_cells.py")
v1 = load_module("stage32_08_materialized_v1_parent_tier", HERE / "run_materialized_signature_cell.py")
cached = load_module("stage32_08_cached_parent_tier", HERE / "run_materialized_signature_cell_cached.py")
exhaustive = load_module("stage32_08_exhaustive_parent_tier", HERE / "run_materialized_cell_exhaustive.py")
coset = load_module("stage32_08_coset_parent_tier", HERE / "run_signature_cell_affine_coset.py")
from cap_certificate import load_and_verify

SCHEMA = "STAGE32_D8_MATERIALIZED_PARENT_TIER_EXHAUSTIVE_V1"
ALGORITHM_ID = "D8_PARENT_LOW_BRANCH_TIER_SHARED_QTAIL12_EXHAUSTIVE_V1"
EXPECTED_CAP_SHA = "75224aee543dcd4a56e814503765d1e1e69514b237fb900688243546ea6b4d03"


def cell_branch_cost(cell: dict[str, Any], qhead_counts: dict[int, int]) -> int:
    t = int(cell["aggregate"][3])
    return (
        int(cell["left_assignment_count"])
        * int(cell["right_assignment_count"])
        * int(qhead_counts[t])
    )


def materialize_cell(
    quotient: dict[str, Any],
    aggregate: dict[str, Any],
    cell: dict[str, Any],
) -> tuple[list[tuple[int, ...]], list[tuple[int, int, int, int]]]:
    left_groups, right_groups = pilot.base.split_groups(aggregate["types"])
    left = v1.materialize_side(
        quotient["K"],
        left_groups,
        tuple(map(int, cell["left_counts"])),
        int(cell["left_signature_hex"], 16),
    )
    right = v1.materialize_side(
        quotient["K"],
        right_groups,
        tuple(map(int, cell["right_counts"])),
        int(cell["right_signature_hex"], 16),
    )
    assert len(left) == int(cell["left_assignment_count"])
    assert len(right) == int(cell["right_assignment_count"])
    exceptional_vectors = sorted(
        {
            tuple(lrow[i] + rrow[i] for i in range(48))
            for lrow in left
            for rrow in right
        }
    )
    assert len(exceptional_vectors) == len(left) * len(right)
    qheads = v1.qhead_assignments(int(cell["aggregate"][3]))
    assert qheads
    return exceptional_vectors, qheads


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--exceptional-mass", type=int, required=True)
    ap.add_argument("--curve-group-mass", type=int, required=True)
    ap.add_argument("--branch-threshold", type=int, required=True)
    ap.add_argument("--node-limit-per-branch", type=int, default=1000000)
    args = ap.parse_args()

    started = time.perf_counter()
    core, _, cap_summary = load_and_verify(args.core, args.cap_certificate)
    assert cap_summary["certificate_canonical_sha256"] == EXPECTED_CAP_SHA
    transform = pilot.base.build_transform(core)
    quotient = pilot.base.quotient_data(transform["inv"])
    aggregate = pilot.base.aggregate_structure(transform["pair"], transform["h"])
    cells, inventory = pilot.build_signature_cells(
        quotient["K"],
        aggregate["types"],
        args.exceptional_mass,
        args.curve_group_mass,
    )
    qhead_counts = {
        int(k): int(v)
        for k, v in inventory["qhead_assignment_count_by_total"].items()
    }

    selected = [
        (index, cell, cell_branch_cost(cell, qhead_counts))
        for index, cell in enumerate(cells)
        if cell_branch_cost(cell, qhead_counts) <= args.branch_threshold
    ]
    selected.sort(key=lambda row: (row[2], row[1]["cell_id"]))
    assert selected

    common = cached.prepare_common(core)
    cell_rows: list[dict[str, Any]] = []
    all_survivors: list[dict[str, Any]] = []
    complete_cell_count = 0
    exact_unsat_cell_count = 0
    exact_sat_cell_count = 0
    unknown_cell_count = 0

    for cell_index, cell, expected_branch_count in selected:
        exceptional_vectors, qheads = materialize_cell(quotient, aggregate, cell)
        total_branch_count = len(exceptional_vectors) * len(qheads)
        assert total_branch_count == expected_branch_count

        branch_rows: list[dict[str, Any]] = []
        cell_survivors: list[dict[str, Any]] = []
        cell_unknown = False
        for branch_index, (exceptional, qhead) in enumerate(
            itertools.product(exceptional_vectors, qheads)
        ):
            rhs = cached.branch_rhs(
                exceptional,
                qhead,
                args.exceptional_mass,
                args.curve_group_mass,
            )
            base, base_cert = cached.branch_base(common, rhs)
            search = exhaustive.search_exhaustive(
                common,
                core,
                quotient["K"],
                aggregate["types"],
                base,
                cell,
                args.exceptional_mass,
                args.curve_group_mass,
                0,
                args.node_limit_per_branch,
            )
            branch_rows.append(
                {
                    "branch_index": branch_index,
                    "exceptional_coordinates_sha256": coset.canonical_sha256(
                        list(exceptional)
                    ),
                    "qhead_coordinates": list(qhead),
                    "base_certificate": base_cert,
                    "search": search,
                }
            )
            cell_survivors.extend(search["survivors"])
            if not search["complete_numerical_enumeration"]:
                cell_unknown = True

        cell_survivors.sort(key=lambda row: tuple(row["basis_coordinates"]))
        keys = [tuple(row["basis_coordinates"]) for row in cell_survivors]
        assert len(keys) == len(set(keys))
        cell_complete = not cell_unknown and len(branch_rows) == total_branch_count
        if cell_complete:
            complete_cell_count += 1
            if cell_survivors:
                cell_result = "SAT_EXHAUSTED"
                exact_sat_cell_count += 1
            else:
                cell_result = "UNSAT"
                exact_unsat_cell_count += 1
        else:
            cell_result = "UNKNOWN_NODE_BUDGET"
            unknown_cell_count += 1

        for survivor in cell_survivors:
            all_survivors.append(
                {
                    **survivor,
                    "source_cell_index": cell_index,
                    "source_cell_id": cell["cell_id"],
                }
            )
        cell_rows.append(
            {
                "cell_index": cell_index,
                "cell_id": cell["cell_id"],
                "aggregate": cell["aggregate"],
                "left_counts": cell["left_counts"],
                "right_counts": cell["right_counts"],
                "materialized_branch_count": total_branch_count,
                "executed_branch_count": len(branch_rows),
                "complete_numerical_enumeration": cell_complete,
                "solver_result": cell_result,
                "exact_numerical_survivor_count": len(cell_survivors),
                "branch_rows": branch_rows,
            }
        )

    all_survivors.sort(key=lambda row: tuple(row["basis_coordinates"]))
    all_keys = [tuple(row["basis_coordinates"]) for row in all_survivors]
    assert len(all_keys) == len(set(all_keys))

    tier_complete = complete_cell_count == len(selected)
    report = {
        "schema": SCHEMA,
        "algorithm_id": ALGORITHM_ID,
        "parameters": {
            "degree": pilot.DEGREE,
            "genus": 0,
            "exceptional_mass": args.exceptional_mass,
            "curve_group_mass": args.curve_group_mass,
            "branch_threshold": args.branch_threshold,
            "node_limit_per_branch": args.node_limit_per_branch,
        },
        "parent_inventory": {
            "signature_cell_count": len(cells),
            "cell_inventory_sha256": inventory["cell_inventory_sha256"],
            "exceptional_assignment_count_after_qtail_quotient": inventory[
                "exceptional_assignment_count_after_qtail_quotient"
            ],
        },
        "tier_inventory": {
            "selected_cell_count": len(selected),
            "scheduled_materialized_branch_count": sum(row[2] for row in selected),
            "selected_cell_ids": [row[1]["cell_id"] for row in selected],
            "selected_cell_indices": [row[0] for row in selected],
        },
        "shared_context": common["certificate"],
        "shared_context_preparation_seconds": common["preparation_seconds"],
        "cells": cell_rows,
        "complete_cell_count": complete_cell_count,
        "exact_unsat_cell_count": exact_unsat_cell_count,
        "exact_sat_cell_count": exact_sat_cell_count,
        "unknown_cell_count": unknown_cell_count,
        "tier_complete_numerical_enumeration": tier_complete,
        "exact_numerical_survivor_count_in_complete_tier": (
            len(all_survivors) if tier_complete else None
        ),
        "confirmed_numerical_survivors": all_survivors,
        "numerical_census_scope": "SELECTED_LOW_BRANCH_SIGNATURE_CELL_TIER_ONLY",
        "full_parent_complete": len(selected) == len(cells) and tier_complete,
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
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }

    deterministic = {
        k: v
        for k, v in report.items()
        if k not in {"elapsed_seconds", "shared_context_preparation_seconds"}
    }
    deterministic_cells = []
    for cell in report["cells"]:
        copy = dict(cell)
        copy["branch_rows"] = [
            {
                **row,
                "search": {
                    k: v
                    for k, v in row["search"].items()
                    if k != "elapsed_seconds"
                },
            }
            for row in cell["branch_rows"]
        ]
        deterministic_cells.append(copy)
    deterministic["cells"] = deterministic_cells
    report["deterministic_sha256_without_runtime"] = coset.canonical_sha256(
        deterministic
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "e": args.exceptional_mass,
                "a": args.curve_group_mass,
                "threshold": args.branch_threshold,
                "selected_cells": len(selected),
                "scheduled_branches": sum(row[2] for row in selected),
                "complete_cells": complete_cell_count,
                "unsat_cells": exact_unsat_cell_count,
                "sat_cells": exact_sat_cell_count,
                "unknown_cells": unknown_cell_count,
                "survivors": len(all_survivors),
                "nodes": sum(
                    int(branch["search"]["enumeration_node_count"])
                    for cell in cell_rows
                    for branch in cell["branch_rows"]
                ),
                "tier_complete": tier_complete,
                "seconds": report["elapsed_seconds"],
                "sha": report["deterministic_sha256_without_runtime"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
