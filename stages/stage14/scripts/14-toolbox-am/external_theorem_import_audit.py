#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
CONTRACT = ROOT / "docs/stage14-toolbox/external-theorem-import-contract.md"
TEMPLATE = ROOT / "docs/stage14-toolbox/external-theorem-import-checklist-template.md"
LEDGER = ROOT / "docs/stage14-toolbox/exponent-ledger.md"
COOKBOOK = ROOT / "docs/stage14-toolbox/proof-recipe-cookbook.md"
RESULT = ROOT / "stages/stage14/14-toolbox-am/result.md"
SHA40 = re.compile(r"^[0-9a-f]{40}$")
STAGE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")
SECTIONS = ["## INPUT", "## OUTPUT", "## VARIABLE DICTIONARY", "## USED BY", "## DO NOT USE FOR", "## PROVENANCE NOTES"]

EXPECTED = {
    "TB-DICTIONARY-external-theorem-import-status": ("DICTIONARY", "CURRENT", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-RECIPE-external-theorem-import-preflight": ("RECIPE", "CURRENT", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-RECIPE-katz-laumon-surface-stationary-phase-contract": ("RECIPE", "CURRENT", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-RECIPE-fu-newton-polyhedron-import-contract": ("RECIPE", "CURRENT", 426, "d04d777c5375e667af0be1ffa216fb0f79a950c4"),
    "TB-WARNING-theorem-name-match-not-hypothesis-match": ("WARNING", "CURRENT", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-WARNING-rejected-shortcut-must-stay-rejected": ("WARNING", "CURRENT", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-WARNING-finite-regression-not-theorem-import": ("WARNING", "CURRENT", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-LEMMA-main-s-two-cell-convergence-13-14": ("LEMMA", "CURRENT", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-RECIPE-cookbook-two-cell-proved-13-14": ("RECIPE", "CURRENT", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-LEDGER-current-whole-family-after-s7-10": ("LEDGER", "SUPERSEDED", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-LEDGER-current-whole-family-after-s7-13": ("LEDGER", "CURRENT", 434, "079d053d1182e82a1924b37bba9ae33a3907f031"),
}


def require(text: str, token: str, where: str) -> None:
    if token not in text:
        raise AssertionError(f"missing {token!r} in {where}")


def main() -> None:
    data = json.loads(INDEX.read_text())
    cards = {c["id"]: c for c in data["cards"]}
    assert len(cards) == len(data["cards"]) == 98

    for c in data["cards"]:
        assert SHA40.fullmatch(c["source_merge_sha"]), (c["id"], c["source_merge_sha"])
        assert (ROOT / c["path"]).exists(), c["path"]
        for src in c["source_files"]:
            assert (ROOT / src).exists(), src

    for cid, (ctype, status, pr, sha) in EXPECTED.items():
        c = cards[cid]
        assert (c["type"], c["status"], c["source_pr"], c["source_merge_sha"]) == (ctype, status, pr, sha), cid
        text = (ROOT / c["path"]).read_text()
        for section in SECTIONS:
            require(text, section, cid)

    assert cards["TB-LEDGER-current-whole-family-after-4bx"]["status"] == "SUPERSEDED"
    assert cards["TB-LEDGER-current-whole-family-after-4bx"]["superseded_by"] == "TB-LEDGER-current-whole-family-after-s7-10"
    assert cards["TB-LEDGER-current-whole-family-after-s7-10"]["superseded_by"] == "TB-LEDGER-current-whole-family-after-s7-13"
    assert cards["TB-LEDGER-updated-conditional-two-cell-after-4bx"]["status"] == "SUPERSEDED"
    assert cards["TB-RECIPE-cookbook-two-cell-conditional-gate"]["status"] == "SUPERSEDED"
    assert cards["TB-RECIPE-cookbook-two-cell-conditional-gate"]["superseded_by"] == "TB-RECIPE-cookbook-two-cell-proved-13-14"

    for key in [
        "finite_mixed_sum_evidence_implies_uniform_theorem",
        "external_theorem_name_match_implies_import",
        "external_theorem_import_without_full_hypothesis_map",
        "rejected_shortcut_may_be_reused_without_new_hypothesis_proof",
        "external_theorem_output_implies_whole_family_without_transfer",
    ]:
        assert data["safety_locks"].get(key) is False, key

    nxt = STAGE.fullmatch(data["next_stage"])
    assert nxt and nxt.group(1) >= "an"

    contract = CONTRACT.read_text()
    for token in [
        "CANDIDATE", "HYPOTHESIS_MAPPED", "REJECTED", "IMPORTED",
        "THEOREM_LOCATOR=", "SMOOTHNESS_OR_SNC_CONDITION=", "NONDEGENERACY_CONDITION=",
        "UNIFORMITY_PARAMETERS=", "EXCEPTIONAL_PARAMETERS=", "external complete-sum bound",
        "Katz 2007 nonsingular-polynomial route", "Katz--Laumon stationary phase",
        "Lei Fu Newton-polyhedron theorem", "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8",
    ]:
        require(contract, token, "import contract")

    template = TEMPLATE.read_text()
    for token in [
        "IMPORT_STATUS=CANDIDATE|HYPOTHESIS_MAPPED|REJECTED|IMPORTED",
        "CHECK_ALL_REQUIRED_HYPOTHESES_MAPPED=true|false",
        "CHECK_EXCEPTIONAL_STRATA_CLOSED=true|false",
        "CHECK_POST_THEOREM_TRANSFER_PROVED=true|false",
    ]:
        require(template, token, "import template")

    s710 = (ROOT / "stages/stage14/14-s7-10/result.md").read_text()
    for token in [
        "DIRECT_KATZ_2007_DELIGNE_POLYNOMIAL_SHORTCUT_APPLICABLE=false",
        "H_DIVISOR_SIMPLE_NORMAL_CROSSING=true",
        "ADJACENT_TWO_CELL_MIXED_FOURIER_OP_BOUND_PROVED=true",
        "TWO_CELL_RECTANGLE_EXPONENT=2/3",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=13/14",
    ]:
        require(s710, token, "s7-10 source")

    by = (ROOT / "stages/stage14/14-4by/result.md").read_text()
    for token in [
        "FU_TWISTED_EXPONENTIAL_SUM_COROLLARY_0_3_IMPORTED=true",
        "ADJACENT_TWO_CELL_RECTANGLE_EXPONENT=2/3",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=13/14",
    ]:
        require(by, token, "4by source")

    s713 = (ROOT / "stages/stage14/14-s7-13/result.md").read_text()
    for token in [
        "STAGE14_S7_13=COMPLETE_FULL_COORDINATE_CANONICAL_REFINEMENT_AND_7_8_BOUND",
        "MERGED_S7_10_TWO_CELL_THEOREM_IMPORTED=true",
        "COMMON_REFINEMENT_RECEIVER_IS_MIN_OF_TWO_VALID_BOUNDS=true",
        "FIXED_COORDINATE_AND_TWO_CELL_SAVINGS_MULTIPLIED=false",
        "FULL_COORDINATE_REFINEMENT_ARCHITECTURE_BARRIER=7/8",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8",
        "CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=17/168",
        "CURRENT_GAP_TO_SQRT=3/8",
    ]:
        require(s713, token, "s7-13 source")

    ledger = LEDGER.read_text()
    cookbook = COOKBOOK.read_text()
    for text, where in [(ledger, "ledger"), (cookbook, "cookbook")]:
        require(text, "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8", where)
        require(text, "CURRENT_REMAINING_GAP_TO_SQRT=3/8", where)
    require(cookbook, "Status: **PROVED CURRENT ARCHITECTURE**", "cookbook")
    require(cookbook, "Katz 2007 direct nonsingular-polynomial shortcut -> REJECTED", "cookbook")

    result = RESULT.read_text()
    for token in [
        "STAGE14_TOOLBOX_AM=COMPLETE_EXTERNAL_THEOREM_HYPOTHESIS_CONTRACT_AND_IMPORT_CHECKLIST",
        "CANONICAL_NEW_CARD_COUNT=11",
        "CANONICAL_TOTAL_CARD_COUNT=98",
        "KATZ_LAUMON_STATIONARY_PHASE_ROUTE_IMPORTED=true",
        "FU_COROLLARY_0_3_ROUTE_IMPORTED=true",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8",
        "CURRENT_REMAINING_GAP_TO_SQRT=3/8",
        "NEXT=Stage14-toolbox-an barrier and obstruction atlas / next-receiver selector",
    ]:
        require(result, token, "toolbox-am result")

    assert Fraction(15,16) - Fraction(13,14) == Fraction(1,112)
    assert Fraction(13,14) - Fraction(7,8) == Fraction(3,56)
    assert Fraction(41,42) - Fraction(7,8) == Fraction(17,168)
    assert Fraction(7,8) - Fraction(1,2) == Fraction(3,8)

    print(json.dumps({
        "stage": "14-toolbox-am",
        "classification": "EXTERNAL_THEOREM_IMPORT_AND_CURRENT_LEDGER_AUDIT",
        "canonical_card_count": len(cards),
        "new_card_count": len(EXPECTED),
        "current_whole_family_exponent": "7/8",
        "current_gap_to_sqrt": "3/8",
        "reusable_two_cell_checkpoint": "13/14",
        "imported_routes": ["Katz-Laumon", "Lei Fu Corollary 0.3"],
        "rejected_shortcuts": ["direct Katz 2007 nonsingular-polynomial shortcut"],
        "toolbox_owned_new_theorem": False,
        "next_stage": data["next_stage"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
