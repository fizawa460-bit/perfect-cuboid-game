#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
AH = ROOT / "stages" / "stage32" / "residual-32-01-production" / "post1648ah-fsm-unibranch-v6-exclusion.json"
OUT = HERE / "node-fiber-injectivity-exclusion-20260908.json"

EXPECTED_AH_CANONICAL = "6ee4ebdf266deec5d7aa865d5b088211f8fffadc99be1119b8cc779c4be9f043"
EXPECTED_OUT_CANONICAL = "f6d3b85e87d99e7a7135aba3cff786393f15f6d847721f842f78886a9c1d5596"

def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

def main() -> None:
    ah = json.loads(AH.read_text())
    if ah["canonical_sha256_without_this_field"] != EXPECTED_AH_CANONICAL:
        raise ValueError("AH source regression")

    d = int(ah["v6_exact_data"]["degree_d"])
    g = int(ah["v6_exact_data"]["geometric_genus_under_test"])
    pairings = [int(x) for x in ah["v6_exact_data"]["exceptional_pairings"]]
    positive = [x for x in pairings if x > 0]
    candidates = [i + 1 for i, x in enumerate(pairings) if x >= 2]

    if (d, g, len(positive), sum(pairings)) != (186, 1, 47, 266):
        raise ValueError("V6 arithmetic regression")

    zeros_lower = 2 * d
    poles_if_one_nonminimal = 8 * (len(positive) - 1)
    if (zeros_lower, poles_if_one_nonminimal) != (372, 368):
        raise ValueError("FSM slack regression")
    if poles_if_one_nonminimal >= zeros_lower:
        raise ValueError("one-nonminimal contradiction disappeared")

    # Under node-fiber injectivity, all 47 unique node branches must therefore
    # be the unique (4,4) pole-producing type. AH's A1 calculation gives
    # exceptional intersection 1 per such branch.
    forced_mass = len(positive) * int(
        ah["local_A1_resolution"]["minimal_cusp_strict_transform_exceptional_intersection"]
    )
    if forced_mass != 47 or forced_mass == sum(pairings):
        raise ValueError("node-fiber-injective mass contradiction regression")
    if len(candidates) != 38:
        raise ValueError("surface-node candidate count regression")

    out = json.loads(OUT.read_text())
    stored = out.pop("canonical_sha256_without_this_field")
    if stored != EXPECTED_OUT_CANONICAL or csha(out) != EXPECTED_OUT_CANONICAL:
        raise ValueError("scratch output canonical regression")
    if out["location_consequence"]["candidate_surface_node_labels_1based"] != candidates:
        raise ValueError("candidate labels regression")
    if out["decision"]["nonbijectivity_type_partially_identified"] != "SURFACE_NODE_MULTIBRANCH_IS_NECESSARY":
        raise ValueError("decision regression")

    print(json.dumps({
        "verdict": "PASS_STAGE32_MAIN_SCRATCH_NODE_FIBER_INJECTIVITY_EXCLUSION",
        "zeros_lower_per_k": zeros_lower,
        "poles_if_one_nonminimal_per_k": poles_if_one_nonminimal,
        "forced_exceptional_mass": forced_mass,
        "observed_exceptional_mass": sum(pairings),
        "required_surface_node_candidates": len(candidates),
        "canonical_sha256": EXPECTED_OUT_CANONICAL,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
