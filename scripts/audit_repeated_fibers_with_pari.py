#!/usr/bin/env python3
"""Run PARI/GP 2-descent on repeated specialized elliptic fibers.

The input comes from the exact bounded-relation audit. For every repeated
lambda fiber, the observed bounded seed points are supplied to PARI's ellrank.
The returned lower and upper rank bounds are unconditional outputs of the
2-descent algorithm. Equality certifies the specialized rank over Q.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_fraction(record: dict[str, Any]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def gp_fraction(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"({value.numerator}/{value.denominator})"


def parse_integer(raw: str, name: str) -> int:
    match = re.search(rf"^{re.escape(name)}=(-?\d+)\s*$", raw, re.MULTILINE)
    if not match:
        raise RuntimeError(f"missing {name} in PARI output:\n{raw}")
    return int(match.group(1))


def run_one(
    gp: str,
    fiber: dict[str, Any],
    point_by_index: dict[int, dict[str, Any]],
    effort: int,
    timeout: int,
) -> dict[str, Any]:
    a2 = parse_fraction(fiber["curve"]["a2"])
    a4 = parse_fraction(fiber["curve"]["a4"])
    basis_indices = [
        int(index)
        for index in fiber["bounded_relation_search"]["basis_source_indices"]
    ]
    gp_points: list[str] = []
    for index in basis_indices:
        point = point_by_index[index]["weierstrass_point"]
        x = parse_fraction(point["x"])
        y = parse_fraction(point["y"])
        gp_points.append(f"[{gp_fraction(x)},{gp_fraction(y)}]")
    points_vector = "[" + ",".join(gp_points) + "]"
    script = f"""
E=ellinit([0,{gp_fraction(a2)},0,{gp_fraction(a4)},0]);
P={points_vector};
print("ALL_POINTS_ON_CURVE=",vecmin(vector(#P,k,ellisoncurve(E,P[k]))));
T=elltors(E);
print("TORSION_ORDER=",T[1]);
print("TORSION_STRUCTURE=",T[2]);
R=ellrank(E,{effort},P);
print("RANK_LOWER=",R[1]);
print("RANK_UPPER=",R[2]);
print("SHA2_INFO=",R[3]);
print("FOUND_GENERATOR_COUNT=",#R[4]);
print("ROOT_NUMBER=",ellrootno(E));
quit;
"""
    try:
        completed = subprocess.run(
            [gp, "-q"],
            input=script,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        return {
            "lambda": fiber["lambda"],
            "status": "timeout",
            "timeout_seconds": timeout,
            "bounded_basis_source_indices": basis_indices,
            "bounded_basis_size": len(basis_indices),
            "error": str(exc),
        }
    raw = completed.stdout + completed.stderr
    if completed.returncode != 0:
        return {
            "lambda": fiber["lambda"],
            "status": "pari_error",
            "bounded_basis_source_indices": basis_indices,
            "bounded_basis_size": len(basis_indices),
            "raw_pari_output": raw,
        }
    structure = re.search(r"^TORSION_STRUCTURE=(\[[^\n]*\])\s*$", raw, re.MULTILINE)
    lower = parse_integer(raw, "RANK_LOWER")
    upper = parse_integer(raw, "RANK_UPPER")
    return {
        "lambda": fiber["lambda"],
        "status": "success",
        "bounded_basis_source_indices": basis_indices,
        "bounded_basis_size": len(basis_indices),
        "all_basis_points_on_curve": bool(parse_integer(raw, "ALL_POINTS_ON_CURVE")),
        "torsion_order": parse_integer(raw, "TORSION_ORDER"),
        "torsion_structure_raw": None if structure is None else structure.group(1),
        "rank_lower_bound": lower,
        "rank_upper_bound": upper,
        "rank_exact": lower == upper,
        "sha_2_information": parse_integer(raw, "SHA2_INFO"),
        "found_generator_count": parse_integer(raw, "FOUND_GENERATOR_COUNT"),
        "root_number": parse_integer(raw, "ROOT_NUMBER"),
        "raw_pari_output": raw,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--relations", type=Path, required=True)
    parser.add_argument("--effort", type=int, default=0)
    parser.add_argument("--timeout-per-fiber", type=int, default=120)
    parser.add_argument("--write-report", type=Path, required=True)
    args = parser.parse_args()

    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP executable 'gp' was not found")
    payload = json.loads(args.relations.read_text(encoding="utf-8"))
    point_by_index = {
        int(point["source_index"]): point for point in payload.get("points", [])
    }
    fibers = payload.get("repeated_fibers", [])
    results = [
        run_one(
            gp,
            fiber,
            point_by_index,
            args.effort,
            args.timeout_per_fiber,
        )
        for fiber in fibers
    ]

    successes = [item for item in results if item["status"] == "success"]
    exact = [item for item in successes if item["rank_exact"]]
    rank_interval_histogram = Counter(
        f"{item['rank_lower_bound']}..{item['rank_upper_bound']}"
        for item in successes
    )
    exact_rank_histogram = Counter(
        str(item["rank_lower_bound"]) for item in exact
    )
    report = {
        "valid": len(successes) == len(results)
        and all(item["all_basis_points_on_curve"] for item in successes),
        "source": args.relations.as_posix(),
        "fiber_count": len(results),
        "success_count": len(successes),
        "timeout_count": sum(item["status"] == "timeout" for item in results),
        "pari_error_count": sum(item["status"] == "pari_error" for item in results),
        "exact_rank_count": len(exact),
        "rank_interval_histogram": dict(sorted(rank_interval_histogram.items())),
        "exact_rank_histogram": dict(sorted(exact_rank_histogram.items())),
        "basis_size_equals_rank_lower_count": sum(
            item["bounded_basis_size"] == item["rank_lower_bound"]
            for item in successes
        ),
        "fibers": results,
        "scope": {
            "certified": (
                "for fibers with equal lower and upper bounds, the specialized "
                "Mordell-Weil rank over Q"
            ),
            "not_certified": [
                "saturation of the observed basis",
                "a uniform rank statement for unobserved fibers",
                "a global point-counting bound on the K3 surface",
                "N_2=o(N_1)",
            ],
        },
    }
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    summary = {key: value for key, value in report.items() if key != "fibers"}
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
