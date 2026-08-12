#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
STAGE15 = ROOT / "stages/stage15"
CONFIG = STAGE15 / "15-6-controller.json"
SUBSTAGE_RE = re.compile(r"15-6([a-z]{2})$")
EXIT_RE = re.compile(r"^(STAGE15_6[A-Z0-9_]*EXIT)=(.+)$", re.MULTILINE)


def ordinal(code: str) -> int:
    return (ord(code[0]) - 97) * 26 + ord(code[1]) - 97


def discover() -> list[tuple[str, Path, Path]]:
    rows: list[tuple[str, Path, Path]] = []
    for directory in STAGE15.glob("15-6??"):
        match = SUBSTAGE_RE.fullmatch(directory.name)
        if not match or not (directory / "result.md").is_file():
            continue
        code = match.group(1)
        verifier = STAGE15 / "replay" / f"verify_stage15_6{code}.py"
        rows.append((code, directory / "result.md", verifier))
    return sorted(rows, key=lambda row: ordinal(row[0]))


def decide(latest_exit: str, failures: list[str]) -> tuple[str, bool, str]:
    if failures:
        return "CODEX", True, "aggregate verifier failure requires repository diagnosis"
    upper = latest_exit.upper()
    if "THEOREM_GATE" in upper or "AUDIT" in upper or "RECEIVER" in upper:
        return "CHATGPT_AUDIT", False, "fresh adversarial mathematical audit required"
    return "CHATGPT_MAIN", False, "continue the active exact route under the cycle protocol"


def main() -> int:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    rows = discover()
    if not rows:
        raise AssertionError("no Stage15-6 substages discovered")

    ordinals = [ordinal(code) for code, _, _ in rows]
    expected = list(range(ordinals[0], ordinals[-1] + 1))
    if ordinals != expected:
        raise AssertionError("Stage15-6 substage sequence has a gap")

    failures: list[str] = []
    for code, _, verifier in rows:
        if not verifier.is_file():
            failures.append(f"6{code}:missing verifier")
            continue
        run = subprocess.run(
            [sys.executable, str(verifier)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
        if run.returncode:
            tail = run.stderr.strip().splitlines()[-1] if run.stderr.strip() else "unknown failure"
            failures.append(f"6{code}:{tail}")

    latest_code, latest_result, _ = rows[-1]
    latest_text = latest_result.read_text(encoding="utf-8")
    exits = EXIT_RE.findall(latest_text)
    if not exits:
        failures.append(f"6{latest_code}:missing frozen EXIT field")
        latest_exit = "MISSING"
    else:
        latest_exit = exits[-1][1]

    owner, codex_required, reason = decide(latest_exit, failures)
    print(f"CONTROLLER_SCHEMA_VERSION={config['schema_version']}")
    print(f"CANONICAL_MAIN_COMMAND={config['canonical_commands']['main']}")
    print(f"CANONICAL_AUDIT_COMMAND={config['canonical_commands']['audit']}")
    print(f"DISCOVERED_SUBSTAGE_COUNT={len(rows)}")
    print(f"CURRENT_SUBSTAGE=15-6{latest_code}")
    print(f"CURRENT_EXIT={latest_exit}")
    print(f"ALL_PRIOR_CHECKS_PASS={'false' if failures else 'true'}")
    print(f"RECOMMENDED_OWNER={owner}")
    print(f"AUDIT_REQUIRED={'true' if owner == 'CHATGPT_AUDIT' else 'false'}")
    print(f"CODEX_REQUIRED={'true' if codex_required else 'false'}")
    print(f"CODEX_REASON={reason if codex_required else 'NONE'}")
    print("MERGE_ALLOWED=false")
    if failures:
        print("FAILURES=" + " | ".join(failures))
        return 1
    print("STAGE15_6_CONTROLLER_VERIFY=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
