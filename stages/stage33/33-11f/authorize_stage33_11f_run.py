#!/usr/bin/env python3
"""Fail-closed semantic run-key gate for the 33-11f exact verifier."""
from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path


KEY = "stages/stage33/33-11f/run-key.json"
LOCKS = {
    "stage": "33-11f",
    "purpose": "26-COLUMN-EXACT-CLOSURE",
    "source_pr": 1457,
    "source_audited_head": "433dc8f644ed173555c261fe1742e32851611ea9",
    "source_certificate_sha256": "1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426",
}


def emit(value, reason):
    print("AUTHORIZATION_REASON=" + reason)
    with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as out:
        out.write(f"authorized={str(value).lower()}\n")


def read_at(ref):
    return json.loads(subprocess.check_output(["git", "show", f"{ref}:{KEY}"], text=True))


def valid(obj):
    return all(obj.get(k) == v for k, v in LOCKS.items())


def main():
    if os.environ.get("EVENT") == "workflow_dispatch":
        current = json.loads(Path(KEY).read_text(encoding="utf-8"))
        emit(current.get("armed") is True and valid(current), "manual-current-key")
        return
    if os.environ.get("EVENT") != "pull_request" or os.environ.get("ACTION") != "synchronize":
        emit(False, "pull-request-opened-or-non-synchronize-is-cold")
        return
    before, head = os.environ.get("BEFORE", ""), os.environ.get("HEAD", "")
    if not re.fullmatch(r"[0-9a-f]{40}", before) or not re.fullmatch(r"[0-9a-f]{40}", head):
        emit(False, "invalid-commit-range")
        return
    subprocess.run(["git", "fetch", "--no-tags", "--depth=1", "origin", before], check=False)
    changed = subprocess.check_output(["git", "diff", "--name-only", before, head], text=True).splitlines()
    if KEY not in [path.replace("\\", "/") for path in changed]:
        emit(False, "dedicated-run-key-not-in-synchronize-range")
        return
    try:
        old, new = read_at(before), read_at(head)
    except Exception:
        emit(False, "run-key-history-unverifiable")
        return
    old_generation, new_generation = old.get("generation"), new.get("generation")
    authorized = (
        isinstance(old_generation, int)
        and isinstance(new_generation, int)
        and new_generation > old_generation
        and new.get("armed") is True
        and valid(new)
    )
    emit(authorized, "semantic-generation-advance" if authorized else "semantic-key-check-failed")


if __name__ == "__main__":
    main()
