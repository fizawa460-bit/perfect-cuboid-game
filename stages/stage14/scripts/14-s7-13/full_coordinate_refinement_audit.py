#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def require_text(path: Path, needles: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


def squarepart_root(n: int) -> int:
    x = n
    y = 1
    p = 2
    while p * p <= x:
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        if e >= 2:
            y *= p ** (e // 2)
        p += 1 if p == 2 else 2
    return y


def squarefree_kernel(n: int) -> int:
    y = squarepart_root(n)
    return n // (y * y)


def audit_predecessors() -> None:
    require_text(
        ROOT / "stages/stage14/14-s7-12/result.md",
        [
            "STAGE14_S7_12=COMPLETE_UNBALANCED_SHORT_DENOMINATOR_RECEIVER_AND_10_11_BOUND",
            "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=10/11",
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
    require_text(
        ROOT / "stages/stage14/14-s7-04/result.md",
        [
            "FIXED_REDUCED_COORDINATE_FIBER_MULTIPLICITY=B^o(1)",
            "JOINT_MULTIPLICATIVE_HEIGHT=Q*S",
        ],
    )


def audit_canonical_decomposition() -> None:
    for n in range(1, 4000):
        y = squarepart_root(n)
        a = squarefree_kernel(n)
        assert n == a * y * y
        p = 2
        while p * p <= a:
            assert a % (p * p) != 0
            p += 1


def audit_dyadic_support() -> None:
    # Finite regression for # {N~A : canonical squarepart root x~X} << A/X.
    # The proof in result.md is the divisor sum; this is only a deterministic census.
    for A in [64, 96, 128, 192, 256, 384, 512, 768, 1024]:
        for X in [1, 2, 4, 8, 16]:
            count = 0
            for n in range(A, 2 * A):
                x = squarepart_root(n)
                if X <= x < 2 * X:
                    count += 1
            envelope = 8 * A // X + 16
            assert count <= envelope, (A, X, count, envelope)


def audit_four_cell_symmetry() -> None:
    from math import gcd

    cells = [1, 2, 3, 5, 7, 11]
    checks = 0
    for r in cells:
        for s in cells:
            for t in cells:
                for j in cells:
                    vals = [r, s, t, j]
                    if any(gcd(vals[i], vals[k]) != 1 for i in range(4) for k in range(i + 1, 4)):
                        continue
                    a = r * s
                    b = t * j
                    c = r * t
                    d = s * j
                    assert a * b == c * d
                    # Both numerator and denominator squarefree coefficients are valid 2-cell products.
                    assert a == r * s
                    assert b == t * j
                    x = 3
                    y = 5
                    P = a * x * x
                    Q = b * y * y
                    assert squarefree_kernel(P) == a
                    assert squarepart_root(P) == x
                    assert squarefree_kernel(Q) == b
                    assert squarepart_root(Q) == y
                    checks += 1
    assert checks > 20


def block_bound(p: Fraction, q: Fraction, s: Fraction, t: Fraction) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    alpha = p - 2 * s
    beta = q - 2 * t
    assert alpha >= 0 and beta >= 0
    m = max(alpha, beta)
    support = p + q - s - t
    two_cell = Fraction(1) - m / 3
    return min(support, two_cell), support, two_cell, m


def audit_exact_optimization() -> None:
    p = q = Fraction(1, 2)
    s = t = Fraction(1, 16)
    val, support, two_cell, m = block_bound(p, q, s, t)
    assert m == Fraction(3, 8)
    assert support == Fraction(7, 8)
    assert two_cell == Fraction(7, 8)
    assert val == Fraction(7, 8)

    # Algebraic envelope at the critical m.
    assert Fraction(1, 2) + m == Fraction(7, 8)
    assert Fraction(1) - m / 3 == Fraction(7, 8)

    # Exhaustive exact rational grid.  Use denominator 32 so the equality geometry
    # p=q=1/2, s=t=1/16 occurs exactly.
    grid_max = Fraction(0)
    maximizers = []
    den = 32
    for qi in range(0, den // 2 + 1):
        qv = Fraction(qi, den)
        for pi in range(0, qi + 1):
            pv = Fraction(pi, den)
            for si in range(0, pi // 2 + 1):
                sv = Fraction(si, den)
                if 2 * sv > pv:
                    continue
                for ti in range(0, qi // 2 + 1):
                    tv = Fraction(ti, den)
                    if 2 * tv > qv:
                        continue
                    v, sup, ana, mm = block_bound(pv, qv, sv, tv)
                    assert sup <= Fraction(1, 2) + mm
                    assert v <= Fraction(7, 8)
                    if v > grid_max:
                        grid_max = v
                        maximizers = [(pv, qv, sv, tv, mm)]
                    elif v == grid_max:
                        maximizers.append((pv, qv, sv, tv, mm))
    assert grid_max == Fraction(7, 8)
    assert (Fraction(1, 2), Fraction(1, 2), Fraction(1, 16), Fraction(1, 16), Fraction(3, 8)) in maximizers

    # Direct one-variable envelope check on a fine rational grid.
    env_max = Fraction(0)
    for i in range(0, 1001):
        mm = Fraction(i, 2000)  # [0,1/2]
        env = min(Fraction(1, 2) + mm, Fraction(1) - mm / 3)
        env_max = max(env_max, env)
        assert env <= Fraction(7, 8)
    assert env_max >= Fraction(1749, 2000)


def audit_ledger() -> None:
    new = Fraction(7, 8)
    assert Fraction(10, 11) - new == Fraction(3, 88)
    assert Fraction(13, 14) - new == Fraction(3, 56)
    assert Fraction(41, 42) - new == Fraction(17, 168)
    assert new - Fraction(1, 2) == Fraction(3, 8)
    assert 2 * Fraction(3, 8) == Fraction(3, 4)


def audit_boundary() -> None:
    require_text(
        ROOT / "stages/stage14/14-s7-13/result.md",
        [
            "STAGE14_S7_13=COMPLETE_FULL_COORDINATE_CANONICAL_REFINEMENT_AND_7_8_BOUND",
            "COMMON_REFINEMENT_RECEIVER_IS_MIN_OF_TWO_VALID_BOUNDS=true",
            "FIXED_COORDINATE_AND_TWO_CELL_SAVINGS_MULTIPLIED=false",
            "CRITICAL_SELECTED_COEFFICIENT_EXPONENT=3/8",
            "CRITICAL_NUMERATOR_SQUAREPART_ROOT_EXPONENT=1/16",
            "CRITICAL_DENOMINATOR_SQUAREPART_ROOT_EXPONENT=1/16",
            "CRITICAL_SHARED_LABEL_EXPONENT=3/4",
            "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8",
            "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true",
            "SQRT_B_UPPER_BOUND_PROVED=false",
            "NEXT=Stage14-s7-14",
        ],
    )


def main() -> None:
    audit_predecessors()
    audit_canonical_decomposition()
    audit_dyadic_support()
    audit_four_cell_symmetry()
    audit_exact_optimization()
    audit_ledger()
    audit_boundary()
    print("STAGE14_S7_13_AUDIT=PASS")
    print("CRITICAL_SELECTED_COEFFICIENT_EXPONENT=3/8")
    print("CRITICAL_SQUAREPART_ROOT_EXPONENT=1/16")
    print("CRITICAL_SHARED_LABEL_EXPONENT=3/4")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8")


if __name__ == "__main__":
    main()
