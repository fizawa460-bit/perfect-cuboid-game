#!/usr/bin/env python3
from __future__ import annotations

from stage15_6ae_single_square_trigger import transfer_report


def determinant_identity(z1: tuple[int, int], z2: tuple[int, int], K: tuple[int, int], m: int, n: int) -> dict:
    a1, b1 = z1
    a2, b2 = z2
    A, B = K

    def u(z: tuple[int, int]) -> tuple[int, int]:
        a, b = z
        return (A * (a*a-b*b) - 2*B*a*b, B * (a*a-b*b) + 2*A*a*b)

    X1, Y1 = u(z1)
    X2, Y2 = u(z2)
    delta = m*m*n*n*(Y1*X2 - Y2*X1)
    k = A*A + B*B
    lp = a1*a2 + b1*b2
    lm = a1*b2 - b1*a2
    factored = -2*m*m*n*n*k*lp*lm
    if delta != factored:
        raise AssertionError((delta, factored))
    return {"z1": list(z1), "z2": list(z2), "K": list(K), "k": k, "L_plus": lp, "L_minus": lm, "delta": delta}


def witness_report() -> list[dict]:
    # Pure algebra witnesses, plus actual retained z's from 6ae.
    rows = [
        determinant_identity((1, 2), (2, 1), (1, 0), 5, 3),
        determinant_identity((2, 1), (1, 3), (1, 2), 7, 4),
    ]
    actual = [transfer_report(5, 3, 7, 4), transfer_report(31, 7, 31, 23), transfer_report(11, 1, 29, 22)]
    z = [tuple(r["z"]) for r in actual]
    K = tuple(actual[0]["K_alpha"])
    rows.append(determinant_identity(z[0], z[1], K, 5, 3))
    return rows


if __name__ == "__main__":
    rows = witness_report()
    print("STAGE15_6AF_CROSS_RESULTANT=PASS")
    for r in rows:
        print(f"PAIR={r['z1']},{r['z2']} L+={r['L_plus']} L-={r['L_minus']} delta={r['delta']}")
