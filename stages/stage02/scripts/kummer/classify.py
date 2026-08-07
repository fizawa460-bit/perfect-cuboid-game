#!/usr/bin/env python3
"""Classify the 255 two-face cuboids on the standard face-cuboid Kummer model.

The script maps every integer point to van Luijk's standard coordinates

    A^2 + C^2 = Y^2,
    B^2 + C^2 = X^2,
    A^2 + X^2 = U^2,

checks membership in the 24 explicitly listed conics, and records the
elliptic-fibration parameter lambda = (Y-A)/C = C/(Y+A).

Only arithmetic and the explicitly stated equations are used.  The output does
not claim that points outside these 24 conics lie on no other rational curve.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


DEFAULT_DATA = Path("data/two_face_cuboids_1e6_fixed.json")
DEFAULT_DERIVED = Path("data/two_face_cuboids_1e6_kummer_classification.json")
DEFAULT_REPORT = Path("data/two_face_cuboids_1e6_kummer_report.json")


def fraction_record(value: Fraction) -> dict[str, int | str]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": (
            str(value.numerator)
            if value.denominator == 1
            else f"{value.numerator}/{value.denominator}"
        ),
    }


def map_to_standard(row: list[Any]) -> tuple[dict[str, int], str]:
    a, b, c, d, category, diag_ab, diag_ac, diag_bc = row

    if category == "ab+ac":
        if diag_ab is None or diag_ac is None:
            raise ValueError("ab+ac point is missing a required diagonal")
        values = (c, b, a, diag_ab, diag_ac, d)
        mapping = "(A,B,C,X,Y,U)=(c,b,a,diag_ab,diag_ac,d)"
    elif category == "ab+bc":
        if diag_ab is None or diag_bc is None:
            raise ValueError("ab+bc point is missing a required diagonal")
        values = (a, c, b, diag_bc, diag_ab, d)
        mapping = "(A,B,C,X,Y,U)=(a,c,b,diag_bc,diag_ab,d)"
    elif category in {"ac+bc", "perfect"}:
        if diag_ac is None or diag_bc is None:
            raise ValueError(f"{category} point is missing a required diagonal")
        values = (a, b, c, diag_bc, diag_ac, d)
        mapping = "(A,B,C,X,Y,U)=(a,b,c,diag_bc,diag_ac,d)"
    else:
        raise ValueError(f"unsupported category: {category!r}")

    return dict(zip(("A", "B", "C", "X", "Y", "U"), values)), mapping


def standard_equations_hold(coords: dict[str, int]) -> bool:
    A, B, C, X, Y, U = (coords[key] for key in "ABCXYU")
    return (
        A * A + C * C == Y * Y
        and B * B + C * C == X * X
        and A * A + X * X == U * U
    )


def gaussian_i_relation(left: int, right: int, sign: int) -> bool:
    """Return whether i*left = sign*right for rational integer inputs.

    Equality in Q(i) forces both rational and imaginary parts to vanish.
    """

    return left == 0 and sign * right == 0


def conic_memberships(coords: dict[str, int]) -> list[str]:
    """Test the 24 conics in van Luijk, section 4.2.

    IDs follow his notation DC++, DA+-, and so on.  Coordinates are rational,
    so membership in a conic defined over Q(i) is tested as equality in Q(i).
    """

    A, B, C, X, Y, U = (coords[key] for key in "ABCXYU")
    memberships: list[str] = []

    for sign_1, char_1 in ((1, "+"), (-1, "-")):
        for sign_2, char_2 in ((1, "+"), (-1, "-")):
            suffix = char_1 + char_2

            if C == 0 and Y == sign_1 * A and X == sign_2 * B and A * A + B * B == U * U:
                memberships.append(f"DC{suffix}")

            if A == 0 and Y == sign_1 * C and X == sign_2 * U and B * B + C * C == X * X:
                memberships.append(f"DA{suffix}")

            if B == 0 and X == sign_1 * C and Y == sign_2 * U and A * A + C * C == Y * Y:
                memberships.append(f"DB{suffix}")

            if (
                Y == 0
                and gaussian_i_relation(A, C, sign_1)
                and B == sign_2 * U
                and B * B + C * C == X * X
            ):
                memberships.append(f"DY{suffix}")

            if (
                X == 0
                and gaussian_i_relation(B, C, sign_1)
                and A == sign_2 * U
                and A * A + C * C == Y * Y
            ):
                memberships.append(f"DX{suffix}")

            if (
                U == 0
                and gaussian_i_relation(X, A, sign_1)
                and gaussian_i_relation(Y, B, sign_2)
                and B * B + C * C == X * X
            ):
                memberships.append(f"DU{suffix}")

    return memberships


def elliptic_parameter(coords: dict[str, int]) -> dict[str, Any]:
    A, C, Y = coords["A"], coords["C"], coords["Y"]

    projective_pair = [Y - A, C]
    if C == 0:
        return {
            "projective_pair": projective_pair,
            "affine": None,
            "identity_verified": (Y - A) * (Y + A) == C * C,
            "strictly_between_zero_and_one": False,
            "van_luijk_fiber_status": "infinity_or_base_point",
        }

    first = Fraction(Y - A, C)
    if Y + A == 0:
        second = None
        identity_verified = False
    else:
        second = Fraction(C, Y + A)
        identity_verified = first == second

    singular_rational_parameters = {Fraction(-1), Fraction(0), Fraction(1)}
    status = (
        "singular_parameter_0_or_pm1"
        if first in singular_rational_parameters
        else "smooth_parameter_over_Q"
    )

    return {
        "projective_pair": projective_pair,
        "affine": fraction_record(first),
        "alternate_affine": None if second is None else fraction_record(second),
        "identity_verified": identity_verified,
        "strictly_between_zero_and_one": Fraction(0) < first < Fraction(1),
        "van_luijk_fiber_status": status,
    }


def classify(data_path: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    payload = json.loads(data_path.read_text(encoding="utf-8"))
    points = payload.get("points", [])
    errors: list[str] = []
    derived_points: list[dict[str, Any]] = []
    lambda_groups: dict[str, list[int]] = defaultdict(list)
    lambda_categories: dict[str, set[str]] = defaultdict(set)
    category_counts: Counter[str] = Counter()
    boundary_count = 0
    conic_member_count = 0
    singular_parameter_count = 0
    positive_count = 0

    for index, row in enumerate(points):
        try:
            coords, mapping = map_to_standard(row)
        except (TypeError, ValueError) as exc:
            errors.append(f"points[{index}]: {exc}")
            continue

        equation_valid = standard_equations_hold(coords)
        if not equation_valid:
            errors.append(f"points[{index}]: standard equations failed")

        positive = all(value > 0 for value in coords.values())
        boundary = any(value == 0 for value in coords.values())
        conics = conic_memberships(coords)
        parameter = elliptic_parameter(coords)

        if positive:
            positive_count += 1
        if boundary:
            boundary_count += 1
        if conics:
            conic_member_count += 1
        if parameter["van_luijk_fiber_status"] != "smooth_parameter_over_Q":
            singular_parameter_count += 1
        if not parameter["identity_verified"]:
            errors.append(f"points[{index}]: lambda identity failed")

        affine = parameter.get("affine")
        lambda_text = None if affine is None else str(affine["text"])
        if lambda_text is not None:
            lambda_groups[lambda_text].append(index)
            lambda_categories[lambda_text].add(str(row[4]))

        category_counts[str(row[4])] += 1
        derived_points.append(
            {
                "source_index": index,
                "source_tuple": {
                    "a": row[0],
                    "b": row[1],
                    "c": row[2],
                    "d": row[3],
                    "category": row[4],
                },
                "standard_mapping": mapping,
                "standard_coordinates": coords,
                "standard_equations_valid": equation_valid,
                "strictly_positive_standard_coordinates": positive,
                "coordinate_boundary_member": boundary,
                "candidate_conic_ids": conics,
                "known_24_conic_member": bool(conics),
                "elliptic_fibration_parameter": parameter,
            }
        )

    repeated_groups = {
        key: indices for key, indices in lambda_groups.items() if len(indices) > 1
    }
    multiplicity_histogram = Counter(len(indices) for indices in lambda_groups.values())
    cross_category_groups = {
        key: {
            "indices": lambda_groups[key],
            "categories": sorted(lambda_categories[key]),
        }
        for key in lambda_groups
        if len(lambda_categories[key]) > 1
    }

    report = {
        "valid": not errors,
        "source": data_path.as_posix(),
        "point_count": len(points),
        "classified_point_count": len(derived_points),
        "category_counts": dict(sorted(category_counts.items())),
        "all_standard_equations_valid": all(
            point["standard_equations_valid"] for point in derived_points
        ),
        "strictly_positive_standard_coordinate_count": positive_count,
        "coordinate_boundary_member_count": boundary_count,
        "known_24_conic_member_count": conic_member_count,
        "singular_fiber_parameter_count": singular_parameter_count,
        "smooth_fiber_parameter_count": len(derived_points) - singular_parameter_count,
        "unique_lambda_count": len(lambda_groups),
        "repeated_lambda_group_count": len(repeated_groups),
        "max_points_on_one_lambda_fiber": max(
            (len(indices) for indices in lambda_groups.values()), default=0
        ),
        "lambda_multiplicity_histogram": {
            str(multiplicity): count
            for multiplicity, count in sorted(multiplicity_histogram.items())
        },
        "repeated_lambda_groups": repeated_groups,
        "cross_category_lambda_groups": cross_category_groups,
        "classification_scope": {
            "proved_by_this_script": [
                "standard-coordinate equations",
                "coordinate-boundary membership",
                "membership in van Luijk's explicitly listed 24 conics",
                "van Luijk elliptic-fibration parameter lambda",
            ],
            "not_proved_by_this_script": [
                "absence from every rational curve on the K3 surface",
                "membership in a specific curve on E x E' beyond the 24 conics",
                "any asymptotic upper bound for N_2(B)",
                "N_2(B)=o(N_1(B))",
            ],
        },
        "errors": errors,
    }

    derived = {
        "metadata": {
            "source": data_path.as_posix(),
            "standard_model": [
                "A^2+C^2=Y^2",
                "B^2+C^2=X^2",
                "A^2+X^2=U^2",
            ],
            "point_count": len(derived_points),
            "warning": (
                "candidate_conic_ids tests only van Luijk's explicitly listed "
                "24 conics; an empty list is not proof that the point lies on "
                "no other rational curve"
            ),
        },
        "points": derived_points,
    }
    return derived, report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--write-derived", type=Path, default=None)
    parser.add_argument("--write-report", type=Path, default=None)
    args = parser.parse_args()

    derived, report = classify(args.data)
    derived_text = json.dumps(derived, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    report_text = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"

    if args.write_derived is not None:
        args.write_derived.parent.mkdir(parents=True, exist_ok=True)
        args.write_derived.write_text(derived_text, encoding="utf-8")
    if args.write_report is not None:
        args.write_report.parent.mkdir(parents=True, exist_ok=True)
        args.write_report.write_text(report_text, encoding="utf-8")
    if args.write_derived is None and args.write_report is None:
        sys.stdout.write(report_text)

    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
