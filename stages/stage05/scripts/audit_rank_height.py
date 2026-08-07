#!/usr/bin/env python3
"""Stage-five arithmetic audit for the two-face cuboid elliptic fibers.

This script performs three separate calculations.

1. Retry the three observed fibers whose PARI/GP 2-descent rank interval was
   previously 1..3, using larger effort values.
2. Recover the saturated rank-one generator for lambda=7/32 and verify the
   exact relation between that generator and the observed cuboid point.
3. Compute PARI canonical heights for all 255 observed points and compare them
   empirically with log(d), the logarithmic height of lambda, and the naive
   x-coordinate height.

The height section is a finite-data diagnostic only. Regression or correlation
on 255 points is not a uniform height comparison and gives no point-counting
bound on the K3 surface.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from fractions import Fraction
from pathlib import Path
from statistics import mean
from typing import Any

from analyze_two_face_mordell_weil import (
    generic_torsion_subgroup,
    point_add,
    point_mul,
    point_on_curve,
)


DEFAULT_RELATIONS = Path("data/two_face_cuboids_1e6_mordell_weil_relations.json")
UNRESOLVED_LAMBDAS = ("81/385", "147/194", "119/130")
GENERATOR_LAMBDA = "7/32"
GENERATOR_SOURCE_INDEX = 224
Point = tuple[Fraction, Fraction] | None


def parse_fraction(record: dict[str, Any]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def point_from_record(record: dict[str, Any]) -> Point:
    if record.get("infinity"):
        return None
    return parse_fraction(record["x"]), parse_fraction(record["y"])


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def fraction_record(value: Fraction) -> dict[str, int | str]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": fraction_text(value),
    }


def point_record(point: Point) -> dict[str, Any]:
    if point is None:
        return {"infinity": True}
    return {
        "infinity": False,
        "x": fraction_record(point[0]),
        "y": fraction_record(point[1]),
    }


def gp_fraction(value: Fraction) -> str:
    return fraction_text(value) if value.denominator == 1 else f"({fraction_text(value)})"


def gp_point(point: Point) -> str:
    if point is None:
        return "[0]"
    return f"[{gp_fraction(point[0])},{gp_fraction(point[1])}]"


def curve_coefficients(lam: Fraction) -> tuple[Fraction, Fraction]:
    a2 = 4 * lam * lam + (lam * lam + 1) ** 2
    a4 = 4 * lam * lam * (lam * lam + 1) ** 2
    return a2, a4


def run_gp(script: str, timeout: int) -> str:
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP executable 'gp' was not found")
    completed = subprocess.run(
        [gp, "-q"],
        input=script,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    raw = completed.stdout + completed.stderr
    if completed.returncode != 0 or "***" in raw:
        raise RuntimeError(f"PARI/GP failed:\n{raw}")
    return raw


def integer_field(raw: str, name: str) -> int:
    match = re.search(rf"^{re.escape(name)}=(-?\d+)\s*$", raw, re.MULTILINE)
    if not match:
        raise RuntimeError(f"missing {name} in PARI output:\n{raw}")
    return int(match.group(1))


def text_field(raw: str, name: str) -> str:
    match = re.search(rf"^{re.escape(name)}=(.+?)\s*$", raw, re.MULTILINE)
    if not match:
        raise RuntimeError(f"missing {name} in PARI output:\n{raw}")
    return match.group(1).strip()


def parse_gp_fraction(text: str) -> Fraction:
    value = text.strip()
    if value.startswith("(") and value.endswith(")"):
        value = value[1:-1]
    return Fraction(value)


def parse_gp_point(text: str) -> Point:
    value = text.strip()
    if value == "[0]":
        return None
    match = re.fullmatch(r"\[\s*([^,]+),\s*([^\]]+)\s*\]", value)
    if not match:
        raise ValueError(f"unsupported PARI point format: {text}")
    return parse_gp_fraction(match.group(1)), parse_gp_fraction(match.group(2))


def load_payload(path: Path) -> tuple[dict[str, Any], dict[int, dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    points = payload.get("points", [])
    by_index = {int(item["source_index"]): item for item in points}
    by_lambda: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in points:
        by_lambda[str(item["lambda"])].append(item)
    return payload, by_index, by_lambda


def retry_one_rank(
    lam_text: str,
    items: list[dict[str, Any]],
    efforts: list[int],
    timeout_per_attempt: int,
) -> dict[str, Any]:
    lam = Fraction(lam_text)
    a2, a4 = curve_coefficients(lam)
    observed = point_from_record(items[0]["weierstrass_point"])
    attempts: list[dict[str, Any]] = []
    for effort in efforts:
        script = f"""
