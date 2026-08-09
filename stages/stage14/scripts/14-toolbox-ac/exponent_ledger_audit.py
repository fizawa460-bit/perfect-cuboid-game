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
STAGE_CODE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")

EXPECTED_AC = {
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


def stage_code(stage: str) -> str:
    m = STAGE_CODE.fullmatch(stage)
    if not m:
        fail(f"invalid toolbox next_stage: {stage}")
    return m.group(1)


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    ledger = LEDGER.read_text(encoding="utf-8")
    result = RESULT.read_text(encoding="utf-8")
    cards = {card["id"]: card for card in data["cards"]}
    if len(cards) != len(data["cards"]):
        fail("duplicate card id")
    if len(cards) < 12:
        fail(f"ac foundation requires at least 12 canonical cards, got {len(cards)}")

    for card_id, (status, pr, merge_sha) in EXPECTED_AC.items():
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

    s5s_M = Fraction(1, 200)
    s5t_M = Fraction(1, 41)
    s5u_M = Fraction(1, 21)
    s5s_B_exp = 1 - s5s_M / 2
    s5t_B_exp = 1 - s5t_M / 2
    s5u_B_exp = 1 - s5u_M / 2
    if s5s_B_exp != Fraction(399, 400):
        fail("s5s B conversion mismatch")
    if s5t_B_exp != Fraction(81, 82):
        fail("s5t B conversion mismatch")
    if s5u_B_exp != Fraction(41, 42):
        fail("s5u B conversion mismatch")
    if not (s5s_M < s5t_M < s5u_M):
        fail("local saving chain is not strictly improving")

    post_gap = s5u_B_exp - Fraction(1, 2)
    if post_gap != Fraction(10, 21):
        fail("post-local sqrt gap mismatch")
    if 2 * post_gap != Fraction(20, 21):
        fail("4bl optimal split mismatch")
    if s5u_B_exp - Fraction(20, 21) != Fraction(1, 42):
        fail("4bl sector gain mismatch")
    if Fraction(41, 84) / 5 != Fraction(41, 420):
        fail("s6-07 five-factor exponent mismatch")

    # ac originally handed off to ad. Later toolbox stages are allowed to advance the registry.
    if stage_code(data["next_stage"]) < "ad":
        fail("toolbox registry regressed before ad")
    if not str(data.get("next_theme", "")).strip():
        fail("toolbox next_theme must remain nonempty")

    for lock in [
        "CURRENT_LOCAL_M_SAVING=1/21",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=41/42",
        "REQUIRED_POST_LOCAL_SAVING=10/21",
        "4BL_SMALL_PARTNER_LEG_SECTOR_EXPONENT=20/21",
        "S6_07_FORCED_LARGE_INCIDENCE_CELL_EXPONENT=41/420",
        "sector exponent -> whole-family exponent",
        "forced variable size -> count saving",
    ]:
        require(ledger, lock, "exponent-ledger.md")

    for lock in [
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
    ]:
        require(result, lock, "14-toolbox-ac/result.md")

    s5u = (ROOT / "stages/stage14/14-s5u/result.md").read_text(encoding="utf-8")
    bl = (ROOT / "stages/stage14/14-4bl/result.md").read_text(encoding="utf-8")
    s607 = (ROOT / "stages/stage14/14-s6-07/result.md").read_text(encoding="utf-8")
    require(s5u, "ACTUAL_LOCAL_SYSTEM_POWER_SAVING_EXPONENT=1/21", "s5u source")
    require(s5u, "ACTIVE_PHYSICAL_BASE_UPPER_BOUND_EXPONENT=41/42", "s5u source")
    require(bl, "SMALL_PARTNER_LEG_EDGE_BOUND=B^(20/21+o(1))", "4bl source")
    require(bl, "FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false", "4bl source")
    require(s607, "FORCED_LARGE_INCIDENCE_CELL_EXPONENT=41/420", "s6-07 source")
    require(s607, "FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false", "s6-07 source")

    print(json.dumps({
        "stage": "14-toolbox-ac",
        "classification": "CURRENT_EXPONENT_AND_SAVING_LEDGER_AUDIT",
        "canonical_card_count": len(cards),
        "ac_card_count": len(EXPECTED_AC),
        "local_saving_chain_M": ["1/200", "1/41", "1/21"],
        "physical_exponent_chain_B": ["399/400", "81/82", "41/42"],
        "required_post_local_saving": "10/21",
        "forward_compatible_next_stage": data["next_stage"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
