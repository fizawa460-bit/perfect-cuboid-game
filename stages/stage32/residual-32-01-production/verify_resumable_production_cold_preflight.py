#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib

from run_full178_resumable_work_unit import CURSOR_KIND, decode_input

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
KEY = ROOT / "stages/stage32/runkeys/residual32-01-full178-resumable-production.json"


def main() -> None:
    x = json.loads(KEY.read_text())
    assert x["schema"] == "STAGE32_RESIDUAL32_01_FULL178_RESUMABLE_PRODUCTION_RUNKEY_V1"
    assert x["workload"] == "FULL178_EXACT_PAIRING_PREFIX_RESUMABLE_PRODUCTION"
    # This verifier checks immutable production structure. The exact lifecycle
    # transition is checked separately by the commit-range authorization gate.
    assert int(x["revision"]) >= 0
    assert isinstance(x["armed"], bool)
    assert x["production_generation"] == 34
    assert x["source_mode"] == "BOOTSTRAP_LOCKED_OLD_FRONTIER_V1"
    assert [(s["generation"], s["start"], s["end"]) for s in x["source_slices"]] == [
        (31, 68, 88),
        (32, 0, 88),
        (33, 0, 110),
    ]
    assert sum(int(s["end"]) - int(s["start"]) for s in x["source_slices"]) == 218
    assert x["source_frontier_count"] == 218
    assert x["dispatch_count"] == 128
    assert x["carry_count"] == 90
    assert x["dispatch_count"] + x["carry_count"] == x["source_frontier_count"]
    assert x["dispatch_canonical_sha256"] == "2d96ebc0ed716d319e554c1ff6ac05dc9ad0bde9dbacc20490c9027c33f210a9"
    assert x["queue_policy"] == "FIFO_GLOBAL_FRONTIER_CARRY_THEN_RESUMABLE_CHILDREN"
    assert x["runner_schema"] == "STAGE32_RESIDUAL32_01_FULL178_RESUMABLE_WORK_UNIT_V1"
    assert x["node_limit_per_work_unit"] == 64000000
    assert x["max_unresolved_children_per_input"] == 1
    assert x["structural_reproduction_upper_bound"] == 1.0
    assert x["effective_heavy_concurrency"] == 17
    assert x["other_stage32_heavy_overlap_bound"] == 1
    assert x["maximum_effective_stage32_heavy_overlap"] == 18
    assert x["effective_heavy_concurrency"] + x["other_stage32_heavy_overlap_bound"] <= 18
    assert x["projected_peak_artifact_mb"] < 500
    assert x["intermediate_retention_days"] == 1
    assert x["frontier_manifest_retention_days"] == 7
    assert x["FULL_178_ROW_SWEEP_AUTHORIZED"] is True
    assert x["B18_RELEASE_AUTHORIZED"] is False
    assert x["THEOREM_CREDIT"] is False and x["RECEIVER_CREDIT"] is False
    assert x["PERFECT_CUBOID_EXISTENCE_CLAIM"] is False
    assert x["PERFECT_CUBOID_NONEXISTENCE_CLAIM"] is False

    # Cursor serialization/reload must be exact in both cold and armed states.
    raw = {
        "kind": "STRATUM_PARTITION",
        "row_id": "g0-d012",
        "e": 14,
        "prefix": [0],
        "next_min": 0,
        "next_max": 1,
    }
    first = decode_input(raw, emin=8)
    assert first["kind"] == CURSOR_KIND
    assert first["row_id"] == "g0-d012"
    assert first["e_current"] == 14
    assert first["continuation"] is None
    second = decode_input(json.loads(json.dumps(first, sort_keys=True)), emin=8)
    assert second == first

    print(json.dumps({
        "verdict": "PASS_RESUMABLE_PRODUCTION_STRUCTURAL_PREFLIGHT",
        "source_frontier_count": x["source_frontier_count"],
        "dispatch_count": x["dispatch_count"],
        "carry_count": x["carry_count"],
        "cursor_roundtrip_exact": True,
        "max_unresolved_children_per_input": 1,
        "stage32_heavy_overlap_bound": 18,
        "runkey_revision": int(x["revision"]),
        "production_armed": bool(x["armed"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
