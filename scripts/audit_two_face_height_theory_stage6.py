#!/usr/bin/env python3
"""Derive and audit uniform height bounds for the face-cuboid elliptic fibers.

For a positive standard face-cuboid point

    A^2 + C^2 = Y^2,
    B^2 + C^2 = X^2,
    A^2 + X^2 = U^2,

write d=U and lambda=(Y-A)/C=m/n in lowest terms.  The script verifies the
algebraic bounds used in stage six of the research memo:

    m^2+n^2 | 2Y,               m^2+n^2 <= 2d,
    h(lambda) <= (1/2) log(2d), h(x) <= 2 log d + log 8.

After the change xi=n^4 x, eta=n^6 y, the fiber has the integral model

    eta^2 = xi (xi + 4m^2n^2) (xi + (m^2+n^2)^2)
          = xi^3 + A2 xi^2 + A4 xi.

The duplication map gives a one-sided canonical-height estimate

    hhat(P) <= (17/6) log d + log 2 + (1/3) log 17.

The proof is elementary once the standard definition

    hhat(P) = (1/2) lim 4^{-k} h(x(2^k P))

is fixed.  The script also checks all stored 255 points and compares the
proven upper bounds with their PARI/GP canonical heights.  It does not prove a
uniform rank bound, a uniform regulator lower bound, a global point-counting
bound, or N_2=o(N_1).
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp


DEFAULT_KUMMER = Path("data/two_face_cuboids_1e6_kummer_classification.json")
DEFAULT_RELATIONS = Path("data/two_face_cuboids_1e6_mordell_weil_relations.json")
DEFAULT_STAGE5 = Path("data/two_face_cuboids_1e6_stage5_report.json")
DEFAULT_OUTPUT = Path("data/two_face_cuboids_1e6_stage6_height_report.json")


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


def rational_multiplicative_height(value: Fraction) -> int:
    return max(abs(value.numerator), value.denominator)


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


def verify_duplication_identity() -> str:
    x, a2, a4 = sp.symbols("x a2 a4")
    numerator_from_tangent = sp.expand(
        (3 * x**2 + 2 * a2 * x + a4) ** 2
        - 4 * (a2 + 2 * x) * x * (x**2 + a2 * x + a4)
    )
    expected = sp.expand((x**2 - a4) ** 2)
    if sp.expand(numerator_from_tangent - expected) != 0:
        raise ArithmeticError("duplication identity failed")
    return "x(2P)=(x(P)^2-A4)^2/[4*x(P)*(x(P)^2+A2*x(P)+A4)]"


def index_by_source(points: list[dict[str, Any]], label: str) -> dict[int, dict[str, Any]]:
    indexed: dict[int, dict[str, Any]] = {}
    for point in points:
        source_index = int(point["source_index"])
        if source_index in indexed:
            raise ValueError(f"duplicate source_index={source_index} in {label}")
        indexed[source_index] = point
    return indexed


def derive_point(
    source_index: int,
    kummer: dict[str, Any],
    relation: dict[str, Any],
    stage5: dict[str, Any],
) -> dict[str, Any]:
    standard = {key: int(value) for key, value in kummer["standard_coordinates"].items()}
    A, B, C, X, Y, U = (standard[key] for key in "ABCXYU")
    d = U
    if d <= 1:
        raise ValueError(f"source_index={source_index}: d must exceed 1")
    if not all(value > 0 for value in standard.values()):
        raise ValueError(f"source_index={source_index}: standard coordinates are not positive")

    parameter = kummer["elliptic_fibration_parameter"]["affine"]
    lam = parse_fraction_record(parameter)
    m, n = lam.numerator, lam.denominator
    if not (0 < m < n and math.gcd(m, n) == 1):
        raise ValueError(f"source_index={source_index}: lambda is not reduced in (0,1)")
    if lam != Fraction(Y - A, C) or lam != Fraction(C, Y + A):
        raise ArithmeticError(f"source_index={source_index}: lambda coordinate identity failed")

    parameter_norm = m * m + n * n
    divides_two_y = (2 * Y) % parameter_norm == 0
    if not divides_two_y:
        raise ArithmeticError(f"source_index={source_index}: m^2+n^2 does not divide 2Y")
    parameter_scale = (2 * Y) // parameter_norm
    parameter_bound = parameter_norm <= 2 * d
    if not parameter_bound:
        raise ArithmeticError(f"source_index={source_index}: m^2+n^2 > 2d")

    relation_point = relation["weierstrass_point"]
    x_relation = parse_fraction_record(relation_point["x"])
    y_relation = parse_fraction_record(relation_point["y"])
    x_direct = Fraction(4 * m * m * (U - B), n * n * (X + B))
    y_direct = Fraction(
        8 * m**3 * (U + X) * (U - B),
        n**3 * C * (X + B),
    )
    if x_direct != x_relation or y_direct != y_relation:
        raise ArithmeticError(f"source_index={source_index}: Weierstrass map mismatch")

    x_height = rational_multiplicative_height(x_direct)
    x_height_bound = 8 * d * d
    if x_height > x_height_bound:
        raise ArithmeticError(f"source_index={source_index}: H(x) bound failed")

    xi = n**4 * x_direct
    eta = n**6 * y_direct
    xi_height = rational_multiplicative_height(xi)
    xi_height_bound = 4 * d**3
    if xi_height > xi_height_bound:
        raise ArithmeticError(f"source_index={source_index}: H(xi) bound failed")

    s = parameter_norm
    a2 = s * s + 4 * m * m * n * n
    a4 = 4 * m * m * n * n * s * s
    if eta * eta != xi * (xi + 4 * m * m * n * n) * (xi + s * s):
        raise ArithmeticError(f"source_index={source_index}: integral model equation failed")
    if a2 > 8 * d**2:
        raise ArithmeticError(f"source_index={source_index}: A2 bound failed")
    if a4 > 16 * d**4:
        raise ArithmeticError(f"source_index={source_index}: A4 bound failed")

    duplication_constant = max((1 + a4) ** 2, 4 * (1 + a2 + a4))
    duplication_constant_bound = 289 * d**8
    if duplication_constant > duplication_constant_bound:
        raise ArithmeticError(
            f"source_index={source_index}: duplication constant bound failed"
        )

    point_specific_upper = 0.5 * math.log(xi_height) + math.log(duplication_constant) / 6
    coarse_upper = (
        Fraction(17, 6) * math.log(d)
        + math.log(2)
        + math.log(17) / 3
    )
    actual_canonical = float(stage5["canonical_height"])
    tolerance = 1e-10
    if actual_canonical > point_specific_upper + tolerance:
        raise ArithmeticError(
            f"source_index={source_index}: canonical height exceeds point-specific bound"
        )
    if actual_canonical > coarse_upper + tolerance:
        raise ArithmeticError(
            f"source_index={source_index}: canonical height exceeds coarse bound"
        )

    return {
        "source_index": source_index,
        "source_tuple": kummer["source_tuple"],
        "standard_coordinates": standard,
        "lambda": str(lam),
        "lambda_numerator_m": m,
        "lambda_denominator_n": n,
        "m2_plus_n2": parameter_norm,
        "m2_plus_n2_divides_2Y": divides_two_y,
        "twoY_over_m2_plus_n2": parameter_scale,
        "m2_plus_n2_le_2d": parameter_bound,
        "lambda_log_height": math.log(n),
        "lambda_log_height_upper": 0.5 * math.log(2 * d),
        "weierstrass_point": {
            "x": fraction_record(x_direct),
            "y": fraction_record(y_direct),
        },
        "affine_x_multiplicative_height": x_height,
        "affine_x_height_bound_8d2": x_height_bound,
        "integral_model_point": {
            "xi": fraction_record(xi),
            "eta": fraction_record(eta),
        },
        "integral_model_coefficients": {"A2": a2, "A4": a4},
        "integral_xi_multiplicative_height": xi_height,
        "integral_xi_height_bound_4d3": xi_height_bound,
        "duplication_constant": duplication_constant,
        "duplication_constant_bound_289d8": duplication_constant_bound,
        "actual_canonical_height": actual_canonical,
        "point_specific_canonical_upper": point_specific_upper,
        "coarse_canonical_upper": float(coarse_upper),
        "point_specific_slack": point_specific_upper - actual_canonical,
        "coarse_slack": float(coarse_upper) - actual_canonical,
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
    index_sets = [set(kummer_by_index), set(relations_by_index), set(stage5_by_index)]
    if not (index_sets[0] == index_sets[1] == index_sets[2]):
        raise ValueError("source_index sets differ among input files")

    duplication_identity = verify_duplication_identity()
    derived_points = [
        derive_point(
            source_index,
            kummer_by_index[source_index],
            relations_by_index[source_index],
            stage5_by_index[source_index],
        )
        for source_index in sorted(kummer_by_index)
    ]

    point_specific_slacks = [point["point_specific_slack"] for point in derived_points]
    coarse_slacks = [point["coarse_slack"] for point in derived_points]
    lambda_ratios = [
        point["lambda_log_height"] / math.log(point["source_tuple"]["d"])
        for point in derived_points
    ]
    x_bound_ratios = [
        point["affine_x_multiplicative_height"]
        / point["affine_x_height_bound_8d2"]
        for point in derived_points
    ]
    xi_bound_ratios = [
        point["integral_xi_multiplicative_height"]
        / point["integral_xi_height_bound_4d3"]
        for point in derived_points
    ]

    return {
        "valid": True,
        "sources": {
            "kummer_classification": kummer_path.as_posix(),
            "mordell_weil_relations": relations_path.as_posix(),
            "stage5_canonical_heights": stage5_path.as_posix(),
        },
        "theorem": {
            "scope": (
                "positive integer points on the smooth standard face-cuboid fiber, "
                "with d=U and lambda=m/n reduced in (0,1)"
            ),
            "parameter_divisibility": "m^2+n^2 divides 2Y",
            "parameter_bound": "m^2+n^2 <= 2d",
            "lambda_height_bound": "h(lambda)=log(n) <= (1/2)log(2d)",
            "affine_x_height_bound": "h(x) <= 2log(d)+log(8)",
            "integral_model": (
                "eta^2=xi(xi+4m^2n^2)(xi+(m^2+n^2)^2), "
                "xi=n^4x, eta=n^6y"
            ),
            "integral_x_height_bound": "h(xi) <= 3log(d)+log(4)",
            "coefficient_bounds": "A2<=8d^2 and A4<=16d^4",
            "duplication_identity": duplication_identity,
            "duplication_height_recurrence": (
                "h(xi(2P)) <= 4h(xi(P))+log(C), "
                "C=max((1+A4)^2,4(1+A2+A4))<=289d^8"
            ),
            "canonical_height_normalization": (
                "hhat(P)=(1/2)lim_{k->infinity}4^{-k}h(xi(2^kP))"
            ),
            "canonical_height_upper_bound": (
                "hhat(P) <= (17/6)log(d)+log(2)+(1/3)log(17)"
            ),
            "parameter_count_consequence": (
                "for d<=B, at most 2B reduced pairs (m,n) can occur from "
                "m,n>0 and m^2+n^2<=2B; this is only an O(B) fiber bound"
            ),
        },
        "finite_audit": {
            "point_count": len(derived_points),
            "all_parameter_divisibility_checks_pass": all(
                point["m2_plus_n2_divides_2Y"] for point in derived_points
            ),
            "all_parameter_bounds_pass": all(
                point["m2_plus_n2_le_2d"] for point in derived_points
            ),
            "all_actual_canonical_heights_below_point_specific_bound": all(
                point["point_specific_slack"] >= -1e-10 for point in derived_points
            ),
            "all_actual_canonical_heights_below_coarse_bound": all(
                point["coarse_slack"] >= -1e-10 for point in derived_points
            ),
            "point_specific_slack_summary": numeric_summary(point_specific_slacks),
            "coarse_slack_summary": numeric_summary(coarse_slacks),
            "h_lambda_over_log_d_summary": numeric_summary(lambda_ratios),
            "H_x_over_8d2_summary": numeric_summary(x_bound_ratios),
            "H_xi_over_4d3_summary": numeric_summary(xi_bound_ratios),
        },
        "counting_consequence": {
            "fixed_fiber": (
                "if the free Mordell-Weil lattice has rank r and smallest "
                "height-pairing eigenvalue mu_lambda>0, then points with d<=B "
                "lie in a Euclidean coefficient ball of squared radius at most "
                "T(B)/mu_lambda, where T(B)=(17/6)log(B)+log(2)+(1/3)log(17)"
            ),
            "still_missing": [
                "a uniform rank bound over all rational lambda",
                "a uniform lower bound for the smallest height-pairing eigenvalue or regulator",
                "control of special fibers and possible torsion enlargement",
                "an average bound strong enough to sum over O(B) possible parameters",
                "a proved lower asymptotic for N_1(B) suitable for comparison",
                "a global upper bound for N_2(B)",
                "N_2(B)=o(N_1(B))",
            ],
        },
        "points": derived_points,
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
            {
                "valid": report["valid"],
                "theorem": report["theorem"],
                "finite_audit": report["finite_audit"],
                "counting_consequence": report["counting_consequence"],
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
