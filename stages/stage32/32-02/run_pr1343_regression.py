#!/usr/bin/env python3
"""Close and regress every PR #1343 low-degree checkpoint shard exactly."""

from __future__ import annotations

import argparse
import concurrent.futures
import dataclasses
import hashlib
import json
import pathlib
import subprocess
import sys
import time
from typing import Any


EXPECTED_UNRESOLVED = {
    0: [43, 44, 45, 46, 47],
    2: [37, 38, 39, 40, 41],
    4: [31, 32, 33, 34],
    6: [25, 26, 27, 28],
    8: [19, 20, 21, 22],
    10: [13, 14, 15],
    12: [7, 8, 9],
}
EXPECTED_FILES = {
    "picard-core.json": "eac92f66d02bb201668ae609108d37160953992915e08464b2bc5dea8f886d56",
    "numeric-magma-slice-d2-g0.txt": "2007c617175e91d0f9b6f037cb79d737dcfcc69f0ab45ca62089ea5514eaafd7",
    "numeric-magma-strata-d4-g1.json": "b563823af07e7173557b05f1dd96b2af45e93416261c4e63bf243cc36a0cc52f",
    "numeric-magma-strata-d6-g1.json": "59632b8896fade21ac483c67b30b166c29323feebb886eaf44f1c5d13959702e",
    "numeric-magma-curvegroup-adaptive-d6-g1-e0.json": "5a1af5269fb453b8841114de9026754d4e092ad74ebd53352ee7c6482956f2ca",
    "numeric-magma-curvegroup-adaptive-d6-g1-e2.json": "33c322864b64d30da5253179801b47a91f19b93a6a3d2b48f08dd251bf6f863e",
    "numeric-magma-curvegroup-adaptive-d6-g1-e4.json": "b6febb89d4eaa9ddd4958d95c74aed91a2162c7cbc93d406b8b66bb20a317de0",
    "numeric-magma-curvegroup-adaptive-d6-g1-e6.json": "b8558c84c16b3b63b6ed00784732b6d7ac45c94e7f85041a31b21f27c3c404e7",
    "numeric-magma-curvegroup-adaptive-d6-g1-e8.json": "b6ceb6e6fc291a1993cbcf18f6472c8a5471f345b70e46a3be7c9325ff8ff0da",
    "numeric-magma-curvegroup-adaptive-d6-g1-e10.json": "dcb85e9db308c567813afe494dc795bc4f54584a64e129950d24da44f41cdad9",
    "numeric-magma-curvegroup-adaptive-d6-g1-e12.json": "70944d0f30d05474bbece2bb71433cbc8b790ac4a53b495e365abeee80d7851d",
}


@dataclasses.dataclass(frozen=True, order=True)
class Task:
    degree: int
    genus: int
    exceptional_mass: int | None
    curve_group_mass: int | None
    source: str

    @property
    def label(self) -> str:
        label = f"d{self.degree}-g{self.genus}"
        if self.exceptional_mass is not None:
            label += f"-e{self.exceptional_mass}"
        if self.curve_group_mass is not None:
            label += f"-a{self.curve_group_mass}"
        return label


def file_sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def lock_artifacts(artifact_dir: pathlib.Path) -> dict[str, str]:
    observed: dict[str, str] = {}
    for name, expected in EXPECTED_FILES.items():
        path = artifact_dir / name
        if not path.exists():
            raise SystemExit(f"missing locked #1343 artifact {name}")
        actual = file_sha256(path)
        if actual != expected:
            raise SystemExit(f"#1343 artifact hash mismatch for {name}: {actual}")
        observed[name] = actual
    return observed


def source_tasks(artifact_dir: pathlib.Path) -> tuple[list[Task], list[Task]]:
    regression = [Task(2, 0, None, None, "#1343 d2/g0 completed row")]
    d4 = json.loads((artifact_dir / "numeric-magma-strata-d4-g1.json").read_text())
    assert d4["all_completed"] and len(d4["results"]) == 16
    for row in d4["results"]:
        assert row["ok"] and "kept=0" in row["stdout"]
        regression.append(Task(4, 1, int(row["e"]), None, "#1343 completed d4/g1 stratum"))

    d6 = json.loads((artifact_dir / "numeric-magma-strata-d6-g1.json").read_text())
    timeout_e = set(EXPECTED_UNRESOLVED)
    for row in d6["results"]:
        e = int(row["e"])
        if e not in timeout_e:
            assert row["ok"] and "kept=0" in row["stdout"]
            regression.append(Task(6, 1, e, None, "#1343 completed d6/g1 stratum"))

    residual: list[Task] = []
    for e, expected_unresolved in EXPECTED_UNRESOLVED.items():
        data = json.loads(
            (artifact_dir / f"numeric-magma-curvegroup-adaptive-d6-g1-e{e}.json").read_text()
        )
        assert data["unresolved"] == expected_unresolved
        assert data["kept_total"] == 0
        completed_a = set()
        for row in data["rows"]:
            assert row["kept"] == 0
            a = int(row["a"])
            completed_a.add(a)
            regression.append(Task(6, 1, e, a, "#1343 completed adaptive singleton"))
        assert completed_a | set(expected_unresolved) == set(range(data["expected_row_count"]))
        for a in expected_unresolved:
            residual.append(Task(6, 1, e, a, "#1343 unresolved calculator singleton"))
    return sorted(regression), sorted(residual)


