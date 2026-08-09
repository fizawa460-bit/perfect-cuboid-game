#!/usr/bin/env python3
"""Stage14-4bc deterministic audit."""

import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4bc/result.md"
SUPPLEMENT = ROOT / "stages/stage14/14-4bc/e-density-completion.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/aux_uniform_e_top_strip_summary.json"
FOUR_BB = ROOT / "stages/stage14/14-4bb/result.md"
S5P = ROOT / "stages/stage14/14-s5p/result.md"
S5C = ROOT / "stages/stage14/14-s5c/result.md"
S5D = ROOT / "stages/stage14/14-s5d/result.md"


def factor_with_exp(n):
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


def prime_factors(n):
    return [p for p, _ in factor_with_exp(n)]


def odd_squareclass_kernel(n):
    r = 1
    for p, e in factor_with_exp(n):
        if p != 2 and e % 2:
            r *= p
    return r


def jacobi_odd(a, n):
    if n == 1:
        return 1
    assert n > 0 and n % 2 and gcd(a, n) == 1
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


def main():
    result = RESULT.read_text()
    supplement = SUPPLEMENT.read_text()
    bb = FOUR_BB.read_text()
    s5p = S5P.read_text()
    s5c = S5C.read_text()
    s5d = S5D.read_text()
    summary = json.loads(SUMMARY.read_text())

    assert "K4_GRAPH_ASSEMBLY_SAVING_EXPONENT=1/200" in bb
    for flag in (
        "AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true",
        "AUXILIARY_PROGRESSION_MODULUS_LOSS_PERSISTS=false",
        "E_SIGNED_ROOT_AUX_UNIFORMITY_PROVED=true",
        "AUXILIARY_STATE_ENERGY_TRANSFER_PROVED=true",
        "HILBERT_QUADRATIC_LARGE_SIEVE_LIFT_PROVED=true",
    ):
        assert flag in s5p
    assert ("H / 23" in s5c) or ("H/23" in s5c)
    assert "p|H : chi(d1)=+1" in s5d
    assert "AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true" in result
    assert "BALANCED_SPLIT_E_TOP_STRIP_TENSOR_PROVED=false" in result
    assert "L(s,chi)L(s,chi*chi_4)G(s)" in supplement

    # Same H-column support never creates an E--E reciprocal edge.
    selected_h = (0, 1, 1)
    unselected_h = (0, 0, 0)
    for row in ((0, 1, 1), (1, 0, 0)):
        assert dot2(row, selected_h) == 0
        assert dot2(row, unselected_h) == 0
    assert dot2((1, 0, 0), selected_h) == 0

    kernel_checks = split_checks = identity_checks = transfer_checks = 0
    for m in range(2, 105):
        for n in range(1, m):
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            E = m * m + n * n
            e = odd_squareclass_kernel(E)
            ratio = E // e
            for p, exponent in factor_with_exp(ratio):
                if p != 2:
                    assert exponent % 2 == 0
            kernel_checks += 1
            for p in prime_factors(e):
                assert p % 4 == 1
                split_checks += 1

            e23 = e0 = 1
            for i, p in enumerate(prime_factors(e)):
                if i % 2:
                    e0 *= p
                else:
                    e23 *= p
            assert e23 * e0 == e and gcd(e23, e0) == 1
            assert min(e23, e0) <= isqrt(e) + 1 <= isqrt(E) + 2

            for name, value in {
                "m": m, "n": n, "m-n": m-n, "m+n": m+n
            }.items():
                for u in prime_factors(value):
                    if u == 2:
                        continue
                    assert gcd(u, e) == 1
                    whole = jacobi_odd(u, e)
                    expected = 1 if name in ("m", "n") else jacobi_odd(2, u)
                    assert whole == expected
                    identity_checks += 1
                    if e23 > 1 and e0 > 1:
                        assert jacobi_odd(u, e23) == whole * jacobi_odd(u, e0)
                        assert jacobi_odd(u, e0) == whole * jacobi_odd(u, e23)
                        transfer_checks += 2

    eta = Fraction(1, 100)
    assert eta / 2 == Fraction(1, 200)
    assert 22 * eta == Fraction(11, 50)
    assert 1 + 44 * eta == Fraction(36, 25)
    assert 66 * eta == Fraction(33, 50)

    # Top-strip boundary: outside a>49/100 and b>99/100,
    # D(a,b)=a+b+1-max(a,b/2) never exceeds 199/100.
    max_outside = Fraction(0)
    for ai in range(201):
        a = Fraction(ai, 200)
        for bi in range(201):
            b = Fraction(bi, 200)
            d = a + b + 1 - max(a, b / 2)
            if not (a > Fraction(49, 100) and b > Fraction(99, 100)):
                assert d <= Fraction(199, 100)
                max_outside = max(max_outside, d)
    assert max_outside == Fraction(199, 100)

    decision = summary["decision"]
    assert decision["AUXILIARY_INCIDENCE_UNIFORMITY_PROVED"] is True
    assert decision["E_ODD_STATE_PIECE_COUNT_MAX"] == 2
    assert decision["SPLIT_E_INTERNAL_RECIPROCAL_EDGE"] is False
    assert decision["WHOLE_E_SPLIT_EDGE_TRANSFER_EXACT"] is True
    assert decision["K5_BULK_SAVING_EXPONENT"] == "1/200"
    assert decision["BALANCED_SPLIT_E_TOP_STRIP_TENSOR_PROVED"] is False
    assert decision["CONDITIONAL_RECIPROCAL_EXPONENT_FORMULA"] == "min(1/200,delta_top)"

    print(f"kernel_checks={kernel_checks}")
    print(f"split_checks={split_checks}")
    print(f"identity_checks={identity_checks}")
    print(f"transfer_checks={transfer_checks}")
    print(f"max_outside_top_strip={max_outside}")
    print(json.dumps(decision, indent=2))


if __name__ == "__main__":
    main()
