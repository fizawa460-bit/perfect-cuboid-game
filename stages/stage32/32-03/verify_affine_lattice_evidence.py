#!/usr/bin/env python3
"""Recompute the exact search; do not trust stored Stage32-03 summaries."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import pathlib
from typing import Any

from affine_lattice import (
    atomic_json,
    build_context,
    canonical_sha256,
    file_sha256,
    solve_cell,
    validate_checkpoint,
)
from run_neighbor_regression import REGRESSION_LABELS, load_predecessor_cell


WORKER_CONTEXT: Any = None


def initialize_worker(core_path: str) -> None:
    global WORKER_CONTEXT
    WORKER_CONTEXT = build_context(pathlib.Path(core_path))


def solve_worker(cell: dict[str, Any]) -> dict[str, Any]:
    assert WORKER_CONTEXT is not None
    return solve_cell(WORKER_CONTEXT, cell)


def verify_canonical(payload: dict[str, Any]) -> None:
    unsigned = dict(payload)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    assert canonical_sha256(unsigned) == claimed


def deterministic_view(payload: dict[str, Any]) -> dict[str, Any]:
    result = dict(payload)
    result.pop("elapsed_seconds")
    result.pop("deterministic_result_sha256")
    result.pop("checkpoint_sha256_without_this_field")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--inherited-evidence", type=pathlib.Path, required=True)
    parser.add_argument("--predecessor-checkpoint-dir", type=pathlib.Path, required=True)
    parser.add_argument("--certificate-dir", type=pathlib.Path, required=True)
    parser.add_argument("--regression-dir", type=pathlib.Path, required=True)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    inherited = json.loads(args.inherited_evidence.read_text(encoding="utf-8"))
    verify_canonical(inherited)
    cells = inherited["terminal_unknown"]
    assert len(cells) == 44
    summary_path = args.certificate_dir / "closure-evidence.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    verify_canonical(summary)

    context = build_context(args.core)
    common_path = args.certificate_dir / "lattice-certificate.json"
    common = json.loads(common_path.read_text(encoding="utf-8"))
    verify_canonical(common)
    assert common == context.common_certificate
    assert file_sha256(common_path) == summary["common_certificate_file_sha256"]

    stored: dict[str, dict[str, Any]] = {}
    for cell in cells:
        path = args.certificate_dir / "cells" / f"{cell['label']}.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        validate_checkpoint(payload)
        assert payload["label"] == cell["label"]
        assert payload["inherited_checkpoint_file_sha256"] == cell[
            "checkpoint_file_sha256"
        ]
        assert payload["inherited_smt2_sha256"] == cell["smt2_sha256"]
        predecessor_shard = args.predecessor_checkpoint_dir / cell["label"]
        assert file_sha256(predecessor_shard / "checkpoint.json") == cell[
            "checkpoint_file_sha256"
        ]
        assert file_sha256(predecessor_shard / "problem.smt2") == cell[
            "smt2_sha256"
        ]
        stored[cell["label"]] = payload

    recomputed: dict[str, dict[str, Any]] = {}
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=args.workers,
        initializer=initialize_worker,
        initargs=(str(args.core.resolve()),),
    ) as executor:
        futures = {executor.submit(solve_worker, cell): cell for cell in cells}
        for future in concurrent.futures.as_completed(futures):
            cell = futures[future]
            payload = future.result()
            assert deterministic_view(payload) == deterministic_view(
                stored[cell["label"]]
            )
            assert payload["deterministic_result_sha256"] == stored[cell["label"]][
                "deterministic_result_sha256"
            ]
            recomputed[cell["label"]] = payload
            print(json.dumps({"verified": cell["label"]}, sort_keys=True), flush=True)

    assert len(recomputed) == 44
    independently_derived = {
        "cell_count": len(recomputed),
        "all_closed": all(row["complete"] for row in recomputed.values()),
        "unknown_count": sum(not row["complete"] for row in recomputed.values()),
        "survivor_count": sum(
            row["exact_survivor_count"] for row in recomputed.values()
        ),
        "results": sorted({row["solver_result"] for row in recomputed.values()}),
        "node_count": sum(row["enumeration_node_count"] for row in recomputed.values()),
        "intersection_prune_count": sum(
            row["intersection_prune_count"] for row in recomputed.values()
        ),
    }
    assert independently_derived["all_closed"] is True
    assert independently_derived["unknown_count"] == 0
    assert independently_derived["cell_count"] == summary["terminal_cell_count"] == 44
    assert independently_derived["survivor_count"] == summary["exact_survivor_count"]
    assert independently_derived["results"] == summary["all_results"]
    assert independently_derived["node_count"] == summary["enumeration_node_count"]
    assert independently_derived["intersection_prune_count"] == summary[
        "intersection_prune_count"
    ]
    assert summary["all_44_e4_a32_terminal_cells_exactly_closed"] is True

    regression_path = args.regression_dir / "regression-evidence.json"
    regression = json.loads(regression_path.read_text(encoding="utf-8"))
    verify_canonical(regression)
    regression_rows = {row["label"]: row for row in regression["rows"]}
    assert set(regression_rows) == set(REGRESSION_LABELS)
    for label in REGRESSION_LABELS:
        cell, predecessor = load_predecessor_cell(
            args.predecessor_checkpoint_dir, label
        )
        replacement_path = args.regression_dir / f"{label}.json"
        replacement = json.loads(replacement_path.read_text(encoding="utf-8"))
        validate_checkpoint(replacement)
        recomputed_replacement = solve_cell(context, cell)
        assert deterministic_view(recomputed_replacement) == deterministic_view(
            replacement
        )
        assert predecessor["solver_result"] == "unsat"
        assert recomputed_replacement["solver_result"] == "UNSAT"
        assert predecessor["exact_survivor_count"] == recomputed_replacement[
            "exact_survivor_count"
        ] == 0
        assert regression_rows[label]["exact_match"] is True

    result = {
        "status": "PASS_FULL_INDEPENDENT_RECOMPUTATION",
        "all_44_e4_a32_terminal_cells_exactly_closed": True,
        "exact_survivor_count": independently_derived["survivor_count"],
        "representative_neighbor_regression_complete": True,
        "representative_neighbor_regression_match": True,
        "closure_evidence_sha256": summary[
            "canonical_sha256_without_this_field"
        ],
        "regression_evidence_sha256": regression[
            "canonical_sha256_without_this_field"
        ],
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
