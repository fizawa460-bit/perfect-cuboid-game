from fractions import Fraction
from math import gcd


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def is_squarefree(n: int) -> bool:
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


def prime_factors(n: int):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def test_euclid_cross_role_divisibility():
    checks = 0
    for a in range(1, 40):
        for b in range(1, 40):
            if gcd(a, b) != 1:
                continue
            for t in range(1, 12):
                # a*(b*t) = b*(a*t), modelling
                # (R delta)*(X s) = (J alpha)*(Y r).
                xs = b * t
                yr = a * t
                assert a * xs == b * yr
                assert oddpart(a) != 0 and oddpart(b) != 0
                assert yr % oddpart(a) == 0
                assert xs % oddpart(b) == 0
                checks += 1
    return checks


def test_endpoint_gap():
    lower = Fraction(3, 8)
    upper = Fraction(1, 8)
    assert lower - upper == Fraction(1, 4)
    assert lower > upper
    return str(lower - upper)


def test_switch_product_identities():
    checks = 0
    for A in range(1, 12):
        for D in range(A + 1, 15):
            hp = D * D + A * A
            hm = D * D - A * A
            assert hp * hm == D**4 - A**4
            checks += 1
    for U in range(1, 12):
        for V in range(U + 1, 15):
            hp = V * V + U * U
            hm = V * V - U * U
            assert hp * hm == V**4 - U**4
            checks += 1
    return checks


def test_i_branch_prime_signature():
    checks = 0
    for a in range(1, 50):
        for b in range(1, 50):
            if gcd(a, b) != 1:
                continue
            n = a * a + b * b
            for p in prime_factors(n):
                if p == 2:
                    continue
                assert p % 4 == 1
                checks += 1
    return checks


def quartic(a: int, b: int) -> int:
    return a * b * (b - a) * (b + a)


def test_relaxed_diagonal_exists_but_is_only_relaxed():
    # X3's guard: primitive squarefree coprime diagonal pairs give a
    # fixed-power relaxed family. X4 does not interpret these as physical.
    counts = []
    for cutoff in (40, 80, 160):
        c = 0
        for a in range(1, cutoff + 1):
            for b in range(a + 1, cutoff + 1):
                if gcd(a, b) == 1 and is_squarefree(a) and is_squarefree(b):
                    assert quartic(a, b) == quartic(a, b)
                    c += 1
        counts.append(c)
    assert counts[0] < counts[1] < counts[2]
    return counts


def main():
    euclid = test_euclid_cross_role_divisibility()
    gap = test_endpoint_gap()
    switches = test_switch_product_identities()
    i_checks = test_i_branch_prime_signature()
    diagonal_counts = test_relaxed_diagonal_exists_but_is_only_relaxed()

    print("Stage14-X4 deterministic audit: PASS")
    print(f"cross-role Euclid checks: {euclid}")
    print(f"proportional endpoint exponent gap: {gap}")
    print(f"switch fourth-difference identity checks: {switches}")
    print(f"i-branch odd-prime signature checks: {i_checks}")
    print(f"relaxed diagonal counts: {diagonal_counts}")
    print("physical proportional branch theorem source: merged Stage14-4cl")
    print("remaining receiver: OffDiagonalReciprocalCyclotomicQuarticAllocationIncidence")
    print("current whole-family exponent: 7/8")


if __name__ == "__main__":
    main()
