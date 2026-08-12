#!/usr/bin/env python3
from __future__ import annotations

import math
from fractions import Fraction

from stage15_6ac_high_low_core import low_core_lift_report


def projective_classification(m: int, n: int) -> dict:
    if not (m > n > 0) or math.gcd(m, n) != 1:
        raise ValueError("primitive physical outer pair m>n>0 required")
    s = m * m + n * n
    d = m * m - n * n
    marker = d * d * s * s * (s * s - d * d) ** 2
    if d <= 0 or s <= 0 or s * s == d * d or marker == 0:
        raise AssertionError("physical pencil must be nondegenerate")
    rho = Fraction(d * d, s * s)
    roots = ["[0:1]", "[1:0]", f"[-{s}:{d}]", f"[-{d}:{s}]"]
    return {
        "m": m,
        "n": n,
        "s": s,
        "d": d,
        "s2_minus_d2": s * s - d * d,
        "discriminant_marker": marker,
        "pencil_roots": roots,
        "cross_ratio_num": rho.numerator,
        "cross_ratio_den": rho.denominator,
        "smooth": True,
        "geometric_genus": 1,
        "degree": 4,
        "singular_conic_branch": False,
    }


def eval_exact_quadrics(row: dict) -> tuple[int, int]:
    m, n, _r, _s = row["params"]
    h_a = row["h_alpha"]
    h_b = row["h_beta"]
    A, B = row["Pi_alpha"]
    C, D = row["Pi_beta"]
    a, b = row["z"]
    u, v = row["w"]

    X = A * (a * a - b * b) - 2 * B * a * b
    Y = B * (a * a - b * b) + 2 * A * a * b
    M = m * n * h_b

    q1 = M * (C * (u * u - v * v) - 2 * D * u * v) - h_a * m * m * Y
    q2 = M * (D * (u * u - v * v) + 2 * C * u * v) - h_a * n * n * X
    return q1, q2


def witness_report() -> list[dict]:
    params_list = [
        (5, 3, 7, 4),
        (31, 7, 31, 23),
        (11, 1, 29, 22),
    ]
    out: list[dict] = []
    for params in params_list:
        row = low_core_lift_report(*params)
        q1, q2 = eval_exact_quadrics(row)
        if (q1, q2) != (0, 0):
            raise AssertionError(f"exact projective quadrics failed for {params}: {(q1, q2)}")
        cls = projective_classification(params[0], params[1])
        out.append(
            {
                "params": list(params),
                "z": row["z"],
                "w": row["w"],
                "q1": q1,
                "q2": q2,
                "s": cls["s"],
                "d": cls["d"],
                "cross_ratio": [cls["cross_ratio_num"], cls["cross_ratio_den"]],
                "discriminant_marker": cls["discriminant_marker"],
            }
        )
    if len({tuple(r["cross_ratio"]) for r in out}) < 2:
        raise AssertionError("outer geometry should move across witness outer pairs")
    return out


def scan_outer_pairs(limit: int = 40) -> dict:
    checked = 0
    min_marker = None
    cross_ratios: set[tuple[int, int]] = set()
    for m in range(2, limit + 1):
        for n in range(1, m):
            if math.gcd(m, n) != 1:
                continue
            row = projective_classification(m, n)
            checked += 1
            marker = row["discriminant_marker"]
            min_marker = marker if min_marker is None else min(min_marker, marker)
            cross_ratios.add((row["cross_ratio_num"], row["cross_ratio_den"]))
    if checked == 0 or min_marker is None or min_marker <= 0:
        raise AssertionError("outer-pair smoothness scan failed")
    return {
        "checked": checked,
        "min_discriminant_marker": min_marker,
        "distinct_cross_ratios": len(cross_ratios),
    }


if __name__ == "__main__":
    scan = scan_outer_pairs()
    rows = witness_report()
    print("STAGE15_6AI_GENUS_ONE_MODEL=PASS")
    print(f"OUTER_PAIRS_CHECKED={scan['checked']}")
    print(f"DISTINCT_CROSS_RATIOS={scan['distinct_cross_ratios']}")
    for row in rows:
        print(
            f"WITNESS={row['params']} z={row['z']} w={row['w']} "
            f"rho={row['cross_ratio'][0]}/{row['cross_ratio'][1]}"
        )
