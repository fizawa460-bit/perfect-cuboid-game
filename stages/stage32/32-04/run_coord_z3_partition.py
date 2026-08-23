#!/usr/bin/env python3
"""Reuse the audited Stage32-02 deterministic partition tree with bounded
intersection-coordinate QF_NIA leaves and an exact affine-lattice terminal
fallback.

The partition order/ranges/aggregation are inherited unchanged.  The normal
leaf backend is run_intersection_coord_budget.py.  Only a fully specified
terminal (b,f,c,h,k,l,m) leaf that remains UNKNOWN(timeout) is handed to the
audited Stage32-03 HNF/Gram-LLL/Fincke--Pohst exact enumerator.  No parent or
intermediate node receives affine credit.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import pathlib
import shutil
import subprocess
import sys
import threading
import time
from typing import Any

CAP_CERTIFICATE: pathlib.Path | None = None
AFFINE_MODULE: Any = None
AFFINE_CONTEXT: Any = None
AFFINE_LOCK = threading.Lock()


def load_module(path: pathlib.Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_predecessor() -> Any:
    path = pathlib.Path(__file__).resolve().parents[1] / "32-02" / "run_exact_z3_partition.py"
    return load_module(path, "stage32_02_partition_coord")


def ensure_affine_context(core_path: pathlib.Path) -> tuple[Any, Any]:
    global AFFINE_MODULE, AFFINE_CONTEXT
    with AFFINE_LOCK:
        if AFFINE_MODULE is None:
            path = pathlib.Path(__file__).resolve().parents[1] / "32-03" / "affine_lattice.py"
            AFFINE_MODULE = load_module(path, "stage32_03_affine_terminal")
        if AFFINE_CONTEXT is None:
            AFFINE_CONTEXT = AFFINE_MODULE.build_context(core_path)
    return AFFINE_MODULE, AFFINE_CONTEXT


def terminal_affine_completion(
    args: argparse.Namespace,
    checkpoint: pathlib.Path,
    label: str,
    quarter_mass: int,
    exceptional_half_mass: int,
    second_curve_quarter_mass: int,
    exceptional_quarter_mass: int,
    second_exceptional_quarter_mass: int,
    curve_eighth_mass: int,
    curve_sixteenth_mass: int,
) -> dict[str, Any]:
    """Replace a terminal coordinate UNKNOWN with an exact affine result.

    The timed-out coordinate checkpoint is preserved byte-for-byte beside the
    replacement checkpoint.  The replacement records hashes of both that input
    and the standalone affine checkpoint so an audit can recompute either path.
    """
    source = json.loads(checkpoint.read_text(encoding="utf-8"))
    if source.get("complete"):
        return source
    assert source.get("solver_result") == "unknown"
    assert source.get("unknown_reason") == "timeout"

    coord_backup = checkpoint.with_name("coord-timeout-checkpoint.json")
    if not coord_backup.exists():
        shutil.copyfile(checkpoint, coord_backup)

    affine, context = ensure_affine_context(args.core.resolve())
    cell = {
        "label": label,
        "degree": int(args.degree),
        "genus": int(args.genus),
        "exceptional_mass": int(args.exceptional_mass),
        "curve_group_mass": int(args.curve_group_mass),
        "curve_quarter_mass": int(quarter_mass),
        "exceptional_half_mass": int(exceptional_half_mass),
        "second_curve_quarter_mass": int(second_curve_quarter_mass),
        "exceptional_quarter_mass": int(exceptional_quarter_mass),
        "second_exceptional_quarter_mass": int(second_exceptional_quarter_mass),
        "curve_eighth_mass": int(curve_eighth_mass),
        "curve_sixteenth_mass": int(curve_sixteenth_mass),
        "checkpoint_file_sha256": affine.file_sha256(coord_backup),
        "smt2_sha256": source.get("smt2_sha256"),
    }

    target = affine.cell_target(cell)
    image_coordinates = context.image_basis.inv() * target
    image_feasible = all(value.q == 1 for value in image_coordinates)
    started = time.perf_counter()
    if image_feasible:
        affine_payload = affine.solve_cell(context, cell)
    else:
        deterministic = {
            "schema": "STAGE32_AFFINE_HNF_IMAGE_REJECTION_V1",
            "algorithm_id": affine.ALGORITHM_ID,
            "label": label,
            "budget": {key: int(cell[key]) for key in affine.BUDGET_KEYS},
            "genus": int(args.genus),
            "core_file_sha256": context.core_hashes["file_sha256"],
            "core_canonical_sha256": context.core_hashes["canonical_sha256"],
            "common_certificate_sha256": context.common_certificate[
                "canonical_sha256_without_this_field"
            ],
            "hnf_image_feasible": False,
            "hnf_image_coordinates": [str(value) for value in image_coordinates],
            "solver_result": "UNSAT_HNF_IMAGE",
            "complete": True,
            "unknown_reason": None,
            "exact_survivor_count": 0,
            "survivors": [],
            "floating_point_feasibility_credit": False,
        }
        affine_payload = dict(deterministic)
        affine_payload["elapsed_seconds"] = round(time.perf_counter() - started, 6)
        affine_payload["deterministic_result_sha256"] = affine.canonical_sha256(deterministic)
        affine_payload["checkpoint_sha256_without_this_field"] = affine.canonical_sha256(
            affine_payload
        )

    affine_checkpoint = checkpoint.with_name("affine-checkpoint.json")
    affine.atomic_json(affine_checkpoint, affine_payload)
    assert affine_payload["complete"] is True
    assert affine_payload["unknown_reason"] is None

    deterministic = {
        "schema": "STAGE32_COORD_AFFINE_TERMINAL_COMPLETION_V1",
        "algorithm_id": "COORD_PARTITION_TO_HNF_KERNEL_EXACT_GRAM_LLL_FP140_V1",
        "label": label,
        "degree": int(args.degree),
        "genus": int(args.genus),
        "exceptional_mass": int(args.exceptional_mass),
        "curve_group_mass": int(args.curve_group_mass),
        "curve_quarter_mass": int(quarter_mass),
        "exceptional_half_mass": int(exceptional_half_mass),
        "second_curve_quarter_mass": int(second_curve_quarter_mass),
        "exceptional_quarter_mass": int(exceptional_quarter_mass),
        "second_exceptional_quarter_mass": int(second_exceptional_quarter_mass),
        "curve_eighth_mass": int(curve_eighth_mass),
        "curve_sixteenth_mass": int(curve_sixteenth_mass),
        "method": "AFFINE_LATTICE_TERMINAL_FALLBACK",
        "complete": True,
        "solver_result": affine_payload["solver_result"],
        "unknown_reason": None,
        "exact_survivor_count": int(affine_payload["exact_survivor_count"]),
        "survivors": affine_payload.get("survivors", []),
        "source_coord_checkpoint_file_sha256": affine.file_sha256(coord_backup),
        "source_coord_deterministic_result_sha256": source[
            "deterministic_result_sha256"
        ],
        "smt2_sha256": source["smt2_sha256"],
        "proof_sha256": None,
        "affine_checkpoint_file_sha256": affine.file_sha256(affine_checkpoint),
        "affine_checkpoint_canonical_sha256": affine_payload[
            "checkpoint_sha256_without_this_field"
        ],
        "affine_deterministic_result_sha256": affine_payload[
            "deterministic_result_sha256"
        ],
        "affine_algorithm_id": affine_payload["algorithm_id"],
        "hnf_image_feasible": bool(affine_payload["hnf_image_feasible"]),
        "cap_certificate_file_sha256": affine.file_sha256(CAP_CERTIFICATE),
        "all_140_nonnegative_intersections_used_by_affine": bool(
            affine_payload.get("all_140_intersection_constraints_used", False)
            or not affine_payload["hnf_image_feasible"]
        ),
        "floating_point_feasibility_credit": False,
        "receiver_credit": False,
    }
    payload = dict(deterministic)
    payload["elapsed_seconds"] = round(
        float(source.get("elapsed_seconds", 0.0))
        + float(affine_payload.get("elapsed_seconds", 0.0)),
        6,
    )
    payload["deterministic_result_sha256"] = affine.canonical_sha256(deterministic)
    payload["checkpoint_sha256_without_this_field"] = affine.canonical_sha256(payload)
    affine.atomic_json(checkpoint, payload)
    return payload


def coord_run_child(
    args: argparse.Namespace,
    quarter_mass: int,
    exceptional_half_mass: int | None = None,
    second_curve_quarter_mass: int | None = None,
    exceptional_quarter_mass: int | None = None,
    second_exceptional_quarter_mass: int | None = None,
    curve_eighth_mass: int | None = None,
    curve_sixteenth_mass: int | None = None,
) -> dict[str, Any]:
    assert CAP_CERTIFICATE is not None
    label = (
        f"d{args.degree}-g{args.genus}-e{args.exceptional_mass}"
        f"-a{args.curve_group_mass}-b{quarter_mass}"
    )
    optional = (
        ("f", "--exceptional-half-mass", exceptional_half_mass),
        ("c", "--second-curve-quarter-mass", second_curve_quarter_mass),
        ("h", "--exceptional-quarter-mass", exceptional_quarter_mass),
        ("k", "--second-exceptional-quarter-mass", second_exceptional_quarter_mass),
        ("l", "--curve-eighth-mass", curve_eighth_mass),
        ("m", "--curve-sixteenth-mass", curve_sixteenth_mass),
    )
    for prefix, _, value in optional:
        if value is not None:
            label += f"-{prefix}{value}"
    checkpoint = args.output_dir / label / "checkpoint.json"
    if checkpoint.exists():
        prior = json.loads(checkpoint.read_text(encoding="utf-8"))
        if prior.get("complete"):
            return prior
        if curve_sixteenth_mass is not None:
            assert None not in (
                exceptional_half_mass,
                second_curve_quarter_mass,
                exceptional_quarter_mass,
                second_exceptional_quarter_mass,
                curve_eighth_mass,
            )
            return terminal_affine_completion(
                args,
                checkpoint,
                label,
                quarter_mass,
                int(exceptional_half_mass),
                int(second_curve_quarter_mass),
                int(exceptional_quarter_mass),
                int(second_exceptional_quarter_mass),
                int(curve_eighth_mass),
                int(curve_sixteenth_mass),
            )
        if any(args.output_dir.glob(f"{label}-*/checkpoint.json")):
            return {
                "complete": False,
                "label": label,
                "curve_quarter_mass": quarter_mass,
                "exceptional_half_mass": exceptional_half_mass,
                "second_curve_quarter_mass": second_curve_quarter_mass,
                "exceptional_quarter_mass": exceptional_quarter_mass,
                "second_exceptional_quarter_mass": second_exceptional_quarter_mass,
                "curve_eighth_mass": curve_eighth_mass,
                "curve_sixteenth_mass": curve_sixteenth_mass,
                "diagnostic": "existing descendant checkpoints supersede timed-out parent",
            }

    command = [
        sys.executable,
        str(pathlib.Path(__file__).with_name("run_intersection_coord_budget.py")),
        "--core", str(args.core),
        "--cap-certificate", str(CAP_CERTIFICATE),
        "--output-dir", str(args.output_dir),
        "--degree", str(args.degree),
        "--genus", str(args.genus),
        "--exceptional-mass", str(args.exceptional_mass),
        "--curve-group-mass", str(args.curve_group_mass),
        "--curve-quarter-mass", str(quarter_mass),
        "--timeout", str(args.timeout),
    ]
    for _, option, value in optional:
        if value is not None:
            command.extend((option, str(value)))
    if args.proof:
        command.append("--proof")
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if checkpoint.exists():
        result = json.loads(checkpoint.read_text(encoding="utf-8"))
        if not result.get("complete") and curve_sixteenth_mass is not None:
            assert None not in (
                exceptional_half_mass,
                second_curve_quarter_mass,
                exceptional_quarter_mass,
                second_exceptional_quarter_mass,
                curve_eighth_mass,
            )
            return terminal_affine_completion(
                args,
                checkpoint,
                label,
                quarter_mass,
                int(exceptional_half_mass),
                int(second_curve_quarter_mass),
                int(exceptional_quarter_mass),
                int(second_exceptional_quarter_mass),
                int(curve_eighth_mass),
                int(curve_sixteenth_mass),
            )
        return result
    return {
        "complete": False,
        "label": label,
        "curve_quarter_mass": quarter_mass,
        "exceptional_half_mass": exceptional_half_mass,
        "second_curve_quarter_mass": second_curve_quarter_mass,
        "exceptional_quarter_mass": exceptional_quarter_mass,
        "second_exceptional_quarter_mass": second_exceptional_quarter_mass,
        "curve_eighth_mass": curve_eighth_mass,
        "curve_sixteenth_mass": curve_sixteenth_mass,
        "returncode": completed.returncode,
        "stdout": completed.stdout[-4000:],
        "stderr": completed.stderr[-4000:],
    }


def main() -> None:
    global CAP_CERTIFICATE
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    own, remaining = parser.parse_known_args()
    CAP_CERTIFICATE = own.cap_certificate.resolve()
    if not CAP_CERTIFICATE.exists():
        raise SystemExit("missing exact dual-cap certificate")
    predecessor = load_predecessor()
    predecessor.run_child = coord_run_child
    sys.argv = [sys.argv[0], *remaining]
    predecessor.main()


if __name__ == "__main__":
    main()
