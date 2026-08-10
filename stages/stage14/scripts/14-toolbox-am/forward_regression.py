#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
CONTRACT = ROOT / "docs/stage14-toolbox/external-theorem-import-contract.md"
TEMPLATE = ROOT / "docs/stage14-toolbox/external-theorem-import-checklist-template.md"
RESULT = ROOT / "stages/stage14/14-toolbox-am/result.md"
STAGE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")
SECTIONS = ["## INPUT", "## OUTPUT", "## VARIABLE DICTIONARY", "## USED BY", "## DO NOT USE FOR", "## PROVENANCE NOTES"]

EXPECTED = {
    "TB-DICTIONARY-external-theorem-import-status": ("DICTIONARY", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-RECIPE-external-theorem-import-preflight": ("RECIPE", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-RECIPE-katz-laumon-surface-stationary-phase-contract": ("RECIPE", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-RECIPE-fu-newton-polyhedron-import-contract": ("RECIPE", 426, "d04d777c5375e667af0be1ffa216fb0f79a950c4"),
    "TB-WARNING-theorem-name-match-not-hypothesis-match": ("WARNING", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-WARNING-rejected-shortcut-must-stay-rejected": ("WARNING", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-WARNING-finite-regression-not-theorem-import": ("WARNING", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-LEMMA-main-s-two-cell-convergence-13-14": ("LEMMA", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-RECIPE-cookbook-two-cell-proved-13-14": ("RECIPE", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-LEDGER-current-whole-family-after-s7-10": ("LEDGER", 425, "1fca91407117c6cf486483b49299733bbbbbd519"),
    "TB-LEDGER-current-whole-family-after-s7-13": ("LEDGER", 434, "079d053d1182e82a1924b37bba9ae33a3907f031"),
}


def require(text: str, token: str, where: str) -> None:
    if token not in text:
        raise AssertionError(f"missing {token!r} in {where}")


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    cards = {c["id"]: c for c in data["cards"]}
    assert len(cards) == len(data["cards"])
    assert len(cards) >= 98

    for cid, (ctype, pr, sha) in EXPECTED.items():
        card = cards.get(cid)
        assert card is not None, cid
        assert (card["type"], card["source_pr"], card["source_merge_sha"]) == (ctype, pr, sha), cid
        assert card["status"] in {"CURRENT", "SUPERSEDED"}, cid
        path = ROOT / card["path"]
        assert path.exists(), path
        text = path.read_text(encoding="utf-8")
        for section in SECTIONS:
            require(text, section, cid)

    # Historical supersession facts frozen by am.
    assert cards["TB-LEDGER-current-whole-family-after-4bx"]["status"] == "SUPERSEDED"
    assert cards["TB-LEDGER-current-whole-family-after-4bx"]["superseded_by"] == "TB-LEDGER-current-whole-family-after-s7-10"
    assert cards["TB-LEDGER-current-whole-family-after-s7-10"]["status"] == "SUPERSEDED"
    assert cards["TB-LEDGER-current-whole-family-after-s7-10"]["superseded_by"] == "TB-LEDGER-current-whole-family-after-s7-13"
    assert cards["TB-RECIPE-cookbook-two-cell-conditional-gate"]["status"] == "SUPERSEDED"
    assert cards["TB-RECIPE-cookbook-two-cell-conditional-gate"]["superseded_by"] == "TB-RECIPE-cookbook-two-cell-proved-13-14"

    # s7-13 was CURRENT at am time; later toolbox stages may supersede the global ledger.
    s713 = cards["TB-LEDGER-current-whole-family-after-s7-13"]
    assert s713["status"] in {"CURRENT", "SUPERSEDED"}
    if s713["status"] == "SUPERSEDED":
        assert s713.get("superseded_by")

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

    contract = CONTRACT.read_text(encoding="utf-8")
    for token in [
        "CANDIDATE", "HYPOTHESIS_MAPPED", "REJECTED", "IMPORTED",
        "Katz 2007 nonsingular-polynomial route",
        "Katz--Laumon stationary phase",
        "Lei Fu Newton-polyhedron theorem",
    ]:
        require(contract, token, "am import contract")

    template = TEMPLATE.read_text(encoding="utf-8")
    for token in [
        "IMPORT_STATUS=CANDIDATE|HYPOTHESIS_MAPPED|REJECTED|IMPORTED",
        "CHECK_ALL_REQUIRED_HYPOTHESES_MAPPED=true|false",
        "CHECK_EXCEPTIONAL_STRATA_CLOSED=true|false",
        "CHECK_POST_THEOREM_TRANSFER_PROVED=true|false",
    ]:
        require(template, token, "am import template")

    result = RESULT.read_text(encoding="utf-8")
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
        require(result, token, "toolbox-am historical result")

    print(json.dumps({
        "stage": "14-toolbox-am",
        "classification": "FORWARD_COMPATIBLE_EXTERNAL_THEOREM_IMPORT_REGRESSION",
        "historical_card_count": 98,
        "live_card_count": len(cards),
        "historical_current_exponent": "7/8",
        "next_stage": data["next_stage"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
