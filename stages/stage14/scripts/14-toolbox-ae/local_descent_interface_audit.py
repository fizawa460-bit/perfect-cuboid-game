#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
ATLAS = ROOT / "docs/stage14-toolbox/local-descent-five-column-interface.md"
RESULT = ROOT / "stages/stage14/14-toolbox-ae/result.md"
STAGE_CODE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")

EXPECTED = {
    "TB-DICTIONARY-five-column-local-routing": ("DICTIONARY", 213, "f0e78817a65527cfb348df5f7f3ed66289afa2da"),
    "TB-FORMULA-local-covering-coordinates": ("FORMULA", 218, "ea0c8b56c9c3bc080dce76e050185d33212fae46"),
    "TB-RECIPE-odd-local-row-dispatch": ("RECIPE", 222, "87c5bec65d36db55de11f07e1d315a640f418673"),
    "TB-FORMULA-q2-hilbert-symbol": ("FORMULA", 224, "ae9cf81bf049c52fb6274ae111bcb1bbdc87e910"),
    "TB-LEMMA-q2-eight-state-covering-image": ("LEMMA", 229, "dd13e6ffae243a4fa3b1144ab97d33e7c8a0ae23"),
    "TB-RECIPE-full-local-character-check": ("RECIPE", 229, "dd13e6ffae243a4fa3b1144ab97d33e7c8a0ae23"),
    "TB-WARNING-local-global-and-orientation-boundary": ("WARNING", 345, "86b91ffcd8bae79452ef75f187c8570a3819d386"),
}
SECTIONS = ["## INPUT", "## OUTPUT", "## VARIABLE DICTIONARY", "## USED BY", "## DO NOT USE FOR", "## PROVENANCE NOTES"]
Q2_CLASSES = (1, 3, 5, 7, 2, 6, 10, 14)
Q2_IMAGE = ((1,1,1),(3,7,5),(5,1,5),(7,7,1),(2,1,2),(6,7,10),(10,1,10),(14,7,2))


def fail(msg: str) -> None:
    raise AssertionError(msg)


def class_bits(x: int) -> tuple[int, int]:
    alpha = 0
    while x % 2 == 0:
        alpha ^= 1
        x //= 2
    return alpha, x % 8


def q2_mul(a: int, b: int) -> int:
    aa, au = class_bits(a)
    ba, bu = class_bits(b)
    target = (aa ^ ba, (au * bu) % 8)
    for rep in Q2_CLASSES:
        if class_bits(rep) == target:
            return rep
    fail("Q2 multiplication failed")
    raise RuntimeError


