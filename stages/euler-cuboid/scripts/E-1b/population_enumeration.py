#!/usr/bin/env python3
"""E-1b: enumerate primitive canonical exactly-one-face populations.

Counting convention (locked by E-1a):

    0 < a < b < c,
    gcd(a,b,c)=1,
    a^2+b^2+c^2 <= B^2.

The space diagonal is NOT required to be integral.

For q in {ab, ac, bc}, A_q(B) counts raw incidences where face q has an
integral diagonal.  Pair overlaps and the triple overlap are then removed by
exact inclusion-exclusion:

    N_ab = A_ab - O_ab_ac - O_ab_bc + T
    N_ac = A_ac - O_ab_ac - O_ac_bc + T
    N_bc = A_bc - O_ab_bc - O_ac_bc + T.

The raw counts are generated from Pythagorean face pairs.  Primitivity of the
third edge is counted by inclusion-exclusion over the distinct prime factors
of gcd(x,y), so the script does not scan all O(B^3) canonical triples.
"""
from __future__ import annotations

import argparse
import json
import math
from functools import lru_cache
from pathlib import Path

DEFAULT_CUTOFFS = (100, 200, 500, 1000, 2000, 5000, 10000)
DEFAULT_OUTPUT = Path("stages/euler-cuboid/data/E-1b/population_report.json")
Q = ("ab", "ac", "bc")


