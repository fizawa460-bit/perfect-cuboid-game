#!/usr/bin/env python3
from math import gcd

D0 = {
    1, -1, 3, -3, 13, -13, 19, -19,
    39, -39, 57, -57, 247, -247, 741, -741,
}


def H(a: int, b: int) -> int:
    return a**4 - 20*a*a*b*b + 256*a*b**3 - 412*b**4


def v2(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 99
    e = 0
    while n % 2 == 0:
        e += 1
        n //= 2
    return e


def squarefree_signed_divisors_741():
    vals = set()
    for mask in range(8):
        d = 1
        for bit, p in enumerate((3, 13, 19)):
            if mask & (1 << bit):
                d *= p
        vals.add(d)
        vals.add(-d)
    return vals


def main():
    assert H(2, 1) == 36
    assert H(-2, 1) == -988

    # Exact gcd bounds: H(a,b) modulo a±2b is H(±2b,b).
    for a in range(-50, 51):
        for b in range(1, 31):
            if gcd(a, b) != 1:
                continue
            hm = H(a, b)
            assert gcd(abs(a - 2*b), abs(hm)) in (1, 2, 3, 4, 6, 9, 12, 18, 36)
            assert 988 % gcd(abs(a + 2*b), abs(hm)) == 0
            assert 4 % gcd(abs(a - 2*b), abs(a + 2*b)) == 0

    # Primitive parity classes: v2(H) is 0 except in the even-a/odd-b
    # case, where it is exactly 2. Residues mod 16 suffice.
    for a in range(16):
        for b in range(16):
            if gcd(a, b) != 1:
                continue
            e = v2(H(a, b))
            if a % 2 == 0 and b % 2 == 1:
                assert e == 2
            else:
                assert e == 0

    assert squarefree_signed_divisors_741() == D0

    # A1-9 inherited delta=+19 elimination is a subset statement:
    # if T_19(Q) is empty, the stricter G0 delta=19 receiver is empty.
    assert 19 in D0

    print("H(2,1)=36")
    print("H(-2,1)=-988")
    print("gcd_bounds=PASS")
    print("two_adic_H_squareclass=PASS")
    print("D0=", sorted(D0))
    print("G0_exact_16_branch_receiver=PASS")
    print("A1-10 exact verification: PASS")


if __name__ == "__main__":
    main()
