#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "stages" / "stage15" / "scripts"))

from paired_enumerator import enumerate_paired  # noqa: E402

LOCKS = {
    2_000: {"M2": 4_812, "N2": 5},
    100_000: {"M2": 796_698, "N2": 89},
}


def run(bound: int) -> dict:
    _, _, summary = enumerate_paired(bound, materialize_rows=False)
    got = {"M2": summary["M2_total"], "N2": summary["N2_total"]}
    expected = LOCKS[bound]
    if got != expected:
        raise AssertionError(f"B={bound} matched lock mismatch: got={got} expected={expected}")
    if summary["N3_total"] != 0:
        raise AssertionError(f"B={bound}: unexpected integral-space triple N3={summary['N3_total']}")
    if not summary["diagnostics"]["exact_two_glue_multiplicity_one"]:
        raise AssertionError(f"B={bound}: exact-two multiplicity gate failed")
    ratio = summary["N2_total"] / summary["M2_total"]
    return {
        "B": bound,
        "M2": summary["M2_total"],
        "N2": summary["N2_total"],
        "N2_over_M2": ratio,
        "M2_direction_a_b_c": summary["M2_direction_a_b_c"],
        "N2_direction_a_b_c": summary["N2_direction_a_b_c"],
        "M3_total": summary["M3_total"],
        "N3_total": summary["N3_total"],
        "diagnostics": summary["diagnostics"],
    }


def main() -> None:
    rows = [run(2_000), run(100_000)]
    out = {
        "id": "24-14num-r201",
        "classification": "EXACT_FINITE_MATCHED_BOOTSTRAP",
        "population": "primitive canonical exactly-two faces under R<=B; N2 is final space-integral subset",
        "rows": rows,
        "claims": {
            "same_population_matched_ratio": True,
            "finite_diagnostic_only": True,
            "asymptotic_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
        "next": "24-14num-r202 scalable streaming/chunked architecture",
    }
    output = Path(__file__).with_name("bootstrap-summary.json")
    output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    print("R201_STAGE18_B2000_M2_LOCK=PASS")
    print("R201_STAGE19_B2000_N2_LOCK=PASS")
    print("R201_MATCHED_B100K_M2_N2_LOCK=PASS")
    print("R201_EXACT_SAME_RUN_SURVIVOR_CLASSIFICATION=PASS")


if __name__ == "__main__":
    main()
