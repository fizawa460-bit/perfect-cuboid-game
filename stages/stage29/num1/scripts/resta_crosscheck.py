#!/usr/bin/env python3
"""Independent finite cross-check for Stage29-num1.

Downloads the aligned OEIS tables A031173/A031174/A031175, reconstructs the
primitive Euler bricks listed by F. Helenius / Giovanni Resta, validates every
record with exact integer arithmetic, then applies the Stage20/28/29 physical
Euclidean cutoff R^2=a^2+b^2+c^2 <= B^2.

This is an independent exhaustive-table cross-check, not the primary repository
enumerator and not an asymptotic argument.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
import urllib.request
from pathlib import Path

URLS = {
    "longest": "https://oeis.org/A031173/b031173.txt",
    "middle": "https://oeis.org/A031174/b031174.txt",
    "shortest": "https://oeis.org/A031175/b031175.txt",
}
CHECKPOINTS = [10_000, 50_000, 200_000, 1_000_000, 5_000_000, 10_000_000,
               50_000_000, 100_000_000, 200_000_000, 500_000_000]
REGRESSION = {10_000: 18, 50_000: 42, 200_000: 82, 1_000_000: 219}
USER_AGENT = "perfect-cuboid-game Stage29-num1 exact finite cross-check/1.0"


def is_square(n: int) -> bool:
    r = math.isqrt(n)
    return r * r == n


def fetch_bfile(url: str) -> tuple[dict[int, int], str]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "text/plain"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = response.read()
    values: dict[int, int] = {}
    for line in raw.decode("utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        try:
            idx, value = int(parts[0]), int(parts[1])
        except ValueError:
            continue
        values[idx] = value
    return values, hashlib.sha256(raw).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    started = time.perf_counter()

    tables: dict[str, dict[int, int]] = {}
    hashes: dict[str, str] = {}
    for name, url in URLS.items():
        tables[name], hashes[name] = fetch_bfile(url)

    indexes = set(tables["longest"]) & set(tables["middle"]) & set(tables["shortest"])
    if not indexes:
        raise SystemExit("no aligned OEIS records downloaded")
    if not (set(tables["longest"]) == set(tables["middle"]) == set(tables["shortest"])):
        raise SystemExit("OEIS tables are not index-aligned")

    bricks: list[tuple[int, int, int, int]] = []
    seen: set[tuple[int, int, int]] = set()
    perfect_hits: list[tuple[int, int, int]] = []
    for idx in sorted(indexes):
        raw = (tables["longest"][idx], tables["middle"][idx], tables["shortest"][idx])
        a, b, c = sorted(raw)
        brick = (a, b, c)
        if brick in seen:
            raise SystemExit(f"duplicate canonical brick at OEIS index {idx}: {brick}")
        seen.add(brick)
        if math.gcd(a, math.gcd(b, c)) != 1:
            raise SystemExit(f"nonprimitive record at OEIS index {idx}: {brick}")
        if not (is_square(a*a+b*b) and is_square(a*a+c*c) and is_square(b*b+c*c)):
            raise SystemExit(f"failed face-diagonal check at OEIS index {idx}: {brick}")
        r2 = a*a + b*b + c*c
        bricks.append((a, b, c, r2))
        if is_square(r2):
            perfect_hits.append(brick)

    rows = []
    previous = 0
    for B in CHECKPOINTS:
        count = sum(r2 <= B*B for _, _, _, r2 in bricks)
        rows.append({"B": B, "M3": count, "increment": count - previous})
        previous = count
        if B in REGRESSION and count != REGRESSION[B]:
            raise SystemExit(f"regression mismatch at B={B}: got {count}, expected {REGRESSION[B]}")

    payload = {
        "track": "Stage29-num1",
        "algorithm": "OEIS-Resta-aligned-table-exact-filter-v1",
        "role": "independent exhaustive-table cross-check",
        "cutoff": "R^2=a^2+b^2+c^2 <= B^2",
        "canonical": "a<=b<=c",
        "primitive": "gcd(a,b,c)=1",
        "record_count": len(bricks),
        "source_urls": URLS,
        "source_sha256": hashes,
        "checkpoints": rows,
        "perfect_cuboid_hits": perfect_hits,
        "perfect_cuboid_hit_count": len(perfect_hits),
        "runtime_sec": time.perf_counter() - started,
        "guards": {
            "NUM_REUSE_PREFLIGHT": "REQUIRED",
            "FINITE_DATA_IS_NOT_ASYMPTOTIC_THEOREM": True,
            "PERFECT_CUBOID_NONEXISTENCE_CLAIM": False,
        },
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
