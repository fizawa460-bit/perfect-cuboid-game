#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def quartic_num(a: int, b: int) -> int:
    # b^4 * (z^4 - 20 z^2 + 256 z - 412), z=a/b.
    return a**4 - 20 * a * a * b * b + 256 * a * b**3 - 412 * b**4


def d_x_num(a: int, b: int) -> int:
    # b^16 * D((a/b)^2).
    A = a**8 - 8 * a**4 * b**4 + b**8
    B = 16 * a**3 * b**3 * (a * a - b * b)
    return A * A + B * B


def d_mod_x2(x: int, p: int) -> int:
    k = x * x % p
    return (
        k**8
        - 16 * k**6
        + 256 * k**5
        - 446 * k**4
        + 256 * k**3
        - 16 * k**2
        + 1
    ) % p


def primes_below(n: int):
    out = []
    for x in range(2, n):
        ok = True
        d = 2
        while d * d <= x:
            if x % d == 0:
                ok = False
                break
            d += 1
        if ok:
            out.append(x)
    return out


def main():
    quartic_bound = 1000
    quartic_examined = 0
    quartic_points = []
    for b in range(1, quartic_bound + 1):
        for a in range(-quartic_bound, quartic_bound + 1):
            if gcd(abs(a), b) != 1:
                continue
            quartic_examined += 1
            n = quartic_num(a, b)
            if is_square(n):
                y = isqrt(n)
                quartic_points.append((Fraction(a, b), Fraction(y, b * b)))

    cover_bound = 500
    cover_examined = 0
    cover_survivors = []
    for b in range(1, cover_bound + 1):
        for a in range(1, cover_bound + 1):
            if gcd(a, b) != 1 or a == b:
                continue
            cover_examined += 1
            n = d_x_num(a, b)
            if is_square(n):
                cover_survivors.append(Fraction(a, b))

    local_sieve_primes = []
    for p in primes_below(500):
        if p == 2:
            continue
        squares = {i * i % p for i in range(p)}
        surviving_x = [x for x in range(p) if d_mod_x2(x, p) in squares]
        if all(x in (0, 1, p - 1) for x in surviving_x):
            local_sieve_primes.append(p)

    expected_quartic = [
        (Fraction(2, 1), Fraction(6, 1)),
        (Fraction(26, 3), Fraction(694, 9)),
        (Fraction(-287, 30), Fraction(54631, 900)),
    ]
    assert quartic_examined == 1216767
    assert quartic_points == expected_quartic
    assert cover_examined == 152230
    assert cover_survivors == []
    assert local_sieve_primes == [3, 5, 7, 23]

    print("quartic_examined=", quartic_examined)
    print("quartic_positive_y_representatives=", quartic_points)
    print("first_two_cover_examined=", cover_examined)
    print("first_two_cover_survivors=", cover_survivors)
    print("local_sieve_primes_below_500=", local_sieve_primes)
    print("A1-4 bounded search: PASS")


if __name__ == "__main__":
    main()
