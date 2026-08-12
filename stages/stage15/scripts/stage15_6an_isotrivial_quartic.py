#!/usr/bin/env python3
from __future__ import annotations


def gaussian_mul(z1: tuple[int, int], z2: tuple[int, int]) -> tuple[int, int]:
    a, b = z1
    c, d = z2
    return a * c - b * d, a * d + b * c


def gaussian_pow(z: tuple[int, int], n: int) -> tuple[int, int]:
    out = (1, 0)
    for _ in range(n):
        out = gaussian_mul(out, z)
    return out


def gaussian_sub(z1: tuple[int, int], z2: tuple[int, int]) -> tuple[int, int]:
    return z1[0] - z2[0], z1[1] - z2[1]


def quartic_coeffs(A: int, B: int) -> tuple[int, int, int, int, int]:
    return (
        A * B,
        2 * (A * A - B * B),
        -6 * A * B,
        -2 * (A * A - B * B),
        A * B,
    )


def quartic_invariants(A: int, B: int) -> tuple[int, int]:
    aa, bb, cc, dd, ee = quartic_coeffs(A, B)
    I = 12 * aa * ee - 3 * bb * dd + cc * cc
    J = (
        72 * aa * cc * ee
        + 9 * bb * cc * dd
        - 27 * aa * dd * dd
        - 27 * bb * bb * ee
        - 2 * cc * cc * cc
    )
    return I, J


def f_g(A: int, B: int, a: int, b: int) -> tuple[int, int]:
    f = A * (a * a - b * b) - 2 * B * a * b
    g = B * (a * a - b * b) + 2 * A * a * b
    return f, g


def verify_complex_identity(A: int, B: int, a: int, b: int) -> bool:
    f, g = f_g(A, B, a, b)
    K2 = gaussian_pow((A, B), 2)
    Kb2 = gaussian_pow((A, -B), 2)
    p4 = gaussian_pow((a, b), 4)
    q4 = gaussian_pow((a, -b), 4)
    rhs = gaussian_sub(gaussian_mul(K2, p4), gaussian_mul(Kb2, q4))
    lhs = (0, 4 * f * g)
    return lhs == rhs


def audit_examples() -> list[dict]:
    examples = [(1, 0, 2, 1), (1, 2, 3, 1), (2, 3, 4, 1), (4, 1, 5, 2)]
    rows = []
    for A, B, a, b in examples:
        k = A * A + B * B
        I, J = quartic_invariants(A, B)
        if I != 12 * k * k or J != 0:
            raise AssertionError((A, B, I, J, k))
        if not verify_complex_identity(A, B, a, b):
            raise AssertionError((A, B, a, b))
        rows.append({"K": [A, B], "z": [a, b], "k": k, "I": I, "J": J})
    return rows


if __name__ == "__main__":
    rows = audit_examples()
    print("STAGE15_6AN_ISOTRIVIAL_QUARTIC=PASS")
    print("UNIVERSAL_GEOMETRIC_MODEL=Y^2=P^4-Q^4")
    print("GEOMETRIC_J=1728")
    for row in rows:
        print(row)
