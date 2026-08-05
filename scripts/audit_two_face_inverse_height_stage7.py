#!/usr/bin/env python3
"""Audit the inverse map and the reverse-height route for two-face cuboids.

Stage six proved a one-way estimate from the primitive projective height d to
canonical height.  This script studies the reverse direction.  On the positive
smooth open of van Luijk's elliptic fibration, with

    t = lambda,
    E_t: y^2 = x (x + 4 t^2) (x + (1+t^2)^2),

an inverse projective map is

    [A:B:C:X:Y:U] = [
        2xy(1-t^2),
        x(4t^2(1+t^2)^2-x^2),
        4txy,
        y^2-x^2(1-t^2)^2,
        2xy(1+t^2),
        y^2+x^2(1-t^2)^2,
    ].

The script verifies this identity symbolically and on all stored 255 points.
After homogenizing the six coordinates simultaneously to multidegree (6,3,2)
in (t,x,y), the largest coefficient L1 norm is 16.  Hence

    log d <= 6 h(t) + 3 h(x) + 2 h(y) + log 16.

The Weierstrass equation gives

    2 h(y) <= 3 h(x) + 6 h(t) + 6 log 2,

and therefore the elementary reverse naive-height estimate

    log d <= 6 h(x) + 12 h(t) + 10 log 2.

For the integral model from stage six the script also verifies polynomial
bounds for c4, Delta and j.  Silverman's 1990 height-difference theorem then
implies an effective mixed comparison

    log d <= 12 hhat(P) + C_lambda h(lambda) + C_0

for absolute effective constants.  This stage deliberately does not assign a
numerical value to C_lambda because that requires transcribing every
normalization-dependent term in Silverman's Theorem 1.1.  More importantly,
the positive h(lambda) term prevents this estimate alone from closing the
global point-counting argument.
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


def parse_fraction_record(record: dict[str, Any]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def fraction_record(value: Fraction) -> dict[str, int | str]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}",
    }


def multiplicative_height(value: Fraction) -> int:
    return max(abs(value.numerator), value.denominator)


def logarithmic_height(value: Fraction) -> float:
    return math.log(multiplicative_height(value))


def numeric_summary(values: list[float]) -> dict[str, float | int]:
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


def index_by_source(points: list[dict[str, Any]], label: str) -> dict[int, dict[str, Any]]:
    indexed: dict[int, dict[str, Any]] = {}
    for point in points:
        source_index = int(point["source_index"])
        if source_index in indexed:
            raise ValueError(f"duplicate source_index={source_index} in {label}")
        indexed[source_index] = point
    return indexed


def normalize_projective(values: list[Fraction]) -> list[int]:
    if not values or all(value == 0 for value in values):
        raise ValueError("projective vector is zero")
    common_denominator = math.lcm(*(value.denominator for value in values))
    integers = [
        value.numerator * (common_denominator // value.denominator)
        for value in values
    ]
    common_gcd = reduce(math.gcd, (abs(value) for value in integers if value != 0))
    integers = [value // common_gcd for value in integers]
    if integers[-1] < 0:
        integers = [-value for value in integers]
    return integers


def inverse_coordinates(t: Fraction, x: Fraction, y: Fraction) -> dict[str, Fraction]:
    one_minus_t2 = 1 - t * t
    one_plus_t2 = 1 + t * t
    return {
        "A": 2 * x * y * one_minus_t2,
        "B": x * (4 * t * t * one_plus_t2 * one_plus_t2 - x * x),
        "C": 4 * t * x * y,
        "X": y * y - x * x * one_minus_t2 * one_minus_t2,
        "Y": 2 * x * y * one_plus_t2,
        "U": y * y + x * x * one_minus_t2 * one_minus_t2,
    }


def reduce_mod_curve(expression: sp.Expr, curve: sp.Expr, y_symbol: sp.Symbol) -> sp.Expr:
    numerator = sp.together(expression).as_numer_denom()[0]
    remainder = sp.rem(sp.Poly(sp.expand(numerator), y_symbol), sp.Poly(curve, y_symbol))
    return sp.factor(remainder.as_expr())


def verify_symbolic_inverse() -> dict[str, Any]:
    t, x, y = sp.symbols("t x y")
    curve = y**2 - x * (x + 4 * t**2) * (x + (1 + t**2) ** 2)
    coordinates = {
        "A": 2 * x * y * (1 - t**2),
        "B": x * (4 * t**2 * (1 + t**2) ** 2 - x**2),
        "C": 4 * t * x * y,
        "X": y**2 - x**2 * (1 - t**2) ** 2,
        "Y": 2 * x * y * (1 + t**2),
        "U": y**2 + x**2 * (1 - t**2) ** 2,
    }
    A, B, C, X, Y, U = (coordinates[key] for key in "ABCXYU")
    checks = {
        "A2_plus_C2_equals_Y2": A**2 + C**2 - Y**2,
        "B2_plus_C2_equals_X2": B**2 + C**2 - X**2,
        "A2_plus_X2_equals_U2": A**2 + X**2 - U**2,
        "lambda_first": Y - A - t * C,
        "lambda_second": C - t * (Y + A),
        "forward_x": 4 * t**2 * C * (U - B) - x * C * (X + B),
        "forward_y": 8 * t**3 * (U + X) * (U - B) - y * C * (X + B),
    }
    reduced = {
        name: reduce_mod_curve(expression, curve, y)
        for name, expression in checks.items()
    }
    failures = {name: str(value) for name, value in reduced.items() if value != 0}
    if failures:
        raise ArithmeticError(f"symbolic inverse-map checks failed: {failures}")

    degree_bounds = {"t": 6, "x": 3, "y": 2}
    coefficient_l1: dict[str, int] = {}
    observed_degrees: dict[str, dict[str, int]] = {}
    for name, expression in coordinates.items():
        polynomial = sp.Poly(sp.expand(expression), t, x, y)
        coefficient_l1[name] = sum(abs(int(value)) for value in polynomial.coeffs())
        observed_degrees[name] = {
            "t": int(polynomial.degree(t)),
            "x": int(polynomial.degree(x)),
            "y": int(polynomial.degree(y)),
        }
        if observed_degrees[name]["t"] > degree_bounds["t"]:
            raise ArithmeticError(f"{name}: t degree exceeds stage-seven bound")
        if observed_degrees[name]["x"] > degree_bounds["x"]:
            raise ArithmeticError(f"{name}: x degree exceeds stage-seven bound")
        if observed_degrees[name]["y"] > degree_bounds["y"]:
            raise ArithmeticError(f"{name}: y degree exceeds stage-seven bound")
    max_l1 = max(coefficient_l1.values())
    if max_l1 != 16:
        raise ArithmeticError(f"expected inverse-map coefficient L1 maximum 16, got {max_l1}")
    return {
        "curve": "y^2=x(x+4*t^2)(x+(1+t^2)^2)",
        "inverse_projective_coordinates": {
            name: str(sp.factor(expression)) for name, expression in coordinates.items()
        },
        "all_symbolic_checks_pass": True,
        "multidegree_bound": degree_bounds,
        "coordinate_coefficient_l1_norms": coefficient_l1,
        "maximum_coefficient_l1_norm": max_l1,
        "observed_coordinate_degrees": observed_degrees,
    }


def derive_point(
    source_index: int,
    kummer: dict[str, Any],
    relation: dict[str, Any],
    stage5: dict[str, Any],
) -> dict[str, Any]:
    standard = {key: int(value) for key, value in kummer["standard_coordinates"].items()}
    expected_vector = [standard[key] for key in "ABCXYU"]
    A, B, C, X, Y, U = expected_vector
    if not all(value > 0 for value in expected_vector):
        raise ValueError(f"source_index={source_index}: standard point is not positive")
    if math.gcd(*expected_vector) != 1:
        raise ArithmeticError(f"source_index={source_index}: standard point is not primitive")
    if max(expected_vector) != U:
        raise ArithmeticError(f"source_index={source_index}: U is not the projective max-height")

    parameter = kummer["elliptic_fibration_parameter"]["affine"]
    t = parse_fraction_record(parameter)
    point = relation["weierstrass_point"]
    x = parse_fraction_record(point["x"])
    y = parse_fraction_record(point["y"])
    if not (0 < t < 1 and x > 0 and y > 0):
        raise ValueError(f"source_index={source_index}: point is outside the positive affine open")

    inverse = inverse_coordinates(t, x, y)
    normalized = normalize_projective([inverse[key] for key in "ABCXYU"])
    if normalized != expected_vector:
        raise ArithmeticError(
            f"source_index={source_index}: inverse map mismatch; "
            f"expected={expected_vector}, actual={normalized}"
        )

    if A * A + C * C != Y * Y:
        raise ArithmeticError(f"source_index={source_index}: first face equation failed")
    if B * B + C * C != X * X:
        raise ArithmeticError(f"source_index={source_index}: second face equation failed")
    if A * A + X * X != U * U:
        raise ArithmeticError(f"source_index={source_index}: space equation failed")
    if t != Fraction(Y - A, C) or t != Fraction(C, Y + A):
        raise ArithmeticError(f"source_index={source_index}: lambda inverse identity failed")
    if x != Fraction(4 * t * t * (U - B), X + B):
        raise ArithmeticError(f"source_index={source_index}: forward x identity failed")
    if y != Fraction(8 * t**3 * (U + X) * (U - B), C * (X + B)):
        raise ArithmeticError(f"source_index={source_index}: forward y identity failed")

    h_t = logarithmic_height(t)
    h_x = logarithmic_height(x)
    h_y = logarithmic_height(y)
    log_d = math.log(U)
    raw_inverse_upper = 6 * h_t + 3 * h_x + 2 * h_y + math.log(16)
    y_equation_upper = 3 * h_x + 6 * h_t + 6 * math.log(2)
    combined_inverse_upper = 6 * h_x + 12 * h_t + 10 * math.log(2)
    tolerance = 1e-10
    if 2 * h_y > y_equation_upper + tolerance:
        raise ArithmeticError(f"source_index={source_index}: y-height inequality failed")
    if log_d > raw_inverse_upper + tolerance:
        raise ArithmeticError(f"source_index={source_index}: raw inverse-height bound failed")
    if log_d > combined_inverse_upper + tolerance:
        raise ArithmeticError(f"source_index={source_index}: combined inverse-height bound failed")

    m, n = t.numerator, t.denominator
    s = m * m + n * n
    root_a = 4 * m * m * n * n
    root_b = s * s
    a2 = root_a + root_b
    a4 = root_a * root_b
    c4 = 16 * (a2 * a2 - 3 * a4)
    discriminant = 16 * a4 * a4 * (a2 * a2 - 4 * a4)
    discriminant_formula = (
        256 * m**4 * n**4 * s**4 * (n * n - m * m) ** 4
    )
    if discriminant != discriminant_formula or discriminant <= 0:
        raise ArithmeticError(f"source_index={source_index}: discriminant formula failed")
    j = Fraction(c4**3, discriminant)
    c4_bound = 512 * n**8
    discriminant_bound = 4096 * n**24
    j_height_bound = 2**27 * n**24
    if c4 > c4_bound:
        raise ArithmeticError(f"source_index={source_index}: c4 bound failed")
    if discriminant > discriminant_bound:
        raise ArithmeticError(f"source_index={source_index}: discriminant bound failed")
    if multiplicative_height(j) > j_height_bound:
        raise ArithmeticError(f"source_index={source_index}: j-height bound failed")

    canonical_height = float(stage5["canonical_height"])
    return {
        "source_index": source_index,
        "source_tuple": kummer["source_tuple"],
        "standard_coordinates": standard,
        "lambda": str(t),
        "weierstrass_point": {"x": fraction_record(x), "y": fraction_record(y)},
        "inverse_projective_coordinates": {
            key: fraction_record(value) for key, value in inverse.items()
        },
        "normalized_inverse_vector": normalized,
        "projective_height_equals_d": max(normalized) == U,
        "heights": {
            "log_d": log_d,
            "h_lambda": h_t,
            "h_x": h_x,
            "h_y": h_y,
            "canonical_height": canonical_height,
            "raw_inverse_upper": raw_inverse_upper,
            "combined_inverse_upper": combined_inverse_upper,
            "raw_inverse_slack": raw_inverse_upper - log_d,
            "combined_inverse_slack": combined_inverse_upper - log_d,
            "log_d_minus_12_canonical": log_d - 12 * canonical_height,
            "lambda_share_hlambda_over_logd": h_t / log_d,
        },
        "integral_model_invariants": {
            "A2": a2,
            "A4": a4,
            "c4": c4,
            "discriminant": discriminant,
            "j": fraction_record(j),
            "c4_bound_512_n8": c4_bound,
            "discriminant_bound_4096_n24": discriminant_bound,
            "j_height_bound_2pow27_n24": j_height_bound,
        },
    }


def build_report(
    kummer_path: Path,
    relations_path: Path,
    stage5_path: Path,
) -> dict[str, Any]:
    kummer_payload = json.loads(kummer_path.read_text(encoding="utf-8"))
    relations_payload = json.loads(relations_path.read_text(encoding="utf-8"))
    stage5_payload = json.loads(stage5_path.read_text(encoding="utf-8"))
    kummer_by_index = index_by_source(kummer_payload["points"], "kummer points")
    relations_by_index = index_by_source(relations_payload["points"], "relation points")
    stage5_by_index = index_by_source(
        stage5_payload["height_pilot"]["points"], "stage-five points"
    )
    if not (
        set(kummer_by_index) == set(relations_by_index) == set(stage5_by_index)
    ):
        raise ValueError("source_index sets differ among stage-seven inputs")

    symbolic = verify_symbolic_inverse()
    points = [
        derive_point(
            source_index,
            kummer_by_index[source_index],
            relations_by_index[source_index],
            stage5_by_index[source_index],
        )
        for source_index in sorted(kummer_by_index)
    ]
    raw_slacks = [point["heights"]["raw_inverse_slack"] for point in points]
    combined_slacks = [point["heights"]["combined_inverse_slack"] for point in points]
    pure_residuals = [point["heights"]["log_d_minus_12_canonical"] for point in points]
    lambda_shares = [point["heights"]["lambda_share_hlambda_over_logd"] for point in points]

    return {
        "valid": True,
        "sources": {
            "kummer_classification": kummer_path.as_posix(),
            "mordell_weil_relations": relations_path.as_posix(),
            "stage5_canonical_heights": stage5_path.as_posix(),
        },
        "symbolic_inverse_audit": symbolic,
        "proved_in_stage7": {
            "inverse_map": (
                "the displayed six homogeneous rational functions invert the "
                "van Luijk Weierstrass map on the positive smooth affine open"
            ),
            "raw_projective_height_bound": (
                "log(d)<=6h(lambda)+3h(x)+2h(y)+log(16)"
            ),
            "weierstrass_y_height_bound": (
                "2h(y)<=3h(x)+6h(lambda)+6log(2)"
            ),
            "combined_reverse_naive_height_bound": (
                "log(d)<=6h(x)+12h(lambda)+10log(2)"
            ),
            "integral_invariant_bounds": [
                "c4<=512*n^8",
                "Delta<=4096*n^24",
                "h(j)<=24h(lambda)+27log(2)",
            ],
        },
        "literature_bridge": {
            "reference": (
                "J. H. Silverman, The difference between the Weil height and "
                "the canonical height on elliptic curves, Math. Comp. 55 "
                "(1990), 723-743, Theorem 1.1, DOI "
                "10.1090/S0025-5718-1990-1035944-5"
            ),
            "theorem_scope": (
                "an explicit bound for hhat(P)-(1/2)h(x(P)) in terms of the "
                "discriminant, j-invariant and integral Weierstrass equation"
            ),
            "stage7_consequence": (
                "there are effective absolute constants C_lambda and C0 such "
                "that log(d)<=12*hhat(P)+C_lambda*h(lambda)+C0"
            ),
            "numerical_C_lambda_fixed_in_stage7": False,
            "reason_not_fixed": (
                "the complete normalization-dependent p(E) expression from "
                "Silverman Theorem 1.1 has not been transcribed into code"
            ),
        },
        "decision": {
            "reverse_height_route_feasible": True,
            "pure_canonical_lower_bound_obtained": False,
            "why_counting_does_not_close": (
                "the effective reverse comparison necessarily retained by this "
                "argument contains h(lambda); the available bound "
                "h(lambda)<=0.5*log(2d) cannot be substituted usefully unless "
                "the final lambda coefficient is made smaller than 2"
            ),
            "next_research_choice": (
                "either sharpen the lambda coefficient drastically, or stop "
                "treating fibers independently and estimate the parameter/fiber "
                "sum by average rank, regulator, local-density, or determinant methods"
            ),
            "wall_discussion_recommended_after_stage7": True,
        },
        "finite_audit": {
            "point_count": len(points),
            "all_inverse_vectors_match": all(
                point["normalized_inverse_vector"]
                == [point["standard_coordinates"][key] for key in "ABCXYU"]
                for point in points
            ),
            "all_projective_heights_equal_d": all(
                point["projective_height_equals_d"] for point in points
            ),
            "raw_inverse_slack_summary": numeric_summary(raw_slacks),
            "combined_inverse_slack_summary": numeric_summary(combined_slacks),
            "log_d_minus_12_canonical_summary": numeric_summary(pure_residuals),
            "h_lambda_over_log_d_summary": numeric_summary(lambda_shares),
        },
        "not_proved": [
            "a numerical optimal value of C_lambda in the mixed reverse comparison",
            "log(d)<=C*hhat(P)+O(1) independently of lambda",
            "a uniform rank bound for all rational lambda",
            "a uniform or average regulator lower bound",
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
    print(json.dumps({key: report[key] for key in ("valid", "proved_in_stage7", "decision", "finite_audit")}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
