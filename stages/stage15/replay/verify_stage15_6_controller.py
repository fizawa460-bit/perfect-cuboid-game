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
VERIFIER_RE = re.compile(r"verify_stage15_6([a-z]{2})(?:_([a-z]{2}))?\.py$")
RESULT_REF_RE = re.compile(r"15-6([a-z]{2})/result\.md")
EXIT_RE = re.compile(r"^STAGE15_6[A-Z0-9_]*EXIT=(.+)$", re.MULTILINE)
NEXT_GATE_RE = re.compile(r"^NEXT_GATE=(.+)$", re.MULTILINE)


def ordinal(code: str) -> int:
    return (ord(code[0]) - 97) * 26 + ord(code[1]) - 97


def discover() -> list[tuple[str, Path]]:
    rows: list[tuple[str, Path]] = []
    for directory in STAGE15.glob("15-6??"):
        match = SUBSTAGE_RE.fullmatch(directory.name)
        if not match or not (directory / "result.md").is_file():
            continue
        code = match.group(1)
        rows.append((code, directory / "result.md"))
    return sorted(rows, key=lambda row: ordinal(row[0]))


def verifier_coverage(codes: set[str]) -> dict[str, Path]:
    coverage: dict[str, Path] = {}
    for verifier in sorted((STAGE15 / "replay").glob("verify_stage15_6*.py")):
        match = VERIFIER_RE.fullmatch(verifier.name)
        if not match:
            continue
        start, end = match.group(1), match.group(2) or match.group(1)
        if ordinal(end) < ordinal(start):
            raise AssertionError(f"reversed verifier range: {verifier.name}")
        for value in range(ordinal(start), ordinal(end) + 1):
            code = chr(value // 26 + 97) + chr(value % 26 + 97)
            if code in codes:
                coverage.setdefault(code, verifier)
        # Batch filenames are historical labels and may lag a repaired batch
        # by one substage.  Explicit result reads are authoritative coverage.
        source = verifier.read_text(encoding="utf-8")
        for code in RESULT_REF_RE.findall(source):
            if code in codes:
                coverage.setdefault(code, verifier)
    return coverage


def current_marker(code: str, text: str) -> tuple[str, str]:
    exact_exit = re.search(
        rf"^STAGE15_6{code.upper()}_EXIT=(.+)$", text, re.MULTILINE
    )
    if exact_exit:
        return exact_exit.group(1), "FROZEN_EXIT"
    gates = NEXT_GATE_RE.findall(text)
    if gates:
        return gates[-1], "CONTROLLER_NEXT_GATE"
    exits = EXIT_RE.findall(text)
    if exits:
        return exits[-1], "LEGACY_EXIT"
    return "MISSING", "MISSING"


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

    ordinals = [ordinal(code) for code, _ in rows]
    expected = list(range(ordinals[0], ordinals[-1] + 1))
    if ordinals != expected:
        raise AssertionError("Stage15-6 substage sequence has a gap")

    failures: list[str] = []
    codes = {code for code, _ in rows}
    coverage = verifier_coverage(codes)
    for code in sorted(codes, key=ordinal):
        if code not in coverage:
            failures.append(f"6{code}:missing verifier coverage")

    verifier_failures: dict[Path, str] = {}
    for verifier in sorted(set(coverage.values())):
        run = subprocess.run(
            [sys.executable, str(verifier)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
        if run.returncode:
            tail = run.stderr.strip().splitlines()[-1] if run.stderr.strip() else "unknown failure"
            verifier_failures[verifier] = tail
    for code in sorted(codes, key=ordinal):
        verifier = coverage.get(code)
        if verifier in verifier_failures:
            failures.append(f"6{code}:{verifier.name}:{verifier_failures[verifier]}")

    latest_code, latest_result = rows[-1]
    latest_text = latest_result.read_text(encoding="utf-8")
    latest_exit, marker_source = current_marker(latest_code, latest_text)
    if latest_exit == "MISSING":
        failures.append(f"6{latest_code}:missing EXIT/controller marker")

    owner, codex_required, reason = decide(latest_exit, failures)
    print(f"CONTROLLER_SCHEMA_VERSION={config['schema_version']}")
    print(f"CANONICAL_MAIN_COMMAND={config['canonical_commands']['main']}")
    print(f"CANONICAL_AUDIT_COMMAND={config['canonical_commands']['audit']}")
    print(f"DISCOVERED_SUBSTAGE_COUNT={len(rows)}")
    print(f"CURRENT_SUBSTAGE=Stage15-6{latest_code}")
    print(f"CURRENT_EXIT={latest_exit}")
    print(f"CURRENT_MARKER_SOURCE={marker_source}")
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
