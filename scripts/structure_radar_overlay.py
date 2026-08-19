#!/usr/bin/env python3
"""Apply persistent StructureRadar search-state sidecar to a worktree registry.

The theorem registry is intentionally large and mostly static. Literature-search
metadata from batch 05 onward lives in a compact sidecar and is overlaid only in
the CI/worktree view used by refresh/verify. Mathematical card fields are never
modified by this helper.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs/structure-radar/structure-registry.json"
OVERLAY = ROOT / "docs/structure-radar/search-state-overrides.json"
ALLOWED = {"search_status", "arsenal_decision", "search_ledger"}


def apply() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    overlay = json.loads(OVERLAY.read_text(encoding="utf-8"))
    if overlay.get("overlay") != "STRUCTURE-RADAR-SEARCH-STATE-OVERLAY-R01":
        raise SystemExit("search-state overlay id mismatch")
    cards = {card["structure_id"]: card for card in registry.get("structures", [])}
    for structure_id, patch in overlay.get("structure_overrides", {}).items():
        if structure_id not in cards:
            raise SystemExit(f"unknown overlay structure: {structure_id}")
        extra = set(patch) - ALLOWED
        if extra:
            raise SystemExit(f"forbidden overlay fields for {structure_id}: {sorted(extra)}")
        cards[structure_id].update(patch)
    REGISTRY.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["apply"])
    args = parser.parse_args()
    if args.command == "apply":
        apply()


if __name__ == "__main__":
    main()
