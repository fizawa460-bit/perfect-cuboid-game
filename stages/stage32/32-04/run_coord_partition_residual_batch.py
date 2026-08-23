#!/usr/bin/env python3
"""Close the 13 post-audit residual parents with bounded coordinates.

Each parent gets one exact direct coordinate attempt.  Only direct UNKNOWNs are
sent to the audited Stage32-02 deterministic partition tree with the coordinate
leaf backend.  This keeps the target bounded to the original 28 PR1343
residual parents and preserves the Stage32 receiver firewalls.
"""
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


def load_regression() -> Any:
    path = pathlib.Path(__file__).resolve().parents[1] / "32-02" / "run_pr1343_regression.py"
    spec = importlib.util.spec_from_file_location("stage32_02_regression_coord_partition", path)
    if spec is None or spec.loader is None:
        raise SystemExit("cannot load Stage32-02 source lock")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def audited_closed() -> tuple[set[str], dict[str, Any]]:
    stage32 = pathlib.Path(__file__).resolve().parents[1]
    local = json.loads((stage32 / "32-02" / "local-evidence.json").read_text(encoding="utf-8"))
    labels = {
        row["label"]
        for row in local["formerly_unresolved_residuals"]
        if row["disposition"].startswith("CLOSED_") and row["exact_survivor_count"] == 0
    }
    assert len(labels) == local["closed_residual_count"] == 14
    affine = json.loads(
        (stage32 / "32-03" / "certificates" / "closure-evidence.json").read_text(encoding="utf-8")
    )
    assert affine["all_44_e4_a32_terminal_cells_exactly_closed"] is True
    assert affine["unknown_count"] == 0 and affine["exact_survivor_count"] == 0
    labels.add("d6-g1-e4-a32")
    assert len(labels) == 15
    return labels, {
        "stage32_02_local_evidence_sha256": local["canonical_sha256_without_this_field"],
        "stage32_03_affine_closure_sha256": affine["canonical_sha256_without_this_field"],
    }


def direct(task: Any, core: pathlib.Path, output: pathlib.Path, cap: pathlib.Path, timeout: float, proof: bool) -> dict[str, Any]:
    command = [
        sys.executable,
        str(pathlib.Path(__file__).with_name("run_intersection_coord_budget.py")),
        "--core", str(core),
        "--cap-certificate", str(cap),
        "--output-dir", str(output),
        "--degree", str(task.degree),
        "--genus", str(task.genus),
        "--exceptional-mass", str(task.exceptional_mass),
        "--curve-group-mass", str(task.curve_group_mass),
        "--timeout", str(timeout),
    ]
    if proof:
        command.append("--proof")
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    checkpoint = output / task.label / "checkpoint.json"
    if not checkpoint.exists():
        return {
            "label": task.label,
            "complete": False,
            "method": "COORD_DIRECT",
            "returncode": completed.returncode,
            "stdout_tail": completed.stdout[-2000:],
            "stderr_tail": completed.stderr[-2000:],
        }
    payload = json.loads(checkpoint.read_text(encoding="utf-8"))
    return {
        "label": task.label,
        "complete": bool(payload["complete"]),
        "method": "COORD_DIRECT",
        "solver_result": payload["solver_result"],
        "unknown_reason": payload["unknown_reason"],
        "exact_survivor_count": payload["exact_survivor_count"],
        "deterministic_result_sha256": payload["deterministic_result_sha256"],
        "checkpoint_sha256_without_this_field": payload["checkpoint_sha256_without_this_field"],
        "smt2_sha256": payload["smt2_sha256"],
        "proof_sha256": payload["proof_sha256"],
        "elapsed_seconds": payload["elapsed_seconds"],
        "returncode": completed.returncode,
    }


