#!/usr/bin/env python3
"""Stage14-4bc deterministic audit.

Regression-locks the s5p imports, split-H/E support algebra, whole-E
squareclass transfer, K5 exponent ledger, and top-strip exponent boundary.
"""

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
    out = 1
    for p, e in factor_with_exp(n):
        if p != 2 and e % 2:
            out *= p
    return out


def jacobi_odd(a: int, n: int) -> int:
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


def main() -> None:
    result = RESULT.read_text()
    supplement = SUPPLEMENT.read_text()
    bb = FOUR_BB.read_text()
    s5p = S5P.read_text()
    s5c = S5C.read_text()
    s5d = S5D.read_text()
    summary = json.loads(SUMMARY.read_text())

    # Imported theorem locks.
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

    # Boundary/result locks.
    for flag in (
        "AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true",
        "SPLIT_E_INTERNAL_RECIPROCAL_EDGE=false",
        "WHOLE_E_SPLIT_EDGE_TRANSFER_EXACT=true",
        "RECIPROCAL_ACTIVE_E_PIECE_CAN_BE_CHOSEN_LE_M=true",
        "SPLIT_E_DENSITY_COMPLETION_LEMMA_PROVED=true",
        "K5_SEPARABLE_E_GRAPH_BULK_ASSEMBLED=true",
        "BALANCED_SPLIT_E_TOP_STRIP_TENSOR_PROVED=false",
        "CONDITIONAL_RECIPROCAL_EXPONENT_FORMULA=min(1/200,delta_top)",
    ):
        assert flag in result
    assert "L(s,chi)L(s,chi*chi_4)G(s)" in supplement

    # Exact F2 support algebra for the H column: no internal E--E edge.
    selected_h = (0, 1, 1)
    unselected_h = (0, 0, 0)
    for row in ((0, 1, 1), (1, 0, 0)):
        assert dot2(row, selected_h) == 0
        assert dot2(row, unselected_h) == 0
    unselected_h_row = (1, 0, 0)
    assert dot2(unselected_h_row, selected_h) == 0
    assert dot2(unselected_h_row, unselected_h) == 0

    kernel_checks = 0
    split_prime_checks = 0
    whole_identity_checks = 0
    transfer_checks = 0
    smaller_piece_checks = 0

    # Finite exact checks over primitive opposite-parity Euclid pairs.
    for m in range(2, 110):
        for n in range(1, m):
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            E = m * m + n * n
            e = odd_squareclass_kernel(E)

            # E/e has even valuation at every odd prime.
            ratio = E // e
            for p, exponent in factor_with_exp(ratio):
                if p != 2:
                    assert exponent % 2 == 0
            kernel_checks += 1

            # Every odd prime in the norm squareclass kernel is split.
            for p in prime_factors(e):
                assert p % 4 == 1
                split_prime_checks += 1

            # Arbitrary deterministic two-piece split; only coprimality and
            # product are needed for the Jacobi transfer identity.
            e23 = 1
            e0 = 1
            for idx, p in enumerate(prime_factors(e)):
                if idx % 2:
                    e0 *= p
                else:
                    e23 *= p
            assert e23 * e0 == e and gcd(e23, e0) == 1
            assert min(e23, e0) <= isqrt(e) + 1
            assert isqrt(e) <= isqrt(E)
            smaller_piece_checks += 1

            forms = {
                "m": m,
                "n": n,
                "m-n": m - n,
                "m+n": m + n,
            }
            for name, value in forms.items():
                for u in prime_factors(value):
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

    # K5 exponent ledger, eta=1/100.
    eta = Fraction(1, 100)
    assert eta / 2 == Fraction(1, 200)
    assert eta == Fraction(1, 100)
    active_short_modulus = 22 * eta
    assert active_short_modulus == Fraction(11, 50)
    periodic_first = 1 + 2 * active_short_modulus
    periodic_second = 3 * active_short_modulus
    assert periodic_first == Fraction(36, 25)
    assert periodic_second == Fraction(33, 50)
    assert periodic_first < 2 and periodic_second < 2

    # Exact top-strip exponent implication on a grid containing both borders.
    kappa = Fraction(1, 100)
    top_a = Fraction(49, 100)
    top_b = Fraction(99, 100)
    max_outside = Fraction(0, 1)
    for ai in range(201):
        a = Fraction(ai, 200)
        for bi in range(201):
            b = Fraction(bi, 200)
            dexp = a + b + 1 - max(a, b / 2)
            inside_top = a > top_a and b > top_b
            if not inside_top:
                max_outside = max(max_outside, dexp)
                assert dexp <= 2 - kappa
    assert max_outside == Fraction(199, 100)

    decision = summary["decision"]
    assert decision["AUXILIARY_INCIDENCE_UNIFORMITY_PROVED"] is True
    assert decision["E_ODD_STATE_PIECE_COUNT_MAX"] == 2
    assert decision["SPLIT_E_INTERNAL_RECIPROCAL_EDGE"] is False
    assert decision["WHOLE_E_SPLIT_EDGE_TRANSFER_EXACT"] is True
    assert decision["K5_BULK_SAVING_EXPONENT"] == "1/200"
    assert decision["BALANCED_SPLIT_E_TOP_STRIP_TENSOR_PROVED"] is False
    assert decision["CONDITIONAL_RECIPROCAL_EXPONENT_FORMULA"] == "min(1/200,delta_top)"
    assert decision["CLOSED_RECIPROCAL_B_SCALE_ERROR_EXPONENT"] == "399/400"

    print(f"kernel_checks={kernel_checks}")
    print(f"split_prime_checks={split_prime_checks}")
    print(f"whole_identity_checks={whole_identity_checks}")
    print(f"transfer_checks={transfer_checks}")
    print(f"smaller_piece_checks={smaller_piece_checks}")
    print(f"max_outside_top_strip_exponent={max_outside}")
    print(json.dumps(decision, indent=2))


if __name__ == "__main__":
    main()
