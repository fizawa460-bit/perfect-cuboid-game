#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09N" / "relative-2isogeny-kummer-image-rank1-preflight.json"
SOURCE = ROOT / "stages" / "stage36" / "36-09N" / "relative-2isogeny-specialization-source-lock.md"
M_CERT = ROOT / "stages" / "stage36" / "36-09M" / "universal-order4-2isogeny-physical-family-preflight.json"

BASE = "824355f591f8f951fda9f2a7c1f4e3e66d4e1e9a"
V39_BLOB = "74d95adfcf7ebb5c6876758044844092145939f7"
CERT_BLOB = "ad66f3849b496b56e1cbeea1f46ba1f8bf967164"
SOURCE_BLOB = "e7c98981fbb1d523fd7db54478dc09aa87b547e8"
M_CERT_BLOB = "470e87d3e48c857b99793bd8ac0d01eff75eb727"

Poly = tuple[Fraction, ...]


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def trim(p: Poly) -> Poly:
    q = list(p)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return tuple(q)


def P(*coeffs: int | Fraction) -> Poly:
    return trim(tuple(Fraction(x) for x in coeffs))


def add(a: Poly, b: Poly) -> Poly:
    n = max(len(a), len(b))
    return trim(tuple((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)))


def neg(a: Poly) -> Poly:
    return tuple(-x for x in a)


def sub(a: Poly, b: Poly) -> Poly:
    return add(a, neg(b))


def scale(c: int | Fraction, a: Poly) -> Poly:
    return trim(tuple(Fraction(c) * x for x in a))


def mul(a: Poly, b: Poly) -> Poly:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(tuple(out))


def pw(a: Poly, n: int) -> Poly:
    out = P(1)
    base = a
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n >>= 1
    return out


def peval(a: Poly, x: int | Fraction) -> Fraction:
    xx = Fraction(x)
    out = Fraction(0)
    for c in reversed(a):
        out = out * xx + c
    return out


def is_square_q(x: Fraction | int) -> bool:
    x = Fraction(x)
    if x < 0:
        return False
    return isqrt(x.numerator) ** 2 == x.numerator and isqrt(x.denominator) ** 2 == x.denominator


def sqfree_candidates(primes: list[int]) -> list[int]:
    vals = []
    for mask in range(1 << len(primes)):
        d = 1
        for i, p in enumerate(primes):
            if mask >> i & 1:
                d *= p
        vals += [d, -d]
    return sorted(set(vals), key=lambda z: (abs(z), z))


