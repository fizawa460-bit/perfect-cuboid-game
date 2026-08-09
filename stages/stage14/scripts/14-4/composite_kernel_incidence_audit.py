#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4bi-L/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/composite_kernel_incidence_summary.json"
FOUR_BH = ROOT / "stages/stage14/14-4bh/result.md"
S6_01 = ROOT / "stages/stage14/14-s6-01/result.md"
S6_02 = ROOT / "stages/stage14/14-s6-02/result.md"


def require(text: str, needle: str) -> None:
    assert needle in text, f"missing required boundary: {needle}"


def prime_factors(n: int) -> list[int]:
    n = abs(n)
    out: list[int] = []
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


def rad_odd(n: int) -> int:
    r = 1
    for p in prime_factors(n):
        if p != 2:
            r *= p
    return r


def divisors_squarefree_rad(r: int) -> list[int]:
    ps = prime_factors(r)
    out = [1]
    for p in ps:
        out += [d * p for d in list(out)]
    return sorted(set(out))


def omega(n: int) -> int:
    return len(prime_factors(n))


def local_line_slopes(p: int, A: int, B: int) -> list[int]:
    assert math.gcd(A * B, p) == 1
    roots = [r for r in range(p) if (A * r * r - B) % p == 0]
    if roots:
        return roots
    # If B/A is a nonresidue, the exact solution set is only (0,0).
    # The line x=0 is a valid one-line upper cover.
    return [0]


def covered_mod_q(q: int, A: int, B: int, x: int, y: int) -> bool:
    for p in prime_factors(q):
        slopes = local_line_slopes(p, A % p, B % p)
        if not any((x - r * y) % p == 0 for r in slopes):
            return False
    return True


def exact_congruence_count(q: int, A: int, B: int, U: int, V: int) -> int:
    return sum(
        1
        for x in range(1, U + 1)
        for y in range(1, V + 1)
        if (A * x * x - B * y * y) % q == 0
    )


def audit_composite_line_cover() -> None:
    moduli = [3, 5, 7, 15, 21, 35, 105]
    for q in moduli:
        assert q % 2 == 1
        assert all(q % (p * p) != 0 for p in prime_factors(q))
        for A in range(1, min(q, 12)):
            for B in range(1, min(q, 12)):
                if math.gcd(A * B, q) != 1:
                    continue
                line_count = 1
                for p in prime_factors(q):
                    line_count *= len(local_line_slopes(p, A % p, B % p))
                assert line_count <= 2 ** omega(q)

                # Every exact residue solution is covered by one local line at every p|q.
                for x in range(q):
                    for y in range(q):
                        if (A * x * x - B * y * y) % q == 0:
                            assert covered_mod_q(q, A, B, x, y)

                # Finite regression for the rectangle shape; the theorem uses an
                # implicit absolute constant, so keep a deliberately generous one.
                for U, V in [(3, 4), (5, 11), (9, 6), (17, 13)]:
                    n = exact_congruence_count(q, A, B, U, V)
                    shape = (U * V / q) + min(U, V) + 1
                    assert n <= 4 * (2 ** omega(q)) * shape


def audit_edge_normalization_and_short_transfer() -> None:
    # Primitive opposite-parity Euclid pairs; here S=2mn, X=m^2-n^2.
    pairs = [(2, 1), (3, 2), (4, 1), (4, 3), (5, 2), (5, 4), (6, 1), (7, 2)]
    tau_values = [-2, -1, 1, 2]

    for m, n in pairs:
        if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
            continue
        S = 2 * m * n
        X = m * m - n * n
        H = m * m + n * n
        assert S * S + X * X == H * H

        As = divisors_squarefree_rad(rad_odd(S))
        Bs = divisors_squarefree_rad(rad_odd(X))
        Cs = divisors_squarefree_rad(rad_odd(H))

        for a in As:
            assert S % a == 0
            assert S * S // a == a * (S // a) ** 2
        for b in Bs:
            assert X % b == 0
            assert X * X // b == b * (X // b) ** 2
        for c in Cs:
            assert H % c == 0
            assert H * H // c == c * (H // c) ** 2

        # Check the coefficient inequality behind D <= 2 U_* on every max edge.
        for a in As:
            for b in Bs:
                for c in Cs:
                    assert math.gcd(a, b) == math.gcd(a, c) == math.gcd(b, c) == 1
                    K = max(a, b, c)
                    for u0, u1, u2 in [(1, 2, 3), (4, 1, 2), (3, 5, 2)]:
                        for t0 in tau_values:
                            for t1 in tau_values:
                                for t2 in tau_values:
                                    if K == a:
                                        lhs = abs(t0 * b * u0 * u0 - t1 * c * u1 * u1)
                                        assert lhs <= 2 * K * (u0 * u0 + u1 * u1)
                                    if K == b:
                                        lhs = abs(t2 * c * u2 * u2 - t0 * a * u0 * u0)
                                        assert lhs <= 2 * K * (u2 * u2 + u0 * u0)
                                    if K == c:
                                        lhs = abs(t2 * b * u2 * u2 - t1 * a * u1 * u1)
                                        assert lhs <= 2 * K * (u2 * u2 + u1 * u1)


