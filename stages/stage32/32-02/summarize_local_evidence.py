#!/usr/bin/env python3
"""Hash and summarize a local Stage32-02 checkpoint tree without rerunning it."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
from typing import Any

from run_pr1343_regression import EXPECTED_UNRESOLVED


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


def checkpoint_label(e: int, a: int) -> str:
    return f"d6-g1-e{e}-a{a}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint-dir", type=pathlib.Path, required=True)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args()

    checkpoint_paths = sorted(args.checkpoint_dir.rglob("checkpoint.json"))
    checkpoints: list[tuple[pathlib.Path, dict[str, Any]]] = []
    for path in checkpoint_paths:
        checkpoints.append((path, json.loads(path.read_text(encoding="utf-8"))))

    file_entries = []
    for path in sorted(p for p in args.checkpoint_dir.rglob("*") if p.is_file()):
        relative = path.relative_to(args.checkpoint_dir).as_posix()
        file_entries.append(
            {"path": relative, "bytes": path.stat().st_size, "sha256": file_sha256(path)}
        )

    residuals = []
    for e, masses in EXPECTED_UNRESOLVED.items():
        for a in masses:
            label = checkpoint_label(e, a)
            direct_path = args.checkpoint_dir / label / "checkpoint.json"
            partition_path = args.checkpoint_dir / f"partition-{label}.json"
            direct = json.loads(direct_path.read_text()) if direct_path.exists() else None
            partition = json.loads(partition_path.read_text()) if partition_path.exists() else None
            if direct and direct.get("complete"):
                disposition = "CLOSED_DIRECT"
                exact_count = direct["exact_survivor_count"]
                result_hash = direct["deterministic_result_sha256"]
            elif partition and partition.get("all_complete"):
                disposition = "CLOSED_PARTITION"
                exact_count = partition["exact_survivor_count"]
                result_hash = partition["deterministic_result_sha256"]
            elif partition:
                disposition = "UNKNOWN_PARTITION_INCOMPLETE"
                exact_count = None
                result_hash = partition["deterministic_result_sha256"]
            else:
                disposition = "UNKNOWN_NOT_YET_PARTITIONED"
                exact_count = None
                result_hash = direct.get("deterministic_result_sha256") if direct else None
            residuals.append(
                {
                    "label": label,
                    "exceptional_mass": e,
                    "curve_group_mass": a,
                    "disposition": disposition,
                    "exact_survivor_count": exact_count,
                    "deterministic_result_sha256": result_hash,
                    "direct_checkpoint_file_sha256": (
                        file_sha256(direct_path) if direct_path.exists() else None
                    ),
                    "partition_manifest_file_sha256": (
                        file_sha256(partition_path) if partition_path.exists() else None
                    ),
                    "partition_wall_seconds": partition.get("wall_seconds") if partition else None,
                }
            )

    terminal_unknown = []
    for path, value in checkpoints:
        if value.get("complete") or value.get("curve_sixteenth_mass") is None:
            continue
        terminal_unknown.append(
            {
                "label": path.parent.name,
                "degree": value["degree"],
                "genus": value["genus"],
                "exceptional_mass": value["exceptional_mass"],
                "curve_group_mass": value["curve_group_mass"],
                "curve_quarter_mass": value["curve_quarter_mass"],
                "exceptional_half_mass": value["exceptional_half_mass"],
                "second_curve_quarter_mass": value["second_curve_quarter_mass"],
                "exceptional_quarter_mass": value["exceptional_quarter_mass"],
                "second_exceptional_quarter_mass": value[
                    "second_exceptional_quarter_mass"
                ],
                "curve_eighth_mass": value["curve_eighth_mass"],
                "curve_sixteenth_mass": value["curve_sixteenth_mass"],
                "solver_result": value["solver_result"],
                "unknown_reason": value["unknown_reason"],
                "elapsed_seconds": value["elapsed_seconds"],
                "smt2_sha256": value["smt2_sha256"],
                "checkpoint_file_sha256": file_sha256(path),
            }
        )

    complete = [value for _, value in checkpoints if value.get("complete")]
    payload: dict[str, Any] = {
        "schema": "STAGE32_02_LOCAL_EVIDENCE_V1",
        "source_pr": 1343,
        "source_runs": [32623143985, 32623610941, 32624596141],
        "checkpoint_inventory": {
            "file_count": len(file_entries),
            "total_bytes": sum(item["bytes"] for item in file_entries),
            "checkpoint_count": len(checkpoints),
            "complete_checkpoint_count": len(complete),
            "incomplete_checkpoint_count": len(checkpoints) - len(complete),
            "proof_file_count": sum(item["path"].endswith("/proof.sexpr") for item in file_entries),
            "problem_file_count": sum(item["path"].endswith("/problem.smt2") for item in file_entries),
            "file_hash_manifest_sha256": canonical_sha256(file_entries),
        },
        "completed_runtime_seconds": {
            "minimum": min(float(value["elapsed_seconds"]) for value in complete),
            "maximum": max(float(value["elapsed_seconds"]) for value in complete),
            "sum": round(sum(float(value["elapsed_seconds"]) for value in complete), 6),
        },
        "formerly_unresolved_residuals": residuals,
        "closed_residual_count": sum(
            item["disposition"].startswith("CLOSED") for item in residuals
        ),
        "terminal_unknown_count": len(terminal_unknown),
        "terminal_unknown": sorted(terminal_unknown, key=lambda item: item["label"]),
        "all_28_residuals_exactly_closed": False,
        "predecessor_regression_complete": False,
        "predecessor_regression_match": None,
        "stop_reason": (
            "The existing deterministic fallback retained terminal QF_NIA "
            "UNKNOWN(timeout) cells after 300 seconds; the user-directed stop rule applies."
        ),
        "receiver_credit": False,
        "full_d176_d192_numerical_orbit_census": False,
        "r29_lg2": "NOT_DISCHARGED",
        "r29_lg2_eff": "NOT_DISCHARGED",
        "r29_lg2_mb": "NOT_DISCHARGED",
        "g10_lowgenus_picard": "AMBER",
    }
    payload["canonical_sha256_without_this_field"] = canonical_sha256(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
