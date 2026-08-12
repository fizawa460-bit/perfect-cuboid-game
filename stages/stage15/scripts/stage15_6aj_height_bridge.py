#!/usr/bin/env python3
from __future__ import annotations

import math

from stage15_4_normal_form import normal_form, toric_raw
from stage15_6ac_high_low_core import low_core_lift_report


def cross_gcds(m: int, n: int, r: int, s: int) -> tuple[int, int]:
    return math.gcd(m * r, n * s), math.gcd(m * s, n * r)


def gcd_factor_report(m: int, n: int, r: int, s: int) -> dict:
    if math.gcd(m, n) != 1 or math.gcd(r, s) != 1:
        raise ValueError("primitive toric pairs required")
    raw = toric_raw(m, n, r, s)
    G = math.gcd(math.gcd(raw[0], raw[1]), raw[2])
    h_a, h_b = cross_gcds(m, n, r, s)
    gamma = G // (h_a * h_b)
    expected = 4 if (m % 2 == n % 2 == r % 2 == s % 2 == 1) else 2
    if G != gamma * h_a * h_b or gamma != expected:
        raise AssertionError((m, n, r, s, G, h_a, h_b, gamma, expected))
    return {"G": G, "h_alpha": h_a, "h_beta": h_b, "gamma": gamma}


def low_core_height_report(m: int, n: int, r: int, s: int) -> dict:
    row = low_core_lift_report(m, n, r, s)
    nf = normal_form(m, n, r, s)
    gf = gcd_factor_report(m, n, r, s)
    a, b = row["z"]
    u, v = row["w"]
    Z = a * a + b * b
    W = u * u + v * v
    k = int(row["k"])
    gamma = gf["gamma"]
    lhs = int(nf["physical_d"])
    num = 2 * k * Z * W
    if num % gamma:
        raise AssertionError("height numerator not divisible by parity factor")
    rhs = num // gamma
    if lhs != rhs:
        raise AssertionError((m, n, r, s, lhs, rhs, k, Z, W, gamma))
    return {
        "params": [m, n, r, s],
        "R": lhs,
        "k": k,
        "Z": Z,
        "W": W,
        "gamma": gamma,
        "kZW": k * Z * W,
        "projective_height": max(abs(a), abs(b), abs(u), abs(v)),
    }


def exhaustive_gcd_scan(limit: int = 24) -> dict:
    checked = gamma2 = gamma4 = 0
    for m in range(2, limit + 1):
        for n in range(1, m):
            if math.gcd(m, n) != 1:
                continue
            for r in range(2, limit + 1):
                for s in range(1, r):
                    if math.gcd(r, s) != 1:
                        continue
                    row = gcd_factor_report(m, n, r, s)
                    checked += 1
                    if row["gamma"] == 2:
                        gamma2 += 1
                    else:
                        gamma4 += 1
    return {"checked": checked, "gamma2": gamma2, "gamma4": gamma4}


def witness_report() -> list[dict]:
    params_list = [(5, 3, 7, 4), (31, 7, 31, 23), (11, 1, 29, 22)]
    rows = [low_core_height_report(*p) for p in params_list]
    for row in rows:
        if row["kZW"] > 2 * row["R"]:
            raise AssertionError("exact product cutoff failed")
        if row["projective_height"] ** 2 > row["kZW"] // row["k"] + 1:
            raise AssertionError("projective height sanity failed")
    return rows


if __name__ == "__main__":
    scan = exhaustive_gcd_scan()
    print("STAGE15_6AJ_HEIGHT_BRIDGE=PASS")
    print(scan)
    for row in witness_report():
        print(row)
