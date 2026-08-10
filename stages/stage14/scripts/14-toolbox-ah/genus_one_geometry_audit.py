#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
ATLAS = ROOT / "docs/stage14-toolbox/two-quadrics-genus-one-geometry.md"
RESULT = ROOT / "stages/stage14/14-toolbox-ah/result.md"
STAGE_CODE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")

EXPECTED = {
    "TB-FORMULA-fixed-packet-two-quadrics": ("FORMULA", "CURRENT", 348, "1338ee0170a6d92c26a9dd4fa21c886a8125d6db"),
    "TB-FORMULA-two-quadric-pencil": ("FORMULA", "CURRENT", 348, "1338ee0170a6d92c26a9dd4fa21c886a8125d6db"),
    "TB-LEMMA-fixed-packet-smooth-genus-one": ("LEMMA", "CURRENT", 348, "1338ee0170a6d92c26a9dd4fa21c886a8125d6db"),
    "TB-LEMMA-coordinate-boundary-finite": ("LEMMA", "CURRENT", 348, "1338ee0170a6d92c26a9dd4fa21c886a8125d6db"),
    "TB-FORMULA-conic-square-lift": ("FORMULA", "CURRENT", 348, "1338ee0170a6d92c26a9dd4fa21c886a8125d6db"),
    "TB-LEMMA-diagonal-pair-genus-one-slope": ("LEMMA", "CURRENT", 395, "aa21a3604cf72e06f797c8ba2ecff96b49e60f44"),
    "TB-BOUND-diagonal-pair-genus-one-count": ("BOUND", "CURRENT", 395, "aa21a3604cf72e06f797c8ba2ecff96b49e60f44"),
    "TB-WARNING-genus-one-quantifier-and-model-boundary": ("WARNING", "CURRENT", 395, "aa21a3604cf72e06f797c8ba2ecff96b49e60f44"),
    "TB-LEDGER-current-main-after-4bq": ("LEDGER", "SUPERSEDED", 395, "aa21a3604cf72e06f797c8ba2ecff96b49e60f44"),
    "TB-LEDGER-current-main-after-4br": ("LEDGER", "CURRENT", 396, "01afa63539e32e62070a84927bbc0530241a79e9"),
}
SECTIONS = ["## INPUT", "## OUTPUT", "## VARIABLE DICTIONARY", "## USED BY", "## DO NOT USE FOR", "## PROVENANCE NOTES"]


def fail(msg: str) -> None:
    raise AssertionError(msg)


def primitive_triples(limit: int = 18):
    out = []
    for m in range(2, limit + 1):
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            e, o, h = 2*m*n, m*m-n*n, m*m+n*n
            out.append((e, o, h))
    return out


def audit_pencil_roots() -> int:
    checked = 0
    for S, X, H in primitive_triples():
        if S*S + X*X != H*H:
            fail("Pythagorean identity failure")
        affine = {Fraction(0), Fraction(1), Fraction(-X*X, S*S)}
        if len(affine) != 3:
            fail(f"pencil affine roots collide for {(S,X,H)}")
        if Fraction(-X*X, S*S) == 1:
            fail("fourth singular parameter collided with lambda=mu")
        checked += 1
    if checked < 40:
        fail("too few pencil samples")
    return checked


def rank_less_than_two(g1, g2, p: int) -> bool:
    for i in range(4):
        for j in range(i + 1, 4):
            if (g1[i] * g2[j] - g1[j] * g2[i]) % p:
                return False
    return True


def audit_smoothness_mod_p() -> int:
    samples = [
        (3, 4, 1, 1, 1, 7),
        (3, 4, 2, -1, -2, 7),
        (5, 12, 1, -1, -1, 11),
    ]
    points = 0
    for S, X, d0, d1, d2, p in samples:
        H2 = S*S + X*X
        if (2*d0*d1*d2*S*X*H2) % p == 0:
            fail("sample prime is not good")
        for u0 in range(p):
            for u1 in range(p):
                for u2 in range(p):
                    for D in range(p):
                        if not (u0 or u1 or u2 or D):
                            continue
                        q1 = (d0*u0*u0 - d1*u1*u1 - S*S*D*D) % p
                        q2 = (d2*u2*u2 - d0*u0*u0 - X*X*D*D) % p
                        if q1 or q2:
                            continue
                        g1 = [(2*d0*u0)%p, (-2*d1*u1)%p, 0, (-2*S*S*D)%p]
                        g2 = [(-2*d0*u0)%p, 0, (2*d2*u2)%p, (-2*X*X*D)%p]
                        if rank_less_than_two(g1, g2, p):
                            fail(f"singular good-reduction point for sample {(S,X,d0,d1,d2,p)}")
                        points += 1
    if points == 0:
        fail("no finite-field points tested")
    return points


