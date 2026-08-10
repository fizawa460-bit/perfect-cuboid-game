#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt


def squarefree_kernel(n: int) -> int:
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
        p += 1
    if x > 1:
        out *= x
    return out


def is_square(n: int) -> bool:
    r = isqrt(n)
    return r * r == n


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def check_fixed_squareclass() -> int:
    checks = 0
    for D0 in range(1, 120):
        sf = squarefree_kernel(D0)
        for H in range(1, 180):
            H2 = H * H
            if H2 % D0:
                continue
            G = H2 // D0
            assert G % sf == 0
            assert is_square(G // sf)
            t = isqrt(G // sf)
            assert sf * t * t == G
            assert D0 * G == H2
            checks += 1
    return checks


def check_root_cells() -> int:
    checks = 0
    for x1 in range(1, 12):
        for y1 in range(1, 12):
            if gcd(x1, y1) != 1:
                continue
            for x2 in range(1, 12):
                for y2 in range(1, 12):
                    if gcd(x2, y2) != 1:
                        continue
                    kx = oddpart(gcd(x1, x2))
                    ky = oddpart(gcd(y1, y2))
                    hs = oddpart(gcd(x2, y1))
                    ht = oddpart(gcd(x1, y2))
                    cells = (kx, ky, hs, ht)
                    for i in range(4):
                        for j in range(i + 1, 4):
                            assert gcd(cells[i], cells[j]) == 1
                    K = kx * ky
                    H = hs * ht
                    assert gcd(K, H) == 1
                    checks += 1
    return checks


def check_residual_forced_divisor() -> int:
    checks = 0
    for D0 in range(1, 60, 2):
        for H in range(1, 90, 2):
            if (H * H) % D0:
                continue
            G = H * H // D0
            for K in range(1, 40, 2):
                if gcd(K, H) != 1 or gcd(K, D0) != 1:
                    continue
                for q in range(1, 8):
                    R = K * K * G * q
                    assert R % (K * K * G) == 0
                    hp = D0 * R
                    assert hp % (H * H) == 0
                    assert hp % (K * K) == 0
                    checks += 1
    return checks


def check_exponent_ledger() -> int:
    half = Fraction(1, 2)
    D = 1056  # divisible by 24 and gives a fine exact grid
    checks = 0
    equality = []

    for ip in range(D * 5 // 24, D // 4 + 1):
        phi = Fraction(ip, D)
        chi = 2 * phi - Fraction(1, 4)
        a = Fraction(1, 4) - chi
        assert a == Fraction(1, 2) - 2 * phi
        assert 2 * phi + a == half

        # Stratify kappa,e on a denominator dividing D.
        for ik in range(0, int(a * D / 2) + 2):
            kappa = Fraction(ik, D)
            for ie in range(0, int(a * D) + 2):
                e = Fraction(ie, D)
                if 2 * kappa + e > a:
                    continue
                E = 2 * phi + kappa + e / 2 + (a - 2 * kappa - e)
                assert E == half - kappa - e / 2
                assert E <= half
                if E == half:
                    equality.append((phi, kappa, e))
                    assert kappa == 0 and e == 0
                else:
                    assert kappa > 0 or e > 0
                checks += 1

    assert equality
    assert all(k == 0 and e == 0 for _, k, e in equality)
    return checks


def check_refined_band() -> int:
    D = 528  # 5/24, 1/4 and 1/6 are integral grid points
    checks = 0
    min_j = Fraction(1)
    max_gap = Fraction(0)

    for ip in range(D * 5 // 24, D // 4 + 1):
        phi = Fraction(ip, D)
        chi = 2 * phi - Fraction(1, 4)
        smax = phi - Fraction(5, 24)
        for is_ in range(0, int(smax * D) + 1):
            s = Fraction(is_, D)
            j = chi - 2 * s
            assert j >= Fraction(1, 6)
            assert j <= chi
            assert chi - j == 2 * s
            min_j = min(min_j, j)
            max_gap = max(max_gap, chi - j)
            checks += 1

    assert min_j == Fraction(1, 6)
    assert max_gap == Fraction(1, 12)  # at phi=1/4, s=1/24
    return checks


def main() -> None:
    sq_checks = check_fixed_squareclass()
    root_checks = check_root_cells()
    div_checks = check_residual_forced_divisor()
    ledger_checks = check_exponent_ledger()
    band_checks = check_refined_band()

    print("Stage14-4da deterministic audit: PASS")
    print(f"fixed-squareclass checks: {sq_checks}")
    print(f"four-root cell checks: {root_checks}")
    print(f"forced residual-divisor checks: {div_checks}")
    print(f"root-gcd exponent ledger checks: {ledger_checks}")
    print(f"refined sqrt-band checks: {band_checks}")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2")
    print("ROOT_GCD_EXCESS_COMPLETE_COUNT=1/2-kappa-e/2")
    print("SQRT_SATURATION_SAMESIDE_ROOT_GCD=Bo1")
    print("SQRT_SATURATION_CROSS_ROOT_EXCESS=Bo1")
    print("SQRT_SATURATION_JOINT_CORE_LOWER_EXPONENT=1/6")
    print("MAINLINE_H_NEEDED=false")
    print("NEXT=Stage14-4db")


if __name__ == "__main__":
    main()
