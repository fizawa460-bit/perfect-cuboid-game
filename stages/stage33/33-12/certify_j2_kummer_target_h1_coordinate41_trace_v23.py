#!/usr/bin/env python3
"""Trace the v22 separating coordinate to its exact raw Pic/2 representative."""
from __future__ import annotations

import hashlib
import json
import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "j2-kummer-target-h1-coordinate41-trace-v23.json"
LOCKS = {
    "v22": (
        HERE / "j2-kummer-source-target-module-source-first-v22.json",
        "e51a5f13a17cf7c24e789dd4feedf6797db5cfa89486046c9a96692abe96ef2c",
    ),
    "h1_basis": (
        HERE / "full-surface-pic2-kummer-target.json",
        "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890",
    ),
    "named_target": (
        HERE / "j2-named-v4-h1-target-before-source-orientation.json",
        "4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3",
    ),
}
PROJECTION_SCRIPT_SHA256 = "6aebc8e3072c52ea797940dbe6ddc535ed2e01fac9d31c715714aad4a2bb8754"


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


data = {name: locked(path, digest) for name, (path, digest) in LOCKS.items()}
projection_path = HERE / "v4_pic2_raw_cocycle_projection.py"
assert hashlib.sha256(projection_path.read_bytes()).hexdigest() == PROJECTION_SCRIPT_SHA256
projection = runpy.run_path(str(projection_path))

v22 = data["v22"]
assert v22["locked_named_j2"]["separating_functional_support_1based"] == [41]
basis = data["h1_basis"]["finite_v4_pic2_cohomology"][
    "H1_quotient_basis_cc_ct_pairs_original_pic2_coordinates_f2"
]
assert len(basis) == 75
b41 = basis[40]
cc_support = [i + 1 for i, x in enumerate(b41["cc"]) if x]
ct_support = [i + 1 for i, x in enumerate(b41["ct"]) if x]
assert cc_support == []
assert ct_support == [9, 11, 19]

target = data["named_target"]
raw = target["raw_named_J2_cocycle_historical_Magma_Pic64_mod2"]
projected = projection["project_raw_cocycle"](raw["cc"], raw["ct"])
assert projected["coordinates_f2"] == target["retained_H1_projection"]["coordinates_f2"]
assert projected["coordinates_f2"][40] == 1
raw_cc_support = [i + 1 for i, x in enumerate(raw["cc"]) if x]
raw_ct_support = [i + 1 for i, x in enumerate(raw["ct"]) if x]
coboundary_support = [
    i + 1 for i, x in enumerate(projected["one_coboundary_coefficient_witness_f2"]) if x
]

out = {
    "schema": "STAGE33_12_J2_KUMMER_TARGET_H1_COORDINATE41_TRACE_V23",
    "stage": "33-12",
    "status": "PASS_EXACT_TARGET_ADAPTER_GAP_TRACED_TO_H1_BASIS41",
    "source_locks": {name: digest for name, (_, digest) in LOCKS.items()},
    "projection_script_sha256": PROJECTION_SCRIPT_SHA256,
    "separating_coordinate": {
        "H1_coordinate_1based": 41,
        "annihilates_every_source_first_j2_reachable_extension_image": True,
        "value_on_locked_named_j2_target": 1,
        "H1_basis41_raw_pic2_cc_support_1based": cc_support,
        "H1_basis41_raw_pic2_ct_support_1based": ct_support,
        "H1_basis41_raw_pair_formula": "(cc=0, ct=e9+e11+e19) in historical Magma Pic64/2 coordinates",
    },
    "locked_target_replay": {
        "raw_cc_support_1based": raw_cc_support,
        "raw_ct_support_1based": raw_ct_support,
        "projection_coboundary_coefficient_support_1based": coboundary_support,
        "H1_support_1based": [i + 1 for i, x in enumerate(projected["coordinates_f2"]) if x],
        "H1_coordinate41": 1,
        "projection_reconstruction_exact": projected["reconstruction_exact"],
    },
    "narrowed_missing_interface": {
        "source_coordinate_or_label_in_blocker": False,
        "exact_last_mismatch": "the locked target contains H1 basis41=(0,e9+e11+e19), while every defect from the source-first J2 row in every locked V4 block extension has basis41 coefficient zero",
        "next_exact_action": "audit the semantic/raw-cocycle justification for the target's basis41 coefficient and the row-action block-extension convention at this one quotient coordinate",
    },
    "promotion_firewall": {
        "source_target_relation_materialized": False,
        "standard_columns_materialized": 0,
        "stage33_progress": "6/11",
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
    },
}
out["canonical_sha256"] = csha(out)
if "--check" in sys.argv:
    assert locked(OUT, out["canonical_sha256"]) == out
else:
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "coordinate": 41,
    "basis41_ct_support": ct_support,
    "canonical_sha256": out["canonical_sha256"],
    "marker": "PROOF_REPLAY_COMPLETE",
}, sort_keys=True))
