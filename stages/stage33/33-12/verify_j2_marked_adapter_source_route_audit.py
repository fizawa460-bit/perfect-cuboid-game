#!/usr/bin/env python3
"""Verify the exact Stage33-12 source-route audit for the marked Br2 adapter gap."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEGACY = HERE.parent / "33-07"
AUDIT = HERE / "j2-marked-adapter-source-route-audit.json"
GAP = HERE / "j2-marked-discriminant-proper-br2-adapter-source-lock-gap.json"
REDUCTION = HERE / "j2-order4-brauer-lift-reduction.json"
ORDER4 = HERE / "materialize_j2_order4_full_surface_brauer_adapter.py"
ACTUAL_GLUE = LEGACY / "certify_index512_actual_geometry_glue_adapter.py"

AUDIT_SHA = "5fec609e3ee75fddc3833124dde81f75514de6ca8600200e594366e30022f3f8"
GAP_SHA = "e27da962e6bd4330bd2e3ede77424bedb5ad40a684d81fadba632ac2fdef8b58"
REDUCTION_SHA = "a524121930e1c712bd8d8220415ef1836b11cd6eb11f2bb44f70dc844f6d85b0"
ORDER4_BLOB = "628e77b4e41fd8f671a2f2475d3e45a82bf1d9bb"
ACTUAL_GLUE_BLOB = "d0917a48d15ea3ff4bd6dd4144d2acced0b27c2a"
STALE_V2_SHA = "d1bb3b6f15019c7ea6b0b93db49df28155bfc4f97d665fecc2a31547910a73f9"
V2_SCHEMA = "STAGE33_12_J2_ORDER4_BRAUER_LIFT_REDUCTION_V2_BILINEAR_EVALUATION"


def locked(path: Path, want: str):
    x = json.loads(path.read_text(encoding="utf-8"))
    body = dict(x)
    claimed = body.pop("canonical_sha256")
    got = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert claimed == got == want, (path, claimed, got, want)
    return x


def git_blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


audit = locked(AUDIT, AUDIT_SHA)
gap = locked(GAP, GAP_SHA)
reduction = locked(REDUCTION, REDUCTION_SHA)
assert audit["schema"] == "STAGE33_12_J2_MARKED_ADAPTER_SOURCE_ROUTE_AUDIT_V1"
assert audit["status"] == "PASS_EXACT_ROUTE_AUDIT_NO_PROMOTION"
assert gap["promotion_firewall"]["marked_adapter_materialized"] is False
assert reduction["schema"] == "STAGE33_12_J2_ORDER4_BRAUER_LIFT_REDUCTION_V1"

# The checked-in order4 producer is exact-hash locked to a different V2 reduction.
assert git_blob(ORDER4) == ORDER4_BLOB
order4_text = ORDER4.read_text(encoding="utf-8")
assert f'REDUCTION_SHA = "{STALE_V2_SHA}"' in order4_text
assert f'assert reduction["schema"] == "{V2_SCHEMA}"' in order4_text
r = audit["exact_route_audit"]["order4_half_lift_route"]
assert r["current_reduction_sha256"] == REDUCTION_SHA
assert r["current_producer_locked_expected_reduction_sha256"] == STALE_V2_SHA
assert r["current_producer_locked_expected_reduction_schema"] == V2_SCHEMA
assert r["current_route_replayable_under_locked_inputs"] is False

# The current actual-geometry glue certifier is the hostile firewalled version:
# it proves existence/order of H=T/L0 but explicitly does not identify rep88 or a labeled H.
assert git_blob(ACTUAL_GLUE) == ACTUAL_GLUE_BLOB
glue_text = ACTUAL_GLUE.read_text(encoding="utf-8")
for exact in (
    '"schema": "STAGE33_07_INDEX512_ACTUAL_GEOMETRY_GLUE_ADAPTER_V2_FIREWALLED"',
    '"actual_glue_H_exists_as_T_over_L0": True',
    '"actual_glue_H_order": 512',
    '"actual_geometry_glue_existence_in_rep88_orbit_proved": False',
    '"actual_labeled_glue_subgroup_identified": False',
    '"actual_labeled_glue_generator_set_identified": False',
):
    assert exact in glue_text, exact
q = audit["exact_route_audit"]["index512_glue_route"]
assert q["actual_geometric_index512_overlattice_exists"] is True
assert q["actual_glue_order"] == 512
assert q["current_actual_labeled_glue_subgroup_identified"] is False
assert q["historical_rep88_orbit_claim_authoritative"] is False

# No diagnostic candidate is promoted by this audit.
fw = audit["promotion_firewall"]
assert fw["marked_adapter_materialized"] is False
assert fw["named_J2_proper_Br2_source_coordinate_materialized"] is False
assert fw["candidate_742_promoted"] is False and fw["candidate_736_promoted"] is False
assert fw["stage33_12_closed_exact"] is False and fw["stage33_13_released"] is False

print(json.dumps({
    "success": True,
    "status": audit["status"],
    "order4_current_route_replayable": False,
    "actual_index512_glue_exists": True,
    "actual_labeled_index512_glue_identified": False,
    "marked_adapter_materialized": False,
    "next_exact_leaf": audit["next_exact_leaf"],
    "certificate_sha256": audit["canonical_sha256"],
}, indent=2, sort_keys=True))
