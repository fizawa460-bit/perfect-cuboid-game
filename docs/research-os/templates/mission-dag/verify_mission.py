#!/usr/bin/env python3
"""Cheap structural verifier for a Research OS Mission DAG.

Usage:
  python verify_mission.py path/to/MISSION.json

The verifier checks orchestration consistency only. It does not certify
mathematical truth, proof authority, hostile-audit credit, or merge readiness.
"""

from __future__ import annotations

import json
import pathlib
import sys

ALLOWED = {"OPEN", "ACTIVE", "BLOCKED", "DONE", "SUPERSEDED", "AUDIT_REQUIRED"}


def die(msg: str) -> None:
    raise SystemExit(f"FAIL: {msg}")


def load(path: pathlib.Path):
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        die(f"cannot read {path}: {exc}")


def main() -> None:
    mission_path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "MISSION.json").resolve()
    mission = load(mission_path)
    root = mission_path.parent

    if mission.get("schema") != "research-os-mission-dag/v1":
        die("unexpected mission schema")
    if not isinstance(mission.get("max_parallel"), int) or mission["max_parallel"] < 1:
        die("max_parallel must be a positive integer")

    nodes = mission.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        die("mission must contain at least one node")

    by_id = {}
    semantic = {}
    for node in nodes:
        nid = node.get("node_id")
        key = node.get("semantic_key")
        status = node.get("status")
        if not nid or nid in by_id:
            die(f"missing or duplicate node_id: {nid!r}")
        if not key or key in semantic:
            die(f"missing or duplicate semantic_key: {key!r}")
        if status not in ALLOWED:
            die(f"{nid}: invalid status {status!r}")
        by_id[nid] = node
        semantic[key] = nid

    for nid, node in by_id.items():
        deps = node.get("depends_on", [])
        if not isinstance(deps, list) or len(deps) != len(set(deps)):
            die(f"{nid}: dependencies must be a unique list")
        if nid in deps:
            die(f"{nid}: self dependency")
        missing = [d for d in deps if d not in by_id]
        if missing:
            die(f"{nid}: unknown dependencies {missing}")

    # DAG cycle check.
    visiting, done = set(), set()

    def visit(nid: str) -> None:
        if nid in done:
            return
        if nid in visiting:
            die(f"dependency cycle through {nid}")
        visiting.add(nid)
        for dep in by_id[nid].get("depends_on", []):
            visit(dep)
        visiting.remove(nid)
        done.add(nid)

    for nid in by_id:
        visit(nid)

    # DONE cannot outrun dependencies.
    for nid, node in by_id.items():
        if node["status"] == "DONE":
            not_done = [d for d in node.get("depends_on", []) if by_id[d]["status"] != "DONE"]
            if not_done:
                die(f"{nid}: DONE while dependencies are not DONE: {not_done}")

    # Verify node state files when materialized.
    for nid, node in by_id.items():
        state_path = node.get("state_path")
        if not state_path:
            die(f"{nid}: missing state_path")
        path = root / state_path
        if not path.exists():
            # Template/initial planning may declare nodes before state materialization.
            if node["status"] != "OPEN":
                die(f"{nid}: state file missing for status {node['status']}: {path}")
            continue
        state = load(path)
        if state.get("node_id") != nid:
            die(f"{nid}: STATE node_id mismatch")
        if state.get("semantic_key") != node["semantic_key"]:
            die(f"{nid}: STATE semantic_key mismatch")
        if node["status"] in {"ACTIVE", "BLOCKED", "DONE", "AUDIT_REQUIRED"}:
            if not state.get("reuse_check", {}).get("performed", False):
                die(f"{nid}: reuse_check must be performed before status {node['status']}")
        route_ids = []
        for attempt in state.get("attempts", []):
            rid = attempt.get("route_id")
            if not rid or rid in route_ids:
                die(f"{nid}: missing or duplicate route_id {rid!r}")
            route_ids.append(rid)
            if attempt.get("status") == "BLOCKED":
                if not attempt.get("blocker") or not attempt.get("reopen_condition"):
                    die(f"{nid}/{rid}: BLOCKED requires blocker and reopen_condition")
        if node["status"] == "DONE" and state.get("retained_result") is None:
            die(f"{nid}: DONE requires retained_result")

    frontier = [
        nid
        for nid, node in by_id.items()
        if node["status"] == "OPEN"
        and all(by_id[d]["status"] == "DONE" for d in node.get("depends_on", []))
    ]

    print(json.dumps({
        "status": "PASS",
        "mission_id": mission.get("mission_id"),
        "node_count": len(nodes),
        "derived_ready_frontier": frontier,
        "max_parallel": mission["max_parallel"],
        "selected_capacity": min(len(frontier), mission["max_parallel"]),
        "mathematical_credit": "NONE",
        "audit_credit": "NONE"
    }, indent=2))


if __name__ == "__main__":
    main()
