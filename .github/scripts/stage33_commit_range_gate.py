#!/usr/bin/env python3
"""Fail-closed PR commit-range gate for Stage33 artifact workflows."""
import fnmatch
import os
import re
import subprocess
from pathlib import Path


def emit(value):
    with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as out:
        out.write(f"authorized={str(value).lower()}\n")


def authorized():
    event = os.environ.get("EVENT", "")
    if event == "workflow_dispatch":
        return True
    if event != "pull_request" or os.environ.get("ACTION") != "synchronize":
        return False
    before = os.environ.get("BEFORE", "")
    head = os.environ.get("HEAD", "")
    if not re.fullmatch(r"[0-9a-f]{40}", before) or not re.fullmatch(r"[0-9a-f]{40}", head):
        return False
    subprocess.run(
        ["git", "fetch", "--no-tags", "--depth=1", "origin", before],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if subprocess.run(
        ["git", "cat-file", "-e", f"{before}^{{commit}}"], check=False
    ).returncode:
        return False
    workflow_ref = os.environ.get("WORKFLOW_REF", "")
    match = re.search(r"(\.github/workflows/[^@]+)@", workflow_ref)
    if not match:
        return False
    workflow_path = match.group(1).replace("\\", "/")
    lines = Path(workflow_path).read_text(encoding="utf-8").splitlines()
    patterns = []
    inside = False
    for line in lines:
        if re.match(r"^\s{4}paths:\s*$", line):
            inside = True
            continue
        if inside and line.strip() and len(line) - len(line.lstrip()) <= 4:
            break
        if inside:
            item = re.match(r"^\s{6}-\s+['\"](.+)['\"]\s*$", line)
            if item:
                pattern = item.group(1).replace("\\", "/")
                # A migration-only workflow edit cannot authorize its compute.
                if pattern != workflow_path:
                    patterns.append(pattern)
    if not patterns:
        return False
    changed = subprocess.check_output(
        ["git", "diff", "--name-only", before, head], text=True
    ).splitlines()
    changed = [path.replace("\\", "/") for path in changed]
    for path in changed:
        if any(fnmatch.fnmatchcase(path, pattern) for pattern in patterns):
            print(f"AUTHORIZED_PATH={path}")
            return True
    print("AUTHORIZED_PATH=NONE")
    return False


emit(authorized())
