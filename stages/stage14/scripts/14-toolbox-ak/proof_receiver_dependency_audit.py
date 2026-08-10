#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
MAP = ROOT / "docs/stage14-toolbox/proof-receiver-dependency-map.md"
LEDGER = ROOT / "docs/stage14-toolbox/exponent-ledger.md"
RESULT = ROOT / "stages/stage14/14-toolbox-ak/result.md"
STAGE_CODE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")
SECTIONS = ["## INPUT", "## OUTPUT", "## VARIABLE DICTIONARY", "## USED BY", "## DO NOT USE FOR", "## PROVENANCE NOTES"]

EXPECTED = {
    "TB-DICTIONARY-proof-receiver-dispatch-levels": ("DICTIONARY", 417, "29e08fea3ebc1838fde2418957b9c0490456e1b1"),
    "TB-RECIPE-dispatch-local-to-global-witness": ("RECIPE", 345, "86b91ffcd8bae79452ef75f187c8570a3819d386"),
    "TB-RECIPE-dispatch-witness-to-radical-geometry": ("RECIPE", 355, "7ab3c21cc07714b24edfa1a36425b4beaeb2a6e7"),
    "TB-RECIPE-dispatch-compact-half-angle-physical": ("RECIPE", 365, "dffc5669ca73c4bb7e4b5115e1fe238dde5605ae"),
    "TB-RECIPE-dispatch-fixed-fiber-active-direction": ("RECIPE", 373, "54aa839606d2ebeee8747837acec940da26a1534"),
    "TB-RECIPE-dispatch-balanced-inert-square-sieve": ("RECIPE", 410, "c99aafc834defe32c232615b86cd6b367cf30e2d"),
    "TB-RECIPE-dispatch-shared-xi-cell-switch": ("RECIPE", 417, "29e08fea3ebc1838fde2418957b9c0490456e1b1"),
    "TB-WARNING-proof-receiver-composition-boundary": ("WARNING", 417, "29e08fea3ebc1838fde2418957b9c0490456e1b1"),
    "TB-LEDGER-current-whole-family-after-s7-08": ("LEDGER", 417, "29e08fea3ebc1838fde2418957b9c0490456e1b1"),
}


def fail(msg: str) -> None:
    raise AssertionError(msg)


def require(text: str, needle: str, where: str) -> None:
    if needle not in text:
        fail(f"missing {needle!r} in {where}")


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    mapping = MAP.read_text(encoding="utf-8")
    ledger = LEDGER.read_text(encoding="utf-8")
    result = RESULT.read_text(encoding="utf-8")
    cards = {c["id"]: c for c in data["cards"]}

    if len(cards) != len(data["cards"]):
        fail("duplicate toolbox card id")
    if len(cards) != 76:
        fail(f"toolbox-ak expects exactly 76 cards, got {len(cards)}")

    for cid, (ctype, pr, sha) in EXPECTED.items():
        card = cards.get(cid)
        if card is None:
            fail(f"missing ak card {cid}")
        if (card["type"], card["status"], card["source_pr"], card["source_merge_sha"]) != (ctype, "CURRENT", pr, sha):
            fail(f"metadata mismatch for {cid}")
        path = ROOT / card["path"]
        if not path.exists():
            fail(f"missing card file {path}")
        text = path.read_text(encoding="utf-8")
        for section in SECTIONS:
            require(text, section, cid)
        for src in card["source_files"]:
            if not (ROOT / src).exists():
                fail(f"missing canonical source {src}")

    old = cards.get("TB-LEDGER-current-main-after-4br")
    if old is None or old.get("status") != "SUPERSEDED":
        fail("4br ledger must be superseded")
    if old.get("superseded_by") != "TB-LEDGER-current-whole-family-after-s7-08":
        fail("4br ledger supersession target mismatch")

    current = cards["TB-LEDGER-current-whole-family-after-s7-08"]
    if current["status"] != "CURRENT":
        fail("s7-08 ledger must be current")

    nxt = STAGE_CODE.fullmatch(data["next_stage"])
    if not nxt or nxt.group(1) < "al":
        fail("toolbox registry must hand off to al or later")
    if data.get("safety_locks", {}).get("receiver_composition_without_transfer_allowed") is not False:
        fail("receiver composition safety lock must be false")

    map_locks = [
        "L0 local state / character row",
        "L8 whole physical family",
        "Never jump a level without a merged handoff theorem.",
        "TB-RECIPE-dispatch-shared-xi-cell-switch",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=18/19",
        "CURRENT_REMAINING_GAP_TO_SQRT=17/38",
    ]
    for lock in map_locks:
        require(mapping, lock, "dependency map")

    ledger_locks = [
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=18/19",
        "WHOLE_FAMILY_POST_LOCAL_SAVING_PROVED=11/798",
        "CURRENT_REMAINING_GAP_TO_SQRT=17/38",
        "HISTORICAL_4BR_WHOLE_FAMILY_EXPONENT=20/21",
        "S7_08_OPTIMAL_LAMBDA=9/19",
        "TB-LEDGER-current-whole-family-after-s7-08 [CURRENT]",
    ]
    for lock in ledger_locks:
        require(ledger, lock, "exponent ledger")

    source = (ROOT / "stages/stage14/14-s7-08/result.md").read_text(encoding="utf-8")
    for lock in [
        "STAGE14_S7_08=COMPLETE_SHARED_XI_CELL_SWITCH_AND_18_19_WHOLE_FAMILY_BOUND",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=18/19",
        "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true",
        "IMPROVEMENT_OVER_20_21=2/399",
        "CURRENT_GAP_TO_SQRT=17/38",
    ]:
        require(source, lock, "s7-08 source")

    result_locks = [
        "STAGE14_TOOLBOX_AK=COMPLETE_PROOF_RECEIVER_DISPATCH_AND_LEMMA_DEPENDENCY_MAP",
        "CANONICAL_NEW_CARD_COUNT=9",
        "CANONICAL_TOTAL_CARD_COUNT=76",
        "PROOF_RECEIVER_LEVEL_COUNT=9",
        "RECEIVER_COMPOSITION_WITHOUT_TRANSFER_ALLOWED=false",
        "HISTORICAL_4BR_LEDGER_SUPERSEDED=true",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=18/19",
        "CURRENT_REMAINING_GAP_TO_SQRT=17/38",
        "NEW_WHOLE_FAMILY_POWER_SAVING_OWNED_BY_TOOLBOX_AK=false",
        "NEXT=Stage14-toolbox-al proof recipe cookbook and receiver checklists",
    ]
    for lock in result_locks:
        require(result, lock, "toolbox-ak result")

    if Fraction(20,21) - Fraction(18,19) != Fraction(2,399):
        fail("20/21 to 18/19 improvement arithmetic regressed")
    if Fraction(18,19) - Fraction(1,2) != Fraction(17,38):
        fail("current sqrt gap arithmetic regressed")
    if Fraction(41,42) - Fraction(18,19) != Fraction(11,798):
        fail("cumulative post-local saving arithmetic regressed")

    print(json.dumps({
        "stage": "14-toolbox-ak",
        "classification": "PROOF_RECEIVER_DEPENDENCY_AUDIT",
        "canonical_card_count": len(cards),
        "new_card_count": len(EXPECTED),
        "receiver_level_count": 9,
        "current_whole_family_exponent": "18/19",
        "current_gap_to_sqrt": "17/38",
        "toolbox_owned_new_theorem": False,
        "next_stage": data["next_stage"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
