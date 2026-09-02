#!/usr/bin/env python3
"""Validate the Arsenal registry and render its catalog and single-ID cards."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys


HERE = Path(__file__).resolve().parent
INDEX = HERE / "index.json"
CATALOG = HERE / "catalog.md"
CARDS = HERE / "cards"


def rel_exists(value: str) -> bool:
    return (HERE / value).resolve().exists()


def collect(data: dict) -> tuple[list[dict], list[str]]:
    entries: list[dict] = []
    errors: list[str] = []

    for item in data.get("selectors", []):
        entries.append({**item, "maturity": "FORMAL", "kind": "selector"})
    for item in data.get("formal_router_weapons", []):
        entries.append({**item, "maturity": "FORMAL", "kind": "weapon"})
    for item in data.get("formal_workflows", []):
        entries.append({**item, "maturity": "WORKFLOW", "kind": "workflow", "role": item.get("name", "")})

    retired: dict[str, str] = {}
    for harvest in data.get("provisional_harvests", []):
        for card_id in harvest.get("active_cards", []):
            entries.append({
                "id": card_id,
                "role": harvest.get("card_roles", {}).get(card_id, ""),
                "path": harvest["path"],
                "maturity": "PROVISIONAL",
                "kind": "weapon",
                "source_stage": harvest["source_stage"],
            })
        retired.update(harvest.get("retired_merged_ids", {}))

    ids = [entry["id"] for entry in entries]
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        errors.append(f"duplicate active IDs: {', '.join(duplicates)}")

    active_ids = set(ids)
    for old, successor in sorted(retired.items()):
        if successor not in active_ids:
            errors.append(f"retired ID {old} has missing successor {successor}")

    for entry in entries:
        if not rel_exists(entry["path"]):
            errors.append(f"missing path for {entry['id']}: {entry['path']}")
    for path in data.get("stable_weapon_libraries", []):
        if not rel_exists(path):
            errors.append(f"missing stable library: {path}")
    for path in data.get("superseded_indexes", []):
        if not rel_exists(path):
            errors.append(f"missing historical index: {path}")
    for record in data.get("support_records", []):
        if record.get("class") not in {"FORMAL", "PROVISIONAL", "WORKFLOW", "HISTORICAL", "RETIRED"}:
            errors.append(f"invalid support-record class: {record.get('class')}")
        if not rel_exists(record["path"]):
            errors.append(f"missing support record: {record['path']}")

    contract = data.get("registry_contract", {})
    if not contract.get("canonical_machine_registry"):
        errors.append("registry_contract.canonical_machine_registry must be true")
    if contract.get("human_catalog") != CATALOG.name:
        errors.append("registry_contract.human_catalog must name catalog.md")
    if contract.get("generated_card_root") != CARDS.name:
        errors.append("registry_contract.generated_card_root must name cards")

    return entries, errors


def link(path: str) -> str:
    return f"[{path}]({path})"


def source_stage(entry: dict) -> str:
    if entry.get("source_stage"):
        return entry["source_stage"]
    prefix = entry["id"].split("-", 1)[0]
    if prefix.startswith("S") and prefix[1:].isdigit():
        return f"Stage{prefix[1:]}"
    return "—"


def card_class(entry: dict) -> str:
    if entry["maturity"] == "WORKFLOW":
        return "workflows"
    if entry["maturity"] == "PROVISIONAL":
        return "provisional"
    return "formal"


def card_path(entry: dict) -> Path:
    return CARDS / card_class(entry) / f"{entry['id']}.md"


def card_link(entry: dict) -> str:
    return card_path(entry).relative_to(HERE).as_posix()


def relative_source_link(entry: dict) -> str:
    source = (HERE / entry["path"]).resolve()
    return Path(os.path.relpath(source, card_path(entry).parent)).as_posix()


def rewrite_excerpt_links(text: str, entry: dict) -> str:
    source_dir = (HERE / entry["path"]).resolve().parent
    target_dir = card_path(entry).parent

    def replace(match: re.Match[str]) -> str:
        label, target = match.groups()
        if "://" in target or target.startswith("#"):
            return match.group(0)
        raw_path, separator, anchor = target.partition("#")
        rewritten = Path(os.path.relpath((source_dir / raw_path).resolve(), target_dir)).as_posix()
        if separator:
            rewritten += f"#{anchor}"
        return f"[{label}]({rewritten})"

    return re.sub(r"\[([^]]+)\]\(([^)]+)\)", replace, text)


def source_excerpt(entry: dict) -> str | None:
    source = (HERE / entry["path"]).resolve()
    lines = source.read_text().splitlines()
    pattern = re.compile(rf"^(#{{2,4}})\s+{re.escape(entry['id'])}(?:\s|$)")
    start = None
    level = 0
    for index, line in enumerate(lines):
        match = pattern.match(line)
        if match:
            start = index
            level = len(match.group(1))
            break
    if start is None:
        return None

    end = len(lines)
    heading = re.compile(r"^(#+)\s+")
    for index in range(start + 1, len(lines)):
        match = heading.match(lines[index])
        if match and len(match.group(1)) <= level:
            end = index
            break
    excerpt = "\n".join(lines[start + 1:end]).strip()
    return rewrite_excerpt_links(excerpt, entry) if excerpt else None


def render_card(entry: dict) -> str:
    source = relative_source_link(entry)
    summary = entry.get("statement") or entry.get("summary") or entry.get("role", "")
    authority = {
        "FORMAL": "Audited reusable contract. Exact hypotheses, scope, and promotion firewalls still apply.",
        "WORKFLOW": "Reusable proof/audit procedure, not a mathematical or population selector.",
        "PROVISIONAL": "Frozen discovery snapshot only. The live Stage controller and current source locks override this card.",
    }[entry["maturity"]]
    lines = [
        f"# {entry['id']}",
        "",
        "<!-- Generated by ../../sync_arsenal_catalog.py; do not edit directly. -->",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| ID | `{entry['id']}` |",
        f"| Maturity | **{entry['maturity']}** |",
        f"| Kind | `{entry['kind']}` |",
        f"| Role | `{entry.get('role', '')}` |",
        f"| Source Stage | {source_stage(entry)} |",
        f"| Authoritative source | [`{entry['path']}`]({source}) |",
        "",
        "## Routing contract",
        "",
        authority,
        "",
        summary,
        "",
        "Use only after matching the source contract's object/population, field, cutoff, canonicalization, multiplicity, measure, quantifiers, and adapter hypotheses. This card grants no credit above the exact source conclusion.",
        "",
    ]
    excerpt = source_excerpt(entry)
    if excerpt:
        lines += [
            "## Exact source section snapshot",
            "",
            "The following section is copied deterministically from the authoritative source by the generator. If the source changes, `--check` fails until this card is regenerated.",
            "",
            excerpt,
            "",
        ]
    else:
        lines += [
            "## Source read required",
            "",
            "The source has no standalone heading matching this registry ID. Open the authoritative source above for the exact proof statement and exclusions.",
            "",
        ]
    return "\n".join(lines)


def retired_entries(data: dict) -> list[dict]:
    entries = []
    for harvest in data.get("provisional_harvests", []):
        for old, successor in sorted(harvest.get("retired_merged_ids", {}).items()):
            entries.append({"id": old, "successor": successor, "source_stage": harvest["source_stage"], "path": harvest["path"]})
    return entries


def retired_card_path(entry: dict) -> Path:
    return CARDS / "retired" / f"{entry['id']}.md"


def render_retired_card(entry: dict) -> str:
    successor = CARDS / "provisional" / f"{entry['successor']}.md"
    successor_link = Path(os.path.relpath(successor, retired_card_path(entry).parent)).as_posix()
    source = Path(os.path.relpath((HERE / entry["path"]).resolve(), retired_card_path(entry).parent)).as_posix()
    return "\n".join([
        f"# {entry['id']}", "",
        "<!-- Generated by ../../sync_arsenal_catalog.py; do not edit directly. -->", "",
        "| Field | Value |", "|---|---|",
        f"| ID | `{entry['id']}` |", "| Maturity | **RETIRED** |",
        f"| Source Stage | {entry['source_stage']} |",
        f"| Successor | [`{entry['successor']}`]({successor_link}) |",
        f"| Provenance | [`{entry['path']}`]({source}) |", "",
        "This identifier is retained for routing only. Do not reuse or treat it as an independent card.", "",
    ])


def render(data: dict, entries: list[dict]) -> str:
    lines = [
        "# Arsenal catalog",
        "",
        "<!-- Generated by sync_arsenal_catalog.py; edit index.json, not this file. -->",
        "",
        "This is the compact human view of [`index.json`](index.json), the sole machine-readable registry. Select an ID to open its small generated card; exact authority remains in the linked stable source.",
        "",
        "## Authority and maturity",
        "",
        "Active Stage controllers and current source locks override every snapshot here. **PROVISIONAL** entries are discovery aids only; **WORKFLOW** entries are procedures, not selectors. Formal status never removes a card's hypotheses or promotion firewalls.",
        "",
    ]

    sections = [
        ("Formal selectors", lambda e: e["kind"] == "selector"),
        ("Formal reusable weapons", lambda e: e["kind"] == "weapon" and e["maturity"] == "FORMAL"),
        ("Formal workflows", lambda e: e["kind"] == "workflow"),
        ("Provisional active-stage snapshots", lambda e: e["maturity"] == "PROVISIONAL"),
    ]
    for title, predicate in sections:
        lines += [f"## {title}", "", "| ID card | Role | Stage | Source |", "|---|---|---|---|"]
        for entry in filter(predicate, entries):
            stage = source_stage(entry)
            role = entry.get("role", "")
            lines.append(f"| [`{entry['id']}`]({card_link(entry)}) | `{role}` | {stage} | {link(entry['path'])} |")
        lines.append("")

    lines += ["## Retired IDs", "", "| Retired ID | Use instead |", "|---|---|"]
    for entry in retired_entries(data):
        old_path = retired_card_path(entry).relative_to(HERE).as_posix()
        successor_path = (CARDS / "provisional" / f"{entry['successor']}.md").relative_to(HERE).as_posix()
        lines.append(f"| [`{entry['id']}`]({old_path}) | [`{entry['successor']}`]({successor_path}) |")

    lines += ["", "## Stable source libraries", ""]
    for path in data.get("stable_weapon_libraries", []):
        lines.append(f"- {link(path)}")

    lines += ["", "## Registry support and provenance", "", "| Class | Record | Purpose |", "|---|---|---|"]
    for record in data.get("support_records", []):
        lines.append(f"| **{record['class']}** | {link(record['path'])} | {record['role']} |")

    lines += [
        "",
        "## Historical and deep lookup",
        "",
        "Use [`deep-source-index.md`](deep-source-index.md) for Stage14, Toolbox, StructureRadar, external-search, failure-history, and other deep provenance. Superseded compiled indexes are historical records only:",
        "",
    ]
    for path in data.get("superseded_indexes", []):
        lines.append(f"- {link(path)}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if catalog.md is stale")
    args = parser.parse_args()

    data = json.loads(INDEX.read_text())
    entries, errors = collect(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    expected = render(data, entries)
    expected_cards = {card_path(entry): render_card(entry) for entry in entries}
    expected_cards.update({retired_card_path(entry): render_retired_card(entry) for entry in retired_entries(data)})
    if args.check:
        if not CATALOG.exists() or CATALOG.read_text() != expected:
            print("ERROR: catalog.md is stale; run sync_arsenal_catalog.py", file=sys.stderr)
            return 1
        stale = [path for path, content in expected_cards.items() if not path.exists() or path.read_text() != content]
        expected_paths = set(expected_cards)
        unexpected = sorted(path for directory in ("formal", "workflows", "provisional", "retired") for path in (CARDS / directory).glob("*.md") if path not in expected_paths)
        if stale or unexpected:
            for path in stale:
                print(f"ERROR: stale or missing card: {path.relative_to(HERE)}", file=sys.stderr)
            for path in unexpected:
                print(f"ERROR: unregistered card: {path.relative_to(HERE)}", file=sys.stderr)
            return 1
        print(f"PASS: {len(entries)} active and {len(retired_entries(data))} retired IDs; paths, successors, catalog, and cards verified")
        return 0

    CATALOG.write_text(expected)
    for path, content in expected_cards.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    print(f"wrote catalog and {len(expected_cards)} ID cards ({len(entries)} active IDs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
