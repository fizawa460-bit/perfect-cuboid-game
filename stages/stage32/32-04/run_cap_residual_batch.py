#!/usr/bin/env python3
"""Close the residual parents not already discharged by audited 32-02/32-03 evidence.

Each current parent first gets a direct exact capped Z3 attempt. A timeout then
falls through to the unchanged Stage32-02 deterministic partition tree whose
leaf backend is replaced by the exact-capped wrapper.
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


def load_predecessor_regression() -> Any:
    path = pathlib.Path(__file__).resolve().parents[1] / "32-02" / "run_pr1343_regression.py"
    spec = importlib.util.spec_from_file_location("stage32_02_regression", path)
    if spec is None or spec.loader is None:
        raise SystemExit("cannot load Stage32-02 regression source lock")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def audited_predecessor_closed_labels() -> tuple[set[str], dict[str, Any]]:
    stage32 = pathlib.Path(__file__).resolve().parents[1]
    local = json.loads((stage32 / "32-02" / "local-evidence.json").read_text(encoding="utf-8"))
    closed = {
        row["label"]
        for row in local["formerly_unresolved_residuals"]
        if row["disposition"].startswith("CLOSED_")
        and row["exact_survivor_count"] == 0
    }
    assert len(closed) == local["closed_residual_count"] == 14

    affine = json.loads(
        (stage32 / "32-03" / "certificates" / "closure-evidence.json").read_text(
            encoding="utf-8"
        )
    )
    assert affine["all_44_e4_a32_terminal_cells_exactly_closed"] is True
    assert affine["unknown_count"] == 0 and affine["exact_survivor_count"] == 0
    closed.add("d6-g1-e4-a32")
    assert len(closed) == 15
    return closed, {
        "stage32_02_local_evidence_sha256": local[
            "canonical_sha256_without_this_field"
        ],
        "stage32_02_closed_parent_count": 14,
        "stage32_03_affine_closure_sha256": affine[
            "canonical_sha256_without_this_field"
        ],
        "stage32_03_added_parent": "d6-g1-e4-a32",
    }


def direct_command(
    task: Any,
    artifact_dir: pathlib.Path,
    output_dir: pathlib.Path,
    certificate: pathlib.Path,
    timeout: float,
    proof: bool,
) -> list[str]:
    command = [
        sys.executable,
        str(pathlib.Path(__file__).with_name("run_cap_z3_budget.py")),
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
    return command


def run_one(
    task: Any,
    artifact_dir: pathlib.Path,
    output_dir: pathlib.Path,
    certificate: pathlib.Path,
    direct_timeout: float,
    partition_timeout: float,
    partition_workers: int,
    proof: bool,
) -> dict[str, Any]:
    completed = subprocess.run(
        direct_command(
            task,
            artifact_dir,
            output_dir,
            certificate,
            direct_timeout,
            proof,
        ),
        capture_output=True,
        text=True,
        check=False,
    )
    checkpoint = output_dir / task.label / "checkpoint.json"
    direct_payload = (
        json.loads(checkpoint.read_text(encoding="utf-8")) if checkpoint.exists() else None
    )
    if direct_payload is not None and direct_payload.get("complete"):
        return {
            "label": task.label,
            "complete": True,
            "method": "CAPPED_DIRECT",
            "solver_result": direct_payload["solver_result"],
            "unknown_reason": None,
            "exact_survivor_count": direct_payload["exact_survivor_count"],
            "elapsed_seconds": direct_payload["elapsed_seconds"],
            "deterministic_result_sha256": direct_payload[
                "deterministic_result_sha256"
            ],
            "smt2_sha256": direct_payload["smt2_sha256"],
            "proof_sha256": direct_payload["proof_sha256"],
            "returncode": completed.returncode,
        }

    partition_command = [
        sys.executable,
        str(pathlib.Path(__file__).with_name("run_cap_z3_partition.py")),
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
        "--workers",
        str(partition_workers),
        "--timeout",
        str(partition_timeout),
    ]
    if proof:
        partition_command.append("--proof")
    partitioned = subprocess.run(
        partition_command, capture_output=True, text=True, check=False
    )
    partition_path = output_dir / f"partition-{task.label}.json"
    if partition_path.exists():
        parent = json.loads(partition_path.read_text(encoding="utf-8"))
        return {
            "label": task.label,
            "complete": bool(parent["all_complete"]),
            "method": "CAPPED_DETERMINISTIC_PARTITION",
            "solver_result": "unsat" if parent["all_complete"] and parent["exact_survivor_count"] == 0 else "incomplete",
            "unknown_reason": None if parent["all_complete"] else "partition_incomplete",
            "exact_survivor_count": parent["exact_survivor_count"] if parent["all_complete"] else None,
            "elapsed_seconds": parent["wall_seconds"],
            "deterministic_result_sha256": parent[
                "deterministic_result_sha256"
            ],
            "partition_manifest": partition_path.name,
            "direct_result": direct_payload["solver_result"] if direct_payload else None,
            "direct_unknown_reason": direct_payload["unknown_reason"] if direct_payload else None,
            "returncode": partitioned.returncode,
        }

    return {
        "label": task.label,
        "complete": False,
        "method": "CAPPED_DETERMINISTIC_PARTITION",
        "solver_result": "incomplete",
        "unknown_reason": "no_partition_manifest",
        "exact_survivor_count": None,
        "direct_result": direct_payload["solver_result"] if direct_payload else None,
        "returncode": partitioned.returncode,
        "stderr_tail": partitioned.stderr[-4000:],
        "stdout_tail": partitioned.stdout[-4000:],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-dir", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--direct-timeout", type=float, default=60.0)
    parser.add_argument("--partition-timeout", type=float, default=45.0)
    parser.add_argument("--partition-workers", type=int, default=1)
    parser.add_argument("--proof", action="store_true")
    args = parser.parse_args()

    predecessor = load_predecessor_regression()
    artifact_hashes = predecessor.lock_artifacts(args.artifact_dir)
    _, residual = predecessor.source_tasks(args.artifact_dir)
    assert len(residual) == 28
    predecessor_closed, predecessor_evidence = audited_predecessor_closed_labels()
    residual_labels = {task.label for task in residual}
    assert predecessor_closed <= residual_labels
    targets = [task for task in residual if task.label not in predecessor_closed]
    assert len(targets) == 13
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
                args.direct_timeout,
                args.partition_timeout,
                args.partition_workers,
                args.proof,
            ): task
            for task in targets
        }
        for future in concurrent.futures.as_completed(futures):
            task = futures[future]
            row = future.result()
            results[task.label] = row
            print(json.dumps(row, sort_keys=True), flush=True)

    ordered = [results[task.label] for task in targets]
    unresolved = [row["label"] for row in ordered if not row.get("complete")]
    survivors = sum(
        int(row.get("exact_survivor_count") or 0)
        for row in ordered
        if row.get("complete")
    )
    complete_current = {
        row["label"] for row in ordered if row.get("complete") and row.get("exact_survivor_count") == 0
    }
    combined_closed = predecessor_closed | complete_current
    manifest = {
        "schema": "STAGE32_CAP_RESIDUAL_BATCH_V2",
        "source_pr": 1343,
        "source_runs": [32623143985, 32623610941, 32624596141],
        "source_artifact_hashes": artifact_hashes,
        "audited_predecessor_evidence": predecessor_evidence,
        "original_residual_task_count": 28,
        "audited_predecessor_closed_parent_count": len(predecessor_closed),
        "current_target_parent_count": len(targets),
        "current_exactly_closed_parent_count": len(complete_current),
        "combined_exactly_closed_parent_count": len(combined_closed),
        "all_28_residual_parents_exactly_closed": len(combined_closed) == 28,
        "exact_survivor_total_current_batch": survivors,
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
