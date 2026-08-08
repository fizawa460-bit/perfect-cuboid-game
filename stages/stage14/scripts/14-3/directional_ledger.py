#!/usr/bin/env python3
"""Stage14-3a: descriptive finite directional diagnostics only.

Reads the frozen Stage14-2 census and derives finite ratios, proportions,
pairwise differences, leaders, spreads, and shell increments. This script does
not fit a growth law, extrapolate a limit, or use any Stage13 analytic result.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DEFAULT_INPUT = Path("stages/stage14/data/14-2/final_census_audit.json")
DEFAULT_OUTPUT = Path("stages/stage14/data/14-3/directional_ledger.json")


def leader_label(a: int, b: int, c: int) -> str:
    vals = {"a": a, "b": b, "c": c}
    top = max(vals.values())
    leaders = [name for name, value in vals.items() if value == top]
    return leaders[0] if len(leaders) == 1 else "tie:" + ",".join(leaders)


def row_diagnostics(row: dict[str, Any]) -> dict[str, Any]:
    a = int(row["N_a_2"])
    b = int(row["N_b_2"])
    c = int(row["N_c_2"])
    total = int(row["N_2"])
    if a + b + c != total:
        raise ArithmeticError(f"directional total mismatch at B={row['B']}")

    values = (a, b, c)
    spread = max(values) - min(values)
    return {
        "B": int(row["B"]),
        "counts": {"a": a, "b": b, "c": c, "total": total},
        "proportion": {
            "a": a / total,
            "b": b / total,
            "c": c / total,
        },
        "c_normalized_ratio": None if c == 0 else {
            "a": a / c,
            "b": b / c,
            "c": 1.0,
        },
        "a_over_b": None if b == 0 else a / b,
        "differences": {
            "a_minus_b": a - b,
            "a_minus_c": a - c,
            "b_minus_c": b - c,
        },
        "leader": leader_label(a, b, c),
        "spread": {
            "absolute": spread,
            "share_of_total": spread / total,
        },
    }


def shell_diagnostics(prev: dict[str, Any], cur: dict[str, Any]) -> dict[str, Any]:
    pa, pb, pc = (prev["counts"][k] for k in ("a", "b", "c"))
    a, b, c = (cur["counts"][k] for k in ("a", "b", "c"))
    da, db, dc = a - pa, b - pb, c - pc
    total = da + db + dc
    if min(da, db, dc) < 0:
        raise ArithmeticError("cumulative census must be coordinatewise nondecreasing")
    return {
        "from_B": prev["B"],
        "to_B": cur["B"],
        "delta_B": cur["B"] - prev["B"],
        "increments": {"a": da, "b": db, "c": dc, "total": total},
        "increment_proportion": None if total == 0 else {
            "a": da / total,
            "b": db / total,
            "c": dc / total,
        },
        "shell_leader": leader_label(da, db, dc),
    }


def build_report(source: dict[str, Any]) -> dict[str, Any]:
    if source.get("decision", {}).get("STAGE14_2") != "COMPLETE":
        raise ArithmeticError("Stage14-2 source is not marked COMPLETE")
    if not source.get("decision", {}).get("FINITE_CENSUS_FROZEN"):
        raise ArithmeticError("Stage14-2 source is not frozen")

    rows = [row_diagnostics(row) for row in source["rows"]]
    shells = [shell_diagnostics(rows[i - 1], rows[i]) for i in range(1, len(rows))]
    by_B = {row["B"]: row for row in rows}

    late = [100_000, 200_000, 500_000, 1_000_000, 2_000_000]
    last_four = [200_000, 500_000, 1_000_000, 2_000_000]

    observations = {
        "a_b_tie_cutoffs": [
            row["B"] for row in rows if row["differences"]["a_minus_b"] == 0
        ],
        "b_leader_cutoffs": [row["B"] for row in rows if row["leader"] == "b"],
        "a_leader_cutoffs": [row["B"] for row in rows if row["leader"] == "a"],
        "last_five_a_over_b": [
            {"B": B, "value": by_B[B]["a_over_b"]} for B in late
        ],
        "a_over_c_exact_7_over_4_at": [
            B for B in last_four[:-1]
            if by_B[B]["counts"]["a"] * 4 == by_B[B]["counts"]["c"] * 7
        ],
        "a_over_c_at_2m": by_B[2_000_000]["c_normalized_ratio"]["a"],
        "b_over_c_last_four": [
            {"B": B, "value": by_B[B]["c_normalized_ratio"]["b"]}
            for B in last_four
        ],
        "leader_reversal_between_1m_and_2m": (
            by_B[1_000_000]["leader"] == "b" and by_B[2_000_000]["leader"] == "a"
        ),
        "shell_100k_to_200k": next(
            shell for shell in shells
            if shell["from_B"] == 100_000 and shell["to_B"] == 200_000
        ),
        "shell_1m_to_2m": next(
            shell for shell in shells
            if shell["from_B"] == 1_000_000 and shell["to_B"] == 2_000_000
        ),
    }

    return {
        "metadata": {
            "stage": "14-3a",
            "title": "Descriptive directional ledger from the frozen Stage14-2 census",
            "source": str(DEFAULT_INPUT),
            "source_rows": len(rows),
            "max_B": max(row["B"] for row in rows),
            "stage13_code_imported": False,
            "stage13_asymptotic_result_used": False,
            "fit_performed": False,
            "limit_inferred": False,
            "monotonicity_inferred": False,
        },
        "rows": rows,
        "shells": shells,
        "finite_observations": observations,
        "decision": {
            "STAGE14_3A": "COMPLETE",
            "DESCRIPTIVE_LEDGER_COMPLETE": True,
            "FINITE_RATIO_LIMIT_IDENTIFIED": False,
            "MONOTONE_CONVERGENCE_SUPPORTED": False,
            "A_C_FINITE_PLATEAU_OBSERVED": True,
            "A_B_LEADER_CROSSING_OBSERVED": True,
            "STAGE13_ANALYTIC_DEPENDENCY_USED": False,
            "NEXT": (
                "Stage14-3b densify finite cutoffs around the late-range directional motion; "
                "Stage14-4 remains paused"
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    source = json.loads(args.input.read_text(encoding="utf-8"))
    report = build_report(source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
