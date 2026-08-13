#!/usr/bin/env python3
"""Deterministic Stage16-20 finite census for the audited exactly-one-face population."""

from __future__ import annotations

import argparse
import csv
from math import gcd, isqrt
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

DEFAULT_THRESHOLDS = (50, 100, 200, 400, 800, 1200, 1600, 2000)
FACE_NAMES = ("ab", "ac", "bc")
Triple = Tuple[int, int, int]
Record = Tuple[int, str]


def is_square(n: int) -> bool:
    r = isqrt(n)
    return r * r == n


def pythagorean_leg_pairs(max_b: int) -> List[Tuple[int, int]]:
    """All positive integer leg pairs whose hypotenuse is <= max_b."""
    pairs = set()
    m = 2
    while m * m + 1 <= max_b:
        for n in range(1, m):
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            h = m * m + n * n
            if h > max_b:
                continue
            u = m * m - n * n
            v = 2 * m * n
            lo, hi = sorted((u, v))
            for scale in range(1, max_b // h + 1):
                pairs.add((scale * lo, scale * hi))
        m += 1
    return sorted(pairs)


def face_signature(a: int, b: int, c: int) -> Tuple[bool, bool, bool]:
    return (
        is_square(a * a + b * b),
        is_square(a * a + c * c),
        is_square(b * b + c * c),
    )


def enumerate_stage16(max_b: int) -> Dict[Triple, Record]:
    """Enumerate all audited Stage16 objects with R <= max_b."""
    max_b2 = max_b * max_b
    records: Dict[Triple, Record] = {}

    for x, y in pythagorean_leg_pairs(max_b):
        remaining = max_b2 - x * x - y * y
        if remaining <= 0:
            continue
        for z in range(1, isqrt(remaining) + 1):
            if z == x or z == y:
                continue
            a, b, c = sorted((x, y, z))
            if not (a < b < c):
                continue
            if gcd(gcd(a, b), c) != 1:
                continue

            signature = face_signature(a, b, c)
            if sum(signature) != 1:
                continue

            face = FACE_NAMES[signature.index(True)]
            records[(a, b, c)] = (a * a + b * b + c * c, face)

    return records


def brute_force_stage16(max_b: int) -> Dict[Triple, Record]:
    """Independent cubic-style reference enumerator for small replay cutoffs."""
    max_b2 = max_b * max_b
    records: Dict[Triple, Record] = {}

    for a in range(1, max_b + 1):
        for b in range(a + 1, max_b + 1):
            ab = a * a + b * b
            if ab >= max_b2:
                break
            c_max = isqrt(max_b2 - ab)
            for c in range(b + 1, c_max + 1):
                if gcd(gcd(a, b), c) != 1:
                    continue
                signature = face_signature(a, b, c)
                if sum(signature) != 1:
                    continue
                face = FACE_NAMES[signature.index(True)]
                records[(a, b, c)] = (ab + c * c, face)

    return records


def census_rows(records: Dict[Triple, Record], thresholds: Iterable[int]) -> List[dict]:
    rows = []
    for bound in thresholds:
        split = {face: 0 for face in FACE_NAMES}
        limit = bound * bound
        for r2, face in records.values():
            if r2 <= limit:
                split[face] += 1
        total = sum(split.values())
        rows.append(
            {
                "B": bound,
                "M1": total,
                "face_ab": split["ab"],
                "face_ac": split["ac"],
                "face_bc": split["bc"],
            }
        )
    return rows


def write_csv(path: Path, rows: List[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=("B", "M1", "face_ab", "face_ac", "face_bc")
        )
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> List[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = []
        for row in csv.DictReader(handle):
            rows.append({key: int(value) for key, value in row.items()})
        return rows


def verify(data_path: Path, self_check_b: int) -> None:
    optimized_small = enumerate_stage16(self_check_b)
    brute_small = brute_force_stage16(self_check_b)
    if optimized_small != brute_small:
        only_optimized = sorted(set(optimized_small) - set(brute_small))[:10]
        only_brute = sorted(set(brute_small) - set(optimized_small))[:10]
        raise SystemExit(
            "small-cutoff cross-check failed: "
            f"optimized_only={only_optimized}, brute_only={only_brute}"
        )

    frozen = read_csv(data_path)
    thresholds = tuple(row["B"] for row in frozen)
    if not thresholds or tuple(sorted(thresholds)) != thresholds:
        raise SystemExit("counts.csv thresholds must be nonempty and strictly ordered")
    if len(set(thresholds)) != len(thresholds):
        raise SystemExit("counts.csv contains duplicate thresholds")

    regenerated = census_rows(enumerate_stage16(max(thresholds)), thresholds)
    if regenerated != frozen:
        raise SystemExit(
            f"frozen census mismatch:\nexpected={frozen}\nregenerated={regenerated}"
        )

    for row in frozen:
        if row["M1"] != row["face_ab"] + row["face_ac"] + row["face_bc"]:
            raise SystemExit(f"face split does not sum to M1 at B={row['B']}")

    print(f"SMALL_CUTOFF_CROSSCHECK_B={self_check_b}:PASS")
    print(f"FROZEN_CENSUS_MAX_B={max(thresholds)}:PASS")
    print("STAGE16_20_VERIFY=PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--self-check-b", type=int, default=100)
    parser.add_argument(
        "--thresholds",
        default=",".join(str(x) for x in DEFAULT_THRESHOLDS),
        help="comma-separated positive integer B cutoffs",
    )
    args = parser.parse_args()

    if args.verify is not None:
        verify(args.verify, args.self_check_b)
        return

    thresholds = tuple(int(x) for x in args.thresholds.split(",") if x)
    if not thresholds or any(x <= 0 for x in thresholds):
        raise SystemExit("thresholds must be positive")
    if tuple(sorted(thresholds)) != thresholds or len(set(thresholds)) != len(thresholds):
        raise SystemExit("thresholds must be strictly increasing")

    rows = census_rows(enumerate_stage16(max(thresholds)), thresholds)
    if args.output is not None:
        write_csv(args.output, rows)
    else:
        writer = csv.DictWriter(
            __import__("sys").stdout,
            fieldnames=("B", "M1", "face_ab", "face_ac", "face_bc"),
        )
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
