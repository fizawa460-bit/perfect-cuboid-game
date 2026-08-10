#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import math
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
ATLAS = ROOT / "docs/stage14-toolbox/kernel-edge-full-radical-incidence.md"
RESULT = ROOT / "stages/stage14/14-toolbox-ag/result.md"
STAGE_CODE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")

EXPECTED = {
    "TB-FORMULA-signed-kernel-edge-packet": ("FORMULA", 345, "86b91ffcd8bae79452ef75f187c8570a3819d386"),
    "TB-DICTIONARY-kernel-five-column-refinement": ("DICTIONARY", 345, "86b91ffcd8bae79452ef75f187c8570a3819d386"),
    "TB-LEMMA-composite-squarefree-line-cover": ("LEMMA", 349, "658d87f16921b88bc240c144ac2702fa08994c1a"),
    "TB-LEMMA-full-leg-radical-modulus": ("LEMMA", 352, "a40878e2efdf17b2f151a9cf15849c001908c3a4"),
    "TB-BOUND-radical-poor-hypotenuse-family": ("BOUND", 352, "a40878e2efdf17b2f151a9cf15849c001908c3a4"),
    "TB-RECIPE-radical-incidence-small-D-dichotomy": ("RECIPE", 355, "7ab3c21cc07714b24edfa1a36425b4beaeb2a6e7"),
    "TB-WARNING-radical-incidence-quantifier-boundary": ("WARNING", 355, "7ab3c21cc07714b24edfa1a36425b4beaeb2a6e7"),
}

SECTIONS = [
    "## INPUT",
    "## OUTPUT",
    "## VARIABLE DICTIONARY",
    "## USED BY",
    "## DO NOT USE FOR",
    "## PROVENANCE NOTES",
]


def fail(msg: str) -> None:
    raise AssertionError(msg)


