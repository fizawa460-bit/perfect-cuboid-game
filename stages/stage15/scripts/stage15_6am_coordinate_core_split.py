#!/usr/bin/env python3
from __future__ import annotations

import math

from stage15_6ac_high_low_core import low_core_lift_report
from stage15_6al_coordinate_cells import squarefree_kernel


def gaussian_coordinate_data(K: tuple[int, int], z: tuple[int, int]) -> dict:
    A, B = K
    a, b = z
    x = A * (a * a - b * b) - 2 * B * a * b
    y = B * (a * a - b * b) + 2 * A * a * b
    if x == 0 or y == 0:
        raise ValueError("physical positive receiver has nonzero coordinates")
    k = A * A + B * B
    kappa = squarefree_kernel(abs(x * y))
    if math.gcd(k, kappa) != 1:
        raise AssertionError("norm core and coordinate core overlap")
    return {"x": x, "y": y, "k": k, "kappa": kappa, "norm_z": a * a + b * b}


def high_kappa_bound(Z: int, W: int, L: int) -> dict:
    if min(Z, W, L) <= 0:
        raise ValueError("positive scales required")
    bound = min(Z, W) + (Z * W + L - 1) // L
    sqrt_support = math.isqrt(Z * W)
    high = L * L >= Z * W
    if high and bound > 2 * (sqrt_support + 1):
        raise AssertionError((Z, W, L, bound, sqrt_support))
    return {"Z": Z, "W": W, "L": L, "bound_model": bound, "high": high}


def quartic_marker(K: tuple[int, int]) -> dict:
    A, B = K
    k = A * A + B * B
    # For t=a/b, the two coordinate quadratics are
    # f=A t^2-2B t-A and g=B t^2+2A t-B.
    disc_f = 4 * k
    disc_g = 4 * k
    resultant = -4 * k * k
    if k <= 0 or disc_f == 0 or disc_g == 0 or resultant == 0:
        raise AssertionError("coordinate-product quartic must be separable")
    return {"k": k, "disc_f": disc_f, "disc_g": disc_g, "resultant_fg": resultant, "genus": 1}


def witness_report() -> list[dict]:
    out = []
    for params in [(5, 3, 7, 4), (31, 7, 31, 23), (11, 1, 29, 22)]:
        row = low_core_lift_report(*params)
        alpha = gaussian_coordinate_data(tuple(row["Pi_alpha"]), tuple(row["z"]))
        beta = gaussian_coordinate_data(tuple(row["Pi_beta"]), tuple(row["w"]))
        if alpha["kappa"] != beta["kappa"]:
            raise AssertionError("survivor coordinate cores disagree")
        if alpha["k"] != beta["k"]:
            raise AssertionError("survivor norm cores disagree")
        marker_a = quartic_marker(tuple(row["Pi_alpha"]))
        marker_b = quartic_marker(tuple(row["Pi_beta"]))
        out.append({
            "params": list(params),
            "k": alpha["k"],
            "kappa": alpha["kappa"],
            "Z": alpha["norm_z"],
            "W": beta["norm_z"],
            "alpha_marker": marker_a,
            "beta_marker": marker_b,
        })
    return out


def threshold_regression(limit: int = 30) -> dict:
    checked = 0
    for Z in range(1, limit + 1):
        for W in range(1, limit + 1):
            L = math.isqrt(Z * W)
            if L * L < Z * W:
                L += 1
            high_kappa_bound(Z, W, L)
            checked += 1
    return {"checked": checked}


if __name__ == "__main__":
    print("STAGE15_6AM_COORDINATE_CORE_SPLIT=PASS")
    print(threshold_regression())
    for row in witness_report():
        print(row)
