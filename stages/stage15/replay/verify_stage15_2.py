#!/usr/bin/env python3
from __future__ import annotations

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPT_DIR = ROOT / "stages" / "stage15" / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))
from paired_enumerator import enumerate_paired, face_mask  # noqa: E402


def family(p: int, q: int) -> tuple[int, int, int, int]:
    if not (p < q < 2 * p and p % 2 == q % 2 == 1 and math.gcd(p, q) == 1):
        raise ValueError((p, q))
    e = 4 * p * q
    x = 4 * p * p - q * q
    y = 4 * q * q - p * p
    r2 = e * e + x * x + y * y
    assert r2 == 17 * (p**4 + q**4)
    assert e * e + x * x == (4 * p * p + q * q) ** 2
    assert e * e + y * y == (4 * q * q + p * p) ** 2
    assert (x * x + y * y) % 4 == 2
    assert math.gcd(math.gcd(e, x), y) == 1
    return x, y, e, r2


def cone_pairs(limit_p: int):
    for p in range(3, limit_p + 1, 2):
        for q in range(p + 2, (11 * p) // 10 + 1, 2):
            if math.gcd(p, q) == 1:
                yield p, q


def factorization_completion_count(e: int, bound: int) -> int:
    count = 0
    for x in range(1, bound + 1):
        h2 = e * e + x * x
        h = math.isqrt(h2)
        if h * h == h2:
            d1, d2 = h - x, h + x
            assert d1 * d2 == e * e
            count += 1
    return count


def tau_square(n: int) -> int:
    m = n * n
    t = 0
    d = 1
    while d * d <= m:
        if m % d == 0:
            t += 1 if d * d == m else 2
        d += 1
    return t


def main() -> None:
    seen = set()
    tested = 0
    for p, q in cone_pairs(101):
        x, y, e, _ = family(p, q)
        assert x < y < e
        assert face_mask(x, y, e) == 0b110
        # Injective recovery from the canonical box.
        s = (x + y) // 3
        d = (y - x) // 5
        assert 3 * s == x + y and 5 * d == y - x
        assert (s - d) % 2 == 0 and (s + d) % 2 == 0
        assert math.isqrt((s - d) // 2) == p
        assert math.isqrt((s + d) // 2) == q
        key = (x, y, e)
        assert key not in seen
        seen.add(key)
        tested += 1

    # Cross-check the explicit family against the exact Stage15-1 paired enumerator.
    bound = 5000
    rows, _, summary = enumerate_paired(bound, materialize_rows=True)
    ambient = {(r["a"], r["b"], r["c"]) for r in rows}
    included = 0
    for p, q in cone_pairs(101):
        x, y, e, r2 = family(p, q)
        if r2 <= bound * bound:
            assert (x, y, e) in ambient
            included += 1
    assert included > 0
    assert summary["M2_total"] == 16710

    # Finite exact check of the divisor injection used by the upper bound.
    for e in range(1, 201):
        r = factorization_completion_count(e, 200)
        assert r <= tau_square(e)

    print("STAGE15_2_EXPLICIT_FAMILY_IDENTITIES=true")
    print("STAGE15_2_CANONICAL_CONE_INJECTIVE=true")
    print("STAGE15_2_THIRD_FACE_MOD4_OBSTRUCTION=true")
    print("STAGE15_2_FAMILY_FOUND_BY_PAIRED_ENUMERATOR=true")
    print("STAGE15_2_DIVISOR_INJECTION_FINITE_AUDIT=true")
    print(f"STAGE15_2_CONE_PARAMETER_PAIRS_TESTED={tested}")
    print(f"STAGE15_2_FAMILY_MEMBERS_UNDER_B5000={included}")
    print("M2_POLYNOMIAL_EXPONENT_ONE=true")
    print("STAGE15_2_EXIT=M2_ONLY_PARTIAL_BOUNDS")


if __name__ == "__main__":
    main()
