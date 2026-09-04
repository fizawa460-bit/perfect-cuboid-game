#!/usr/bin/env python3
"""Bounded interface diagnostic for transporting the exact #1529 S symmetry to Stage33 proper14.

No new Brauer/Gysin column is granted here.  The diagnostic reads only the
source-locked retained Stage32 automorphism data and the certified Stage33-09
marked-Picard bridge to determine whether S:B1->B3 has an exact target action.
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
S09 = HERE.parent / "33-09"
S32 = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(S07))

from stage32_picard_marking_retained import load as load_marking  # type: ignore

ADAPTER = S32 / "post1529-fsm-stoll-diagonal-action-source-lock.json"
BRIDGE = S09 / "marked-picard-basis-bridge-certified.json"
MARKING_SHA = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
ADAPTER_SHA = "5726289d8948beaaf3ed4e2dc260f49d1b3b3054642f3460b6b1e53c77ea23bc"
BRIDGE_BLOB = "77b16e2ee80c33af27f7a5a04e1c465e9fc1acea"


def csha(obj: dict, field: str) -> str:
    body = dict(obj)
    claimed = body.pop(field)
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert claimed == got
    return got


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


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
    try:
        return [int(x) for x in line.split()]
    except ValueError:
        return None


marking = load_marking()
assert marking["canonical_sha256"] == MARKING_SHA
adapter = json.loads(ADAPTER.read_text(encoding="utf-8"))
assert csha(adapter, "canonical_sha256_without_this_field") == ADAPTER_SHA
assert blob_sha(BRIDGE) == BRIDGE_BLOB
bridge = json.loads(BRIDGE.read_text(encoding="utf-8"))
S = adapter["fsm_section2_actions"]["S"]
assert S["stoll_word"] == "g2*g5"
assert S["normalized_box_action"] == ["a3", "-a2", "a1", "b3", "b2", "b1", "c"]

# Hperp structural inventory retained from the previous V82 probe.
htext = marking.get("hperp_text", "")
assert isinstance(htext, str)
lines = htext.splitlines()
parsed = [ints(ln) for ln in lines]
count_hist = collections.Counter(len(v) for v in parsed if v is not None)
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

# Inspect only schema/keys and small symbolic metadata from the certified
# bridge.  Do not dump 64x64 matrices in the log.
bridge_top = {k: shape(v) for k, v in bridge.items()}
acs = bridge.get("actual_coordinate_swaps_in_historical_magma_picard_basis", {})
assert isinstance(acs, dict)
acs_shapes = {k: shape(v) for k, v in acs.items()}
small_acs = {
    k: v for k, v in acs.items()
    if isinstance(v, (str, bool, int, float))
    or (isinstance(v, list) and len(v) <= 20 and not (v and isinstance(v[0], list)))
}

print(json.dumps({
    "success": True,
    "marker": "V82_BOUNDED_S_TRANSPORT_INTERFACE_DIAGNOSTIC",
    "marking_canonical_sha256": MARKING_SHA,
    "bridge_blob_sha1": BRIDGE_BLOB,
    "bridge_canonical_sha256": bridge.get("canonical_sha256"),
    "S_stoll_word": S["stoll_word"],
    "S_box_action": S["normalized_box_action"],
    "S_maps_B1_to_B3": True,
    "hperp_line_count": len(lines),
    "hperp_numeric_token_count_histogram": dict(sorted(count_hist.items())),
    "hperp_block_runs": runs,
    "bridge_top_level_shapes": bridge_top,
    "coordinate_swap_interface_shapes": acs_shapes,
    "coordinate_swap_small_metadata": small_acs,
    "proper14_action_materialized": False,
    "b3_gysin_image_materialized": False,
    "merge_allowed": False,
}, sort_keys=True))
