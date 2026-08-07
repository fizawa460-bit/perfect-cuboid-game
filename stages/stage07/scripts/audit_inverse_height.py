#!/usr/bin/env python3
"""Audit the inverse map and reverse-height route for two-face cuboids.

On the positive smooth fiber

    E_t: y^2 = x(x+4t^2)(x+(1+t^2)^2),

the script verifies the projective inverse

    A = 2xy(1-t^2)
    B = x(4t^2(1+t^2)^2-x^2)
    C = 4txy
    X = y^2-x^2(1-t^2)^2
    Y = 2xy(1+t^2)
    U = y^2+x^2(1-t^2)^2.

The simultaneous multidegree is at most (6,3,2), and the largest coordinate
coefficient L1 norm is 17.  Therefore

    log d <= 6h(t)+3h(x)+2h(y)+log(17),

and the curve equation yields

    log d <= 6h(x)+12h(t)+6log(2)+log(17).

The script also bounds c4, Delta and j for the integral model and records the
Silverman height-difference bridge.  It does not claim a lambda-free reverse
bound or a global point-counting theorem.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
from fractions import Fraction
from functools import reduce
from pathlib import Path
from typing import Any

import sympy as sp


DEFAULT_KUMMER = Path("data/two_face_cuboids_1e6_kummer_classification.json")
DEFAULT_RELATIONS = Path("data/two_face_cuboids_1e6_mordell_weil_relations.json")
DEFAULT_STAGE5 = Path("data/two_face_cuboids_1e6_stage5_report.json")
DEFAULT_OUTPUT = Path("data/two_face_cuboids_1e6_stage7_inverse_height_report.json")
KEYS = "ABCXYU"


def parse_fraction(record: dict[str, Any]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def fraction_record(value: Fraction) -> dict[str, int | str]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}",
    }


def height(value: Fraction) -> int:
    return max(abs(value.numerator), value.denominator)


def log_height(value: Fraction) -> float:
    return math.log(height(value))


def summary(values: list[float]) -> dict[str, float | int]:
    if not values:
        return {"count": 0}
    ordered = sorted(values)
    return {
        "count": len(values),
        "min": ordered[0],
        "median": statistics.median(ordered),
        "mean": statistics.fmean(ordered),
        "max": ordered[-1],
    }


def indexed(points: list[dict[str, Any]], label: str) -> dict[int, dict[str, Any]]:
    result: dict[int, dict[str, Any]] = {}
    for point in points:
        index = int(point["source_index"])
        if index in result:
            raise ValueError(f"duplicate source_index={index} in {label}")
        result[index] = point
    return result


def normalize(values: list[Fraction]) -> list[int]:
    denominator = math.lcm(*(value.denominator for value in values))
    integers = [
        value.numerator * (denominator // value.denominator) for value in values
    ]
    divisor = reduce(math.gcd, (abs(value) for value in integers if value))
    integers = [value // divisor for value in integers]
    if integers[-1] < 0:
        integers = [-value for value in integers]
    return integers


def inverse_map(t: Fraction, x: Fraction, y: Fraction) -> dict[str, Fraction]:
    minus = 1 - t * t
    plus = 1 + t * t
    return {
        "A": 2 * x * y * minus,
        "B": x * (4 * t * t * plus * plus - x * x),
        "C": 4 * t * x * y,
        "X": y * y - x * x * minus * minus,
        "Y": 2 * x * y * plus,
        "U": y * y + x * x * minus * minus,
    }


def remainder_mod_curve(expression: sp.Expr, curve: sp.Expr, y: sp.Symbol) -> sp.Expr:
    numerator = sp.together(expression).as_numer_denom()[0]
    return sp.factor(
        sp.rem(sp.Poly(sp.expand(numerator), y), sp.Poly(curve, y)).as_expr()
    )


def symbolic_audit() -> dict[str, Any]:
    t, x, y = sp.symbols("t x y")
    curve = y**2 - x * (x + 4 * t**2) * (x + (1 + t**2) ** 2)
    values = {
        "A": 2 * x * y * (1 - t**2),
        "B": x * (4 * t**2 * (1 + t**2) ** 2 - x**2),
        "C": 4 * t * x * y,
        "X": y**2 - x**2 * (1 - t**2) ** 2,
        "Y": 2 * x * y * (1 + t**2),
        "U": y**2 + x**2 * (1 - t**2) ** 2,
    }
    A, B, C, X, Y, U = (values[key] for key in KEYS)
    checks = {
        "face_AC": A**2 + C**2 - Y**2,
        "face_BC": B**2 + C**2 - X**2,
        "space": A**2 + X**2 - U**2,
        "lambda_1": Y - A - t * C,
        "lambda_2": C - t * (Y + A),
        "forward_x": 4 * t**2 * C * (U - B) - x * C * (X + B),
        "forward_y": 8 * t**3 * (U + X) * (U - B) - y * C * (X + B),
    }
    failures = {
        name: str(remainder_mod_curve(expression, curve, y))
        for name, expression in checks.items()
        if remainder_mod_curve(expression, curve, y) != 0
    }
    if failures:
        raise ArithmeticError(f"symbolic inverse checks failed: {failures}")

    degree_limit = {"t": 6, "x": 3, "y": 2}
    coefficient_norms: dict[str, int] = {}
    degrees: dict[str, dict[str, int]] = {}
    for name, expression in values.items():
        polynomial = sp.Poly(sp.expand(expression), t, x, y)
        coefficient_norms[name] = sum(abs(int(c)) for c in polynomial.coeffs())
        degrees[name] = {
            "t": int(polynomial.degree(t)),
            "x": int(polynomial.degree(x)),
            "y": int(polynomial.degree(y)),
        }
        for symbol in ("t", "x", "y"):
            if degrees[name][symbol] > degree_limit[symbol]:
                raise ArithmeticError(f"{name}: {symbol} degree bound failed")
    max_norm = max(coefficient_norms.values())
    if max_norm != 17:
        raise ArithmeticError(f"expected maximum coefficient L1 norm 17, got {max_norm}")
    return {
        "all_symbolic_checks_pass": True,
        "curve": "y^2=x(x+4*t^2)(x+(1+t^2)^2)",
        "inverse_projective_coordinates": {
            key: str(sp.factor(value)) for key, value in values.items()
        },
        "multidegree_bound": degree_limit,
        "coordinate_coefficient_l1_norms": coefficient_norms,
        "maximum_coefficient_l1_norm": max_norm,
        "observed_coordinate_degrees": degrees,
    }


def derive_point(
    source_index: int,
    kummer: dict[str, Any],
    relation: dict[str, Any],
    stage5: dict[str, Any],
) -> dict[str, Any]:
    standard = {key: int(value) for key, value in kummer["standard_coordinates"].items()}
    expected = [standard[key] for key in KEYS]
    A, B, C, X, Y, U = expected
    if not all(value > 0 for value in expected):
        raise ValueError(f"source_index={source_index}: nonpositive standard coordinate")
    if math.gcd(*expected) != 1 or max(expected) != U:
        raise ArithmeticError(f"source_index={source_index}: primitive height normalization failed")

    t = parse_fraction(kummer["elliptic_fibration_parameter"]["affine"])
    x = parse_fraction(relation["weierstrass_point"]["x"])
    y = parse_fraction(relation["weierstrass_point"]["y"])
    if not (0 < t < 1 and x > 0 and y > 0):
        raise ValueError(f"source_index={source_index}: point outside positive affine open")

    inverse = inverse_map(t, x, y)
    normalized = normalize([inverse[key] for key in KEYS])
    if normalized != expected:
        raise ArithmeticError(
            f"source_index={source_index}: inverse mismatch {normalized} != {expected}"
        )
    if A * A + C * C != Y * Y or B * B + C * C != X * X:
        raise ArithmeticError(f"source_index={source_index}: face equation failed")
    if A * A + X * X != U * U:
        raise ArithmeticError(f"source_index={source_index}: space equation failed")
    if t != Fraction(Y - A, C) or t != Fraction(C, Y + A):
        raise ArithmeticError(f"source_index={source_index}: lambda identity failed")
    if x != Fraction(4 * t * t * (U - B), X + B):
        raise ArithmeticError(f"source_index={source_index}: forward x failed")
    if y != Fraction(8 * t**3 * (U + X) * (U - B), C * (X + B)):
        raise ArithmeticError(f"source_index={source_index}: forward y failed")

    ht, hx, hy, logd = log_height(t), log_height(x), log_height(y), math.log(U)
    raw_upper = 6 * ht + 3 * hx + 2 * hy + math.log(17)
    y_upper = 3 * hx + 6 * ht + 6 * math.log(2)
    combined_upper = 6 * hx + 12 * ht + 6 * math.log(2) + math.log(17)
    if 2 * hy > y_upper + 1e-10:
        raise ArithmeticError(f"source_index={source_index}: y-height bound failed")
    if logd > raw_upper + 1e-10 or logd > combined_upper + 1e-10:
        raise ArithmeticError(f"source_index={source_index}: inverse-height bound failed")

    m, n = t.numerator, t.denominator
    s = m * m + n * n
    root_a, root_b = 4 * m * m * n * n, s * s
    a2, a4 = root_a + root_b, root_a * root_b
    c4 = 16 * (a2 * a2 - 3 * a4)
    discriminant = 16 * a4 * a4 * (a2 * a2 - 4 * a4)
    expected_discriminant = 256 * m**4 * n**4 * s**4 * (n * n - m * m) ** 4
    if discriminant != expected_discriminant or discriminant <= 0:
        raise ArithmeticError(f"source_index={source_index}: discriminant identity failed")
    j = Fraction(c4**3, discriminant)
    c4_bound = 512 * n**8
    discriminant_bound = 4096 * n**24
    j_bound = 2**27 * n**24
    if c4 > c4_bound or discriminant > discriminant_bound or height(j) > j_bound:
        raise ArithmeticError(f"source_index={source_index}: invariant bound failed")

    canonical = float(stage5["canonical_height"])
    return {
        "source_index": source_index,
        "source_tuple": kummer["source_tuple"],
        "standard_coordinates": standard,
        "lambda": str(t),
        "weierstrass_point": {"x": fraction_record(x), "y": fraction_record(y)},
        "normalized_inverse_vector": normalized,
        "projective_height_equals_d": max(normalized) == U,
        "heights": {
            "log_d": logd,
            "h_lambda": ht,
            "h_x": hx,
            "h_y": hy,
            "canonical_height": canonical,
            "raw_inverse_upper": raw_upper,
            "combined_inverse_upper": combined_upper,
            "raw_inverse_slack": raw_upper - logd,
            "combined_inverse_slack": combined_upper - logd,
            "log_d_minus_12_canonical": logd - 12 * canonical,
            "lambda_share_hlambda_over_logd": ht / logd,
        },
        "integral_model_invariants": {
            "A2": a2,
            "A4": a4,
            "c4": c4,
            "discriminant": discriminant,
            "j": fraction_record(j),
            "c4_bound_512_n8": c4_bound,
            "discriminant_bound_4096_n24": discriminant_bound,
            "j_height_bound_2pow27_n24": j_bound,
        },
    }


def build_report(kummer_path: Path, relations_path: Path, stage5_path: Path) -> dict[str, Any]:
    kummer_data = json.loads(kummer_path.read_text(encoding="utf-8"))
    relation_data = json.loads(relations_path.read_text(encoding="utf-8"))
    stage5_data = json.loads(stage5_path.read_text(encoding="utf-8"))
    kummer = indexed(kummer_data["points"], "kummer")
    relations = indexed(relation_data["points"], "relations")
    stage5 = indexed(stage5_data["height_pilot"]["points"], "stage5")
    if not (set(kummer) == set(relations) == set(stage5)):
        raise ValueError("source index sets differ")

    symbolic = symbolic_audit()
    points = [
        derive_point(index, kummer[index], relations[index], stage5[index])
        for index in sorted(kummer)
    ]
    raw = [point["heights"]["raw_inverse_slack"] for point in points]
    combined = [point["heights"]["combined_inverse_slack"] for point in points]
    pure = [point["heights"]["log_d_minus_12_canonical"] for point in points]
    shares = [point["heights"]["lambda_share_hlambda_over_logd"] for point in points]

    return {
        "valid": True,
        "sources": {
            "kummer_classification": kummer_path.as_posix(),
            "mordell_weil_relations": relations_path.as_posix(),
            "stage5_canonical_heights": stage5_path.as_posix(),
        },
        "symbolic_inverse_audit": symbolic,
        "proved_in_stage7": {
            "inverse_map": "the displayed six coordinates invert the Weierstrass map on the positive smooth affine open",
            "raw_projective_height_bound": "log(d)<=6h(lambda)+3h(x)+2h(y)+log(17)",
            "weierstrass_y_height_bound": "2h(y)<=3h(x)+6h(lambda)+6log(2)",
            "combined_reverse_naive_height_bound": "log(d)<=6h(x)+12h(lambda)+6log(2)+log(17)",
            "integral_invariant_bounds": [
                "c4<=512*n^8",
                "Delta<=4096*n^24",
                "h(j)<=24h(lambda)+27log(2)",
            ],
        },
        "literature_bridge": {
            "reference": "J. H. Silverman, The difference between the Weil height and the canonical height on elliptic curves, Math. Comp. 55 (1990), 723-743, Theorem 1.1, DOI 10.1090/S0025-5718-1990-1035944-5",
            "theorem_scope": "explicit bounds for hhat(P)-(1/2)h(x(P)) in terms of an integral Weierstrass equation, its discriminant and j-invariant",
            "stage7_consequence": "effective absolute constants C_lambda,C0 exist with log(d)<=12*hhat(P)+C_lambda*h(lambda)+C0",
            "numerical_C_lambda_fixed_in_stage7": False,
            "reason_not_fixed": "the complete normalization-dependent p(E) expression in Silverman Theorem 1.1 was not transcribed into code",
        },
        "decision": {
            "reverse_height_route_feasible": True,
            "pure_canonical_lower_bound_obtained": False,
            "why_counting_does_not_close": "the mixed reverse estimate retains h(lambda); substituting h(lambda)<=0.5*log(2d) is useful only if the final lambda coefficient is below 2",
            "next_research_choice": "sharpen the lambda coefficient drastically, or switch to an average parameter/fiber sum using rank, regulator, local conditions or determinant methods",
            "wall_discussion_recommended_after_stage7": True,
        },
        "finite_audit": {
            "point_count": len(points),
            "all_inverse_vectors_match": all(
                point["normalized_inverse_vector"]
                == [point["standard_coordinates"][key] for key in KEYS]
                for point in points
            ),
            "all_projective_heights_equal_d": all(point["projective_height_equals_d"] for point in points),
            "raw_inverse_slack_summary": summary(raw),
            "combined_inverse_slack_summary": summary(combined),
            "log_d_minus_12_canonical_summary": summary(pure),
            "h_lambda_over_log_d_summary": summary(shares),
        },
        "not_proved": [
            "a numerical optimal C_lambda in the mixed reverse comparison",
            "a lambda-free bound log(d)<=C*hhat(P)+O(1)",
            "a uniform rank or regulator estimate for all rational lambda",
            "a global upper bound for two-face cuboids",
            "N_2(B)=o(N_1(B))",
        ],
        "points": points,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kummer", type=Path, default=DEFAULT_KUMMER)
    parser.add_argument("--relations", type=Path, default=DEFAULT_RELATIONS)
    parser.add_argument("--stage5", type=Path, default=DEFAULT_STAGE5)
    parser.add_argument("--write-report", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    report = build_report(args.kummer, args.relations, args.stage5)
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {key: report[key] for key in ("valid", "proved_in_stage7", "decision", "finite_audit")},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