def partition(task: Any, core: pathlib.Path, output: pathlib.Path, cap: pathlib.Path, timeout: float, workers: int, proof: bool) -> dict[str, Any]:
    command = [
        sys.executable,
        str(pathlib.Path(__file__).with_name("run_coord_z3_partition.py")),
        "--cap-certificate", str(cap),
        "--core", str(core),
        "--output-dir", str(output),
        "--degree", str(task.degree),
        "--genus", str(task.genus),
        "--exceptional-mass", str(task.exceptional_mass),
        "--curve-group-mass", str(task.curve_group_mass),
        "--workers", str(workers),
        "--timeout", str(timeout),
    ]
    if proof:
        command.append("--proof")
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    path = output / f"partition-{task.label}.json"
    if not path.exists():
        return {
            "label": task.label,
            "complete": False,
            "method": "COORD_DETERMINISTIC_PARTITION",
            "returncode": completed.returncode,
            "stdout_tail": completed.stdout[-4000:],
            "stderr_tail": completed.stderr[-4000:],
        }
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {
        "label": task.label,
        "complete": bool(payload["all_complete"]),
        "method": "COORD_DETERMINISTIC_PARTITION",
        "exact_survivor_count": payload["exact_survivor_count"],
        "deterministic_result_sha256": payload["deterministic_result_sha256"],
        "wall_seconds": payload["wall_seconds"],
        "partition_file": path.name,
        "returncode": completed.returncode,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-dir", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    parser.add_argument("--direct-workers", type=int, default=4)
    parser.add_argument("--direct-timeout", type=float, default=120.0)
    parser.add_argument("--leaf-workers", type=int, default=4)
    parser.add_argument("--leaf-timeout", type=float, default=30.0)
    parser.add_argument("--proof", action="store_true")
    args = parser.parse_args()

    regression = load_regression()
    artifact_hashes = regression.lock_artifacts(args.artifact_dir)
    _, residual = regression.source_tasks(args.artifact_dir)
    assert len(residual) == 28
    predecessor_closed, predecessor_evidence = audited_closed()
    targets = [task for task in residual if task.label not in predecessor_closed]
    assert len(targets) == 13
    args.output_dir.mkdir(parents=True, exist_ok=True)
    core = args.artifact_dir / "picard-core.json"

    started = time.perf_counter()
    direct_results: dict[str, dict[str, Any]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.direct_workers) as executor:
        futures = {
            executor.submit(
                direct, task, core, args.output_dir, args.cap_certificate,
                args.direct_timeout, args.proof
            ): task
            for task in targets
        }
        for future in concurrent.futures.as_completed(futures):
            task = futures[future]
            row = future.result()
            direct_results[task.label] = row
            print(json.dumps(row, sort_keys=True), flush=True)

    results: dict[str, dict[str, Any]] = {}
    for task in targets:
        row = direct_results[task.label]
        if row.get("complete"):
            results[task.label] = row
            continue
        refined = partition(
            task,
            core,
            args.output_dir,
            args.cap_certificate,
            args.leaf_timeout,
            args.leaf_workers,
            args.proof,
        )
        refined["direct_result"] = row
        results[task.label] = refined
        print(json.dumps(refined, sort_keys=True), flush=True)

    ordered = [results[task.label] for task in targets]
    current_closed = {
        row["label"]
        for row in ordered
        if row.get("complete") and row.get("exact_survivor_count") == 0
    }
    combined = predecessor_closed | current_closed
    unresolved = [task.label for task in targets if task.label not in current_closed]
    manifest = {
        "schema": "STAGE32_COORD_PARTITION_RESIDUAL_BATCH_V1",
        "source_pr": 1343,
        "source_runs": [32623143985, 32623610941, 32624596141],
        "source_artifact_hashes": artifact_hashes,
        "audited_predecessor_evidence": predecessor_evidence,
        "original_residual_parent_count": 28,
        "audited_predecessor_closed_parent_count": len(predecessor_closed),
        "current_target_parent_count": len(targets),
        "current_exactly_closed_parent_count": len(current_closed),
        "combined_exactly_closed_parent_count": len(combined),
        "all_28_residual_parents_exactly_closed": len(combined) == 28,
        "unresolved": unresolved,
        "entries": ordered,
        "direct_timeout_seconds": args.direct_timeout,
        "partition_leaf_timeout_seconds": args.leaf_timeout,
        "wall_seconds": round(time.perf_counter() - started, 6),
        "proof_requested": args.proof,
        "low_degree_prefix_complete": False,
        "full_d176_d192_numerical_orbit_census": False,
        "receiver_credit": False,
        "r29_lg2": "NOT_DISCHARGED",
        "r29_lg2_eff": "NOT_DISCHARGED",
        "r29_lg2_mb": "NOT_DISCHARGED",
        "g10_lowgenus_picard": "AMBER",
    }
    (args.output_dir / "coord-partition-residual-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, sort_keys=True))
    if not manifest["all_28_residual_parents_exactly_closed"]:
        raise SystemExit("bounded coordinate partition batch retained unresolved parents")


if __name__ == "__main__":
    main()
