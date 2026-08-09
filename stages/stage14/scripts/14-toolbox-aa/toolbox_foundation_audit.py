#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
README = ROOT / "docs/stage14-toolbox/README.md"
SCHEMA = ROOT / "docs/stage14-toolbox/card-schema.md"
TEMPLATE = ROOT / "docs/stage14-toolbox/card-template.md"

HEX40 = re.compile(r"^[0-9a-f]{40}$")
CODE = re.compile(r"^[a-z]{2}$")
NEXT_STAGE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")


def next_code(code: str) -> str:
    if not CODE.fullmatch(code):
        raise ValueError(code)
    a, b = ord(code[0]) - 97, ord(code[1]) - 97
    b += 1
    if b == 26:
        b = 0
        a += 1
    if a == 26:
        raise OverflowError("toolbox two-letter namespace exhausted after zz")
    return chr(97 + a) + chr(97 + b)


def fail(msg: str) -> None:
    raise AssertionError(msg)


def main() -> None:
    for path in (INDEX, README, SCHEMA, TEMPLATE):
        if not path.exists():
            fail(f"missing toolbox foundation file: {path}")

    data = json.loads(INDEX.read_text(encoding="utf-8"))

    if data["toolbox"] != "Stage14-toolbox":
        fail("wrong toolbox name")
    if data["foundation_stage"] != "Stage14-toolbox-aa":
        fail("wrong foundation stage")
    if data["schema_version"] != 1:
        fail("unexpected schema version")

    expected_types = {"FORMULA", "LEMMA", "BOUND", "DICTIONARY", "RECIPE", "LEDGER", "WARNING"}
    expected_statuses = {"CURRENT", "SUPERSEDED", "DEPRECATED", "PARKED"}
    expected_scopes = {"MAIN", "S", "BOTH"}
    if set(data["allowed_types"]) != expected_types:
        fail("type enum drift")
    if set(data["allowed_statuses"]) != expected_statuses:
        fail("status enum drift")
    if set(data["allowed_scopes"]) != expected_scopes:
        fail("scope enum drift")

    numbering = data["numbering"]
    if numbering["first"] != "aa":
        fail("first toolbox code must be aa")
    if numbering["substage_suffix_default_allowed"]:
        fail("toolbox substages must not be default")

    successor_regression = {
        "aa": "ab",
        "ay": "az",
        "az": "ba",
        "by": "bz",
        "bz": "ca",
        "zy": "zz",
    }
    for old, expected in successor_regression.items():
        got = next_code(old)
        if got != expected:
            fail(f"successor mismatch {old}: {got} != {expected}")
    try:
        next_code("zz")
    except OverflowError:
        pass
    else:
        fail("zz must terminate the two-letter namespace")

    # Foundation invariants must remain true after later toolbox stages advance
    # the mutable registry. The initial aa->ab handoff is locked in README;
    # index.next_stage is deliberately allowed to move forward.
    next_stage = data["next_stage"]
    match = NEXT_STAGE.fullmatch(next_stage)
    if not match:
        fail(f"invalid current toolbox next_stage: {next_stage}")
    if match.group(1) == "aa":
        fail("current toolbox next_stage must advance beyond foundation aa")
    if not data["next_theme"].strip():
        fail("next theme must be nonempty")

    policy = data["source_policy"]
    if not policy["canonical_cards_require_merged_source"]:
        fail("canonical merged-source gate disabled")
    if policy["open_pr_may_be_canonical_source"]:
        fail("open PR canonicalization is forbidden")
    if not policy["source_merge_sha_required"]:
        fail("merge SHA provenance must be required")
    if policy["toolbox_may_strengthen_source_theorem"]:
        fail("toolbox must not strengthen source theorems")

    selection = data["selection_policy"]
    if selection["fixed_mathematical_roadmap"]:
        fail("toolbox must stay permanent/dynamic, not fixed-roadmap")
    if selection["future_main_result_required"] or selection["future_s_result_required"]:
        fail("toolbox must remain independent of future main/s progress")
    if not selection["historical_asset_mining_allowed"]:
        fail("historical mining must remain enabled")

    locks = data["safety_locks"]
    if any(locks.values()):
        fail("all unsafe implications must remain false")

    cards = data["cards"]
    ids: set[str] = set()
    for card in cards:
        required = {
            "id", "type", "status", "title", "scope",
            "source_stage", "source_pr", "source_merge_sha", "source_files"
        }
        missing = required - card.keys()
        if missing:
            fail(f"card missing fields {card.get('id')}: {sorted(missing)}")
        if card["id"] in ids:
            fail(f"duplicate card id: {card['id']}")
        ids.add(card["id"])
        if card["type"] not in expected_types:
            fail(f"bad card type: {card['id']}")
        if card["status"] not in expected_statuses:
            fail(f"bad card status: {card['id']}")
        if card["scope"] not in expected_scopes:
            fail(f"bad card scope: {card['id']}")
        if not isinstance(card["source_pr"], int) or card["source_pr"] <= 0:
            fail(f"bad source PR: {card['id']}")
        if not HEX40.fullmatch(card["source_merge_sha"]):
            fail(f"bad source merge SHA: {card['id']}")
        if not card["source_files"]:
            fail(f"empty source files: {card['id']}")
        for source_file in card["source_files"]:
            if not (ROOT / source_file).is_file():
                fail(f"missing source file for {card['id']}: {source_file}")
        if card["status"] == "SUPERSEDED" and not card.get("superseded_by"):
            fail(f"superseded card lacks successor: {card['id']}")
        if card["status"] == "DEPRECATED" and not card.get("deprecated_reason"):
            fail(f"deprecated card lacks reason: {card['id']}")

    readme = README.read_text(encoding="utf-8")
    schema = SCHEMA.read_text(encoding="utf-8")
    template = TEMPLATE.read_text(encoding="utf-8")

    text_locks = [
        "TOOLBOX_REQUIRES_FUTURE_MAIN_RESULT=false",
        "TOOLBOX_REQUIRES_FUTURE_S_RESULT=false",
        "TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false",
        "NEXT=Stage14-toolbox-ab cross-route variable and normalization dictionary",
    ]
    for lock in text_locks:
        if lock not in readme:
            fail(f"README contract missing: {lock}")

    for field in ("INPUT", "OUTPUT", "VARIABLE DICTIONARY", "USED BY", "DO NOT USE FOR", "PROVENANCE NOTES"):
        if field not in schema or field not in template:
            fail(f"card schema/template missing section: {field}")

    report = {
        "stage": "14-toolbox-aa",
        "classification": "PERMANENT_REUSABLE_RESEARCH_TOOLBOX_FOUNDATION_AUDIT",
        "schema_version": data["schema_version"],
        "canonical_card_count": len(cards),
        "numbering_regressions": successor_regression,
        "allowed_types": sorted(expected_types),
        "allowed_statuses": sorted(expected_statuses),
        "source_merge_gate": True,
        "future_main_dependency": False,
        "future_s_dependency": False,
        "fixed_mathematical_roadmap": False,
        "historical_asset_mining": True,
        "current_next_stage": data["next_stage"],
        "current_next_theme": data["next_theme"],
        "initial_handoff_locked_in_readme": "Stage14-toolbox-ab",
        "decision": {
            "TOOLBOX_FOUNDATION_VALID": True,
            "TWO_LETTER_NUMBERING_VALID": True,
            "CANONICAL_SOURCE_PROVENANCE_REQUIRED": True,
            "SUPERSESSION_CHAIN_SUPPORTED": True,
            "PROGRESS_INDEPENDENT_MAINTENANCE_SUPPORTED": True,
            "FOUNDATION_AUDIT_FORWARD_COMPATIBLE_WITH_LATER_TOOLBOX_STAGES": True,
            "NEW_THEOREM_OWNERSHIP": False
        }
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
