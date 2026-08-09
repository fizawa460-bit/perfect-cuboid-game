#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gc
import importlib.util
import json
import statistics
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
A5_PATH = ROOT / "stages/stage14/scripts/14-num-alpha5/safe_primitive_sieve_audit.py"
NUM3_PATH = ROOT / "stages/stage14/scripts/14-num3/extended_exact_census.py"
DEFAULT_BOUNDS = (200_000, 500_000, 1_000_000, 2_000_000)
DEFAULT_REPEATS = 3


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


A5 = load_module("stage14_num_alpha5", A5_PATH)
NUM3 = load_module("stage14_num3", NUM3_PATH)


def run_alpha(bound: int):
    t0 = time.perf_counter()
    objects, profile = A5.stream_pruned(bound)
    summary = NUM3.summarize(objects)
    wall = time.perf_counter() - t0
    return objects, summary, profile, wall


def run_ordinary(bound: int):
    t0 = time.perf_counter()
    objects, index_profile, kernel_profile = NUM3.enumerate_chunk(bound, 0, 1)
    summary = NUM3.summarize(objects)
    wall = time.perf_counter() - t0
    return objects, summary, {"index": index_profile, "kernel": kernel_profile}, wall


def summaries_equal(a, b):
    return a == b


def bench_bound(bound: int, repeats: int):
    trials = []
    alpha_times = []
    ordinary_times = []
    reference_objects = None
    reference_summary = None

    for r in range(repeats):
        order = ("alpha", "ordinary") if r % 2 == 0 else ("ordinary", "alpha")
        run_data = {}
        for engine in order:
            gc.collect()
            if engine == "alpha":
                objects, summary, profile, wall = run_alpha(bound)
            else:
                objects, summary, profile, wall = run_ordinary(bound)
            run_data[engine] = {
                "objects": objects,
                "summary": summary,
                "profile": profile,
                "wall_seconds": wall,
            }

        alpha = run_data["alpha"]
        ordinary = run_data["ordinary"]
        if alpha["objects"] != ordinary["objects"]:
            raise ArithmeticError(
                f"alpha/ordinary object-set mismatch B={bound} repeat={r}; "
                f"missing={sorted(ordinary['objects']-alpha['objects'])[:5]} "
                f"extra={sorted(alpha['objects']-ordinary['objects'])[:5]}"
            )
        if not summaries_equal(alpha["summary"], ordinary["summary"]):
            raise ArithmeticError(f"alpha/ordinary summary mismatch B={bound} repeat={r}")
        if reference_objects is None:
            reference_objects = set(alpha["objects"])
            reference_summary = alpha["summary"]
        elif alpha["objects"] != reference_objects or alpha["summary"] != reference_summary:
            raise ArithmeticError(f"non-deterministic alpha result B={bound} repeat={r}")

        alpha_times.append(alpha["wall_seconds"])
        ordinary_times.append(ordinary["wall_seconds"])
        trials.append({
            "repeat": r + 1,
            "order": list(order),
            "alpha_wall_seconds": alpha["wall_seconds"],
            "ordinary_wall_seconds": ordinary["wall_seconds"],
            "speedup_ordinary_over_alpha": ordinary["wall_seconds"] / max(alpha["wall_seconds"], 1e-12),
            "objects_equal": True,
            "summaries_equal": True,
        })

    alpha_median = statistics.median(alpha_times)
    ordinary_median = statistics.median(ordinary_times)
    speedup = ordinary_median / max(alpha_median, 1e-12)
    return {
        "bound": bound,
        "objects": len(reference_objects or ()),
        "summary": reference_summary,
        "repeats": repeats,
        "trials": trials,
        "alpha_wall_seconds": {
            "samples": alpha_times,
            "median": alpha_median,
            "min": min(alpha_times),
            "max": max(alpha_times),
        },
        "ordinary_wall_seconds": {
            "samples": ordinary_times,
            "median": ordinary_median,
            "min": min(ordinary_times),
            "max": max(ordinary_times),
        },
        "median_speedup_ordinary_over_alpha": speedup,
        "alpha_at_least_20pct_faster": speedup >= 1.25,
        "exact_object_sets_equal_every_repeat": True,
    }


def choose_crossover(rows):
    # Formal crossover: first tested bound starting a run of at least two
    # consecutive bounds with >=1.25x ordinary/alpha speedup, and the largest
    # tested bound must also satisfy the threshold.
    flags = [row["median_speedup_ordinary_over_alpha"] >= 1.25 for row in rows]
    largest_ok = bool(flags and flags[-1])
    first = None
    for i in range(len(flags) - 1):
        if flags[i] and flags[i + 1]:
            first = rows[i]["bound"]
            break
    return first if largest_ok else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bounds", nargs="*", type=int, default=list(DEFAULT_BOUNDS))
    ap.add_argument("--repeats", type=int, default=DEFAULT_REPEATS)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    bounds = sorted(dict.fromkeys(args.bounds))
    if args.repeats < 3:
        raise SystemExit("alpha7 requires at least 3 repeats")

    rows = [bench_bound(B, args.repeats) for B in bounds]
    crossover = choose_crossover(rows)
    largest = rows[-1]
    meaningful = crossover is not None
    report = {
        "stage": "14-num-alpha7",
        "classification": "FINITE_EXACT_MATCHED_END_TO_END_CROSSOVER_BENCHMARK",
        "benchmark_contract": {
            "same_process_python": True,
            "same_runner": True,
            "same_cutoff": True,
            "same_complete_object_output": True,
            "same_num3_summary_output": True,
            "ordinary_engine": "Stage14-num3 one-chunk full shared-hypotenuse census",
            "alpha_engine": "Stage14-num-alpha5 pruned diagonal-first Gaussian collision census",
            "alternating_order": True,
            "repeats_per_bound": args.repeats,
            "formal_speedup_threshold": 1.25,
            "crossover_rule": "first of two consecutive tested bounds >=1.25x, with largest tested bound also >=1.25x",
            "note": "one-chunk ordinary is a conservative single-process comparator; production chunking trades memory for repeated scans and possible parallel wall-time",
        },
        "rows": rows,
        "decision": {
            "STAGE14_NUM_ALPHA7": "COMPLETE_MATCHED_END_TO_END_CROSSOVER_BENCHMARK",
            "EXACT_EQUALITY_PRESERVED_IN_ALL_TIMED_RUNS": True,
            "MEANINGFUL_END_TO_END_SPEEDUP_PROVED": meaningful,
            "FIRST_TESTED_SUSTAINED_20PCT_CROSSOVER_BOUND": crossover,
            "LARGEST_TESTED_BOUND": largest["bound"],
            "LARGEST_BOUND_MEDIAN_SPEEDUP_ORDINARY_OVER_ALPHA": largest["median_speedup_ordinary_over_alpha"],
            "FINITE_ENGINEERING_BENCHMARK_ONLY": True,
            "ASYMPTOTIC_COMPLEXITY_CLAIM": False,
            "NEXT": "Stage14-num-alpha8 scale exact alpha census beyond ordinary rolling cutoff" if meaningful else "Stage14-num-alpha7b optimize or abandon alpha acceleration",
        },
    }
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
