#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
LEDGER = ROOT / "docs/stage14-toolbox/exponent-ledger.md"
RESULT = ROOT / "stages/stage14/14-toolbox-ac/result.md"

HEX40 = re.compile(r"^[0-9a-f]{40}$")

EXPECTED_NEW = {
    "TB-BOUND-local-descent-s5s": ("SUPERSEDED", 328, "3cbdde9bc94c55c63f72946805d3315e83c35097"),
    "TB-BOUND-local-descent-s5t": ("SUPERSEDED", 333, "9f9e74f22e80fb8432e865f3eebee8cd7c842fff"),
    "TB-BOUND-local-descent-current": ("CURRENT", 338, "516ffb08155e0aa618b2539efb07802a389ca219"),
    "TB-LEDGER-post-local-sqrt-gap": ("CURRENT", 341, "b4c9408441e501cb4d8f9a98b71f809d30a25f97"),
    "TB-BOUND-dual-half-angle-small-leg-sector": ("CURRENT", 365, "dffc5669ca73c4bb7e4b5115e1fe238dde5605ae"),
    "TB-LEDGER-s6-07-forced-incidence-scale": ("CURRENT", 364, "c51992e2373c0f7f265275c211684f6bd5ef9ccf"),
    "TB-WARNING-exponent-scope-and-transfer": ("CURRENT", 365, "dffc5669ca73c4bb7e4b5115e1fe238dde5605ae"),
}


def fail(msg: str) -> None:
    raise AssertionError(msg)


