#!/usr/bin/env python3
"""Audit the j-map and a first local-divisibility sieve for two-face cuboids.

This stage deliberately distinguishes three statements:

1. ordinary local solubility of the fiber;
2. existence of a reduction with q and the standard coordinate B both units;
3. existence of a positive primitive integer point of bounded height.

Only (1) and the finite modular computations in (2) are decided here.  They
must not be promoted to a global point-counting theorem.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


DEFAULT_CLASSIFICATION = Path("data/two_face_cuboids_1e6_kummer_classification.json")
DEFAULT_REPORT = Path("data/two_face_cuboids_1e6_stage8_local_sieve_report.json")
THRESHOLDS = [10_000, 20_000, 50_000, 100_000, 200_000, 500_000, 1_000_000]
PRIME_LIMIT = 499


def primes_upto(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return [p for p in range(3, limit + 1, 2) if sieve[p]]


def symbolic_j_map() -> dict[str, Any]:
    t, x, s, X = sp.symbols("t x s X")
    a2 = sp.expand(4 * t**2 + (1 + t**2) ** 2)
    a4 = sp.expand(4 * t**2 * (1 + t**2) ** 2)
    b2 = 4 * a2
    b4 = 2 * a4
    b6 = sp.Integer(0)
    b8 = -a4**2
    c4 = sp.factor(b2**2 - 24 * b4)
    delta = sp.factor(-b2**2 * b8 - 8 * b4**3 - 27 * b6**2 + 9 * b2 * b4 * b6)

    expected_c4 = 16 * (
        t**4 - 2 * t**3 + 2 * t**2 + 2 * t + 1
    ) * (
        t**4 + 2 * t**3 + 2 * t**2 - 2 * t + 1
    )
    expected_delta = 256 * t**4 * (t - 1) ** 4 * (t + 1) ** 4 * (t**2 + 1) ** 4
    if sp.expand(c4 - expected_c4) != 0:
        raise ArithmeticError("unexpected c4 factorization")
    if sp.expand(delta - expected_delta) != 0:
        raise ArithmeticError("unexpected discriminant factorization")

    raw_numerator = sp.factor(c4**3)
    raw_denominator = sp.factor(delta)
    polynomial_gcd = sp.factor(
        sp.gcd(sp.Poly(raw_numerator, t), sp.Poly(raw_denominator, t)).as_expr()
    )
    if sp.degree(polynomial_gcd, t) != 0:
        raise ArithmeticError(
            f"j numerator and denominator have a positive-degree common factor {polynomial_gcd}"
        )
    reduced = sp.cancel(raw_numerator / raw_denominator)
    numerator, denominator = (
        sp.factor(part) for part in sp.fraction(reduced)
    )

    numerator_degree = sp.degree(numerator, t)
    denominator_degree = sp.degree(denominator, t)
    map_degree = max(numerator_degree, denominator_degree)
    infinity_pole_order = map_degree - denominator_degree
    if (numerator_degree, denominator_degree, map_degree, infinity_pole_order) != (24, 20, 24, 4):
        raise ArithmeticError("unexpected j-map degrees")

    # At infinity use t=1/s, x=X/s^4, y=Y/s^6.  The transformed cubic is
    # exactly the same family with parameter s, so infinity has the same
    # local model as t=0.
    transformed_rhs = sp.factor(
        s**12
        * (
            (X / s**4)
            * (X / s**4 + 4 / s**2)
            * (X / s**4 + (1 + 1 / s**2) ** 2)
        )
    )
    expected_transformed_rhs = sp.factor(X * (X + 4 * s**2) * (X + (1 + s**2) ** 2))
    if sp.factor(transformed_rhs - expected_transformed_rhs) != 0:
        raise ArithmeticError("reciprocal model at infinity did not match")

    finite_bad_factors = ["t", "t-1", "t+1", "t^2+1"]
    fibers = [
        {"place": "t=0", "ord_delta": 4, "ord_c4": 0, "kodaira_type": "I4"},
        {"place": "t=1", "ord_delta": 4, "ord_c4": 0, "kodaira_type": "I4"},
        {"place": "t=-1", "ord_delta": 4, "ord_c4": 0, "kodaira_type": "I4"},
        {
            "place": "t=i",
            "field": "Q(i)",
            "ord_delta": 4,
            "ord_c4": 0,
            "kodaira_type": "I4",
        },
        {
            "place": "t=-i",
            "field": "Q(i)",
            "ord_delta": 4,
            "ord_c4": 0,
            "kodaira_type": "I4",
        },
        {
            "place": "t=infinity",
            "ord_delta": 4,
            "ord_c4": 0,
            "kodaira_type": "I4",
            "verification": "reciprocal minimal model equals the t=0 model",
        },
    ]

    return {
        "weierstrass_model": "y^2=x(x+4t^2)(x+(1+t^2)^2)",
        "a2": str(a2),
        "a4": str(a4),
        "c4_factorized": str(c4),
        "delta_factorized": str(delta),
        "j_factorized": f"({sp.factor(numerator)})/({sp.factor(denominator)})",
        "j_numerator_denominator_polynomial_gcd": str(polynomial_gcd),
        "j_common_factor_is_constant_only": True,
        "j_numerator_degree": int(numerator_degree),
        "j_denominator_degree": int(denominator_degree),
        "j_map_degree": int(map_degree),
        "infinity_pole_order": int(infinity_pole_order),
        "finite_discriminant_factors": finite_bad_factors,
        "singular_fibers": fibers,
        "euler_number_sum": sum(fiber["ord_delta"] for fiber in fibers),
        "scope_note": (
            "degree 24 is obtained from this explicit rational function; it is not inferred "
            "from the K3 property alone"
        ),
    }


def reduced_lambda(point: dict[str, Any]) -> tuple[int, int]:
    affine = point["elliptic_fibration_parameter"]["affine"]
    m = int(affine["numerator"])
    n = int(affine["denominator"])
    g = math.gcd(m, n)
    m //= g
    n //= g
    if not (0 < m < n):
        raise ArithmeticError(f"lambda is not reduced in (0,1): {m}/{n}")
    return m, n


def point_q(point: dict[str, Any], m: int, n: int) -> int:
    coords = point["standard_coordinates"]
    numerator = 2 * int(coords["Y"])
    denominator = m * m + n * n
    q, rem = divmod(numerator, denominator)
    if rem:
        raise ArithmeticError("q=2Y/(m^2+n^2) is not integral")
    if 2 * int(coords["A"]) != q * (n * n - m * m):
        raise ArithmeticError("A parameterization failed")
    if int(coords["C"]) != q * m * n:
        raise ArithmeticError("C parameterization failed")
    if 2 * int(coords["Y"]) != q * (m * m + n * n):
        raise ArithmeticError("Y parameterization failed")
    if (m + n) % 2 == 1 and q % 2:
        raise ArithmeticError("opposite-parity parameters require even q")
    return q


def candidate_pair_count(bound: int) -> int:
    count = 0
    radius_squared = 2 * bound
    max_n = math.isqrt(radius_squared)
    for n in range(2, max_n + 1):
        remaining = radius_squared - n * n
        if remaining <= 0:
            continue
        max_m = min(n - 1, math.isqrt(remaining))
        for m in range(1, max_m + 1):
            if math.gcd(m, n) == 1:
                count += 1
    return count


def projective_class(m: int, n: int, p: int) -> str:
    mr = m % p
    nr = n % p
    if nr == 0:
        return "infinity"
    return str((mr * pow(nr, -1, p)) % p)


def has_b_unit_solution_for_class(label: str, p: int) -> bool:
    inv2 = pow(2, -1, p)
    if label == "infinity":
        m, n = 1, 0
    else:
        m, n = int(label), 1
    a0 = ((n * n - m * m) * inv2) % p
    c0 = (m * n) % p
    squares = {z * z % p for z in range(p)}
    for x0 in range(p):
        b2 = (x0 * x0 - c0 * c0) % p
        if b2 == 0 or b2 not in squares:
            continue
        u2 = (a0 * a0 + x0 * x0) % p
        if u2 in squares:
            return True
    return False


def obstructed_classes(p: int) -> list[str]:
    labels = [str(t) for t in range(p)] + ["infinity"]
    return [label for label in labels if not has_b_unit_solution_for_class(label, p)]


def empirical_thresholds(points: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    previous: dict[str, Any] | None = None
    for bound in THRESHOLDS:
        selected = [point for point in points if int(point["source_tuple"]["d"]) <= bound]
        lambdas = {reduced_lambda(point) for point in selected}
        point_count = len(selected)
        fiber_count = len(lambdas)
        row: dict[str, Any] = {
            "B": bound,
            "two_face_point_count": point_count,
            "realized_lambda_count": fiber_count,
            "mean_points_per_realized_lambda": point_count / fiber_count if fiber_count else 0.0,
            "repeat_excess": point_count - fiber_count,
            "all_reduced_parameter_pair_count": candidate_pair_count(bound),
        }
        row["realized_fraction_of_parameter_pairs"] = (
            fiber_count / row["all_reduced_parameter_pair_count"]
            if row["all_reduced_parameter_pair_count"]
            else 0.0
        )
        if previous and previous["two_face_point_count"] and point_count:
            row["local_log_slope_N2"] = math.log(
                point_count / previous["two_face_point_count"]
            ) / math.log(bound / previous["B"])
        else:
            row["local_log_slope_N2"] = None
        if previous and previous["realized_lambda_count"] and fiber_count:
            row["local_log_slope_realized_lambda"] = math.log(
                fiber_count / previous["realized_lambda_count"]
            ) / math.log(bound / previous["B"])
        else:
            row["local_log_slope_realized_lambda"] = None
        rows.append(row)
        previous = row
    return rows


def local_divisibility_audit(points: list[dict[str, Any]]) -> dict[str, Any]:
    primes = primes_upto(PRIME_LIMIT)
    per_prime: list[dict[str, Any]] = []
    obstructing_primes: list[int] = []

    point_cache: list[tuple[dict[str, Any], int, int, int]] = []
    for point in points:
        m, n = reduced_lambda(point)
        q = point_q(point, m, n)
        point_cache.append((point, m, n, q))

    for p in primes:
        bad = obstructed_classes(p)
        bad_set = set(bad)
        if bad:
            obstructing_primes.append(p)
        observed_hits = 0
        q_only = 0
        b_only = 0
        both = 0
        for point, m, n, q in point_cache:
            label = projective_class(m, n, p)
            if label not in bad_set:
                continue
            observed_hits += 1
            b_coord = int(point["standard_coordinates"]["B"])
            q_divides = q % p == 0
            b_divides = b_coord % p == 0
            if not (q_divides or b_divides):
                raise ArithmeticError(
                    f"local divisibility implication failed at p={p}, lambda={m}/{n}"
                )
            if q_divides and b_divides:
                both += 1
            elif q_divides:
                q_only += 1
            else:
                b_only += 1
        per_prime.append(
            {
                "p": p,
                "projective_class_count": p + 1,
                "ordinary_local_obstruction_count": 0,
                "b_unit_obstructed_class_count": len(bad),
                "b_unit_obstructed_classes": bad,
                "observed_points_in_obstructed_classes": observed_hits,
                "observed_divisibility_explanation": {
                    "p_divides_q_only": q_only,
                    "p_divides_B_only": b_only,
                    "p_divides_both": both,
                },
            }
        )

    bad_lookup = {
        row["p"]: set(row["b_unit_obstructed_classes"])
        for row in per_prime
        if row["b_unit_obstructed_class_count"]
    }
    divisor_sieve_rows: list[dict[str, Any]] = []
    for bound in THRESHOLDS:
        total = 0
        excluded = 0
        max_forced_product = 1
        radius_squared = 2 * bound
        max_n = math.isqrt(radius_squared)
        for n in range(2, max_n + 1):
            remaining = radius_squared - n * n
            if remaining <= 0:
                continue
            max_m = min(n - 1, math.isqrt(remaining))
            for m in range(1, max_m + 1):
                if math.gcd(m, n) != 1:
                    continue
                total += 1
                forced_product = 2 if (m + n) % 2 == 1 else 1
                for p, bad_set in bad_lookup.items():
                    if projective_class(m, n, p) in bad_set:
                        forced_product *= p
                max_forced_product = max(max_forced_product, forced_product)
                # If p is in the bad set, p divides q*B_coordinate.  Since
                # q <= 2d/(m^2+n^2) and B_coordinate <= d, q*B_coordinate
                # <= 2*bound^2/(m^2+n^2).  Exclusion is rigorous only when
                # the forced squarefree product exceeds this upper bound.
                upper_q_times_B = (2 * bound * bound) // (m * m + n * n)
                if forced_product > upper_q_times_B:
                    excluded += 1
        divisor_sieve_rows.append(
            {
                "B": bound,
                "candidate_parameter_pairs": total,
                "rigorously_excluded_by_simple_qB_divisibility": excluded,
                "surviving_parameter_pairs": total - excluded,
                "maximum_forced_squarefree_product": max_forced_product,
            }
        )

    return {
        "prime_limit": PRIME_LIMIT,
        "primes_tested": primes,
        "ordinary_local_solubility": {
            "all_projective_parameter_classes_admissible": True,
            "universal_boundary_solution": (
                "after scaling by q: b=0, x=c0=mn, "
                "u=(m^2+n^2)/2; equivalently B=0, X=C, U=Y"
            ),
            "consequence": (
                "ordinary local solubility cannot remove any lambda class because every fiber "
                "contains the boundary conic section"
            ),
        },
        "b_unit_refinement": {
            "meaning": (
                "if a projective lambda class has no solution with p not dividing qB, then every "
                "global integer point in that class satisfies p | qB"
            ),
            "obstructing_primes_in_tested_range": obstructing_primes,
            "per_prime": per_prime,
            "observed_point_checks_pass": True,
        },
        "simple_divisor_sieve": {
            "rows": divisor_sieve_rows,
            "scope": (
                "uses only parity and the tested p|qB implications; zero exclusions do not rule "
                "out stronger square-sieve, p-adic-height or determinant-method arguments"
            ),
        },
    }


def build_report(classification_path: Path) -> dict[str, Any]:
    data = json.loads(classification_path.read_text(encoding="utf-8"))
    points = data["points"]
    if len(points) != 255:
        raise ArithmeticError(f"expected 255 points, found {len(points)}")

    q_values: list[int] = []
    opposite_parity_count = 0
    for point in points:
        m, n = reduced_lambda(point)
        q = point_q(point, m, n)
        q_values.append(q)
        if (m + n) % 2 == 1:
            opposite_parity_count += 1

    threshold_rows = empirical_thresholds(points)
    local = local_divisibility_audit(points)
    simple_exclusions = sum(
        row["rigorously_excluded_by_simple_qB_divisibility"]
        for row in local["simple_divisor_sieve"]["rows"]
    )

    return {
        "valid": True,
        "metadata": {
            "source": str(classification_path),
            "point_count": len(points),
            "thresholds": THRESHOLDS,
        },
        "j_map": symbolic_j_map(),
        "integer_parameterization": {
            "lambda": "m/n with gcd(m,n)=1 and 0<m<n",
            "q_definition": "q=2Y/(m^2+n^2) in Z",
            "coordinates": [
                "A=q(n^2-m^2)/2",
                "C=qmn",
                "Y=q(m^2+n^2)/2",
            ],
            "parity_rule": "if m,n have opposite parity then q is even",
            "all_255_points_verified": True,
            "opposite_parity_point_count": opposite_parity_count,
            "q_summary": {
                "min": min(q_values),
                "max": max(q_values),
                "mean": sum(q_values) / len(q_values),
                "median": sorted(q_values)[len(q_values) // 2],
            },
        },
        "empirical_growth": {
            "rows": threshold_rows,
            "warning": (
                "local log-slopes and realized fractions are finite-data diagnostics, not "
                "asymptotic exponents or density theorems"
            ),
        },
        "local_divisibility_audit": local,
        "decision": {
            "deg_j_24_verified": True,
            "route_A_status": (
                "deprioritized for generic Silverman-bound optimization, but not proved impossible "
                "for the special positive primitive integral subset"
            ),
            "ordinary_local_sparsity_route_succeeds": False,
            "simple_local_divisibility_sieve_exclusion_total": simple_exclusions,
            "why_local_route_does_not_close": (
                "the universal B=0 boundary section gives local points for every lambda; the "
                "first qB-unit refinement produces no candidate exclusions at the audited bounds"
            ),
            "next_research_options": [
                "square sieve after Pythagorean parameterization",
                "determinant-method/direct counting for the extra square conditions",
                "construct a rigorous lower-bound family for the one-face count N1(B)",
            ],
            "wall_discussion_recommended_after_stage8": True,
        },
        "not_proved": [
            "that realized-lambda sparsity is caused by local congruence obstructions",
            "an asymptotic exponent for N2(B) or the realized-lambda count",
            "N2(B)=O(B^(1/2+epsilon))",
            "a global upper bound for N2(B)",
            "N2(B)=o(N1(B))",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--classification", type=Path, default=DEFAULT_CLASSIFICATION)
    parser.add_argument("--write-report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    report = build_report(args.classification)
    args.write_report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "valid": report["valid"],
        "j_map_degree": report["j_map"]["j_map_degree"],
        "singular_fibers": len(report["j_map"]["singular_fibers"]),
        "obstructing_primes": report["local_divisibility_audit"]["b_unit_refinement"]["obstructing_primes_in_tested_range"],
        "simple_exclusion_total": report["decision"]["simple_local_divisibility_sieve_exclusion_total"],
        "wall_discussion_recommended": report["decision"]["wall_discussion_recommended_after_stage8"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
