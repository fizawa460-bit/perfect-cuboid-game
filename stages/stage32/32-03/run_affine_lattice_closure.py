#!/usr/bin/env python3
"""Run and checkpoint the exact closure of the 44 inherited terminal cells."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import pathlib
import platform
from typing import Any

from affine_lattice import (
    ALGORITHM_ID,
    atomic_json,
    build_context,
    canonical_sha256,
    file_sha256,
    solve_cell,
    validate_checkpoint,
)


WORKER_CONTEXT: Any = None


def initialize_worker(core_path: str) -> None:
    global WORKER_CONTEXT
    WORKER_CONTEXT = build_context(pathlib.Path(core_path))


def solve_worker(cell: dict[str, Any]) -> dict[str, Any]:
    assert WORKER_CONTEXT is not None
    return solve_cell(WORKER_CONTEXT, cell)


def validate_inherited_files(
    cells: list[dict[str, Any]], predecessor_dir: pathlib.Path
) -> None:
    for cell in cells:
        shard = predecessor_dir / cell["label"]
        checkpoint = shard / "checkpoint.json"
        problem = shard / "problem.smt2"
        assert file_sha256(checkpoint) == cell["checkpoint_file_sha256"]
        assert file_sha256(problem) == cell["smt2_sha256"]
        payload = json.loads(checkpoint.read_text(encoding="utf-8"))
        assert payload["complete"] is False
        assert payload["solver_result"] == "unknown"
        assert payload["unknown_reason"] == "timeout"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--inherited-evidence", type=pathlib.Path, required=True)
    parser.add_argument("--predecessor-checkpoint-dir", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--labels", nargs="*")
    args = parser.parse_args()

    inherited = json.loads(args.inherited_evidence.read_text(encoding="utf-8"))
    inherited_unsigned = dict(inherited)
    inherited_claimed = inherited_unsigned.pop("canonical_sha256_without_this_field")
    assert canonical_sha256(inherited_unsigned) == inherited_claimed
    cells = inherited["terminal_unknown"]
    assert len(cells) == inherited["terminal_unknown_count"] == 44
    if args.labels:
        wanted = set(args.labels)
        cells = [cell for cell in cells if cell["label"] in wanted]
        assert len(cells) == len(wanted)
    validate_inherited_files(cells, args.predecessor_checkpoint_dir)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_dir = args.output_dir / "cells"
    checkpoint_dir.mkdir(exist_ok=True)
    context = build_context(args.core)
    atomic_json(args.output_dir / "lattice-certificate.json", context.common_certificate)

    results: dict[str, dict[str, Any]] = {}
    pending: list[dict[str, Any]] = []
    for cell in cells:
        path = checkpoint_dir / f"{cell['label']}.json"
        if path.exists():
            payload = json.loads(path.read_text(encoding="utf-8"))
            validate_checkpoint(payload)
            assert payload["label"] == cell["label"]
            assert payload["inherited_checkpoint_file_sha256"] == cell[
                "checkpoint_file_sha256"
            ]
            assert payload["inherited_smt2_sha256"] == cell["smt2_sha256"]
            results[cell["label"]] = payload
        else:
            pending.append(cell)

    if pending:
        with concurrent.futures.ProcessPoolExecutor(
            max_workers=args.workers,
            initializer=initialize_worker,
            initargs=(str(args.core.resolve()),),
        ) as executor:
            futures = {executor.submit(solve_worker, cell): cell for cell in pending}
            for future in concurrent.futures.as_completed(futures):
                cell = futures[future]
                payload = future.result()
                validate_checkpoint(payload)
                path = checkpoint_dir / f"{cell['label']}.json"
                atomic_json(path, payload)
                results[cell["label"]] = payload
                print(
                    json.dumps(
                        {
                            "label": cell["label"],
                            "result": payload["solver_result"],
                            "survivors": payload["exact_survivor_count"],
                            "nodes": payload["enumeration_node_count"],
                            "seconds": payload["elapsed_seconds"],
                        },
                        sort_keys=True,
                    ),
                    flush=True,
                )

    ordered = [results[cell["label"]] for cell in cells]
    file_rows = []
    for cell in cells:
        path = checkpoint_dir / f"{cell['label']}.json"
        file_rows.append(
            {
                "label": cell["label"],
                "file": path.relative_to(args.output_dir).as_posix(),
                "sha256": file_sha256(path),
            }
        )
    all_closed = len(ordered) == 44 and all(row["complete"] for row in ordered)
    summary = {
        "schema": "STAGE32_E4_A32_TERMINAL_CLOSURE_V1",
        "algorithm_id": ALGORITHM_ID,
        "source_pr": 1344,
        "inherited_evidence_sha256": inherited_claimed,
        "core_file_sha256": context.core_hashes["file_sha256"],
        "common_certificate_file": "lattice-certificate.json",
        "common_certificate_file_sha256": file_sha256(
            args.output_dir / "lattice-certificate.json"
        ),
        "terminal_cell_count": len(ordered),
        "all_44_e4_a32_terminal_cells_exactly_closed": all_closed,
        "fixed_budget_map_rank": context.common_certificate["fixed_map_rank"],
        "reduced_kernel_dimension": context.common_certificate["kernel_dimension"],
        "hnf_image_index": context.common_certificate["hnf_image_index"],
        "hnf_image_rejected_cell_count": sum(
            not row["hnf_image_feasible"] for row in ordered
        ),
        "unknown_count": sum(not row["complete"] for row in ordered),
        "exact_survivor_count": sum(row["exact_survivor_count"] for row in ordered),
        "all_results": sorted({row["solver_result"] for row in ordered}),
        "runtime_seconds": {
            "sum": round(sum(row["elapsed_seconds"] for row in ordered), 6),
            "minimum": min(row["elapsed_seconds"] for row in ordered),
            "maximum": max(row["elapsed_seconds"] for row in ordered),
        },
        "enumeration_node_count": sum(row["enumeration_node_count"] for row in ordered),
        "intersection_prune_count": sum(row["intersection_prune_count"] for row in ordered),
        "cells": [
            {
                "label": row["label"],
                "old_disposition": "UNKNOWN(timeout)",
                "old_checkpoint_file_sha256": row[
                    "inherited_checkpoint_file_sha256"
                ],
                "old_smt2_sha256": row["inherited_smt2_sha256"],
                "new_disposition": row["solver_result"],
                "exact_survivor_count": row["exact_survivor_count"],
                "deterministic_result_sha256": row["deterministic_result_sha256"],
                "enumeration_transcript_sha256": row[
                    "enumeration_transcript_sha256"
                ],
                "runtime_seconds": row["elapsed_seconds"],
            }
            for row in ordered
        ],
        "checkpoint_files": file_rows,
        "environment": {
            "platform": platform.platform(),
            "processor": platform.processor(),
            "workers": args.workers,
            **context.common_certificate["tool_versions"],
        },
        "receiver_credit": False,
        "full_d176_d192_numerical_orbit_census": False,
        "low_degree_prefix_complete": False,
        "r29_lg2": "NOT_DISCHARGED",
        "r29_lg2_eff": "NOT_DISCHARGED",
        "r29_lg2_mb": "NOT_DISCHARGED",
        "g10_lowgenus_picard": "AMBER",
    }
    summary["canonical_sha256_without_this_field"] = canonical_sha256(summary)
    atomic_json(args.output_dir / "closure-evidence.json", summary)
    print(json.dumps(summary, sort_keys=True))
    if not all_closed:
        raise SystemExit("the complete 44-cell target has not been closed")


if __name__ == "__main__":
    main()
