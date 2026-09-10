#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WF_DIR = ROOT / ".github" / "workflows"
INVENTORY = Path(__file__).with_name("repo-workflow-trigger-inventory-20260911.json")

ACTIVE_AUTO = {
    ".github/workflows/pages.yml",
    ".github/workflows/research-arsenal.yml",
    ".github/workflows/structure-radar.yml",
    ".github/workflows/stage32-n356-deterministic-terminal-check.yml",
    ".github/workflows/stage32-main-startup-authority.yml",
    ".github/workflows/stage32-claim-frontier-integrity.yml",
    ".github/workflows/stage32-stale-run-sweeper.yml",
    ".github/workflows/stage32-ex5-main.yml",
    ".github/workflows/stage32ex5-bc2-24-explicit-fibre-degree-partition.yml",
    ".github/workflows/stage35-35-01-to-09-audit.yml",
    ".github/workflows/stage35-ex-goal4cf-selected-discriminant-height.yml",
    ".github/workflows/stage36-bootstrap-audit.yml",
}
MANUAL = {
    ".github/workflows/stage32-n350-symbolic-mirror-generator.yml",
    ".github/workflows/stage32-q604-opposite-pair-residue-pack.yml",
}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def workflow_paths() -> list[Path]:
    return sorted([*WF_DIR.glob("*.yml"), *WF_DIR.glob("*.yaml")])


def family(path: str) -> str:
    name = Path(path).name
    if name.startswith(("stage32-ex", "stage32ex")):
        return "Stage32EX"
    if name.startswith("stage35-ex"):
        return "Stage35EX"
    m = re.match(r"stage(\d+)", name)
    if m:
        return f"Stage{m.group(1)}"
    return "REPO"


def classify(path: str) -> str:
    if path in ACTIVE_AUTO:
        return "ACTIVE_AUTO"
    if path in MANUAL:
        return "MANUAL"
    # Every known Stage workflow not explicitly live is historical/superseded.
    if re.match(r"\.github/workflows/stage\d", path):
        return "RETIRED"
    # Unknown repo-level workflows fail closed until explicitly reviewed.
    return "MANUAL"


def top_level_on(lines: list[str]) -> tuple[int, int] | None:
    for i, line in enumerate(lines):
        if line.startswith("on:"):
            end = i + 1
            if line.strip() != "on:":
                return i, end
            while end < len(lines):
                s = lines[end]
                if s and not s[0].isspace() and not s.lstrip().startswith("#"):
                    break
                end += 1
            return i, end
    return None


def events(text: str) -> set[str]:
    lines = text.splitlines()
    span = top_level_on(lines)
    if span is None:
        return set()
    start, end = span
    first = lines[start].strip()
    if first != "on:":
        rhs = first.split(":", 1)[1].strip()
        if rhs.startswith("[") and rhs.endswith("]"):
            return {x.strip().strip("'\"") for x in rhs[1:-1].split(",") if x.strip()}
        return {rhs.strip("'\"")} if rhs else set()
    out = set()
    for line in lines[start + 1:end]:
        m = re.match(r"^  ([A-Za-z0-9_-]+):", line)
        if m:
            out.add(m.group(1))
    return out


def manualize(text: str) -> str:
    lines = text.splitlines()
    span = top_level_on(lines)
    if span is None:
        raise AssertionError("missing top-level on: block")
    start, end = span
    replacement = ["on:", "  workflow_dispatch:"]
    return "\n".join(lines[:start] + replacement + lines[end:]) + ("\n" if text.endswith("\n") else "")


def build_inventory(changed: list[str]) -> dict:
    groups: dict[str, list[str]] = {k: [] for k in ("ACTIVE_AUTO", "MANUAL", "RETIRED")}
    fam: dict[str, Counter] = defaultdict(Counter)
    for p in workflow_paths():
        r = rel(p)
        cls = classify(r)
        groups[cls].append(r)
        fam[family(r)][cls] += 1
        fam[family(r)]["TOTAL"] += 1
    counts = {k: len(v) for k, v in groups.items()}
    counts["TOTAL"] = sum(counts.values())
    return {
        "schema_version": 1,
        "generated_on": "2026-09-11",
        "scope": "repository-wide workflow lifecycle policy",
        "classification_contract": "explicit live allowlist; known Stage workflows not live are RETIRED; unknown repo workflows fail closed to MANUAL",
        "counts": counts,
        "families": {k: dict(v) for k, v in sorted(fam.items())},
        "classifications": groups,
        "automatic_triggers_removed_by_migration": changed,
        "branch_local_live_catalog": sorted(ACTIVE_AUTO),
        "notes": [
            "RETIRED and MANUAL workflows are normalized to workflow_dispatch only.",
            "ACTIVE_AUTO includes current research leaves and repository safety/authority gates.",
            "Stage33 MAIN and Stage35 MAIN have no open PR at migration time; Stage33 leaf workflows therefore remain retired while the Stage35 aggregate audit remains live.",
            "Stage32EX5 BC2-24 is the only live BC2 leaf; BC2-12 through BC2-23 are not live.",
        ],
    }


def verify_inventory(inv: dict) -> list[str]:
    failures: list[str] = []
    actual = build_inventory([])["classifications"]
    expected = inv.get("classifications", {})
    if actual != expected:
        failures.append("inventory is stale: classification/path set differs from .github/workflows")
    for p in workflow_paths():
        r = rel(p)
        cls = classify(r)
        ev = events(p.read_text())
        if cls in {"MANUAL", "RETIRED"} and ev != {"workflow_dispatch"}:
            failures.append(f"{cls} must be workflow_dispatch-only: {r} events={sorted(ev)}")
        if cls == "ACTIVE_AUTO" and not (ev - {"workflow_dispatch", "workflow_call"}):
            failures.append(f"ACTIVE_AUTO has no automatic event: {r} events={sorted(ev)}")
    return failures


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--write-inventory", action="store_true")
    args = ap.parse_args()

    changed: list[str] = []
    if args.fix:
        for p in workflow_paths():
            r = rel(p)
            if classify(r) not in {"MANUAL", "RETIRED"}:
                continue
            text = p.read_text()
            if events(text) != {"workflow_dispatch"}:
                p.write_text(manualize(text))
                changed.append(r)

    generated = build_inventory(changed)
    if args.write_inventory:
        INVENTORY.write_text(json.dumps(generated, indent=2, sort_keys=False) + "\n")
    if not INVENTORY.is_file():
        raise SystemExit(f"missing inventory: {INVENTORY}")
    inv = json.loads(INVENTORY.read_text())
    failures = verify_inventory(inv)
    if failures:
        raise SystemExit("\n".join(failures))

    c = inv["counts"]
    print("PASS repository-wide workflow trigger lifecycle inventory")
    print(f"ACTIVE_AUTO={c['ACTIVE_AUTO']} MANUAL={c['MANUAL']} RETIRED={c['RETIRED']} TOTAL={c['TOTAL']}")
    for name, row in inv["families"].items():
        print(f"FAMILY {name} TOTAL={row.get('TOTAL',0)} ACTIVE_AUTO={row.get('ACTIVE_AUTO',0)} MANUAL={row.get('MANUAL',0)} RETIRED={row.get('RETIRED',0)}")
    print("historical_or_manual_automatic_triggers=0")
    print("mathematical_authority_changed=false")


if __name__ == "__main__":
    main()