default(realprecision,80);
E=ellinit([0,{gp_fraction(a2)},0,{gp_fraction(a4)},0]);
P={gp_point(observed)};
R=ellrank(E,{effort},[P]);
print("RANK_LOWER=",R[1]);
print("RANK_UPPER=",R[2]);
print("SHA2_INFO=",R[3]);
print("FOUND_GENERATOR_COUNT=",#R[4]);
print("ROOT_NUMBER=",ellrootno(E));
quit;
"""
        try:
            raw = run_gp(script, timeout_per_attempt)
            attempt = {
                "effort": effort,
                "status": "success",
                "rank_lower_bound": integer_field(raw, "RANK_LOWER"),
                "rank_upper_bound": integer_field(raw, "RANK_UPPER"),
                "sha_2_information": integer_field(raw, "SHA2_INFO"),
                "found_generator_count": integer_field(raw, "FOUND_GENERATOR_COUNT"),
                "root_number": integer_field(raw, "ROOT_NUMBER"),
                "raw_pari_output": raw,
            }
            attempt["rank_exact"] = (
                attempt["rank_lower_bound"] == attempt["rank_upper_bound"]
            )
        except subprocess.TimeoutExpired as exc:
            attempt = {
                "effort": effort,
                "status": "timeout",
                "error": str(exc),
            }
        except Exception as exc:  # preserve a reproducible failed attempt
            attempt = {
                "effort": effort,
                "status": "error",
                "error": str(exc),
            }
        attempts.append(attempt)
        if attempt.get("rank_exact"):
            break
    final = attempts[-1]
    return {
        "lambda": lam_text,
        "source_indices": [int(item["source_index"]) for item in items],
        "attempts": attempts,
        "resolved": bool(final.get("rank_exact")),
        "final_rank_lower_bound": final.get("rank_lower_bound"),
        "final_rank_upper_bound": final.get("rank_upper_bound"),
    }


def retry_unresolved_ranks(
    by_lambda: dict[str, list[dict[str, Any]]],
    efforts: list[int],
    timeout_per_attempt: int,
) -> dict[str, Any]:
    missing = [lam for lam in UNRESOLVED_LAMBDAS if lam not in by_lambda]
    if missing:
        raise ValueError(f"unresolved lambda values missing from input: {missing}")
    results: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        future_map = {
            executor.submit(
                retry_one_rank,
                lam,
                by_lambda[lam],
                efforts,
                timeout_per_attempt,
            ): lam
            for lam in UNRESOLVED_LAMBDAS
        }
        for future in as_completed(future_map):
            results.append(future.result())
    results.sort(key=lambda item: Fraction(item["lambda"]))
    return {
        "target_count": len(results),
        "resolved_count": sum(item["resolved"] for item in results),
        "unresolved_count": sum(not item["resolved"] for item in results),
        "effort_sequence": efforts,
        "fibers": results,
    }


def identify_generator_relation(observed: Point, generator: Point, lam: Fraction) -> dict[str, Any] | None:
    torsion = generic_torsion_subgroup(lam)
    for coefficient in (-2, 2):
        multiple = point_mul(coefficient, generator, lam)
        for entry in torsion:
            if point_add(multiple, entry["point"], lam) == observed:
                return {
                    "generator_coefficient": coefficient,
                    "torsion_label": entry["label"],
                    "formula": f"P={coefficient}G+{entry['label']}",
                }
    return None


def audit_generator_7_32(
    by_index: dict[int, dict[str, Any]],
    saturation_bound: int,
    timeout: int,
) -> dict[str, Any]:
    item = by_index.get(GENERATOR_SOURCE_INDEX)
    if item is None:
        raise ValueError(f"source index {GENERATOR_SOURCE_INDEX} is missing")
    if str(item["lambda"]) != GENERATOR_LAMBDA:
        raise ValueError(
            f"source index {GENERATOR_SOURCE_INDEX} has lambda={item['lambda']}"
        )
    lam = Fraction(GENERATOR_LAMBDA)
    a2, a4 = curve_coefficients(lam)
    observed = point_from_record(item["weierstrass_point"])
    script = f"""
default(realprecision,100);
E=ellinit([0,{gp_fraction(a2)},0,{gp_fraction(a4)},0]);
P={gp_point(observed)};
W=ellsaturation(E,[P],{saturation_bound});
print("SATURATED_GENERATOR_COUNT=",#W);
print("SATURATED_GENERATOR=",W[1]);
regP=matdet(ellheightmatrix(E,[P]));
regW=matdet(ellheightmatrix(E,W));
print("OBSERVED_REGULATOR=",regP);
print("SATURATED_REGULATOR=",regW);
print("INDEX_SQUARED=",round(regP/regW));
quit;
"""
    raw = run_gp(script, timeout)
    generator = parse_gp_point(text_field(raw, "SATURATED_GENERATOR"))
    if not point_on_curve(generator, lam):
        raise ArithmeticError("PARI saturated generator is not on the curve")
    relation = identify_generator_relation(observed, generator, lam)
    return {
        "valid": relation is not None,
        "lambda": GENERATOR_LAMBDA,
        "source_index": GENERATOR_SOURCE_INDEX,
        "source_tuple": item["source_tuple"],
        "saturation_bound": saturation_bound,
        "observed_point": point_record(observed),
        "saturated_generator": point_record(generator),
        "saturated_generator_count": integer_field(raw, "SATURATED_GENERATOR_COUNT"),
        "observed_regulator_raw": text_field(raw, "OBSERVED_REGULATOR"),
        "saturated_regulator_raw": text_field(raw, "SATURATED_REGULATOR"),
        "index_squared": integer_field(raw, "INDEX_SQUARED"),
        "exact_relation": relation,
        "raw_pari_output": raw,
        "scope": {
            "certified": (
                "the displayed group-law relation is an exact rational identity; "
                f"the PARI saturation result excludes index primes below {saturation_bound}"
            ),
            "not_certified": (
                "full saturation at primes at or above the chosen bound"
            ),
        },
    }


def canonical_heights(
    points: list[dict[str, Any]],
    timeout: int,
) -> dict[int, float]:
    lines = ["default(realprecision,80);"]
    for item in points:
        source_index = int(item["source_index"])
        lam = Fraction(str(item["lambda"]))
        a2, a4 = curve_coefficients(lam)
        point = point_from_record(item["weierstrass_point"])
        lines.extend(
            [
                f"E=ellinit([0,{gp_fraction(a2)},0,{gp_fraction(a4)},0]);",
                f"P={gp_point(point)};",
                f'print("HEIGHT|{source_index}|",ellheight(E,P));',
            ]
        )
    lines.append("quit;")
    raw = run_gp("\n".join(lines) + "\n", timeout)
    heights: dict[int, float] = {}
    for match in re.finditer(r"^HEIGHT\|(\d+)\|(.+?)\s*$", raw, re.MULTILINE):
        heights[int(match.group(1))] = float(match.group(2))
    if len(heights) != len(points):
        missing = sorted(
            int(item["source_index"])
            for item in points
            if int(item["source_index"]) not in heights
        )
        raise RuntimeError(f"missing canonical heights for source indices {missing}")
    return heights


def pearson(left: list[float], right: list[float]) -> float | None:
    if len(left) != len(right) or len(left) < 2:
        return None
    ml = mean(left)
    mr = mean(right)
    numerator = sum((x - ml) * (y - mr) for x, y in zip(left, right))
    dl = math.sqrt(sum((x - ml) ** 2 for x in left))
    dr = math.sqrt(sum((y - mr) ** 2 for y in right))
    return None if dl == 0 or dr == 0 else numerator / (dl * dr)


def solve_linear_system(matrix: list[list[float]], vector: list[float]) -> list[float]:
    n = len(vector)
    augmented = [row[:] + [vector[i]] for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = max(range(column, n), key=lambda row: abs(augmented[row][column]))
        if abs(augmented[pivot][column]) < 1e-14:
            raise ArithmeticError("singular normal-equation matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [value / divisor for value in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                augmented[row][j] - factor * augmented[column][j]
                for j in range(n + 1)
            ]
    return [augmented[i][-1] for i in range(n)]


def ordinary_least_squares(rows: list[list[float]], target: list[float]) -> dict[str, Any]:
    width = len(rows[0])
    xtx = [[0.0 for _ in range(width)] for _ in range(width)]
    xty = [0.0 for _ in range(width)]
    for row, value in zip(rows, target):
        for i in range(width):
            xty[i] += row[i] * value
            for j in range(width):
                xtx[i][j] += row[i] * row[j]
    coefficients = solve_linear_system(xtx, xty)
    fitted = [sum(c * x for c, x in zip(coefficients, row)) for row in rows]
    residuals = [value - prediction for value, prediction in zip(target, fitted)]
    target_mean = mean(target)
    ss_total = sum((value - target_mean) ** 2 for value in target)
    ss_residual = sum(value * value for value in residuals)
    return {
        "coefficients": coefficients,
        "r_squared": None if ss_total == 0 else 1 - ss_residual / ss_total,
        "residual_min": min(residuals),
        "residual_max": max(residuals),
        "residual_mean": mean(residuals),
        "residual_root_mean_square": math.sqrt(ss_residual / len(residuals)),
    }


def summarize_values(values: list[float]) -> dict[str, float]:
    ordered = sorted(values)
    n = len(ordered)
    return {
        "count": n,
        "min": ordered[0],
        "median": ordered[n // 2] if n % 2 else (ordered[n // 2 - 1] + ordered[n // 2]) / 2,
        "mean": mean(ordered),
        "max": ordered[-1],
    }


def height_pilot(points: list[dict[str, Any]], timeout: int) -> dict[str, Any]:
    heights = canonical_heights(points, timeout)
    records: list[dict[str, Any]] = []
    for item in points:
        source_index = int(item["source_index"])
        lam = Fraction(str(item["lambda"]))
        d = int(item["source_tuple"]["d"])
        x = parse_fraction(item["weierstrass_point"]["x"])
        canonical = heights[source_index]
        log_d = math.log(d)
        lambda_height = math.log(max(abs(lam.numerator), lam.denominator))
        x_height = math.log(max(abs(x.numerator), x.denominator))
        records.append(
            {
                "source_index": source_index,
                "category": item["source_tuple"]["category"],
                "lambda": str(item["lambda"]),
                "d": d,
                "canonical_height": canonical,
                "log_d": log_d,
                "lambda_log_height": lambda_height,
                "x_log_height": x_height,
                "canonical_over_log_d": canonical / log_d,
                "canonical_minus_log_d": canonical - log_d,
                "canonical_minus_half_x_height": canonical - 0.5 * x_height,
            }
        )
    canonical_values = [item["canonical_height"] for item in records]
    log_d_values = [item["log_d"] for item in records]
    lambda_values = [item["lambda_log_height"] for item in records]
    x_values = [item["x_log_height"] for item in records]
    regression = ordinary_least_squares(
        [[1.0, item["log_d"], item["lambda_log_height"]] for item in records],
        canonical_values,
    )
    category_records: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        category_records[str(record["category"])].append(record)
    return {
        "point_count": len(records),
        "canonical_height_summary": summarize_values(canonical_values),
        "canonical_over_log_d_summary": summarize_values(
            [item["canonical_over_log_d"] for item in records]
        ),
        "canonical_minus_log_d_summary": summarize_values(
            [item["canonical_minus_log_d"] for item in records]
        ),
        "canonical_minus_half_x_height_summary": summarize_values(
            [item["canonical_minus_half_x_height"] for item in records]
        ),
        "correlations": {
            "canonical_height_vs_log_d": pearson(canonical_values, log_d_values),
            "canonical_height_vs_lambda_log_height": pearson(canonical_values, lambda_values),
            "canonical_height_vs_x_log_height": pearson(canonical_values, x_values),
            "log_d_vs_lambda_log_height": pearson(log_d_values, lambda_values),
        },
        "ols_model": {
            "formula": "canonical_height = beta0 + beta_d*log(d) + beta_lambda*h(lambda)",
            "beta0": regression["coefficients"][0],
            "beta_d": regression["coefficients"][1],
            "beta_lambda": regression["coefficients"][2],
            "r_squared": regression["r_squared"],
            "residual_min": regression["residual_min"],
            "residual_max": regression["residual_max"],
            "residual_mean": regression["residual_mean"],
            "residual_root_mean_square": regression["residual_root_mean_square"],
        },
        "category_summaries": {
            category: {
                "point_count": len(items),
                "canonical_height": summarize_values(
                    [item["canonical_height"] for item in items]
                ),
                "canonical_over_log_d": summarize_values(
                    [item["canonical_over_log_d"] for item in items]
                ),
            }
            for category, items in sorted(category_records.items())
        },
        "points": records,
        "scope": {
            "established": (
                "the listed PARI canonical heights and finite-sample statistics "
                "for the 255 stored points"
            ),
            "not_established": [
                "a uniform inequality valid for all rational lambda and points",
                "bounded regression residuals outside the stored sample",
                "a canonical-height point-counting bound",
                "N_2=o(N_1)",
            ],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--relations", type=Path, default=DEFAULT_RELATIONS)
    parser.add_argument("--rank-efforts", default="4,8")
    parser.add_argument("--rank-timeout-per-attempt", type=int, default=900)
    parser.add_argument("--generator-saturation-bound", type=int, default=1000)
    parser.add_argument("--generator-timeout", type=int, default=600)
    parser.add_argument("--height-timeout", type=int, default=900)
    parser.add_argument("--write-report", type=Path, required=True)
    args = parser.parse_args()

    efforts = [int(item) for item in args.rank_efforts.split(",") if item.strip()]
    if not efforts or any(item < 0 for item in efforts):
        parser.error("rank efforts must be a comma-separated list of nonnegative integers")
    if args.generator_saturation_bound < 2:
        parser.error("generator saturation bound must be at least 2")

    payload, by_index, by_lambda = load_payload(args.relations)
    points = payload.get("points", [])
    rank_audit = retry_unresolved_ranks(
        by_lambda,
        efforts,
        args.rank_timeout_per_attempt,
    )
    generator_audit = audit_generator_7_32(
        by_index,
        args.generator_saturation_bound,
        args.generator_timeout,
    )
    heights = height_pilot(points, args.height_timeout)
    report = {
        "valid": generator_audit["valid"] and heights["point_count"] == 255,
        "source": args.relations.as_posix(),
        "unresolved_rank_retry": rank_audit,
        "lambda_7_32_generator": generator_audit,
        "height_pilot": heights,
        "global_scope": {
            "new_certificates": [
                "any exact rank whose PARI lower and upper bounds agree",
                "the exact displayed group-law relation at lambda=7/32",
                "canonical heights for the stored 255 points",
            ],
            "not_proved": [
                "a uniform rank bound for unobserved fibers",
                "a uniform comparison between H=d and canonical height",
                "a global upper bound for two-face cuboids",
                "N_2=o(N_1)",
            ],
        },
    }
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    summary = {
        "valid": report["valid"],
        "unresolved_rank_retry": {
            key: value
            for key, value in rank_audit.items()
            if key != "fibers"
        },
        "lambda_7_32_generator": {
            key: value
            for key, value in generator_audit.items()
            if key not in {"raw_pari_output"}
        },
        "height_pilot": {
            key: value
            for key, value in heights.items()
            if key != "points"
        },
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
