#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4bh/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/two_quadric_geometry_summary.json"
FOUR_BG = ROOT / "stages/stage14/14-4bg/result.md"


def require(text: str, needle: str) -> None:
    assert needle in text, f"missing: {needle}"


def projectively_equal(p: tuple[int, int], q: tuple[int, int]) -> bool:
    return p[0] * q[1] == p[1] * q[0]


def count_two_lines(ell: int, r: int, ui: int, uj: int) -> int:
    count = 0
    for x in range(-ui, ui + 1):
        for y in range(-uj, uj + 1):
            if (x - r * y) % ell == 0 or (x + r * y) % ell == 0:
                count += 1
    return count


def main() -> None:
    result = RESULT.read_text()
    summary = json.loads(SUMMARY.read_text())
    four_bg = FOUR_BG.read_text()

    require(four_bg, "INTEGRAL_WITNESS_EQUATION_EXACT=true")
    require(four_bg, "FIXED_STATE_TWO_QUADRIC_DIFFERENCE_SYSTEM_EXACT=true")
    require(four_bg, "CURRENT_SQRT_REMAINING_POST_LOCAL_DELTA=10/21")

    # The local exponent ledger remains unchanged in this geometric stage.
    assert Fraction(41, 42) - Fraction(1, 2) == Fraction(10, 21)

    # Pencil root separation and the exact root-discriminant factor.
    triples = [(3, 4, 5), (5, 12, 13), (7, 24, 25), (20, 21, 29)]
    for S, X, H in triples:
        assert S * S + X * X == H * H
        roots = [(0, 1), (1, 0), (1, 1), (-X * X, S * S)]
        for p, q in combinations(roots, 2):
            assert not projectively_equal(p, q)
        det_product = 1
        for (a, b), (c, d) in combinations(roots, 2):
            det_product *= a * d - b * c
        assert det_product * det_product == S**4 * X**4 * H**4

    # For a square product, a nontrivial parity vector has exactly two active factors.
    even_parity = [bits for bits in product((0, 1), repeat=3) if sum(bits) % 2 == 0]
    assert even_parity == [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
    assert {bits for bits in even_parity if any(bits)} == {
        (1, 1, 0),  # S edge 01
        (1, 0, 1),  # X edge 02
        (0, 1, 1),  # H edge 12
    }

    # Finite regression of the two-line rectangular lattice count.  The constant
    # is deliberately loose; the theorem records only the O(Ui*Uj/ell+min+1) shape.
    for ell in (3, 5, 7, 11, 13):
        for r in range(1, ell):
            for ui in (1, 2, 5, 9, 17):
                for uj in (1, 3, 6, 10, 19):
                    n = count_two_lines(ell, r, ui, uj)
                    rhs = 16 * (ui * uj / ell + min(ui, uj) + 1)
                    assert n <= rhs, (ell, r, ui, uj, n, rhs)

    fixed = summary["fixed_packet"]
    assert fixed["pencil_determinant"] == (
        "d0*d1*d2*lambda*mu*(lambda-mu)*(lambda*S^2+mu*X^2)"
    )
    assert len(fixed["singular_parameters"]) == 4
    assert fixed["positive_dimensional_coordinate_boundary"] is False

    elim = summary["elimination"]
    assert elim["conic"] == "d2*u2^2-d1*u1^2=H^2*D^2"
    assert elim["double_cover_branch_count_geometric"] == 4

    inc = summary["large_prime_incidence"]
    assert inc["residue_geometry"] == "at most two lines"
    assert inc["box_bound"] == "O(Ui*Uj/ell + min(Ui,Uj) + 1)"
    assert inc["sector_saving"] == "B^(-eta)"

    flags = summary["flags"]
    expected_true = [
        "FIXED_PACKET_PENCIL_DETERMINANT_EXACT",
        "FIXED_PACKET_PENCIL_HAS_FOUR_DISTINCT_SINGULAR_PARAMETERS",
        "FIXED_PACKET_CURVE_SMOOTH_GENUS_ONE",
        "ONE_SQUARE_VARIABLE_ELIMINATION_EXACT",
        "CONIC_PLUS_SQUARE_LIFT_EXACT",
        "ODD_KERNEL_EDGE_PACKET_FACTORIZATION_REPROVED",
        "LARGE_KERNEL_EDGE_PRIME_TWO_LINE_CONGRUENCE",
        "DYADIC_LARGE_PRIME_INCIDENCE_BOUND_PROVED",
        "DIRECT_POST_LOCAL_LARGE_KERNEL_SECTOR_SAVING_PROVED",
        "DETERMINANT_METHOD_GEOMETRY_READY",
    ]
    for key in expected_true:
        assert flags[key] is True, key
    assert flags["POSITIVE_DIMENSIONAL_TORSION_OR_COORDINATE_BOUNDARY"] is False
    assert flags["DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED"] is False
    assert flags["SQRT_B_UPPER_BOUND_PROVED"] is False
    assert flags["SQRT_B_ASYMPTOTIC_PROVED"] is False

    require(result, "STAGE14_4BH=TWO_QUADRIC_GENUS_ONE_GEOMETRY_AND_LARGE_KERNEL_INCIDENCE_SPLIT")
    require(result, "FIXED_PACKET_CURVE_SMOOTH_GENUS_ONE=true")
    require(result, "DIRECT_POST_LOCAL_LARGE_KERNEL_SECTOR_SAVING_PROVED=true")
    require(result, "DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false")
    require(result, "NEXT=Stage14-4bi")

    print("STAGE14_4BH_AUDIT=PASS")
    print("pencil_roots=4_distinct")
    print("fixed_packet_geometry=smooth_genus_one")
    print("large_kernel_incidence=at_most_two_lines")
    print("sector_saving=B^(-eta)")
    print("full_delta_post=OPEN")


if __name__ == "__main__":
    main()
