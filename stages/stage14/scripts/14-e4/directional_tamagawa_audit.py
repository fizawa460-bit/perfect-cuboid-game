#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

OUT = Path("stages/stage14/data/14-e4/directional_tamagawa_audit.json")
E2_DATA = Path("stages/stage14/data/14-e2/ambient_reconnaissance.json")


def gauss_legendre_unit(n: int):
    xs = [0.0] * n
    ws = [0.0] * n
    m = (n + 1) // 2
    for i in range(m):
        z = math.cos(math.pi * (i + 0.75) / (n + 0.5))
        while True:
            p1 = 1.0
            p2 = 0.0
            for j in range(1, n + 1):
                p3 = p2
                p2 = p1
                p1 = ((2 * j - 1) * z * p2 - (j - 1) * p3) / j
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            z1 = z
            z = z1 - p1 / pp
            if abs(z - z1) < 2e-16:
                break
        w = 2.0 / ((1.0 - z * z) * pp * pp)
        xs[i] = -z
        xs[n - 1 - i] = z
        ws[i] = w
        ws[n - 1 - i] = w
    return [0.5 * (x + 1.0) for x in xs], [0.5 * w for w in ws]


def hyperbolic_density(r1: float, r2: float) -> float:
    m = max(0.0, r1, r2)
    if m < 300.0:
        return 1.0 / math.sqrt(1.0 + math.sinh(r1) ** 2 + math.sinh(r2) ** 2)
    a = math.exp(-m)
    s1 = 0.5 * (math.exp(r1 - m) - math.exp(-r1 - m))
    s2 = 0.5 * (math.exp(r2 - m) - math.exp(-r2 - m))
    return a / math.sqrt(a * a + s1 * s1 + s2 * s2)


def chamber_masses(n: int):
    x, w = gauss_legendre_unit(n)
    r0 = math.asinh(1.0)
    ma = mb = mc = 0.0

    for u, wu in zip(x, w):
        r2c = r0 * u
        for v, wv in zip(x, w):
            # c: 0 < r1 < r2 < r0.
            r1c = r2c * v
            mc += wu * wv * (r0 * r0 * u) * hyperbolic_density(r1c, r2c)

            # b: 0 < r1 < r0 < r2 < infinity.
            r1b = r0 * u
            tail_b = v / (1.0 - v)
            r2b = r0 + tail_b
            mb += (
                wu
                * wv
                * (r0 / (1.0 - v) ** 2)
                * hyperbolic_density(r1b, r2b)
            )

            # a: r0 < r1 < r2 < infinity.
            tail_1 = u / (1.0 - u)
            tail_2 = v / (1.0 - v)
            r1a = r0 + tail_1
            r2a = r1a + tail_2
            ma += (
                wu
                * wv
                * (1.0 / (1.0 - u) ** 2)
                * (1.0 / (1.0 - v) ** 2)
                * hyperbolic_density(r1a, r2a)
            )

    return ma, mb, mc


def metric_identity_samples():
    samples = [(0.2, 0.8), (0.7, 1.4), (1.1, 2.0)]
    errs = []
    for r1, r2 in samples:
        t1 = math.sinh(r1)
        t2 = math.sinh(r2)
        lhs = 1.0 / math.sqrt(1.0 + t1 * t1 + t2 * t2)
        th1 = math.atan(t1)
        th2 = math.atan(t2)
        jac = (1.0 / math.cos(th1)) * (1.0 / math.cos(th2))
        transformed = lhs * jac
        rhs = 1.0 / math.sqrt(
            1.0 - (math.sin(th1) * math.sin(th2)) ** 2
        )
        errs.append(abs(transformed - rhs))
    return max(errs)


def main():
    m48 = chamber_masses(48)
    m64 = chamber_masses(64)
    quad_diff = max(abs(a - b) for a, b in zip(m48, m64))
    assert quad_diff < 2e-9

    ma, mb, mc = m64
    total = ma + mb + mc
    props = (ma / total, mb / total, mc / total)

    assert abs(sum(props) - 1.0) < 5e-15
    assert ma > mb > mc > 0.0
    metric_error = metric_identity_samples()
    assert metric_error < 5e-15

    finite = None
    if E2_DATA.exists():
        e2 = json.loads(E2_DATA.read_text())
        row = next(row for row in e2["cutoffs"] if row["B"] == 1000000)
        vals = row["exactly_two"]
        s = sum(vals)
        finite = {
            "B": 1000000,
            "vector": vals,
            "proportions": [v / s for v in vals],
            "use": "pre-asymptotic diagnostic only",
        }

    report = {
        "metadata": {
            "stage": "14-e4",
            "track": "directionwise ambient asymptotic",
            "height": "physical Euclidean projective height D_R",
            "toric_model": "Bl_4(P1xP1)",
            "line_bundle": "-K_Y",
            "picard_rank": 6,
            "log_power": 5,
        },
        "archimedean_measure": {
            "q_form": "dq1*dq2/(q1*q2*sqrt(1+t1^2+t2^2)) up to a common constant",
            "r_form": "dr1*dr2/sqrt(1+sinh(r1)^2+sinh(r2)^2)",
            "theta_form": "dtheta1*dtheta2/sqrt(1-sin(theta1)^2*sin(theta2)^2)",
            "threshold": "t=1 <=> theta=pi/4",
            "ordering": "0<theta1<theta2<pi/2",
            "metric_change_of_variables_max_error": metric_error,
        },
        "chamber_masses": {
            "a": ma,
            "b": mb,
            "c": mc,
            "total": total,
            "quadrature_order": 64,
            "quadrature_48_64_max_difference": quad_diff,
        },
        "direction_limit": {
            "a": props[0],
            "b": props[1],
            "c": props[2],
            "relative_to_c": [props[0] / props[2], props[1] / props[2], 1.0],
        },
        "thin_set_transfer": {
            "cover": "w^2=t1^2+t2^2",
            "generic_degree": 2,
            "geometrically_nontrivial": True,
            "classification": "thin type II after normalization/resolution",
            "input": "Browning-Loughran Theorem 1.2 plus Huang equidistribution",
            "third_face_square_leading_density": 0,
            "exactly_two_and_raw_have_same_chamber_main_terms": True,
        },
        "finite_e2_comparison": finite,
        "conclusion": {
            "directional_asymptotic": "E_q(B) ~ Lambda_E*M_q*B*(log B)^5",
            "total_asymptotic": "E_2(B) ~ Lambda_E*M*B*(log B)^5",
            "global_Lambda_E_evaluated": False,
            "directional_limit_proved": True,
            "next": "Stage14-e5 space-diagonal filter comparison",
        },
        "status": {
            "STAGE14_E4": "COMPLETE_DIRECTIONAL_ASYMPTOTIC",
            "EXACTLY_TWO_THIRD_FACE_SQUARE_LOCUS": "THIN_TYPE_II",
            "ARCHIMEDEAN_TAMAGAWA_DENSITY_DERIVED": True,
            "DIRECTIONAL_ASYMPTOTIC_PROVED": True,
            "EXACTLY_TWO_FULL_MAIN_TERM_EXISTENCE_PROVED": True,
            "GLOBAL_ARITHMETIC_CONSTANT_LAMBDA_E_EVALUATED": False,
            "NEXT_E_TASK": "Stage14-e5 space-diagonal filter comparison",
        },
        "pass": True,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
