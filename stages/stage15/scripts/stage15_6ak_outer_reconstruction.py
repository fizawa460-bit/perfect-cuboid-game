#!/usr/bin/env python3
from __future__ import annotations

import math
from fractions import Fraction

from stage15_6ac_high_low_core import low_core_lift_report


def is_square(n: int) -> bool:
    q = math.isqrt(n)
    return q * q == n


def rational_sqrt(fr: Fraction) -> Fraction | None:
    a = math.isqrt(fr.numerator)
    b = math.isqrt(fr.denominator)
    if a * a == fr.numerator and b * b == fr.denominator:
        return Fraction(a, b)
    return None


def reconstruct_from_primitive_coordinates(x: int, y: int, p: int, q: int) -> dict:
    if min(x, y, p, q) <= 0:
        raise ValueError("positive coordinates required")
    if math.gcd(x, y) != 1 or math.gcd(p, q) != 1:
        raise ValueError("primitive coordinate pairs required")
    if not is_square(x * y * p * q):
        raise ValueError("coordinate product is not a square")

    mn = rational_sqrt(Fraction(x * p, y * q))
    rs = rational_sqrt(Fraction(x * q, y * p))
    if mn is None or rs is None:
        raise AssertionError("product-square condition did not produce rational square ratios")
    m, n = mn.numerator, mn.denominator
    r, s = rs.numerator, rs.denominator

    ha = Fraction(m * r, x)
    hb = Fraction(m * s, p)
    if ha.denominator != 1 or hb.denominator != 1:
        raise AssertionError("normalizer is not integral")
    h_a, h_b = ha.numerator, hb.numerator

    if (m * r, n * s, m * s, n * r) != (h_a * x, h_a * y, h_b * p, h_b * q):
        raise AssertionError("reconstruction identities failed")
    if math.gcd(m * r, n * s) != h_a or math.gcd(m * s, n * r) != h_b:
        raise AssertionError("reconstructed normalizers are not the cross gcds")
    return {
        "m": m,
        "n": n,
        "r": r,
        "s": s,
        "h_alpha": h_a,
        "h_beta": h_b,
    }


def actual_low_core_reverse(m: int, n: int, r: int, s: int) -> dict:
    row = low_core_lift_report(m, n, r, s)
    A, B = row["Pi_alpha"]
    C, D = row["Pi_beta"]
    a, b = row["z"]
    u, v = row["w"]
    x = A * (a * a - b * b) - 2 * B * a * b
    y = B * (a * a - b * b) + 2 * A * a * b
    p = C * (u * u - v * v) - 2 * D * u * v
    q = D * (u * u - v * v) + 2 * C * u * v
    if min(x, y, p, q) <= 0:
        raise AssertionError("physical witness core orientation should have positive reduced coordinates")
    rec = reconstruct_from_primitive_coordinates(x, y, p, q)
    if (rec["m"], rec["n"], rec["r"], rec["s"]) != (m, n, r, s):
        raise AssertionError((row, rec))
    return {
        "params": [m, n, r, s],
        "coordinates": [x, y, p, q],
        "product": x * y * p * q,
        "sqrt_product": math.isqrt(x * y * p * q),
        **rec,
    }


def exhaustive_coordinate_scan(limit: int = 10) -> dict:
    candidates = reconstructed = 0
    for x in range(1, limit + 1):
        for y in range(1, limit + 1):
            if math.gcd(x, y) != 1:
                continue
            for p in range(1, limit + 1):
                for q in range(1, limit + 1):
                    if math.gcd(p, q) != 1:
                        continue
                    if not is_square(x * y * p * q):
                        continue
                    candidates += 1
                    reconstruct_from_primitive_coordinates(x, y, p, q)
                    reconstructed += 1
    return {"product_square_candidates": candidates, "reconstructed": reconstructed}


def witness_report() -> list[dict]:
    return [actual_low_core_reverse(*p) for p in [(5, 3, 7, 4), (31, 7, 31, 23), (11, 1, 29, 22)]]


if __name__ == "__main__":
    print("STAGE15_6AK_OUTER_RECONSTRUCTION=PASS")
    print(exhaustive_coordinate_scan())
    for row in witness_report():
        print(row)
