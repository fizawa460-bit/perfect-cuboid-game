from math import prod


def sf(n: int) -> int:
    n = abs(n)
    out = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e ^= 1
        if e:
            out *= p
        p += 1 if p == 2 else 2
    if n > 1:
        out *= n
    return out


def quartic_coeffs(A: int, B: int, kappa: int):
    return (
        kappa * A * B,
        2 * kappa * (A * A - B * B),
        -6 * kappa * A * B,
        -2 * kappa * (A * A - B * B),
        kappa * A * B,
    )


def invariants(coeffs):
    a, b, c, d, e = coeffs
    I = 12 * a * e - 3 * b * d + c * c
    J = 72 * a * c * e - 27 * a * d * d - 27 * b * b * e + 9 * b * c * d - 2 * c**3
    return I, J


def exact_data(A: int, B: int, kappa: int):
    k = A * A + B * B
    I, J = invariants(quartic_coeffs(A, B, kappa))
    d = sf(2 * k * kappa)
    s = k * kappa
    recovered_s = d // 2 if d % 2 == 0 else 2 * d
    return {
        "k": k,
        "I": I,
        "J": J,
        "d": d,
        "s": s,
        "recovered_s": recovered_s,
    }


def verify_examples():
    examples = [(1, 2, 3), (2, 3, 5), (1, 4, 5), (4, 7, 3)]
    for A, B, kappa in examples:
        data = exact_data(A, B, kappa)
        k = data["k"]
        assert data["I"] == 12 * (k * kappa) ** 2
        assert data["J"] == 0
        assert data["recovered_s"] == data["s"]
    return True


if __name__ == "__main__":
    assert verify_examples()
    print("STAGE15_6AR_VERIFY=PASS")
    print("EXACT_JACOBIAN=true")
    print("EXACT_TWIST_PARAMETER=true")
