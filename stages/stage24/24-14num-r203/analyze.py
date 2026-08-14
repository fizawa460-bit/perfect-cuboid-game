#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

DIRECTIONS = ("a", "b", "c")


def effective_exponent(y0: int | float, y1: int | float, b0: int, b1: int) -> float:
    return math.log(y1 / y0) / math.log(b1 / b0)


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit and summarize the finite r201/r202 matched census")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    source = json.loads(args.input.read_text(encoding="utf-8"))
    rows = source["rows"]
    if [row["B"] for row in rows] != [2000, 100000, 200000, 500000, 1000000]:
        raise AssertionError("unexpected cutoff ladder")

    enriched = []
    for row in rows:
        if sum(row["M2_direction_a_b_c"]) != row["M2"]:
            raise AssertionError(f"M2 direction sum mismatch at B={row['B']}")
        if sum(row["N2_direction_a_b_c"]) != row["N2"]:
            raise AssertionError(f"N2 direction sum mismatch at B={row['B']}")
        ratios = [n / m for n, m in zip(row["N2_direction_a_b_c"], row["M2_direction_a_b_c"])]
        enriched.append({
            **row,
            "N2_over_M2": row["N2"] / row["M2"],
            "directional_N2_over_M2_a_b_c": ratios,
            "directional_ratio_spread_max_over_min": max(ratios) / min(ratios),
        })

    intervals = []
    for left, right in zip(enriched, enriched[1:]):
        m_exp = effective_exponent(left["M2"], right["M2"], left["B"], right["B"])
        n_exp = effective_exponent(left["N2"], right["N2"], left["B"], right["B"])
        intervals.append({
            "B0": left["B"],
            "B1": right["B"],
            "M2_effective_exponent": m_exp,
            "N2_effective_exponent": n_exp,
            "ratio_effective_exponent": n_exp - m_exp,
        })

    ratios = [row["N2_over_M2"] for row in enriched]
    if not all(a > b for a, b in zip(ratios, ratios[1:])):
        raise AssertionError("observed survivor ratios are not strictly decreasing")

    row_100k = next(row for row in enriched if row["B"] == 100000)
    row_1m = next(row for row in enriched if row["B"] == 1000000)
    decade_m_exp = effective_exponent(row_100k["M2"], row_1m["M2"], 100000, 1000000)
    decade_n_exp = effective_exponent(row_100k["N2"], row_1m["N2"], 100000, 1000000)

    output = {
        "id": "24-14num-r203",
        "classification": "FINITE_MATCHED_RATIO_AUDIT_AND_INTERPRETATION",
        "population_contract_match": "EXACT",
        "rows": enriched,
        "intervals": intervals,
        "decade_100k_to_1m": {
            "M2_growth_factor": row_1m["M2"] / row_100k["M2"],
            "N2_growth_factor": row_1m["N2"] / row_100k["N2"],
            "ratio_decrease_factor": row_100k["N2_over_M2"] / row_1m["N2_over_M2"],
            "M2_effective_exponent": decade_m_exp,
            "N2_effective_exponent": decade_n_exp,
            "ratio_effective_exponent": decade_n_exp - decade_m_exp,
        },
        "observations": {
            "finite_survivor_ratio_strictly_decreases_on_sampled_ladder": True,
            "directional_survivor_rates_are_equal": False,
            "one_million_directional_order": [
                direction
                for _, direction in sorted(
                    zip(row_1m["directional_N2_over_M2_a_b_c"], DIRECTIONS), reverse=True
                )
            ],
        },
        "claims": {
            "exact_finite_census": True,
            "asymptotic_exponent_claim": False,
            "monotonicity_beyond_sampled_cutoffs_claim": False,
            "directional_limit_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
        "next_computation": {
            "required_now": False,
            "automatic_execution": False,
            "reopen_trigger": "a_later_Stage24_checkpoint_needs_to_distinguish_specific_candidate_laws_or_test_directional_stabilization",
        },
        "provenance": source["provenance"],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    print("R203_INPUT_TOTALS_AND_DIRECTIONS=PASS")
    print("R203_RATIO_AUDIT=PASS")
    print("R203_NO_ASYMPTOTIC_PROMOTION=PASS")
    print("R203_ADDITIONAL_COMPUTATION_REQUIRED=false")


if __name__ == "__main__":
    main()
