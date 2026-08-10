#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
RESULT = ROOT / "stages/stage14/14-toolbox-al/result.md"

AL_EXPECTED = {
    "TB-RECIPE-cookbook-local-global-witness": (345, "86b91ffcd8bae79452ef75f187c8570a3819d386"),
    "TB-RECIPE-cookbook-witness-kernel-geometry": (355, "7ab3c21cc07714b24edfa1a36425b4beaeb2a6e7"),
    "TB-RECIPE-cookbook-compact-physical": (365, "dffc5669ca73c4bb7e4b5115e1fe238dde5605ae"),
    "TB-RECIPE-cookbook-fixed-fiber-active-direction": (373, "54aa839606d2ebeee8747837acec940da26a1534"),
    "TB-RECIPE-cookbook-one-cell-18-19": (417, "29e08fea3ebc1838fde2418957b9c0490456e1b1"),
    "TB-LEMMA-main-s-one-cell-convergence-18-19": (418, "7589d54816852529ce40db404a2ced2381656e1f"),
    "TB-RECIPE-cookbook-two-cell-conditional-gate": (419, "dcfe86c8002b8f403fe3f35315bf71288f8be875"),
    "TB-WARNING-proved-vs-conditional-recipe-status": (419, "dcfe86c8002b8f403fe3f35315bf71288f8be875"),
    "TB-RECIPE-cookbook-thick-reoptimized-15-16": (422, "6774b9b6fb662cb14cc221c0b56bb74c077a3659"),
    "TB-LEDGER-current-whole-family-after-4bx": (422, "6774b9b6fb662cb14cc221c0b56bb74c077a3659"),
    "TB-LEDGER-updated-conditional-two-cell-after-4bx": (422, "6774b9b6fb662cb14cc221c0b56bb74c077a3659"),
}


def main() -> None:
    data = json.loads(INDEX.read_text())
    cards = {c["id"]: c for c in data["cards"]}
    assert len(cards) == len(data["cards"])
    assert len(cards) >= 87
    for cid, (pr, sha) in AL_EXPECTED.items():
        c = cards[cid]
        assert c["source_pr"] == pr
        assert c["source_merge_sha"] == sha
        assert (ROOT / c["path"]).exists()
        for src in c["source_files"]:
            assert (ROOT / src).exists()

    # Later toolbox stages may supersede the two terminal al ledgers/recipe,
    # but their provenance and al result boundary remain immutable.
    assert cards["TB-RECIPE-cookbook-two-cell-conditional-gate"]["status"] in {"CURRENT", "SUPERSEDED"}
    assert cards["TB-LEDGER-current-whole-family-after-4bx"]["status"] in {"CURRENT", "SUPERSEDED"}
    assert cards["TB-LEDGER-updated-conditional-two-cell-after-4bx"]["status"] in {"CURRENT", "SUPERSEDED"}

    result = RESULT.read_text()
    for token in [
        "STAGE14_TOOLBOX_AL=COMPLETE_PROOF_RECIPE_COOKBOOK_AND_RECEIVER_CHECKLISTS",
        "CANONICAL_TOTAL_CARD_COUNT=87",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=15/16",
        "UPDATED_TWO_CELL_CONDITIONAL_TARGET=13/14",
        "NEXT=Stage14-toolbox-am external theorem hypothesis contract and import checklist",
    ]:
        assert token in result

    print(json.dumps({
        "stage": "14-toolbox-al",
        "classification": "FORWARD_COMPATIBLE_FROZEN_INTERFACE_REGRESSION",
        "historical_card_count": 87,
        "live_card_count": len(cards),
        "historical_current_exponent": "15/16",
        "historical_conditional_target": "13/14",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