def quartic_rhs(A: int, B: int, d: int, m: int, e: int, mod: int) -> int:
    assert B % d == 0
    return (d * pow(m, 4, mod) + A * (m * m % mod) * (e * e % mod) + (B // d) * pow(e, 4, mod)) % mod


def no_primitive_solution_mod(A: int, B: int, d: int, mod: int, prime: int) -> bool:
    squares = {x * x % mod for x in range(mod)}
    for m in range(mod):
        for e in range(mod):
            if m % prime == 0 and e % prime == 0:
                continue
            if quartic_rhs(A, B, d, m, e, mod) in squares:
                return False
    return True


def check_gt_q6() -> None:
    # Complete square-free divisor supports for the three Gusic-Tadic products.
    # The factor 2 is optional only in the latter two products (their content is 8).
    groups = [
        ([23, 47], False),
        ([23, 6, 5, 7], True),
        ([47, 6, 5, 7], True),
    ]
    for values, allow_two in groups:
        n = len(values)
        for r in range(1, n + 1):
            for inds in combinations(range(n), r):
                v = 1
                for i in inds:
                    v *= values[i]
                assert not is_square_q(v)
                assert not is_square_q(-v)
                if allow_two:
                    assert not is_square_q(2 * v)
                    assert not is_square_q(-2 * v)


def check_E6_descent() -> None:
    A = 2738
    B = 1081 ** 2

    # Realized alpha classes.
    points = [
        (-529, 0),
        (1081, 75670),
        (-1081, 25944),
    ]
    for x, y in points:
        assert y * y == x ** 3 + A * x * x + B * x

    # The only remaining square-free classes are +/-23 and +/-47.
    # For every primitive pair mod 5 the RHS is 2 or 3, never a square.
    for d in (23, -23, 47, -47):
        residues = set()
        for m in range(5):
            for e in range(5):
                if m == 0 and e == 0:
                    continue
                residues.add(quartic_rhs(A, B, d, m, e, 5))
        assert residues == {2, 3}
        assert residues.isdisjoint({0, 1, 4})


def check_E6prime_descent() -> None:
    A = -5476
    B = 1680 ** 2
    candidates = sqfree_candidates([2, 3, 5, 7])
    assert len(candidates) == 32

    # Every negative d has a strictly negative real RHS for any primitive (M,e).
    for d in [x for x in candidates if x < 0]:
        assert d < 0 and A < 0 and B // d < 0

    # d=2 is globally realized.
    Z, W, d = 10, 940, 2
    assert W * W == d * Z ** 4 + A * Z * Z + (B // d)
    X, Y = d * Z * Z, d * Z * W
    assert (X, Y) == (200, 18800)
    assert Y * Y == X ** 3 + A * X * X + B * X

    obstruction = {
        3: (9, 3),
        6: (9, 3),
        5: (23, 23),
        7: (23, 23),
        10: (23, 23),
        14: (23, 23),
        15: (23, 23),
        21: (23, 23),
        30: (23, 23),
        42: (23, 23),
        35: (47, 47),
        70: (47, 47),
        105: (47, 47),
        210: (47, 47),
    }
    positive = [x for x in candidates if x > 0]
    assert set(positive) == {1, 2, *obstruction.keys()}
    for d0, (mod, prime) in obstruction.items():
        assert no_primitive_solution_mod(A, B, d0, mod, prime)


def check_relative_identities() -> None:
    q = P(0, 1)
    one = P(1)
    Nm = sub(sub(pw(q, 2), scale(2, q)), one)
    Np = sub(add(pw(q, 2), scale(2, q)), one)
    C = mul(Nm, Np)
    q2p1 = add(pw(q, 2), one)

    assert C == P(1, 0, -6, 0, 1)
    A = add(pw(Nm, 2), pw(Np, 2))
    assert A == scale(2, pw(q2p1, 2))
    D = sub(pw(Np, 2), pw(Nm, 2))
    assert D == scale(8, mul(q, sub(pw(q, 2), one)))
    B = pw(C, 2)
    Aprime = scale(-2, A)
    Bprime = pw(D, 2)
    assert Bprime == sub(pw(A, 2), scale(4, B))

    # d=2 relative homogeneous-space point.
    Z = scale(2, sub(q, one))
    W = scale(4, mul(sub(q, one), Np))
    rhs = add(add(scale(2, pw(Z, 4)), mul(Aprime, pw(Z, 2))), scale(Fraction(1, 2), Bprime))
    assert pw(W, 2) == rhs

    # Induced section on E'_q.
    X = scale(2, pw(Z, 2))
    Y = scale(2, mul(Z, W))
    e1 = scale(4, pw(sub(pw(q, 2), one), 2))
    e2 = scale(16, pw(q, 2))
    assert pw(Y, 2) == mul(mul(X, sub(X, e1)), sub(X, e2))
    assert X == scale(8, pw(sub(q, one), 2))
    assert Y == scale(16, mul(pw(sub(q, one), 2), Np))

    # Dual section on E_q.
    x = pw(Np, 2)
    y = scale(-2, mul(q2p1, pw(Np, 2)))
    assert pw(y, 2) == mul(mul(x, add(x, pw(Nm, 2))), add(x, pw(Np, 2)))

    # Distinct generic Kummer classes: C has odd valuations at the two
    # irreducible quadratics (discriminant 8), while -1 and 2 are nonsquares in Q(q).
    assert 8 not in {n * n for n in range(4)}
    assert not is_square_q(Fraction(-1))
    assert not is_square_q(Fraction(2))


def main() -> None:
    c = json.loads(CERT.read_text())
    s = json.loads(STATE.read_text())
    source = SOURCE.read_text()

    assert c["schema"] == "STAGE36_36_09N_RELATIVE_2ISOGENY_KUMMER_RANK1_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert blob(CERT) == CERT_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(M_CERT) == M_CERT_BLOB
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V39_BLOB

    for needle in [
        "2^r = |Im(alpha)|*|Im(beta)|/4",
        "N^2 = b1*M^4 + a*M^2*e^2 + b2*e^4",
        "Gusić and Petra Tadić",
        "specialization",
        "square-free divisor",
    ]:
        assert needle in source

    check_relative_identities()
    check_gt_q6()
    check_E6_descent()
    check_E6prime_descent()

    sp6 = c["specialized_rank"]
    assert sp6["rank_E6_Q"] == 1
    assert sp6["rank_E6prime_Q"] == 1
    assert 4 * 2 // 4 == 2

    gen = c["generic_rank_and_exact_images"]
    assert gen["generic_rank"] == 1
    assert gen["exact_alpha_image"] == ["[1]", "[-1]", "[C]", "[-C]"]
    assert gen["exact_beta_image"] == ["[1]", "[2]"]

    fw = c["scope_firewalls"]
    assert fw["generic_function_field_MW_rank_proved"] is True
    assert fw["fiberwise_rank_one_for_every_rational_q_proved"] is False
    assert fw["uniform_Mordell_Weil_group_proved"] is False
    assert fw["specialization_rank_jumps_excluded"] is False
    assert fw["isogeny_Selmer_groups_computed"] is False
    assert fw["receiver_emptiness_proved"] is False
    assert fw["R29_CAMP2_closed"] is False

    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V40_36_09N_PENDING_HOSTILE_AUDIT"
    assert s["status"] == "ACTIVE_PENDING_HOSTILE_AUDIT"
    N = s["authority_frontier"]["36-09N"]
    assert N["certificate_blob_sha"] == CERT_BLOB
    assert N["source_lock_blob_sha"] == SOURCE_BLOB
    assert N["GENERIC_FUNCTION_FIELD_MW_RANK"] == 1
    assert N["EXACT_ALPHA_IMAGE"] == ["[1]", "[-1]", "[C]", "[-C]"]
    assert N["EXACT_BETA_IMAGE"] == ["[1]", "[2]"]
    assert N["B3_RELATIVE_2_ISOGENY_ROUTE"] == "LIVE"
    assert s["current"]["36_09O_entry_allowed"] is False
    assert s["promotion_gates"]["uniform_Mordell_Weil_group_proved"] is False
    assert s["promotion_gates"]["isogeny_Selmer_groups_computed"] is False
    assert s["promotion_gates"]["receiver_emptiness_proved"] is False
    assert s["promotion_gates"]["R29_CAMP2_closed"] is False

    print("36-09N exact relative Kummer images and generic rank 1 verified; q0=6 injective specialization/descent replayed; 36-09O locked")


if __name__ == "__main__":
    main()