def sqrt_roots_mod(a: int, p: int) -> list[int]:
    return [x for x in range(p) if x*x % p == a % p]


def audit_four_branch_sample() -> int:
    total = 0
    S, X = 3, 4
    for p in (7, 11):
        r1 = sqrt_roots_mod(S*S, p)
        r2 = sqrt_roots_mod(X*X, p)
        if len(r1) != 2 or len(r2) != 2:
            fail("branch roots did not split into two signs")
        pts = {(u1, u2) for u1 in r1 for u2 in r2}
        if len(pts) != 4:
            fail("branch locus does not have four split geometric samples")
        total += len(pts)
    return total


def audit_diagonal_slope_injection(limit: int = 32) -> int:
    seen: dict[Fraction, tuple[int, int]] = {}
    pairs = 0
    for x in range(1, limit + 1):
        for y in range(1, limit + 1):
            if math.gcd(x, y) != 1:
                continue
            t = Fraction(x, y)
            old = seen.get(t)
            if old is not None and old != (x, y):
                fail(f"reduced slope collision {old} vs {(x,y)}")
            seen[t] = (x, y)
            pairs += 1
    if pairs < 500:
        fail("too few coprime diagonal pairs")
    return pairs


def audit_quartic_smoothness() -> int:
    checked = 0
    for p in (7, 11, 13):
        K, A, B = 2, 3, 4
        for t in range(p):
            f = K * (A*A - B*B*pow(t, 4, p))
            fp = -4*K*B*B*pow(t, 3, p)
            if f % p == 0 and fp % p == 0:
                fail(f"repeated affine quartic root mod {p}")
            checked += 1
    return checked


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    atlas = ATLAS.read_text(encoding="utf-8")
    result = RESULT.read_text(encoding="utf-8")
    cards = {c["id"]: c for c in data["cards"]}
    if len(cards) != len(data["cards"]) or len(cards) != 48:
        fail(f"registry count/uniqueness failure: {len(cards)}")

    for cid, (ctype, status, pr, sha) in EXPECTED.items():
        card = cards.get(cid)
        if not card:
            fail(f"missing {cid}")
        if (card["type"], card["status"], card["source_pr"], card["source_merge_sha"]) != (ctype, status, pr, sha):
            fail(f"metadata mismatch for {cid}")
        text = (ROOT / card["path"]).read_text(encoding="utf-8")
        for sec in SECTIONS:
            if sec not in text:
                fail(f"{cid} missing {sec}")
        for source in card["source_files"]:
            if not (ROOT / source).exists():
                fail(f"missing source file {source}")

    old = cards["TB-LEDGER-post-local-sqrt-gap"]
    q = cards["TB-LEDGER-current-main-after-4bq"]
    r = cards["TB-LEDGER-current-main-after-4br"]
    if old["status"] != "SUPERSEDED" or old.get("superseded_by") != "TB-LEDGER-current-main-after-4bq":
        fail("historical 10/21 ledger chain broken")
    if q["status"] != "SUPERSEDED" or q.get("superseded_by") != "TB-LEDGER-current-main-after-4br":
        fail("4bq ledger chain broken")
    if r["status"] != "CURRENT":
        fail("4br ledger is not current")
    old_text = (ROOT / old["path"]).read_text(encoding="utf-8")
    q_text = (ROOT / q["path"]).read_text(encoding="utf-8")
    if "STATUS: SUPERSEDED" not in old_text or "SUPERSEDED_BY: TB-LEDGER-current-main-after-4bq" not in old_text:
        fail("historical 10/21 ledger card body not updated")
    if "STATUS: SUPERSEDED" not in q_text or "SUPERSEDED_BY: TB-LEDGER-current-main-after-4br" not in q_text:
        fail("4bq ledger card body not updated")

    nxt = STAGE_CODE.fullmatch(data["next_stage"])
    if not nxt or nxt.group(1) < "ai":
        fail("registry must hand off to ai or later")

    atlas_locks = [
        "C_sigma={Q1=Q2=0}",
        "lambda*mu*(lambda-mu)*(lambda*S^2+mu*X^2)",
        "W^2=F0*((b0*d0)^2-(a0*c0)^2*t^4)",
        "E_good-res(B)<<B^(3/7+1/2+o(1))=B^(13/14+o(1))",
        "61/63-1/2=59/126",
        "20/21-1/2=19/42",
    ]
    for lock in atlas_locks:
        if lock not in atlas:
            fail(f"atlas missing {lock}")

    source_locks = {
        "stages/stage14/14-s6-02/result.md": [
            "FIXED_PACKET_PENCIL_DETERMINANT_EXACT=true",
            "FIXED_PACKET_SMOOTH_GENUS_ONE_PROVED=true",
            "POSITIVE_DIMENSIONAL_TORSION_BOUNDARY_COMPONENT=false",
            "CONIC_PLUS_SQUARE_LIFT_EXACT=true",
        ],
        "stages/stage14/14-4bq/result.md": [
            "MAIN_DIAGONAL_MOVING_SLOPE_GENUS_ONE=true",
            "OFF_DIAGONAL_MOVING_SLOPE_GENUS_ONE=true",
            "GOOD_CELL_RESIDUAL_BOUND=B^(13/14+o(1))",
            "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/63",
            "REMAINING_GAP_TO_SQRT=59/126",
        ],
        "stages/stage14/14-4br/result.md": [
            "CROSS_SECTOR_BOUND=B^(20/21+o(1))",
            "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=20/21",
            "CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=1/42",
            "REMAINING_GAP_TO_SQRT=19/42",
        ],
    }
    for path, locks in source_locks.items():
        text = (ROOT / path).read_text(encoding="utf-8")
        for lock in locks:
            if lock not in text:
                fail(f"source boundary missing {lock}")

    expected_result = [
        "STAGE14_TOOLBOX_AH=COMPLETE_TWO_QUADRICS_AND_GENUS_ONE_GEOMETRY",
        "CANONICAL_NEW_CARD_COUNT=10",
        "CANONICAL_TOTAL_CARD_COUNT=48",
        "FIXED_PACKET_SMOOTH_GENUS_ONE_FROZEN=true",
        "POSITIVE_DIMENSIONAL_COORDINATE_BOUNDARY=false",
        "DIAGONAL_PAIR_GENUS_ONE_GOOD_RESIDUAL_BOUND=13/14",
        "HISTORICAL_4BQ_WHOLE_FAMILY_EXPONENT=61/63",
        "CURRENT_WHOLE_FAMILY_EXPONENT=20/21",
        "CUMULATIVE_POST_LOCAL_SAVING=1/42",
        "CURRENT_REMAINING_GAP_TO_SQRT=19/42",
        "GENUS_ONE_ALONE_IMPLIES_MOVING_FAMILY_SAVING=false",
        "NEXT=Stage14-toolbox-ai compact torsion denominator and half-angle identities",
    ]
    for lock in expected_result:
        if lock not in result:
            fail(f"result missing {lock}")

    if Fraction(3, 7) + Fraction(1, 2) != Fraction(13, 14):
        fail("13/14 ledger failure")
    q_sectors = [Fraction(20,21), Fraction(61,63), Fraction(13,14)]
    if max(q_sectors) != Fraction(61,63):
        fail("4bq sector max failure")
    if Fraction(41,42) - Fraction(61,63) != Fraction(1,126):
        fail("4bq 1/126 saving ledger failure")
    if Fraction(61,63) - Fraction(1,2) != Fraction(59,126):
        fail("4bq 59/126 gap ledger failure")
    r_sectors = [Fraction(20,21), Fraction(20,21), Fraction(13,14)]
    if max(r_sectors) != Fraction(20,21):
        fail("4br sector max failure")
    if Fraction(41,42) - Fraction(20,21) != Fraction(1,42):
        fail("4br cumulative saving ledger failure")
    if Fraction(20,21) - Fraction(1,2) != Fraction(19,42):
        fail("4br current sqrt gap ledger failure")

    pencil = audit_pencil_roots()
    ff_points = audit_smoothness_mod_p()
    branches = audit_four_branch_sample()
    slopes = audit_diagonal_slope_injection()
    quartic = audit_quartic_smoothness()

    print(json.dumps({
        "stage": "14-toolbox-ah",
        "classification": "TWO_QUADRICS_GENUS_ONE_GEOMETRY_AUDIT",
        "canonical_card_count": len(cards),
        "new_card_count": len(EXPECTED),
        "pencil_samples_checked": pencil,
        "good_reduction_curve_points_checked": ff_points,
        "split_branch_points_checked": branches,
        "coprime_reduced_slopes_checked": slopes,
        "quartic_affine_derivative_checks": quartic,
        "historical_4bq_exponent": "61/63",
        "current_main_exponent": "20/21",
        "remaining_gap_to_sqrt": "19/42",
        "next_stage": data["next_stage"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
