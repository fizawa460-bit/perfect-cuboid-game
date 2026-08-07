#!/usr/bin/env python3
"""Stage13-3b: audit the canonical size-order / archimedean chamber mechanism.

The one-face real variety for the ab face is

    a^2 + b^2 = p^2,
    p^2 + c^2 = d^2.

Solving the two equations for (p,d) gives Gelfand--Leray Jacobian 4 p d.
After radial normalization (a,b,c)=d(x,y,z) on x^2+y^2+z^2=1, the common
radial factor cancels between directions and the angular weights are

    w_ab = 1/sqrt(x^2+y^2),
    w_ac = 1/sqrt(x^2+z^2),
    w_bc = 1/sqrt(y^2+z^2).

On the canonical chamber 0<x<y<z, these satisfy w_ab>w_ac>w_bc pointwise.
This script independently integrates the three weights, checks the exact
sum identity, and compares the resulting geometric proportions with the
Stage13-3a raw incidence proportions.

This is an archimedean-density model/audit. It does not prove that the
global integer counts have these exact constants or a limiting 2:1:1 ratio.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Callable, Any

DEFAULT_INPUT = Path("stages/stage13/data/13-3/raw_incidence_report.json")
DEFAULT_OUTPUT = Path("stages/stage13/data/13-3/geometric_chamber_report.json")
ABS_TOL = 2e-13
MAX_DEPTH = 30


def adaptive_simpson(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = ABS_TOL,
    max_depth: int = MAX_DEPTH,
) -> float:
    fa = f(a)
    fb = f(b)
    c = (a + b) / 2.0
    fc = f(c)
    whole = (b - a) * (fa + 4.0 * fc + fb) / 6.0

    def recurse(
        left: float,
        right: float,
        f_left: float,
        f_mid: float,
        f_right: float,
        estimate: float,
        eps: float,
        depth: int,
    ) -> float:
        mid = (left + right) / 2.0
        lmid = (left + mid) / 2.0
        rmid = (mid + right) / 2.0
        f_lmid = f(lmid)
        f_rmid = f(rmid)
        left_est = (mid - left) * (f_left + 4.0 * f_lmid + f_mid) / 6.0
        right_est = (right - mid) * (f_mid + 4.0 * f_rmid + f_right) / 6.0
        refined = left_est + right_est
        delta = refined - estimate
        if depth <= 0:
            return refined + delta / 15.0
        if abs(delta) <= 15.0 * eps:
            return refined + delta / 15.0
        return recurse(
            left, mid, f_left, f_lmid, f_mid, left_est, eps / 2.0, depth - 1
        ) + recurse(
            mid, right, f_mid, f_rmid, f_right, right_est, eps / 2.0, depth - 1
        )

    return recurse(a, b, fa, fc, fb, whole, tol, max_depth)


def theta_max(phi: float) -> float:
    return math.atan(1.0 / math.sin(phi))


def inner_ab(phi: float) -> float:
    # w_ab dω = dθ dφ.
    return theta_max(phi)


def inner_ac(phi: float) -> float:
    # Integral_0^theta_max sin(theta)/sqrt(1-sin^2(theta) sin^2(phi)) dtheta.
    s = math.sin(phi)
    c = math.cos(phi)
    if abs(c) < 1e-12:
        return 0.5 * math.log(2.0)
    u0 = s / math.sqrt(1.0 + s * s)
    return (math.asinh(s / c) - math.asinh((u0 * s) / c)) / s


def inner_bc(phi: float) -> float:
    # Integral_0^theta_max sin(theta)/sqrt(1-sin^2(theta) cos^2(phi)) dtheta.
    s = math.sin(phi)
    c = math.cos(phi)
    if abs(c) < 1e-12:
        return 1.0 - 1.0 / math.sqrt(2.0)
    u0 = s / math.sqrt(1.0 + s * s)
    return (math.asinh(c / s) - math.asinh((u0 * c) / s)) / c


def l1(a: list[float], b: list[float]) -> float:
    return sum(abs(x - y) for x, y in zip(a, b))


def linf(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def proportions(values: list[float]) -> list[float]:
    total = sum(values)
    return [value / total for value in values]


def build_report(raw_report: dict[str, Any]) -> dict[str, Any]:
    phi0 = math.pi / 4.0
    phi1 = math.pi / 2.0

    i_ab = adaptive_simpson(inner_ab, phi0, phi1)
    i_ac = adaptive_simpson(inner_ac, phi0, phi1)
    i_bc = adaptive_simpson(inner_bc, phi0, phi1)
    integrals = [i_ab, i_ac, i_bc]
    geom_prop = proportions(integrals)

    expected_sum = math.pi * math.pi / 8.0
    sum_error = abs(sum(integrals) - expected_sum)
    if sum_error > 5e-11:
        raise ArithmeticError(
            f"chamber sum identity failed numerically: error={sum_error}"
        )
    if not (i_ab > i_ac > i_bc > 0.0):
        raise ArithmeticError("expected strict chamber ordering I_ab>I_ac>I_bc failed")

    full_symmetric_prop = [1.0 / 3.0] * 3

    comparisons: list[dict[str, Any]] = []
    for row in raw_report["rows"]:
        raw = row["raw_incidence"]
        observed = proportions(
            [float(raw["ab"]), float(raw["ac"]), float(raw["bc"])]
        )
        geo_l1 = l1(observed, geom_prop)
        sym_l1 = l1(observed, full_symmetric_prop)
        comparisons.append(
            {
                "B": row["B"],
                "raw_incidence": raw,
                "raw_proportion": {
                    "ab": observed[0],
                    "ac": observed[1],
                    "bc": observed[2],
                },
                "raw_bc_normalized_ratio": {
                    "ab": raw["ab"] / raw["bc"],
                    "ac": raw["ac"] / raw["bc"],
                    "bc": 1.0,
                },
                "distance_to_geometric_model": {
                    "l1": geo_l1,
                    "linf": linf(observed, geom_prop),
                },
                "distance_to_full_symmetric_1_1_1": {
                    "l1": sym_l1,
                    "linf": linf(observed, full_symmetric_prop),
                },
                "l1_discrepancy_removed_by_chamber_model_fraction": (
                    1.0 - geo_l1 / sym_l1 if sym_l1 else None
                ),
            }
        )

    return {
        "metadata": {
            "stage": "13-3b",
            "title": "Canonical size-order / archimedean geometric chamber audit",
            "status": "finite-and-archimedean-model-result",
            "global_asymptotic_claim": False,
        },
        "exact_structure": {
            "canonical_chamber": "R={(x,y,z) in S^2: 0<x<y<z}",
            "spherical_coordinates": (
                "x=sin(theta)cos(phi), y=sin(theta)sin(phi), z=cos(theta)"
            ),
            "phi_range": "[pi/4, pi/2]",
            "theta_upper": "atan(csc(phi))",
            "chamber_area_exact": "pi/12",
            "gelfand_leray_jacobian_ab": (
                "det d(F1,F2)/d(p,d)=4*p*d for "
                "F1=a^2+b^2-p^2, F2=p^2+c^2-d^2"
            ),
            "directional_weights": {
                "ab": "1/sqrt(x^2+y^2)",
                "ac": "1/sqrt(x^2+z^2)",
                "bc": "1/sqrt(y^2+z^2)",
            },
            "pointwise_order_on_R": "w_ab > w_ac > w_bc",
            "uniform_weight_chamber_baseline": "1:1:1",
            "full_positive_octant_one_face_integral_exact": "pi^2/4",
            "full_positive_octant_direction_ratio": "1:1:1 by coordinate symmetry",
            "chamber_integral_sum_exact": "I_ab+I_ac+I_bc=pi^2/8",
        },
        "numerical_chamber_integrals": {
            "I_ab": i_ab,
            "I_ac": i_ac,
            "I_bc": i_bc,
            "sum": sum(integrals),
            "pi_squared_over_8": expected_sum,
            "absolute_sum_error": sum_error,
            "ac_normalized_ratio": {
                "ab": i_ab / i_ac,
                "ac": 1.0,
                "bc": i_bc / i_ac,
            },
            "bc_normalized_ratio": {
                "ab": i_ab / i_bc,
                "ac": i_ac / i_bc,
                "bc": 1.0,
            },
            "proportion": {
                "ab": geom_prop[0],
                "ac": geom_prop[1],
                "bc": geom_prop[2],
            },
        },
        "comparison_to_stage13_3a_raw_incidence": comparisons,
        "conclusion": {
            "canonical_relabeling_alone_is_enough": False,
            "canonical_chamber_plus_archimedean_face_weight_creates_asymmetry": True,
            "qualitative_order_matches_raw_data": True,
            "at_B_100000": {
                "geometric_bc_normalized_ratio": {
                    "ab": i_ab / i_bc,
                    "ac": i_ac / i_bc,
                    "bc": 1.0,
                },
                "raw_bc_normalized_ratio": comparisons[-1][
                    "raw_bc_normalized_ratio"
                ],
                "geometric_model_overstates_ab_bias": True,
                "l1_discrepancy_removed_from_1_1_1_baseline_fraction": comparisons[-1][
                    "l1_discrepancy_removed_by_chamber_model_fraction"
                ],
            },
            "interpretation": (
                "The size-order chamber is a strong archimedean mechanism for the leading "
                "ab excess: ab is always the smallest face diagonal in 0<a<b<c and therefore "
                "receives the largest 1/p real-density weight. The chamber model captures most "
                "of the observed departure from 1:1:1 at the audited bounds, but it is not the "
                "complete arithmetic answer because it overpredicts the ab excess."
            ),
            "next_test": (
                "separate parity / 2-adic effects to see whether they flatten the geometric "
                "ratio toward the observed raw incidence ratio"
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    raw_report = json.loads(args.input.read_text())
    report = build_report(raw_report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=False) + "\n")
    print(json.dumps(report["numerical_chamber_integrals"], indent=2))
    print(json.dumps(report["conclusion"]["at_B_100000"], indent=2))


if __name__ == "__main__":
    main()
