#!/usr/bin/env python3
"""Network-free exact replay of the retained sign(a3) recovery of BigK row 39."""
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROBE = HERE / "probe_j2_order4_row39_retained_symmetry_v11.py"
CERT = HERE / "j2-order4-row39-retained-symmetry-transport-v11.json"
NEXT = HERE / "j2-order4-retained-pullback-row-availability-v12.json"
CERT_SHA = "a83d558fc96822d9b8a01512e7d1afa3cf9db0958718325a27fddb32ba753604"
NEXT_SHA = "61a8523c8ca788c58aa0c3732694406230e4fd11afbe67a2d63d5543b0dda9ec"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body)
    return obj


cert = locked(CERT, CERT_SHA)
nxt = locked(NEXT, NEXT_SHA)
probe = runpy.run_path(str(PROBE))["out"]
assert probe["success"] is True
assert probe["transport"] == {
    "automorphism": "sign_a3",
    "stage32_aut_generator_index_1based": 6,
    "BigK_source_row_1based": 35,
    "BigK_target_row_1based": 39,
    "full_surface_known_source_preimage_1based": 53,
    "full_surface_known_target_preimage_1based": 57,
}
assert cert["schema"] == "STAGE33_12_J2_ORDER4_ROW39_RETAINED_SYMMETRY_TRANSPORT_V1"
assert cert["row39"] == {
    "BigK_index_1based": 39,
    **probe["row39"],
}
assert cert["retained_symmetry_transport"]["source_full_surface_known_preimage_indices_1based"] == [53]
assert cert["retained_symmetry_transport"]["target_full_surface_known_preimage_indices_1based"] == [57]
assert cert["retained_symmetry_transport"]["whole_pullback_divisor_transported_exactly"] is True
assert cert["retained_symmetry_transport"]["additional_contracted_exceptional_components_on_row39"] is False
assert cert["execution"]["remote_cas_used"] is False
assert cert["execution"]["new_external_magma_dispatch_used"] is False
assert cert["exact_consequence"]["remaining_unretained_rows_1based"] == [20, 67]
assert cert["exact_consequence"]["named_j2_order4_source_coordinate_materialized"] is False
assert not cert["promotion_firewall"]["stage33_12_closed_exact"]
assert not cert["promotion_firewall"]["theorem_credit"]
assert not cert["promotion_firewall"]["receiver_credit"]
assert not cert["promotion_firewall"]["endpoint_credit"]
assert cert["promotion_firewall"]["matrix_standard_columns_materialized"] == 0
assert cert["stage33_progress"] == "6/11"

assert nxt["schema"] == "STAGE33_12_J2_ORDER4_RETAINED_PULLBACK_ROW_AVAILABILITY_V2"
assert nxt["source_locks"]["row39_retained_symmetry_transport_sha256"] == CERT_SHA
assert nxt["effective_unretained_required_rows_1based"] == [20, 67]
assert nxt["effective_retained_required_rows_1based"] == [2, 4, 9, 10, 35, 39, 47, 49]
assert nxt["newly_recovered_row_1based"] == [39]
assert nxt["acquisition_boundary"]["new_external_magma_dispatch_authorized"] is False
assert nxt["no_inference"]["historical_mask6_reused_as_named_j2_source"] is False
assert nxt["no_inference"]["named_j2_order4_source_coordinate_materialized"] is False
assert nxt["no_inference"]["s3_or_target_compatibility_may_fill_missing_rows"] is False
assert nxt["promotion_firewall"]["matrix_standard_columns_materialized"] == 0
assert nxt["stage33_progress"] == "6/11"

print(json.dumps({
    "success": True,
    "row39_certificate_sha256": CERT_SHA,
    "next_availability_sha256": NEXT_SHA,
    "remaining_unretained_BigK_rows_1based": [20, 67],
    "new_external_magma_dispatch_used": False,
    "named_j2_order4_source_coordinate_materialized": False,
}, sort_keys=True))
