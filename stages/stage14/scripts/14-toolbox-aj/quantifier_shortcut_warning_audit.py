#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
ATLAS = ROOT / "docs/stage14-toolbox/quantifier-shortcut-warning-atlas.md"
RESULT = ROOT / "stages/stage14/14-toolbox-aj/result.md"
STAGE_CODE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")
SECTIONS = ["## INPUT", "## OUTPUT", "## VARIABLE DICTIONARY", "## USED BY", "## DO NOT USE FOR", "## PROVENANCE NOTES"]

EXPECTED = {
    "TB-WARNING-quantifier-ladder": (355, "7ab3c21cc07714b24edfa1a36425b4beaeb2a6e7"),
    "TB-WARNING-local-to-global-shortcut": (345, "86b91ffcd8bae79452ef75f187c8570a3819d386"),
    "TB-WARNING-necessary-sufficient-physical-image": (369, "e9916a9e21dc305fa30e240d3db962a26af1653b"),
    "TB-WARNING-fixed-object-moving-family": (395, "aa21a3604cf72e06f797c8ba2ecff96b49e60f44"),
    "TB-WARNING-sector-to-whole-family": (365, "dffc5669ca73c4bb7e4b5115e1fe238dde5605ae"),
    "TB-WARNING-structural-size-to-saving": (365, "dffc5669ca73c4bb7e4b5115e1fe238dde5605ae"),
    "TB-WARNING-deterministic-allocation-not-random": (364, "c51992e2373c0f7f265275c211684f6bd5ef9ccf"),
    "TB-WARNING-automatic-square-factor-double-count": (369, "e9916a9e21dc305fa30e240d3db962a26af1653b"),
    "TB-WARNING-fixed-fiber-active-direction": (373, "54aa839606d2ebeee8747837acec940da26a1534"),
    "TB-WARNING-stale-threshold-current-ledger": (396, "01afa63539e32e62070a84927bbc0530241a79e9"),
}


def fail(msg: str) -> None:
    raise AssertionError(msg)


def require(text: str, needle: str, where: str) -> None:
    if needle not in text:
        fail(f"missing {needle!r} in {where}")


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    atlas = ATLAS.read_text(encoding="utf-8")
    result = RESULT.read_text(encoding="utf-8")
    cards = {c["id"]: c for c in data["cards"]}

    if len(cards) != len(data["cards"]):
        fail("duplicate toolbox card id")
    if len(cards) < 67:
        fail(f"toolbox-aj expects at least 67 cards, got {len(cards)}")

    for cid, (pr, sha) in EXPECTED.items():
        card = cards.get(cid)
        if not card:
            fail(f"missing aj warning card {cid}")
        if (card["type"], card["status"], card["source_pr"], card["source_merge_sha"]) != ("WARNING", "CURRENT", pr, sha):
            fail(f"metadata mismatch for {cid}")
        text = (ROOT / card["path"]).read_text(encoding="utf-8")
        for sec in SECTIONS:
            require(text, sec, cid)
        for src in card["source_files"]:
            if not (ROOT / src).exists():
                fail(f"missing source file {src}")

    nxt = STAGE_CODE.fullmatch(data["next_stage"])
    if not nxt or nxt.group(1) < "ak":
        fail("toolbox registry must hand off to ak or later")
    if not str(data.get("next_theme", "")).strip():
        fail("next_theme must remain nonempty")

    safety = data.get("safety_locks", {})
    required_false = [
        "local_solubility_implies_global_solubility",
        "coordinate_density_saving_implies_packet_count_saving_without_transfer",
        "fixed_curve_bound_implies_moving_family_bound",
        "deterministic_allocation_implies_random_density",
        "automatic_square_factor_may_be_recharged",
        "fixed_fiber_sparsity_implies_active_direction_sparsity",
    ]
    for key in required_false:
        if safety.get(key) is not False:
            fail(f"safety lock not false: {key}")

    atlas_locks = [
        "local state",
        "Coordinate density -> packet existence",
        "Local -> global",
        "Necessary physical-image equation -> converse",
        "Fixed genus-one curve -> moving family",
        "Sector exponent -> whole-family exponent",
        "Large structural parameter -> saving",
        "Deterministic divisor allocation -> random signs",
        "Automatic square factor -> fresh sieve factor",
        "Fixed-fiber sparsity -> active-direction sparsity",
        "Historical threshold -> current gap",
        "SOURCE LEVEL",
        "TARGET LEVEL",
    ]
    for lock in atlas_locks:
        require(atlas, lock, "warning atlas")

    result_locks = [
        "STAGE14_TOOLBOX_AJ=COMPLETE_QUANTIFIER_MISMATCH_AND_INVALID_SHORTCUT_WARNING_ATLAS",
        "CANONICAL_NEW_CARD_COUNT=10",
        "CANONICAL_TOTAL_CARD_COUNT=67",
        "QUANTIFIER_LADDER_FROZEN=true",
        "COORDINATE_DENSITY_TO_PACKET_EXISTENCE_SHORTCUT_ALLOWED=false",
        "LOCAL_TO_GLOBAL_SHORTCUT_ALLOWED=false",
        "FIXED_OBJECT_TO_MOVING_FAMILY_SHORTCUT_ALLOWED=false",
        "SECTOR_TO_WHOLE_FAMILY_SHORTCUT_ALLOWED=false",
        "AUTOMATIC_SQUARE_FACTOR_RECHARGE_ALLOWED=false",
        "FIXED_FIBER_TO_ACTIVE_DIRECTION_SPARSITY_SHORTCUT_ALLOWED=false",
        "CURRENT_WHOLE_FAMILY_EXPONENT=20/21",
        "CURRENT_REMAINING_GAP_TO_SQRT=19/42",
        "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
        "NEXT=Stage14-toolbox-ak proof-receiver dispatch and lemma dependency map",
    ]
    for lock in result_locks:
        require(result, lock, "toolbox-aj result")

    if Fraction(20, 21) - Fraction(1, 2) != Fraction(19, 42):
        fail("current sqrt-gap arithmetic regressed")

    print(json.dumps({
        "stage": "14-toolbox-aj",
        "classification": "QUANTIFIER_SHORTCUT_WARNING_AUDIT",
        "canonical_card_count": len(cards),
        "new_warning_card_count": len(EXPECTED),
        "current_main_exponent": "20/21",
        "current_gap_to_sqrt": "19/42",
        "new_theorem_claimed": False,
        "next_stage": data["next_stage"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
