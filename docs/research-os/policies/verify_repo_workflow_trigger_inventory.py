#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WF_DIR = ROOT / ".github" / "workflows"
BASE_INVENTORY = Path(__file__).with_name("repo-workflow-trigger-inventory-20260911.json")
CURRENT_DELTA = Path(__file__).with_name("repo-workflow-trigger-inventory-current-delta-20260914.json")

ACTIVE_AUTO = {
    ".github/workflows/pages.yml",
    ".github/workflows/research-arsenal.yml",
    ".github/workflows/structure-radar.yml",
    ".github/workflows/stage32-main-startup-authority.yml",
    ".github/workflows/stage32-claim-frontier-integrity.yml",
    ".github/workflows/stage32-stale-run-sweeper.yml",
    ".github/workflows/stage32-ex5-main.yml",
    ".github/workflows/stage32-ex5-hpadj08-kernel.yml",
    ".github/workflows/stage32-ex5-hpadj08-full178.yml",
    ".github/workflows/stage32ex5-bc2-24-explicit-fibre-degree-partition.yml",
    ".github/workflows/stage35-35-01-to-09-audit.yml",
    ".github/workflows/stage35-ex-goal4cf-selected-discriminant-height.yml",
    ".github/workflows/stage36-bootstrap-audit.yml",
}
MANUAL = {
    ".github/workflows/stage32-01-178-n350-production-leaf-contract.yml",
    ".github/workflows/stage32-root-cleanup-phase-b.yml",
    ".github/workflows/stage32-n350-symbolic-mirror-generator.yml",
    ".github/workflows/stage32-q604-opposite-pair-residue-pack.yml",
}
CLASSES = ("ACTIVE_AUTO", "MANUAL", "RETIRED")


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
    if re.match(r"\.github/workflows/stage\d", path):
        return "RETIRED"
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


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def resolved_expected_classifications(base: dict, delta: dict) -> dict[str, list[str]]:
    if delta.get("schema") != "REPO_WORKFLOW_TRIGGER_INVENTORY_CURRENT_DELTA_V1":
        raise AssertionError("current inventory delta schema drift")
    if canonical(delta) != delta.get("canonical_sha256_without_this_field"):
        raise AssertionError("current inventory delta canonical drift")
    if delta.get("base_inventory_path") != BASE_INVENTORY.relative_to(ROOT).as_posix():
        raise AssertionError("current inventory delta base path drift")
    if git_blob_sha(BASE_INVENTORY.read_bytes()) != delta.get("base_inventory_git_blob_sha"):
        raise AssertionError("current inventory baseline blob drift")
    groups = {k: list(base.get("classifications", {}).get(k, [])) for k in CLASSES}
    additions = delta.get("additions", {})
    removals = delta.get("removals", {})
    if set(additions) - set(CLASSES) or set(removals) - set(CLASSES):
        raise AssertionError("current inventory delta class drift")
    for cls in CLASSES:
        for path in removals.get(cls, []):
            if path not in groups[cls]:
                raise AssertionError(f"inventory removal missing from baseline: {cls} {path}")
            groups[cls].remove(path)
        for path in additions.get(cls, []):
            if any(path in groups[c] for c in CLASSES):
                raise AssertionError(f"inventory addition already classified: {path}")
            groups[cls].append(path)
        groups[cls].sort()
    all_paths = [p for cls in CLASSES for p in groups[cls]]
    if len(all_paths) != len(set(all_paths)):
        raise AssertionError("resolved inventory has duplicate paths")
    return groups


def actual_groups() -> dict[str, list[str]]:
    groups = {k: [] for k in CLASSES}
    for p in workflow_paths():
        groups[classify(rel(p))].append(rel(p))
    for cls in CLASSES:
        groups[cls].sort()
    return groups


def counts(groups: dict[str, list[str]]) -> dict[str, int]:
    out = {k: len(groups[k]) for k in CLASSES}
    out["TOTAL"] = sum(out.values())
    return out


def families(groups: dict[str, list[str]]) -> dict[str, dict[str, int]]:
    fam: dict[str, Counter] = defaultdict(Counter)
    for cls in CLASSES:
        for path in groups[cls]:
            fam[family(path)][cls] += 1
            fam[family(path)]["TOTAL"] += 1
    return {k: dict(v) for k, v in sorted(fam.items())}


def verify(base: dict, delta: dict) -> tuple[list[str], dict[str, list[str]]]:
    failures: list[str] = []
    try:
        expected = resolved_expected_classifications(base, delta)
    except AssertionError as exc:
        return [str(exc)], actual_groups()
    actual = actual_groups()
    if actual != expected:
        failures.append("inventory is stale: resolved baseline+delta classification/path set differs from .github/workflows")
    if counts(expected) != delta.get("expected_counts"):
        failures.append("current inventory delta expected_counts drift")
    if families(expected) != delta.get("expected_families"):
        failures.append("current inventory delta expected_families drift")
    live = sorted(p for p in ACTIVE_AUTO if (ROOT / p).is_file())
    if live != delta.get("expected_branch_local_live_catalog"):
        failures.append("current inventory delta branch_local_live_catalog drift")
    for p in workflow_paths():
        r = rel(p)
        cls = classify(r)
        ev = events(p.read_text())
        if cls in {"MANUAL", "RETIRED"} and ev != {"workflow_dispatch"}:
            failures.append(f"{cls} must be workflow_dispatch-only: {r} events={sorted(ev)}")
        if cls == "ACTIVE_AUTO" and not (ev - {"workflow_dispatch", "workflow_call"}):
            failures.append(f"ACTIVE_AUTO has no automatic event: {r} events={sorted(ev)}")
    return failures, actual


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--write-inventory", action="store_true")
    args = ap.parse_args()
    if args.fix:
        for p in workflow_paths():
            r = rel(p)
            if classify(r) not in {"MANUAL", "RETIRED"}:
                continue
            text = p.read_text()
            if events(text) != {"workflow_dispatch"}:
                p.write_text(manualize(text))
    if args.write_inventory:
        raise SystemExit("the 2026-09-11 full inventory is immutable; update repo-workflow-trigger-inventory-current-delta-20260914.json instead")
    if not BASE_INVENTORY.is_file() or not CURRENT_DELTA.is_file():
        raise SystemExit("missing workflow inventory authority")
    base = json.loads(BASE_INVENTORY.read_text())
    delta = json.loads(CURRENT_DELTA.read_text())
    failures, groups = verify(base, delta)
    if failures:
        raise SystemExit("\n".join(failures))
    c = counts(groups)
    print("PASS repository-wide workflow trigger lifecycle inventory")
    print(f"ACTIVE_AUTO={c['ACTIVE_AUTO']} MANUAL={c['MANUAL']} RETIRED={c['RETIRED']} TOTAL={c['TOTAL']}")
    for name, row in families(groups).items():
        print(f"FAMILY {name} TOTAL={row.get('TOTAL',0)} ACTIVE_AUTO={row.get('ACTIVE_AUTO',0)} MANUAL={row.get('MANUAL',0)} RETIRED={row.get('RETIRED',0)}")
    print(f"baseline_blob={delta['base_inventory_git_blob_sha']}")
    print(f"current_delta_canonical={delta['canonical_sha256_without_this_field']}")
    print("historical_or_manual_automatic_triggers=0")
    print("mathematical_authority_changed=false")


if __name__ == "__main__":
    main()
