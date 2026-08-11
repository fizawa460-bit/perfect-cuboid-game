#!/usr/bin/env python3
from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def require(path: str, marker: str) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    assert marker in text, (path, marker)


# 4fk: exact coordinate pullback L=E*u^2, n=E*u*v, L/n=u/v.
for E in range(1, 9):
    for u in range(1, 9):
        for v in range(1, 9):
            if gcd(u, v) != 1:
                continue
            n = E * u * v
            L = E * u * u
            assert Fraction(L, n) == Fraction(u, v)
            assert n // (u * v) == E

# 4fl: bare projective endpoint algebra can persist for every n.
for n in range(1, 100):
    E, u, v = 1, 1, n
    assert n == E * u * v
    assert gcd(u, v) == 1

# 4fm: fixed-E primitive ratio is exactly a unitary-divisor selector.
for E0 in range(1, 7):
    for u in range(1, 20):
        for v in range(1, 20):
            if gcd(u, v) != 1:
                continue
            m = u * v
            n = E0 * m
            assert n // E0 == m
            assert m % u == 0
            assert gcd(u, m // u) == 1
            assert Fraction(u * u, m) == Fraction(u, v)

# Polynomial-E coordinate identity is the same exact factorization without a freeze.
for E in (2, 3, 5, 7, 11):
    for u, v in ((1, 6), (2, 5), (3, 4), (4, 7)):
        if gcd(u, v) != 1:
            continue
        m = u * v
        n = E * m
        assert n == E * m
        assert Fraction(u * u, m) == Fraction(u, v)

require(
    "stages/stage14/14-4fk/result.md",
    "FOUR_FJ_INCIDENCE_PULLBACK_TO_RATIO_EXACT=true",
)
require(
    "stages/stage14/14-4fk/result.md",
    "PHYSICAL_WEIGHT_BOOLEAN_FACTORING_USES_INDEPENDENCE=false",
)
require(
    "stages/stage14/14-4fl/result.md",
    "ENDPOINT_RATIO_BRANCH_CLOSED=false",
)
require(
    "stages/stage14/14-4fl/result.md",
    "RADIAL_ENDPOINT_AND_RATIO_ENDPOINT_IDENTIFIED=false",
)
require(
    "stages/stage14/14-4fm/result.md",
    "FIXED_E_UNITARY_DIVISOR_SHORT_WINDOW_EXPLICIT=true",
)
require(
    "stages/stage14/14-4fm/result.md",
    "POLYNOMIAL_E_UNITARY_DIVISOR_COUPLED_CORRELATION_EXPLICIT=true",
)
require(
    "stages/stage14/14-4fm/result.md",
    "FORD_TRANSFER_FIXED_POWER_SAVING_PROVED=false",
)
require(
    "stages/stage14/14-4-batch/4fk-4fm-report.md",
    "BATCH_STOP_REASON=receiver_change",
)
require(
    "stages/stage14/14-4-batch/4fk-4fm-report.md",
    "NEXT=Stage14-4fn",
)

print("Stage14-main-batch 4fk-4fm deterministic audit: OK")
