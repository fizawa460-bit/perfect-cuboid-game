#!/usr/bin/env python3
"""Replay the generic raw-cocycle -> locked 75D H1 projection on named J2."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from v4_pic2_raw_cocycle_projection import project_raw_cocycle


HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-named-v4-h1-target-before-source-orientation.json"
CT = HERE / "j2-ct-six-kc-support-fullpic64-pullbacks.json"
CC = HERE / "j2-cc-actual-cech-global-square-overlap.json"
CERT_SHA = "4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3"
CT_SHA = "592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d"
CC_SHA = "82ac2b6fe8d023c915e9cf3bb8ff38d4782dbec47f98e2593f964ea020ccc6fd"


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body)
    return obj


cert = locked(CERT, CERT_SHA)
ct_cert = locked(CT, CT_SHA)
cc_cert = locked(CC, CC_SHA)
raw_cc = cc_cert["actual_cc_defect"][
    "full_surface_Pic64_historical_Magma_mod2_coordinates"
]
raw_ct = ct_cert["ct_sum_fullPic64_historical_Magma_coordinates_mod2"]
projection = project_raw_cocycle(raw_cc, raw_ct)
stored = cert["retained_H1_projection"]

assert projection["coordinates_f2"] == stored["coordinates_f2"]
assert projection["coordinate_weight"] == stored["coordinate_weight"] == 15
assert projection["nonzero"] == stored["nonzero"] is True
assert (
    projection["one_coboundary_coefficient_witness_f2"]
    == stored["one_coboundary_coefficient_witness_f2"]
)
assert projection["reconstruction_exact"] is True

print(json.dumps({
    "success": True,
    "adapter_replays_named_J2_exactly": True,
    "named_J2_H1_target_weight": projection["coordinate_weight"],
    "certificate_sha256": CERT_SHA,
}, sort_keys=True))
