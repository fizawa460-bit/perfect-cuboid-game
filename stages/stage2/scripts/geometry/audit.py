#!/usr/bin/env python3
"""Audit the fixed two-face cuboid dataset and the standard face-cuboid surface.

The data audit uses only Python's standard library.  The optional geometry audit
requires SymPy and independently solves the Jacobian singular-locus equations
for the standard model

    A^2 + C^2 = Y^2,
    B^2 + C^2 = X^2,
    A^2 + X^2 = U^2

in P^5 over an algebraic closure of Q.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Any


DEFAULT_DATA = Path("data/two_face_cuboids_1e6_fixed.json")
DEFAULT_REPORT = Path("data/two_face_cuboids_1e6_audit_report.json")
CATEGORIES = ("ab+ac", "ab+bc", "ac+bc", "perfect")
EXPECTED_SCHEMA = [
    "a",
    "b",
    "c",
    "d",
    "category",
    "diag_ab",
    "diag_ac",
    "diag_bc",
]


def integer_square_root(value: int) -> int | None:
    if value < 0:
        return None
    root = math.isqrt(value)
    return root if root * root == value else None


def expected_category(
    diag_ab: int | None,
    diag_ac: int | None,
    diag_bc: int | None,
) -> str | None:
    flags = {
        "ab": diag_ab is not None,
        "ac": diag_ac is not None,
        "bc": diag_bc is not None,
    }
    active = [name for name, present in flags.items() if present]
    if len(active) == 3:
        return "perfect"
    if len(active) == 2:
        return "+".join(active)
    return None


def audit_data(data_path: Path) -> dict[str, Any]:
    payload = json.loads(data_path.read_text(encoding="utf-8"))
    metadata = payload.get("metadata", {})
    points = payload.get("points", [])
    errors: list[str] = []

    if metadata.get("pointSchema") != EXPECTED_SCHEMA:
        errors.append(
            f"pointSchema mismatch: expected {EXPECTED_SCHEMA!r}, "
            f"got {metadata.get('pointSchema')!r}"
        )

    max_d = int(metadata.get("maxD", 0))
    seen: set[tuple[int, int, int, int]] = set()
    category_counts: Counter[str] = Counter()
    actual_threshold_counts: dict[str, dict[str, int]] = {}
    previous_d = -1
    sorted_by_d = True

    for index, row in enumerate(points):
        label = f"points[{index}]"
        if not isinstance(row, list) or len(row) != 8:
            errors.append(f"{label}: expected an 8-item list, got {row!r}")
            continue

        a, b, c, d, category, stored_ab, stored_ac, stored_bc = row

        if not all(isinstance(value, int) for value in (a, b, c, d)):
            errors.append(f"{label}: a,b,c,d must all be integers")
            continue
        if category not in CATEGORIES:
            errors.append(f"{label}: unsupported category {category!r}")

        if not (0 < a < b < c):
            errors.append(f"{label}: ordering/positivity failed: {(a, b, c)!r}")
        if math.gcd(math.gcd(a, b), c) != 1:
            errors.append(f"{label}: gcd(a,b,c) is not 1")
        if d > max_d:
            errors.append(f"{label}: d={d} exceeds metadata maxD={max_d}")
        if a * a + b * b + c * c != d * d:
            errors.append(f"{label}: space-diagonal equation failed")

        if d < previous_d:
            sorted_by_d = False
        previous_d = d

        key = (a, b, c, d)
        if key in seen:
            errors.append(f"{label}: duplicate tuple {key!r}")
        seen.add(key)

        calc_ab = integer_square_root(a * a + b * b)
        calc_ac = integer_square_root(a * a + c * c)
        calc_bc = integer_square_root(b * b + c * c)
        calculated = (calc_ab, calc_ac, calc_bc)
        stored = (stored_ab, stored_ac, stored_bc)

        if stored != calculated:
            errors.append(
                f"{label}: stored face diagonals {stored!r} "
                f"do not equal calculated {calculated!r}"
            )

        derived_category = expected_category(*calculated)
        if derived_category is None:
            errors.append(f"{label}: fewer than two face diagonals are integral")
        elif category != derived_category:
            errors.append(
                f"{label}: category {category!r} != derived {derived_category!r}"
            )

        if category != "perfect":
            if sum(value is not None for value in calculated) != 2:
                errors.append(
                    f"{label}: exactly-two record does not have exactly two squares"
                )

        category_counts[str(category)] += 1

    metadata_counts = metadata.get("counts", {})
    for threshold_text, expected in metadata_counts.items():
        threshold = int(threshold_text)
        rows = [
            row
            for row in points
            if isinstance(row, list) and len(row) == 8 and row[3] <= threshold
        ]
        counts = Counter(str(row[4]) for row in rows)
        actual = {
            "total": len(rows),
            "ab+ac": counts["ab+ac"],
            "ab+bc": counts["ab+bc"],
            "ac+bc": counts["ac+bc"],
            "perfect": counts["perfect"],
        }
        actual_threshold_counts[threshold_text] = actual
        if actual != expected:
            errors.append(
                f"threshold {threshold_text}: metadata {expected!r} != actual {actual!r}"
            )

    expected_final = metadata_counts.get(str(max_d))
    if expected_final is not None:
        final_counts = {
            "total": len(points),
            "ab+ac": category_counts["ab+ac"],
            "ab+bc": category_counts["ab+bc"],
            "ac+bc": category_counts["ac+bc"],
            "perfect": category_counts["perfect"],
        }
        if final_counts != expected_final:
            errors.append(
                f"maxD category counts: metadata {expected_final!r} "
                f"!= actual {final_counts!r}"
            )

    return {
        "valid": not errors,
        "source": data_path.as_posix(),
        "point_count": len(points),
        "max_d_limit": max_d,
        "max_d_observed": max((row[3] for row in points), default=None),
        "sorted_by_d": sorted_by_d,
        "duplicate_count": len(points) - len(seen),
        "category_counts": {
            category: category_counts[category] for category in CATEGORIES
        },
        "threshold_counts_verified": not any(
            error.startswith("threshold ") for error in errors
        ),
        "actual_threshold_counts": actual_threshold_counts,
        "errors": errors,
    }


def _canonical_sympy(value: Any) -> str:
    import sympy as sp

    value = sp.simplify(value)
    if value == sp.I:
        return "i"
    if value == -sp.I:
        return "-i"
    return str(value)


def _normalize_projective(point: tuple[Any, ...]) -> tuple[Any, ...]:
    import sympy as sp

    for value in point:
        value = sp.simplify(value)
        if value != 0:
            return tuple(sp.simplify(entry / value) for entry in point)
    raise ValueError("zero projective vector")


def audit_geometry() -> dict[str, Any]:
    try:
        import sympy as sp
    except ImportError as exc:
        raise RuntimeError(
            "The geometry audit requires SymPy. Install it with "
            "`python -m pip install sympy`."
        ) from exc

    A, B, C, X, Y, U = sp.symbols("A B C X Y U")
    variables = (A, B, C, X, Y, U)
    equations = (
        A**2 + C**2 - Y**2,
        B**2 + C**2 - X**2,
        A**2 + X**2 - U**2,
    )
    jacobian = sp.Matrix(equations).jacobian(variables)
    nonzero_minors = []
    for columns in combinations(range(6), 3):
        determinant = sp.factor(jacobian[:, columns].det())
        if determinant != 0:
            nonzero_minors.append(determinant)

    singular_points: set[tuple[Any, ...]] = set()
    chart_solution_counts: dict[str, int] = {}
    for chart_index, chart_variable in enumerate(variables):
        remaining = variables[:chart_index] + variables[chart_index + 1 :]
        chart_equations = [
            sp.expand(expression.subs(chart_variable, 1))
            for expression in equations + tuple(nonzero_minors)
        ]
        solutions = sp.solve_poly_system(chart_equations, *remaining)
        chart_solution_counts[str(chart_variable)] = len(solutions)
        for solution in solutions:
            entries = list(solution)
            entries.insert(chart_index, sp.Integer(1))
            singular_points.add(_normalize_projective(tuple(entries)))

    expected_points: set[tuple[Any, ...]] = set()
    for epsilon in (sp.Integer(1), sp.Integer(-1)):
        for delta in (sp.Integer(1), sp.Integer(-1)):
            expected_points.add((1, 0, 0, 0, epsilon, delta))
            expected_points.add((0, 1, 0, epsilon, 0, delta))
            expected_points.add((1, 0, epsilon * sp.I, delta * sp.I, 0, 0))
            expected_points.add((0, 1, epsilon * sp.I, 0, delta * sp.I, 0))

    missing = expected_points - singular_points
    unexpected = singular_points - expected_points

    rank_failures: list[list[str]] = []
    positive_region_count = 0
    rational_count = 0
    qi_nonrational_count = 0
    formatted_points: list[list[str]] = []

    for point in singular_points:
        rank = jacobian.subs(dict(zip(variables, point))).rank()
        if rank != 2:
            rank_failures.append([_canonical_sympy(value) for value in point])

        if all(value.is_real is True and value > 0 for value in point):
            positive_region_count += 1

        has_i = any(sp.simplify(value).has(sp.I) for value in point)
        if has_i:
            qi_nonrational_count += 1
        else:
            rational_count += 1
        formatted_points.append([_canonical_sympy(value) for value in point])

    # One representative of each of the four symmetry types. After eliminating
    # two smooth local variables, the residual quadratic tangent cones are:
    tangent_cones = (
        B**2 + C**2 - X**2,
        A**2 + C**2 - Y**2,
        B**2 + Y**2 - U**2,
        A**2 + X**2 - U**2,
    )
    tangent_variables = ((B, C, X), (A, C, Y), (B, Y, U), (A, X, U))
    hessian_determinants = [
        int(sp.det(sp.hessian(cone, variables_)))
        for cone, variables_ in zip(tangent_cones, tangent_variables)
    ]

    errors: list[str] = []
    if len(singular_points) != 16:
        errors.append(f"expected 16 singular points, found {len(singular_points)}")
    if missing:
        errors.append(f"missing expected singular points: {len(missing)}")
    if unexpected:
        errors.append(f"unexpected singular points: {len(unexpected)}")
    if rank_failures:
        errors.append(f"Jacobian rank was not 2 at {len(rank_failures)} points")
    if any(value == 0 for value in hessian_determinants):
        errors.append("a representative tangent-cone Hessian is degenerate")
    if positive_region_count != 0:
        errors.append("a singular point was found in the strictly positive region")
    if rational_count != 8 or qi_nonrational_count != 8:
        errors.append(
            "unexpected field split: "
            f"Q={rational_count}, Q(i)\\Q={qi_nonrational_count}"
        )

    formatted_points.sort(key=lambda row: tuple(row))
    return {
        "valid": not errors,
        "model": [
            "A^2+C^2-Y^2=0",
            "B^2+C^2-X^2=0",
            "A^2+X^2-U^2=0",
        ],
        "nonzero_jacobian_3x3_minors": len(nonzero_minors),
        "chart_solution_counts_before_deduplication": chart_solution_counts,
        "geometric_singular_point_count": len(singular_points),
        "q_rational_point_count": rational_count,
        "qi_nonrational_point_count": qi_nonrational_count,
        "positive_region_singular_point_count": positive_region_count,
        "jacobian_rank_two_at_all_points": not rank_failures,
        "representative_tangent_cone_hessian_determinants": hessian_determinants,
        "all_representative_tangent_cones_nondegenerate": all(
            value != 0 for value in hessian_determinants
        ),
        "singular_points": formatted_points,
        "errors": errors,
    }


def build_report(data_path: Path, include_geometry: bool) -> dict[str, Any]:
    report: dict[str, Any] = {
        "data_audit": audit_data(data_path),
    }
    if include_geometry:
        report["geometry_audit"] = audit_geometry()
    report["valid"] = all(
        section.get("valid", False)
        for name, section in report.items()
        if name.endswith("_audit")
    )
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data",
        type=Path,
        default=DEFAULT_DATA,
        help=f"source JSON (default: {DEFAULT_DATA})",
    )
    parser.add_argument(
        "--geometry",
        action="store_true",
        help="also solve the Jacobian singular-locus equations with SymPy",
    )
    parser.add_argument(
        "--write-report",
        type=Path,
        default=None,
        help=(
            "write the JSON report to this path; use an explicit path such as "
            f"{DEFAULT_REPORT}"
        ),
    )
    args = parser.parse_args()

    report = build_report(args.data, args.geometry)
    output = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"

    if args.write_report is not None:
        args.write_report.parent.mkdir(parents=True, exist_ok=True)
        args.write_report.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)

    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
