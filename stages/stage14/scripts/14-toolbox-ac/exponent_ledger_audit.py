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
STAGE_CODE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")


def fail(msg: str) -> None:
    raise AssertionError(msg)


def require(text: str, needle: str, where: str) -> None:
    if needle not in text:
        fail(f"missing {needle!r} in {where}")


def require_any(text: str, needles: list[str], where: str) -> None:
    if not any(needle in text for needle in needles):
        fail(f"missing all semantic alternatives {needles!r} in {where}")


def stage_code(stage: str) -> str:
    m = STAGE_CODE.fullmatch(stage)
    if not m:
        fail(f"bad toolbox stage code {stage}")
    return m.group(1)


def resolve_current_ledger(cards: dict[str, dict]) -> str:
    cid = "TB-LEDGER-post-local-sqrt-gap"
    seen: set[str] = set()
    while True:
        if cid in seen:
            fail("ledger supersession cycle")
        seen.add(cid)
        card = cards.get(cid)
        if not card:
            fail(f"missing ledger card {cid}")
        status = card.get("status")
        if status == "CURRENT":
            return cid
        if status != "SUPERSEDED":
            fail(f"unexpected ledger status {cid}: {status}")
        nxt = card.get("superseded_by")
        if not nxt:
            fail(f"superseded ledger without successor {cid}")
        cid = nxt


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    ledger = LEDGER.read_text(encoding="utf-8")
    result = RESULT.read_text(encoding="utf-8")
    cards = {c["id"]: c for c in data["cards"]}

    if len(cards) != len(data["cards"]):
        fail("duplicate toolbox card id")

    expected_local = {
        "TB-BOUND-local-descent-s5s": ("SUPERSEDED", "TB-BOUND-local-descent-s5t"),
        "TB-BOUND-local-descent-s5t": ("SUPERSEDED", "TB-BOUND-local-descent-current"),
        "TB-BOUND-local-descent-current": ("CURRENT", None),
    }
    for cid, (status, successor) in expected_local.items():
        card = cards.get(cid)
        if not card or card.get("status") != status:
            fail(f"local bound status mismatch {cid}")
        if successor is not None and card.get("superseded_by") != successor:
            fail(f"local bound successor mismatch {cid}")
        if not (ROOT / card["path"]).exists():
            fail(f"missing local bound card file {cid}")

    current_id = resolve_current_ledger(cards)
    current_card = cards[current_id]
    if not (ROOT / current_card["path"]).exists():
        fail("current ledger card file missing")

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

    historical_gap = s5u_B_exp - Fraction(1, 2)
    if historical_gap != Fraction(10, 21):
        fail("historical post-local sqrt gap mismatch")
    if 2 * historical_gap != Fraction(20, 21):
        fail("4bl optimal split mismatch")
    if s5u_B_exp - Fraction(20, 21) != Fraction(1, 42):
        fail("4bl sector gain mismatch")
    if Fraction(41, 84) / 5 != Fraction(41, 420):
        fail("s6-07 five-factor exponent mismatch")

    if stage_code(data["next_stage"]) < "ad":
        fail("toolbox registry regressed before ad")
    if not str(data.get("next_theme", "")).strip():
        fail("toolbox next_theme must remain nonempty")

    # Freeze the ac-era mathematics semantically while allowing later toolbox
    # stages to reformat the live human-facing ledger and extend the current
    # supersession chain.
    for lock in [
        "CURRENT_LOCAL_M_SAVING=1/21",
        "CURRENT_LOCAL_PHYSICAL_BASELINE_EXPONENT=41/42",
        "41/42 - 1/2 = 10/21",
        "sector exponent -> whole-family exponent",
    ]:
        require(ledger, lock, "exponent-ledger.md")
    require_any(
        ledger,
        ["B^(41/420)", "S6_07_FORCED_LARGE_INCIDENCE_CELL_EXPONENT=41/420"],
        "exponent-ledger.md",
    )
    require_any(
        ledger,
        ["forced variable size -> count saving", "forced variable size", "FORCED_LARGE_INCIDENCE_CELL_EXPONENT"],
        "exponent-ledger.md",
    )

    current_main_exp = "41/42"
    if current_id == "TB-LEDGER-current-main-after-4bq":
        for lock in [
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=61/63",
            "WHOLE_FAMILY_POST_LOCAL_SAVING_PROVED=1/126",
            "CURRENT_REMAINING_GAP_TO_SQRT=59/126",
            "FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=true",
        ]:
            require(ledger, lock, "exponent-ledger.md")
        current_main_exp = "61/63"
    elif current_id == "TB-LEDGER-current-main-after-4br":
        for lock in [
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=20/21",
            "WHOLE_FAMILY_POST_LOCAL_SAVING_PROVED=1/42",
            "CURRENT_REMAINING_GAP_TO_SQRT=19/42",
            "FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=true",
        ]:
            require(ledger, lock, "exponent-ledger.md")
        current_main_exp = "20/21"
    else:
        require(ledger, "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=", "exponent-ledger.md")
        require(ledger, "CURRENT_REMAINING_GAP_TO_SQRT=", "exponent-ledger.md")
        current_main_exp = f"future:{current_id}"

    for lock in [
        "STAGE14_TOOLBOX_AC=COMPLETE_CURRENT_EXPONENT_AND_SAVING_LEDGER",
        "CURRENT_LOCAL_M_SAVING=1/21",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=41/42",
        "REQUIRED_POST_LOCAL_SAVING=10/21",
        "SECTORAL_EXPONENT_PROMOTED_TO_WHOLE_FAMILY=false",
    ]:
        require(result, lock, "toolbox-ac result")

    print(json.dumps({
        "stage": "14-toolbox-ac",
        "classification": "EXPONENT_LEDGER_AUDIT",
        "local_baseline": "41/42",
        "resolved_current_ledger_card": current_id,
        "resolved_current_main_exponent": current_main_exp,
        "historical_gap_to_sqrt": "10/21",
        "next_stage": data["next_stage"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
