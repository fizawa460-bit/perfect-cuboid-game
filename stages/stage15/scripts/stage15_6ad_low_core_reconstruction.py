#!/usr/bin/env python3
from __future__ import annotations

import math

from stage15_6ac_high_low_core import (
    gdiv_exact,
    gaussian_square_root,
    gmul,
    low_core_lift_report,
)


def gadd(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int]:
    return z[0] + w[0], z[1] + w[1]


def gsub(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int]:
    return z[0] - w[0], z[1] - w[1]


def gscale(c: int, z: tuple[int, int]) -> tuple[int, int]:
    return c * z[0], c * z[1]


def gconj(z: tuple[int, int]) -> tuple[int, int]:
    return z[0], -z[1]


def gsquare(z: tuple[int, int]) -> tuple[int, int]:
    return gmul(z, z)


def reconstruct_from_z(report: dict) -> dict:
    m, n, r_expected, s_expected = map(int, report["params"])
    h_alpha = int(report["h_alpha"])
    h_beta = int(report["h_beta"])
    K_alpha = tuple(map(int, report["Pi_alpha"]))
    K_beta = tuple(map(int, report["Pi_beta"]))
    z = tuple(map(int, report["z"]))
    w_expected = tuple(map(int, report["w"]))

    if math.gcd(abs(z[0]), abs(z[1])) != 1:
        raise AssertionError("remaining Gaussian parameter z is not primitive")

    alpha0 = gmul(K_alpha, gsquare(z))
    X, Y = alpha0
    if (h_alpha * X) % m or (h_alpha * Y) % n:
        raise AssertionError("z does not reconstruct integral physical r,s")
    r = h_alpha * X // m
    s = h_alpha * Y // n
    if (r, s) != (r_expected, s_expected):
        raise AssertionError("z reconstruction disagrees with physical pair")

    if (m * s) % h_beta or (n * r) % h_beta:
        raise AssertionError("reconstructed beta0 is nonintegral")
    beta0 = (m * s // h_beta, n * r // h_beta)
    quotient = gdiv_exact(beta0, K_beta)
    if quotient is None:
        raise AssertionError("fixed z does not reconstruct integral w^2")
    root = gaussian_square_root(quotient)
    if root is None:
        raise AssertionError("fixed z transfer is not a Gaussian square")

    if gsquare(root) != quotient:
        raise AssertionError("Gaussian square root failed")
    if gmul(K_beta, quotient) != beta0:
        raise AssertionError("beta reconstruction failed")

    # Root uniqueness over an integral domain: for nonzero quotient, roots are ±root.
    roots = {root, (-root[0], -root[1])}
    if w_expected not in roots and (-w_expected[0], -w_expected[1]) not in roots:
        # The 6ac core representative may absorb a unit. The quotient is the invariant object.
        if gsquare(w_expected) != quotient:
            raise AssertionError("stored w is inconsistent with reconstructed w^2")

    H_plus = m * m + n * n
    H_minus = m * m - n * n
    rhs_inside = gsub(gscale(H_plus, gconj(alpha0)), gscale(H_minus, alpha0))
    rhs = gscale(h_alpha, gmul((0, 1), rhs_inside))
    lhs = gscale(2 * m * n * h_beta, beta0)
    if lhs != rhs:
        raise AssertionError("anti-linear transfer identity failed")

    denominator = gscale(2 * m * n * h_beta, K_beta)
    transfer_square = gdiv_exact(rhs, denominator)
    if transfer_square != quotient:
        raise AssertionError("direct anti-linear transfer did not recover w^2")

    return {
        "params": [m, n, r, s],
        "K_alpha": list(K_alpha),
        "K_beta": list(K_beta),
        "z": list(z),
        "w_square": list(quotient),
        "w_root_fiber_upper_bound": 2,
        "anti_linear_transfer": list(rhs),
        "z_primitive": True,
    }


def witness_report() -> list[dict]:
    witnesses = [
        (5, 3, 7, 4),
        (31, 7, 31, 23),
        (11, 1, 29, 22),
    ]
    out = []
    for params in witnesses:
        row = low_core_lift_report(*params)
        out.append(reconstruct_from_z(row))
    return out


if __name__ == "__main__":
    print("STAGE15_6AD_RECONSTRUCTION=PASS")
    for row in witness_report():
        print(
            f"WITNESS={row['params']} z={row['z']} "
            f"w2={row['w_square']} fiber<={row['w_root_fiber_upper_bound']}"
        )
