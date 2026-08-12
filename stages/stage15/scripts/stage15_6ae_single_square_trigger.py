#!/usr/bin/env python3
from __future__ import annotations

import math

from stage15_6ac_high_low_core import low_core_lift_report, gmul


def transfer_report(m: int, n: int, r: int, s: int) -> dict:
    row = low_core_lift_report(m, n, r, s)
    h_a = row["h_alpha"]
    h_b = row["h_beta"]
    K_a = tuple(row["Pi_alpha"])
    K_b = tuple(row["Pi_beta"])
    z = tuple(row["z"])
    w = tuple(row["w"])

    alpha = gmul(K_a, gmul(z, z))
    beta = gmul(K_b, gmul(w, w))
    X, Y = alpha

    if m * r != h_a * X or n * s != h_a * Y:
        raise AssertionError("alpha reconstruction failed")
    if m * s != h_b * beta[0] or n * r != h_b * beta[1]:
        raise AssertionError("beta reconstruction failed")

    lhs = (m * n * h_b * beta[0], m * n * h_b * beta[1])
    rhs = (h_a * m * m * Y, h_a * n * n * X)
    if lhs != rhs:
        raise AssertionError("minimal anisotropic transfer failed")

    k = row["k"]
    wnorm = w[0] * w[0] + w[1] * w[1]
    quartic_lhs = m**4 * Y * Y + n**4 * X * X
    # Cleared-denominator norm identity:
    # h_a^2*(m^4 Y^2+n^4 X^2)=(mn h_b)^2*k*|w|^4.
    quartic_left_cleared = h_a * h_a * quartic_lhs
    quartic_right_cleared = (m * n * h_b) ** 2 * k * wnorm * wnorm
    if quartic_left_cleared != quartic_right_cleared:
        raise AssertionError("quartic norm projection failed")

    if math.gcd(abs(z[0]), abs(z[1])) != 1:
        raise AssertionError("remaining Gaussian parameter must be primitive")

    return {
        "params": [m, n, r, s],
        "k": k,
        "q": row["q"],
        "K_alpha": list(K_a),
        "K_beta": list(K_b),
        "z": list(z),
        "w": list(w),
        "X": X,
        "Y": Y,
        "transfer_lhs": list(lhs),
        "transfer_rhs": list(rhs),
        "quartic_left_cleared": quartic_left_cleared,
        "quartic_right_cleared": quartic_right_cleared,
    }


def witness_report() -> list[dict]:
    witnesses = [
        (5, 3, 7, 4),
        (31, 7, 31, 23),
        (11, 1, 29, 22),
    ]
    return [transfer_report(*p) for p in witnesses]


if __name__ == "__main__":
    rows = witness_report()
    print("STAGE15_6AE_SINGLE_SQUARE_TRIGGER=PASS")
    for row in rows:
        print(
            f"LOW={row['params']} q={row['q']} z={row['z']} "
            f"transfer={row['transfer_lhs']}"
        )
