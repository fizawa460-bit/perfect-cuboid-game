#!/usr/bin/env python3


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


def f_mod(x: int, p: int) -> int:
    return (
        pow(x, 16, p)
        - 16 * pow(x, 12, p)
        + 256 * pow(x, 10, p)
        - 446 * pow(x, 8, p)
        + 256 * pow(x, 6, p)
        - 16 * pow(x, 4, p)
        + 1
    ) % p


def affine_survivors(p: int):
    squares = {y * y % p for y in range(p)}
    return [x for x in range(p) if f_mod(x, p) in squares]


def main():
    # For the genus-7 curve y^2=F(x), a good-reduction prime with only
    # x=0,+/-1 as affine survivor x-values would give at most 8 points on
    # the smooth projective curve: 6 above those values and 2 at infinity.
    # Hasse-Weil gives #C(F_p) >= p+1-14*sqrt(p). For p>=211 this is >8,
    # since p^2-210p+49>0 already at 211 and increases thereafter.
    assert 211 * 211 - 210 * 211 + 49 > 0

    special = []
    counts = {}
    for p in primes_below(211):
        if p == 2:
            continue
        survivors = affine_survivors(p)
        counts[p] = len(survivors)
        if all(x in (0, 1, p - 1) for x in survivors):
            special.append(p)

    assert special == [3, 5, 7, 23]
    assert affine_survivors(13) == [0, 1, 5, 8, 12]
    assert affine_survivors(19) == [0, 1, 7, 8, 11, 12, 18]

    print("odd_primes_scanned_below_211=", len(counts))
    print("trivial_reduction_only_primes=", special)
    print("bad_reduction_p13_survivors=", affine_survivors(13))
    print("bad_reduction_p19_survivors=", affine_survivors(19))
    print("hasse_weil_threshold_prime=211")
    print("A1-6 local-sieve completeness: PASS")


if __name__ == "__main__":
    main()
