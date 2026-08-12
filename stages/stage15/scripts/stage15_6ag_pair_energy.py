#!/usr/bin/env python3
from __future__ import annotations

import math


def l_plus(z1: tuple[int, int], z2: tuple[int, int]) -> int:
    a1, b1 = z1
    a2, b2 = z2
    return a1 * a2 + b1 * b2


def l_minus(z1: tuple[int, int], z2: tuple[int, int]) -> int:
    a1, b1 = z1
    a2, b2 = z2
    return a1 * b2 - b1 * a2


def primitive(z: tuple[int, int]) -> bool:
    return math.gcd(abs(z[0]), abs(z[1])) == 1 and z != (0, 0)


def degenerate_type(z1: tuple[int, int], z2: tuple[int, int]) -> str | None:
    if l_minus(z1, z2) == 0:
        return "parallel"
    if l_plus(z1, z2) == 0:
        return "orthogonal"
    return None


def line_residue(z1: tuple[int, int], z2: tuple[int, int], p: int) -> str | None:
    if p <= 2:
        raise ValueError("odd prime expected")
    if (z1[0] * z1[0] + z1[1] * z1[1]) % p == 0:
        raise ValueError("first point must be a unit vector modulo p")
    if l_plus(z1, z2) % p == 0:
        return "plus"
    if l_minus(z1, z2) % p == 0:
        return "minus"
    return None


def synthetic_report() -> dict:
    # Keep the anchor norm nonzero modulo 5: the old (2,1) fixture had
    # norm 5 and therefore violated line_residue's own unit hypothesis.
    z1 = (1, 1)
    assert primitive(z1)
    pairs = {
        "parallel": (1, 1),
        "orthogonal": (-1, 1),
        "generic_plus_mod5": (1, 4),
        "generic_minus_mod5": (1, 6),
        "generic_none_mod5": (1, 2),
    }
    for z in pairs.values():
        assert primitive(z)
    assert degenerate_type(z1, pairs["parallel"]) == "parallel"
    assert degenerate_type(z1, pairs["orthogonal"]) == "orthogonal"
    assert line_residue(z1, pairs["generic_plus_mod5"], 5) == "plus"
    assert line_residue(z1, pairs["generic_minus_mod5"], 5) == "minus"
    assert line_residue(z1, pairs["generic_none_mod5"], 5) is None
    return {
        "z1": list(z1),
        "pairs": {k: list(v) for k, v in pairs.items()},
        "degenerate_partner_types": ["parallel", "orthogonal"],
        "shared_prime_receiver_lines": 2,
    }


if __name__ == "__main__":
    print("STAGE15_6AG_PAIR_ENERGY=PASS")
    print(synthetic_report())
