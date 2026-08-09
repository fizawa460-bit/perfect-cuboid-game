#!/usr/bin/env python3
from __future__ import annotations

import base64
import bz2
import csv
import io
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "stages/stage14/data/14-num-alpha11/b500m_objects.csv.bz2.b64"
DIAG1 = ROOT / "stages/stage14/data/14-num-alpha11-diag1/shell_distribution_summary.json"
STEP = 50_000_000
BMAX = 500_000_000
SHELLS = [(lo, lo + STEP) for lo in range(0, BMAX, STEP)]


def load_rows():
    encoded = "".join(SOURCE.read_text(encoding="ascii").split())
    raw = bz2.decompress(base64.b64decode(encoded)).decode("utf-8")
    rows = [tuple(int(r[k]) for k in ("a", "b", "c", "d", "mask")) for r in csv.DictReader(io.StringIO(raw))]
    if len(rows) != 3495 or len(set(rows)) != 3495:
        raise ArithmeticError(f"B500 source regression failed: rows={len(rows)} unique={len(set(rows))}")
    return rows


def label(mask):
    return {0b011: "a", 0b101: "b", 0b110: "c", 0b111: "triple"}.get(mask)


def summarize_shell(rows, lo, hi):
    counts = {"a": 0, "b": 0, "c": 0, "triple": 0}
    for row in rows:
        if lo < row[3] <= hi:
            q = label(row[4])
            if q is None:
                raise ArithmeticError(f"unexpected mask {row[4]}")
            counts[q] += 1
    n2 = counts["a"] + counts["b"] + counts["c"]
    if n2 == 0:
        raise ArithmeticError(f"empty 50m shell {(lo, hi)}")
    ratios = {q: counts[q] / n2 for q in ("a", "b", "c")}
    se = {q: math.sqrt(ratios[q] * (1.0 - ratios[q]) / n2) for q in ratios}
    return {
        "lo_exclusive": lo,
        "hi_inclusive": hi,
        "N2": n2,
        "counts": counts,
        "ratios": ratios,
        "marginal_binomial_se_descriptive": se,
    }


def shift(x, y):
    return {q: abs(y["ratios"][q] - x["ratios"][q]) for q in ("a", "b", "c")}


def main():
    rows = load_rows()
    shells = [summarize_shell(rows, lo, hi) for lo, hi in SHELLS]

    total = {q: sum(s["counts"][q] for s in shells) for q in ("a", "b", "c", "triple")}
    if (total["a"], total["b"], total["c"], total["triple"]) != (1374, 1371, 750, 0):
        raise ArithmeticError(f"alpha11 total regression failed: {total}")

    diag1 = json.loads(DIAG1.read_text(encoding="utf-8"))
    parent_recomposition = []
    for i, parent in enumerate(diag1["shells"]):
        left, right = shells[2 * i], shells[2 * i + 1]
        recomposed = {
            "a": left["counts"]["a"] + right["counts"]["a"],
            "b": left["counts"]["b"] + right["counts"]["b"],
            "c": left["counts"]["c"] + right["counts"]["c"],
            "triple": left["counts"]["triple"] + right["counts"]["triple"],
            "N2": left["N2"] + right["N2"],
        }
        expected = {q: parent[q] for q in ("a", "b", "c")}
        expected.update({"triple": 0, "N2": parent["N2"]})
        ok = recomposed == expected
        if not ok:
            raise ArithmeticError(f"diag1 parent recomposition failed at index {i}: {recomposed} != {expected}")
        parent_recomposition.append({
            "parent_lo": parent["lo"],
            "parent_hi": parent["hi"],
            "exact": True,
            "first_half_to_second_half_absolute_ratio_shift": shift(left, right),
        })

    adjacent = []
    for x, y in zip(shells, shells[1:]):
        adjacent.append({
            "from_shell": [x["lo_exclusive"], x["hi_inclusive"]],
            "to_shell": [y["lo_exclusive"], y["hi_inclusive"]],
            "absolute_ratio_shift": shift(x, y),
        })

    candidates = []
    for item in adjacent:
        for q, v in item["absolute_ratio_shift"].items():
            candidates.append((v, q, item["from_shell"], item["to_shell"]))
    max_adj = max(candidates)

    half_candidates = []
    for item in parent_recomposition:
        for q, v in item["first_half_to_second_half_absolute_ratio_shift"].items():
            half_candidates.append((v, q, item["parent_lo"], item["parent_hi"]))
    max_half = max(half_candidates)

    report = {
        "stage": "14-num-alpha11-diag2",
        "classification": "B500M_NONOVERLAPPING_50M_SHELL_DIRECTION_DIAGNOSTIC",
        "source": "merged Stage14-num-alpha11 frozen B500m exact census",
        "source_rows": len(rows),
        "global_counts": total,
        "shells": shells,
        "diag1_100m_parent_recomposition": parent_recomposition,
        "adjacent_50m_shell_shifts": adjacent,
        "max_adjacent_50m_absolute_ratio_shift": {
            "value": max_adj[0],
            "direction": max_adj[1],
            "from_shell": max_adj[2],
            "to_shell": max_adj[3],
        },
        "max_within_100m_half_to_half_absolute_ratio_shift": {
            "value": max_half[0],
            "direction": max_half[1],
            "parent_shell": [max_half[2], max_half[3]],
        },
        "interpretation_boundary": {
            "descriptive_only": True,
            "cumulative_2pct_gate_not_reused_as_statistical_significance": True,
            "marginal_standard_errors_not_independence_tests": True,
            "purpose": "test whether diag1 100m movement persists or localizes when each parent shell is split into two exact 50m halves",
        },
        "next": "Stage14-num-alpha11-diag3 statistical fluctuation calibration / shell homogeneity test",
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
