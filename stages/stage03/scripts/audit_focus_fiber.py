#!/usr/bin/env python3
"""Use PARI/GP to audit one specialized face-cuboid elliptic fiber.

PARI's ellrank returns unconditional lower and upper bounds from 2-descent.
An equality of the two bounds certifies the Mordell-Weil rank for that fiber.
The computation is separate from the bounded exact relation search and does
not generalize automatically to every fiber or to the global K3 surface.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_fraction(record: dict[str, Any]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def gp_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def load_focus(
    relations_path: Path, lambda_text: str
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    payload = json.loads(relations_path.read_text(encoding="utf-8"))
    fibers = payload.get("repeated_fibers", [])
    fiber = next((item for item in fibers if item.get("lambda") == lambda_text), None)
    if fiber is None:
        raise ValueError(f"lambda={lambda_text} is not a repeated fiber")
    point_by_index = {
        int(item["source_index"]): item for item in payload.get("points", [])
    }
    basis_indices = fiber["bounded_relation_search"]["basis_source_indices"]
    basis_points = [point_by_index[int(index)] for index in basis_indices]
    return fiber, basis_points


def run_pari(
    fiber: dict[str, Any], basis_points: list[dict[str, Any]], effort: int
) -> tuple[dict[str, Any], str]:
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP executable 'gp' was not found")

    a2 = parse_fraction(fiber["curve"]["a2"])
    a4 = parse_fraction(fiber["curve"]["a4"])
    gp_points = []
    for item in basis_points:
        point = item["weierstrass_point"]
        if point.get("infinity"):
            raise ValueError("the bounded basis unexpectedly contains infinity")
        x = parse_fraction(point["x"])
        y = parse_fraction(point["y"])
        gp_points.append(f"[{gp_fraction(x)},{gp_fraction(y)}]")

    points_vector = "[" + ",".join(gp_points) + "]"
    script = f"""
E=ellinit([0,{gp_fraction(a2)},0,{gp_fraction(a4)},0]);
P={points_vector};
print("PARI_VERSION=",version());
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
    completed = subprocess.run(
        [gp, "-q"],
        input=script,
        text=True,
        capture_output=True,
        timeout=600,
        check=False,
    )
    raw = completed.stdout + completed.stderr
    if completed.returncode != 0:
        raise RuntimeError(
            f"PARI/GP exited with status {completed.returncode}:\n{raw}"
        )

    def integer_field(name: str) -> int:
        match = re.search(rf"^{re.escape(name)}=(-?\d+)\s*$", raw, re.MULTILINE)
        if not match:
            raise RuntimeError(f"missing {name} in PARI output:\n{raw}")
        return int(match.group(1))

    structure_match = re.search(
        r"^TORSION_STRUCTURE=(\[[^\n]*\])\s*$", raw, re.MULTILINE
    )
    version_match = re.search(r"^PARI_VERSION=(.+)$", raw, re.MULTILINE)
    result = {
        "pari_version": None if version_match is None else version_match.group(1).strip(),
        "all_basis_points_on_curve": bool(integer_field("ALL_POINTS_ON_CURVE")),
        "torsion_order": integer_field("TORSION_ORDER"),
        "torsion_structure_raw": (
            None if structure_match is None else structure_match.group(1)
        ),
        "rank_lower_bound": integer_field("RANK_LOWER"),
        "rank_upper_bound": integer_field("RANK_UPPER"),
        "sha_2_information": integer_field("SHA2_INFO"),
        "found_generator_count": integer_field("FOUND_GENERATOR_COUNT"),
        "root_number": integer_field("ROOT_NUMBER"),
    }
    result["rank_exact"] = (
        result["rank_lower_bound"] == result["rank_upper_bound"]
    )
    return result, raw


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--relations",
        type=Path,
        default=Path("data/two_face_cuboids_1e6_mordell_weil_relations.json"),
    )
    parser.add_argument("--lambda", dest="lambda_text", default="16/21")
    parser.add_argument("--effort", type=int, default=1)
    parser.add_argument("--write-report", type=Path, required=True)
    args = parser.parse_args()

    fiber, basis_points = load_focus(args.relations, args.lambda_text)
    pari, raw = run_pari(fiber, basis_points, args.effort)
    report = {
        "valid": pari["all_basis_points_on_curve"],
        "lambda": args.lambda_text,
        "bounded_relation_basis_source_indices": fiber[
            "bounded_relation_search"
        ]["basis_source_indices"],
        "bounded_relation_basis_size": fiber[
            "bounded_relation_search"
        ]["bounded_basis_size"],
        "pari": pari,
        "scope": {
            "certified_when_rank_bounds_equal": (
                "the specialized elliptic curve's Mordell-Weil rank over Q"
            ),
            "not_certified": [
                "that the observed bounded basis is saturated",
                "that it is a full Mordell-Weil basis",
                "the rank of any other lambda fiber",
                "a global point-counting bound on the K3 surface",
            ],
        },
        "raw_pari_output": raw,
    }
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
