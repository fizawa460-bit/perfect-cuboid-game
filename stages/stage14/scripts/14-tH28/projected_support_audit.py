from math import isqrt


def lpf(n: int) -> int:
    p = 2
    last = 1
    while p * p <= n:
        while n % p == 0:
            last = p
            n //= p
        p += 1 if p == 2 else 2
    return max(last, n)


def valuation(n: int, p: int) -> int:
    e = 0
    while n % p == 0:
        e += 1
        n //= p
    return e


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


def prime_factors(n: int):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out.append(n)
    return out


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True


def main():
    # Exhaustively audit the algebraic implications on a finite diagnostic box.
    checked = 0
    for B in range(10, 300):
        for hk0 in range(1, 7):
            for u in range(0, 16):
                for v in range(1, 16):
                    if gcd(u, v) != 1:
                        continue
                    n = u*u + v*v
                    for ell in range(5, 500):
                        if not is_prime(ell) or ell % 4 != 1:
                            continue
                        Q = ell * n
                        if ell * ell <= 4 * B:
                            continue
                        if ell * ell <= 2 * hk0 * Q:
                            continue
                        if hk0 * Q > 2 * B:
                            continue
                        checked += 1
                        assert ell > 2 * hk0 * n
                        assert ell > n
                        assert lpf(Q) == ell
                        assert valuation(Q, ell) == 1
                        for p in prime_factors(n):
                            if p % 2:
                                assert p % 4 == 1

    assert checked > 0

    # The theorem applicability lock is intentionally negative.
    verdict = {
        "DIRECT_THEOREM_APPLICABLE": False,
        "UNIFORM_FIXED_POWER_SAVING_PROVED": False,
        "CERTIFIED_B_POWER_SAVING_EXPONENT": 0,
        "LPF_AUTOMATIC_FROM_STRONG_GAP": True,
        "ELL_VALUATION_ONE_AUTOMATIC_FROM_STRONG_GAP": True,
        "ODD_SPLIT_SUPPORT_AUTOMATIC_FROM_PRIMITIVE_NORM": True,
        "WHOLE_FAMILY_CROSS_PROMOTION_PROVED": False,
    }
    for key, value in verdict.items():
        print(f"{key}={str(value).lower() if isinstance(value, bool) else value}")
    print(f"FINITE_DIAGNOSTIC_CASES={checked}")


if __name__ == "__main__":
    main()
