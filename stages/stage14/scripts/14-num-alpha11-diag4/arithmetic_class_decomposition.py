#!/usr/bin/env python3
from __future__ import annotations

import base64
import bz2
import csv
import io
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / "stages/stage14/data/14-num-alpha11/b500m_objects.csv.bz2.b64"
INERT_TEST_PRIMES = (7, 11, 19, 23)
INERT_SANITY_PRIMES = (3, 7, 11, 19, 23)
DIRECTIONS = ("a", "b", "c")
LATE_LO = (300_000_000, 400_000_000)
LATE_HI = (400_000_000, 500_000_000)


def load_rows():
    encoded = "".join(SOURCE.read_text(encoding="ascii").split())
    raw = bz2.decompress(base64.b64decode(encoded)).decode("utf-8")
    rows = [tuple(int(r[k]) for k in ("a", "b", "c", "d", "mask")) for r in csv.DictReader(io.StringIO(raw))]
    if len(rows) != 3495 or len(set(rows)) != 3495:
        raise ArithmeticError(f"B500 source regression failed: rows={len(rows)} unique={len(set(rows))}")
    return rows


def object_view(row):
    a, b, c, d, mask = row
    if mask == 0b011:
        return "a", a, (b, c), b * b + c * c
    if mask == 0b101:
        return "b", b, (a, c), a * a + c * c
    if mask == 0b110:
        return "c", c, (a, b), a * a + b * b
    raise ArithmeticError(f"unexpected non-exactly-two mask: {mask}")


