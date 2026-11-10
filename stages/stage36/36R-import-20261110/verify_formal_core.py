#!/usr/bin/env python3
"""Bounded, exact, no-network verification of Stage36 36R formal core.

This is a finite/symbolic desk check, NOT a hostile-audit PASS, mathematical
claim promotion, or current-main integration authorization.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
INVENTORY = ROOT / "stages/stage36/36-02/representative-inventory.json"


def make_mask(bits: str) -> int:
    return sum(1 << i for i, bit in enumerate(bits) if bit == "1")


def subspace(basis: list[int]) -> frozenset[int]:
    space = {0}
    for b in basis:
        space |= {x ^ b for x in tuple(space)}
    return frozenset(space)


def permute_mask(x: int, permutation: tuple[int, ...], lines: list[str]) -> int:
    ans = 0
    for i, label in enumerate(lines):
        if (x >> i) & 1:
            target = (label[0] + str(permutation[int(label[1]) - 1])
                      if label[0] in ("A", "B") else label)
            ans ^= 1 << lines.index(target)
    return ans


def add(a: list[int], b: list[int]) -> list[int]:
    return [((a[i] if i < len(a) else 0) +
             (b[i] if i < len(b) else 0))
            for i in range(max(len(a), len(b)))]


def neg(a: list[int]) -> list[int]:
    return [-x for x in a]


def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def power(a: list[int], n: int) -> list[int]:
    out = [1]
    for _ in range(n):
        out = mul(out, a)
    return out


def main() -> None:
    data = json.loads(INVENTORY.read_text(encoding="utf-8"))
    lines = data["conventions"]["line_order"]
    assert lines == ["A1", "A2", "A3", "B3", "B2", "B1", "C"]
    assert len(data["representatives"]) == 3
    orbits = []
    for rep in data["representatives"].values():
        labels = rep["label_map"]
        assert sorted(int(labels[l], 2) for l in lines) == list(range(1, 8))
        basis = [make_mask(x) for x in rep["kernel_upstairs_basis"]]
        orbit = {
            subspace([permute_mask(b, p, lines) for b in basis])
            for p in itertools.permutations((1, 2, 3))
        }
        assert len(orbit) == rep["q_orbit_size"]
        orbits.append(orbit)

    kernels = set().union(*orbits)
    assert sorted(map(len, orbits)) == [2, 2, 6]
    assert len(kernels) == 10
    V = frozenset(x for x in range(128) if x.bit_count() % 2 == 0)
    B1, B2 = lines.index("B1"), lines.index("B2")
    g = (1 << B1) ^ (1 << B2)
    V_J = frozenset(c for c in V if ((c >> B1) & 1) == ((c >> B2) & 1))
    assert len(V) == 64 and len(V_J) == 32
    for H in kernels:
        assert len(H) == 16 and 127 in H
        assert g not in H
        V_H = frozenset(c for c in V if all((c & h).bit_count() % 2 == 0 for h in H))
        assert len(V_H) == 8
        assert {x ^ y for x in V_H for y in V_J} == set(V)
    print("PASS: 6+2+2 yields 10 distinct admissible H; g not in H; V_H+V_J=V")

    # Symbolic polynomial equality in p. Coefficients in increasing p degree.
    # With y=t^2, u=(p^2-1)/(2p), v=(p^2+1)/(2p),
    # s=4*v^2*y/(1-y)^2, c=(p+1)/(p-1).
    # (s+1)(1-y)^2 = (y+p^2)(y+p^-2).
    # (s+u^2)(1-y)^2 = u^2(y+c^2)(y+c^-2).
    p = [0, 1]
    one = [1]
    two = [2]
    p2 = power(p, 2)
    plus = add(p2, one)
    minus = add(p2, neg(one))
    # Coefficient of y after clearing common denominator p^2 in first identity.
    lhs_first = add(power(plus, 2), neg(mul(two, p2)))
    rhs_first = add(power(p2, 2), one)
    assert lhs_first == rhs_first
    # Coefficient of y after clearing 4p^2 in second identity.
    lhs_second = add(mul([4], power(plus, 2)), neg(mul(two, power(minus, 2))))
    rhs_second = add(power(add(p, one), 4), power(add(p, neg(one)), 4))
    assert lhs_second == rhs_second
    print("PASS: both 36R-04 squareclass identities hold as polynomial identities")

    a, b = 53, 8
    H = a*a + b*b
    P = a*a - b*b
    assert H == 2873 == 17*13*13
    assert P == 2745 == 3*3*5*61
    assert 5185 == 17*5*61
    print("PASS: 36R-05 p=53/8 third-class factor arithmetic only")
    print("HOLD: local solubility of third class at all places NOT reproduced")
    print("HOLD: Br(U_H) and inverse-map boundary completeness NOT checked")
    print("HOLD: independent hostile audit and fresh-session blind pass NOT performed")


if __name__ == "__main__":
    main()
