#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
PROD = ROOT / "stages/stage32/residual-32-01-production"

def load(name: str):
    return json.loads((PROD / name).read_text(encoding="utf-8"))

hard = load("full178-resumable-generation38-256m-hard-tail-diagnostic-main-checkpoint.json")
volume = load("full178-resumable-generation38-residual-volume-main-checkpoint.json")
state = load("state.json")
indexed = load("full178-prefix-indexed-compression-main-checkpoint.json")

expected = {
    "g0-d008": ((18, 22), 30, 8),
    "g0-d010": ((18, 23), 38, 15),
    "g0-d012": ((17, 22), 45, 23),
    "g0-d014": ((16, 22), 53, 31),
    "g0-d016": ((16, 23), 60, 37),
    "g0-d018": ((16, 21), 68, 47),
    "g0-d020": ((16, 21), 76, 55),
    "g0-d022": ((15, 21), 83, 62),
}

assert hard["exact_transition"]["survived_count"] == 52
assert hard["survivor_mechanism"]["same_e_after_full_256m"] == 52
assert hard["survivor_mechanism"]["unique_survivor_rows"] == 8
assert hard["survivor_mechanism"]["interpretation_is_theorem"] is False

growth = volume["row_tail_growth"]
assert set(growth) == set(expected)
later_total = 0
for row_id, (expected_range, expected_emax, expected_later) in expected.items():
    rec = growth[row_id]
    d = int(row_id.split("-d", 1)[1])
    assert d in range(8, 23, 2)
    assert tuple(rec["current_e_range"]) == expected_range
    assert rec["emax"] == expected_emax == (19 * d) // 5
    assert rec["later_e"] == expected_later == expected_emax - expected_range[1]
    later_total += rec["later_e"]

assert later_total == 278
assert volume["current_frontier_measurement"]["later_e_strata_owned_by_row_tail_sources"] == 278
assert volume["current_frontier_measurement"]["unique_rows"] == 8
assert volume["current_frontier_measurement"]["frontier_count"] == 52

pic = state["resumable_hardness_avoidance"]["prefix_indexed_compression"]
assert pic["gen38_52_unit_prefix_frontier_status"] == "SUPERSEDED_AS_PREFIX_FAMILY_ENUMERATION_MECHANISM"
assert pic["historical_gen38_evidence_revoked"] is False
assert pic["terminal_set_semantics_preserved"] is True
assert pic["numerical_picard_leaf_checks_complete"] is False

idx = indexed["indexed_reparameterization"]
assert idx["conclusion"] == "success"
assert idx["terminal_set_semantics_preserved"] is True
assert idx["random_access_unrank"] is True
assert idx["inverse_rank"] is True
assert idx["small_family_full_set_bijection_checked"] is True
assert indexed["gen38_frontier_interpretation"]["status_for_prefix_family_representation"] == \
    "SUPERSEDED_BY_EXACT_SYMBOLIC_COUNT_PLUS_INDEXED_RANDOM_ACCESS"
assert indexed["symbolic_full178_prefix_census"]["numerical_picard_leaf_checks_complete"] is False

constraints = indexed["exact_terminal_family"]["constraints"]
assert constraints == [
    "all xi >= 0",
    "sum(xi for i != 4) <= e",
    "0 <= x4 <= 19*d-5*e",
    "x0 <= x1",
    "if x0==x1 then (x5,x6) <=lex (x8,x9)",
    "x1+x8+x9+x10 == 0 (mod 2)",
]

print(json.dumps({
    "result": "PASS_N102_EXACT_HARD_TAIL_STRUCTURAL_REDUCTION",
    "row_family": list(expected),
    "later_e_total": later_total,
    "historical_survivors": 52,
    "prefix_enumeration": "SUPERSEDED_BY_EXACT_INDEXED_TERMINAL_REPARAMETERIZATION",
    "numerical_picard_leaf_checks_complete": False
}, sort_keys=True))