def q2_hilbert(a: int, b: int) -> int:
    alpha, u = class_bits(a)
    beta, v = class_bits(b)
    eu, ev = ((u - 1) // 2) & 1, ((v - 1) // 2) & 1
    ou, ov = ((u * u - 1) // 8) & 1, ((v * v - 1) // 8) & 1
    bit = (eu * ev + alpha * ov + beta * ou) & 1
    return -1 if bit else 1


def odd_prime_divisors(n: int) -> set[int]:
    out: set[int] = set()
    while n % 2 == 0 and n:
        n //= 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            out.add(p)
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        out.add(n)
    return out


def audit_five_columns(limit: int = 45) -> tuple[int, int]:
    pairs = rows = 0
    for m in range(2, limit + 1):
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            A, B, C, D, E = m, n, m-n, m+n, m*m+n*n
            cols = [A, B, C, D, E]
            for i in range(5):
                for j in range(i+1, 5):
                    if math.gcd(cols[i], cols[j]) not in (1, 2):
                        fail(f"odd support collision {(m,n,i,j)}")
            S5, X5, H = C*D, 2*A*B, E
            if S5*S5 + X5*X5 != H*H:
                fail("historical s5 orientation failed")
            primes = odd_prime_divisors(A*B*C*D*E)
            column_primes = [odd_prime_divisors(v) for v in cols]
            for p in primes:
                memberships = [p in s for s in column_primes]
                if sum(memberships) != 1:
                    fail(f"odd prime {p} not in unique five-column support for {(m,n)}")
                idx = memberships.index(True)
                if idx in (0,1) and X5 % p:
                    fail("s5 A/B routing to X failed")
                if idx in (2,3) and S5 % p:
                    fail("s5 C/D routing to S failed")
                if idx == 4 and H % p:
                    fail("s5 E routing to H failed")
                rows += 1
            # s6-01 swaps the two legs but not the columns.
            S6, X6 = X5, S5
            if S6*S6 + X6*X6 != H*H:
                fail("s6 swapped orientation failed")
            pairs += 1
    if pairs < 100:
        fail("too few Euclid samples")
    return pairs, rows


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    atlas = ATLAS.read_text(encoding="utf-8")
    result = RESULT.read_text(encoding="utf-8")
    cards = {c["id"]: c for c in data["cards"]}
    if len(cards) != len(data["cards"]) or len(cards) < 25:
        fail("registry card count/uniqueness failure")

    for cid, (ctype, pr, sha) in EXPECTED.items():
        card = cards.get(cid)
        if not card:
            fail(f"missing {cid}")
        if (card["type"], card["status"], card["source_pr"], card["source_merge_sha"]) != (ctype, "CURRENT", pr, sha):
            fail(f"provenance/type mismatch {cid}")
        text = (ROOT / card["path"]).read_text(encoding="utf-8")
        for sec in SECTIONS:
            if sec not in text:
                fail(f"{cid} missing {sec}")
        for source in card["source_files"]:
            if not (ROOT / source).exists():
                fail(f"missing source {source}")

    nxt = STAGE_CODE.fullmatch(data["next_stage"])
    if not nxt or nxt.group(1) < "af":
        fail("registry must hand off to af or later")

    for lock in [
        "S = CD = m^2-n^2", "X = 2AB = 2mn", "S = 2AB", "X = CD",
        "p|S -> label 12", "p|X -> label 13", "p|X, p==3 mod4 : automatic",
        "(1,1,1)", "(14,7,2)", "local admissible => globally soluble",
    ]:
        if lock not in atlas:
            fail(f"atlas missing {lock}")

    if len({class_bits(x) for x in Q2_CLASSES}) != 8:
        fail("Q2 representatives not unique")
    for a in Q2_CLASSES:
        for b in Q2_CLASSES:
            if q2_hilbert(a,b) != q2_hilbert(b,a):
                fail("Q2 Hilbert symmetry failure")
    states = [(a,b,q2_mul(a,b)) for a in Q2_CLASSES for b in Q2_CLASSES]
    if len(states) != 64:
        fail("Q2 product-square state count failure")
    if len(set(Q2_IMAGE)) != 8:
        fail("Q2 image count failure")
    for a,b,c in Q2_IMAGE:
        if q2_mul(q2_mul(a,b),c) != 1:
            fail(f"Q2 image state not product-square {(a,b,c)}")

    source_locks = {
        "stages/stage14/14-s5b/result.md": "FIVE_MOVING_FACTORS_ODD_PAIRWISE_COPRIME=true",
        "stages/stage14/14-s5c/result.md": "ODD_SUPPORTED_FACTOR_TO_LABEL_ROUTING_DERIVED=true",
        "stages/stage14/14-s5d/result.md": "ALL_ODD_BAD_PRIME_ROWS_EXPLICIT=true",
        "stages/stage14/14-s5e/result.md": "Q2_HILBERT_SYMBOL_FORMULA_LOCKED=true",
        "stages/stage14/14-s5f/result.md": "FULL_LOCAL_2_DESCENT_CHARACTER_SYSTEM_COMPLETE=true",
        "stages/stage14/14-s6-01/result.md": "FIVE_EUCLID_COLUMN_REFINEMENT_EXACT=true",
    }
    for path, lock in source_locks.items():
        if lock not in (ROOT/path).read_text(encoding="utf-8"):
            fail(f"source boundary missing {lock}")

    for lock in [
        "STAGE14_TOOLBOX_AE=COMPLETE_LOCAL_2_DESCENT_FIVE_COLUMN_INTERFACE",
        "CANONICAL_NEW_CARD_COUNT=7", "S5_S6_ORIENTATION_ADAPTER_FROZEN=true",
        "Q2_COVERING_SOLUBLE_STATE_COUNT=8", "LOCAL_ADMISSIBLE_IMPLIES_GLOBAL_SOLUBLE=false",
        "GLOBAL_SOLUBLE_IMPLIES_PHYSICAL_HIT=false", "OPEN_PR_USED_AS_CANONICAL_SOURCE=false",
        "TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false",
        "NEXT=Stage14-toolbox-af integral global-small-point witness formulas",
    ]:
        if lock not in result:
            fail(f"result missing {lock}")

    pairs, rows = audit_five_columns()
    print(json.dumps({
        "stage": "14-toolbox-ae",
        "classification": "LOCAL_2_DESCENT_FIVE_COLUMN_INTERFACE_AUDIT",
        "canonical_card_count": len(cards), "new_card_count": len(EXPECTED),
        "primitive_euclid_pairs_checked": pairs, "odd_prime_column_rows_checked": rows,
        "q2_product_square_state_count": len(states), "q2_covering_image_state_count": len(Q2_IMAGE),
        "orientation_adapter_checked": True, "local_to_global_converse_allowed": False,
        "next_stage": data["next_stage"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
