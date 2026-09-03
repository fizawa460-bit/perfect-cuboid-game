#!/usr/bin/env python3
"""Validate the compact Stage33 MAIN state during the post-V36 authority gate.

The former implementation regenerated a pre-V25 projection from controller.json.
That is unsafe while MAIN-STATE.authority_sync is ACTIVE_POST_V36_OVERRIDE,
because exact mathematical authority has advanced through V36 while the full
controller remains on the legacy route.  During this gate this command is
therefore deliberately read-only: both normal and --check modes verify the
V25/V33/V34/V35/V36/V37 source locks and compact routing state, and neither
mode overwrites MAIN-STATE.json.

A future coherent repair may replace this validator only when controller.json
and the generated compact projection are synchronized together.
"""
from __future__ import annotations

import argparse
import json
import runpy
from pathlib import Path

H = Path(__file__).resolve().parent
OUT = H / "MAIN-STATE.json"
VERIFY = H / "33-12/verify_j2_post_v36_authority_sync_v37.py"
RETIRED_HANDOFF = H / "MAIN-BATCH-HANDOFF.md"

parser = argparse.ArgumentParser()
parser.add_argument("--check", action="store_true")
args = parser.parse_args()

assert not RETIRED_HANDOFF.exists(), "MAIN-BATCH-HANDOFF.md is retired; use MAIN-STATE.work_checkpoint"
state = json.loads(OUT.read_text())
authority_sync = state.get("authority_sync", {})

if authority_sync.get("status") != "ACTIVE_POST_V36_OVERRIDE":
    raise SystemExit(
        "sync_main_state.py is intentionally read-only until the post-V36 gate "
        "is cleared by one coherent controller+generator synchronization."
    )

assert authority_sync.get("clear_only_after_controller_and_generator_are_synchronized_together") is True
assert authority_sync.get("legacy_generator_must_not_overwrite_main_state") is True
assert VERIFY.exists()

# The verifier source-locks the current exact frontier and all promotion firewalls.
runpy.run_path(str(VERIFY), run_name="__main__")

print(json.dumps({
    "success": True,
    "mode": "check" if args.check else "validate-no-write",
    "authority_sync": "ACTIVE_POST_V36_OVERRIDE",
    "main_state_overwritten": False,
    "legacy_v24_projection_regenerated": False,
    "marker": "MAIN_STATE_OVERRIDE_VALIDATED",
}, sort_keys=True))
