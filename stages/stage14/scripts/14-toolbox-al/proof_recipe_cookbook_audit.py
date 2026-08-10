#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
COOKBOOK = ROOT / "docs/stage14-toolbox/proof-recipe-cookbook.md"
TEMPLATE = ROOT / "docs/stage14-toolbox/proof-recipe-checklist-template.md"
RESULT = ROOT / "stages/stage14/14-toolbox-al/result.md"
STAGE_CODE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")
SECTIONS = ["## INPUT", "## OUTPUT", "## VARIABLE DICTIONARY", "## USED BY", "## DO NOT USE FOR", "## PROVENANCE NOTES"]

EXPECTED = {
    "TB-RECIPE-cookbook-local-global-witness": ("RECIPE", 345, "86b91ffcd8bae79452ef75f187c8570a3819d386"),
    "TB-RECIPE-cookbook-witness-kernel-geometry": ("RECIPE", 355, "7ab3c21cc07714b24edfa1a36425b4beaeb2a6e7"),
    "TB-RECIPE-cookbook-compact-physical": ("RECIPE", 365, "dffc5669ca73c4bb7e4b5115e1fe238dde5605ae"),
    "TB-RECIPE-cookbook-fixed-fiber-active-direction": ("RECIPE", 373, "54aa839606d2ebeee8747837acec940da26a1534"),
    "TB-RECIPE-cookbook-one-cell-18-19": ("RECIPE", 417, "29e08fea3ebc1838fde2418957b9c0490456e1b1"),
    "TB-LEMMA-main-s-one-cell-convergence-18-19": ("LEMMA", 418, "7589d54816852529ce40db404a2ced2381656e1f"),
    "TB-RECIPE-cookbook-two-cell-conditional-gate": ("RECIPE", 419, "dcfe86c8002b8f403fe3f35315bf71288f8be875"),
    "TB-WARNING-proved-vs-conditional-recipe-status": ("WARNING", 419, "dcfe86c8002b8f403fe3f35315bf71288f8be875"),
    "TB-RECIPE-cookbook-thick-reoptimized-15-16": ("RECIPE", 422, "6774b9b6fb662cb14cc221c0b56bb74c077a3659"),
    "TB-LEDGER-current-whole-family-after-4bx": ("LEDGER", 422, "6774b9b6fb662cb14cc221c0b56bb74c077a3659"),
    "TB-LEDGER-updated-conditional-two-cell-after-4bx": ("LEDGER", 422, "6774b9b6fb662cb14cc221c0b56bb74c077a3659"),
}


def fail(msg: str) -> None:
    raise AssertionError(msg)


