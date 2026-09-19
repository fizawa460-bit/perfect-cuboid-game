#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from math import isqrt

def g1_bound(N: int) -> Fraction:
    den = 28 - 3*N
    if den <= 0:
        raise ValueError("no finite bound from this gate")
    return Fraction(168*N, den)

def g0_poly(N: int, d: int) -> int:
    # Equivalent to
    # (d+4)^2/N <= 3(2d^2+110d+221)/56.
    return 56*(d+4)**2 - 3*N*(2*d*d + 110*d + 221)

def floor_sqrt_frac_num(num: int, den: int) -> int:
    # floor(sqrt(num/den))
    q = num // den
    r = isqrt(q)
    while (r+1)*(r+1)*den <= num:
        r += 1
    while r*r*den > num:
        r -= 1
    return r

def main() -> None:
    assert g1_bound(8) == 336
    assert g1_bound(9) == 1512

    # g=0: exact integer cutoff checks.
    assert g0_poly(8, 275) <= 0
    assert g0_poly(8, 276) > 0
    assert g0_poly(9, 1263) <= 0
    assert g0_poly(9, 1264) > 0

    # N=10 asymptotic coefficient for forced FSM-minimal branches:
    # 3/2 - sqrt(15/14) > 0 because (3/2)^2=9/4 > 15/14.
    assert Fraction(9,4) > Fraction(15,14)

    # Finite threshold replays for the lower bounds in the note.
    # Compare after squaring only where the target side is positive.
    def f1_positive(d: int) -> bool:
        # 2d - sqrt(15d(d+56)/14) - 10 - 1/2 sqrt(d^2+80d+400) > 0
        # numerical replay is only a checksum; exact route uses displayed inequalities.
        import decimal
        decimal.getcontext().prec = 60
        D=decimal.Decimal
        return (
            2*D(d)
            -(D(15)*D(d)*D(d+56)/D(14)).sqrt()
            -D(10)
            -(D(d*d+80*d+400)).sqrt()/D(2)
        ) > 0

    def f0_positive(d: int) -> bool:
        import decimal
        decimal.getcontext().prec = 60
        D=decimal.Decimal
        return (
            2*D(d+4)
            -(D(15)*D(2*d*d+110*d+221)/D(28)).sqrt()
            -D(10)
            -(D(d*d+48*d+496)).sqrt()/D(2)
        ) > 0

    assert not f1_positive(116)
    assert f1_positive(117)
    assert not f0_positive(84)
    assert f0_positive(85)

    print("PASS_MB104_Z_REVIVED_PASS2_NUMERICS")

if __name__ == "__main__":
    main()
