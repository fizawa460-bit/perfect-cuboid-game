from __future__ import annotations

from math import isqrt


def squarefree_part(n: int) -> int:
    n = abs(n)
    out = 1
    p = 2
    while p * p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            out *= p
        p += 1 if p == 2 else 2
    if n > 1:
        out *= n
    return out


def quartic_value(kappa_f: int, kappa_g: int, c: int, e: int) -> int:
    return kappa_f * kappa_f * c**4 + kappa_g * kappa_g * e**4


def product_square_report(F1: int, F2: int) -> dict[str, int | bool]:
    prod = F1 * F2
    S = isqrt(prod)
    return {
        "F1": F1,
        "F2": F2,
        "k1": squarefree_part(F1),
        "k2": squarefree_part(F2),
        "product_is_square": S * S == prod,
        "S": S,
    }


def witness() -> dict[str, object]:
    # Stage15-6aa S-only physical witness (m,n,r,s)=(13,1,9,1).
    # alpha=117+i, beta=13+9i, k=10, Z=37, W=5, R=925.
    F1 = quartic_value(13, 1, 3, 1)
    F2 = quartic_value(13, 1, 1, 3)
    rep = product_square_report(F1, F2)
    rep.update({
        "kappa": 13,
        "Z": 37,
        "W": 5,
        "physical_R": 925,
        "gamma": 4,
        "expected_S": 1850,
    })
    return rep


if __name__ == "__main__":
    print(witness())
