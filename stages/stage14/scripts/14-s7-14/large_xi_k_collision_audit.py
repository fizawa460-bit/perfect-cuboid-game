#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def require_text(path: Path, needles: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


def squarefree_kernel(n: int) -> int:
    assert n >= 1
    out = 1
    p = 2
    x = n
    while p * p <= x:
        e = 0
        while x % p == 0:
            x //= p
            e ^= 1
        if e:
            out *= p
        p += 1 if p == 2 else 2
    if x > 1:
        out *= x
    return out


def is_squarefree(n: int) -> bool:
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


def omega(n: int) -> int:
    out = 0
    p = 2
    x = n
    while p * p <= x:
        if x % p == 0:
            out += 1
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        out += 1
    return out


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def audit_predecessors() -> None:
    require_text(
        ROOT / "stages/stage14/14-s7-13/result.md",
        [
            "STAGE14_S7_13=COMPLETE_FULL_COORDINATE_CANONICAL_REFINEMENT_AND_7_8_BOUND",
            "CRITICAL_SHARED_LABEL_EXPONENT=3/4",
            "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8",
            "FIXED_COORDINATE_AND_TWO_CELL_SAVINGS_MULTIPLIED=false",
        ],
    )
    require_text(
        ROOT / "stages/stage14/14-s7-10/result.md",
        [
            "ADJACENT_TWO_CELL_MIXED_FOURIER_OP_BOUND_PROVED=true",
            "TWO_CELL_RECTANGLE_EXPONENT=2/3",
        ],
    )


def audit_fixed_xi_partition_count() -> None:
    checked = 0
    for xi in range(1, 600):
        if not is_squarefree(xi):
            continue
        pairs = []
        for a in divisors(xi):
            b = xi // a
            if gcd(a, b) == 1 and is_squarefree(a) and is_squarefree(b):
                pairs.append((a, b))
        assert len(pairs) == 2 ** omega(xi), (xi, len(pairs), omega(xi))
        checked += 1
    assert checked > 200


def audit_xi_k_coprimality() -> None:
    checks = 0
    for Q in range(2, 180):
        for P in range(1, Q):
            if gcd(P, Q) != 1:
                continue
            xi = squarefree_kernel(P * Q)
            k = squarefree_kernel(Q * Q - P * P)
            assert squarefree_kernel(P) * squarefree_kernel(Q) == xi
            assert gcd(xi, k) == 1, (P, Q, xi, k)
            assert gcd(Q * Q - P * P, P * Q) == 1
            checks += 1
    assert checks > 5000


def audit_xi_shell_minimax() -> None:
    gamma = Fraction(3, 4)
    support = (1 + gamma) / 2
    two_cell = 1 - gamma / 6
    assert support == Fraction(7, 8)
    assert two_cell == Fraction(7, 8)

    # Exact crossing.
    # (1+g)/2 = 1-g/6  => 4g=3.
    assert 4 * gamma == 3

    # Fine rational grid verifies that min of the increasing/decreasing
    # branches never exceeds 7/8.
    grid_max = Fraction(0)
    argmax = None
    for i in range(0, 1201):
        g = Fraction(i, 1200)
        val = min((1 + g) / 2, 1 - g / 6)
        if val > grid_max:
            grid_max = val
            argmax = g
        assert val <= Fraction(7, 8)
    assert grid_max == Fraction(7, 8)
    assert argmax == Fraction(3, 4)

    # Critical internal squarepart-product exponent.
    assert (1 - gamma) / 2 == Fraction(1, 8)


def audit_critical_cell_pattern() -> None:
    r = Fraction(1, 4)
    s = Fraction(1, 8)
    t = Fraction(1, 8)
    j = Fraction(1, 4)
    gamma = r + s + t + j
    assert gamma == Fraction(3, 4)

    a = r + s
    b = t + j
    c = r + t
    d = s + j
    assert a == b == c == d == Fraction(3, 8)

    max_cell = max(r, s, t, j)
    max_adjacent = max(a, b, c, d)
    one_cell_global = 1 - max_cell / 2
    two_cell_global = 1 - max_adjacent / 3
    assert one_cell_global == Fraction(7, 8)
    assert two_cell_global == Fraction(7, 8)

    # Match the s7-13 equality squarepart roots.
    p = q = Fraction(1, 2)
    xroot = (p - a) / 2
    yroot = (q - b) / 2
    assert xroot == yroot == Fraction(1, 16)


def audit_critical_twist_range() -> None:
    xi_exp = Fraction(3, 4)
    k_exp_max = Fraction(1)
    n_exp_max = xi_exp + k_exp_max
    assert n_exp_max == Fraction(7, 4)


def audit_pointwise_multiplicity_countermodel() -> None:
    # Pointwise multiplicity O(1) does not imply off-diagonal collision saving.
    # N coordinates arranged two per label have collision mass of order N.
    for labels in [10, 50, 200]:
        r = [2] * labels
        total = sum(r)
        offdiag = sum(v * (v - 1) for v in r)
        assert max(r) == 2
        assert offdiag == total


def audit_boundary() -> None:
    require_text(
        ROOT / "stages/stage14/14-s7-14/result.md",
        [
            "STAGE14_S7_14=COMPLETE_LARGE_SHARED_LABEL_SHELL_AND_TRANSVERSE_K_COLLISION_RECEIVER",
            "XI_SHELL_COORDINATE_SUPPORT_EXPONENT=(1+gamma)/2",
            "XI_SHELL_SELECTED_TWO_CELL_EXPONENT=1-gamma/6",
            "XI_ONLY_MINIMAX_CRITICAL_EXPONENT=gamma=3/4",
            "XI_ONLY_MINIMAX_BARRIER=7/8",
            "CRITICAL_INTERNAL_SQUAREPART_PRODUCT_EXPONENT=1/8",
            "TRANSVERSE_LABEL_K=ker(Q^2-P^2)",
            "GCD_K_XI=1",
            "CRITICAL_J1728_TWIST_N_MAX_EXPONENT=7/4",
            "OFF_DIAGONAL_XI_K_COLLISION_ENERGY_RECEIVER_DEFINED=true",
            "OFF_DIAGONAL_XI_K_COLLISION_POWER_SAVING_PROVED=false",
            "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8",
            "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
            "NEXT=Stage14-s7-15",
        ],
    )


def main() -> None:
    audit_predecessors()
    audit_fixed_xi_partition_count()
    audit_xi_k_coprimality()
    audit_xi_shell_minimax()
    audit_critical_cell_pattern()
    audit_critical_twist_range()
    audit_pointwise_multiplicity_countermodel()
    audit_boundary()
    print("STAGE14_S7_14_AUDIT=PASS")
    print("CRITICAL_XI_EXPONENT=3/4")
    print("XI_ONLY_MINIMAX_BARRIER=7/8")
    print("TRANSVERSE_LABEL=K")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8")


if __name__ == "__main__":
    main()
