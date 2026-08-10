#!/usr/bin/env python3
from fractions import Fraction


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    v = pow(a, (p - 1) // 2, p)
    return -1 if v == p - 1 else v


def corr(row1, row2):
    return sum(a * b for a, b in zip(row1, row2))


def main() -> None:
    P = 4
    row = [1] * P
    assert 2 * 1 * (-1) * corr(row, row) ** 2 == -2 * P * P

    primes = [5, 13]
    row_d1 = [legendre(1, p) for p in primes]
    row_d6 = [legendre(6, p) for p in primes]
    assert row_d1 == [1, 1]
    assert row_d6 == [1, -1]
    assert corr(row_d1, row_d6) == 0

    H, P = 2, 4
    raw_target = H * P * P
    centered_value = H * (H - 1) * P * P
    centered_random_scale = H * H * P
    assert centered_value == raw_target == 32
    assert centered_value > centered_random_scale == 16
    assert Fraction(1, 7) - Fraction(1, 8) == Fraction(1, 56)

    r, P = 7, 11
    exact_energy = r
    raw_second_moment = P * (P - 1) * r * r
    near_linear_target = P * P * exact_energy
    assert raw_second_moment > near_linear_target

    H, P = 1, 5
    raw = H * H * P * P
    state_diag = H * P * P
    assert raw - state_diag == 0
    assert raw - state_diag - state_diag < 0

    rho = Fraction(1, 7)
    d_safe = Fraction(4, 1)
    assert 2 * rho == Fraction(2, 7)
    assert 2 * rho < d_safe

    print("Stage14-toolbox-H0 interface counterexample audit: PASS")
    print("CE1 signed positivity guard: PASS")
    print("CE2 same-k/Gaussian-row bridge guard: PASS")
    print("CE3 raw-vs-centered scale guard: PASS")
    print("CE4 principal coherence guard: PASS")
    print("CE5 diagonal-once guard: PASS")
    print("CE7 rho=1/7 conductor-scale guard: PASS")


if __name__ == "__main__":
    main()
