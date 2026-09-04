#!/usr/bin/env python3
"""Bounded interface diagnostic for transporting the exact #1529 S symmetry to Stage33 proper14.

This leaf grants no new Brauer/Gysin column. It exposes only structural metadata
from the source-locked retained Stage32 Hperp transcript needed to decide
whether B1 -> B3 transport can be made mechanically exact.
"""
from __future__ import annotations

import collections
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
S07 = HERE.parent / "33-07"
S32 = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(S07))

from stage32_picard_marking_retained import load as load_marking  # type: ignore

ADAPTER = S32 / "post1529-fsm-stoll-diagonal-action-source-lock.json"
MARKING_SHA = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
ADAPTER_SHA = "5726289d8948beaaf3ed4e2dc260f49d1b3b3054642f3460b6b1e53c77ea23bc"


def csha(obj: dict, field: str) -> str:
    body = dict(obj)
    claimed = body.pop(field)
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert claimed == got
    return got


def shape(x):
    if isinstance(x, list):
        if not x:
            return [0]
        if isinstance(x[0], list):
            return [len(x), len(x[0])]
        return [len(x)]
    if isinstance(x, dict):
        return {"keys": sorted(x.keys())}
    return type(x).__name__


def ints(line: str):
    toks = line.split()
    try:
        return [int(x) for x in toks]
    except ValueError:
        return None


marking = load_marking()
assert marking["canonical_sha256"] == MARKING_SHA
adapter = json.loads(ADAPTER.read_text(encoding="utf-8"))
assert csha(adapter, "canonical_sha256_without_this_field") == ADAPTER_SHA
S = adapter["fsm_section2_actions"]["S"]
assert S["stoll_word"] == "g2*g5"
assert S["normalized_box_action"] == ["a3", "-a2", "a1", "b3", "b2", "b1", "c"]

summary = {k: shape(v) for k, v in marking.items() if k != "canonical_sha256"}
nested = {}
for k in ("picard", "picard_core", "all140", "known_classes", "aut_action", "marking"):
    if k in marking and isinstance(marking[k], dict):
        nested[k] = {kk: shape(vv) for kk, vv in marking[k].items()}

htext = marking.get("hperp_text", "")
assert isinstance(htext, str)
lines = htext.splitlines()
parsed = [ints(ln) for ln in lines]
count_hist = collections.Counter(len(v) for v in parsed if v is not None)
dimension_like = [
    {"line_1based": i + 1, "values": v}
    for i, v in enumerate(parsed)
    if v is not None and 1 <= len(v) <= 4
]
non_numeric = [
    {"line_1based": i + 1, "prefix": lines[i][:120]}
    for i, v in enumerate(parsed)
    if v is None
]
# Identify run boundaries of equal numeric token count. This reveals matrix
# blocks without dumping their entries.
runs = []
i = 0
while i < len(lines):
    v = parsed[i]
    kind = "non_numeric" if v is None else f"numeric_{len(v)}"
    j = i + 1
    while j < len(lines):
        w = parsed[j]
        k2 = "non_numeric" if w is None else f"numeric_{len(w)}"
        if k2 != kind:
            break
        j += 1
    runs.append({"start_1based": i + 1, "end_1based": j, "kind": kind, "count": j - i})
    i = j

print(json.dumps({
    "success": True,
    "marker": "V82_BOUNDED_S_TRANSPORT_INTERFACE_DIAGNOSTIC",
    "marking_canonical_sha256": MARKING_SHA,
    "S_stoll_word": S["stoll_word"],
    "S_maps_B1_to_B3": True,
    "top_level_interface": summary,
    "nested_candidate_interfaces": nested,
    "hperp_line_count": len(lines),
    "hperp_numeric_token_count_histogram": dict(sorted(count_hist.items())),
    "hperp_dimension_like_lines": dimension_like,
    "hperp_non_numeric_lines": non_numeric,
    "hperp_block_runs": runs,
    "proper14_action_materialized": False,
    "b3_gysin_image_materialized": False,
    "merge_allowed": False,
}, sort_keys=True))
