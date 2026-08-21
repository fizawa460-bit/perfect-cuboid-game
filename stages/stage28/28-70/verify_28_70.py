#!/usr/bin/env python3
"""Consistency verifier for the audited and merged Stage28 checkpoint70 closeout state."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label}: missing {needle!r}")


def main() -> None:
    result = read("stages/stage28/28-70/result.md")
    bundle = read("stages/stage28/28-70/self-contained-bundle.md")
    final = read("stages/stage28/final.md")
    audit = read("stages/stage28/28-70/audit.md")
    discovery = read("stages/stage28/28-70/discovery-ledger.md")
    arsenal = read("docs/stage28-arsenal-promotion.md")
    registry = json.loads(read("stages/stage28/28-70/closeout-registry.json"))
    controller = json.loads(read("stages/stage28/28-controller.json"))

    # Submission synthesis remains immutable provenance.
    require(result, "SYNTHESIS_STOP_RULE_SATISFIED=YES", "result")
    require(result, "SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false", "result")
    require(result, "PERFECT_CUBOID_CONCLUSION=NONE", "result")
    require(result, "ORDERING_THRESHOLD=K_28 compared with kappa/(24*pi*C_M2)", "result")

    require(bundle, "SYNTHESIS_STOP_RULE_SATISFIED=YES", "bundle")
    require(bundle, "Stage19 physical M4 rational curve: absent", "bundle")
    require(bundle, "Stage20 Saunderson physical M-degree: 6", "bundle")
    require(bundle, "Stage19 M6 absence: not proved", "bundle")
    require(bundle, "PERFECT_CUBOID_CONCLUSION=NONE", "bundle")

    # Post-audit authoritative final surface.
    require(final, "CHECKPOINT70_AUDIT=PASS", "final")
    require(final, "Stage19 every odd physical M-degree = absent", "final")
    require(final, "Stage20 Saunderson physical M-degree = 6", "final")
    require(final, "Stage19 physical M6 absence          = not proved", "final")
    require(final, "SYNTHESIS_STOP_RULE_SATISFIED=YES", "final")
    require(final, "STAGE29_OPEN_PR_REQUIRES_STAGE28_FINAL_REFRESH=true", "final")
    require(final, "PERFECT_CUBOID_CONCLUSION=NONE", "final")

    require(audit, "AUDIT_VERDICT=PASS", "audit")
    require(audit, "MECHANICAL_CLOSEOUT_REPAIR=ADD stages/stage28/final.md", "audit")
    require(audit, "OPEN_GATE_RESEARCH_REQUEST_READY_AUDIT=PASS", "audit")

    require(discovery, "DISCOVERY_LEDGER_STATUS=COMPLETE", "discovery")
    require(discovery, "REPO_REUSE_PREFLIGHT=PASS", "discovery")
    require(discovery, "NUM_REUSE_CHECK=PASS", "discovery")
    require(discovery, "S1415-ATTACK-0217", "discovery")
    require(discovery, "S1415-ATTACK-0224", "discovery")

    for weapon in ("S28-W01", "S28-W02", "S28-W03", "S28-W04"):
        require(arsenal, weapon, "arsenal")
    require(arsenal, "PROMOTION_AUDIT=PASS", "arsenal")

    assert registry["stage"] == "Stage28"
    assert registry["checkpoint"] == 70
    assert registry["status"] == "CLOSED_AUDITED_PASS_MERGED"
    assert registry["interaction"]["ordering_threshold_K28"] == "kappa/(24*pi*C_M2)"
    assert registry["known_results"]["source_target_ordering_identified"] is False
    assert registry["synthesis"]["synthesis_stop_rule_satisfied"] is True
    assert registry["firewalls"]["perfect_cuboid_conclusion"] == "NONE"
    assert registry["artifacts"]["final"] == "stages/stage28/final.md"
    assert registry["audit_status"] == "PASS"
    assert registry["closeout_pr"] == 1284
    assert registry["closeout_merge_commit"] == "a4b57ef8f776390a33faf6efe0766d676df33088"
    assert registry["close_stage_completed"] is True
    assert registry["merge_allowed"] is False
    assert registry["advance_allowed"] is False
    assert registry["stage29_refresh_required"] is True
    assert registry["next_expected_command"] == "Stage29-audit"

    assert controller["stage"] == "Stage28"
    assert controller["status"] == "CLOSED_AUDITED_PASS_MERGED"
    assert controller["current_checkpoint"] == 70
    assert controller["checkpoint_status"]["60"] == "R3_AUDITED_PASS_MERGED"
    assert controller["checkpoint_status"]["70"] == "AUDITED_PASS_MERGED"
    assert controller["checkpoint70"]["synthesis_stop_rule_satisfied"] is True
    assert controller["checkpoint70"]["source_target_asymptotic_ordering_identified"] is False
    assert controller["checkpoint70"]["final"] == "stages/stage28/final.md"
    assert controller["checkpoint70"]["audit_status"] == "PASS"
    assert controller["checkpoint70"]["pr"] == 1284
    assert controller["checkpoint70"]["merge_commit"] == "a4b57ef8f776390a33faf6efe0766d676df33088"
    assert controller["checkpoint70"]["stage29_refresh_required"] is True
    assert controller["audit_status"] == "PASS"
    assert controller["main_status"] == "CLOSED_AUDITED_PASS_MERGED"
    assert controller["advance_allowed"] is False
    assert controller["merge_allowed"] is False
    assert controller["next_expected_command"] == "Stage29-audit"

    print("Stage28-70 audited merged closeout consistency: PASS")


if __name__ == "__main__":
    main()