def rad_odd(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
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


def squarefree_divisors(r: int) -> list[int]:
    primes: list[int] = []
    n = r
    p = 3
    while p * p <= n:
        if n % p == 0:
            primes.append(p)
            n //= p
        else:
            p += 2
    if n > 1:
        primes.append(n)
    out = [1]
    for p in primes:
        out += [d * p for d in out]
    return sorted(set(out))


def tau_packets() -> list[tuple[int, int, int]]:
    vals = (-2, -1, 1, 2)
    out: list[tuple[int, int, int]] = []
    for t in itertools.product(vals, repeat=3):
        prod = t[0] * t[1] * t[2]
        if prod <= 0:
            continue
        r = math.isqrt(prod)
        if r * r == prod:
            out.append(t)
    return out


def audit_radical_divisibility(limit: int = 50) -> tuple[int, int]:
    pairs = 0
    divisor_checks = 0
    for m in range(2, limit + 1):
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            S = 2 * m * n
            X = m * m - n * n
            H = m * m + n * n
            if S * S + X * X != H * H:
                fail("Euclid identity failure")
            RS, RX, RH = rad_odd(S), rad_odd(X), rad_odd(H)
            if math.gcd(RS, RX) != 1 or math.gcd(RS, RH) != 1 or math.gcd(RX, RH) != 1:
                fail("primitive leg radicals must be pairwise coprime")
            for leg, R in ((S, RS), (X, RX), (H, RH)):
                for edge in squarefree_divisors(R):
                    if leg % edge:
                        fail("edge divisor does not divide its leg")
                    normalized = edge * (leg // edge) ** 2
                    if normalized % R:
                        fail(f"full radical does not divide normalized edge expression {(leg,R,edge)}")
                    divisor_checks += 1
            pairs += 1
    if pairs < 100 or divisor_checks < 500:
        fail("insufficient deterministic radical samples")
    return pairs, divisor_checks


def prime_divisors(q: int) -> list[int]:
    out: list[int] = []
    n = q
    p = 3
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            n //= p
        else:
            p += 2
    if n > 1:
        out.append(n)
    return out


def local_roots(A: int, B: int, p: int) -> list[int]:
    # Slopes x=r*y for the nonzero projective branch; if the ratio is a
    # nonresidue, the only solution is (0,0), which any chosen line covers.
    roots = [r for r in range(p) if (A * r * r - B) % p == 0]
    return roots if roots else [0]


def covered_by_local_lines(x: int, y: int, A: int, B: int, q: int) -> bool:
    for p in prime_divisors(q):
        if (A * x * x - B * y * y) % p:
            return False
        roots = local_roots(A % p, B % p, p)
        if not any((x - r * y) % p == 0 for r in roots):
            return False
    return True


def audit_line_cover() -> int:
    moduli = (3, 5, 7, 15, 21, 35, 105)
    checks = 0
    for q in moduli:
        if any(q % (p * p) == 0 for p in prime_divisors(q)):
            fail("test modulus not squarefree")
        units = [u for u in range(1, q) if math.gcd(u, q) == 1]
        # Deterministic representative coefficient pairs, enough to exercise
        # residue and nonresidue local branches without a huge CI loop.
        coeffs = [(units[i], units[(3 * i + 1) % len(units)]) for i in range(min(8, len(units)))]
        for A, B in coeffs:
            line_count = 1
            for p in prime_divisors(q):
                line_count *= len(local_roots(A % p, B % p, p))
            if line_count > 2 ** len(prime_divisors(q)):
                fail("CRT line count exceeds 2^omega(q)")
            for x in range(q):
                for y in range(q):
                    if (A * x * x - B * y * y) % q == 0:
                        if not covered_by_local_lines(x, y, A, B, q):
                            fail(f"solution escaped line cover {(q,A,B,x,y)}")
                        checks += 1
    if checks < 100:
        fail("too few line-cover checks")
    return checks


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    atlas = ATLAS.read_text(encoding="utf-8")
    result = RESULT.read_text(encoding="utf-8")
    cards = {c["id"]: c for c in data["cards"]}

    if len(cards) != len(data["cards"]):
        fail("duplicate toolbox card ids")
    if len(cards) < 38:
        fail(f"toolbox-ag expects at least 38 cards, got {len(cards)}")

    for cid, (ctype, pr, sha) in EXPECTED.items():
        card = cards.get(cid)
        if card is None:
            fail(f"missing ag card {cid}")
        if (card["type"], card["status"], card["source_pr"], card["source_merge_sha"]) != (ctype, "CURRENT", pr, sha):
            fail(f"type/provenance mismatch for {cid}")
        text = (ROOT / card["path"]).read_text(encoding="utf-8")
        for section in SECTIONS:
            if section not in text:
                fail(f"{cid} missing section {section}")
        for source in card["source_files"]:
            if not (ROOT / source).exists():
                fail(f"missing source {source} for {cid}")

    nxt = STAGE_CODE.fullmatch(data["next_stage"])
    if not nxt or nxt.group(1) < "ah":
        fail("toolbox registry must be at ah or later after ag")
    # At ag itself the exact handoff theme was fixed. Once the registry has
    # advanced beyond ah, only require a nonempty next theme; later stages own it.
    if nxt.group(1) == "ah":
        if data.get("next_theme") != "two-quadrics and genus-one geometry":
            fail("unexpected toolbox-ag handoff theme")
    elif not str(data.get("next_theme", "")).strip():
        fail("advanced toolbox registry must retain a nonempty next theme")

    taus = tau_packets()
    if len(taus) != 16:
        fail(f"tau packet count mismatch: {len(taus)}")

    pairs, divisor_checks = audit_radical_divisibility()
    line_checks = audit_line_cover()

    if Fraction(41, 42) - Fraction(1, 2) != Fraction(10, 21):
        fail("critical exponent identity failure")
    if min(Fraction(1, 2), Fraction(10, 21)) != Fraction(10, 21):
        fail("critical full-radical coordinate exponent mismatch")

    atlas_locks = [
        "d0 = tau0*a*b",
        "2^omega(q)",
        "R_H = rad_odd(H)",
        "small selected kernel != small full radical",
        "coordinate incidence saving != packet-existence saving",
        "rho = 1/2",
        "nu  = 10/21",
    ]
    for lock in atlas_locks:
        if lock not in atlas:
            fail(f"atlas missing lock {lock}")

    source_locks = {
        "stages/stage14/14-s6-01/result.md": [
            "ODD_KERNEL_EDGE_PACKET_FACTORIZATION=true",
            "TWO_ADIC_SIGN_PACKET_COUNT=16",
        ],
        "stages/stage14/14-4bi-L/result.md": [
            "COMPOSITE_EDGE_RECTANGLE_BOUND_PROVED=true",
            "SMOOTH_LARGE_EDGE_KERNEL_INCIDENCE_CLOSED=true",
        ],
        "stages/stage14/14-4bi-S/result.md": [
            "FULL_ODD_EDGE_RADICAL_CONGRUENCES_PROVED=true",
            "RADICAL_POOR_HYPOTENUSE_SECTOR_GLOBALLY_SPARSE=true",
            "SMALL_KERNEL_INTRINSIC_MODULUS_OBSTRUCTION=false",
        ],
        "stages/stage14/14-4bj/result.md": [
            "RADICAL_POOR_THRESHOLD_FOR_SQRT_SCALE=1/2",
            "REQUIRED_POST_LOCAL_SAVING=10/21",
            "EXISTENCE_VS_COORDINATE_DENSITY_QUANTIFIER_GAP=true",
        ],
    }
    for path, locks in source_locks.items():
        text = (ROOT / path).read_text(encoding="utf-8")
        for lock in locks:
            if lock not in text:
                fail(f"source boundary missing {lock} in {path}")

    for lock in [
        "STAGE14_TOOLBOX_AG=COMPLETE_ODD_KERNEL_EDGE_PACKET_AND_FULL_RADICAL_INCIDENCE",
        "CANONICAL_NEW_CARD_COUNT=7",
        "CANONICAL_TOTAL_CARD_COUNT=38",
        "TAU_PACKET_COUNT=16",
        "LARGEST_PRIME_REQUIRED_FOR_INCIDENCE=false",
        "SMALL_SELECTED_KERNEL_INTRINSIC_MODULUS_OBSTRUCTION=false",
        "COORDINATE_DENSITY_IMPLIES_PACKET_EXISTENCE_SAVING=false",
        "OPEN_PR_USED_AS_CANONICAL_SOURCE=false",
        "TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false",
        "NEXT=Stage14-toolbox-ah two-quadrics and genus-one geometry",
    ]:
        if lock not in result:
            fail(f"result boundary missing {lock}")

    print(json.dumps({
        "stage": "14-toolbox-ag",
        "classification": "ODD_KERNEL_EDGE_AND_FULL_RADICAL_INCIDENCE_AUDIT",
        "canonical_card_count": len(cards),
        "new_card_count": len(EXPECTED),
        "tau_packet_count": len(taus),
        "primitive_euclid_pairs_checked": pairs,
        "full_radical_divisor_checks": divisor_checks,
        "composite_line_cover_solution_checks": line_checks,
        "critical_rho": "1/2",
        "critical_nu": "10/21",
        "coordinate_to_packet_transfer_claimed": False,
        "next_stage": data["next_stage"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
