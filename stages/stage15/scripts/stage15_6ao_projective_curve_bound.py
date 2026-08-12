#!/usr/bin/env python3
from __future__ import annotations

import math


def squarefree_kernel(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    out = 1
    p = 2
    while p * p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            out *= p
        p += 1
    if n > 1:
        out *= n
    return out


def f_g(A: int, B: int, a: int, b: int) -> tuple[int, int]:
    return (
        A * (a * a - b * b) - 2 * B * a * b,
        B * (a * a - b * b) + 2 * A * a * b,
    )


def exact_square_split(x: int, y: int) -> dict:
    if x <= 0 or y <= 0 or math.gcd(x, y) != 1:
        raise ValueError("positive primitive coordinate pair required")
    kx = squarefree_kernel(x)
    ky = squarefree_kernel(y)
    c2 = x // kx
    d2 = y // ky
    c = math.isqrt(c2)
    d = math.isqrt(d2)
    if c * c != c2 or d * d != d2:
        raise AssertionError("squarefree split failed")
    return {"kappa_x": kx, "kappa_y": ky, "c": c, "d": d, "kappa": kx * ky}


def find_witnesses(limit: int = 20) -> list[dict]:
    rows: list[dict] = []
    for A in range(1, 6):
        for B in range(0, 5):
            k = A * A + B * B
            for a in range(2, limit + 1):
                for b in range(1, a):
                    if math.gcd(a, b) != 1:
                        continue
                    x, y = f_g(A, B, a, b)
                    if x <= 0 or y <= 0 or math.gcd(x, y) != 1:
                        continue
                    split = exact_square_split(x, y)
                    q1 = x - split["kappa_x"] * split["c"] ** 2
                    q2 = y - split["kappa_y"] * split["d"] ** 2
                    if q1 or q2:
                        raise AssertionError("P3 equations failed")
                    Z = a * a + b * b
                    H = max(a, b, split["c"], split["d"])
                    # H^2 <= sqrt(k)*Z follows from c^2,d^2 <= |K z^2|=sqrt(k)*Z.
                    if H**4 > k * Z * Z:
                        raise AssertionError("height inequality failed")
                    rows.append(
                        {
                            "K": [A, B],
                            "z": [a, b],
                            "k": k,
                            "Z": Z,
                            "kappa": split["kappa"],
                            "P3": [a, b, split["c"], split["d"]],
                        }
                    )
                    if len(rows) >= 6:
                        return rows
    raise AssertionError("not enough witnesses")


if __name__ == "__main__":
    rows = find_witnesses()
    print("STAGE15_6AO_PROJECTIVE_EMBEDDING=PASS")
    print("PROJECTIVE_HEIGHT_BOUND=H^4<=k*Z^2")
    for row in rows:
        print(row)
