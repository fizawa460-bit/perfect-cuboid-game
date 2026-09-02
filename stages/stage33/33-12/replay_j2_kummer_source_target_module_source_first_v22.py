#!/usr/bin/env python3
"""Replay the full V4 extension audit from the v21 source-first J2 row."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "audit_v4_kummer_extension_space_after_j2_anchor.py"
OUT = HERE / "j2-kummer-source-target-module-source-first-v22.json"
BASE_SHA256 = "1da134f48a1eddb9eb3e843455f29c0a1bffa9fe6f17eb02afdeda51ba73765d"
BASE_BLOB = "2c3a05de3f49799392805b4dbeae0f1367517ec8"
V21_SHA = "19c464602d6ad1b6c32b0b08c50a6bcc55b8e606642a5ae52e7f51fdc2f12366"


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


v21 = locked(HERE / "j2-order4-swap-functional-source-v21.json", V21_SHA)
source_text = BASE.read_text()
assert hashlib.sha256(source_text.encode()).hexdigest() == BASE_SHA256

patched = source_text
replacements = [
    (
        'ADJOINT = HERE / "j2-picard-adjoint-proper-br2.json"',
        'V21 = HERE / "j2-order4-swap-functional-source-v21.json"',
    ),
    (
        'ADJOINT_SHA = "066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8"',
        f'V21_SHA = "{V21_SHA}"',
    ),
    ('adjoint = locked(ADJOINT, ADJOINT_SHA)', 'v21_source = locked(V21, V21_SHA)'),
    (
        'j2 = adjoint["proper_brauer2_pullback"]["proper_Br2_14D_coordinate_f2"]',
        'j2 = v21_source["named_full_surface_source"]["proper14_f2"]',
    ),
    (
        '"j2_picard_adjoint_canonical_sha256": ADJOINT_SHA,',
        '"j2_source_first_v21_canonical_sha256": V21_SHA,',
    ),
]
for old, new in replacements:
    assert old in patched
    patched = patched.replace(old, new)

needle = '''def insert_labelled(echelon: dict[int, tuple[int, int]], vector: int, label: int) -> bool:
    while vector:
        pivot = vector.bit_length() - 1
        if pivot in echelon:
            vector ^= echelon[pivot][0]
            label ^= echelon[pivot][1]
        else:
            echelon[pivot] = (vector, label)
            return True
    return False
'''
addition = needle + '''

def separating_functional(rows: list[int], target: int, n: int) -> int:
    equations = [int(row) for row in rows] + [int(target) | (1 << n)]
    rank = 0
    pivots = []
    for col in range(n):
        pivot = next((i for i in range(rank, len(equations)) if (equations[i] >> col) & 1), None)
        if pivot is None:
            continue
        equations[rank], equations[pivot] = equations[pivot], equations[rank]
        for i in range(len(equations)):
            if i != rank and ((equations[i] >> col) & 1):
                equations[i] ^= equations[rank]
        pivots.append(col)
        rank += 1
    assert not any((row & ((1 << n) - 1)) == 0 and ((row >> n) & 1) for row in equations)
    witness = 0
    for i, col in enumerate(pivots):
        if (equations[i] >> n) & 1:
            witness |= 1 << col
    assert all(((witness & row).bit_count() & 1) == 0 for row in rows)
    assert (witness & target).bit_count() & 1
    return witness
'''
assert needle in patched
patched = patched.replace(needle, addition)

needle = 'j2_target_reachable = in_span(j2_reachable, j2_h1)'
replacement = needle + '''
j2_separating_functional = separating_functional(list(j2_reachable.values()), j2_h1, H1)
assert all(((j2_separating_functional & row).bit_count() & 1) == 0 for row in j2_reachable.values())
assert (j2_separating_functional & j2_h1).bit_count() & 1
'''
assert needle in patched
patched = patched.replace(needle, replacement)

needle = '''        "locked_target_reachable_from_locked_source": j2_target_reachable,
    },'''
replacement = '''        "locked_target_reachable_from_locked_source": j2_target_reachable,
        "separating_functional_75D_f2": [(j2_separating_functional >> i) & 1 for i in range(H1)],
        "separating_functional_support_1based": [i + 1 for i in range(H1) if (j2_separating_functional >> i) & 1],
        "separating_functional_annihilates_reachable_subspace": True,
        "separating_functional_value_on_locked_target": 1,
    },'''
assert needle in patched
patched = patched.replace(needle, replacement)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    exec(compile(patched, str(BASE), "exec"), {"__file__": str(BASE), "__name__": "__main__"})
raw = json.loads(capture.getvalue().strip().splitlines()[-1])
raw.pop("canonical_sha256")
reach = raw["target_reachability_over_all_nonzero_retained_sources"]
compatible = reach.pop("compatible_source_masks_decimal")
reach.pop("compatible_source_supports_1based")
compatible_set = set(compatible)
incompatible = [mask for mask in range(1, 1 << 10) if mask not in compatible_set]
assert len(compatible) == reach["compatible_source_count"]
reach["incompatible_source_count"] = len(incompatible)
reach["incompatible_source_masks_decimal"] = incompatible
reach["all_nonzero_retained_sources_partitioned"] = len(compatible) + len(incompatible) == (1 << 10) - 1

raw["schema"] = "STAGE33_12_V4_KUMMER_EXTENSION_REACHABILITY_SOURCE_FIRST_V3"
raw["status"] = "FAIL_EXACT_SOURCE_FIRST_J2_TARGET_UNREACHABLE"
raw["source_locks"]["base_audit_script_git_blob_sha1"] = BASE_BLOB
raw["source_locks"]["base_audit_script_sha256"] = BASE_SHA256
raw["source_locks"]["j2_source_first_v21_canonical_sha256"] = V21_SHA
raw["exact_consequence"] = {
    "named_j2_source_coordinate_remains_exact": True,
    "source_label_or_orientation_is_no_longer_in_the_blocker": True,
    "locked_75D_target_reachable_from_source": False,
    "reachable_subspace_dimension_f2": raw["locked_named_j2"]["reachable_H1_subspace_dimension_f2"],
    "separating_functional_materialized": True,
    "remaining_interface": "TARGET_H1_PROJECTION_OR_KUMMER_BLOCK_EXTENSION_CONVENTION_ADAPTER",
    "historical_source_target_relation_restored": False,
    "standard_columns_materialized": 0,
}
raw["promotion_firewall"] = {
    "source_coordinate_revoked": False,
    "target_coordinate_revoked": False,
    "source_target_relation_materialized": False,
    "stage33_progress": "6/11",
    "stage33_12_closed_exact": False,
    "stage33_13_released": False,
    "theorem_credit": False,
    "receiver_credit": False,
    "endpoint_credit": False,
}

assert raw["locked_named_j2"]["proper14_f2"] == v21["named_full_surface_source"]["proper14_f2"]
assert raw["locked_named_j2"]["retained10_support_1based"] == [2, 3]
assert raw["locked_named_j2"]["locked_target_reachable_from_locked_source"] is False
assert raw["locked_named_j2"]["reachable_H1_subspace_dimension_f2"] == 13
assert raw["locked_named_j2"]["separating_functional_value_on_locked_target"] == 1
assert raw["locked_named_j2"]["separating_functional_annihilates_reachable_subspace"] is True

raw["canonical_sha256"] = csha(raw)
if "--check" in sys.argv:
    assert locked(OUT, raw["canonical_sha256"]) == raw
else:
    OUT.write_text(json.dumps(raw, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "status": raw["status"],
    "reachable_dimension": 13,
    "target_reachable": False,
    "separating_support": raw["locked_named_j2"]["separating_functional_support_1based"],
    "compatible_source_count": len(compatible),
    "incompatible_source_count": len(incompatible),
    "canonical_sha256": raw["canonical_sha256"],
    "marker": "PROOF_REPLAY_COMPLETE",
}, sort_keys=True))
