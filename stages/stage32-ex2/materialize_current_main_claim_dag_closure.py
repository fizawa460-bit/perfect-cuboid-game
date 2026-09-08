#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REG = "stages/stage32/proof/CLAIM-REGISTRY.json"
LANES = "stages/stage32/proof/LANE-ADAPTERS.json"
HIST = {"DECLARED_GOAL", "SUPERSEDED", "REVOKED"}
BRANCH_ADAPTER = "S32.ADAPTER.EX_TO_MAIN_PROMOTION_BOUNDARY.V3"


def git(*args: str, binary: bool = False):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=not binary)


def blob(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def show_bytes(ref: str, path: str) -> bytes:
    return git("show", f"{ref}:{path}", binary=True)


def main() -> int:
    generated = json.loads((ROOT / REG).read_text())
    branch = json.loads(git("show", f"HEAD:{REG}"))
    lanes = json.loads((ROOT / LANES).read_text())
    branch_owned = {c["claim_id"] for c in branch["claims"] if c["claim_id"].startswith("S32.EX2.")}
    if any(c["claim_id"] == BRANCH_ADAPTER for c in branch["claims"]):
        branch_owned.add(BRANCH_ADAPTER)

    protected: set[str] = set()
    for c in generated["claims"]:
        if c["claim_id"] not in branch_owned:
            continue
        for lock in c.get("source_locks", []):
            protected.add(lock["path"])
        if c.get("replay_verifier"):
            protected.add(c["replay_verifier"])

    required: dict[str, str | None] = {}

    def require(path: str, expected: str | None) -> None:
        if path in protected:
            return
        old = required.get(path)
        if old is not None and expected is not None and old != expected:
            raise SystemExit(f"conflicting main source locks for {path}: {old} != {expected}")
        if path not in required or expected is not None:
            required[path] = expected

    for c in generated["claims"]:
        if c["claim_id"] in branch_owned:
            continue
        for lock in c.get("source_locks", []):
            p = lock["path"]
            if c.get("authority_status") in HIST and p.endswith("/MAIN-STATE.json"):
                continue
            require(p, lock.get("blob_sha1"))
        replay = c.get("replay_verifier")
        if replay:
            require(replay, None)

    for lane in lanes["lanes"]:
        if lane.get("lane") != "EX2":
            require(lane["state_path"], None)

    materialized: list[str] = []
    for p, expected in sorted(required.items()):
        path = ROOT / p
        if path.is_file():
            data = path.read_bytes()
            if expected is None or blob(data) == expected:
                continue
        main_data = show_bytes("origin/main", p)
        main_blob = blob(main_data)
        if expected is not None and main_blob != expected:
            raise SystemExit(f"origin/main does not satisfy registered lock {p}: {main_blob} != {expected}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(main_data)
        materialized.append(p)

    print(json.dumps({"materialized_count": len(materialized), "materialized": materialized}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
