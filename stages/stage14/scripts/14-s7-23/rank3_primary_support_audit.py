#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s7-23.

This audit checks the new exact primary-support lemma for the s7-22 dual CRT
normal and the endpoint exponent contradiction.  It is a regression/falsifier,
not a proof by finite search.
"""

from fractions import Fraction
from functools import reduce
from itertools import combinations, product as cartesian_product
from math import gcd, prod


ROWS = {
    "R": lambda lam: (0, 1, 0, -lam),
    "J": lambda lam: (1, 0, -lam, 0),
    "S": lambda lam: (0, -lam, 1, 0),
    "T": lambda lam: (-lam, 0, 0, 1),
}

ZERO_CELLS = {
    0: ("R", "S"),
    1: ("J", "T"),
    2: ("R", "T"),
    3: ("J", "S"),
}


def gcd_many(values):
    return reduce(gcd, values)


def centered(n: int, modulus: int) -> int:
    n %= modulus
    if n > modulus // 2:
        n -= modulus
    return n


def synthetic_primary_projection_audit() -> None:
    """Build many direct-product dual characters and test zero support."""

    order_sets = [
        {"R": 3, "J": 5, "S": 7, "T": 11},
        {"R": 5, "J": 7, "S": 11, "T": 13},
        {"R": 7, "J": 11, "S": 13, "T": 17},
    ]

    checked = 0
    for orders in order_sets:
        d_h = prod(orders.values())
        for lambdas in [
            {"R": 2, "J": 2, "S": 3, "T": 4},
            {"R": 1, "J": 3, "S": 5, "T": 2},
            {"R": 2, "J": 4, "S": 6, "T": 3},
        ]:
            # keep every lambda a unit for its component order
            if any(gcd(lambdas[c], orders[c]) != 1 for c in orders):
                continue

            rows = {c: ROWS[c](lambdas[c]) for c in orders}
            coeff_choices = []
            for c in ("R", "J", "S", "T"):
                units = [a for a in range(1, min(orders[c], 5)) if gcd(a, orders[c]) == 1]
                coeff_choices.append(units[:2])

            for coeff_tuple in cartesian_product(*coeff_choices):
                coeff = dict(zip(("R", "J", "S", "T"), coeff_tuple))
                nums = []
                for j in range(4):
                    value = sum(
                        Fraction(coeff[c] * rows[c][j], orders[c])
                        for c in ("R", "J", "S", "T")
                    )
                    n = value * d_h
                    assert n.denominator == 1
                    nums.append(centered(n.numerator, d_h))

                # Exact character order must be the product because every
                # component coefficient is a unit and component orders are coprime.
                assert gcd_many([d_h] + [abs(x) for x in nums]) == 1

                # Sparse-row primary projection: each component order divides
                # the coordinates where its row is zero.
                for c in ("R", "J", "S", "T"):
                    for j, entry in enumerate(rows[c]):
                        if entry == 0:
                            assert nums[j] % orders[c] == 0

                # Product form used in the theorem.
                assert nums[0] % (orders["R"] * orders["S"]) == 0
                assert nums[1] % (orders["J"] * orders["T"]) == 0
                assert nums[2] % (orders["R"] * orders["T"]) == 0
                assert nums[3] % (orders["J"] * orders["S"]) == 0
                checked += 1

    assert checked > 0
    print(f"synthetic direct-product dual characters checked: {checked}")


def exponent_contradiction_audit() -> None:
    unit = Fraction(1, 16)
    d_min = unit
    d_max = 8 * unit
    d_h_min = 21 * unit
    c_coord_max = 3 * unit
    c_pair_max = 2 * c_coord_max

    assert d_min == Fraction(1, 16)
    assert d_max == Fraction(1, 2)
    assert d_h_min == Fraction(21, 16)
    assert c_pair_max == Fraction(3, 8)

    # Exhaust every 1/16-grid component exponent in the licensed endpoint
    # window.  This independently checks the six pair minima.
    minima = {}
    for i, j in combinations(range(4), 2):
        best = None
        for r, jj, s, t in cartesian_product(range(1, 9), repeat=4):
            e = {
                "R": r * unit,
                "J": jj * unit,
                "S": s * unit,
                "T": t * unit,
            }
            if sum(e.values()) < d_h_min:
                continue
            forced = sum(e[c] for c in ZERO_CELLS[i]) + sum(e[c] for c in ZERO_CELLS[j])
            if best is None or forced < best:
                best = forced
        assert best is not None
        minima[(i + 1, j + 1)] = best

    assert minima[(1, 2)] == Fraction(21, 16)
    assert minima[(3, 4)] == Fraction(21, 16)
    for pair in [(1, 3), (1, 4), (2, 3), (2, 4)]:
        assert minima[pair] == Fraction(14, 16)

    assert min(minima.values()) == Fraction(7, 8)
    assert min(minima.values()) - c_pair_max == Fraction(1, 2)
    assert all(v > c_pair_max for v in minima.values())

    print("normal pair exponent ceiling: 3/8")
    print("minimum forced divisor exponent for any nonzero coordinate pair: 7/8")
    print("uniform contradiction margin: 1/2")


def positivity_support_audit() -> None:
    # If a primitive normal has <=1 nonzero coordinate, it cannot annihilate
    # a vector with all positive coordinates.
    positive_vectors = [
        (1, 1, 1, 1),
        (1, 2, 3, 4),
        (4, 3, 2, 1),
    ]
    normals = []
    for j in range(4):
        for a in (-3, -1, 1, 3):
            c = [0, 0, 0, 0]
            c[j] = a
            normals.append(tuple(c))
    for c in normals:
        for x in positive_vectors:
            assert sum(a * b for a, b in zip(c, x)) != 0
    print("positive physical vector excludes one-coordinate normals")


def quantitative_ledger_audit() -> None:
    residual_support = Fraction(5, 8)
    current = Fraction(7, 8)
    required_average_cell = current - residual_support
    assert required_average_cell == Fraction(1, 4)
    print("4ch residual support exponent: 5/8")
    print("remaining average low-rank cell multiplicity threshold: 1/4")


def main() -> None:
    synthetic_primary_projection_audit()
    exponent_contradiction_audit()
    positivity_support_audit()
    quantitative_ledger_audit()
    print("Stage14-s7-23 audit: PASS")


if __name__ == "__main__":
    main()
