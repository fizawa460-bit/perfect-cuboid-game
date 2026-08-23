#!/usr/bin/env python3
"""Recompute all 28 PR #1343 residual singletons with exact dual caps."""
from __future__ import annotations

import argparse
import concurrent.futures
import importlib.util
import json
import pathlib
import subprocess
import sys
import time
from typing import Any


def load_predecessor_regression() -> Any:
    path = pathlib.Path(__file__).resolve().parents[1] / "32-02" / "run_pr1343_regression.py"
    spec = importlib.util.spec_from_file_location("stage32_02_regression", path)
    if spec is None or spec.loader is None:
        raise SystemExit("cannot load Stage32-02 regression source lock")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def run_one(
    task: Any,
    artifact_dir: pathlib.Path,
    output_dir: pathlib.Path,
    certificate: pathlib.Path,
    timeout: float,
    proof: bool,
) -> dict[str, Any]:
    wrapper = pathlib.Path(__file__).with_name("run_cap_z3_budget.py")
    command = [
        sys.executable,
        str(wrapper),
        "--cap-certificate",
        str(certificate),
        "--core",
        str(artifact_dir / "picard-core.json"),
        "--output-dir",
        str(output_dir),
        "--degree",
        str(task.degree),
        "--genus",
        str(task.genus),
        "--exceptional-mass",
        str(task.exceptional_mass),
        "--curve-group-mass",
        str(task.curve_group_mass),
        "--threads",
        "1",
        "--timeout",
        str(timeout),
    ]
    if proof:
        command.append("--proof")
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    checkpoint = output_dir / task.label / "checkpoint.json"
    if not checkpoint.exists():
        return {
            "label": task.label,
            "complete": False,
            "returncode": completed.returncode,
            "stderr_tail": completed.stderr[-4000:],
            "stdout_tail": completed.stdout[-4000:],
        }
    payload = json.loads(checkpoint.read_text(encoding="utf-8"))
    return {
        "label": task.label,
        "complete": bool(payload["complete"]),
        "solver_result": payload["solver_result"],
        "unknown_reason": payload["unknown_reason"],
        "exact_survivor_count": payload["exact_survivor_count"],
        "elapsed_seconds": payload["elapsed_seconds"],
        "deterministic_result_sha256": payload["deterministic_result_sha256"],
        "smt2_sha256": payload["smt2_sha256"],
        "proof_sha256": payload["proof_sha256"],
        "checkpoint_sha256_without_this_field": payload[
            "checkpoint_sha256_without_this_field"
        ],
        "returncode": completed.returncode,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-dir", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=float, default=180.0)
    parser.add_argument("--proof", action="store_true")
    args = parser.parse_args()

    predecessor = load_predecessor_regression()
    artifact_hashes = predecessor.lock_artifacts(args.artifact_dir)
    _, residual = predecessor.source_tasks(args.artifact_dir)
    assert len(residual) == 28
    args.output_dir.mkdir(parents=True, exist_ok=True)

    started = time.perf_counter()
    results: dict[str, dict[str, Any]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(
                run_one,
                task,
                args.artifact_dir,
                args.output_dir,
                args.cap_certificate,
                args.timeout,
                args.proof,
            ): task
            for task in residual
        }
        for future in concurrent.futures.as_completed(futures):
            task = futures[future]
            row = future.result()
            results[task.label] = row
            print(json.dumps(row, sort_keys=True), flush=True)

    ordered = [results[task.label] for task in residual]
    unresolved = [row["label"] for row in ordered if not row.get("complete")]
    survivors = sum(
        int(row.get("exact_survivor_count") or 0)
        for row in ordered
        if row.get("complete")
    )
    manifest = {
        "schema": "STAGE32_CAP_RESIDUAL_BATCH_V1",
        "source_pr": 1343,
        "source_runs": [32623143985, 32623610941, 32624596141],
        "source_artifact_hashes": artifact_hashes,
        "residual_task_count": 28,
        "all_28_residuals_exactly_closed": not unresolved and len(ordered) == 28,
        "exact_survivor_total": survivors,
        "unresolved": unresolved,
        "entries": ordered,
        "wall_seconds": round(time.perf_counter() - started, 6),
        "proof_requested": args.proof,
        "intersection_caps": {
            "curves": "<= floor(d/2)",
            "exceptionals": "<= floor(d/4)",
        },
        "low_degree_prefix_complete": False,
        "full_d176_d192_numerical_orbit_census": False,
        "receiver_credit": False,
        "r29_lg2": "NOT_DISCHARGED",
        "r29_lg2_eff": "NOT_DISCHARGED",
        "r29_lg2_mb": "NOT_DISCHARGED",
        "g10_lowgenus_picard": "AMBER",
    }
    (args.output_dir / "cap-residual-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, sort_keys=True))


if __name__ == "__main__":
    main()
