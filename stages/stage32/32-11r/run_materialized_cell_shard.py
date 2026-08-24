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
S32_08 = S32 / "32-08"
sys.path.insert(0, str(S32_05))


def load_module(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


exhaustive = load_module(
    "stage32_11r_exhaustive",
    S32_08 / "run_materialized_cell_exhaustive.py",
)
from cap_certificate import load_and_verify

SCHEMA = "STAGE32_D8_MATERIALIZED_CELL_BRANCH_SHARD_V1"
ALGORITHM_ID = "D8_FIX52_SHARED_QTAIL12_EXHAUSTIVE_BRANCH_MOD_SHARD_V1"
EXPECTED_CAP_SHA = "75224aee543dcd4a56e814503765d1e1e69514b237fb900688243546ea6b4d03"


def expected_mod_count(total: int, shard_count: int, shard_index: int) -> int:
    return total // shard_count + (1 if shard_index < total % shard_count else 0)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--exceptional-mass", type=int, required=True)
    ap.add_argument("--curve-group-mass", type=int, required=True)
    ap.add_argument("--cell-index", type=int, required=True)
    ap.add_argument("--expected-cell-id", required=True)
    ap.add_argument("--expected-total-branches", type=int, required=True)
    ap.add_argument("--shard-index", type=int, required=True)
    ap.add_argument("--shard-count", type=int, required=True)
    ap.add_argument("--node-limit-per-branch", type=int, default=1000000)
    args = ap.parse_args()

    assert args.shard_count > 1
    assert 0 <= args.shard_index < args.shard_count
    started = time.perf_counter()

    core, _, cap_summary = load_and_verify(args.core, args.cap_certificate)
    assert cap_summary["certificate_canonical_sha256"] == EXPECTED_CAP_SHA

    pilot = exhaustive.pilot
    v1 = exhaustive.v1
    cached = exhaustive.cached
    coset = exhaustive.coset

    transform = pilot.base.build_transform(core)
    quotient = pilot.base.quotient_data(transform["inv"])
    aggregate = pilot.base.aggregate_structure(transform["pair"], transform["h"])
    cells, inventory = pilot.build_signature_cells(
        quotient["K"],
        aggregate["types"],
        args.exceptional_mass,
        args.curve_group_mass,
    )
    assert 0 <= args.cell_index < len(cells)
    cell = cells[args.cell_index]
    assert cell["cell_id"] == args.expected_cell_id

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
    qheads = v1.qhead_assignments(int(cell["aggregate"][3]))
    assert qheads

    exceptional_vectors = sorted(
        {
            tuple(l[i] + r[i] for i in range(48))
            for l in left
            for r in right
        }
    )
    assert len(exceptional_vectors) == len(left) * len(right)
    total_branch_count = len(exceptional_vectors) * len(qheads)
    assert total_branch_count == args.expected_total_branches
    expected_shard_branches = expected_mod_count(
        total_branch_count, args.shard_count, args.shard_index
    )

    common = cached.prepare_common(core)
    branches: list[dict[str, Any]] = []
    survivors: list[dict[str, Any]] = []
    any_unknown = False

    for branch_index, (exceptional, qhead) in enumerate(
        itertools.product(exceptional_vectors, qheads)
    ):
        if branch_index % args.shard_count != args.shard_index:
            continue
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
        branches.append(
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
        survivors.extend(search["survivors"])
        if not search["complete_numerical_enumeration"]:
            any_unknown = True

    assert len(branches) == expected_shard_branches
    assert all(
        int(row["branch_index"]) % args.shard_count == args.shard_index
        for row in branches
    )

    survivors.sort(key=lambda row: tuple(row["basis_coordinates"]))
    keys = [tuple(row["basis_coordinates"]) for row in survivors]
    assert len(keys) == len(set(keys))

    complete = not any_unknown and len(branches) == expected_shard_branches
    if not complete:
        result = "UNKNOWN_NODE_BUDGET"
    elif survivors:
        result = "SHARD_SAT_EXHAUSTED"
    else:
        result = "SHARD_UNSAT"

    report = {
        "schema": SCHEMA,
        "algorithm_id": ALGORITHM_ID,
        "parameters": {
            "degree": pilot.DEGREE,
            "genus": 0,
            "exceptional_mass": args.exceptional_mass,
            "curve_group_mass": args.curve_group_mass,
            "cell_index": args.cell_index,
            "cell_id": cell["cell_id"],
            "node_limit_per_branch": args.node_limit_per_branch,
            "shard_index": args.shard_index,
            "shard_count": args.shard_count,
            "branch_partition": "GLOBAL_BRANCH_INDEX_MOD_SHARD_COUNT",
        },
        "signature_cell_inventory_sha256": inventory["cell_inventory_sha256"],
        "signature_cell": cell,
        "materialization": {
            "left_assignment_count": len(left),
            "right_assignment_count": len(right),
            "exceptional_vector_count": len(exceptional_vectors),
            "qhead_assignment_count": len(qheads),
            "total_parent_cell_branch_count": total_branch_count,
            "expected_shard_branch_count": expected_shard_branches,
            "executed_shard_branch_count": len(branches),
            "all_exceptional_assignments_materialized_before_partition": True,
            "all_qhead_assignments_materialized_before_partition": True,
            "fixed_selected_coordinate_count_per_branch": 52,
        },
        "shared_context": common["certificate"],
        "shared_context_preparation_seconds": common["preparation_seconds"],
        "branches": branches,
        "solver_result": result,
        "complete_shard_numerical_enumeration": complete,
        "exact_numerical_survivor_count_in_shard": (
            len(survivors) if complete else None
        ),
        "numerical_survivors": survivors,
        "numerical_census_scope": "ONE_SIGNATURE_CELL_BRANCH_SHARD_ONLY",
        "effectivity_classification_complete": False,
        "actual_curve_existence_claim": False,
        "parent_exactly_closed": False,
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
    deterministic["branches"] = [
        {
            **row,
            "search": {
                k: v
                for k, v in row["search"].items()
                if k != "elapsed_seconds"
            },
        }
        for row in report["branches"]
    ]
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
                "cell_index": args.cell_index,
                "cell_id": cell["cell_id"],
                "shard": f"{args.shard_index}/{args.shard_count}",
                "total_cell_branches": total_branch_count,
                "shard_branches": len(branches),
                "nodes": sum(
                    int(row["search"]["enumeration_node_count"])
                    for row in branches
                ),
                "survivors": len(survivors),
                "complete": complete,
                "result": result,
                "seconds": report["elapsed_seconds"],
                "sha": report["deterministic_sha256_without_runtime"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
