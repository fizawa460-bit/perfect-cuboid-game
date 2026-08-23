#!/usr/bin/env python3
"""Exact fixed-budget Stage32 enumeration with the Normaliz CLI.

This backend enumerates integral Picard coordinates directly inside the 140
known-class halfspaces.  It therefore applies the exact positive-dual budget
before any quadratic/lattice-ball enumeration.  Normaliz's integer
project-and-lift algorithm is used; ProjectionFloat is deliberately forbidden.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import time


EXPECTED_SCHEMA = "STAGE32_PICARD_CORE_INDLIST_V1"
EXPECTED_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"


def canonical_json_sha256(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def load_core(path: pathlib.Path) -> tuple[dict, str]:
    core = json.loads(path.read_text(encoding="utf-8"))
    assert core["schema"] == EXPECTED_SCHEMA
    assert core["source"]["git_blob_sha1"] == EXPECTED_BLOB
    assert core["rank"] == 64
    assert core["known_class_count"] == 140
    assert core["h2"] == 16
    unhashed = dict(core)
    claimed = unhashed.pop("canonical_sha256_without_this_field")
    actual = canonical_json_sha256(unhashed)
    assert actual == claimed
    return core, actual


def dot(left: list[int], right: list[int]) -> int:
    return sum(a * b for a, b in zip(left, right))


def column_pairing(vector: list[int], gram: list[list[int]]) -> list[int]:
    return [sum(vector[i] * gram[i][j] for i in range(64)) for j in range(64)]


def exact_forms(core: dict) -> tuple[list[int], list[int], list[int]]:
    gram = core["basis_gram"]
    intersections = core["raw_cross_pairings_with_basis"]
    hform = column_pairing(core["hyperplane"], gram)
    exceptional = [sum(intersections[k][j] for k in range(92, 140)) for j in range(64)]
    first_curve_group = [sum(intersections[k][j] for k in range(46)) for j in range(64)]
    weighted = [
        sum(intersections[k][j] for k in range(92))
        + 5 * sum(intersections[k][j] for k in range(92, 140))
        for j in range(64)
    ]
    assert weighted == [19 * x for x in hform]
    return hform, exceptional, first_curve_group


def normaliz_input(core: dict, degree: int, exceptional_mass: int, curve_group_mass: int) -> str:
    hform, exceptional, first_curve_group = exact_forms(core)
    rows = core["raw_cross_pairings_with_basis"]
    equations = (
        hform + [-degree],
        exceptional + [-exceptional_mass],
        first_curve_group + [-curve_group_mass],
    )
    lines = ["amb_space 64", f"inhom_inequalities {len(rows)}"]
    lines.extend(" ".join(map(str, row + [0])) for row in rows)
    lines.append(f"inhom_equations {len(equations)}")
    lines.extend(" ".join(map(str, row)) for row in equations)
    lines.extend(("Projection", "NumberLatticePoints", "NoGradingDenom"))
    return "\n".join(lines) + "\n"


def parse_count(out_text: str) -> int:
    patterns = (
        r"number of lattice points\s*[:=]?\s*(\d+)",
        r"NumberLatticePoints\s*[:=]?\s*(\d+)",
        r"lattice points in polytope\s*[:=]?\s*(\d+)",
    )
    for pattern in patterns:
        match = re.search(pattern, out_text, flags=re.IGNORECASE)
        if match:
            return int(match.group(1))
    raise RuntimeError("Normaliz output did not contain an auditable lattice-point count")


def run_shard(args: argparse.Namespace, core: dict, core_sha256: str) -> dict:
    shard_id = f"d{args.degree}-g{args.genus}-e{args.exceptional_mass}-a{args.curve_group_mass}"
    shard_dir = args.output_dir / shard_id
    shard_dir.mkdir(parents=True, exist_ok=True)
    project = f"stage32-{shard_id}"
    input_text = normaliz_input(core, args.degree, args.exceptional_mass, args.curve_group_mass)
    input_path = shard_dir / f"{project}.in"
    input_path.write_text(input_text, encoding="utf-8", newline="\n")
    input_sha256 = hashlib.sha256(input_text.encode()).hexdigest()
    command = [str(args.normaliz), "-B", f"-x={args.threads}", "-f", project]
    start = time.perf_counter()
    completed = subprocess.run(
        command,
        cwd=shard_dir,
        check=False,
        capture_output=True,
        text=True,
        timeout=args.timeout,
    )
    elapsed = time.perf_counter() - start
    out_path = shard_dir / f"{project}.out"
    out_text = out_path.read_text(encoding="utf-8", errors="replace") if out_path.exists() else ""
    count = parse_count(out_text) if completed.returncode == 0 else None
    payload = {
        "schema": "STAGE32_EXACT_NORMALIZ_BUDGET_SHARD_V1",
        "backend": "Normaliz exact integer project-and-lift",
        "normaliz_version": subprocess.run(
            [str(args.normaliz), "--version"], capture_output=True, text=True, check=True
        ).stdout.strip(),
        "degree": args.degree,
        "genus": args.genus,
        "exceptional_mass": args.exceptional_mass,
        "curve_group_mass": args.curve_group_mass,
        "weighted_intersection_budget": 19 * args.degree,
        "picard_core_sha256": core_sha256,
        "normaliz_input_sha256": input_sha256,
        "normaliz_input": input_path.name,
        "exact_lattice_point_count_before_adjunction": count,
        "returncode": completed.returncode,
        "elapsed_seconds": round(elapsed, 6),
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "floating_point_credit": False,
        "complete": completed.returncode == 0 and count is not None,
    }
    unsigned = dict(payload)
    payload["checkpoint_sha256_without_this_field"] = canonical_json_sha256(unsigned)
    checkpoint = shard_dir / "checkpoint.json"
    checkpoint.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--normaliz", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--degree", type=int, required=True)
    parser.add_argument("--genus", type=int, choices=(0, 1), required=True)
    parser.add_argument("--exceptional-mass", type=int, required=True)
    parser.add_argument("--curve-group-mass", type=int, required=True)
    parser.add_argument("--threads", type=int, default=0)
    parser.add_argument("--timeout", type=float, default=3600)
    args = parser.parse_args()
    if args.degree <= 0 or args.degree % 2:
        raise SystemExit("degree must be positive and even")
    if not 0 <= args.exceptional_mass <= 19 * args.degree // 5:
        raise SystemExit("exceptional mass is outside the exact weighted budget")
    curve_total = 19 * args.degree - 5 * args.exceptional_mass
    if not 0 <= args.curve_group_mass <= curve_total:
        raise SystemExit("curve-group mass is outside the exact weighted budget")
    core, core_sha256 = load_core(args.core)
    result = run_shard(args, core, core_sha256)
    print(json.dumps(result, sort_keys=True))
    if not result["complete"]:
        raise SystemExit("exact Normaliz shard did not complete")


if __name__ == "__main__":
    main()
