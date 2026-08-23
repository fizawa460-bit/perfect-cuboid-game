#!/usr/bin/env python3
"""Representative equivalence regression against proof-bearing #1344 cells."""

from __future__ import annotations

import argparse
import json
import pathlib

from affine_lattice import (
    atomic_json,
    build_context,
    canonical_sha256,
    file_sha256,
    solve_cell,
    validate_checkpoint,
)


REGRESSION_LABELS = (
    "d6-g1-e4-a32-b10-f2-c31-h2-k1-l4-m2",
    "d6-g1-e4-a32-b11-f2-c30-h2-k1-l5-m3",
    "d6-g1-e4-a32-b12-f2-c31-h2-k1-l6-m3",
    "d6-g1-e4-a32-b11-f2-c31-h2-k1-l4-m0",
)


def load_predecessor_cell(root: pathlib.Path, label: str) -> tuple[dict, dict]:
    shard = root / label
    checkpoint_path = shard / "checkpoint.json"
    problem_path = shard / "problem.smt2"
    proof_path = shard / "proof.sexpr"
    predecessor = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    assert predecessor["complete"] is True
    assert predecessor["solver_result"] == "unsat"
    assert predecessor["unknown_reason"] is None
    assert predecessor["exact_survivor_count"] == 0
    assert predecessor["proof_sha256"] == file_sha256(proof_path)
    assert predecessor["smt2_sha256"] == file_sha256(problem_path)
    cell = dict(predecessor)
    cell["label"] = label
    cell["checkpoint_file_sha256"] = file_sha256(checkpoint_path)
    return cell, {
        "checkpoint_file_sha256": cell["checkpoint_file_sha256"],
        "smt2_sha256": predecessor["smt2_sha256"],
        "proof_sha256": predecessor["proof_sha256"],
        "elapsed_seconds": predecessor["elapsed_seconds"],
        "solver_result": predecessor["solver_result"],
        "exact_survivor_count": predecessor["exact_survivor_count"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--predecessor-checkpoint-dir", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    context = build_context(args.core)
    rows = []
    for label in REGRESSION_LABELS:
        cell, predecessor = load_predecessor_cell(
            args.predecessor_checkpoint_dir, label
        )
        result = solve_cell(context, cell)
        validate_checkpoint(result)
        path = args.output_dir / f"{label}.json"
        atomic_json(path, result)
        match = (
            result["solver_result"] == "UNSAT"
            and result["exact_survivor_count"]
            == predecessor["exact_survivor_count"]
        )
        rows.append(
            {
                "label": label,
                "predecessor": predecessor,
                "replacement": {
                    "solver_result": result["solver_result"],
                    "exact_survivor_count": result["exact_survivor_count"],
                    "deterministic_result_sha256": result[
                        "deterministic_result_sha256"
                    ],
                    "enumeration_transcript_sha256": result[
                        "enumeration_transcript_sha256"
                    ],
                    "checkpoint_file": path.name,
                    "checkpoint_file_sha256": file_sha256(path),
                    "elapsed_seconds": result["elapsed_seconds"],
                },
                "exact_match": match,
            }
        )
        print(
            json.dumps(
                {
                    "label": label,
                    "exact_match": match,
                    "seconds": result["elapsed_seconds"],
                },
                sort_keys=True,
            ),
            flush=True,
        )
    evidence = {
        "schema": "STAGE32_AFFINE_LATTICE_NEIGHBOR_REGRESSION_V1",
        "scope": "four representative proof-bearing completed neighboring terminal cells",
        "representative_neighbor_regression_complete": len(rows) == 4,
        "representative_neighbor_regression_match": all(
            row["exact_match"] for row in rows
        ),
        "predecessor_proof_files_independently_hashed": True,
        "rows": rows,
    }
    evidence["canonical_sha256_without_this_field"] = canonical_sha256(evidence)
    atomic_json(args.output_dir / "regression-evidence.json", evidence)
    if not evidence["representative_neighbor_regression_match"]:
        raise SystemExit("representative predecessor regression mismatch")


if __name__ == "__main__":
    main()