def require(text: str, needle: str, where: str) -> None:
    if needle not in text:
        fail(f"missing {needle!r} in {where}")


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    cookbook = COOKBOOK.read_text(encoding="utf-8")
    template = TEMPLATE.read_text(encoding="utf-8")
    result = RESULT.read_text(encoding="utf-8")
    cards = {c["id"]: c for c in data["cards"]}

    if len(cards) != len(data["cards"]):
        fail("duplicate toolbox card id")
    if len(cards) != 87:
        fail(f"toolbox-al expects exactly 87 cards, got {len(cards)}")

    for cid, (ctype, pr, sha) in EXPECTED.items():
        card = cards.get(cid)
        if card is None:
            fail(f"missing al card {cid}")
        if (card["type"], card["status"], card["source_pr"], card["source_merge_sha"]) != (ctype, "CURRENT", pr, sha):
            fail(f"metadata mismatch for {cid}")
        path = ROOT / card["path"]
        if not path.exists():
            fail(f"missing card file {path}")
        text = path.read_text(encoding="utf-8")
        for section in SECTIONS:
            require(text, section, cid)
        for source in card["source_files"]:
            if not (ROOT / source).exists():
                fail(f"missing canonical source {source}")

    old_current = cards.get("TB-LEDGER-current-whole-family-after-s7-08")
    if old_current is None or old_current.get("status") != "SUPERSEDED":
        fail("s7-08 ledger must be superseded after 4bx")
    if old_current.get("superseded_by") != "TB-LEDGER-current-whole-family-after-4bx":
        fail("s7-08 ledger supersession target mismatch")
    current = cards.get("TB-LEDGER-current-whole-family-after-4bx")
    if current is None or current.get("status") != "CURRENT":
        fail("4bx ledger must be current")

    locks = data.get("safety_locks", {})
    for key in [
        "receiver_composition_without_transfer_allowed",
        "conditional_recipe_may_promote_current_ledger",
        "finite_mixed_sum_evidence_implies_uniform_theorem",
    ]:
        if locks.get(key) is not False:
            fail(f"safety lock {key} must be false")

    nxt = STAGE_CODE.fullmatch(data["next_stage"])
    if not nxt or nxt.group(1) < "am":
        fail("registry must hand off to am or later")

    for heading in [
        "## 0. Universal preflight",
        "## 1. Recipe A",
        "## 2. Recipe B",
        "## 3. Recipe C",
        "## 4. Recipe D",
        "## 5. Recipe E",
        "## 6. Recipe F",
        "## 7. Recipe G",
        "## 8. Receiver-composition checklist",
        "## 9. New-result maintenance checklist",
        "## 10. Current boundary at toolbox-al",
    ]:
        require(cookbook, heading, "cookbook")

    cookbook_locks = [
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=15/16",
        "CURRENT_REMAINING_GAP_TO_SQRT=7/16",
        "HISTORICAL_ONE_CELL_WHOLE_FAMILY_EXPONENT=18/19",
        "HISTORICAL_S7_09_CONDITIONAL_WHOLE_FAMILY_EXPONENT=16/17",
        "UPDATED_CONDITIONAL_TWO_CELL_WHOLE_FAMILY_EXPONENT=13/14",
        "S7_09_TWO_CELL_MIXED_FOURIER_BOUND_PROVED=false",
        "Status: **PROVED HISTORICAL ARCHITECTURE**",
        "Status: **PROVED CURRENT ARCHITECTURE**",
        "Status: **CONDITIONAL RESEARCH RECIPE**",
        "Sequential one-cell savings do not automatically multiply.",
        "L=H^(4/5)",
        "N_packet << M*H^(-4/5) B^o(1)",
    ]
    for lock in cookbook_locks:
        require(cookbook, lock, "cookbook")

    for lock in [
        "RECIPE_STATUS=PROVED|CONDITIONAL|HEURISTIC",
        "MISSING_THEOREM_GATE=",
        "CURRENT_WHOLE_FAMILY_EXPONENT=15/16",
        "CURRENT_GAP_TO_SQRT=7/16",
        "CURRENT_CONDITIONAL_TWO_CELL_TARGET=13/14",
    ]:
        require(template, lock, "checklist template")

    s708 = (ROOT / "stages/stage14/14-s7-08/result.md").read_text(encoding="utf-8")
    for lock in [
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=18/19",
        "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true",
    ]:
        require(s708, lock, "s7-08 source")

    bw = (ROOT / "stages/stage14/14-4bw/result.md").read_text(encoding="utf-8")
    for lock in [
        "MERGED_S7_08_CANONICAL_18_19_SOURCE=true",
        "STAGE14_4BW_INDEPENDENT_REDERIVATION=true",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=18/19",
    ]:
        require(bw, lock, "4bw source")

    s709 = (ROOT / "stages/stage14/14-s7-09/result.md").read_text(encoding="utf-8")
    for lock in [
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=18/19",
        "ADJACENT_TWO_CELL_MIXED_FOURIER_OP_BOUND_PROVED=false",
        "CONDITIONAL_WHOLE_FAMILY_EXPONENT=16/17",
        "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
    ]:
        require(s709, lock, "s7-09 source")

    bx = (ROOT / "stages/stage14/14-4bx/result.md").read_text(encoding="utf-8")
    for lock in [
        "STAGE14_4BX=REOPTIMIZED_THICK_PACKET_SQUARE_SIEVE_AND_15_16_WHOLE_FAMILY_BOUND",
        "OPTIMAL_THICK_AUXILIARY_PRIME_SCALE=H^(4/5)",
        "THICK_PACKET_RELATIVE_SAVING=H^(-4/5)",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=15/16",
        "IMPROVEMENT_OVER_18_19=3/304",
        "CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=13/336",
        "CURRENT_GAP_TO_SQRT=7/16",
        "S7_09_TWO_CELL_MIXED_FOURIER_BOUND_PROVED=false",
        "UPDATED_CONDITIONAL_TWO_CELL_WHOLE_FAMILY_EXPONENT=13/14",
        "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true",
    ]:
        require(bx, lock, "4bx source")

    result_locks = [
        "STAGE14_TOOLBOX_AL=COMPLETE_PROOF_RECIPE_COOKBOOK_AND_RECEIVER_CHECKLISTS",
        "CANONICAL_NEW_CARD_COUNT=11",
        "CANONICAL_TOTAL_CARD_COUNT=87",
        "COOKBOOK_RECIPE_COUNT=7",
        "UNIVERSAL_PREFLIGHT_CHECK_COUNT=10",
        "RECEIVER_COMPOSITION_GATE_COUNT=4",
        "CURRENT_4BX_15_16_RECIPE_FROZEN=true",
        "TWO_CELL_RECIPE_STATUS=CONDITIONAL",
        "S7_09_TWO_CELL_MIXED_FOURIER_BOUND_PROVED=false",
        "HISTORICAL_TWO_CELL_CONDITIONAL_TARGET=16/17",
        "UPDATED_TWO_CELL_CONDITIONAL_TARGET=13/14",
        "CONDITIONAL_13_14_PROMOTED_TO_CURRENT=false",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=15/16",
        "CURRENT_REMAINING_GAP_TO_SQRT=7/16",
        "IMPROVEMENT_OVER_18_19=3/304",
        "CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=13/336",
        "NEW_WHOLE_FAMILY_POWER_SAVING_OWNED_BY_TOOLBOX_AL=false",
        "NEXT=Stage14-toolbox-am external theorem hypothesis contract and import checklist",
    ]
    for lock in result_locks:
        require(result, lock, "toolbox-al result")

    if Fraction(18, 19) - Fraction(15, 16) != Fraction(3, 304):
        fail("18/19 to 15/16 improvement arithmetic regressed")
    if Fraction(15, 16) - Fraction(1, 2) != Fraction(7, 16):
        fail("15/16 sqrt gap arithmetic regressed")
    if Fraction(41, 42) - Fraction(15, 16) != Fraction(13, 336):
        fail("post-local saving arithmetic regressed")
    if Fraction(18, 19) - Fraction(16, 17) != Fraction(2, 323):
        fail("historical conditional gain arithmetic regressed")
    if Fraction(15, 16) - Fraction(13, 14) != Fraction(1, 112):
        fail("updated conditional target gap arithmetic regressed")

    print(json.dumps({
        "stage": "14-toolbox-al",
        "classification": "PROOF_RECIPE_COOKBOOK_AUDIT",
        "canonical_card_count": len(cards),
        "new_card_count": len(EXPECTED),
        "cookbook_recipe_count": 7,
        "current_whole_family_exponent": "15/16",
        "current_gap_to_sqrt": "7/16",
        "historical_one_cell_exponent": "18/19",
        "updated_conditional_two_cell_exponent": "13/14",
        "conditional_promoted": False,
        "toolbox_owned_new_theorem": False,
        "next_stage": data["next_stage"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
