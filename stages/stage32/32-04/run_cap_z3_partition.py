#!/usr/bin/env python3
"""Reuse the audited Stage32-02 deterministic partition tree with verified caps.

Only the child backend is replaced: every leaf is sent through
run_cap_z3_budget.py with an already exact-verified dual-cap certificate.
The predecessor partition aggregation/order/ranges are otherwise reused.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import pathlib
import subprocess
import sys
from typing import Any

CAP_CERTIFICATE: pathlib.Path | None = None


def load_predecessor() -> Any:
    path = pathlib.Path(__file__).resolve().parents[1] / "32-02" / "run_exact_z3_partition.py"
    spec = importlib.util.spec_from_file_location("stage32_02_partition", path)
    if spec is None or spec.loader is None:
        raise SystemExit("cannot load Stage32-02 partition backend")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def capped_run_child(
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
        ("f", exceptional_half_mass),
        ("c", second_curve_quarter_mass),
        ("h", exceptional_quarter_mass),
        ("k", second_exceptional_quarter_mass),
        ("l", curve_eighth_mass),
        ("m", curve_sixteenth_mass),
    )
    for prefix, value in optional:
        if value is not None:
            label += f"-{prefix}{value}"

    checkpoint = args.output_dir / label / "checkpoint.json"
    if checkpoint.exists():
        prior = json.loads(checkpoint.read_text(encoding="utf-8"))
        if prior.get("complete"):
            return prior
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
                "diagnostic": "existing descendant checkpoints supersede this timed-out parent",
            }

    wrapper = pathlib.Path(__file__).with_name("run_cap_z3_budget.py")
    command = [
        sys.executable,
        str(wrapper),
        "--cap-certificate",
        str(CAP_CERTIFICATE),
        "--core",
        str(args.core),
        "--output-dir",
        str(args.output_dir),
        "--degree",
        str(args.degree),
        "--genus",
        str(args.genus),
        "--exceptional-mass",
        str(args.exceptional_mass),
        "--curve-group-mass",
        str(args.curve_group_mass),
        "--curve-quarter-mass",
        str(quarter_mass),
        "--threads",
        "1",
        "--timeout",
        str(args.timeout),
    ]
    option_names = (
        ("--exceptional-half-mass", exceptional_half_mass),
        ("--second-curve-quarter-mass", second_curve_quarter_mass),
        ("--exceptional-quarter-mass", exceptional_quarter_mass),
        ("--second-exceptional-quarter-mass", second_exceptional_quarter_mass),
        ("--curve-eighth-mass", curve_eighth_mass),
        ("--curve-sixteenth-mass", curve_sixteenth_mass),
    )
    for name, value in option_names:
        if value is not None:
            command.extend((name, str(value)))
    if args.proof:
        command.append("--proof")

    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if checkpoint.exists():
        return json.loads(checkpoint.read_text(encoding="utf-8"))
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
        raise SystemExit("missing exact cap certificate")

    predecessor = load_predecessor()
    predecessor.run_child = capped_run_child
    sys.argv = [sys.argv[0], *remaining]
    predecessor.main()


if __name__ == "__main__":
    main()
