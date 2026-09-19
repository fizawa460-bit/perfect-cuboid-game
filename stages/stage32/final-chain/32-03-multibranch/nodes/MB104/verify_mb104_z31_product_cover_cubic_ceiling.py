#!/usr/bin/env python3
from fractions import Fraction


def require(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


def hk(k):
    # genus 5 curve X(8)
    if k == 0:
        return 1
    if k == 1:
        return 5
    return 8*k - 4


def product_dim(m):
    return sum(hk(i)*hk(m-i) for i in range(m+1))


def closed_form(m):
    return Fraction(32,3)*m**3 - 32*m**2 + Fraction(208,3)*m - 48


def main():
    for m in range(4,500):
        require(product_dim(m) == closed_form(m), f"product formula m={m}")

    require(Fraction(32,3)/8 == Fraction(4,3), "order-8 invariant cubic coefficient")
    require(14*Fraction(11,108) == Fraction(77,54), "N14 full extension cubic cost")
    require(Fraction(77,54)-Fraction(4,3) == Fraction(5,54), "N14 cubic deficit")

    # FSM branchwise pole inequality rearrangements.
    # d <= 16g-16+4R8.
    # g=1 => R8>=d/4; g=0 => R8>=d/4+4.
    for d in range(4,400,4):
        r8_g1 = Fraction(d,4)
        r8_g0 = Fraction(d,4)+4
        require(d <= 4*r8_g1, "g1 FSM rearrangement")
        require(d <= -16 + 4*r8_g0, "g0 FSM rearrangement")

    print("PASS: product Sym^m dimension cubic 32/3; order-8 invariant cubic 4/3; N14 deficit remains 5/54")


if __name__ == "__main__":
    main()