def main() -> None:
    result = RESULT.read_text()
    summary = json.loads(SUMMARY.read_text())
    four_bh = FOUR_BH.read_text()
    s6_01 = S6_01.read_text()
    s6_02 = S6_02.read_text()

    require(four_bh, "STAGE14_4BH=TWO_QUADRIC_GENUS_ONE_GEOMETRY_AND_LARGE_KERNEL_INCIDENCE_SPLIT")
    require(s6_01, "ODD_KERNEL_EDGE_PACKET_FACTORIZATION=true")
    require(s6_01, "TWO_ADIC_SIGN_PACKET_COUNT=16")
    require(s6_02, "STAGE14_S6_02=COMPLETE_GENUS_ONE_PACKET_GEOMETRY_AND_LARGE_PRIME_INCIDENCE_SECTOR")
    require(s6_02, "EDGE_LINE_RECTANGLE_BOUND_PROVED=true")

    # Exact exponent contract inherited by the split.
    assert Fraction(41, 42) - Fraction(1, 2) == Fraction(10, 21)
    kappa = Fraction(1, 9)
    upsilon = Fraction(1, 7)
    assert min(kappa, upsilon) == Fraction(1, 9)

    audit_composite_line_cover()
    audit_edge_normalization_and_short_transfer()

    dichotomy = summary["large_kernel_dichotomy"]
    assert dichotomy["K"] == "max(a,b,c)"
    assert dichotomy["long_incident"]["relative_gain"] == "B^(-min(kappa,upsilon)+epsilon)"
    assert dichotomy["short_incident"]["consequence"] == "D < 2*B^upsilon"

    flags = summary["flags"]
    expected_true = [
        "S6_01_EDGE_PACKET_FACTORIZATION_IMPORTED",
        "S6_02_PRIME_LEVEL_INCIDENCE_IMPORTED",
        "COMPOSITE_EDGE_KERNEL_NORMALIZATION_EXACT",
        "COMPOSITE_EDGE_RECTANGLE_BOUND_PROVED",
        "SMOOTH_LARGE_EDGE_KERNEL_INCIDENCE_CLOSED",
        "LARGEST_KERNEL_SHORT_INCIDENT_IMPLIES_D_LE_2_USTAR",
        "LARGE_KERNEL_SHORT_INCIDENT_TRANSFERS_TO_SMALL_DENOMINATOR",
        "S_ROUTE_RECEIVES_SMALL_KERNEL_OR_SMALL_DENOMINATOR",
    ]
    for key in expected_true:
        assert flags[key] is True, key
    assert flags["ARBITRARY_LARGE_KERNEL_REMAINDER_OPEN"] is False
    assert flags["FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED"] is False
    assert flags["SQRT_B_UPPER_BOUND_PROVED"] is False

    require(result, "STAGE14_4BI_L=COMPOSITE_EDGE_KERNEL_INCIDENCE_AND_LARGE_KERNEL_DICHOTOMY_CLOSED")
    require(result, "SMOOTH_LARGE_EDGE_KERNEL_INCIDENCE_CLOSED=true")
    require(result, "LARGEST_KERNEL_SHORT_INCIDENT_IMPLIES_D_LE_2_USTAR=true")
    require(result, "ARBITRARY_LARGE_KERNEL_REMAINDER_OPEN=false")
    require(result, "FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false")
    require(result, "NEXT=Stage14-4bj after 14-4bi-S")

    print("STAGE14_4BI_L_AUDIT=PASS")
    print("composite_modulus=edge_kernel_a_b_or_c")
    print("line_multiplicity<=2^omega(kernel)")
    print("long_gain=B^(-min(kappa,upsilon)+epsilon)")
    print("short_transfer=D<2*B^upsilon")
    print("sqrt_remaining=10/21")


if __name__ == "__main__":
    main()
