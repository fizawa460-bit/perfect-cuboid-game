#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "stages" / "stage15" / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from paired_enumerator import enumerate_paired  # noqa: E402
from scaled_enumerator import enumerate_scaled  # noqa: E402

COMPARISON_FIELDS = (
    "M2_total",
    "M2_direction_a_b_c",
    "N2_total",
    "N2_direction_a_b_c",
    "M3_total",
    "N3_total",
)
DIAGNOSTIC_FIELDS = (
    "integer_pythagorean_triangles_hyp_le_B",
    "glued_pairs_inside_R_before_physical_filters",
    "distinct_primitive_canonical_objects_with_at_least_two_faces",
    "exact_two_glue_multiplicity_one",
    "triple_glue_multiplicity_three",
)


def projection(summary: dict) -> dict:
    result = {key: summary[key] for key in COMPARISON_FIELDS}
    result["diagnostics"] = {key: summary["diagnostics"][key] for key in DIAGNOSTIC_FIELDS}
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="r202 overlap and shard invariance validation")
    parser.add_argument("--bound", type=int, default=200_000, choices=(200_000,))
    parser.add_argument("--shards", type=int, default=2)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    _, _, legacy = enumerate_paired(args.bound, materialize_rows=False)
    single = enumerate_scaled(args.bound, 1)
    sharded = enumerate_scaled(args.bound, args.shards)
    expected = projection(legacy)
    if projection(single) != expected:
        raise AssertionError("single-shard streaming result differs from legacy r201 enumerator")
    if projection(sharded) != expected:
        raise AssertionError("multi-shard streaming result differs from legacy r201 enumerator")

    out = {
        "id": "24-14num-r202-validation",
        "bound_R": args.bound,
        "legacy_equals_single_shard": True,
        "legacy_equals_multi_shard": True,
        "shared_edge_disjoint_union": sharded["diagnostics"]["shared_edge_disjoint_union"],
        "exact_two_glue_multiplicity_one": sharded["diagnostics"]["exact_two_glue_multiplicity_one"],
        "triple_glue_multiplicity_three": sharded["diagnostics"]["triple_glue_multiplicity_three"],
        "projection": expected,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    print("R202_LEGACY_OVERLAP_EQUALITY=PASS")
    print("R202_SHARD_INVARIANCE=PASS")
    print("R202_MULTIPLICITY_GATES=PASS")


if __name__ == "__main__":
    main()
