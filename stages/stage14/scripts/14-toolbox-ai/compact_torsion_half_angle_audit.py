#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
ATLAS = ROOT / "docs/stage14-toolbox/compact-torsion-half-angle-atlas.md"
RESULT = ROOT / "stages/stage14/14-toolbox-ai/result.md"
STAGE_CODE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")

EXPECTED = {
    "TB-FORMULA-compact-t0-torsion-translation": ("FORMULA", 356, "c2273d0388b48f8fb51d9dc69d8977efbc83db37"),
    "TB-LEMMA-physical-compact-class-reduction": ("LEMMA", 356, "c2273d0388b48f8fb51d9dc69d8977efbc83db37"),
    "TB-FORMULA-physical-conjugate-gap-coordinate": ("FORMULA", 360, "42f4315b0659bd402a94adeb8822588ea153305a"),
    "TB-FORMULA-minus-half-angle-denominator": ("FORMULA", 360, "42f4315b0659bd402a94adeb8822588ea153305a"),
    "TB-FORMULA-dual-compact-half-angle-selectors": ("FORMULA", 365, "dffc5669ca73c4bb7e4b5115e1fe238dde5605ae"),
    "TB-FORMULA-dual-denominator-cancellation-product": ("FORMULA", 365, "dffc5669ca73c4bb7e4b5115e1fe238dde5605ae"),
    "TB-DICTIONARY-dual-selector-gcd-matrix": ("DICTIONARY", 364, "c51992e2373c0f7f265275c211684f6bd5ef9ccf"),
    "TB-RECIPE-compact-half-angle-prime-routing": ("RECIPE", 364, "c51992e2373c0f7f265275c211684f6bd5ef9ccf"),
    "TB-WARNING-compact-selector-quantifier-boundary": ("WARNING", 365, "dffc5669ca73c4bb7e4b5115e1fe238dde5605ae"),
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


def require(text: str, needle: str, where: str) -> None:
    if needle not in text:
        fail(f"missing {needle!r} in {where}")


def audit_t0_involution() -> int:
    # E_{3,4}: y^2=x(x-9)(x+16). The non-torsion integral point
    # (24,120) is sent by T0 to (-6,30) and back.
    S, X = 3, 4
    z, w = Fraction(24), Fraction(120)
    checks = 0
    for expected in [(Fraction(-6), Fraction(30)), (Fraction(24), Fraction(120))]:
        z2 = -S*S*X*X / z
        w2 = S*S*X*X*w / (z*z)
        if (z2, w2) != expected:
            fail(f"T0 involution mismatch: {(z2,w2)} != {expected}")
        if w2*w2 != z2*(z2-S*S)*(z2+X*X):
            fail("translated point left the elliptic curve")
        z, w = z2, w2
        checks += 1
    return checks


def primitive_pairs(limit: int = 30):
    for m in range(2, limit + 1):
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m-n) % 2 == 0:
                continue
            yield m, n


