#!/usr/bin/env python3
"""Certify Stage33-09 Picard-equivariant transport from retained source evidence."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "marked-picard-basis-source.json"
BRIDGE = HERE / "marked-picard-basis-bridge-certified.json"
OUT = HERE / "stage33-09-closure.json"
SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
NAMES = ["cc", "ct", "a1", "a2", "a3", "b1", "b2", "b3", "c"]


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path) -> dict:
    x = json.loads(path.read_text(encoding="utf-8"))
    body = dict(x)
    claimed = body.pop("canonical_sha256", None)
    if claimed != csha(body):
        raise SystemExit(f"canonical hash regression: {path.name}")
    return x


src = load_locked(SOURCE)
cert = load_locked(BRIDGE)
if src["schema"] != "STAGE33_07_INDLIST_TO_MAGMA_PICARD_BASIS_V1":
    raise SystemExit("marked source bridge schema moved")
if cert["schema"] != "STAGE33_07_MARKED_PICARD_BASIS_BRIDGE_CERTIFIED_V1":
    raise SystemExit("marked certified bridge schema moved")
if src["source"]["git_blob_sha1"] != SOURCE_BLOB:
    raise SystemExit("upstream source blob moved")
if cert["source_locks"]["upstream_git_blob_sha1"] != SOURCE_BLOB:
    raise SystemExit("certified bridge upstream source blob moved")
if cert["source_locks"]["marked_bridge_certificate_sha256"] != src["canonical_sha256"]:
    raise SystemExit("certified bridge does not consume the retained marked source bridge")

b = cert["basis_bridge"]
if b["from"] != "upstream primitive INDLIST known-class basis":
    raise SystemExit("marked basis source moved")
if b["to"] != "historical retained Magma Basis(Pic)":
    raise SystemExit("historical retained target basis moved")
if abs(int(b["determinant"])) != 1 or not b["full_gram_transport_exact"]:
    raise SystemExit("marked bridge is not an exact unimodular Gram transport")
if b["named_action_intertwining_verified"] != NAMES:
    raise SystemExit("named integral action coverage moved")

s = cert["actual_coordinate_swaps_in_historical_magma_picard_basis"]
if not all([
    s["both_integral_unimodular_gram_isometries"],
    s["both_involutions"],
    s["s3_braid_exact"],
    s["commute_with_cc_ct"],
    s["seven_sign_conjugations_exact"],
]):
    raise SystemExit("actual swap transport is incomplete")

e = cert["exact_consequence"]
if not e["historical_retained_picard_basis_now_marked_by_actual_140_class_geometry"]:
    raise SystemExit("historical retained Picard marking is not certified")
if not e["actual_integral_swaps_now_available_in_historical_q256_picard_basis"]:
    raise SystemExit("actual integral swaps are not available in retained q256 Picard basis")
if int(e["connecting_matrix_columns_explicitly_materialized"]) != 0:
    raise SystemExit("Stage33-09 must not claim connecting-map columns")
if e["middle_gersten_module_action_materialized"] or e["absolute_delta_loc_computed"] or e["arithmetic_hs_closed"]:
    raise SystemExit("Stage33-09 downstream firewall violated")
if cert["stage33_progress"] != "6/11" or cert["stage33_08_released"] or cert["theorem_credit"] or cert["endpoint_credit"]:
    raise SystemExit("Stage33-09 inherited firewall moved")

out = {
    "schema": "STAGE33_09_PICARD_EQUIVARIANT_TRANSPORT_CLOSURE_V1",
    "parent_big_task": "33-07",
    "source_locks": {
        "upstream_git_blob_sha1": SOURCE_BLOB,
        "marked_picard_source_sha256": src["canonical_sha256"],
        "marked_picard_bridge_certificate_sha256": cert["canonical_sha256"],
        "retained_old_picard_base_sha256": cert["source_locks"]["retained_old_picard_base_sha256"],
        "retained_old_picard_signs_sha256": cert["source_locks"]["retained_old_picard_signs_sha256"],
        "current_stage32_marking_bundle_sha256": cert["source_locks"]["current_stage32_marking_bundle_sha256"],
        "actual_galois_at2_certificate_sha256": cert["source_locks"]["actual_galois_at2_certificate_sha256"],
    },
    "exit_condition": {
        "HISTORICAL_RETAINED_PICARD_MARKING_BRIDGE_CERTIFIED": True,
        "NAMED_INTEGRAL_AND_TWO_TORSION_ACTIONS_SOURCE_LOCKED": True,
        "PICARD_EQUIVARIANT_TRANSPORT_CLOSED": True,
    },
    "named_integral_action_coverage": NAMES + ["swap12", "swap13"],
    "historical_q256_basis_marking_exact": True,
    "stage33_10_released": True,
    "stage33_progress": "6/11",
    "stage33_07_closed": False,
    "stage33_08_released": False,
    "connecting_matrix_columns_explicitly_materialized": 0,
    "absolute_h1_receiver_exact": False,
    "arithmetic_localization_connecting_map_computed": False,
    "arithmetic_hs_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "next_item": "Stage33-10_ABSOLUTE_H1_AND_GALOIS_DESCENT_ADAPTER",
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("STAGE33_09_PICARD_EQUIVARIANT_TRANSPORT=PASS_EXACT")
print("CERTIFICATE_SHA256=" + out["canonical_sha256"])
print("NEXT=" + out["next_item"])
