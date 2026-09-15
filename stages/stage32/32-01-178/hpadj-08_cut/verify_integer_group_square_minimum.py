#!/usr/bin/env python3
from __future__ import annotations

import json


def min_integer_square_sum(total: int, slots: int) -> int:
    if total < 0 or slots <= 0:
        raise ValueError("invalid total/slots")
    q, r = divmod(total, slots)
    return (slots - r) * q * q + r * (q + 1) * (q + 1)


def cauchy_scaled24(a: int, b: int, c: int) -> int:
    return 8 * a * a + 8 * b * b + 6 * c * c


def integer_min_scaled24(a: int, b: int, c: int) -> int:
    return 24 * (
        min_integer_square_sum(a, 3)
        + min_integer_square_sum(b, 3)
        + min_integer_square_sum(c, 4)
    )


def main() -> None:
    strict = 0
    equal = 0
    max_gain = 0
    witness = None
    # FULL178 has d<=192, hence the retained group masses used by the
    # HPADJ07/N358 convolution are bounded by h=d//2<=96.
    for a in range(97):
        for b in range(97):
            for c in range(97):
                old = cauchy_scaled24(a, b, c)
                new = integer_min_scaled24(a, b, c)
                if new < old:
                    raise AssertionError((a, b, c, old, new))
                gain = new - old
                if gain:
                    strict += 1
                    if gain > max_gain:
                        max_gain = gain
                        witness = [a, b, c, old, new]
                else:
                    equal += 1

    # Equality is exactly the divisible case for all three groups.
    for a in range(97):
        for b in range(97):
            for c in range(97):
                eq = integer_min_scaled24(a, b, c) == cauchy_scaled24(a, b, c)
                expected = (a % 3 == 0 and b % 3 == 0 and c % 4 == 0)
                if eq != expected:
                    raise AssertionError((a, b, c, eq, expected))

    print(json.dumps({
        "status": "PASS_HPADJ08_CUT_INTEGER_GROUP_SQUARE_DOMINANCE",
        "domain": "0<=a,b,c<=96",
        "strictly_stronger_group_triples": strict,
        "equal_group_triples": equal,
        "max_scaled24_gain": max_gain,
        "max_gain_witness": witness,
        "population_pruning_credit": False,
        "main_pruning_credit": False,
        "next": "replay existing HPADJ07 population convolution with integer_min_scaled24 threshold",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
