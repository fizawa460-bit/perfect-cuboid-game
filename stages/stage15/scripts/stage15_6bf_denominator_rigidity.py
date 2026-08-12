from __future__ import annotations

from fractions import Fraction
from math import gcd


def lambda_factor(k: int, kappa: int) -> int:
    return 1 if (k * kappa) % 2 else 2


def reduced_U(k: int, kappa: int, Z: int, c: int, e: int) -> Fraction:
    return Fraction(k * Z, lambda_factor(k, kappa) * c * e)


def expected_denominator(kappa: int, c: int, e: int) -> int:
    return (2 if kappa % 2 == 0 else 1) * c * e


def odd_denominator_coprime(k: int, Z: int, c: int, e: int) -> bool:
    q = c * e
    while q % 2 == 0:
        q //= 2
    return gcd(q, k * Z) == 1


def witness() -> dict[str, object]:
    # Physical 6aa S-only alpha-state: f=117=13*3^2, g=1.
    U1 = reduced_U(k=10, kappa=13, Z=37, c=3, e=1)
    # Small exact even-kappa state: f=2, g=1, F=5=k*1^2.
    U2 = reduced_U(k=5, kappa=2, Z=1, c=1, e=1)
    return {
        "odd_kappa_state": {
            "U": [U1.numerator, U1.denominator],
            "expected_denominator": expected_denominator(13, 3, 1),
            "odd_denominator_coprime": odd_denominator_coprime(10, 37, 3, 1),
        },
        "even_kappa_state": {
            "U": [U2.numerator, U2.denominator],
            "expected_denominator": expected_denominator(2, 1, 1),
            "odd_denominator_coprime": odd_denominator_coprime(5, 1, 1, 1),
        },
    }


if __name__ == "__main__":
    print(witness())