def legendre(n: int, p: int) -> int:
    x = n % p
    if x == 0:
        return 0
    z = pow(x, (p - 1) // 2, p)
    if z == 1:
        return 1
    if z == p - 1:
        return -1
    raise ArithmeticError((n, p, z))


def qr0(n: int, p: int) -> bool:
    return legendre(n, p) >= 0


def chi2_sf_even_df(x: float, df: int) -> float:
    if df <= 0 or df % 2:
        raise ValueError("positive even df required")
    y = x / 2.0
    return math.exp(-y) * sum(y ** k / math.factorial(k) for k in range(df // 2))


def contingency_test(table):
    row_totals = [sum(r) for r in table]
    col_totals = [sum(table[i][j] for i in range(len(table))) for j in range(len(table[0]))]
    n = sum(row_totals)
    chi2 = 0.0
    expected_min = float("inf")
    for i, row in enumerate(table):
        for j, obs in enumerate(row):
            exp = row_totals[i] * col_totals[j] / n
            expected_min = min(expected_min, exp)
            chi2 += (obs - exp) ** 2 / exp
    df = (len(table) - 1) * (len(table[0]) - 1)
    if df <= 0 or df % 2:
        raise ArithmeticError(f"unexpected contingency df={df}")
    return {
        "n": n,
        "df": df,
        "pearson_chi2": chi2,
        "pearson_p": chi2_sf_even_df(chi2, df),
        "cramers_v": math.sqrt(chi2 / (n * min(len(table) - 1, len(table[0]) - 1))),
        "minimum_expected_cell": expected_min,
        "inferential_eligible_min_expected_ge_5": expected_min >= 5.0,
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


def partition_specs():
    specs = [
        ("d_mod8", "parity_geometry", lambda row, view: str(row[3] % 8)),
        ("d_mod16", "parity_geometry", lambda row, view: str(row[3] % 16)),
        ("shared_edge_parity", "parity_geometry", lambda row, view: str(view[1] & 1)),
        ("shared_edge_mod4", "parity_geometry", lambda row, view: str(view[1] % 4)),
        ("shared_edge_mod8", "parity_geometry", lambda row, view: str(view[1] % 8)),
        ("nonshared_parity_pair", "parity_geometry", lambda row, view: f"{view[2][0]&1}{view[2][1]&1}"),
    ]
    for p in INERT_TEST_PRIMES:
        specs.extend([
            (f"p{p}_d_legendre", "inert_diagonal", lambda row, view, p=p: str(legendre(row[3], p))),
            (f"p{p}_missing_face_qr0", "inert_missing_face", lambda row, view, p=p: "pass" if qr0(view[3], p) else "fail"),
            (f"p{p}_shared_divisible", "inert_divisibility", lambda row, view, p=p: "yes" if view[1] % p == 0 else "no"),
            (f"p{p}_nonshared_zero_count", "inert_divisibility", lambda row, view, p=p: str(sum(x % p == 0 for x in view[2]))),
        ])
    return specs


def class_direction_table(rows, keyfn):
    counts = defaultdict(lambda: Counter({q: 0 for q in DIRECTIONS}))
    for row in rows:
        view = object_view(row)
        counts[keyfn(row, view)][view[0]] += 1
    classes = sorted(counts)
    table = [[counts[k][q] for q in DIRECTIONS] for k in classes]
    return classes, table, counts


def direction_ratios(rows):
    c = Counter(object_view(r)[0] for r in rows)
    n = sum(c.values())
    return {q: c[q] / n for q in DIRECTIONS}


def vec_norm(v):
    return math.sqrt(sum(x * x for x in v))


def late_mixture_decomposition(rows, keyfn):
    lo_rows = [r for r in rows if LATE_LO[0] < r[3] <= LATE_LO[1]]
    hi_rows = [r for r in rows if LATE_HI[0] < r[3] <= LATE_HI[1]]
    if len(lo_rows) != 328 or len(hi_rows) != 301:
        raise ArithmeticError(f"late shell regression failed: {len(lo_rows)}, {len(hi_rows)}")

    combined = lo_rows + hi_rows
    class_dir = defaultdict(Counter)
    class_total = Counter()
    for row in combined:
        view = object_view(row)
        k = keyfn(row, view)
        class_dir[k][view[0]] += 1
        class_total[k] += 1

    classes = sorted(class_total)
    weights = {}
    for tag, subset in (("lo", lo_rows), ("hi", hi_rows)):
        mix = Counter(keyfn(r, object_view(r)) for r in subset)
        weights[tag] = {k: mix[k] / len(subset) for k in classes}

    cond = {k: {q: class_dir[k][q] / class_total[k] for q in DIRECTIONS} for k in classes}
    predicted = {}
    for tag in ("lo", "hi"):
        predicted[tag] = {q: sum(weights[tag][k] * cond[k][q] for k in classes) for q in DIRECTIONS}

    observed = {"lo": direction_ratios(lo_rows), "hi": direction_ratios(hi_rows)}
    obs_shift = [observed["hi"][q] - observed["lo"][q] for q in DIRECTIONS]
    pred_shift = [predicted["hi"][q] - predicted["lo"][q] for q in DIRECTIONS]
    residual = [obs_shift[i] - pred_shift[i] for i in range(3)]
    obs_norm = vec_norm(obs_shift)
    pred_norm = vec_norm(pred_shift)
    residual_norm = vec_norm(residual)
    cosine = 0.0 if pred_norm == 0 or obs_norm == 0 else sum(a*b for a, b in zip(obs_shift, pred_shift)) / (obs_norm * pred_norm)
    tv = 0.5 * sum(abs(weights["hi"][k] - weights["lo"][k]) for k in classes)
    return {
        "class_count": len(classes),
        "late_class_mix_total_variation": tv,
        "observed_direction_ratios": observed,
        "mixture_only_predicted_direction_ratios": predicted,
        "observed_shift_hi_minus_lo": {q: obs_shift[i] for i, q in enumerate(DIRECTIONS)},
        "mixture_predicted_shift_hi_minus_lo": {q: pred_shift[i] for i, q in enumerate(DIRECTIONS)},
        "observed_shift_l2": obs_norm,
        "mixture_predicted_shift_l2": pred_norm,
        "residual_shift_l2": residual_norm,
        "mixture_explained_fraction_l2": 1.0 - residual_norm / obs_norm if obs_norm else 0.0,
        "shift_cosine_alignment": cosine,
        "same_data_descriptive_only": True,
    }


def local_missing_face_panel(rows):
    panel = {}
    for p in INERT_SANITY_PRIMES:
        by_dir = {}
        total_pass = 0
        for q in DIRECTIONS:
            subset = [r for r in rows if object_view(r)[0] == q]
            passes = sum(qr0(object_view(r)[3], p) for r in subset)
            total_pass += passes
            by_dir[q] = {"pass": passes, "total": len(subset), "rate": passes / len(subset)}
        panel[str(p)] = {
            "overall_pass": total_pass,
            "overall_total": len(rows),
            "overall_rate": total_pass / len(rows),
            "by_direction": by_dir,
            "stage13_lambda_p_context_only": (p + 5) / (2 * (p + 1)),
            "stage13_lambda_p_is_not_a_null_expectation_for_exactly_two_to_third_face": True,
        }
    return panel


def main():
    rows = load_rows()
    totals = Counter(object_view(r)[0] for r in rows)
    if tuple(totals[q] for q in DIRECTIONS) != (1374, 1371, 750):
        raise ArithmeticError(f"direction total regression failed: {totals}")
    if any(r[4] == 0b111 for r in rows):
        raise ArithmeticError("unexpected triple in frozen B500 source")
    if any(r[3] % 4 != 1 for r in rows):
        raise ArithmeticError("primitive two-face diagonal d mod 4 support regression failed")
    for p in INERT_SANITY_PRIMES:
        if any(r[3] % p == 0 for r in rows):
            raise ArithmeticError(f"inert prime {p} unexpectedly divides primitive diagonal")

    results = []
    for name, family, keyfn in partition_specs():
        classes, table, _ = class_direction_table(rows, keyfn)
        if len(classes) < 2:
            results.append({
                "name": name,
                "family": family,
                "classes": classes,
                "testable": False,
                "reason": "only one observed class",
                "late_mixture": late_mixture_decomposition(rows, keyfn),
            })
            continue
        test = contingency_test(table)
        results.append({
            "name": name,
            "family": family,
            "classes": classes,
            "table_class_by_direction_abc": table,
            "testable": True,
            **test,
            "late_mixture": late_mixture_decomposition(rows, keyfn),
        })

    eligible = [r for r in results if r.get("testable") and r["inferential_eligible_min_expected_ge_5"]]
    holm = holm_adjust([r["pearson_p"] for r in eligible])
    for r, p_adj in zip(eligible, holm):
        r["holm_adjusted_pearson_p_across_predeclared_eligible_partitions"] = p_adj
        r["holm_reject_5pct"] = p_adj < 0.05
    for r in results:
        if "holm_adjusted_pearson_p_across_predeclared_eligible_partitions" not in r:
            r["holm_adjusted_pearson_p_across_predeclared_eligible_partitions"] = None
            r["holm_reject_5pct"] = False

    eligible_sorted_p = sorted(eligible, key=lambda r: r["holm_adjusted_pearson_p_across_predeclared_eligible_partitions"])
    testable = [r for r in results if r.get("testable")]
    strongest_v = max(testable, key=lambda r: r["cramers_v"])
    best_mix = max(results, key=lambda r: r["late_mixture"]["mixture_explained_fraction_l2"])
    family_top = {}
    for family in sorted({r["family"] for r in testable}):
        fam = [r for r in testable if r["family"] == family]
        family_top[family] = max(fam, key=lambda r: r["cramers_v"])["name"]

    local_panel = local_missing_face_panel(rows)
    report = {
        "stage": "14-num-alpha11-diag4",
        "classification": "PREDECLARED_ARITHMETIC_CLASS_AND_INERT_CONGRUENCE_DECOMPOSITION",
        "source": "merged Stage14-num-alpha11 frozen exact B500m 3495-row object source",
        "source_rows": len(rows),
        "global_direction_counts": {q: totals[q] for q in DIRECTIONS},
        "predeclared_partition_count": len(results),
        "inferential_eligible_partition_count": len(eligible),
        "partition_results": results,
        "missing_third_face_inert_qr0_panel": local_panel,
        "selection_summary": {
            "smallest_holm_partition": eligible_sorted_p[0]["name"] if eligible_sorted_p else None,
            "smallest_holm_adjusted_p": eligible_sorted_p[0]["holm_adjusted_pearson_p_across_predeclared_eligible_partitions"] if eligible_sorted_p else None,
            "any_holm_reject_5pct": any(r["holm_reject_5pct"] for r in eligible),
            "strongest_cramers_v_partition": strongest_v["name"],
            "strongest_cramers_v": strongest_v["cramers_v"],
            "best_late_mixture_partition": best_mix["name"],
            "best_late_mixture_explained_fraction_l2": best_mix["late_mixture"]["mixture_explained_fraction_l2"],
            "best_late_mixture_shift_cosine_alignment": best_mix["late_mixture"]["shift_cosine_alignment"],
            "family_top_by_cramers_v": family_top,
        },
        "interpretation_boundary": {
            "partitions_predeclared_before_reading_diag4_output": True,
            "holm_family": "all testable partitions with minimum expected cell >=5",
            "sparse_partitions_inferentially_excluded": True,
            "late_300m_400m_vs_400m_500m_mixture_decomposition_is_same_data_descriptive": True,
            "stage13_lambda_p_values_are_context_only_not_null_expectations_here": True,
            "iid_arithmetic_objects_claim": False,
            "asymptotic_claim": False,
        },
        "decision": {
            "ARITHMETIC_CLASS_DECOMPOSITION_COMPLETE": True,
            "HOLM_CORRECTED_DIRECTION_ASSOCIATION_FOUND": any(r["holm_reject_5pct"] for r in eligible),
            "LATE_SHELL_SHIFT_FULLY_EXPLAINED_BY_TESTED_CLASS_MIXTURE": best_mix["late_mixture"]["mixture_explained_fraction_l2"] >= 0.8 and best_mix["late_mixture"]["shift_cosine_alignment"] >= 0.8,
            "FINER_25M_SHELLS_RECOMMENDED_NEXT": False,
            "IID_ARITHMETIC_OBJECTS_CLAIM": False,
            "ASYMPTOTIC_CLAIM": False,
            "NEXT": "Stage14-num-alpha11-diag5 family/cluster dependence and same-diagonal multiplicity diagnostics, informed by the strongest diag4 arithmetic partitions",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