def run_task(
    task: Task,
    core: pathlib.Path,
    output_dir: pathlib.Path,
    timeout: float,
    proof: bool,
) -> dict[str, Any]:
    checkpoint = output_dir / task.label / "checkpoint.json"
    if checkpoint.exists():
        prior = json.loads(checkpoint.read_text())
        if prior.get("complete") and prior.get("exact_survivor_count") == 0:
            prior["reused"] = True
            prior["result_file"] = str(checkpoint)
            return prior
    command = [
        sys.executable,
        str(pathlib.Path(__file__).with_name("run_exact_z3_budget.py")),
        "--core",
        str(core),
        "--output-dir",
        str(output_dir),
        "--degree",
        str(task.degree),
        "--genus",
        str(task.genus),
        "--threads",
        "1",
        "--timeout",
        str(timeout),
    ]
    if task.exceptional_mass is not None:
        command.extend(("--exceptional-mass", str(task.exceptional_mass)))
    if task.curve_group_mass is not None:
        command.extend(("--curve-group-mass", str(task.curve_group_mass)))
    if proof:
        command.append("--proof")
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode:
        if task.exceptional_mass is None or task.curve_group_mass is None:
            raise RuntimeError(
                f"{task.label} failed with {completed.returncode}\n"
                f"{completed.stdout}\n{completed.stderr}"
            )
        partition_command = [
            sys.executable,
            str(pathlib.Path(__file__).with_name("run_exact_z3_partition.py")),
            "--core",
            str(core),
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
            "1",
            "--timeout",
            str(timeout),
        ]
        if proof:
            partition_command.append("--proof")
        partitioned = subprocess.run(
            partition_command, capture_output=True, text=True, check=False
        )
        partition_path = output_dir / f"partition-{task.label}.json"
        if partitioned.returncode or not partition_path.exists():
            raise RuntimeError(
                f"{task.label} direct and partitioned searches failed\n"
                f"DIRECT:\n{completed.stdout}\n{completed.stderr}\n"
                f"PARTITION:\n{partitioned.stdout}\n{partitioned.stderr}"
            )
        parent = json.loads(partition_path.read_text())
        return {
            "complete": parent["all_complete"],
            "exact_survivor_count": parent["exact_survivor_count"],
            "deterministic_result_sha256": parent["deterministic_result_sha256"],
            "smt2_sha256": None,
            "proof_sha256": None,
            "elapsed_seconds": parent["wall_seconds"],
            "partitioned": True,
            "reused": False,
            "result_file": str(partition_path),
        }
    result = json.loads(checkpoint.read_text())
    result["reused"] = False
    result["partitioned"] = False
    result["result_file"] = str(checkpoint)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-dir", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument(
        "--scope", choices=("residual", "regression", "all"), default="residual"
    )
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=float, default=1800)
    parser.add_argument("--proof", action="store_true")
    args = parser.parse_args()
    artifact_hashes = lock_artifacts(args.artifact_dir)
    regression, residual = source_tasks(args.artifact_dir)
    if len(regression) != 600:
        raise SystemExit(f"expected 600 completed #1343 shards/rows, got {len(regression)}")
    if len(residual) != 28:
        raise SystemExit(f"expected 28 residual singletons, got {len(residual)}")
    tasks = residual if args.scope == "residual" else regression
    if args.scope == "all":
        tasks = sorted(regression + residual)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    results: dict[str, dict[str, Any]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(
                run_task,
                task,
                args.artifact_dir / "picard-core.json",
                args.output_dir,
                args.timeout,
                args.proof,
            ): task
            for task in tasks
        }
        for future in concurrent.futures.as_completed(futures):
            task = futures[future]
            result = future.result()
            if not result["complete"] or result["exact_survivor_count"] != 0:
                raise SystemExit(f"exact disagreement or incomplete shard: {task.label}")
            results[task.label] = result
            print(
                json.dumps(
                    {
                        "label": task.label,
                        "source": task.source,
                        "seconds": result["elapsed_seconds"],
                        "survivors": result["exact_survivor_count"],
                        "reused": result["reused"],
                    },
                    sort_keys=True,
                ),
                flush=True,
            )

    entries = []
    by_label = {task.label: task for task in tasks}
    for label in sorted(results):
        result = results[label]
        result_file = pathlib.Path(result["result_file"])
        entries.append(
            {
                "label": label,
                "source": by_label[label].source,
                "exact_survivor_count": result["exact_survivor_count"],
                "deterministic_result_sha256": result["deterministic_result_sha256"],
                "smt2_sha256": result["smt2_sha256"],
                "proof_sha256": result["proof_sha256"],
                "result_file_sha256": file_sha256(result_file),
                "partitioned": bool(result.get("partitioned", False)),
                "elapsed_seconds": result["elapsed_seconds"],
            }
        )
    manifest: dict[str, Any] = {
        "schema": "STAGE32_PR1343_EXACT_REGRESSION_MANIFEST_V1",
        "scope": args.scope,
        "source_pr": 1343,
        "source_runs": [32623143985, 32623610941, 32624596141],
        "source_artifact_hashes": artifact_hashes,
        "expected_completed_regression_count": len(regression),
        "expected_residual_singleton_count": len(residual),
        "executed_task_count": len(tasks),
        "all_complete": len(entries) == len(tasks),
        "exact_survivor_total": sum(entry["exact_survivor_count"] for entry in entries),
        "wall_seconds": round(time.perf_counter() - started, 6),
        "entries": entries,
        "full_d176_d192_numerical_orbit_census": False,
        "receiver_credit": False,
    }
    deterministic = json.loads(json.dumps(manifest))
    deterministic.pop("wall_seconds")
    for entry in deterministic["entries"]:
        entry.pop("elapsed_seconds")
        entry.pop("result_file_sha256")
    manifest["deterministic_manifest_sha256_without_this_field"] = canonical_sha256(deterministic)
    path = args.output_dir / f"manifest-{args.scope}.json"
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))


if __name__ == "__main__":
    main()
