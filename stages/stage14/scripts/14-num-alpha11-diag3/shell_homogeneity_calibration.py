#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "stages/stage14/data/14-num-alpha11-diag2/shell50_distribution_summary.json"


def chi2_sf_even_df(x: float, df: int) -> float:
    if df <= 0 or df % 2:
        raise ValueError("this deterministic helper requires positive even df")
    y = x / 2.0
    return math.exp(-y) * sum(y ** k / math.factorial(k) for k in range(df // 2))


def contingency_test(table):
    rows = [sum(r) for r in table]
    cols = [sum(table[i][j] for i in range(len(table))) for j in range(len(table[0]))]
    n = sum(rows)
    chi2 = 0.0
    g = 0.0
    expected_min = float("inf")
    for i, row in enumerate(table):
        for j, obs in enumerate(row):
            exp = rows[i] * cols[j] / n
            expected_min = min(expected_min, exp)
            chi2 += (obs - exp) ** 2 / exp
            if obs:
                g += 2.0 * obs * math.log(obs / exp)
    df = (len(table) - 1) * (len(table[0]) - 1)
    min_dim = min(len(table) - 1, len(table[0]) - 1)
    return {
        "n": n,
        "df": df,
        "pearson_chi2": chi2,
        "pearson_p": chi2_sf_even_df(chi2, df),
        "g_stat": g,
        "g_p": chi2_sf_even_df(g, df),
        "cramers_v": math.sqrt(chi2 / (n * min_dim)),
        "minimum_expected_cell": expected_min,
    }


def holm_adjust(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    adjusted = [0.0] * len(ps)
    running = 0.0
    m = len(ps)
    for rank, idx in enumerate(order):
        value = min(1.0, (m - rank) * ps[idx])
        running = max(running, value)
        adjusted[idx] = running
    return adjusted


def main():
    src = json.loads(SOURCE.read_text(encoding="utf-8"))
    shells = src["shells"]
    if len(shells) != 10 or src["source_rows"] != 3495:
        raise ArithmeticError("diag2 source regression failed")
    table50 = [[s["a"], s["b"], s["c"]] for s in shells]
    if [sum(r) for r in table50] != [s["N2"] for s in shells]:
        raise ArithmeticError("diag2 shell row totals mismatch")

    parents = []
    for i in range(0, 10, 2):
        parents.append([table50[i][j] + table50[i + 1][j] for j in range(3)])

    global50 = contingency_test(table50)
    global100 = contingency_test(parents)
    late_contrast = contingency_test([parents[3], parents[4]])

    adjacent = []
    for i in range(9):
        t = contingency_test([table50[i], table50[i + 1]])
        adjacent.append({
            "from_shell": [shells[i]["lo"], shells[i]["hi"]],
            "to_shell": [shells[i + 1]["lo"], shells[i + 1]["hi"]],
            **t,
        })
    adj_holm = holm_adjust([x["pearson_p"] for x in adjacent])
    for x, p in zip(adjacent, adj_holm):
        x["holm_adjusted_pearson_p"] = p
        x["holm_reject_5pct"] = p < 0.05

    within = []
    for parent_idx, i in enumerate(range(0, 10, 2)):
        t = contingency_test([table50[i], table50[i + 1]])
        within.append({
            "parent_shell": [shells[i]["lo"], shells[i + 1]["hi"]],
            **t,
        })
    within_holm = holm_adjust([x["pearson_p"] for x in within])
    for x, p in zip(within, within_holm):
        x["holm_adjusted_pearson_p"] = p
        x["holm_reject_5pct"] = p < 0.05

    report = {
        "stage": "14-num-alpha11-diag3",
        "classification": "MULTINOMIAL_NULL_CALIBRATION_OF_SHELL_DIRECTION_VARIATION",
        "source": "merged Stage14-num-alpha11-diag2 50m exact shell summary",
        "source_rows": src["source_rows"],
        "null_model": "conditional on each shell N2, directions are multinomial with one common pooled (Ra,Rb,Rc) across shells",
        "global_50m_homogeneity": global50,
        "global_100m_parent_homogeneity": global100,
        "exploratory_300m_400m_vs_400m_500m": {
            **late_contrast,
            "same_data_exploratory_contrast": True,
        },
        "adjacent_50m_pair_tests": adjacent,
        "within_100m_half_tests": within,
        "decision": {
            "GLOBAL_50M_HOMOGENEITY_REJECTED_AT_5PCT": global50["pearson_p"] < 0.05,
            "GLOBAL_100M_PARENT_HOMOGENEITY_REJECTED_AT_5PCT": global100["pearson_p"] < 0.05,
            "ADJACENT_50M_HOLM_ANY_REJECTED_AT_5PCT": any(x["holm_reject_5pct"] for x in adjacent),
            "WITHIN_100M_HOLM_ANY_REJECTED_AT_5PCT": any(x["holm_reject_5pct"] for x in within),
            "OLD_CUMULATIVE_2PCT_GATE_USED": False,
            "IID_ARITHMETIC_OBJECTS_CLAIM": False,
            "ASYMPTOTIC_CLAIM": False,
            "INTERPRETATION": "visible shell swings are not globally decisive against a common multinomial direction law at 50m resolution; aggregated 100m and the selected late contrast are exploratory signals worth arithmetic-class decomposition",
            "NEXT": "Stage14-num-alpha11-diag4 arithmetic-class/congruence decomposition before finer 25m shells",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
