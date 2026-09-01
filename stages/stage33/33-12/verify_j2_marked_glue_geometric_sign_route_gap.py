#!/usr/bin/env python3
"""Verify the Stage33-12 safe geometric-sign route boundary for the marked Br2 adapter."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEGACY = HERE.parent / "33-07"
CERT = HERE / "j2-marked-glue-geometric-sign-route-gap.json"
ROUTE = HERE / "j2-marked-adapter-source-route-audit.json"
ACTUAL_GLUE = LEGACY / "certify_index512_actual_geometry_glue_adapter.py"
ELEMENTARY = LEGACY / "aggregate_elementary_index512_q256_geometric_sign_split.py"
K1 = LEGACY / "nonelementary-k1-geometric-sign-fixed-p7-rescue128-census.json"
K2 = LEGACY / "nonelementary-k2-geometric-sign-fixed-census.json"

CERT_SHA = "23b6fc3e9cf666e81f0c11c4c57c7070a1cc4c459c35515a6d934db3a84f3ee9"
ROUTE_SHA = "5fec609e3ee75fddc3833124dde81f75514de6ca8600200e594366e30022f3f8"
K1_SHA = "7ac64a76b8132e044b145d009e331476f55e04a78001a127bce6fe3034c206fa"
K2_SHA = "44390c7bd74b8be73f74ccc305e1b4229a73433b20f1ce9f1d02a63e0526558b"
ACTUAL_GLUE_BLOB = "d0917a48d15ea3ff4bd6dd4144d2acced0b27c2a"
ELEMENTARY_BLOB = "e8436e09483605f4fc6c082636292fce557cdfbc"


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


cert = locked(CERT, CERT_SHA)
route = locked(ROUTE, ROUTE_SHA)
k1 = locked(K1, K1_SHA)
k2 = locked(K2, K2_SHA)

assert cert["schema"] == "STAGE33_12_J2_MARKED_GLUE_GEOMETRIC_SIGN_ROUTE_GAP_V1"
assert cert["status"] == "PASS_EXACT_GEOMETRIC_SIGN_ROUTE_BOUNDARY_NO_PROMOTION"
assert route["exact_route_audit"]["index512_glue_route"]["actual_geometric_index512_overlattice_exists"] is True
assert route["exact_route_audit"]["index512_glue_route"]["actual_glue_order"] == 512
assert route["exact_route_audit"]["index512_glue_route"]["current_actual_labeled_glue_subgroup_identified"] is False
assert route["exact_route_audit"]["index512_glue_route"]["current_actual_labeled_glue_generator_set_identified"] is False

assert git_blob(ACTUAL_GLUE) == ACTUAL_GLUE_BLOB
glue_text = ACTUAL_GLUE.read_text(encoding="utf-8")
assert '"actual_glue_H_exists_as_T_over_L0": True' in glue_text
assert '"actual_glue_H_order": 512' in glue_text
assert '"actual_labeled_glue_subgroup_identified": False' in glue_text
assert '"actual_labeled_glue_generator_set_identified": False' in glue_text

assert git_blob(ELEMENTARY) == ELEMENTARY_BLOB
elementary_text = ELEMENTARY.read_text(encoding="utf-8")
assert "'arithmetic_cc_ct_used':False" in elementary_text
assert "'geometric_coordinate_signs_used':7" in elementary_text
assert "'actual_index512_glue_identified':False" in elementary_text
assert "this census does not identify T(S)/L0" in elementary_text

assert k1["geometric_coordinate_sign_family_enforced"] == 7
assert k1["arithmetic_generators_used"] == []
assert k1["k1_nonelementary_type_rejected"] is True
assert k1["weighted_H_checked"] == 1311205952
assert k1["weighted_H_survivors"] == 0
assert k1["actual_index512_glue_identified"] is False

assert k2["geometric_coordinate_signs_used"] == 7
assert k2["arithmetic_generators_used"] == []
assert k2["k2_nonelementary_type_rejected"] is True
assert k2["weighted_H_checked"] == 129468416
assert k2["weighted_H_survivors"] == 0
assert k2["actual_index512_glue_identified"] is False

f = cert["exact_findings"]
assert f["actual_geometric_index512_glue_exists"] is True
assert f["actual_glue_order"] == 512
assert f["actual_labeled_glue_subgroup_identified"] is False
assert f["actual_labeled_glue_generator_set_identified"] is False
assert f["seven_geometric_coordinate_sign_involutions_are_safe_inputs"] is True
assert f["arithmetic_cc_ct_promoted_as_integral_geometry"] is False

fw = cert["promotion_firewall"]
assert fw["marked_adapter_materialized"] is False
assert fw["named_J2_proper_Br2_source_coordinate_materialized"] is False
assert fw["candidate_742_promoted"] is False
assert fw["candidate_736_promoted"] is False
assert fw["historical_mask_6_restored"] is False
assert fw["stage33_12_closed_exact"] is False
assert fw["stage33_13_released"] is False

print(json.dumps({
    "success": True,
    "status": cert["status"],
    "actual_index512_glue_exists": True,
    "actual_labeled_index512_glue_identified": False,
    "k1_survivors": k1["weighted_H_survivors"],
    "k2_survivors": k2["weighted_H_survivors"],
    "marked_adapter_materialized": False,
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
