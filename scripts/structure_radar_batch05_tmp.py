#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs/structure-radar/structure-registry.json"
PROGRESS = ROOT / "docs/structure-radar/progress.json"
LEDGER = "docs/structure-radar/literature/SR-SEARCH-05.md"
TARGETS = [
    "SR-STR-031", "SR-STR-032", "SR-STR-033", "SR-STR-036",
    "SR-STR-037", "SR-STR-038", "SR-STR-039", "SR-STR-040",
]
BATCH_ID = "SR-BATCH-LITERATURE_SEARCH-05-R01"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def save(path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def find_structure_cards(obj):
    if isinstance(obj, list):
        if obj and all(isinstance(x, dict) for x in obj):
            ids = {x.get("structure_id") for x in obj}
            if all(t in ids for t in TARGETS):
                return obj
        for x in obj:
            found = find_structure_cards(x)
            if found is not None:
                return found
    elif isinstance(obj, dict):
        for x in obj.values():
            found = find_structure_cards(x)
            if found is not None:
                return found
    return None


def find_batch_list(obj):
    if isinstance(obj, list):
        if any(isinstance(x, dict) and x.get("batch_id") == "SR-BATCH-LITERATURE_SEARCH-04-R01" for x in obj):
            return obj
        for x in obj:
            found = find_batch_list(x)
            if found is not None:
                return found
    elif isinstance(obj, dict):
        for x in obj.values():
            found = find_batch_list(x)
            if found is not None:
                return found
    return None


def main():
    registry = load(REGISTRY)
    cards = find_structure_cards(registry)
    assert cards is not None, "structure card list not found"
    by_id = {c.get("structure_id"): c for c in cards}
    for sid in TARGETS:
        card = by_id[sid]
        assert card.get("search_status") == "NOT_SEARCHED", (sid, card.get("search_status"))
        assert card.get("arsenal_decision") == "PENDING", (sid, card.get("arsenal_decision"))
        assert card.get("card_status") in {"NORMALIZED", "AUDITED"}, (sid, card.get("card_status"))
        card["search_status"] = "SEARCHED"
        card["arsenal_decision"] = "ACTIVE"
        card["search_ledger"] = LEDGER
    save(REGISTRY, registry)

    progress = load(PROGRESS)
    batches = find_batch_list(progress)
    assert batches is not None, "progress batch list not found"
    assert not any(isinstance(x, dict) and x.get("batch_id") == BATCH_ID for x in batches)
    batches.append({
        "batch_id": BATCH_ID,
        "task_id": "SR-SEARCH-01",
        "status": "SUBMITTED_FOR_AUDIT",
        "source_ids": [],
        "sources_reviewed": 0,
        "structures_added": 0,
        "structures_updated": 8,
        "structure_carrier_sources": 0,
        "structures_deduped": 0,
        "searches_completed": 8,
        "arsenal_decisions": 8,
        "audit_required": True,
        "duplicate_source": 0,
        "no_distinct_structure": 0,
    })
    save(PROGRESS, progress)

    subprocess.run(["python", "scripts/structure_radar.py", "refresh"], cwd=ROOT, check=True)
    subprocess.run(["python", "scripts/structure_radar.py", "verify"], cwd=ROOT, check=True)

    queue = load(ROOT / "docs/structure-radar/exploration-queue.json")
    controller = load(ROOT / "docs/structure-radar/controller.json")
    assert len(queue["tasks"]) == 22, len(queue["tasks"])
    assert queue["tasks"][0]["status"] == "READY"
    assert queue["tasks"][0]["structure_ids"] == [
        "SR-STR-041", "SR-STR-042", "SR-STR-043", "SR-STR-044",
        "SR-STR-045", "SR-STR-046", "SR-STR-047", "SR-STR-048",
    ]
    assert controller["queue"]["task_count"] == 22
    assert controller["registry"]["unresolved_search_count"] == 169
    assert controller["registry"]["pending_arsenal_decision_count"] == 188
    print("BATCH_ID=" + BATCH_ID)
    print("SEARCHES_COMPLETED=8")
    print("UNRESOLVED_SEARCH=169")
    print("PENDING_ARSENAL=188")
    print("QUEUE_TASKS=22")
    print("AUDIT_REQUIRED=true")
    print("MERGE_ALLOWED=false")
    print("NEXT_EXPECTED_COMMAND=StructureRadar-audit")


if __name__ == "__main__":
    main()
