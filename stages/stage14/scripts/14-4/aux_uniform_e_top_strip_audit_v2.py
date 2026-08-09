#!/usr/bin/env python3
"""Stage14-4bc deterministic audit, squareclass-kernel corrected."""

import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4bc/result.md"
NOTATION = ROOT / "stages/stage14/14-4bc/notation.md"
SUPPLEMENT = ROOT / "stages/stage14/14-4bc/e-density-completion.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/aux_uniform_e_top_strip_summary.json"
FOUR_BB = ROOT / "stages/stage14/14-4bb/result.md"
FOUR_AY = ROOT / "stages/stage14/14-4ay/result.md"
S5C = ROOT / "stages/stage14/14-s5c/result.md"
S5D = ROOT / "stages/stage14/14-s5d/result.md"
S5M = ROOT / "stages/stage14/14-s5m/result.md"


def factor_with_exp(n: int):
    n = abs(n)
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p += 1 if p == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out


def prime_factors(n: int):
    return [p for p, _ in factor_with_exp(n)]


def odd_squareclass_kernel(n: int) -> int:
    r = 1
    for p, e in factor_with_exp(n):
        if p != 2 and e % 2 == 1:
            r *= p
    return r


def jacobi_odd(a: int, n: int) -> int:
    if n == 1:
        return 1
    assert n > 0 and n % 2 == 1 and gcd(a, n) == 1
    a %= n
    ans = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                ans = -ans
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            ans = -ans
        a %= n
    return ans if n == 1 else 0


def dot2(a, b):
    return sum(x * y for x, y in zip(a, b)) % 2


def main() -> None:
    result = RESULT.read_text()
    notation = NOTATION.read_text()
    supplement = SUPPLEMENT.read_text()
    summary = json.loads(SUMMARY.read_text())
    bb = FOUR_BB.read_text()
    ay = FOUR_AY.read_text()
    s5c = S5C.read_text()
    s5d = S5D.read_text()
    s5m = S5M.read_text()

    assert "K4_GRAPH_ASSEMBLY_SAVING_EXPONENT=1/200" in bb
    assert "FROZEN_AUXILIARY_MODULUS_DOES_NOT_WORSEN_SLICING_ERROR=true" in ay
    assert ("H / 23" in s5c) or ("H/23" in s5c)
    assert "p|H : chi(d1)=+1" in s5d
    assert "MEDIUM_E_LINEAR_DISPERSION_PROVED=true" in s5m
    assert "E_FIXED_ROOT_SHORTEST_VECTOR_BOUND_PROVED=true" in s5m
    assert "AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true" in result
    assert "BALANCED_SPLIT_E_TOP_STRIP_DISPERSION_PROVED=false" in result
    assert "squareclass-kernel" in notation
    assert "F(s)=L(s,chi)L(s,chi*chi4)G(s)" in supplement

    # H-column same-factor interaction is identically even/zero.
    selected = (0, 1, 1)
    unselected = (0, 0, 0)
    for row in ((0, 1, 1), (1, 0, 0)):
        assert dot2(row, selected) == 0
        assert dot2(row, unselected) == 0
    assert dot2((1, 0, 0), selected) == 0
    assert dot2((1, 0, 0), unselected) == 0

    kernel_square_checks = 0
    prime_mod4_checks = 0
    whole_identity_checks = 0
    transfer_checks = 0
    min_piece_checks = 0

    for m in range(2, 100):
        for n in range(1, m):
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            E = m * m + n * n
            e = odd_squareclass_kernel(E)
            # By construction E/e has even odd-prime valuations.
            odd_part_ratio = E // e
            for p, exp in factor_with_exp(odd_part_ratio):
                if p != 2:
                    assert exp % 2 == 0
            kernel_square_checks += 1

            for p in prime_factors(e):
                assert p % 4 == 1
                prime_mod4_checks += 1

            e23 = 1
            e0 = 1
            for idx, p in enumerate(prime_factors(e)):
                if idx % 2:
                    e0 *= p
                else:
                    e23 *= p
            assert e23 * e0 == e
            assert min(e23, e0) <= isqrt(e) + 1
            assert isqrt(e) <= isqrt(E)
            min_piece_checks += 1

            forms = {
                "m": m,
                "n": n,
                "m-n": m - n,
                "m+n": m + n,
            }
            for name, val in forms.items():
                for u in prime_factors(val):
                    if u == 2:
                        continue
                    assert gcd(u, e) == 1
                    lhs = jacobi_odd(u, e)
                    rhs = 1 if name in ("m", "n") else jacobi_odd(2, u)
                    assert lhs == rhs
                    whole_identity_checks += 1
                    if e23 > 1 and e0 > 1:
                        assert jacobi_odd(u, e23) == lhs * jacobi_odd(u, e0)
                        assert jacobi_odd(u, e0) == lhs * jacobi_odd(u, e23)
                        transfer_checks += 2

    eta = Fraction(1, 100)
    assert eta / 2 == Fraction(1, 200)
    assert 22 * eta == Fraction(11, 50)
    assert 1 + 44 * eta == Fraction(36, 25)
    assert 66 * eta == Fraction(33, 50)
    assert Fraction(36, 25) < 2
    assert Fraction(33, 50) < 2

    kappa = Fraction(1, 100)
    top_b = 1 - kappa
    top_a = Fraction(1, 2) - kappa
    max_outside = Fraction(0, 1)
    # 1/200 grid contains both declared boundaries exactly.
    for ai in range(201):
        a = Fraction(ai, 200)
        for bi in range(201):
            b = Fraction(bi, 200)
            dexp = a + b + 1 - max(a, b / 2)
            in_top = b > top_b and a > top_a
            if not in_top:
                max_outside = max(max_outside, dexp)
                assert dexp <= 2 - kappa
    assert max_outside == 2 - kappa

    decision = summary["decision"]
    assert decision["AUXILIARY_INCIDENCE_UNIFORMITY_PROVED"] is True
    assert decision["E_ODD_STATE_PIECE_COUNT_MAX"] == 2
    assert decision["SPLIT_E_INTERNAL_RECIPROCAL_EDGE"] is False
    assert decision["WHOLE_E_SPLIT_EDGE_TRANSFER_EXACT"] is True
    assert decision["K5_BULK_SAVING_EXPONENT"] == "1/200"
    assert decision["BALANCED_SPLIT_E_TOP_STRIP_DISPERSION_PROVED"] is False
    assert decision["CONDITIONAL_RECIPROCAL_EXPONENT_FORMULA"] == "min(1/200,delta_top)"

    print(f"kernel_square_checks={kernel_square_checks}")
    print(f"prime_mod4_checks={prime_mod4_checks}")
    print(f"whole_identity_checks={whole_identity_checks}")
    print(f"transfer_checks={transfer_checks}")
    print(f"min_piece_checks={min_piece_checks}")
    print(f"max_outside_top_strip_exponent={max_outside}")
    print(json.dumps(decision, indent=2))


if __name__ == "__main__":
    main()
