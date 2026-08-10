#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
ATLAS = ROOT / "docs/stage14-toolbox/barrier-obstruction-atlas.md"
SELECTOR = ROOT / "docs/stage14-toolbox/next-receiver-selector.md"
RESULT = ROOT / "stages/stage14/14-toolbox-an/result.md"
SHA40 = re.compile(r"^[0-9a-f]{40}$")
STAGE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")
SECTIONS = ["## INPUT", "## OUTPUT", "## VARIABLE DICTIONARY", "## USED BY", "## DO NOT USE FOR", "## PROVENANCE NOTES"]

EXPECTED = {
    "TB-DICTIONARY-obstruction-atlas-status": ("DICTIONARY", 437, "31c3636016f5f0ff80133f0c1b6a9cbbd91a3697"),
    "TB-LEDGER-current-7-8-critical-geometry": ("LEDGER", 438, "3fdad0c0673526ea39fed935b4ea69fcaf52a125"),
    "TB-LEMMA-shared-label-7-8-minimax-barrier": ("LEMMA", 438, "3fdad0c0673526ea39fed935b4ea69fcaf52a125"),
    "TB-RECIPE-realized-label-sparsity-improvement-contract": ("RECIPE", 438, "3fdad0c0673526ea39fed935b4ea69fcaf52a125"),
    "TB-RECIPE-transverse-coefficient-improvement-contract": ("RECIPE", 438, "3fdad0c0673526ea39fed935b4ea69fcaf52a125"),
    "TB-LEDGER-xi-k-offdiagonal-collision-target": ("LEDGER", 437, "31c3636016f5f0ff80133f0c1b6a9cbbd91a3697"),
    "TB-WARNING-fixed-xi-k-multiplicity-not-collision-saving": ("WARNING", 437, "31c3636016f5f0ff80133f0c1b6a9cbbd91a3697"),
    "TB-LEDGER-selector-sensitive-two-modulus-gap": ("LEDGER", 439, "72dd462552e64c312c13746f4533c5ef7512d52a"),
    "TB-WARNING-complete-cancellation-not-sparse-selector": ("WARNING", 439, "72dd462552e64c312c13746f4533c5ef7512d52a"),
    "TB-WARNING-pair-collapse-before-physical-cancellation-circular": ("WARNING", 439, "72dd462552e64c312c13746f4533c5ef7512d52a"),
    "TB-RECIPE-next-receiver-selector-7-8": ("RECIPE", 437, "31c3636016f5f0ff80133f0c1b6a9cbbd91a3697"),
}


