from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt


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


def fg(A: int, B: int, a: int, b: int) -> tuple[int, int]:
    return (
        A * (a * a - b * b) - 2 * B * a * b,
        B * (a * a - b * b) + 2 * A * a * b,
    )


def hessian_value(A: int, B: int, kappa: int, a: int, b: int) -> int:
    k = A * A + B * B
    z = a * a + b * b
    return 12 * kappa * kappa * k * k * z * z


def twist_parameter(k: int, kappa: int) -> int:
    return squarefree_part(2 * k * kappa)


def covering_point(A: int, B: int, kappa: int, a: int, b: int) -> tuple[Fraction, Fraction]:
    k = A * A + B * B
    f, g = fg(A, B, a, b)
    if f * g <= 0 or (f * g) % kappa:
        raise ValueError("not a positive Stage15 coordinate-core state")
    t2 = f * g // kappa
    t = isqrt(t2)
    if t * t != t2:
        raise ValueError("coordinate-core square condition fails")
    z = a * a + b * b
    s = k * kappa
    d = twist_parameter(k, kappa)
    X = Fraction(d * (f * f + g * g), 2 * f * g)
    if s % 2:
        Y = Fraction(k * k * z * (f * f - g * g), t ** 3)
    else:
        Y = Fraction(k * k * z * (f * f - g * g), 8 * t ** 3)
    if Y * Y != X * X * X - d * d * X:
        raise AssertionError("covering point does not satisfy E_d")
    return X, Y


def witness() -> dict[str, object]:
    # 6aa S-only witness alpha0=117+i = (3+i?) core-square state.
    # K=3+i has norm k=10 and z=6+i has norm 37:
    # (3+i)(6+i)^2 = 117+i.
    A, B, kappa, a, b = 3, 1, 13, 6, 1
    f, g = fg(A, B, a, b)
    X, Y = covering_point(A, B, kappa, a, b)
    return {
        "K": [A, B],
        "k": A * A + B * B,
        "kappa": kappa,
        "z": [a, b],
        "Z": a * a + b * b,
        "f_g": [f, g],
        "twist_d": twist_parameter(A * A + B * B, kappa),
        "X": [X.numerator, X.denominator],
        "Y": [Y.numerator, Y.denominator],
    }


if __name__ == "__main__":
    print(witness())
