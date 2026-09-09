#!/usr/bin/env python3
"""Instantiate a Mission DAG research harness.

Example:
  python instantiate_mission.py stages/stage40-ex1 stage40ex1 \
    "Decide the exact target statement" --max-parallel 8
"""

from __future__ import annotations

import argparse
import json
import pathlib


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("destination")
    p.add_argument("mission_id")
    p.add_argument("target")
    p.add_argument("--max-parallel", type=int, default=8)
    args = p.parse_args()
    if args.max_parallel < 1:
        p.error("--max-parallel must be positive")

    dst = pathlib.Path(args.destination)
    if dst.exists() and any(dst.iterdir()):
        raise SystemExit(f"refusing non-empty destination: {dst}")
    (dst / "nodes" / "N001").mkdir(parents=True, exist_ok=True)

    semantic = f"{args.mission_id}:root-target"
    mission = {
        "schema": "research-os-mission-dag/v1",
        "mission_id": args.mission_id,
        "target": args.target,
        "integration_surface": "UNSET",
        "max_parallel": args.max_parallel,
        "status": "ACTIVE",
        "operator_commands": {
            "start": f"research-start {args.mission_id}: {args.target}",
            "cycle": f"{args.mission_id}-mainbatch",
            "audit": f"{args.mission_id}-audit",
        },
        "nodes": [{
            "node_id": "N001",
            "semantic_key": semantic,
            "title": "Root mission target",
            "depends_on": [],
            "state_path": "nodes/N001/STATE.json",
            "status": "OPEN",
        }],
        "status_vocabulary": ["OPEN", "ACTIVE", "BLOCKED", "DONE", "SUPERSEDED", "AUDIT_REQUIRED"],
        "rules": {
            "frontier_is_derived": True,
            "search_before_create": True,
            "duplicate_semantic_key_forbidden": True,
            "retry_blocked_route_only_after_reopen_condition": True,
            "audit_credit_self_grant_forbidden": True,
            "merge_without_user_authorization_forbidden": True,
        },
    }
    state = {
        "schema": "research-os-mission-node/v1",
        "node_id": "N001",
        "semantic_key": semantic,
        "statement": args.target,
        "scope": {
            "population": "TO_BE_LOCKED",
            "field_or_model": "TO_BE_LOCKED",
            "quantifiers": "TO_BE_LOCKED",
            "required_output": "TO_BE_LOCKED",
        },
        "reuse_check": {"performed": False, "queries": [], "matches": [], "decision": "PENDING"},
        "attempts": [],
        "retained_result": None,
        "credit_ceiling": "NONE",
        "next_action": "LOCK_SCOPE_THEN_SEARCH_BEFORE_CREATE",
        "notes": [],
    }

    (dst / "MISSION.json").write_text(json.dumps(mission, indent=2) + "\n")
    (dst / "nodes" / "N001" / "STATE.json").write_text(json.dumps(state, indent=2) + "\n")

    template_dir = pathlib.Path(__file__).resolve().parent
    mainbatch = (template_dir / "MAINBATCH.template.md").read_text().replace("__MISSION__", args.mission_id)
    (dst / "MAINBATCH.md").write_text(mainbatch)

    print(f"created {args.mission_id} at {dst}")
    print(f"next operator command: {args.mission_id}-mainbatch")


if __name__ == "__main__":
    main()
