#!/usr/bin/env python3
"""Bind READY Mission-DAG nodes to stable human-facing lane commands.

Usage:
  python dispatch_ready.py path/to/MISSION.json

The dispatcher writes only MISSION.json.dispatch. It does not create Git
branches itself; the executing agent should create/use each recorded
work_branch before launching the lane. If fewer than two READY nodes exist,
no dispatch is issued because parallelism is not justified.
"""

from __future__ import annotations

import json
import pathlib
import string
import sys


def die(msg: str) -> None:
    raise SystemExit(f"FAIL: {msg}")


def load(path: pathlib.Path):
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        die(f"cannot read {path}: {exc}")


def main() -> None:
    mission_path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "MISSION.json")
    mission = load(mission_path)
    if mission.get("schema") != "research-os-mission-dag/v1":
        die("unexpected mission schema")

    nodes = mission.get("nodes", [])
    by_id = {n["node_id"]: n for n in nodes}
    ready = [
        n for n in nodes
        if n.get("status") == "OPEN"
        and all(by_id[d].get("status") == "DONE" for d in n.get("depends_on", []))
    ]

    cap = mission.get("max_parallel", 1)
    if not isinstance(cap, int) or cap < 1:
        die("max_parallel must be positive")

    mission_id = mission.get("mission_id")
    if not mission_id:
        die("missing mission_id")

    existing = mission.get("dispatch", {}).get("assignments", [])
    live_existing = [a for a in existing if a.get("node_id") in by_id and by_id[a["node_id"]].get("status") in {"OPEN", "ACTIVE"}]
    if live_existing:
        print(json.dumps({
            "status": "EXISTING_DISPATCH",
            "mission_id": mission_id,
            "parallel_commands": [a.get("command") for a in live_existing],
            "assignments": live_existing,
        }, indent=2))
        return

    if len(ready) < 2:
        print(json.dumps({
            "status": "NO_PARALLEL_DISPATCH",
            "mission_id": mission_id,
            "ready_count": len(ready),
            "reason": "fewer than two READY nodes",
            "next_command": f"{mission_id}-mainbatch",
        }, indent=2))
        return

    selected = ready[:cap]
    if len(selected) > len(string.ascii_lowercase):
        die("more than 26 parallel slots are not supported")

    previous_generation = mission.get("dispatch", {}).get("generation", 0)
    generation = previous_generation + 1
    assignments = []
    for slot, node in zip(string.ascii_lowercase, selected):
        assignments.append({
            "slot": slot,
            "node_id": node["node_id"],
            "node_title": node.get("title", node["node_id"]),
            "command": f"{mission_id}-{slot}",
            "work_branch": f"{mission_id}-lane-{slot}-g{generation}",
            "status": "ISSUED",
        })

    mission["dispatch"] = {
        "generation": generation,
        "assignments": assignments,
    }
    mission_path.write_text(json.dumps(mission, indent=2) + "\n")

    print(json.dumps({
        "status": "PARALLEL_DISPATCH_ISSUED",
        "mission_id": mission_id,
        "generation": generation,
        "parallel_commands": [a["command"] for a in assignments],
        "assignments": assignments,
        "human_action": "launch each command in a separate chat; keep mainbatch as the integrator",
    }, indent=2))


if __name__ == "__main__":
    main()
