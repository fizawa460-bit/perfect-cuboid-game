#!/usr/bin/env python3
"""Deterministic audit for Stage14-4cj.

The asymptotic proof is the CRT-modulus versus Plucker-minor height argument in
14-4cj/result.md.  This script freezes its algebraic pattern, endpoint exponent
ledger, and finite physical reducedness regression.
"""

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
S7_AUDIT = HERE.parents[1] / "14-s7-20" / "balanced_eight_cell_audit.py"
spec = spec_from_file_location("stage14_s7_20_audit", S7_AUDIT)
assert spec is not None and spec.loader is not None
s7 = module_from_spec(spec)
spec.loader.exec_module(s7)


def minors(a, b):
    p = {}
    for i in range(4):
        for j in range(i + 1, 4):
            p[(i + 1, j + 1)] = a[i] * b[j] - a[j] * b[i]
    return p


def rank_two(a, b):
    return any(v != 0 for v in minors(a, b).values())


def audit_plucker_zero_pattern():
    """Exhaustively verify the linear-algebra consequence of four mixed zeros."""
    values = (-1, 0, 1)
    checked_rank2 = 0
    surviving_patterns = set()
    for a in product(values, repeat=4):
        if a == (0, 0, 0, 0):
            continue
        for b in product(values, repeat=4):
            if b == (0, 0, 0, 0) or not rank_two(a, b):
                continue
            p = minors(a, b)
            if not all(p[k] == 0 for k in ((1, 3), (1, 4), (2, 3), (2, 4))):
                continue
            checked_rank2 += 1
            # Plucker relation reduces to p12*p34=0.
            assert p[(1, 2)] * p[(3, 4)] == 0
            if p[(1, 2)] != 0:
                assert a[2] == b[2] == a[3] == b[3] == 0
                surviving_patterns.add("12")
            elif p[(3, 4)] != 0:
                assert a[0] == b[0] == a[1] == b[1] == 0
                surviving_patterns.add("34")
            else:
                raise AssertionError("rank two with all Plucker minors zero")
    assert checked_rank2 > 0
    assert surviving_patterns == {"12", "34"}
    return checked_rank2


def make_groups(X):
    groups = {}
    for Q in range(2, X + 1):
        for P in range(1, Q):
            if gcd(P, Q) != 1:
                continue
            st = s7.make_state(P, Q)
            groups.setdefault((st["xi"], st["k"]), []).append(st)
    return groups


def audit_physical_primitivity(X=420):
    groups = make_groups(X)
    checked = 0
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                # These are the physical root coordinates used by Lambda_xi.
                root = (a["x"], a["y"], b["x"], b["y"])
                assert gcd(a["x"], a["y"]) == 1
                assert gcd(b["x"], b["y"]) == 1
                g = 0
                for z in root:
                    g = gcd(g, z)
                assert g == 1
                assert all(z > 0 for z in root)
                checked += 1
    assert checked > 0
    return checked


def main():
    pattern_count = audit_plucker_zero_pattern()
    physical_pairs = audit_physical_primitivity()

    root_exp = Fraction(1, 16)
    minor_exp = 2 * root_exp
    min_cell_exp = Fraction(1, 8)
    min_cell_square_exp = 2 * min_cell_exp
    gap = min_cell_square_exp - minor_exp
    assert minor_exp == Fraction(1, 8)
    assert min_cell_square_exp == Fraction(1, 4)
    assert gap == Fraction(1, 8)

    residual_support = Fraction(5, 8)
    raw_root_direction_box = 4 * root_exp
    assert raw_root_direction_box == Fraction(1, 4)
    assert residual_support + raw_root_direction_box == Fraction(7, 8)

    print("Stage14-4cj audit: PASS")
    print(f"rank-two mixed-zero toy matrices checked: {pattern_count}")
    print(f"finite physical dual-cross pairs checked: {physical_pairs}")
    print("mixed Plucker minor exponent ceiling: 1/8")
    print("balanced cell-square exponent floor: 1/4")
    print("modulus/height contradiction gap: 1/8")
    print("physical root vectors primitive: yes")
    print("residual support + raw root-direction box: 5/8 + 1/4 = 7/8")


if __name__ == "__main__":
    main()
