#!/usr/bin/env python3
"""Build and verify the repository-wide StructureRadar corpus and queue."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
RADAR = ROOT / "docs" / "structure-radar"
MANIFEST_PATH = RADAR / "source-manifest.json"
MANIFEST_PART_DIR = RADAR / "source-manifest"
QUEUE_PATH = RADAR / "exploration-queue.json"
CONTROLLER_PATH = RADAR / "controller.json"
PROGRESS_PATH = RADAR / "progress.json"
REGISTRY_PATH = RADAR / "structure-registry.json"

REVIEWED = {
    "STRUCTURES_RECORDED",
    "NO_DISTINCT_STRUCTURE",
    "DUPLICATE_SOURCE",
    "DEFERRED_WITH_REASON",
    "AUDITED",
}
DECISIONS = {"ACTIVE", "PARKED", "EXTERNAL_GATE", "REJECTED", "PENDING"}
SEARCH_STATES = {
    "NOT_SEARCHED",
    "SEARCH_IN_PROGRESS",
    "SEARCHED",
    "NEEDS_REFRESH",
    "DEFERRED_WITH_REASON",
}
CARD_STATES = {"DRAFT", "NORMALIZED", "SUBMITTED_FOR_AUDIT", "AUDITED"}
CHUNK_SIZE = 60
MANIFEST_PART_SIZE = 250


def die(message: str) -> None:
    raise SystemExit(message)


def load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        die(f"missing required file: {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(data: Any) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False) + "\n"


def tracked_paths() -> list[str]:
    command = ["git", "ls-files", "-z"]
    result = subprocess.run(command, cwd=ROOT, check=True, capture_output=True)
    return sorted(item for item in result.stdout.decode().split("\0") if item)


def stage_number(path: str) -> int | None:
    match = re.search(r"(?:^|/)(?:stage|Stage)(\d+)(?:s)?(?:/|[-_])", path)
    return int(match.group(1)) if match else None


def is_stage_arsenal(path: str) -> bool:
    return bool(re.fullmatch(r"docs/stage\d+(?:-[^/]*)?-arsenal(?:-promotion|-index)?\.md", path))


def source_kind(path: str) -> str | None:
    name = Path(path).name
    suffix = Path(path).suffix
    if path.startswith("docs/structure-radar/"):
        return None
    if path in {"docs/research-arsenal-index.json", "docs/research-arsenal-index.md"}:
        return "CENTRAL_ARSENAL"
    if is_stage_arsenal(path) or path in {
        "docs/stage14-arsenal.md",
        "docs/stage14-arsenal-index.md",
        "docs/stage14-arsenal-stage15-map.md",
    }:
        return "STAGE_ARSENAL"
    if path in {
        "docs/stage14-15-bound-attack-map.md",
        "docs/stage14-15-bound-deep-review-queue.json",
        "docs/stage14-15-bound-deep-review-queue.md",
    }:
        return "CURATED_ATTACK_LEDGER"
    if "/q-research/" in path and Path(path).suffix in {".md", ".json"}:
        return "LITERATURE_RADAR"
    if path == "docs/00_CURRENT_RESEARCH_STATUS.md":
        return "PROJECT_STATUS"
    if path in {"README.md", "stages/README.md"}:
        return "PROJECT_DOC"
    if not path.startswith("stages/") and not path.startswith("docs/"):
        return None
    if name == "self-contained-bundle.md":
        return "SELF_CONTAINED_BUNDLE"
    if name == "final.md":
        return "FINAL"
    if name == "result.md":
        return "RESULT"
    if name.startswith("audit") and name.endswith(".md"):
        return "AUDIT"
    if name == "roadmap.md" or (path.startswith("docs/stage") and "roadmap" in name):
        return "ROADMAP"
    parts = Path(path).parts
    if len(parts) == 3 and parts[0] == "stages" and name.endswith("-controller.json"):
        return "STAGE_CONTROLLER"
    if path.startswith("docs/") and suffix == ".md":
        return "PROJECT_DOC"
    if path.startswith("docs/") and suffix == ".json":
        return "MACHINE_INDEX"
    if path.startswith("stages/") and suffix == ".md":
        return "SUPPORTING_MATH_DOC"
    if path.startswith("stages/") and suffix == ".json":
        if "/data/" in path or "/evidence/" in path:
            return "COMPUTATIONAL_REPORT"
        return "MACHINE_CONTRACT"
    return None


def source_priority(path: str, kind: str, stage: int | None) -> int:
    if kind in {"CENTRAL_ARSENAL", "STAGE_ARSENAL"}:
        return 0
    if kind == "CURATED_ATTACK_LEDGER":
        return 1
    if stage is not None and stage >= 26 and "/archive/" not in path:
        return 1
    if kind == "LITERATURE_RADAR":
        return 2
    if stage is not None and 16 <= stage <= 25 and "/archive/" not in path:
        return 2
    if stage in {14, 15}:
        return 3
    if kind in {"COMPUTATIONAL_REPORT", "MACHINE_CONTRACT", "MACHINE_INDEX"}:
        return 5
    if "/archive/" in path:
        return 5
    return 4


def queue_group(path: str, kind: str, stage: int | None) -> str:
    if kind in {"CENTRAL_ARSENAL", "STAGE_ARSENAL"}:
        return "CURRENT_ARSENALS"
    if kind == "CURATED_ATTACK_LEDGER":
        return "STAGE14_15_CURATED"
    if stage is not None and stage >= 26 and "/archive/" not in path:
        return "RECENT_STAGE26_PLUS"
    if kind == "LITERATURE_RADAR":
        return "EXISTING_Q_LITERATURE"
    if stage is not None and 16 <= stage <= 25 and "/archive/" not in path:
        return "STAGE16_25_CURRENT"
    if stage in {14, 15}:
        return "STAGE14_15_DEEP_CORPUS"
    if stage is not None and stage <= 13:
        return "STAGE02_13_HISTORY"
    return "OTHER_ARCHIVE_AND_CONTEXT"


def stable_source_id(path: str) -> str:
    return "SRC-" + hashlib.sha1(path.encode("utf-8")).hexdigest()[:12].upper()


def file_fingerprint(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def corpus_fingerprint(sources: Iterable[dict[str, Any]]) -> str:
    rows = [f"{item['path']}\0{item['fingerprint']}" for item in sources]
    return hashlib.sha256("\n".join(rows).encode("utf-8")).hexdigest()


def promotion_backflow_gaps(paths: list[str]) -> list[str]:
    arsenal = load_json(ROOT / "docs" / "research-arsenal-index.json")
    indexed = {weapon["source"] for weapon in arsenal.get("weapons", []) if weapon.get("source")}
    candidates = []
    for path in paths:
        if re.fullmatch(r"docs/stage(?:2[0-9]|[3-9][0-9]+)-arsenal-promotion\.md", path):
            candidates.append(path)
        elif path in {"docs/stage20-arsenal.md", "docs/stage21-arsenal.md"}:
            candidates.append(path)
    return sorted(path for path in candidates if path not in indexed)


def build_manifest(progress: dict[str, Any]) -> dict[str, Any]:
    reviews = progress.get("source_reviews", {})
    paths = tracked_paths()
    sources = []
    for path in paths:
        kind = source_kind(path)
        if kind is None:
            continue
        absolute = ROOT / path
        if not absolute.is_file():
            continue
        stage = stage_number(path)
        fingerprint = file_fingerprint(absolute)
        source_id = stable_source_id(path)
        review = reviews.get(source_id)
        if review is None:
            state = "NEW"
        elif review.get("fingerprint") != fingerprint:
            state = "CHANGED"
        elif review.get("status") in REVIEWED:
            state = "CURRENT_REVIEWED"
        else:
            state = "UNRESOLVED"
        sources.append(
            {
                "source_id": source_id,
                "path": path,
                "fingerprint": fingerprint,
                "stage": f"Stage{stage}" if stage is not None else None,
                "kind": kind,
                "evidence_role": {
                    "CENTRAL_ARSENAL": "CURATED_INDEX",
                    "STAGE_ARSENAL": "CURATED_PROMOTION",
                    "CURATED_ATTACK_LEDGER": "CURATED_DISCOVERY_LEDGER",
                    "LITERATURE_RADAR": "PRIOR_LITERATURE_ANALYSIS",
                    "AUDIT": "AUDIT_EVIDENCE",
                    "FINAL": "CERTIFIED_SYNTHESIS",
                    "SELF_CONTAINED_BUNDLE": "CERTIFIED_SYNTHESIS",
                    "RESULT": "RESEARCH_RESULT",
                    "ROADMAP": "PLANNED_OR_OPEN_STRUCTURE",
                    "STAGE_CONTROLLER": "LIFECYCLE_CONTEXT",
                    "PROJECT_STATUS": "LIFECYCLE_CONTEXT",
                    "PROJECT_DOC": "SUPPORTING_CONTEXT",
                    "MACHINE_INDEX": "MACHINE_READABLE_CONTEXT",
                    "SUPPORTING_MATH_DOC": "SUPPORTING_MATHEMATICS",
                    "COMPUTATIONAL_REPORT": "COMPUTATIONAL_EVIDENCE",
                    "MACHINE_CONTRACT": "MACHINE_READABLE_CONTEXT",
                }[kind],
                "archive": "/archive/" in path,
                "priority": source_priority(path, kind, stage),
                "queue_group": queue_group(path, kind, stage),
                "review_state": state,
            }
        )
    sources.sort(key=lambda item: (item["priority"], item["queue_group"], item["path"]))
    stage_counts = Counter(item["stage"] or "NON_STAGE" for item in sources)
    kind_counts = Counter(item["kind"] for item in sources)
    state_counts = Counter(item["review_state"] for item in sources)
    stages = sorted(
        {int(item["stage"][5:]) for item in sources if item["stage"]},
    )
    return {
        "schema_version": 1,
        "manifest": "STRUCTURE-RADAR-SOURCE-MANIFEST-R01",
        "scope": {
            "all_merged_stages": True,
            "future_stage_auto_discovery": True,
            "stage14_15_are_bootstrap_not_boundary": True,
            "unmerged_pr_heads_are_canonical": False,
            "current_arsenal_always_included": True,
        },
        "latest_stage_discovered": f"Stage{max(stages)}" if stages else None,
        "corpus_fingerprint": corpus_fingerprint(sources),
        "source_count": len(sources),
        "counts_by_stage": dict(sorted(stage_counts.items())),
        "counts_by_kind": dict(sorted(kind_counts.items())),
        "counts_by_review_state": dict(sorted(state_counts.items())),
        "arsenal_backflow_gaps": promotion_backflow_gaps(paths),
        "sources": sources,
    }


GROUP_ORDER = [
    "CURRENT_ARSENALS",
    "RECENT_STAGE26_PLUS",
    "STAGE14_15_CURATED",
    "STAGE16_25_CURRENT",
    "EXISTING_Q_LITERATURE",
    "STAGE14_15_DEEP_CORPUS",
    "STAGE02_13_HISTORY",
    "OTHER_ARCHIVE_AND_CONTEXT",
]


def chunks(items: list[dict[str, Any]], size: int) -> Iterable[list[dict[str, Any]]]:
    for start in range(0, len(items), size):
        yield items[start : start + size]


def build_queue(manifest: dict[str, Any], registry: dict[str, Any]) -> dict[str, Any]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for source in manifest["sources"]:
        if source["review_state"] != "CURRENT_REVIEWED":
            grouped[source["queue_group"]].append(source)

    tasks = []
    for group in GROUP_ORDER:
        for index, batch in enumerate(chunks(grouped.get(group, []), CHUNK_SIZE), start=1):
            tasks.append(
                {
                    "task_id": f"SR-CENSUS-{group}-{index:02d}",
                    "phase": "SOURCE_CENSUS",
                    "group": group,
                    "status": "PENDING",
                    "source_ids": [item["source_id"] for item in batch],
                    "required_output": "normalized structure cards or an explicit per-source no-new-structure/duplicate decision",
                }
            )

    source_map = {item["source_id"]: item for item in manifest["sources"]}
    stale_cards = []
    for card in registry.get("structures", []):
        if any(
            provenance.get("source_id") not in source_map
            or provenance.get("fingerprint") != source_map[provenance["source_id"]]["fingerprint"]
            for provenance in card.get("repo_provenance", [])
        ):
            stale_cards.append(card)
    for index, batch in enumerate(chunks(stale_cards, 12), start=1):
        tasks.append(
            {
                "task_id": f"SR-REFRESH-{index:02d}",
                "phase": "CARD_REFRESH",
                "group": "CHANGED_OR_REMOVED_PROVENANCE",
                "status": "PENDING",
                "structure_ids": [item["structure_id"] for item in batch],
                "required_output": "revalidate the card against current source fingerprints before further search or promotion",
            }
        )

    searchable = [
        card
        for card in registry.get("structures", [])
        if card.get("card_status") in {"NORMALIZED", "AUDITED"}
        and card.get("search_status") in {"NOT_SEARCHED", "NEEDS_REFRESH"}
    ]
    for index, batch in enumerate(chunks(searchable, 8), start=1):
        tasks.append(
            {
                "task_id": f"SR-SEARCH-{index:02d}",
                "phase": "LITERATURE_SEARCH",
                "group": "NORMALIZED_STRUCTURE_SEARCH",
                "status": "PENDING",
                "structure_ids": [item["structure_id"] for item in batch],
                "required_output": "primary-source literature ledger and exact perfect-cuboid transfer decision",
            }
        )

    if tasks:
        tasks[0]["status"] = "READY"
    counts = Counter(task["status"] for task in tasks)
    return {
        "schema_version": 1,
        "queue": "STRUCTURE-RADAR-EXPLORATION-QUEUE-R01",
        "corpus_fingerprint": manifest["corpus_fingerprint"],
        "batch_source_limit": CHUNK_SIZE,
        "tasks": tasks,
        "counts_by_status": dict(sorted(counts.items())),
    }


def validate_registry(registry: dict[str, Any], manifest: dict[str, Any]) -> None:
    if registry.get("registry") != "STRUCTURE-RADAR-REGISTRY-R01":
        die("structure registry id mismatch")
    cards = registry.get("structures")
    if not isinstance(cards, list):
        die("structure registry cards must be a list")
    ids = [card.get("structure_id") for card in cards]
    if None in ids or len(ids) != len(set(ids)):
        die("missing or duplicate structure_id")
    source_map = {item["source_id"]: item for item in manifest["sources"]}
    for card in cards:
        required = {
            "structure_id",
            "canonical_math_name",
            "exact_equations_or_object",
            "search_terms_primary",
            "search_terms_aliases",
            "theorem_species",
            "repo_provenance",
            "target_populations",
            "potential_weapon_types",
            "applicability_gaps",
            "existing_radar_overlap",
            "search_status",
            "arsenal_decision",
            "card_status",
        }
        missing = sorted(required - set(card))
        if missing:
            die(f"structure card {card['structure_id']} missing: {', '.join(missing)}")
        if card["search_status"] not in SEARCH_STATES:
            die(f"invalid search status: {card['structure_id']}")
        if card["arsenal_decision"] not in DECISIONS:
            die(f"invalid arsenal decision: {card['structure_id']}")
        if card["card_status"] not in CARD_STATES:
            die(f"invalid card status: {card['structure_id']}")
        for provenance in card["repo_provenance"]:
            provenance_required = {"source_id", "path", "locator", "fingerprint"}
            if provenance_required - set(provenance):
                die(f"incomplete provenance: {card['structure_id']}")
            if provenance.get("source_id") not in source_map:
                die(f"unknown provenance source: {card['structure_id']}")
            if provenance["path"] != source_map[provenance["source_id"]]["path"]:
                die(f"provenance path mismatch: {card['structure_id']}")


def validate_progress(progress: dict[str, Any]) -> None:
    if progress.get("registry") != "STRUCTURE-RADAR-PROGRESS-R01":
        die("progress registry id mismatch")
    reviews = progress.get("source_reviews")
    if not isinstance(reviews, dict):
        die("source_reviews must be an object")
    for source_id, review in reviews.items():
        if not re.fullmatch(r"SRC-[0-9A-F]{12}", source_id):
            die(f"invalid progress source id: {source_id}")
        if review.get("status") not in REVIEWED:
            die(f"invalid progress status: {source_id}")
        if not re.fullmatch(r"[0-9a-f]{64}", review.get("fingerprint", "")):
            die(f"invalid progress fingerprint: {source_id}")


def build_controller(manifest: dict[str, Any], queue: dict[str, Any], registry: dict[str, Any]) -> dict[str, Any]:
    ready = next((task for task in queue["tasks"] if task["status"] == "READY"), None)
    cards = registry.get("structures", [])
    unresolved_search = sum(card.get("search_status") in {"NOT_SEARCHED", "SEARCH_IN_PROGRESS", "NEEDS_REFRESH"} for card in cards)
    unresolved_decisions = sum(card.get("arsenal_decision") == "PENDING" for card in cards)
    stale_cards = sum(task["phase"] == "CARD_REFRESH" for task in queue["tasks"])
    source_complete = all(item["review_state"] == "CURRENT_REVIEWED" for item in manifest["sources"])
    source_task_count = sum(task["phase"] == "SOURCE_CENSUS" for task in queue["tasks"])
    campaign_close = (
        source_complete
        and unresolved_search == 0
        and unresolved_decisions == 0
        and stale_cards == 0
        and not manifest["arsenal_backflow_gaps"]
        and bool(registry.get("structures"))
    )
    return {
        "schema_version": 1,
        "controller": "STRUCTURE-RADAR-CONTROLLER-R01",
        "status": "READY" if ready else ("AUDIT_REQUIRED" if campaign_close else "WAITING_FOR_REGISTRY_WORK"),
        "primary_operator": "ChatGPT",
        "commands": {
            "main": "StructureRadar-main-batch",
            "audit": "StructureRadar-audit",
        },
        "scope": {
            "all_merged_stages_and_future": True,
            "latest_stage_discovered": manifest["latest_stage_discovered"],
            "stage14_15_fixed_boundary": False,
            "stage14_15_bootstrap_priority": True,
            "central_and_stage_arsenals_always_scanned": True,
        },
        "corpus": {
            "fingerprint": manifest["corpus_fingerprint"],
            "source_count": manifest["source_count"],
            "review_states": manifest["counts_by_review_state"],
            "arsenal_backflow_gaps": manifest["arsenal_backflow_gaps"],
        },
        "queue": {
            "task_count": len(queue["tasks"]),
            "source_census_task_count": source_task_count,
            "current_task": ready["task_id"] if ready else None,
            "current_phase": ready["phase"] if ready else None,
        },
        "initial_execution_estimate": {
            "recommended_source_tasks_per_main_invocation": "3-6",
            "estimated_main_invocations_min": (source_task_count + 5) // 6,
            "estimated_main_invocations_max": (source_task_count + 2) // 3,
            "estimate_is_guarantee": False,
            "material_new_cards_may_add_audit_or_search_rounds": True,
        },
        "registry": {
            "structure_count": len(cards),
            "unresolved_search_count": unresolved_search,
            "pending_arsenal_decision_count": unresolved_decisions,
            "stale_provenance_task_count": stale_cards,
        },
        "codex_delegation": {
            "routine_research_delegated": False,
            "allowed_reasons": [
                "EXTRACTOR_OR_VERIFIER_FAILURE",
                "MANIFEST_OR_PROGRESS_INCONSISTENCY",
                "LARGE_DETERMINISTIC_REINDEX",
                "PROVENANCE_MAPPING_CONFLICT",
                "CI_OR_WORKFLOW_FAILURE",
            ],
        },
        "close_conditions": {
            "all_current_sources_reviewed": source_complete,
            "all_searches_resolved": unresolved_search == 0,
            "all_arsenal_decisions_resolved": unresolved_decisions == 0,
            "all_card_provenance_current": stale_cards == 0,
            "arsenal_backflow_clear": not manifest["arsenal_backflow_gaps"],
            "final_independent_audit_required": True,
            "campaign_close_allowed_before_final_audit": campaign_close,
        },
        "next_expected_command": "StructureRadar-main-batch" if ready else "StructureRadar-audit" if campaign_close else "StructureRadar-main-batch",
        "pull_request_policy": {
            "main_batches_use_draft_pr": True,
            "main_lane_may_self_award_mathematical_audit_pass": False,
            "audit_pass_closes_only_submitted_batch": True,
        },
    }


def generated_documents() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    progress = load_json(PROGRESS_PATH)
    registry = load_json(REGISTRY_PATH)
    validate_progress(progress)
    manifest = build_manifest(progress)
    validate_registry(registry, manifest)
    queue = build_queue(manifest, registry)
    controller = build_controller(manifest, queue, registry)
    return manifest, queue, controller


def manifest_documents(manifest: dict[str, Any]) -> dict[Path, str]:
    sources = manifest["sources"]
    part_records = []
    documents: dict[Path, str] = {}
    for index, batch in enumerate(chunks(sources, MANIFEST_PART_SIZE), start=1):
        relative = f"docs/structure-radar/source-manifest/part-{index:04d}.json"
        part = {
            "schema_version": 1,
            "manifest": "STRUCTURE-RADAR-SOURCE-MANIFEST-PART-R01",
            "corpus_fingerprint": manifest["corpus_fingerprint"],
            "part_number": index,
            "source_count": len(batch),
            "sources": batch,
        }
        text = dump_json(part)
        documents[ROOT / relative] = text
        part_records.append(
            {
                "path": relative,
                "source_count": len(batch),
                "first_source_id": batch[0]["source_id"],
                "last_source_id": batch[-1]["source_id"],
                "content_fingerprint": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            }
        )
    index_data = {key: value for key, value in manifest.items() if key != "sources"}
    index_data["part_size"] = MANIFEST_PART_SIZE
    index_data["parts"] = part_records
    documents[MANIFEST_PATH] = dump_json(index_data)
    return documents


def verify_cross_file(manifest: dict[str, Any], queue: dict[str, Any], controller: dict[str, Any]) -> None:
    if not manifest["scope"]["all_merged_stages"] or not manifest["scope"]["future_stage_auto_discovery"]:
        die("radar scope is not repository-wide and future-aware")
    if not manifest["scope"]["stage14_15_are_bootstrap_not_boundary"]:
        die("Stage14/15 incorrectly became the scope boundary")
    paths = {item["path"] for item in manifest["sources"]}
    required = {
        "docs/research-arsenal-index.json",
        "docs/stage14-15-bound-attack-map.md",
        "docs/stage14-15-bound-deep-review-queue.json",
        "docs/stage14-toolbox/index.json",
        "docs/stage14-toolbox/cards/TB-FORMULA-two-quadric-pencil.md",
        "docs/stage26-arsenal-promotion.md",
        "stages/stage02/data/geometry/audit_report.json",
        "stages/stage12/archive/docs/stage12-n1-2c-gao-zhao.md",
        "stages/stage26/26-60/general-saunderson-proof.md",
        "stages/stage26/26-70/result.md",
        "stages/stage27/27-40/result.md",
    }
    missing = sorted(required - paths)
    if missing:
        die("mandatory radar source missing: " + ", ".join(missing))
    latest_match = re.fullmatch(r"Stage(\d+)", manifest["latest_stage_discovered"] or "")
    if latest_match is None or int(latest_match.group(1)) < 27:
        die("latest merged stage discovery regressed below Stage27")
    source_ids = {item["source_id"] for item in manifest["sources"] if item["review_state"] != "CURRENT_REVIEWED"}
    queued_ids = [source_id for task in queue["tasks"] if task["phase"] == "SOURCE_CENSUS" for source_id in task["source_ids"]]
    if len(queued_ids) != len(set(queued_ids)):
        die("source appears in more than one census queue task")
    if set(queued_ids) != source_ids:
        die("census queue does not exactly cover unreviewed/changed sources")
    if sum(task["status"] == "READY" for task in queue["tasks"]) > 1:
        die("more than one StructureRadar task is READY")
    if controller["scope"]["stage14_15_fixed_boundary"]:
        die("controller regressed to a Stage14/15-only scope")
    if controller["corpus"]["fingerprint"] != manifest["corpus_fingerprint"]:
        die("controller corpus fingerprint mismatch")


def refresh(check: bool) -> None:
    manifest, queue, controller = generated_documents()
    verify_cross_file(manifest, queue, controller)
    expected = {
        QUEUE_PATH: dump_json(queue),
        CONTROLLER_PATH: dump_json(controller),
    }
    expected.update(manifest_documents(manifest))
    expected_part_paths = {path for path in expected if path.parent == MANIFEST_PART_DIR}
    existing_part_paths = set(MANIFEST_PART_DIR.glob("part-*.json")) if MANIFEST_PART_DIR.is_dir() else set()
    if check:
        stale = [str(path.relative_to(ROOT)) for path, text in expected.items() if not path.is_file() or path.read_text(encoding="utf-8") != text]
        stale.extend(str(path.relative_to(ROOT)) for path in sorted(existing_part_paths - expected_part_paths))
        if stale:
            die("generated StructureRadar files are stale: " + ", ".join(stale))
    else:
        RADAR.mkdir(parents=True, exist_ok=True)
        MANIFEST_PART_DIR.mkdir(parents=True, exist_ok=True)
        for path in existing_part_paths - expected_part_paths:
            path.unlink()
        for path, text in expected.items():
            path.write_text(text, encoding="utf-8")
    print("STRUCTURE_RADAR_CONTROLLER=PASS")
    print(f"LATEST_STAGE={manifest['latest_stage_discovered']}")
    print(f"SOURCE_COUNT={manifest['source_count']}")
    print(f"QUEUE_TASKS={len(queue['tasks'])}")
    print(f"ARSENAL_BACKFLOW_GAPS={len(manifest['arsenal_backflow_gaps'])}")
    print(f"CORPUS_FINGERPRINT={manifest['corpus_fingerprint']}")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("refresh", help="rewrite manifest, queue, and controller")
    sub.add_parser("verify", help="verify committed generated files")
    args = parser.parse_args()
    refresh(check=args.command == "verify")


if __name__ == "__main__":
    main()
