#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.metadata
import importlib.util
import itertools
import json
import pathlib
import platform
import sys
import time
from typing import Any

HERE = pathlib.Path(__file__).resolve().parent
S32 = HERE.parent
S32_05 = S32 / "32-05"
S32_08 = S32 / "32-08"
sys.path.insert(0, str(S32_05))
sys.path.insert(0, str(HERE))


def load_module(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


exhaustive = load_module(
    "stage32_16_exhaustive",
    S32_08 / "run_materialized_cell_exhaustive.py",
)
from cap_certificate import load_and_verify
from compact_e20_dynamic_shard import compact_row, csha, expected_mod_count

PLAN_SCHEMA = "STAGE32_D8_E20_A0_TIER65536_WORK_BALANCED_PLAN_V1"
RAW_SCHEMA = "STAGE32_D8_MATERIALIZED_CELL_BRANCH_SHARD_V1"
RECEIPT_SCHEMA = "STAGE32_D8_E20_A0_EXACT_WORK_BUNDLE_RECEIPT_V1"
ALGORITHM_ID = "D8_FIX52_SHARED_QTAIL12_EXHAUSTIVE_DYNAMIC_MOD_SHARD_BUNDLE_CONTEXT_V1"
EXPECTED_CAP_SHA = "75224aee543dcd4a56e814503765d1e1e69514b237fb900688243546ea6b4d03"


def package_version(name: str) -> str:
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return "NOT_INSTALLED"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    ap.add_argument("--plan", type=pathlib.Path, required=True)
    ap.add_argument("--bundle-id", required=True)
    ap.add_argument("--output-dir", type=pathlib.Path, required=True)
    ap.add_argument("--node-limit-per-branch", type=int, default=1_000_000)
    ap.add_argument("--max-raw-bytes", type=int, default=1_000_000_000)
    ap.add_argument("--max-compact-bytes", type=int, default=20_000)
    args = ap.parse_args()
    assert args.node_limit_per_branch == 1_000_000
    assert args.max_raw_bytes > 0 and args.max_compact_bytes > 0
    started = time.perf_counter()

    plan = json.loads(args.plan.read_text())
    assert plan["schema"] == PLAN_SCHEMA
    plan_unsigned = dict(plan)
    plan_claimed = plan_unsigned.pop("canonical_sha256_without_this_field")
    assert csha(plan_unsigned) == plan_claimed
    assert int(plan["parameters"]["node_limit_per_branch"]) == args.node_limit_per_branch
    matches = [b for b in plan["bundles"] if str(b["bundle_id"]) == args.bundle_id]
    regression = plan.get("representative_predecessor_regression")
    if regression and str(regression["bundle_id"]) == args.bundle_id:
        regression_item = dict(regression["item"])
        matches.append(
            {
                "bundle_id": args.bundle_id,
                "expected_branches": int(regression_item["expected_shard_branches"]),
                "item_count": 1,
                "items": [regression_item],
            }
        )
    assert len(matches) == 1
    bundle = matches[0]
    items = list(bundle["items"])
    assert items and int(bundle["item_count"]) == len(items)
    assert sum(int(i["expected_shard_branches"]) for i in items) == int(
        bundle["expected_branches"]
    )

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
        quotient["K"], aggregate["types"], 20, 0
    )
    common = cached.prepare_common(core)
    left_groups, right_groups = pilot.base.split_groups(aggregate["types"])
    context_ready = time.perf_counter()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    item_receipts: list[dict[str, Any]] = []
    max_raw_bytes_observed = 0
    total_raw_bytes = 0
    total_compact_bytes = 0
    total_nodes = 0
    total_survivors = 0

    active_cell_index: int | None = None
    active_cell: dict[str, Any] | None = None
    active_vectors: list[tuple[int, ...]] | None = None
    active_qheads: list[tuple[int, ...]] | None = None
    active_left_count = active_right_count = 0

    for ordinal, item in enumerate(items):
        item_started = time.perf_counter()
        cell_index = int(item["cell_index"])
        shard_index = int(item["shard_index"])
        shard_count = int(item["shard_count"])
        total_branches = int(item["total_branches"])
        assert shard_count >= 1 and 0 <= shard_index < shard_count
        assert int(item["expected_shard_branches"]) == expected_mod_count(
            total_branches, shard_count, shard_index
        )
        assert 0 <= cell_index < len(cells)

        if active_cell_index != cell_index:
            cell = cells[cell_index]
            assert cell["cell_id"] == str(item["cell_id"])
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
            actual_total = len(exceptional_vectors) * len(qheads)
            assert actual_total == total_branches
            active_cell_index = cell_index
            active_cell = cell
            active_vectors = exceptional_vectors
            active_qheads = qheads
            active_left_count = len(left)
            active_right_count = len(right)
        else:
            assert active_cell is not None
            assert active_cell["cell_id"] == str(item["cell_id"])
            assert active_vectors is not None and active_qheads is not None
            assert len(active_vectors) * len(active_qheads) == total_branches

        assert active_cell is not None
        assert active_vectors is not None and active_qheads is not None
        branches: list[dict[str, Any]] = []
        survivors: list[dict[str, Any]] = []
        any_unknown = False
        for branch_index, (exceptional, qhead) in enumerate(
            itertools.product(active_vectors, active_qheads)
        ):
            if branch_index % shard_count != shard_index:
                continue
            rhs = cached.branch_rhs(exceptional, qhead, 20, 0)
            base, base_cert = cached.branch_base(common, rhs)
            search = exhaustive.search_exhaustive(
                common,
                core,
                quotient["K"],
                aggregate["types"],
                base,
                active_cell,
                20,
                0,
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

        expected_branches = expected_mod_count(
            total_branches, shard_count, shard_index
        )
        assert len(branches) == expected_branches
        assert all(
            int(row["branch_index"]) % shard_count == shard_index for row in branches
        )
        survivors.sort(key=lambda row: tuple(row["basis_coordinates"]))
        keys = [tuple(row["basis_coordinates"]) for row in survivors]
        assert len(keys) == len(set(keys))
        complete = not any_unknown and len(branches) == expected_branches
        if not complete:
            result = "UNKNOWN_NODE_BUDGET"
        elif survivors:
            result = "SHARD_SAT_EXHAUSTED"
        else:
            result = "SHARD_UNSAT"

        raw = {
            "schema": RAW_SCHEMA,
            "algorithm_id": ALGORITHM_ID,
            "parameters": {
                "degree": pilot.DEGREE,
                "genus": 0,
                "exceptional_mass": 20,
                "curve_group_mass": 0,
                "cell_index": cell_index,
                "cell_id": active_cell["cell_id"],
                "node_limit_per_branch": args.node_limit_per_branch,
                "shard_index": shard_index,
                "shard_count": shard_count,
                "branch_partition": "GLOBAL_BRANCH_INDEX_MOD_SHARD_COUNT",
            },
            "signature_cell_inventory_sha256": inventory["cell_inventory_sha256"],
            "signature_cell": active_cell,
            "materialization": {
                "left_assignment_count": active_left_count,
                "right_assignment_count": active_right_count,
                "exceptional_vector_count": len(active_vectors),
                "qhead_assignment_count": len(active_qheads),
                "total_parent_cell_branch_count": total_branches,
                "expected_shard_branch_count": expected_branches,
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
            "numerical_census_scope": "ONE_SIGNATURE_CELL_DYNAMIC_BRANCH_SHARD_ONLY",
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
            "elapsed_seconds": round(time.perf_counter() - item_started, 6),
        }
        deterministic = {
            k: v
            for k, v in raw.items()
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
            for row in raw["branches"]
        ]
        raw["deterministic_sha256_without_runtime"] = coset.canonical_sha256(
            deterministic
        )

        stem = f"cell{cell_index:04d}-s{shard_index}of{shard_count}"
        raw_path = args.output_dir / f"{stem}-raw.json"
        compact_path = args.output_dir / f"{stem}-compact.json"
        raw_path.write_text(json.dumps(raw, indent=2, sort_keys=True) + "\n")
        raw_bytes = raw_path.stat().st_size
        max_raw_bytes_observed = max(max_raw_bytes_observed, raw_bytes)
        total_raw_bytes += raw_bytes
        assert raw_bytes <= args.max_raw_bytes

        # This call rechecks every exact branch row. No raw file is removed unless
        # the shard is complete, non-UNKNOWN, and the compact certificate verifies.
        compact = compact_row(raw)
        compact_path.write_text(json.dumps(compact, indent=2, sort_keys=True) + "\n")
        compact_bytes = compact_path.stat().st_size
        total_compact_bytes += compact_bytes
        assert compact_bytes <= args.max_compact_bytes
        raw_path.unlink()
        assert not raw_path.exists()

        nodes = int(compact["total_search_nodes"])
        survivor_count = int(compact["exact_numerical_survivor_count_in_shard"])
        total_nodes += nodes
        total_survivors += survivor_count
        item_receipts.append(
            {
                "ordinal": ordinal,
                "cell_index": cell_index,
                "cell_id": str(item["cell_id"]),
                "shard_index": shard_index,
                "shard_count": shard_count,
                "executed_branches": expected_branches,
                "search_nodes": nodes,
                "survivors": survivor_count,
                "raw_bytes_before_verified_compaction": raw_bytes,
                "compact_bytes": compact_bytes,
                "raw_deterministic_sha256": compact[
                    "source_raw_deterministic_sha256"
                ],
                "compact_canonical_sha256": compact[
                    "canonical_sha256_without_this_field"
                ],
                "branch_exact_evidence_stream_sha256": compact[
                    "branch_exact_evidence_stream_sha256"
                ],
                "elapsed_seconds": raw["elapsed_seconds"],
            }
        )
        print(
            json.dumps(
                {
                    "bundle": args.bundle_id,
                    "item": ordinal,
                    "cell": cell_index,
                    "shard": f"{shard_index}/{shard_count}",
                    "branches": expected_branches,
                    "nodes": nodes,
                    "survivors": survivor_count,
                    "raw_bytes": raw_bytes,
                    "compact_bytes": compact_bytes,
                },
                sort_keys=True,
            ),
            flush=True,
        )
        del branches, survivors, raw, compact

    elapsed = round(time.perf_counter() - started, 6)
    deterministic_receipt = {
        "schema": RECEIPT_SCHEMA,
        "plan_sha256": plan_claimed,
        "bundle_id": args.bundle_id,
        "planned_expected_branches": int(bundle["expected_branches"]),
        "executed_branches": sum(int(r["executed_branches"]) for r in item_receipts),
        "item_count": len(item_receipts),
        "all_items_complete": True,
        "unknown_branch_count": 0,
        "exact_numerical_survivor_count": total_survivors,
        "total_search_nodes": total_nodes,
        "certificates": [
            {k: v for k, v in row.items() if k != "elapsed_seconds"}
            for row in item_receipts
        ],
        "runner_local_raw_evidence_deleted_after_verification": True,
        "raw_branch_rows_uploaded": False,
        "theorem_credit": False,
        "receiver_credit": False,
    }
    receipt = {
        **deterministic_receipt,
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "python_flint": package_version("python-flint"),
            "sympy": package_version("sympy"),
        },
        "runtime": {
            "context_initialization_seconds": round(context_ready - started, 6),
            "shared_exact_context_preparation_seconds": round(
                float(common["preparation_seconds"]), 6
            ),
            "bundle_elapsed_seconds": elapsed,
            "item_elapsed_seconds": [r["elapsed_seconds"] for r in item_receipts],
            "maximum_runner_local_raw_bytes": max_raw_bytes_observed,
            "total_runner_local_raw_bytes_before_compaction": total_raw_bytes,
            "total_compact_bytes": total_compact_bytes,
        },
    }
    receipt["deterministic_sha256_without_environment_or_runtime"] = csha(
        deterministic_receipt
    )
    receipt["canonical_sha256_without_this_field"] = csha(receipt)
    receipt_path = args.output_dir / "bundle-receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    assert not list(args.output_dir.glob("*-raw.json"))
    print(
        json.dumps(
            {
                "bundle": args.bundle_id,
                "items": len(item_receipts),
                "branches": receipt["executed_branches"],
                "nodes": total_nodes,
                "survivors": total_survivors,
                "seconds": elapsed,
                "max_raw_bytes": max_raw_bytes_observed,
                "receipt_sha": receipt["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
