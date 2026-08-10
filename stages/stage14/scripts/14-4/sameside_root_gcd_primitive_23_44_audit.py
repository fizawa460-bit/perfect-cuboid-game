#!/usr/bin/env python3
from fractions import Fraction
from math import gcd


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def check_four_root_gcd_cells() -> int:
    checks = 0
    for x1 in range(1, 15):
        for y1 in range(1, 15):
            if gcd(x1, y1) != 1:
                continue
            for x2 in range(1, 15):
                for y2 in range(1, 15):
                    if gcd(x2, y2) != 1:
                        continue
                    kx = oddpart(gcd(x1, x2))
                    ky = oddpart(gcd(y1, y2))
                    hs = oddpart(gcd(x2, y1))
                    ht = oddpart(gcd(x1, y2))
                    cells = [kx, ky, hs, ht]
                    for i in range(4):
                        for j in range(i + 1, 4):
                            assert gcd(cells[i], cells[j]) == 1
                    lhs = oddpart(gcd(x1 * y1, x2 * y2))
                    rhs = kx * ky * hs * ht
                    assert lhs == rhs
                    K = kx * ky
                    X = x1 * x2
                    Y = y1 * y2
                    assert (X * Y) % (K * K) == 0
                    checks += 1
    return checks


def check_column_transfer() -> int:
    checks = 0
    for K in range(1, 40, 2):
        for jm in range(1, 30, 2):
            if gcd(K, jm) != 1:
                continue
            for h in range(1, 20):
                L = K * jm * h
                assert L % jm == 0
                q = L // jm
                assert q % K == 0
                checks += 1
    return checks


def check_row_square_cancellation() -> int:
    checks = 0
    for K in range(1, 20, 2):
        K2 = K * K
        for mk in range(1, 20):
            for nk in range(1, 20):
                M = K2 * mk
                N = K2 * nk
                for C in range(1, 25, 2):
                    if gcd(C, K) != 1:
                        continue
                    if (M - N) % C == 0:
                        assert (mk - nk) % C == 0
                        checks += 1
                    if (M + N) % C == 0:
                        assert (mk + nk) % C == 0
                        checks += 1
    return checks


def check_kappa_ledger() -> int:
    base = Fraction(19, 44)
    a = Fraction(1, 22)
    current = Fraction(23, 44)
    sqrt = Fraction(1, 2)
    threshold = Fraction(1, 132)

    def positive(x: Fraction) -> Fraction:
        return max(Fraction(0), x)

    def E(k: Fraction) -> Fraction:
        return base + k + 2 * positive(a - 2 * k)

    assert E(Fraction(0)) == current
    assert E(Fraction(1, 44)) == Fraction(20, 44)
    assert E(Fraction(1, 22)) == Fraction(21, 44)
    assert E(threshold) == sqrt

    points = 0
    max_e = Fraction(0)
    max_points = []
    # denominator 2904 is divisible by 22, 44 and 132.
    D = 2904
    for i in range(0, D // 22 + 1):
        k = Fraction(i, D)
        e = E(k)
        assert e <= current
        if k > 0:
            assert e < current
        if k >= threshold:
            assert e <= sqrt
        if e > max_e:
            max_e = e
            max_points = [k]
        elif e == max_e:
            max_points.append(k)
        points += 1
    assert max_e == current
    assert max_points == [Fraction(0)]

    # Exact piecewise formulas.
    for i in range(0, D // 44 + 1):
        k = Fraction(i, D)
        assert E(k) == current - 3 * k
    for i in range(D // 44, D // 22 + 1):
        k = Fraction(i, D)
        assert E(k) == base + k
    return points


def check_endpoint_ledger() -> None:
    theta = Fraction(23, 88)
    phi = Fraction(19, 88)
    chi = 2 * theta + 2 * phi - Fraction(3, 4)
    assert chi == Fraction(9, 44)
    assert 2 * phi == Fraction(19, 44)
    assert Fraction(1, 4) - chi == Fraction(1, 22)
    assert 2 * (Fraction(1, 4) - chi) == Fraction(1, 11)
    assert 2 * theta == Fraction(23, 44)
    assert Fraction(23, 44) - Fraction(1, 2) == Fraction(1, 44)


def main() -> None:
    check_endpoint_ledger()
    root_checks = check_four_root_gcd_cells()
    column_checks = check_column_transfer()
    row_checks = check_row_square_cancellation()
    grid_points = check_kappa_ledger()

    print("Stage14-4cz deterministic audit: PASS")
    print(f"four-root gcd-cell checks: {root_checks}")
    print(f"column K-transfer checks: {column_checks}")
    print(f"row K^2-cancellation checks: {row_checks}")
    print(f"exact kappa grid points: {grid_points}")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44")
    print("SAMESIDE_ROOT_GCD_SQRT_CLOSURE_THRESHOLD=1/132")
    print("SAMESIDE_ROOT_GCD_AT_23_44_SATURATION=Bo1")
    print("GLOBAL_ODD_FOUR_ROOT_PRIMITIVITY_AT_SATURATION=true")
    print("NEXT=Stage14-4da")


if __name__ == "__main__":
    main()
