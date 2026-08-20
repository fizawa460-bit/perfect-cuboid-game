#!/usr/bin/env python3
"""Pause-aware entry point for the StructureRadar controller.

The initial repository-wide StructureRadar campaign is closed.  While the
post-close external-gate campaign is paused, explicitly classified auxiliary
A-lines are kept outside the active main-stage corpus.  Any other new/changed
source remains visible to the core verifier and therefore still forces a
refresh/reopen rather than being silently ignored.
"""

from __future__ import annotations

import json
from pathlib import Path

import structure_radar_core as core

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "docs" / "structure-radar" / "pause-scope-policy.json"


def load_policy() -> dict:
    return json.loads(POLICY_PATH.read_text(encoding="utf-8"))


POLICY = load_policy()
_ORIGINAL_TRACKED_PATHS = core.tracked_paths
_ORIGINAL_BUILD_CONTROLLER = core.build_controller


def pause_filtered_tracked_paths() -> list[str]:
    prefixes = tuple(item["prefix"] for item in POLICY.get("excluded_source_prefixes", []))
    return [path for path in _ORIGINAL_TRACKED_PATHS() if not path.startswith(prefixes)]


def pause_aware_controller(manifest: dict, queue: dict, registry: dict, progress: dict) -> dict:
    controller = _ORIGINAL_BUILD_CONTROLLER(manifest, queue, registry, progress)
    if POLICY.get("status") == "PAUSED_RETURN_TO_STAGE27" and controller["close_conditions"]["campaign_closed"]:
        controller["post_close"] = {
            "phase": "EXTERNAL_GATE_CLOSURE",
            "initial_campaign_closed": True,
            "campaign_state": "PAUSED_RETURN_TO_STAGE27",
            "normal_deepening_paused": True,
            "remaining_external_gates_mandatory_before_stage27": False,
            "return_targets": POLICY.get("return_targets", []),
            "pause_record": POLICY.get("pause_record"),
            "reopen_on_corpus_change": True,
            "reopen_requires_new_evidence_or_receiver_change": bool(
                POLICY.get("reopen_requires_new_evidence_or_receiver_change", True)
            ),
        }
        controller["next_expected_command"] = "NONE_STRUCTURE_RADAR_PAUSED"
    return controller


core.tracked_paths = pause_filtered_tracked_paths
core.build_controller = pause_aware_controller


if __name__ == "__main__":
    core.main()
