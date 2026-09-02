#!/usr/bin/env python3
"""Query the machine-only positive-asset evidence locator and emit JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


INDEX = Path(__file__).with_name("index.json")


def normalize(value: str) -> str:
    value = re.sub(r"x\s*\(\s*8\s*\)", " x8 ", value.lower())
    value = re.sub(r"\bx8\s*[x×]\s*x8\b", " x8 product x8 ", value)
    return " ".join(re.findall(r"[a-z0-9]+", value.replace("×", " x ")))


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)
    elif isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from strings(item)


def field_score(asset: dict, term: str) -> tuple[int, list[str]]:
    wanted = normalize(term)
    wanted_tokens = set(wanted.split())
    weights = {
        "asset_id": 12,
        "objects": 10,
        "aliases": 9,
        "relations": 7,
        "outputs": 6,
        "candidate_queries": 4,
        "files": 2,
        "limitations": 1,
    }
    score = 0
    fields = []
    for field, weight in weights.items():
        haystack = normalize(" ".join(strings(asset.get(field, []))))
        if wanted and wanted in haystack:
            score += weight * 2
            fields.append(field)
        elif wanted_tokens and wanted_tokens.issubset(set(haystack.split())):
            score += weight
            fields.append(field)
    return score, fields


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("terms", nargs="+", help="objects, aliases, relations, or labels")
    parser.add_argument("--stage", type=int)
    parser.add_argument("--authority")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    registry = json.loads(INDEX.read_text())
    matches = []
    for asset in registry["assets"]:
        if args.stage is not None and asset["stage"] != args.stage:
            continue
        if args.authority is not None and asset["authority"] != args.authority:
            continue
        score = 0
        matched = {}
        for term in args.terms:
            term_score, fields = field_score(asset, term)
            if term_score:
                score += term_score
                matched[term] = fields
        if score:
            matches.append({
                "asset_id": asset["asset_id"],
                "score": score,
                "matched_terms": matched,
                "stage": asset["stage"],
                "authority": asset["authority"],
                "status": asset["status"],
                "objects": asset["objects"],
                "relations": asset["relations"],
                "outputs": asset["outputs"],
                "limitations": asset["limitations"],
                "files": asset["files"],
                "source_refs": asset["source_refs"],
            })
    matches.sort(key=lambda item: (-item["score"], item["asset_id"]))
    result = {
        "schema": "PERFECT_CUBOID_EVIDENCE_QUERY_RESULT_V1",
        "query": args.terms,
        "filters": {"stage": args.stage, "authority": args.authority},
        "registry_indexed_main_commit": registry["indexed_main_commit"],
        "match_count": len(matches),
        "matches": matches[:args.limit],
        "firewalls": {
            "query_miss_proves_repo_absence": False,
            "locator_match_grants_mathematical_credit": False,
            "live_stage_authority_must_be_checked": True
        }
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
