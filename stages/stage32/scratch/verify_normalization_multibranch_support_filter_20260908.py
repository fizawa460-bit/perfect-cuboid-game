#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
AH = ROOT / "stages" / "stage32" / "residual-32-01-production" / "post1648ah-fsm-unibranch-v6-exclusion.json"
OUT = HERE / "normalization-multibranch-support-filter-20260908.json"

EXPECTED_AH_CANONICAL = "6ee4ebdf266deec5d7aa865d5b088211f8fffadc99be1119b8cc779c4be9f043"
EXPECTED_OUT_CANONICAL = "21b3ab5ef9f751cd5de47b024cf43c7d177c10f41839b797098c8bd1f00a00be"

def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

def main() -> None:
    ah = json.loads(AH.read_text())
    if ah["canonical_sha256_without_this_field"] != EXPECTED_AH_CANONICAL:
        raise ValueError("AH source regression")
    pairings = [int(x) for x in ah["v6_exact_data"]["exceptional_pairings"]]
    if len(pairings) != 48:
        raise ValueError("exceptional count regression")
    if sum(pairings) != 266:
        raise ValueError("exceptional mass regression")

    zero = [i + 1 for i, x in enumerate(pairings) if x == 0]
    unit = [i + 1 for i, x in enumerate(pairings) if x == 1]
    nonunit = [i + 1 for i, x in enumerate(pairings) if x >= 2]
    positive = [i + 1 for i, x in enumerate(pairings) if x > 0]
    excess = sum(max(x - 1, 0) for x in pairings)

    if len(positive) != 47 or zero != [6]:
        raise ValueError("positive support regression")
    if unit != [1, 2, 3, 7, 15, 20, 22, 24, 36]:
        raise ValueError("unit-label regression")
    if len(nonunit) != 38:
        raise ValueError("nonunit candidate count regression")
    if excess != 219:
        raise ValueError("branch-excess capacity regression")

    out = json.loads(OUT.read_text())
    stored = out.pop("canonical_sha256_without_this_field")
    if stored != EXPECTED_OUT_CANONICAL or csha(out) != EXPECTED_OUT_CANONICAL:
        raise ValueError("scratch output canonical regression")
    if out["exact_v6_filter"]["nonunit_positive_labels_1based"] != nonunit:
        raise ValueError("candidate labels regression")
    if out["decision"]["surface_node_branch_excluded_labels_1based"] != sorted(zero + unit):
        raise ValueError("excluded labels regression")

    print(json.dumps({
        "verdict": "PASS_STAGE32_MAIN_SCRATCH_NORMALIZATION_MULTIBRANCH_SUPPORT_FILTER",
        "surface_node_candidates": len(nonunit),
        "surface_node_excluded_by_m_le_1": len(zero) + len(unit),
        "branch_excess_capacity_upper_bound": excess,
        "canonical_sha256": EXPECTED_OUT_CANONICAL,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
