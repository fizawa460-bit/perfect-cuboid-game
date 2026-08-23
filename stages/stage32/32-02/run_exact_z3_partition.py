#!/usr/bin/env python3
"""Exact deterministic subdivision of a hard Stage32 (d,g,e,a) shard."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import pathlib
import subprocess
import sys
import time
from typing import Any


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def file_sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_child(
    args: argparse.Namespace,
    quarter_mass: int,
    exceptional_half_mass: int | None = None,
    second_curve_quarter_mass: int | None = None,
    exceptional_quarter_mass: int | None = None,
    second_exceptional_quarter_mass: int | None = None,
    curve_eighth_mass: int | None = None,
    curve_sixteenth_mass: int | None = None,
) -> dict[str, Any]:
    label = (
        f"d{args.degree}-g{args.genus}-e{args.exceptional_mass}"
        f"-a{args.curve_group_mass}-b{quarter_mass}"
    )
    if exceptional_half_mass is not None:
        label += f"-f{exceptional_half_mass}"
    if second_curve_quarter_mass is not None:
        label += f"-c{second_curve_quarter_mass}"
    if exceptional_quarter_mass is not None:
        label += f"-h{exceptional_quarter_mass}"
    if second_exceptional_quarter_mass is not None:
        label += f"-k{second_exceptional_quarter_mass}"
    if curve_eighth_mass is not None:
        label += f"-l{curve_eighth_mass}"
    if curve_sixteenth_mass is not None:
        label += f"-m{curve_sixteenth_mass}"
    checkpoint = args.output_dir / label / "checkpoint.json"
    if checkpoint.exists():
        prior = json.loads(checkpoint.read_text())
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
                "diagnostic": "existing descendant checkpoints supersede this timed-out parent",
            }
    command = [
        sys.executable,
        str(pathlib.Path(__file__).with_name("run_exact_z3_budget.py")),
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
    if exceptional_half_mass is not None:
        command.extend(("--exceptional-half-mass", str(exceptional_half_mass)))
    if second_curve_quarter_mass is not None:
        command.extend(("--second-curve-quarter-mass", str(second_curve_quarter_mass)))
    if exceptional_quarter_mass is not None:
        command.extend(("--exceptional-quarter-mass", str(exceptional_quarter_mass)))
    if second_exceptional_quarter_mass is not None:
        command.extend(
            ("--second-exceptional-quarter-mass", str(second_exceptional_quarter_mass))
        )
    if curve_eighth_mass is not None:
        command.extend(("--curve-eighth-mass", str(curve_eighth_mass)))
    if curve_sixteenth_mass is not None:
        command.extend(("--curve-sixteenth-mass", str(curve_sixteenth_mass)))
    if args.proof:
        command.append("--proof")
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode:
        failure = {
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
            "stdout": completed.stdout,
            "stderr": completed.stderr,
        }
        return failure
    return json.loads(checkpoint.read_text())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--degree", type=int, required=True)
    parser.add_argument("--genus", type=int, choices=(0, 1), required=True)
    parser.add_argument("--exceptional-mass", type=int, required=True)
    parser.add_argument("--curve-group-mass", type=int, required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=float, default=300)
    parser.add_argument("--proof", action="store_true")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    start = time.perf_counter()
    results: dict[int, dict[str, Any]] = {}
    quarter_masses = list(range(args.curve_group_mass + 1))
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(run_child, args, mass): mass for mass in quarter_masses}
        for future in concurrent.futures.as_completed(futures):
            mass = futures[future]
            result = future.result()
            results[mass] = result
            print(
                json.dumps(
                    {
                        "curve_quarter_mass": mass,
                        "complete": result.get("complete", False),
                        "survivors": result.get("exact_survivor_count"),
                        "seconds": result.get("elapsed_seconds"),
                    },
                    sort_keys=True,
                ),
                flush=True,
            )

    refined: dict[int, list[dict[str, Any]]] = {}
    incomplete_masses = [mass for mass in quarter_masses if not results[mass].get("complete")]
    if incomplete_masses and args.exceptional_mass > 0:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(run_child, args, mass, half): (mass, half)
                for mass in incomplete_masses
                for half in range(args.exceptional_mass + 1)
            }
            for future in concurrent.futures.as_completed(futures):
                mass, half = futures[future]
                result = future.result()
                refined.setdefault(mass, []).append(result)
                print(
                    json.dumps(
                        {
                            "curve_quarter_mass": mass,
                            "exceptional_half_mass": half,
                            "complete": result.get("complete", False),
                            "survivors": result.get("exact_survivor_count"),
                            "seconds": result.get("elapsed_seconds"),
                        },
                        sort_keys=True,
                    ),
                    flush=True,
                )

    deep_refined: dict[tuple[int, int], list[dict[str, Any]]] = {}
    incomplete_halves = [
        (mass, int(child["exceptional_half_mass"]))
        for mass, children in refined.items()
        for child in children
        if not child.get("complete") and "exceptional_half_mass" in child
    ]
    second_group_total = 19 * args.degree - 5 * args.exceptional_mass - args.curve_group_mass
    if incomplete_halves:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(run_child, args, mass, half, second): (mass, half, second)
                for mass, half in incomplete_halves
                for second in range(second_group_total + 1)
            }
            for future in concurrent.futures.as_completed(futures):
                mass, half, second = futures[future]
                result = future.result()
                deep_refined.setdefault((mass, half), []).append(result)
                print(
                    json.dumps(
                        {
                            "curve_quarter_mass": mass,
                            "exceptional_half_mass": half,
                            "second_curve_quarter_mass": second,
                            "complete": result.get("complete", False),
                            "survivors": result.get("exact_survivor_count"),
                            "seconds": result.get("elapsed_seconds"),
                        },
                        sort_keys=True,
                    ),
                    flush=True,
                )

    ultra_refined: dict[tuple[int, int, int], list[dict[str, Any]]] = {}
    incomplete_seconds = [
        (mass, half, int(grandchild["second_curve_quarter_mass"]))
        for (mass, half), grandchildren in deep_refined.items()
        for grandchild in grandchildren
        if not grandchild.get("complete")
        and "second_curve_quarter_mass" in grandchild
    ]
    if incomplete_seconds:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(run_child, args, mass, half, second, quarter): (
                    mass,
                    half,
                    second,
                    quarter,
                )
                for mass, half, second in incomplete_seconds
                for quarter in range(half + 1)
            }
            for future in concurrent.futures.as_completed(futures):
                mass, half, second, quarter = futures[future]
                result = future.result()
                ultra_refined.setdefault((mass, half, second), []).append(result)
                print(
                    json.dumps(
                        {
                            "curve_quarter_mass": mass,
                            "exceptional_half_mass": half,
                            "second_curve_quarter_mass": second,
                            "exceptional_quarter_mass": quarter,
                            "complete": result.get("complete", False),
                            "survivors": result.get("exact_survivor_count"),
                            "seconds": result.get("elapsed_seconds"),
                        },
                        sort_keys=True,
                    ),
                    flush=True,
                )

    hyper_refined: dict[tuple[int, int, int, int], list[dict[str, Any]]] = {}
    incomplete_quarters = [
        (mass, half, second, int(great["exceptional_quarter_mass"]))
        for (mass, half, second), greats in ultra_refined.items()
        for great in greats
        if not great.get("complete") and "exceptional_quarter_mass" in great
    ]
    if incomplete_quarters:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(run_child, args, mass, half, second, quarter, other): (
                    mass,
                    half,
                    second,
                    quarter,
                    other,
                )
                for mass, half, second, quarter in incomplete_quarters
                for other in range(args.exceptional_mass - half + 1)
            }
            for future in concurrent.futures.as_completed(futures):
                mass, half, second, quarter, other = futures[future]
                result = future.result()
                hyper_refined.setdefault((mass, half, second, quarter), []).append(result)
                print(
                    json.dumps(
                        {
                            "curve_quarter_mass": mass,
                            "exceptional_half_mass": half,
                            "second_curve_quarter_mass": second,
                            "exceptional_quarter_mass": quarter,
                            "second_exceptional_quarter_mass": other,
                            "complete": result.get("complete", False),
                            "survivors": result.get("exact_survivor_count"),
                            "seconds": result.get("elapsed_seconds"),
                        },
                        sort_keys=True,
                    ),
                    flush=True,
                )

    nano_refined: dict[tuple[int, int, int, int, int], list[dict[str, Any]]] = {}
    incomplete_other_quarters = [
        (
            mass,
            half,
            second,
            quarter,
            int(hyper["second_exceptional_quarter_mass"]),
        )
        for (mass, half, second, quarter), hypers in hyper_refined.items()
        for hyper in hypers
        if not hyper.get("complete")
        and "second_exceptional_quarter_mass" in hyper
    ]
    if incomplete_other_quarters:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(
                    run_child, args, mass, half, second, quarter, other, eighth
                ): (mass, half, second, quarter, other, eighth)
                for mass, half, second, quarter, other in incomplete_other_quarters
                for eighth in range(mass + 1)
            }
            for future in concurrent.futures.as_completed(futures):
                mass, half, second, quarter, other, eighth = futures[future]
                result = future.result()
                nano_refined.setdefault(
                    (mass, half, second, quarter, other), []
                ).append(result)
                print(
                    json.dumps(
                        {
                            "curve_quarter_mass": mass,
                            "exceptional_half_mass": half,
                            "second_curve_quarter_mass": second,
                            "exceptional_quarter_mass": quarter,
                            "second_exceptional_quarter_mass": other,
                            "curve_eighth_mass": eighth,
                            "complete": result.get("complete", False),
                            "survivors": result.get("exact_survivor_count"),
                            "seconds": result.get("elapsed_seconds"),
                        },
                        sort_keys=True,
                    ),
                    flush=True,
                )

    pico_refined: dict[tuple[int, int, int, int, int, int], list[dict[str, Any]]] = {}
    incomplete_eighths = [
        (
            mass,
            half,
            second,
            quarter,
            other,
            int(nano["curve_eighth_mass"]),
        )
        for (mass, half, second, quarter, other), nanos in nano_refined.items()
        for nano in nanos
        if not nano.get("complete") and "curve_eighth_mass" in nano
    ]
    if incomplete_eighths:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(
                    run_child,
                    args,
                    mass,
                    half,
                    second,
                    quarter,
                    other,
                    eighth,
                    sixteenth,
                ): (mass, half, second, quarter, other, eighth, sixteenth)
                for mass, half, second, quarter, other, eighth in incomplete_eighths
                for sixteenth in range(eighth + 1)
            }
            for future in concurrent.futures.as_completed(futures):
                mass, half, second, quarter, other, eighth, sixteenth = futures[future]
                result = future.result()
                pico_refined.setdefault(
                    (mass, half, second, quarter, other, eighth), []
                ).append(result)
                print(
                    json.dumps(
                        {
                            "curve_quarter_mass": mass,
                            "exceptional_half_mass": half,
                            "second_curve_quarter_mass": second,
                            "exceptional_quarter_mass": quarter,
                            "second_exceptional_quarter_mass": other,
                            "curve_eighth_mass": eighth,
                            "curve_sixteenth_mass": sixteenth,
                            "complete": result.get("complete", False),
                            "survivors": result.get("exact_survivor_count"),
                            "seconds": result.get("elapsed_seconds"),
                        },
                        sort_keys=True,
                    ),
                    flush=True,
                )

    entries = []
    all_complete = True
    survivor_total = 0
    for mass in quarter_masses:
        result = results[mass]
        complete = bool(result.get("complete"))
        if complete:
            survivor_total += int(result["exact_survivor_count"])
            label = (
                f"d{args.degree}-g{args.genus}-e{args.exceptional_mass}"
                f"-a{args.curve_group_mass}-b{mass}"
            )
            checkpoint = args.output_dir / label / "checkpoint.json"
            entries.append(
                {
                    "curve_quarter_mass": mass,
                    "exact_survivor_count": result["exact_survivor_count"],
                    "deterministic_result_sha256": result["deterministic_result_sha256"],
                    "smt2_sha256": result["smt2_sha256"],
                    "proof_sha256": result["proof_sha256"],
                    "checkpoint_file_sha256": file_sha256(checkpoint),
                    "elapsed_seconds": result["elapsed_seconds"],
                }
            )
        elif mass in refined:
            children = sorted(refined[mass], key=lambda child: child["exceptional_half_mass"])
            child_entries = []
            child_total = 0
            children_complete = True
            for child in children:
                half = int(child["exceptional_half_mass"])
                if child.get("complete"):
                    child_total += int(child["exact_survivor_count"])
                    child_entries.append(
                        {
                            "exceptional_half_mass": half,
                            "exact_survivor_count": child["exact_survivor_count"],
                            "deterministic_result_sha256": child["deterministic_result_sha256"],
                            "smt2_sha256": child["smt2_sha256"],
                            "proof_sha256": child["proof_sha256"],
                            "elapsed_seconds": child["elapsed_seconds"],
                        }
                    )
                    continue
                grandchildren = sorted(
                    deep_refined.get((mass, half), []),
                    key=lambda grandchild: grandchild["second_curve_quarter_mass"],
                )
                grand_entries = []
                grand_total = 0
                grand_complete = len(grandchildren) == second_group_total + 1
                for grandchild in grandchildren:
                    second = int(grandchild["second_curve_quarter_mass"])
                    if grandchild.get("complete"):
                        grand_total += int(grandchild["exact_survivor_count"])
                        grand_entries.append(
                            {
                                "second_curve_quarter_mass": second,
                                "exact_survivor_count": grandchild["exact_survivor_count"],
                                "deterministic_result_sha256": grandchild[
                                    "deterministic_result_sha256"
                                ],
                                "smt2_sha256": grandchild["smt2_sha256"],
                                "proof_sha256": grandchild["proof_sha256"],
                                "elapsed_seconds": grandchild["elapsed_seconds"],
                            }
                        )
                        continue
                    great_grandchildren = sorted(
                        ultra_refined.get((mass, half, second), []),
                        key=lambda great: great["exceptional_quarter_mass"],
                    )
                    great_complete = len(great_grandchildren) == half + 1
                    great_entries = []
                    great_total = 0
                    second_exceptional_half = args.exceptional_mass - half
                    for great in great_grandchildren:
                        quarter = int(great["exceptional_quarter_mass"])
                        if great.get("complete"):
                            great_total += int(great["exact_survivor_count"])
                            great_entries.append(
                                {
                                    "exceptional_quarter_mass": quarter,
                                    "exact_survivor_count": great["exact_survivor_count"],
                                    "deterministic_result_sha256": great[
                                        "deterministic_result_sha256"
                                    ],
                                    "smt2_sha256": great["smt2_sha256"],
                                    "proof_sha256": great["proof_sha256"],
                                    "elapsed_seconds": great["elapsed_seconds"],
                                }
                            )
                            continue
                        hyper_children = sorted(
                            hyper_refined.get((mass, half, second, quarter), []),
                            key=lambda hyper: hyper[
                                "second_exceptional_quarter_mass"
                            ],
                        )
                        hyper_complete = len(hyper_children) == second_exceptional_half + 1
                        hyper_entries = []
                        hyper_total = 0
                        for hyper in hyper_children:
                            other = int(hyper["second_exceptional_quarter_mass"])
                            if hyper.get("complete"):
                                hyper_total += int(hyper["exact_survivor_count"])
                                hyper_entries.append(
                                    {
                                        "second_exceptional_quarter_mass": other,
                                        "exact_survivor_count": hyper[
                                            "exact_survivor_count"
                                        ],
                                        "deterministic_result_sha256": hyper[
                                            "deterministic_result_sha256"
                                        ],
                                        "smt2_sha256": hyper["smt2_sha256"],
                                        "proof_sha256": hyper["proof_sha256"],
                                        "elapsed_seconds": hyper["elapsed_seconds"],
                                    }
                                )
                                continue
                            nano_children = sorted(
                                nano_refined.get(
                                    (mass, half, second, quarter, other), []
                                ),
                                key=lambda nano: nano["curve_eighth_mass"],
                            )
                            nano_complete = len(nano_children) == mass + 1
                            nano_entries = []
                            nano_total = 0
                            for nano in nano_children:
                                eighth = int(nano["curve_eighth_mass"])
                                if nano.get("complete"):
                                    nano_total += int(nano["exact_survivor_count"])
                                    nano_entries.append(
                                        {
                                            "curve_eighth_mass": eighth,
                                            "exact_survivor_count": nano[
                                                "exact_survivor_count"
                                            ],
                                            "deterministic_result_sha256": nano[
                                                "deterministic_result_sha256"
                                            ],
                                            "smt2_sha256": nano["smt2_sha256"],
                                            "proof_sha256": nano["proof_sha256"],
                                            "elapsed_seconds": nano["elapsed_seconds"],
                                        }
                                    )
                                    continue
                                pico_children = sorted(
                                    pico_refined.get(
                                        (mass, half, second, quarter, other, eighth), []
                                    ),
                                    key=lambda pico: pico["curve_sixteenth_mass"],
                                )
                                pico_complete = (
                                    len(pico_children) == eighth + 1
                                    and all(pico.get("complete") for pico in pico_children)
                                )
                                if not pico_complete:
                                    nano_complete = False
                                    nano_entries.append(
                                        {
                                            "curve_eighth_mass": eighth,
                                            "complete": False,
                                            "diagnostic": nano,
                                        }
                                    )
                                    continue
                                pico_total = sum(
                                    int(pico["exact_survivor_count"])
                                    for pico in pico_children
                                )
                                nano_total += pico_total
                                nano_entries.append(
                                    {
                                        "curve_eighth_mass": eighth,
                                        "refinement": "nonexceptional intersections 1..5 sum",
                                        "partition_values": list(range(eighth + 1)),
                                        "exact_survivor_count": pico_total,
                                        "children": [
                                            {
                                                "curve_sixteenth_mass": pico[
                                                    "curve_sixteenth_mass"
                                                ],
                                                "exact_survivor_count": pico[
                                                    "exact_survivor_count"
                                                ],
                                                "deterministic_result_sha256": pico[
                                                    "deterministic_result_sha256"
                                                ],
                                                "smt2_sha256": pico["smt2_sha256"],
                                                "proof_sha256": pico["proof_sha256"],
                                                "elapsed_seconds": pico[
                                                    "elapsed_seconds"
                                                ],
                                            }
                                            for pico in pico_children
                                        ],
                                    }
                                )
                            if not nano_complete:
                                hyper_complete = False
                                hyper_entries.append(
                                    {
                                        "second_exceptional_quarter_mass": other,
                                        "complete": False,
                                        "children": nano_entries,
                                    }
                                )
                                continue
                            hyper_total += nano_total
                            hyper_entries.append(
                                {
                                    "second_exceptional_quarter_mass": other,
                                    "refinement": "nonexceptional intersections 1..11 sum",
                                    "partition_values": list(range(mass + 1)),
                                    "exact_survivor_count": nano_total,
                                    "children": nano_entries,
                                }
                            )
                        if not hyper_complete:
                            great_complete = False
                            great_entries.append(
                                {
                                    "exceptional_quarter_mass": quarter,
                                    "complete": False,
                                    "children": hyper_entries,
                                }
                            )
                            continue
                        great_total += hyper_total
                        great_entries.append(
                            {
                                "exceptional_quarter_mass": quarter,
                                "refinement": "exceptional intersections 25..36 sum",
                                "partition_values": list(
                                    range(second_exceptional_half + 1)
                                ),
                                "exact_survivor_count": hyper_total,
                                "children": hyper_entries,
                            }
                        )
                    if not great_complete:
                        grand_complete = False
                        grand_entries.append(
                            {
                                "second_curve_quarter_mass": second,
                                "complete": False,
                                "children": great_entries,
                            }
                        )
                        continue
                    grand_total += great_total
                    grand_entries.append(
                        {
                            "second_curve_quarter_mass": second,
                            "refinement": "exceptional intersections 1..12 sum",
                            "partition_values": list(range(half + 1)),
                            "exact_survivor_count": great_total,
                            "children": great_entries,
                        }
                    )
                if not grand_complete:
                    children_complete = False
                    child_entries.append(
                        {
                            "exceptional_half_mass": half,
                            "complete": False,
                            "children": grand_entries,
                        }
                    )
                    continue
                child_total += grand_total
                child_entries.append(
                    {
                        "exceptional_half_mass": half,
                        "refinement": "second curve group classes 47..69 sum",
                        "partition_values": list(range(second_group_total + 1)),
                        "exact_survivor_count": grand_total,
                        "children": grand_entries,
                    }
                )
            if not children_complete:
                all_complete = False
                entries.append(
                    {
                        "curve_quarter_mass": mass,
                        "complete": False,
                        "children": child_entries,
                    }
                )
                continue
            survivor_total += child_total
            entries.append(
                {
                    "curve_quarter_mass": mass,
                    "refinement": "exceptional intersections 1..24 sum",
                    "partition_values": list(range(args.exceptional_mass + 1)),
                    "exact_survivor_count": child_total,
                    "children": child_entries,
                }
            )
        else:
            all_complete = False
            entries.append(
                {
                    "curve_quarter_mass": mass,
                    "complete": False,
                    "diagnostic": result,
                }
            )
    parent: dict[str, Any] = {
        "schema": "STAGE32_EXACT_Z3_PARTITION_V1",
        "partition": "sum of intersections with known nonexceptional classes 1..23",
        "degree": args.degree,
        "genus": args.genus,
        "exceptional_mass": args.exceptional_mass,
        "curve_group_mass": args.curve_group_mass,
        "partition_values": quarter_masses,
        "all_complete": all_complete,
        "exact_survivor_count": survivor_total if all_complete else None,
        "wall_seconds": round(time.perf_counter() - start, 6),
        "entries": entries,
        "floating_point_feasibility_credit": False,
    }
    deterministic = json.loads(json.dumps(parent))
    deterministic.pop("wall_seconds")
    for entry in deterministic["entries"]:
        entry.pop("elapsed_seconds", None)
        entry.pop("checkpoint_file_sha256", None)
        for child in entry.get("children", []):
            child.pop("elapsed_seconds", None)
            for grandchild in child.get("children", []):
                grandchild.pop("elapsed_seconds", None)
                for great_grandchild in grandchild.get("children", []):
                    great_grandchild.pop("elapsed_seconds", None)
                    for hyper_child in great_grandchild.get("children", []):
                        hyper_child.pop("elapsed_seconds", None)
                        for nano_child in hyper_child.get("children", []):
                            nano_child.pop("elapsed_seconds", None)
                            for pico_child in nano_child.get("children", []):
                                pico_child.pop("elapsed_seconds", None)
    parent["deterministic_result_sha256"] = canonical_sha256(deterministic)
    label = (
        f"d{args.degree}-g{args.genus}-e{args.exceptional_mass}"
        f"-a{args.curve_group_mass}"
    )
    path = args.output_dir / f"partition-{label}.json"
    path.write_text(json.dumps(parent, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(parent, sort_keys=True))
    if not all_complete:
        raise SystemExit("exact partition exposed unresolved child shards")


if __name__ == "__main__":
    main()
