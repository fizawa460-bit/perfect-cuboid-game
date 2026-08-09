#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def rad_odd(n: int) -> int:
    n = abs(n)
    while n % 2 == 0 and n:
        n //= 2
    r = 1
    p = 3
    while p * p <= n:
        if n % p == 0:
            r *= p
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        r *= n
    return r


def rad_all(n: int) -> int:
    n = abs(n)
    r = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            r *= p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        r *= n
    return r


def squarefree_divisors(r: int):
    ps = []
    x = r
    p = 3
    while p * p <= x:
        if x % p == 0:
            ps.append(p)
            while x % p == 0:
                x //= p
        p += 2
    if x > 1:
        ps.append(x)
    for mask in range(1 << len(ps)):
        d = 1
        for i, p in enumerate(ps):
            if mask >> i & 1:
                d *= p
        yield d


def omega(n: int) -> int:
    return sum(1 for p in prime_factors(n))


def prime_factors(n: int):
    n = abs(n)
    p = 2
    while p * p <= n:
        if n % p == 0:
            yield p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        yield n


def roots_mod_prime(A: int, B: int, p: int):
    # Unit-slope cover for A*x^2 == B*y^2 (mod p).
    roots = [r for r in range(1, p) if (A * r * r - B) % p == 0]
    if roots:
        return roots
    # In the non-residue case the only true solution is (0,0); any unit line covers it.
    return [1]


def crt_pair(a1: int, m1: int, a2: int, m2: int) -> int:
    assert math.gcd(m1, m2) == 1
    return (a1 + ((a2 - a1) * pow(m1, -1, m2) % m2) * m1) % (m1 * m2)


def cover_slopes(A: int, B: int, q: int):
    assert q % 2 == 1
    ps = list(prime_factors(q))
    assert math.prod(ps) == q
    slopes = [(0, 1)]
    for p in ps:
        rs = roots_mod_prime(A % p, B % p, p)
        nxt = []
        for old, mod in slopes:
            for r in rs:
                nxt.append((crt_pair(old, mod, r, p), mod * p))
        slopes = nxt
    return [r % q for r, mod in slopes]


def audit_line_cover():
    cases = 0
    for q in [3, 5, 7, 15, 21, 35, 105]:
        for A in range(1, q):
            if math.gcd(A, q) != 1:
                continue
            for B in range(1, q):
                if math.gcd(B, q) != 1:
                    continue
                slopes = cover_slopes(A, B, q)
                assert len(slopes) <= 2 ** omega(q)
                for x in range(q):
                    for y in range(q):
                        if (A * x * x - B * y * y) % q == 0:
                            assert any((x - r * y) % q == 0 for r in slopes)
                cases += 1
    return cases


def audit_rectangle_shape():
    checks = 0
    for q in [3, 5, 7, 15, 21, 35]:
        for r in range(1, q):
            if math.gcd(r, q) != 1:
                continue
            for U in [2, 3, 5, 8, 13, 21]:
                for V in [2, 4, 7, 11, 17]:
                    n = sum(1 for x in range(1, U + 1) for y in range(1, V + 1)
                            if (x - r * y) % q == 0)
                    # A safe explicit version of UV/q + min(U,V) + 1.
                    rhs = U * V / q + min(U, V) + 1
                    assert n <= math.ceil(rhs)
                    checks += 1
    return checks


