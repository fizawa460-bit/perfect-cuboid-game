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
N356_WORKFLOW = ".github/workflows/stage32-01-178-n356-optimistic-exceptional-transport.yml"

# Repository-wide automatic surface. Entries may be absent on a sibling PR branch;
# if they are present, they are intentionally automatic.
ACTIVE_AUTO = {
    ".github/workflows/pages.yml",
    ".github/workflows/research-arsenal.yml",
    ".github/workflows/structure-radar.yml",
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
    ".github/workflows/stage32-01-178-n350-production-leaf-contract.yml",
    ".github/workflows/stage32-root-cleanup-phase-b.yml",
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


def classify_tree() -> tuple[dict[str, list[str]], dict[str, dict[str, int]]]:
    groups: dict[str, list[str]] = {k: [] for k in ("ACTIVE_AUTO", "MANUAL", "RETIRED")}
    fam: dict[str, Counter] = defaultdict(Counter)
    for p in workflow_paths():
        r = rel(p)
        cls = classify(r)
        groups[cls].append(r)
        fam[family(r)][cls] += 1
        fam[family(r)]["TOTAL"] += 1
    return groups, {k: dict(v) for k, v in sorted(fam.items())}


def build_inventory(changed: list[str]) -> dict:
    groups, fam = classify_tree()
    counts = {k: len(v) for k, v in groups.items()}
    counts["TOTAL"] = sum(counts.values())
    return {
        "schema_version": 3,
        "generated_on": "2026-09-12",
        "scope": "repository-wide workflow lifecycle policy",
        "classification_contract": "ACTIVE_AUTO and MANUAL are explicit allowlists; every reachable Stage workflow absent from both is RETIRED; unknown non-Stage workflows fail closed to MANUAL; exact-head verifier enumerates all reachable workflows and validates events/counts/families",
        "counts": counts,
        "families": fam,
        "active_auto": groups["ACTIVE_AUTO"],
        "manual": groups["MANUAL"],
        "retired_count": len(groups["RETIRED"]),
        "automatic_triggers_removed_by_migration": changed,
        "branch_local_live_catalog": sorted(p for p in ACTIVE_AUTO if (ROOT / p).is_file()),
        "notes": [
            "RETIRED and MANUAL workflows are normalized to workflow_dispatch only.",
            "ACTIVE_AUTO includes current research leaves and repository safety/authority gates.",
            "ACTIVE_AUTO entries absent from the current sibling branch do not affect that branch inventory.",
            "Stage33 MAIN and Stage35 MAIN have no open PR at migration time; Stage33 historical leaf workflows remain retired while the Stage35 aggregate audit remains live where present.",
            "Stage32EX5 BC2-24 is the only live BC2 leaf; BC2-12 through BC2-23 are not live.",
            "Stage32 N356 optimistic exceptional transport is AUDITED-CONSUMED and RETIRED; historical replay is workflow_dispatch-only.",
            "Stage32 current retained research leaf is N361; its exact-head replay is enforced by the Stage32 claim-frontier safety gate rather than a leaf-specific automatic workflow.",
        ],
    }


def verify_inventory(inv: dict) -> list[str]:
    failures: list[str] = []
    if inv.get("schema_version") != 3:
        failures.append("inventory schema_version must be 3")

    groups, fam = classify_tree()
    counts = {k: len(v) for k, v in groups.items()}
    counts["TOTAL"] = sum(counts.values())

    if inv.get("active_auto") != groups["ACTIVE_AUTO"]:
        failures.append("inventory is stale: ACTIVE_AUTO allowlist differs from exact workflow tree")
    if inv.get("manual") != groups["MANUAL"]:
        failures.append("inventory is stale: MANUAL allowlist differs from exact workflow tree")
    if inv.get("retired_count") != len(groups["RETIRED"]):
        failures.append("inventory is stale: RETIRED count differs from exact workflow tree")
    if inv.get("counts") != counts:
        failures.append("inventory is stale: lifecycle counts differ from exact workflow tree")
    if inv.get("families") != fam:
        failures.append("inventory is stale: family counts differ from exact workflow tree")

    expected_live = sorted(p for p in ACTIVE_AUTO if (ROOT / p).is_file())
    if inv.get("branch_local_live_catalog") != expected_live:
        failures.append("inventory is stale: branch_local_live_catalog differs from exact workflow tree")

    if N356_WORKFLOW in groups["ACTIVE_AUTO"]:
        failures.append("consumed N356 leaf is still ACTIVE_AUTO")
    if N356_WORKFLOW not in groups["RETIRED"]:
        failures.append("consumed N356 leaf is not RETIRED")
    removed = inv.get("automatic_triggers_removed_by_migration", [])
    if N356_WORKFLOW not in removed:
        failures.append("inventory does not record N356 automatic-trigger retirement")
    notes = inv.get("notes", [])
    if not any("N356" in str(note) and "AUDITED-CONSUMED" in str(note) for note in notes):
        failures.append("repository inventory lacks audited-consumed N356 rationale")
    if not any("N361" in str(note) and "claim-frontier" in str(note) for note in notes):
        failures.append("repository inventory lacks current N361 retained-leaf rationale")

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
    print("N356=AUDITED_CONSUMED_RETIRED current_retained_leaf=N361")
    print("historical_or_manual_automatic_triggers=0")
    print("mathematical_authority_changed=false")


if __name__ == "__main__":
    main()
