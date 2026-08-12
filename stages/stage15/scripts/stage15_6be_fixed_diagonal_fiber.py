from __future__ import annotations

from math import isqrt


def divisor_count(n: int) -> int:
    out = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out *= e + 1
        p += 1 if p == 2 else 2
    if n > 1:
        out *= 2
    return out


def r2_count(n: int) -> int:
    # Number of ordered signed integer pairs (x,y) with x^2+y^2=n.
    total = 0
    lim = isqrt(n)
    for x in range(-lim, lim + 1):
        y2 = n - x * x
        if y2 < 0:
            continue
        y = isqrt(y2)
        if y * y != y2:
            continue
        total += 1 if y == 0 else 2
    return total


def witness() -> dict[str, int | bool]:
    S = 1850
    F1, F2 = 13690, 250
    return {
        "S": S,
        "F1": F1,
        "F2": F2,
        "F_product_matches": F1 * F2 == S * S,
        "tau_S2": divisor_count(S * S),
        "tau_F1": divisor_count(F1),
        "tau_F2": divisor_count(F2),
        "r2_F1": r2_count(F1),
        "r2_F2": r2_count(F2),
        "r2_F1_le_4tau": r2_count(F1) <= 4 * divisor_count(F1),
        "r2_F2_le_4tau": r2_count(F2) <= 4 * divisor_count(F2),
    }


if __name__ == "__main__":
    print(witness())