def pythagorean_pairs(B: int) -> list[tuple[int, int]]:
    """All positive x<y with x^2+y^2 a square <=B^2."""
    pairs: set[tuple[int, int]] = set()
    m = 2
    while m * m + 1 <= B:
        for n in range(1, m):
            if (m - n) % 2 == 0 or math.gcd(m, n) != 1:
                continue
            h = m * m + n * n
            if h > B:
                continue
            x, y = sorted((m * m - n * n, 2 * m * n))
            for k in range(1, B // h + 1):
                pairs.add((k * x, k * y))
        m += 1
    return sorted(pairs)


def distinct_prime_factors(n: int) -> list[int]:
    out: list[int] = []
    if n % 2 == 0:
        out.append(2)
        while n % 2 == 0:
            n //= 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        out.append(n)
    return out


@lru_cache(maxsize=None)
def squarefree_mu_divisors(g: int) -> tuple[tuple[int, int], ...]:
    """Return (d,mu(d)) for squarefree divisors built from primes dividing g."""
    rows: list[tuple[int, int]] = [(1, 1)]
    for p in distinct_prime_factors(g):
        rows += [(d * p, -mu) for d, mu in tuple(rows)]
    return tuple(rows)


def coprime_upto(n: int, g: int) -> int:
    if n <= 0:
        return 0
    return sum(mu * (n // d) for d, mu in squarefree_mu_divisors(g))


def coprime_interval(lo: int, hi: int, g: int) -> int:
    if hi < lo:
        return 0
    return coprime_upto(hi, g) - coprime_upto(lo - 1, g)


def enumerate_population(B: int) -> dict:
    B2 = B * B
    pairs = pythagorean_pairs(B)
    pairset = set(pairs)
    adjacency: list[list[int]] = [[] for _ in range(B + 1)]
    raw = {q: 0 for q in Q}

    for x, y in pairs:
        adjacency[x].append(y)
        adjacency[y].append(x)
        remaining = B2 - x * x - y * y
        if remaining <= 0:
            continue
        zmax = math.isqrt(remaining)
        g = math.gcd(x, y)

        # q=ab: a=x, b=y, c>y.
        raw["ab"] += coprime_interval(y + 1, zmax, g)
        # q=ac: a=x, c=y, x<b<y.
        raw["ac"] += coprime_interval(x + 1, min(y - 1, zmax), g)
        # q=bc: b=x, c=y, 0<a<x.
        raw["bc"] += coprime_interval(1, min(x - 1, zmax), g)

    overlap = {"ab_ac": 0, "ab_bc": 0, "ac_bc": 0}
    triple: set[tuple[int, int, int]] = set()

    # ab & ac: a is the shared edge; choose a<b<c among upper partners of a.
    for a in range(1, B + 1):
        upper = sorted(v for v in adjacency[a] if v > a)
        for i, b in enumerate(upper):
            for c in upper[i + 1 :]:
                if a * a + b * b + c * c > B2:
                    break
                if math.gcd(math.gcd(a, b), c) != 1:
                    continue
                overlap["ab_ac"] += 1
                if (b, c) in pairset:
                    triple.add((a, b, c))

    # ab & bc: b is the shared edge; choose a<b<c.
    for b in range(1, B + 1):
        lower = [v for v in adjacency[b] if v < b]
        upper = sorted(v for v in adjacency[b] if v > b)
        for a in lower:
            for c in upper:
                if a * a + b * b + c * c > B2:
                    break
                if math.gcd(math.gcd(a, b), c) != 1:
                    continue
                overlap["ab_bc"] += 1
                if (a, c) in pairset:
                    triple.add((a, b, c))

    # ac & bc: c is the shared edge; choose a<b<c among lower partners of c.
    for c in range(1, B + 1):
        lower = sorted(v for v in adjacency[c] if v < c)
        for i, a in enumerate(lower):
            for b in lower[i + 1 :]:
                if a * a + b * b + c * c > B2:
                    break
                if math.gcd(math.gcd(a, b), c) != 1:
                    continue
                overlap["ac_bc"] += 1
                if (a, b) in pairset:
                    triple.add((a, b, c))

    T = len(triple)
    exact = {
        "ab": raw["ab"] - overlap["ab_ac"] - overlap["ab_bc"] + T,
        "ac": raw["ac"] - overlap["ab_ac"] - overlap["ac_bc"] + T,
        "bc": raw["bc"] - overlap["ab_bc"] - overlap["ac_bc"] + T,
    }
    total = sum(exact.values())

    return {
        "B": B,
        "pythagorean_face_pairs": len(pairs),
        "raw_incidence": raw,
        "pair_overlap": overlap,
        "triple_overlap": T,
        "exact_one": exact,
        "exact_one_total": total,
        "proportion": {q: exact[q] / total for q in Q},
        "bc_normalized_ratio": {q: exact[q] / exact["bc"] for q in Q},
    }


def is_square(n: int) -> bool:
    r = math.isqrt(n)
    return r * r == n


def brute_force(B: int) -> dict[str, int]:
    """Small-B validator only."""
    out = {q: 0 for q in Q}
    B2 = B * B
    for a in range(1, B):
        for b in range(a + 1, B):
            ab2 = a * a + b * b
            if ab2 >= B2:
                break
            for c in range(b + 1, B):
                if ab2 + c * c > B2:
                    break
                if math.gcd(math.gcd(a, b), c) != 1:
                    continue
                flags = (
                    is_square(ab2),
                    is_square(a * a + c * c),
                    is_square(b * b + c * c),
                )
                if sum(flags) == 1:
                    out[Q[flags.index(True)]] += 1
    return out


def build_report(cutoffs: tuple[int, ...]) -> dict:
    rows = [enumerate_population(B) for B in cutoffs]
    validation = []
    for B in (20, 30, 50, 80):
        fast = enumerate_population(B)["exact_one"]
        brute = brute_force(B)
        validation.append({"B": B, "fast": fast, "brute": brute, "match": fast == brute})
    assert all(row["match"] for row in validation)

    return {
        "metadata": {
            "stage": "E-1b",
            "scope": "finite primitive canonical exactly-one face population profile",
            "space_diagonal_integrality_required": False,
        },
        "counting_convention": {
            "canonical_order": "0<a<b<c",
            "primitive": "gcd(a,b,c)=1",
            "cutoff": "a^2+b^2+c^2<=B^2",
            "space_diagonal_note": "D=sqrt(a^2+b^2+c^2) need not be integral",
        },
        "inclusion_exclusion": {
            "ab": "N_ab=A_ab-O_ab_ac-O_ab_bc+T",
            "ac": "N_ac=A_ac-O_ab_ac-O_ac_bc+T",
            "bc": "N_bc=A_bc-O_ab_bc-O_ac_bc+T",
        },
        "validation": validation,
        "rows": rows,
        "status": {
            "E_1B_complete": True,
            "small_B_bruteforce_validation": True,
            "largest_B": max(cutoffs),
            "next": "E-1c finite-profile scaling and directional-ratio analysis",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoffs", nargs="+", type=int, default=list(DEFAULT_CUTOFFS))
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    cutoffs = tuple(sorted(set(args.cutoffs)))
    report = build_report(cutoffs)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["rows"][-1], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
