#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
ATLAS = ROOT / "docs/stage14-toolbox/integral-global-small-point-witness-formulas.md"
RESULT = ROOT / "stages/stage14/14-toolbox-af/result.md"
STAGE_CODE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")

EXPECTED = {
    "TB-FORMULA-rational-witness-denominator": "FORMULA",
    "TB-FORMULA-integral-witness-equation": "FORMULA",
    "TB-LEMMA-witness-pairwise-gcd-support": "LEMMA",
    "TB-BOUND-witness-polynomial-box": "BOUND",
    "TB-RECIPE-physical-to-integral-witness": "RECIPE",
    "TB-WARNING-witness-quantifier-and-denominator-boundary": "WARNING",
}
SECTIONS = ["## INPUT", "## OUTPUT", "## VARIABLE DICTIONARY", "## USED BY", "## DO NOT USE FOR", "## PROVENANCE NOTES"]
MERGE_SHA = "86b91ffcd8bae79452ef75f187c8570a3819d386"


def fail(msg: str) -> None:
    raise AssertionError(msg)


def primitive_faces(limit: int = 12):
    for m in range(2, limit + 1):
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            e = 2*m*n
            o = m*m-n*n
            h = m*m+n*n
            yield e, o, h
            yield o, e, h


def find_integral_witnesses(target: int = 24):
    hits = []
    for S, X, H in primitive_faces():
        for D in range(1, 5):
            for A in range(-1000, 1001):
                if math.gcd(A, D) != 1:
                    continue
                G0 = A
                G1 = A-S*S*D*D
                G2 = A+X*X*D*D
                if 0 in (G0, G1, G2):
                    continue
                prod = G0*G1*G2
                if prod < 0:
                    continue
                Y = math.isqrt(prod)
                if Y*Y != prod:
                    continue
                hits.append((S, X, H, A, D, Y, G0, G1, G2))
                if len(hits) >= target:
                    return hits
    return hits


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    atlas = ATLAS.read_text(encoding="utf-8")
    result = RESULT.read_text(encoding="utf-8")
    cards = {c["id"]: c for c in data["cards"]}
    if len(cards) != len(data["cards"]):
        fail("duplicate toolbox card id")
    if len(cards) < 31:
        fail(f"af expects at least 31 cards, got {len(cards)}")

    for cid, ctype in EXPECTED.items():
        card = cards.get(cid)
        if card is None:
            fail(f"missing af card {cid}")
        if card["type"] != ctype or card["status"] != "CURRENT":
            fail(f"wrong type/status {cid}")
        if card["source_pr"] != 345 or card["source_merge_sha"] != MERGE_SHA:
            fail(f"wrong canonical provenance {cid}")
        text = (ROOT / card["path"]).read_text(encoding="utf-8")
        for sec in SECTIONS:
            if sec not in text:
                fail(f"{cid} missing {sec}")
        for source in card["source_files"]:
            if not (ROOT/source).exists():
                fail(f"missing source {source}")

    nxt = STAGE_CODE.fullmatch(data["next_stage"])
    if not nxt or nxt.group(1) < "ag":
        fail("toolbox registry must hand off to ag or later")

    for lock in [
        "Z=A/D^2", "W=Y/D^3", "Y^2=A(A-S^2D^2)(A+X^2D^2)",
        "gcd(G0,G1)|S^2", "gcd(G0,G2)|X^2", "gcd(G1,G2)|H^2",
        "V(B)<=J_C(B)<=N_local(B)", "integral witness => physical reconstruction        false",
    ]:
        if lock not in atlas:
            fail(f"atlas missing {lock}")

    source = (ROOT / "stages/stage14/14-s6-01/result.md").read_text(encoding="utf-8")
    for lock in [
        "MONIC_WEIERSTRASS_DENOMINATOR_SQUARE_CUBE_PROVED=true",
        "INTEGRAL_WITNESS_EQUATION_EXACT=true",
        "PAIRWISE_ODD_GCD_SUPPORT_EXACT=true",
        "POLYNOMIAL_WITNESS_BOX_PROVED=true",
        "DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false",
    ]:
        if lock not in source:
            fail(f"s6-01 boundary missing {lock}")

    for lock in [
        "STAGE14_TOOLBOX_AF=COMPLETE_INTEGRAL_GLOBAL_SMALL_POINT_WITNESS_FORMULAS",
        "CANONICAL_NEW_CARD_COUNT=6",
        "RATIONAL_WITNESS_SQUARE_CUBE_DENOMINATOR_FROZEN=true",
        "INTEGRAL_WITNESS_EQUATION_FROZEN=true",
        "PAIRWISE_GCD_EDGE_SUPPORT_FROZEN=true",
        "WITNESS_POLYNOMIAL_BOX_FROZEN=true",
        "INTEGRAL_WITNESS_IMPLIES_PHYSICAL_RECONSTRUCTION=false",
        "POLYNOMIAL_BOX_PROMOTED_TO_COUNT_SAVING=false",
        "SIGNED_KERNEL_EDGE_PACKET_CANONICALIZED_IN_AF=false",
        "NEXT=Stage14-toolbox-ag odd kernel edge packet and full-radical incidence",
    ]:
        if lock not in result:
            fail(f"result missing {lock}")

    witnesses = find_integral_witnesses()
    if len(witnesses) < 20:
        fail(f"too few deterministic integral witness samples: {len(witnesses)}")
    if not any(w[4] > 1 for w in witnesses):
        fail("audit did not include any D>1 witness")

    for S, X, H, A, D, Y, G0, G1, G2 in witnesses:
        if S*S + X*X != H*H:
            fail("Pythagorean identity failure")
        if math.gcd(A,D) != 1:
            fail("primitive denominator failure")
        if G0-G1 != S*S*D*D or G2-G0 != X*X*D*D or G2-G1 != H*H*D*D:
            fail("factor difference identity failure")
        if G0*G1*G2 != Y*Y:
            fail("integral witness square failure")
        if math.gcd(abs(G0), abs(G1)) > S*S:
            fail("01 gcd magnitude impossible")
        if S*S % math.gcd(abs(G0), abs(G1)):
            fail("01 gcd support failure")
        if X*X % math.gcd(abs(G0), abs(G2)):
            fail("02 gcd support failure")
        if H*H % math.gcd(abs(G1), abs(G2)):
            fail("12 gcd support failure")
        for G in (G0,G1,G2):
            if math.gcd(abs(G), D) != 1:
                fail("denominator prime entered witness factor")

    print(json.dumps({
        "stage": "14-toolbox-af",
        "classification": "INTEGRAL_GLOBAL_SMALL_POINT_WITNESS_FORMULA_AUDIT",
        "canonical_card_count": len(cards),
        "new_card_count": len(EXPECTED),
        "integral_witness_samples_checked": len(witnesses),
        "contains_nontrivial_denominator_sample": any(w[4] > 1 for w in witnesses),
        "kernel_packet_reserved_for_next_stage": True,
        "toolbox_owns_new_theorem": False,
        "next_stage": data["next_stage"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
