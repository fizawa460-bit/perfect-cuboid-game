#!/usr/bin/env python3
from __future__ import annotations

import math

from stage15_6ak_outer_reconstruction import actual_low_core_reverse, is_square


def squarefree_kernel(n: int) -> int:
    if n <= 0:
        raise ValueError("positive integer expected")
    out = 1
    p = 2
    while p * p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            out *= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out *= n
    return out


def square_root_after_kernel(n: int, kernel: int) -> int:
    q = n // kernel
    r = math.isqrt(q)
    if kernel * r * r != n:
        raise AssertionError((n, kernel))
    return r


def cell_decomposition(x: int, y: int, p: int, q: int) -> dict:
    if min(x, y, p, q) <= 0:
        raise ValueError("positive coordinates required")
    if math.gcd(x, y) != 1 or math.gcd(p, q) != 1:
        raise ValueError("primitive coordinate pairs required")
    if not is_square(x * y * p * q):
        raise ValueError("product-square condition required")

    sx, sy, sp, sq = map(squarefree_kernel, (x, y, p, q))
    k_xp = math.gcd(sx, sp)
    k_xq = math.gcd(sx, sq)
    k_yp = math.gcd(sy, sp)
    k_yq = math.gcd(sy, sq)
    cells = (k_xp, k_xq, k_yp, k_yq)
    for i, a in enumerate(cells):
        for b in cells[i + 1 :]:
            if math.gcd(a, b) != 1:
                raise AssertionError("squareclass cells are not pairwise coprime")

    kappa = math.prod(cells)
    if sx != k_xp * k_xq or sy != k_yp * k_yq:
        raise AssertionError("alpha squareclass partition failed")
    if sp != k_xp * k_yp or sq != k_xq * k_yq:
        raise AssertionError("beta squareclass partition failed")
    if squarefree_kernel(x * y) != kappa or squarefree_kernel(p * q) != kappa:
        raise AssertionError("common coordinate-product kernel failed")

    X = square_root_after_kernel(x, sx)
    Y = square_root_after_kernel(y, sy)
    P = square_root_after_kernel(p, sp)
    Q = square_root_after_kernel(q, sq)
    if x != k_xp * k_xq * X * X:
        raise AssertionError("x reconstruction failed")
    if y != k_yp * k_yq * Y * Y:
        raise AssertionError("y reconstruction failed")
    if p != k_xp * k_yp * P * P:
        raise AssertionError("p reconstruction failed")
    if q != k_xq * k_yq * Q * Q:
        raise AssertionError("q reconstruction failed")

    return {
        "kappa": kappa,
        "kappa_xp": k_xp,
        "kappa_xq": k_xq,
        "kappa_yp": k_yp,
        "kappa_yq": k_yq,
        "agree": k_xp * k_yq,
        "switch": k_xq * k_yp,
        "square_parts": [X, Y, P, Q],
    }


def actual_witness_report() -> list[dict]:
    rows = []
    for params in [(5, 3, 7, 4), (31, 7, 31, 23), (11, 1, 29, 22)]:
        rev = actual_low_core_reverse(*params)
        x, y, p, q = rev["coordinates"]
        cells = cell_decomposition(x, y, p, q)
        from stage15_6ac_high_low_core import low_core_lift_report
        lift = low_core_lift_report(*params)
        k = int(lift["k"])
        if math.gcd(k, cells["kappa"]) != 1:
            raise AssertionError("norm core and coordinate-product core must be coprime")
        rows.append({"params": list(params), "k": k, "coordinates": [x, y, p, q], **cells})
    return rows


def exhaustive_cell_scan(limit: int = 9) -> dict:
    checked = nontrivial = 0
    for x in range(1, limit + 1):
        for y in range(1, limit + 1):
            if math.gcd(x, y) != 1:
                continue
            for p in range(1, limit + 1):
                for q in range(1, limit + 1):
                    if math.gcd(p, q) != 1 or not is_square(x * y * p * q):
                        continue
                    row = cell_decomposition(x, y, p, q)
                    checked += 1
                    nontrivial += row["kappa"] > 1
    return {"checked": checked, "nontrivial_kappa": nontrivial}


if __name__ == "__main__":
    print("STAGE15_6AL_COORDINATE_CELLS=PASS")
    print(exhaustive_cell_scan())
    for row in actual_witness_report():
        print(row)
