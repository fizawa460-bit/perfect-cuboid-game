#!/usr/bin/env python3
"""Replay the Stage33-12 order-4 retained pullback-row availability narrowing."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]

CERT = HERE / "j2-order4-retained-pullback-row-availability-v11.json"
ORDER4 = HERE / "j2-order4-brauer-lift-reduction.json"
CT_ROWS = HERE / "j2-ct-six-kc-support-fullpic64-pullbacks.json"
CONTROLLER = ROOT / "stages/stage33/controller.json"

ORDER4_SHA = "a524121930e1c712bd8d8220415ef1836b11cd6eb11f2bb44f70dc844f6d85b0"
CT_ROWS_SHA = "592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d"
CERT_SHA = "80331cf22bdb1663bc3834039d2c65e4c006aea8d3c06d3fbf379fe1354cdf72"


def csha(obj: dict) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text())
    body = dict(obj)
    got = body.pop("canonical_sha256")
    assert got == expected == csha(body), path
    return obj


cert = load_canonical(CERT, CERT_SHA)
order4 = load_canonical(ORDER4, ORDER4_SHA)
ct_rows = load_canonical(CT_ROWS, CT_ROWS_SHA)
controller = json.loads(CONTROLLER.read_text())

required = order4["semantic_order4_generator"]["required_BigK_rows_1based"]
original_additional = order4["next_numeric_leaf"]["materialize_additional_BigK_pullback_rows_1based"]
reuse = order4["next_numeric_leaf"]["reuse_already_materialized_BigK_rows_1based"]
ct_indices = ct_rows["target_BigK_support_1based"]
new_reuse = sorted(set(original_additional) & set(ct_indices))
effective_retained = sorted(set(reuse) | set(new_reuse))
effective_unretained = sorted(set(required) - set(effective_retained))

assert required == [2, 4, 9, 10, 20, 35, 39, 47, 49, 67]
assert original_additional == [20, 35, 39, 67]
assert reuse == [2, 4, 9, 10, 47, 49]
assert ct_indices == [26, 35, 42, 47, 49, 52]
assert new_reuse == [35]
assert effective_retained == [2, 4, 9, 10, 35, 47, 49]
assert effective_unretained == [20, 39, 67]

assert cert["order4_required_BigK_pullback_rows_1based"] == required
assert cert["order4_original_additional_rows_1based"] == original_additional
assert cert["order4_reuse_rows_1based"] == reuse
assert cert["ct_six_support_certificate_BigK_rows_1based"] == ct_indices
assert cert["newly_reusable_order4_row_from_existing_ct_certificate_1based"] == new_reuse
assert cert["effective_retained_required_rows_1based"] == effective_retained
assert cert["effective_unretained_required_rows_1based"] == effective_unretained

s = controller["stage33_12"]
assert controller["schema"] == "STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V55_V10_AUDIT_PASS_NAMED_ORDER4_SOURCE_GAP"
assert s["new_external_magma_dispatch_authorized"] is False
assert s["finite_v4_kummer_columns_materialized"] == 0
assert s["corrected_J2_proper_Br2_14D_coordinate_materialized"] is False
assert s["corrected_J2_retained_10D_domain_coordinate_materialized"] is False
assert s["historical_picard_adjoint_mask6_reused_as_named_J2_source"] is False
assert controller["stage33_progress"] == "6/11"
assert controller["merge_allowed"] is False
assert controller["theorem_credit"] is False
assert controller["receiver_credit"] is False
assert controller["endpoint_credit"] is False

assert cert["acquisition_boundary"]["new_external_magma_dispatch_authorized"] is False
assert cert["no_inference"]["historical_mask6_reused_as_named_j2_source"] is False
assert cert["no_inference"]["named_j2_order4_source_coordinate_materialized"] is False
assert cert["promotion_firewall"]["matrix_standard_columns_materialized"] == 0
assert cert["promotion_firewall"]["stage33_12_closed_exact"] is False

print(json.dumps({
    "success": True,
    "canonical_sha256": CERT_SHA,
    "newly_reusable_row": 35,
    "effective_unretained_rows": effective_unretained,
    "external_magma_dispatch_authorized": False,
    "named_j2_source_materialized": False,
}, sort_keys=True))