def require(text: str, token: str, where: str) -> None:
    if token not in text:
        raise AssertionError(f"missing {token!r} in {where}")


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    cards = {c["id"]: c for c in data["cards"]}
    assert len(cards) == len(data["cards"]) == 109

    for c in data["cards"]:
        assert SHA40.fullmatch(c["source_merge_sha"]), (c["id"], c["source_merge_sha"])
        assert (ROOT / c["path"]).exists(), c["path"]
        for src in c["source_files"]:
            assert (ROOT / src).exists(), (c["id"], src)

    for cid, (ctype, pr, sha) in EXPECTED.items():
        card = cards[cid]
        assert (card["type"], card["status"], card["source_pr"], card["source_merge_sha"]) == (ctype, "CURRENT", pr, sha), cid
        text = (ROOT / card["path"]).read_text(encoding="utf-8")
        for section in SECTIONS:
            require(text, section, cid)

    current = cards["TB-LEDGER-current-whole-family-after-s7-13"]
    assert current["status"] == "CURRENT"
    assert current["source_pr"] == 434
    assert current["source_merge_sha"] == "079d053d1182e82a1924b37bba9ae33a3907f031"

    locks = data["safety_locks"]
    for key in [
        "xi_only_support_recount_beats_current_barrier",
        "fixed_xi_k_pointwise_multiplicity_implies_collision_power_saving",
        "complete_angular_bound_implies_sparse_physical_selector_bound",
        "pair_collapse_before_physical_cancellation_allowed",
        "t_two_modulus_receiver_implies_main_xi_k_collision_without_bridge",
        "correlated_two_cell_savings_may_be_multiplied_without_transverse_theorem",
    ]:
        assert locks.get(key) is False, key

    nxt = STAGE.fullmatch(data["next_stage"])
    assert nxt and nxt.group(1) >= "ao"
    assert data["next_theme"] == "critical-shell collision and second-moment interface contracts"

    atlas = ATLAS.read_text(encoding="utf-8")
    for token in [
        "CURRENT_CHECKPOINT",
        "HISTORICAL_ARCHITECTURE",
        "CLOSED_POSITIVE",
        "CLOSED_NEGATIVE",
        "LIVE_PRIMARY",
        "LIVE_BRIDGE",
        "SUPPORT_TRIGGERED",
        "FORBIDDEN",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8",
        "CURRENT_CRITICAL_SHARED_LABEL_EXPONENT=3/4",
        "PRIMARY_DIRECT_OBSTRUCTION=off-diagonal-(xi,k)-collision-energy",
        "TH14_NEEDED=true",
        "LARGE_XI_SUPPORT_ALONE_BEATS_7_8=false",
        "SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_PROVED=false",
    ]:
        require(atlas, token, "barrier atlas")

    selector = SELECTOR.read_text(encoding="utf-8")
    for token in [
        "DIRECT_GO",
        "BRIDGE_GO",
        "SUPPORT_GO",
        "PARK",
        "REJECT",
        "DIRECT_GO: XI_K_COLLISION_POWER_SAVING",
        "DIRECT_GO: REALIZED_XI_SPARSITY",
        "DIRECT_GO: TRANSVERSE_COEFFICIENT_GAIN",
        "REJECT: XI_ONLY_BARRIER_ALREADY_7_8",
        "OPERATOR_BRIDGE_REQUIRED=true|false",
        "PAIR_COLLAPSE_BEFORE_CANCELLATION=false",
        "TH14_NEEDED=true",
    ]:
        require(selector, token, "receiver selector")

    s713 = (ROOT / "stages/stage14/14-s7-13/result.md").read_text(encoding="utf-8")
    for token in [
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8",
        "CURRENT_GAP_TO_SQRT=3/8",
        "FULL_COORDINATE_REFINEMENT_ARCHITECTURE_BARRIER=7/8",
    ]:
        require(s713, token, "s7-13")

    s714 = (ROOT / "stages/stage14/14-s7-14/result.md").read_text(encoding="utf-8")
    for token in [
        "XI_ONLY_MINIMAX_CRITICAL_EXPONENT=gamma=3/4",
        "XI_ONLY_MINIMAX_BARRIER=7/8",
        "TRANSVERSE_LABEL_K=ker(Q^2-P^2)",
        "GCD_K_XI=1",
        "OFF_DIAGONAL_XI_K_COLLISION_ENERGY_RECEIVER_DEFINED=true",
        "FIXED_XI_K_POINTWISE_MULTIPLICITY_ALONE_GIVES_POWER_SAVING=false",
        "OFF_DIAGONAL_XI_K_COLLISION_POWER_SAVING_PROVED=false",
    ]:
        require(s714, token, "s7-14")

    cb = (ROOT / "stages/stage14/14-4cb/result.md").read_text(encoding="utf-8")
    for token in [
        "SHARED_LABEL_SUPPORT_EXPONENT=1/2+gamma/2",
        "SHARED_LABEL_TWO_CELL_EXPONENT=1-gamma/6",
        "SHARED_LABEL_CRITICAL_EXPONENT=3/4",
        "SHARED_LABEL_SUPPORT_PLUS_ONE_TWO_CELL_ARCHITECTURE_BARRIER=7/8",
        "REALIZED_LABEL_SPARSITY_POWER_SAVING_PROVED=false",
        "TRANSVERSE_COEFFICIENT_GAIN_PROVED=false",
    ]:
        require(cb, token, "4cb")

    t50 = (ROOT / "stages/stage14/14-t50/result.md").read_text(encoding="utf-8")
    for token in [
        "EXTERNAL_BAD_AUXILIARY_AGGREGATE_BOUND_PROVED=true",
        "TH8_PHYSICAL_ROUTE_B_EQUALS_T49_FROBENIUS_KERNEL=true",
        "TH11_MULTI_MODULUS_REOPEN_TRIGGER_HIT=true",
        "T32_COMPLETE_ANGULAR_BOUND_DIRECTLY_CONTROLS_SPARSE_PHYSICAL_SELECTOR=false",
        "SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_REQUIRED=true",
        "SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_PROVED=false",
        "TH14_NEEDED=true",
    ]:
        require(t50, token, "t50")

    g = Fraction(3, 4)
    assert Fraction(1,2) + g/2 == Fraction(7,8)
    assert Fraction(1,1) - g/6 == Fraction(7,8)
    assert Fraction(41,42) - Fraction(7,8) == Fraction(17,168)
    assert Fraction(7,8) - Fraction(1,2) == Fraction(3,8)
    delta = Fraction(1,12)
    e_delta = Fraction(1,1) - Fraction(1,1) / (Fraction(8,1) - 12*delta)
    assert e_delta == Fraction(6,7)
    eta = Fraction(1,12)
    e_eta = (Fraction(7,1) + 3*eta) / (Fraction(8,1) + 6*eta)
    assert e_eta < Fraction(7,8)

    result = RESULT.read_text(encoding="utf-8")
    for token in [
        "STAGE14_TOOLBOX_AN=COMPLETE_BARRIER_OBSTRUCTION_ATLAS_AND_NEXT_RECEIVER_SELECTOR",
        "CANONICAL_NEW_CARD_COUNT=11",
        "CANONICAL_TOTAL_CARD_COUNT=109",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8",
        "PRIMARY_DIRECT_OBSTRUCTION=OFF_DIAGONAL_XI_K_COLLISION_ENERGY",
        "T_TWO_MODULUS_TO_MAIN_XI_K_OPERATOR_BRIDGE_PROVED=false",
        "TH14_NEEDED=true",
        "TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false",
        "NEXT=Stage14-toolbox-ao critical-shell collision and second-moment interface contracts",
    ]:
        require(result, token, "toolbox-an result")

    print(json.dumps({
        "stage": "14-toolbox-an",
        "classification": "BARRIER_OBSTRUCTION_ATLAS_AND_NEXT_RECEIVER_SELECTOR_AUDIT",
        "canonical_card_count": len(cards),
        "new_card_count": len(EXPECTED),
        "current_whole_family_exponent": "7/8",
        "critical_xi_exponent": "3/4",
        "direct_primary": "xi-k offdiagonal collision energy",
        "support_trigger": "tH14",
        "toolbox_owned_new_theorem": False,
        "next_stage": data["next_stage"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
