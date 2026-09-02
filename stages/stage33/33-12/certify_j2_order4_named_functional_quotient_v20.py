#!/usr/bin/env python3
"""Reduce the v19 correction torsor to the exact named-column quotient."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "j2-order4-named-functional-quotient-v20.json"
LOCKS = {
    "v19_correction_torsor": (
        HERE / "j2-order4-integral-correction-torsor-v19.json",
        "3ee11e0ecdc855083a4260c2ae4f24ef4c160a7e26a48fd3872369d117118576",
    ),
    "actual_swap_descent": (
        HERE / "j2-actual-swap-mixed-discriminant-descent.json",
        "93dc99201a04fdec7c8ad8369409e7cb593ae7f8fba44b772df1b2cc1d29cfa3",
    ),
}


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
v19 = data["v19_correction_torsor"]
swap = data["actual_swap_descent"]
enum = v19["exact_enumeration"]

assert v19["integrality_equation"]["solution_affine_dimension_f2"] == 14
assert enum["corrected_integral_order4_lifts"] == 1 << 14
assert enum["distinct_proper14_functionals"] == 16
assert enum["preimages_per_proper14_functional"] == 1 << 10
fixed = enum["joint_cc_ct_fixed_functionals"]
assert [x["retained10_mask_decimal"] for x in fixed] == [4, 5, 6, 7]

# In the retained row convention these four records are literally the affine
# plane (a,b,1,0,...,0).  Thus the named matrix column forgets the ten-bit
# fiber of integral corrections and needs only the two quotient bits (a,b).
plane = []
for rec in fixed:
    r = rec["retained10_f2"]
    assert len(r) == 10 and r[2] == 1 and not any(r[3:])
    assert rec["retained10_mask_decimal"] == sum(x << i for i, x in enumerate(r))
    plane.append({
        "quotient_bits_ab": r[:2],
        "retained10_f2": r,
        "retained10_mask_decimal": rec["retained10_mask_decimal"],
        "proper14_f2": rec["proper14_f2"],
        "proper14_mask_decimal": rec["proper14_mask_decimal"],
    })
assert sorted(x["quotient_bits_ab"] for x in plane) == [[0, 0], [0, 1], [1, 0], [1, 1]]

images = swap["residual_order4_affine_candidate_S3_action"]["candidate_images_by_retained10_mask"]
images = {int(k): {g: int(v) for g, v in rec.items()} for k, rec in images.items()}
assert sorted(images) == [4, 5, 6, 7]
assert images == {
    4: {"swap12": 7, "swap13": 4},
    5: {"swap12": 5, "swap13": 7},
    6: {"swap12": 6, "swap13": 6},
    7: {"swap12": 4, "swap13": 5},
}

out = {
    "schema": "STAGE33_12_J2_ORDER4_NAMED_FUNCTIONAL_QUOTIENT_V20",
    "stage": "33-12",
    "status": "PASS_EXACT_NAMED_COLUMN_GAP_REDUCED_TO_TWO_BITS",
    "source_locks": {name: digest for name, (_, digest) in LOCKS.items()},
    "exact_quotient": {
        "integral_correction_torsor_dimension_f2": 14,
        "integral_correction_count": 1 << 14,
        "proper14_functional_image_dimension_f2": 4,
        "proper14_functional_count": 16,
        "integral_corrections_per_functional": 1 << 10,
        "cc_ct_fixed_functional_count": 4,
        "cc_ct_fixed_correction_count": 1 << 12,
        "named_column_relevant_quotient_dimension_f2": 2,
        "named_column_relevant_quotient_count": 4,
        "retained10_affine_plane_formula": "(a,b,1,0,0,0,0,0,0,0), a,b in F2",
        "affine_plane_records": plane,
        "ten_correction_bits_are_invisible_to_the_proper_br2_source_column": True,
    },
    "actual_s3_action_on_two_bit_quotient": {
        "images_by_retained10_mask": {str(k): v for k, v in images.items()},
        "orbits": [[6], [4, 5, 7]],
        "unique_joint_fixed_mask": 6,
        "joint_fixedness_of_named_order4_lift_source_locked": False,
        "named_mask_selected": False,
    },
    "narrowed_missing_interface": {
        "previous_14_bit_selector_required_for_named_column": False,
        "minimal_missing_object": "one source-locked two-bit quotient value (a,b), equivalently the named order-4 lift's actual swap12/swap13 behavior on the four-element affine plane",
        "if_joint_swap_fixed_is_source_proved": "the exact action forces retained10 mask 6",
        "otherwise": "a source-locked nonfixed lift together with its labeled swap images identifies one of masks 4,5,7",
        "source_side_only": True,
    },
    "anti_inference": {
        "historical_mask6_assumed": False,
        "s3_fixedness_of_semantic_u1_promoted_to_order4_lift_fixedness": False,
        "target_compatibility_used": False,
        "correction_fiber_representative_promoted_to_named_lift": False,
    },
    "promotion_firewall": {
        "mathematical_state_promotion_performed": False,
        "named_j2_source_coordinate_materialized": False,
        "first_75D_matrix_column_materialized": False,
        "finite_v4_kummer_columns_materialized": 0,
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
    "named_column_gap_bits": 2,
    "candidate_masks": [4, 5, 6, 7],
    "named_selected": False,
    "canonical_sha256": out["canonical_sha256"],
    "marker": "PROOF_REPLAY_COMPLETE",
}, sort_keys=True))
