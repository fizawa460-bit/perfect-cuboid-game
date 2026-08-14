#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import multiprocessing as mp
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "stages" / "stage15" / "scripts"))

from paired_enumerator import (  # noqa: E402
    DIRECTION_ORDER,
    MASK_TO_DIRECTION,
    face_mask,
    generate_leg_index,
)

MAX_BOUND = 1_000_000
STAGED_BOUNDS = (200_000, 500_000, 1_000_000)

_BY_LEG: dict[int, list[int]] = {}
_BOUND = 0


def _init_worker(by_leg: dict[int, list[int]], bound: int) -> None:
    global _BY_LEG, _BOUND
    _BY_LEG = by_leg
    _BOUND = bound


def _scan_shared_edges(shared_edges: list[int]) -> dict:
    m2_dir = Counter({direction: 0 for direction in DIRECTION_ORDER})
    n2_dir = Counter({direction: 0 for direction in DIRECTION_ORDER})
    triple_sources: Counter[tuple[int, int, int]] = Counter()
    glued_pairs_inside_r = 0
    primitive_pairs = 0

    for shared in shared_edges:
        entries = _BY_LEG[shared]
        for i, x in enumerate(entries):
            for y in entries[i + 1 :]:
                r2 = shared * shared + x * x + y * y
                if r2 > _BOUND * _BOUND:
                    continue
                glued_pairs_inside_r += 1
                a, b, c = sorted((shared, x, y))
                if not (a < b < c) or math.gcd(math.gcd(a, b), c) != 1:
                    continue
                primitive_pairs += 1
                mask = face_mask(a, b, c)
                if mask.bit_count() == 2:
                    direction = MASK_TO_DIRECTION[mask]
                    expected_shared = {"a": a, "b": b, "c": c}[direction]
                    if shared != expected_shared:
                        raise ArithmeticError(
                            f"exact-two object glued through wrong shared edge: {(a, b, c, shared, mask)}"
                        )
                    m2_dir[direction] += 1
                    d = math.isqrt(r2)
                    if d * d == r2:
                        n2_dir[direction] += 1
                elif mask == 0b111:
                    triple_sources[(a, b, c)] += 1
                else:
                    raise ArithmeticError(f"glued pair lost square faces: {(a, b, c, shared, mask)}")

    return {
        "m2_dir": dict(m2_dir),
        "n2_dir": dict(n2_dir),
        "triple_sources": [[*key, count] for key, count in sorted(triple_sources.items())],
        "glued_pairs_inside_r": glued_pairs_inside_r,
        "primitive_pairs": primitive_pairs,
        "shared_edges": len(shared_edges),
        "first_shared": shared_edges[0] if shared_edges else None,
        "last_shared": shared_edges[-1] if shared_edges else None,
    }


def _partition(values: list[int], shard_count: int) -> list[list[int]]:
    if shard_count < 1:
        raise ValueError("shard_count must be positive")
    return [values[i::shard_count] for i in range(shard_count)]


def enumerate_scaled(bound: int, shard_count: int) -> dict:
    if bound not in STAGED_BOUNDS:
        raise ValueError(f"bound must be one of {STAGED_BOUNDS}; got {bound}")
    if bound > MAX_BOUND:
        raise ValueError(f"hard cap exceeded: {bound}>{MAX_BOUND}")

    by_leg, triangle_count = generate_leg_index(bound)
    shared_edges = sorted(by_leg)
    shards = _partition(shared_edges, shard_count)

    flattened = [shared for shard in shards for shared in shard]
    if len(flattened) != len(set(flattened)) or set(flattened) != set(shared_edges):
        raise AssertionError("shared-edge shards are not an exact disjoint cover")

    if shard_count == 1:
        _init_worker(by_leg, bound)
        partials = [_scan_shared_edges(shards[0])]
    else:
        context = mp.get_context("fork")
        with context.Pool(
            processes=min(shard_count, max(1, mp.cpu_count())),
            initializer=_init_worker,
            initargs=(by_leg, bound),
        ) as pool:
            partials = pool.map(_scan_shared_edges, shards)

    m2_dir = Counter({direction: 0 for direction in DIRECTION_ORDER})
    n2_dir = Counter({direction: 0 for direction in DIRECTION_ORDER})
    triple_sources: Counter[tuple[int, int, int]] = Counter()
    for partial in partials:
        m2_dir.update(partial["m2_dir"])
        n2_dir.update(partial["n2_dir"])
        for a, b, c, count in partial["triple_sources"]:
            triple_sources[(a, b, c)] += count

    bad_triples = {key: count for key, count in triple_sources.items() if count != 3}
    if bad_triples:
        sample = list(sorted(bad_triples.items()))[:5]
        raise AssertionError(f"triple multiplicity is not three: {sample}")

    n3_total = 0
    for a, b, c in triple_sources:
        r2 = a * a + b * b + c * c
        d = math.isqrt(r2)
        n3_total += int(d * d == r2)

    m2_total = sum(m2_dir.values())
    n2_total = sum(n2_dir.values())
    return {
        "id": "24-14num-r202",
        "classification": "EXACT_FINITE_STREAMING_SHARDED_CENSUS",
        "bound_R": bound,
        "hard_cap_R": MAX_BOUND,
        "M2_total": m2_total,
        "M2_direction_a_b_c": [m2_dir[d] for d in DIRECTION_ORDER],
        "N2_total": n2_total,
        "N2_direction_a_b_c": [n2_dir[d] for d in DIRECTION_ORDER],
        "N2_over_M2": n2_total / m2_total,
        "M3_total": len(triple_sources),
        "N3_total": n3_total,
        "diagnostics": {
            "integer_pythagorean_triangles_hyp_le_B": triangle_count,
            "glued_pairs_inside_R_before_physical_filters": sum(
                part["glued_pairs_inside_r"] for part in partials
            ),
            "primitive_glue_source_incidences": sum(part["primitive_pairs"] for part in partials),
            "distinct_primitive_canonical_objects_with_at_least_two_faces": m2_total + len(triple_sources),
            "exact_two_glue_multiplicity_one": True,
            "triple_glue_multiplicity_three": True,
            "shard_count": shard_count,
            "shared_edge_count": len(shared_edges),
            "shared_edge_disjoint_union": True,
            "shards": [
                {
                    "index": index,
                    "shared_edges": part["shared_edges"],
                    "first_shared": part["first_shared"],
                    "last_shared": part["last_shared"],
                }
                for index, part in enumerate(partials)
            ],
        },
        "claims": {
            "population_contract_unchanged_from_r201": True,
            "finite_diagnostic_only": True,
            "asymptotic_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Exact Stage24 r202 streaming/sharded M2->N2 census")
    parser.add_argument("--bound", type=int, required=True, choices=STAGED_BOUNDS)
    parser.add_argument("--shards", type=int, default=2)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    summary = enumerate_scaled(args.bound, args.shards)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