def audit_half_angle_and_dual_product() -> tuple[int, int]:
    half_angle = 0
    dual = 0
    for m, n in primitive_pairs():
        E = 2*m*n
        O = m*m-n*n
        H = m*m+n*n
        for S2, X2 in ((E, O), (O, E)):
            if S2 == E:
                kappa, s, t = 1, m+n, m-n
            else:
                kappa, s, t = 2, m, n
            if H+S2 != kappa*s*s or H-S2 != kappa*t*t or X2 != kappa*s*t:
                fail("half-angle normalization mismatch")
            if math.gcd(s, t) != 1:
                fail("half-angle roots must be coprime")
            half_angle += 1

            # Every divisor choice for the two compact denominator roots obeys
            # the exact product identity once the complementary cofactors are defined.
            ds = [d for d in range(1, s+1) if s % d == 0]
            dt = [d for d in range(1, t+1) if t % d == 0]
            for Dp in ds[:4]:
                for Dm in dt[:4]:
                    kp, km = s//Dp, t//Dm
                    Q, K = Dp*Dm, kp*km
                    if Q*K != X2//kappa:
                        fail("dual product QK=X2/kappa failed")
                    dual += 1
    if half_angle < 100 or dual < 500:
        fail("insufficient deterministic half-angle samples")
    return half_angle, dual


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    atlas = ATLAS.read_text(encoding="utf-8")
    result = RESULT.read_text(encoding="utf-8")
    cards = {c["id"]: c for c in data["cards"]}

    if len(cards) != len(data["cards"]):
        fail("duplicate toolbox card id")
    if len(cards) < 57:
        fail(f"toolbox-ai expects at least 57 cards, got {len(cards)}")

    for cid, (ctype, pr, sha) in EXPECTED.items():
        card = cards.get(cid)
        if card is None:
            fail(f"missing ai card {cid}")
        if (card["type"], card["status"], card["source_pr"], card["source_merge_sha"]) != (ctype, "CURRENT", pr, sha):
            fail(f"metadata mismatch for {cid}")
        path = ROOT / card["path"]
        if not path.exists():
            fail(f"missing card file {path}")
        text = path.read_text(encoding="utf-8")
        for section in SECTIONS:
            if section not in text:
                fail(f"{cid} missing {section}")
        for src in card["source_files"]:
            if not (ROOT / src).exists():
                fail(f"missing canonical source {src}")

    nxt = STAGE_CODE.fullmatch(data["next_stage"])
    if not nxt or nxt.group(1) < "aj":
        fail("toolbox registry must hand off to aj or later")
    if not str(data.get("next_theme", "")).strip():
        fail("next_theme must remain nonempty")

    atlas_locks = [
        "Z(P+T0)=-S^2*X^2/Z(P)",
        "Z_-=-U*V/X2^2",
        "D_-^2=(H2-S2)/gcd(N-,H2-S2)",
        "Z_+=Z(P+T-)=-N+/R+",
        "Q*K=s*t=X2/kappa",
        "(D_-)_good       = q-+",
        "There is no free `2^{-omega}` density factor.",
    ]
    for lock in atlas_locks:
        require(atlas, lock, "compact torsion atlas")

    source_locks = {
        "stages/stage14/14-s6-05/result.md": [
            "T0_TRANSLATION_FORMULA_EXACT=true",
            "COMPACT_TRANSLATE_NONZERO_MOD_2=true",
            "PHYSICAL_COMPACT_TAU_PACKET_COUNT=4",
            "TORSION_TRANSLATE_DENOMINATOR_INVOLUTION_EXACT=true",
        ],
        "stages/stage14/14-s6-06/result.md": [
            "PHYSICAL_GAP_FACTORIZATION_EXACT=true",
            "PARTNER_HALF_ANGLE_DIVISOR_D_T=true",
            "HALF_ANGLE_CANCELLATION_COFACTOR_EXACT=true",
            "GOOD_ODD_T0_ROOT_SIGN_LAW=true",
        ],
        "stages/stage14/14-s6-07/result.md": [
            "DUAL_COMPACT_HALF_ANGLE_SELECTORS_EXACT=true",
            "GOOD_ODD_ROOT_SIGN_GCD_MATRIX_EXACT=true",
            "GOOD_PART_X2_FOUR_GCD_CELL_PRODUCT=true",
            "ROOT_SIGN_INDEPENDENT_BERNOULLI_MODEL_JUSTIFIED=false",
        ],
        "stages/stage14/14-4bl/result.md": [
            "DUAL_PRODUCT_IDENTITY=Q*K=X2/kappa",
            "DUAL_CANCELLATION_SQUARE_DIVIDES_NPLUS_NMINUS=true",
            "JOINT_DUAL_SELECTOR_INCIDENCE_THEOREM_PROVED=false",
        ],
    }
    for path, locks in source_locks.items():
        text = (ROOT / path).read_text(encoding="utf-8")
        for lock in locks:
            require(text, lock, path)

    result_locks = [
        "STAGE14_TOOLBOX_AI=COMPLETE_COMPACT_TORSION_DENOMINATOR_AND_HALF_ANGLE_ATLAS",
        "CANONICAL_NEW_CARD_COUNT=9",
        "CANONICAL_TOTAL_CARD_COUNT=57",
        "PHYSICAL_COMPACT_TAU_PACKET_COUNT=4",
        "DUAL_PRODUCT_IDENTITY_QK_EQUAL_X2_OVER_KAPPA_FROZEN=true",
        "ROOT_SIGN_INDEPENDENT_BERNOULLI_MODEL_ALLOWED=false",
        "GENERIC_D_IDENTIFIED_WITH_COMPACT_SELECTOR=false",
        "D_MIN_IDENTIFIED_WITH_DUAL_SELECTORS=false",
        "CURRENT_WHOLE_FAMILY_EXPONENT=20/21",
        "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
        "NEXT=Stage14-toolbox-aj quantifier-mismatch and invalid-shortcut warnings",
    ]
    for lock in result_locks:
        require(result, lock, "toolbox-ai result")

    involution_checks = audit_t0_involution()
    half_angle_checks, dual_checks = audit_half_angle_and_dual_product()

    if Fraction(20,21) - Fraction(1,2) != Fraction(19,42):
        fail("current main sqrt-gap arithmetic regressed")

    print(json.dumps({
        "stage": "14-toolbox-ai",
        "classification": "COMPACT_TORSION_HALF_ANGLE_ATLAS_AUDIT",
        "canonical_card_count": len(cards),
        "new_card_count": len(EXPECTED),
        "t0_involution_checks": involution_checks,
        "half_angle_normalizations_checked": half_angle_checks,
        "dual_product_checks": dual_checks,
        "current_main_exponent": "20/21",
        "new_whole_family_saving_claimed": False,
        "next_stage": data["next_stage"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