def audit_full_radical_divisibility():
    checks = 0
    for m in range(2, 30):
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            # Both orientations occur in the project; only pairwise coprimality matters here.
            S = 2 * m * n
            X = m * m - n * n
            H = m * m + n * n
            assert S * S + X * X == H * H
            RS, RX, RH = rad_odd(S), rad_odd(X), rad_odd(H)
            assert math.gcd(RS, RX) == math.gcd(RS, RH) == math.gcd(RX, RH) == 1
            for a in squarefree_divisors(RS):
                assert S % a == 0
                assert (a * (S // a) ** 2) % RS == 0
                checks += 1
            for b in squarefree_divisors(RX):
                assert X % b == 0
                assert (b * (X // b) ** 2) % RX == 0
                checks += 1
            for c in squarefree_divisors(RH):
                assert H % c == 0
                assert (c * (H // c) ** 2) % RH == 0
                checks += 1
    return checks


def audit_short_transfer():
    checks = 0
    taus = [-2, -1, 1, 2]
    for H in range(5, 80, 2):
        for a in [1, 3, 5, 7]:
            if a > H:
                continue
            for b in [1, 3, 5, 7]:
                if b > H:
                    continue
                for c in [1, 3, 5, 7]:
                    if c > H or H % c:
                        continue
                    for t1, t2 in itertools.product(taus, repeat=2):
                        for u1 in range(1, 8):
                            for u2 in range(1, 8):
                                lhs = abs(t2 * b * u2 * u2 - t1 * a * u1 * u1)
                                # If this tuple happens to satisfy H^2 D^2/c = lhs exactly,
                                # verify the theorem D <= 2*max(u1,u2).
                                num = lhs * c
                                if num == 0:
                                    continue
                                d = math.isqrt(num)
                                if d * d == num and d % H == 0:
                                    D = d // H
                                    if D > 0:
                                        assert D <= 2 * max(u1, u2)
                                        checks += 1
    return checks


def audit_radical_poor_finite():
    # Finite diagnostic only; theorem is proved analytically in result.md.
    B = 20000
    out = {}
    for rho_num, rho_den in [(1, 4), (1, 3), (1, 2)]:
        R = int(B ** (rho_num / rho_den))
        cnt = sum(1 for n in range(1, B + 1) if rad_all(n) <= R)
        out[f"{rho_num}/{rho_den}"] = {"R": R, "count": cnt}
    return out


def audit_upstream_flags():
    required = {
        "stages/stage14/14-4bi-L/result.md": [
            "STAGE14_4BI_L=COMPOSITE_EDGE_KERNEL_INCIDENCE_AND_LARGE_KERNEL_DICHOTOMY_CLOSED",
            "ARBITRARY_LARGE_KERNEL_REMAINDER_OPEN=false",
        ],
        "stages/stage14/14-s6-01/result.md": [
            "ODD_KERNEL_EDGE_PACKET_FACTORIZATION=true",
            "FIXED_PACKET_TWO_QUADRIC_SYSTEM_EXACT=true",
        ],
        "stages/stage14/14-s6-02/result.md": [
            "FIXED_PACKET_SMOOTH_GENUS_ONE_PROVED=true",
            "FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false",
        ],
    }
    for rel, flags in required.items():
        text = (ROOT / rel).read_text()
        for flag in flags:
            assert flag in text, (rel, flag)


def main():
    audit_upstream_flags()
    radical_checks = audit_full_radical_divisibility()
    line_cases = audit_line_cover()
    rectangle_checks = audit_rectangle_shape()
    short_checks = audit_short_transfer()
    radical_diag = audit_radical_poor_finite()

    assert Fraction(41, 42) - Fraction(1, 2) == Fraction(10, 21)

    summary_path = ROOT / "stages/stage14/data/14-4/radical_smallD_core_summary.json"
    summary = json.loads(summary_path.read_text())
    assert summary["claims"]["FULL_ODD_EDGE_RADICAL_CONGRUENCES_PROVED"] is True
    assert summary["claims"]["SMALL_KERNEL_INTRINSIC_MODULUS_OBSTRUCTION"] is False
    assert summary["claims"]["S_ROUTE_GLOBAL_POSITIVE_SAVING_PROVED"] is False
    assert summary["exponents"]["required_post_local_saving"] == "10/21"

    print(f"FULL_RADICAL_DIVISIBILITY_CHECKS={radical_checks}")
    print(f"CRT_LINE_COVER_CASES={line_cases}")
    print(f"RECTANGLE_SHAPE_CHECKS={rectangle_checks}")
    print(f"SHORT_TRANSFER_EXACT_HITS={short_checks}")
    print("RADICAL_POOR_FINITE_DIAGNOSTIC=" + json.dumps(radical_diag, sort_keys=True))
    print("FULL_ODD_EDGE_RADICAL_CONGRUENCE_AUDIT=true")
    print("SMALL_KERNEL_INTRINSIC_MODULUS_OBSTRUCTION=false")
    print("POST_LOCAL_REQUIRED_DELTA=10/21")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
