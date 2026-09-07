#!/usr/bin/env python3
"""Bounded selector for the retained exceptional P1 tangent-coordinate payload.

The retained source is intentionally read repo-side.  This script emits only
small schema/path summaries for the four A2_02 exceptional components.  It is
an inventory diagnostic, not an H2(mu2) witness and grants no mathematical
credit.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = ROOT / "stages/stage33/33-07/exceptional-p1-tangent-coordinates.json"
OUT = HERE / "e3-v91c1x-r4-exceptional-chart-selector.json"
TARGETS = ("EXC_003", "EXC_004", "EXC_011", "EXC_012")
TOKENS = (
    "chart", "patch", "open", "cover", "overlap", "local", "equation",
    "uniformizer", "tangent", "coordinate", "affine", "r0", "r1",
    "transition", "glue", "exceptional", "component", "edge", "prime",
)
MAX_HITS_PER_TARGET = 24
MAX_LIST = 24
MAX_TEXT = 240


def canonical_sha256(obj: Any) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def path_text(path: tuple[Any, ...]) -> str:
    out = "$"
    for p in path:
        if isinstance(p, int):
            out += f"[{p}]"
        else:
            out += "." + str(p)
    return out


def small_value(v: Any) -> Any:
    if v is None or isinstance(v, (bool, int, float)):
        return v
    if isinstance(v, str):
        return v if len(v) <= MAX_TEXT else v[:MAX_TEXT] + "…"
    if isinstance(v, list):
        if len(v) <= MAX_LIST and all(
            x is None or isinstance(x, (bool, int, float, str)) for x in v
        ):
            return [small_value(x) for x in v]
        return {"type": "list", "length": len(v)}
    if isinstance(v, dict):
        return {"type": "dict", "keys": sorted(v)[:80], "key_count": len(v)}
    return {"type": type(v).__name__}


def interesting_dict(d: dict[str, Any]) -> dict[str, Any]:
    selected = {}
    for k, v in d.items():
        kl = k.lower()
        if any(tok in kl for tok in TOKENS):
            selected[k] = small_value(v)
    return {
        "keys": sorted(d)[:120],
        "key_count": len(d),
        "interesting_fields": selected,
    }


def target_in_scalar(v: Any, target: str) -> bool:
    if isinstance(v, str):
        return target in v
    return False


data = json.loads(SOURCE.read_text(encoding="utf-8"))
hits: dict[str, list[dict[str, Any]]] = {t: [] for t in TARGETS}


def walk(node: Any, path: tuple[Any, ...], ancestors: tuple[tuple[tuple[Any, ...], dict[str, Any]], ...]) -> None:
    if isinstance(node, dict):
        new_ancestors = ancestors + ((path, node),)
        for k, v in node.items():
            child_path = path + (k,)
            for target in TARGETS:
                if len(hits[target]) < MAX_HITS_PER_TARGET and (
                    target in str(k) or target_in_scalar(v, target)
                ):
                    parent_rows = []
                    for apath, adict in new_ancestors[-3:]:
                        parent_rows.append({
                            "path": path_text(apath),
                            "summary": interesting_dict(adict),
                        })
                    hits[target].append({
                        "match_path": path_text(child_path),
                        "matched_key": str(k),
                        "matched_value": small_value(v),
                        "parents_nearest_last": parent_rows,
                    })
            walk(v, child_path, new_ancestors)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, path + (i,), ancestors)
    else:
        for target in TARGETS:
            if len(hits[target]) < MAX_HITS_PER_TARGET and target_in_scalar(node, target):
                parent_rows = []
                for apath, adict in ancestors[-3:]:
                    parent_rows.append({
                        "path": path_text(apath),
                        "summary": interesting_dict(adict),
                    })
                hits[target].append({
                    "match_path": path_text(path),
                    "matched_value": small_value(node),
                    "parents_nearest_last": parent_rows,
                })


walk(data, (), ())

all_interesting_keys: set[str] = set()
for rows in hits.values():
    for row in rows:
        for parent in row["parents_nearest_last"]:
            all_interesting_keys.update(parent["summary"]["interesting_fields"].keys())

lower_keys = {k.lower() for k in all_interesting_keys}
cert = {
    "schema": "stage33.e3.v91c1x_r4.exceptional_chart_selector.v1",
    "stage": "33-12",
    "role": "EXACT_NONCREDIT_R4_EXCEPTIONAL_SOURCE_SELECTOR",
    "source_path": str(SOURCE.relative_to(ROOT)),
    "source_size_bytes": SOURCE.stat().st_size,
    "targets": list(TARGETS),
    "hit_counts": {k: len(v) for k, v in hits.items()},
    "hits": hits,
    "interesting_keys_union": sorted(all_interesting_keys),
    "bounded_schema_flags": {
        "chart_like_key_seen": any("chart" in k or "patch" in k for k in lower_keys),
        "cover_or_overlap_key_seen": any("cover" in k or "overlap" in k or "open" in k for k in lower_keys),
        "uniformizer_or_local_equation_key_seen": any("uniformizer" in k or "local_equation" in k for k in lower_keys),
        "tangent_or_coordinate_key_seen": any("tangent" in k or "coordinate" in k or "affine" in k for k in lower_keys),
        "transition_or_glue_key_seen": any("transition" in k or "glue" in k for k in lower_keys),
        "r0_or_r1_key_seen": any(k in {"r0", "r1"} or "r0_" in k or "r1_" in k for k in lower_keys),
    },
    "interpretation_firewall": {
        "selector_proves_open_cover": False,
        "selector_proves_overlap_transition": False,
        "selector_proves_component_uniformizer": False,
        "accepted_source_h2_mu2_representative_materialized": False,
        "literal_mu2_2_cocycle_materialized": False,
        "equivalent_unimodular_cech_glue_materialized": False,
        "swap23_common_refinement_materialized": False,
        "h2_fixedness_credit": False,
        "mask20_credit": False,
        "theorem_credit": False,
        "merge_allowed": False,
    },
}
cert["canonical_sha256"] = canonical_sha256(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "marker": "V91C1X_R4_EXCEPTIONAL_CHART_COMPACT_SELECTOR",
    "hit_counts": cert["hit_counts"],
    "bounded_schema_flags": cert["bounded_schema_flags"],
    "certificate_sha256": cert["canonical_sha256"],
}, sort_keys=True))
