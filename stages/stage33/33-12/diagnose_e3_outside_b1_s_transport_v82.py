#!/usr/bin/env python3
"""Bounded interface diagnostic for transporting the exact #1529 S symmetry to Stage33 proper14.

This leaf does not grant a new Brauer/Gysin column.  It only exposes the
already source-locked retained Stage32 marking interface needed to decide
whether the B1 -> B3 symmetry route can be made mechanically exact without a
repository-wide search.
"""
from __future__ import annotations

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


marking = load_marking()
assert marking["canonical_sha256"] == MARKING_SHA
adapter = json.loads(ADAPTER.read_text(encoding="utf-8"))
assert csha(adapter, "canonical_sha256_without_this_field") == ADAPTER_SHA
S = adapter["fsm_section2_actions"]["S"]
assert S["stoll_word"] == "g2*g5"
assert S["normalized_box_action"] == ["a3", "-a2", "a1", "b3", "b2", "b1", "c"]

summary = {k: shape(v) for k, v in marking.items() if k != "canonical_sha256"}
# Nested summaries only for exact interfaces plausibly useful to construct the
# Picard/proper14 action; no payload values or recursive repo enumeration.
nested = {}
for k in ("picard", "picard_core", "all140", "known_classes", "aut_action", "marking"):
    if k in marking and isinstance(marking[k], dict):
        nested[k] = {kk: shape(vv) for kk, vv in marking[k].items()}

print(json.dumps({
    "success": True,
    "marker": "V82_BOUNDED_S_TRANSPORT_INTERFACE_DIAGNOSTIC",
    "marking_canonical_sha256": MARKING_SHA,
    "S_stoll_word": S["stoll_word"],
    "S_maps_B1_to_B3": True,
    "top_level_interface": summary,
    "nested_candidate_interfaces": nested,
    "proper14_action_materialized": False,
    "b3_gysin_image_materialized": False,
    "merge_allowed": False,
}, sort_keys=True))
