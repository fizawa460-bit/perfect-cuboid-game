#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
INVENTORY = Path(__file__).with_name("stage32-pr-workflow-trigger-inventory-20260911.json")


def top_level_on_block(text: str) -> str:
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "on:" and not line.startswith((" ", "\t")):
            start = i + 1
            break
    if start is None:
        raise AssertionError("missing top-level on: block")
    out: list[str] = []
    for line in lines[start:]:
        if line and not line.startswith((" ", "\t")) and not line.lstrip().startswith("#"):
            break
        out.append(line)
    return "\n".join(out)


def events(path: Path) -> set[str]:
    block = top_level_on_block(path.read_text())
    return set(re.findall(r"^\s{2}([A-Za-z0-9_-]+):", block, flags=re.MULTILINE))


def main() -> None:
    inv = json.loads(INVENTORY.read_text())
    groups = {k: inv[k] for k in ("active_auto", "manual", "retired")}
    flattened = [p for values in groups.values() for p in values]
    assert len(flattened) == len(set(flattened)), "duplicate workflow path in inventory"
    assert len(flattened) == inv["counts"]["total"] == 41
    assert len(groups["active_auto"]) == inv["counts"]["active_auto"] == 3
    assert len(groups["manual"]) == inv["counts"]["manual"] == 2
    assert len(groups["retired"]) == inv["counts"]["retired"] == 36
    assert inv["notes"]["mathematical_authority_changed"] is True
    assert inv["notes"]["n356"] == "consumed historical Stage32 MAIN leaf; workflow_dispatch-only replay retained"

    failures: list[str] = []
    for cls, paths in groups.items():
        for rel in paths:
            path = ROOT / rel
            if not path.is_file():
                failures.append(f"{cls}: missing {rel}")
                continue
            ev = events(path)
            has_pr = bool({"pull_request", "pull_request_target"} & ev)
            if cls == "active_auto":
                if not has_pr:
                    failures.append(f"ACTIVE_AUTO missing PR trigger: {rel} events={sorted(ev)}")
            else:
                if has_pr:
                    failures.append(f"{cls.upper()} still has PR trigger: {rel} events={sorted(ev)}")
                if "workflow_dispatch" not in ev:
                    failures.append(f"{cls.upper()} missing workflow_dispatch: {rel} events={sorted(ev)}")

    if failures:
        raise SystemExit("\n".join(failures))

    print("PASS Stage32 PR workflow trigger lifecycle inventory")
    print("ACTIVE_AUTO=3 MANUAL=2 RETIRED=36 TOTAL=41")
    print("historical_or_manual_pr_auto_triggers=0")
    print("mathematical_authority_changed=true")


if __name__ == "__main__":
    main()
