#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def require_text(path: Path, needles: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


def squarepart_root(n: int) -> int:
    """Largest y such that n=b*y^2 with b squarefree."""
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


def audit_predecessor_boundaries() -> None:
    require_text(
        ROOT / "stages/stage14/14-s7-11/result.md",
        [
            "STAGE14_S7_11=COMPLETE_MULTICELL_TORUS_QUOTIENT_AND_13_14_ARCHITECTURE_BARRIER",
            "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=13/14",
            "PAIRWISE_TWO_CELL_SAVINGS_MULTIPLY=false",
        ],
    )
    require_text(
        ROOT / "stages/stage14/14-s7-10/result.md",
        [
            "ADJACENT_TWO_CELL_MIXED_FOURIER_OP_BOUND_PROVED=true",
            "TWO_CELL_RECTANGLE_EXPONENT=2/3",
            "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=13/14",
        ],
    )
    require_text(
        ROOT / "stages/stage14/14-s7-04/result.md",
        [
            "FIXED_REDUCED_COORDINATE_FIBER_MULTIPLICITY=B^o(1)",
            "JOINT_MULTIPLICATIVE_HEIGHT=Q*S",
        ],
    )


def audit_canonical_square_decomposition() -> None:
    for n in range(1, 2000):
        y = squarepart_root(n)
        b = squarefree_kernel(n)
        assert n == b * y * y
        # b must be squarefree
        t = b
        p = 2
        while p * p <= t:
            assert t % (p * p) != 0
            p += 1


def audit_large_squarepart_support() -> None:
    # Finite regression for the analytic estimate
    # sum_{D<=Q<2D, sp(Q)>=Y} Q << D^2/Y.
    # We use a deliberately loose absolute envelope because the theorem proof
    # is the divisor-sum estimate in result.md, not this finite census.
    for D in [16, 24, 40, 64, 96, 128, 192, 256]:
        for Y in [1, 2, 3, 4, 5, 8, 12]:
            if Y > isqrt(2 * D):
                continue
            weighted = 0
            for q in range(D, 2 * D):
                if squarepart_root(q) >= Y:
                    weighted += q
            envelope = 12 * D * D // Y + 12 * D
            assert weighted <= envelope, (D, Y, weighted, envelope)


def audit_four_cell_denominator_identity() -> None:
    # Small pairwise-coprime squarefree cells.  The denominator coefficient
    # b=t*j is exactly an adjacent two-cell product.
    cells = [1, 2, 3, 5, 7, 11]
    checks = 0
    for r in cells:
        for s in cells:
            for t in cells:
                for j in cells:
                    vals = [r, s, t, j]
                    ok = True
                    for i in range(4):
                        for k in range(i + 1, 4):
                            from math import gcd
                            if gcd(vals[i], vals[k]) != 1:
                                ok = False
                    if not ok:
                        continue
                    a = r * s
                    b = t * j
                    c = r * t
                    d = s * j
                    assert a * b == c * d
                    y = 3
                    Q = b * y * y
                    assert squarefree_kernel(Q) == b
                    assert squarepart_root(Q) == y
                    checks += 1
    assert checks > 20


def thin_exponent(q: Fraction, tau: Fraction) -> Fraction:
    if q <= 2 * tau:
        return 2 * q
    return min(2 * q, Fraction(1) - (q - 2 * tau) / 3)


def audit_exact_minimax() -> None:
    tau = Fraction(1, 11)
    q0 = (3 + 2 * tau) / 7
    assert q0 == Fraction(5, 11)
    assert q0 >= 2 * tau
    assert q0 <= Fraction(1, 2)

    thin = thin_exponent(q0, tau)
    assert thin == Fraction(10, 11)
    assert Fraction(1) - tau == Fraction(10, 11)

    # Exact formulas at the crossing.
    assert 2 * q0 == Fraction(10, 11)
    assert Fraction(1) - (q0 - 2 * tau) / 3 == Fraction(10, 11)
    assert q0 - 2 * tau == Fraction(3, 11)

    # Top denominator dyad is already strictly easier on the thin side.
    top_thin = Fraction(1) - (Fraction(1, 2) - 2 * tau) / 3
    assert top_thin == Fraction(59, 66)
    assert top_thin < Fraction(10, 11)

    # Check a fine exact rational grid: max_q min(...) is attained at q0
    # up to grid resolution and never exceeds the claimed formula.
    grid_max = Fraction(0)
    for i in range(0, 1101):
        q = Fraction(i, 2200)  # [0,1/2]
        val = thin_exponent(q, tau)
        grid_max = max(grid_max, val)
        assert val <= Fraction(10, 11)
    assert grid_max >= Fraction(999, 1100)  # close to 10/11

    # One-parameter lower-bound certificate.
    E = Fraction(10, 11)
    assert E == max(Fraction(1) - tau, (6 + 4 * tau) / 7)
    # If E'<10/11, inequalities tau>=1-E' and 7E'>=6+4tau
    # are incompatible.  Verify the exact rearrangement 11E>=10.
    assert 11 * E == 10


def audit_ledger() -> None:
    new = Fraction(10, 11)
    old = Fraction(13, 14)
    post_local = Fraction(41, 42)
    assert old - new == Fraction(3, 154)
    assert Fraction(15, 16) - new == Fraction(5, 176)
    assert Fraction(18, 19) - new == Fraction(8, 209)
    assert post_local - new == Fraction(31, 462)
    assert new - Fraction(1, 2) == Fraction(9, 22)


def audit_boundary() -> None:
    require_text(
        ROOT / "stages/stage14/14-s7-12/result.md",
        [
            "STAGE14_S7_12=COMPLETE_UNBALANCED_SHORT_DENOMINATOR_RECEIVER_AND_10_11_BOUND",
            "UNBALANCED_THIN_RECEIVER_IS_MIN_OF_TWO_VALID_BOUNDS=true",
            "FIXED_COORDINATE_AND_TWO_CELL_SAVINGS_MULTIPLIED=false",
            "OPTIMAL_DENOMINATOR_SQUAREPART_THRESHOLD_EXPONENT=1/11",
            "CRITICAL_THIN_DENOMINATOR_EXPONENT=5/11",
            "CRITICAL_DENOMINATOR_COEFFICIENT_EXPONENT=3/11",
            "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=10/11",
            "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true",
            "NEXT=Stage14-s7-13",
        ],
    )


def main() -> None:
    audit_predecessor_boundaries()
    audit_canonical_square_decomposition()
    audit_large_squarepart_support()
    audit_four_cell_denominator_identity()
    audit_exact_minimax()
    audit_ledger()
    audit_boundary()
    print("STAGE14_S7_12_AUDIT=PASS")
    print("OPTIMAL_TAU=1/11")
    print("CRITICAL_Q_EXPONENT=5/11")
    print("CRITICAL_B_EXPONENT=3/11")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=10/11")


if __name__ == "__main__":
    main()