def require(text: str, needle: str, where: str) -> None:
    if needle not in text:
        fail(f"missing {needle!r} in {where}")


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    ledger = LEDGER.read_text(encoding="utf-8")
    result = RESULT.read_text(encoding="utf-8")

    cards = {card["id"]: card for card in data["cards"]}
    if len(cards) != len(data["cards"]):
        fail("duplicate card id")
    if len(cards) != 12:
        fail(f"expected 12 canonical cards after ac, got {len(cards)}")

    for card_id, (status, pr, merge_sha) in EXPECTED_NEW.items():
        if card_id not in cards:
            fail(f"missing ac card: {card_id}")
        card = cards[card_id]
        if card["status"] != status:
            fail(f"wrong status for {card_id}: {card['status']}")
        if card["source_pr"] != pr:
            fail(f"wrong source PR for {card_id}")
        if card["source_merge_sha"] != merge_sha or not HEX40.fullmatch(merge_sha):
            fail(f"wrong merge SHA for {card_id}")
        for source in card["source_files"]:
            if not (ROOT / source).exists():
                fail(f"missing source file for {card_id}: {source}")
        path = card.get("path")
        if not path or not (ROOT / path).exists():
            fail(f"missing card file for {card_id}: {path}")

    if cards["TB-BOUND-local-descent-s5s"].get("superseded_by") != "TB-BOUND-local-descent-s5t":
        fail("s5s supersession chain broken")
    if cards["TB-BOUND-local-descent-s5t"].get("superseded_by") != "TB-BOUND-local-descent-current":
        fail("s5t supersession chain broken")

    # Exact arithmetic: same normalized local problem.
    s5s_M = Fraction(1, 200)
    s5t_M = Fraction(1, 41)
    s5u_M = Fraction(1, 21)
    s5s_B_exp = Fraction(1, 1) - s5s_M / 2
    s5t_B_exp = Fraction(1, 1) - s5t_M / 2
    s5u_B_exp = Fraction(1, 1) - s5u_M / 2

    if s5s_B_exp != Fraction(399, 400):
        fail("s5s B conversion mismatch")
    if s5t_B_exp != Fraction(81, 82):
        fail("s5t B conversion mismatch")
    if s5u_B_exp != Fraction(41, 42):
        fail("s5u B conversion mismatch")
    if not (s5s_M < s5t_M < s5u_M):
        fail("local saving chain is not strictly improving")

    sqrt_target = Fraction(1, 2)
    post_gap = s5u_B_exp - sqrt_target
    if post_gap != Fraction(10, 21):
        fail("post-local sqrt gap mismatch")

    split = 2 * post_gap
    if split != Fraction(20, 21):
        fail("4bl optimal split mismatch")
    if s5u_B_exp - split != Fraction(1, 42):
        fail("4bl sector gain mismatch")
    if Fraction(41, 84) / 5 != Fraction(41, 420):
        fail("s6-07 five-factor exponent mismatch")

    if data["next_stage"] != "Stage14-toolbox-ad":
        fail("toolbox-ac must hand off to ad")
    if data["next_theme"] != "Pythagorean and Euclid conversion formulas":
        fail("unexpected ad theme")

    ledger_locks = [
        "CURRENT_LOCAL_M_SAVING=1/21",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=41/42",
        "REQUIRED_POST_LOCAL_SAVING=10/21",
        "4BL_SMALL_PARTNER_LEG_SECTOR_EXPONENT=20/21",
        "S6_07_FORCED_LARGE_INCIDENCE_CELL_EXPONENT=41/420",
        "sector exponent -> whole-family exponent",
        "forced variable size -> count saving",
    ]
    for lock in ledger_locks:
        require(ledger, lock, "exponent-ledger.md")

    result_locks = [
        "STAGE14_TOOLBOX_AC=COMPLETE_CURRENT_EXPONENT_AND_SAVING_LEDGER",
        "CURRENT_LOCAL_M_SAVING=1/21",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=41/42",
        "REQUIRED_POST_LOCAL_SAVING=10/21",
        "SECTORAL_EXPONENT_PROMOTED_TO_WHOLE_FAMILY=false",
        "FORCED_VARIABLE_SCALE_PROMOTED_TO_COUNT_SAVING=false",
        "SINGLE_EDGE_1_OVER_20_PROMOTED_TO_WHOLE_SYSTEM=false",
        "FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false",
        "OPEN_PR_USED_AS_CANONICAL_SOURCE=false",
        "NEXT=Stage14-toolbox-ad Pythagorean and Euclid conversion formulas",
    ]
    for lock in result_locks:
        require(result, lock, "14-toolbox-ac/result.md")

    # Check source theorem boundaries used to avoid false promotion.
    s5u = (ROOT / "stages/stage14/14-s5u/result.md").read_text(encoding="utf-8")
    bl = (ROOT / "stages/stage14/14-4bl/result.md").read_text(encoding="utf-8")
    s607 = (ROOT / "stages/stage14/14-s6-07/result.md").read_text(encoding="utf-8")
    require(s5u, "ACTUAL_LOCAL_SYSTEM_POWER_SAVING_EXPONENT=1/21", "s5u source")
    require(s5u, "ACTIVE_PHYSICAL_BASE_UPPER_BOUND_EXPONENT=41/42", "s5u source")
    require(bl, "SMALL_PARTNER_LEG_EDGE_BOUND=B^(20/21+o(1))", "4bl source")
    require(bl, "FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false", "4bl source")
    require(s607, "FORCED_LARGE_INCIDENCE_CELL_EXPONENT=41/420", "s6-07 source")
    require(s607, "FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false", "s6-07 source")

    report = {
        "stage": "14-toolbox-ac",
        "classification": "CURRENT_EXPONENT_AND_SAVING_LEDGER_AUDIT",
        "canonical_card_count": len(cards),
        "new_card_count": len(EXPECTED_NEW),
        "local_saving_chain_M": ["1/200", "1/41", "1/21"],
        "physical_exponent_chain_B": ["399/400", "81/82", "41/42"],
        "current_physical_exponent": "41/42",
        "sqrt_target": "1/2",
        "required_post_local_saving": "10/21",
        "sectoral": {
            "4bl_small_partner_leg_exponent": "20/21",
            "4bl_gain_vs_current": "1/42",
            "promoted_to_whole_family": False,
        },
        "structural": {
            "s6_07_forced_incidence_scale": "41/420",
            "promoted_to_count_saving": False,
        },
        "open_pr_canonical_source": False,
        "toolbox_owns_new_theorem": False,
        "next_stage": data["next_stage"],
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
