#!/usr/bin/env python3
"""Verify V87: legacy Stage33-11 Gersten machinery is not yet a source-bound e3 mask20 preimage."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CERT = HERE / "e3-legacy-gersten-mask20-source-binding-gap-v87.json"
EXPECTED = "c7daf46a4e05d4692f1065e8ed677d5be9a172126952e93207a26d5b2c839447"


def csha(obj):
    body=dict(obj); body.pop("canonical_sha256",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def blob_sha(path):
    raw=path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode()+raw).hexdigest()

x=json.loads(CERT.read_text(encoding="utf-8"))
assert x["canonical_sha256"]==EXPECTED==csha(x)
for lock in x["source_locks"].values():
    p=ROOT/lock["path"]
    assert p.exists(), p
    assert blob_sha(p)==lock["git_blob_sha1"], (p,blob_sha(p),lock["git_blob_sha1"])

v47=json.loads((HERE/"e3-proper14-boundary-bridge-construction-contract-v47.json").read_text())
audit=json.loads((ROOT/"stages/stage33/33-11/audit-state.json").read_text())
v85=json.loads((HERE/"e3-coordinate-conjugate-sign-quotient-route-freeze-v85.json").read_text())

assert v47["bridge"]["matrix_shape"]==[14,14]
assert v47["bridge"]["materialized"] is False
assert v47["bridge"]["usable_for_e3"] is False
assert sum(r["status"]=="UNMATERIALIZED" for r in v47["required_columns"])==14
assert v47["e3_target_after_bridge_only"]["proper14_mask_decimal"]==20
assert v47["e3_target_after_bridge_only"]["mapping_executed"] is False

assert audit["verdict"]=="FAIL_REPAIR_REQUIRED"
assert audit["exact_progress_after_audit"]=="0/26"
assert audit["rejected_as_exact_evidence"]["working_zero_map_coverage"]=="26/26"
assert audit["rejected_as_exact_evidence"]["mathematical_nonzero_claim"] is False
assert audit["firewalls"]["stage33_11_closed_exact"] is False

assert v85["sign_quotient_consequence"]["e3_target_mask_decimal"]==20
assert v85["exact_boundary"]["global_H2_mu2_nonexistence_claim"] is False

s=x["exact_legacy_pipeline_status"]
assert s["exact_connecting_columns_certified"]==0
assert s["strict_transform_prime_refinement_complete"] is False
assert s["working_26_of_26_zero_map_rejected_as_exact_evidence"] is True
b=x["exact_mask20_binding_status"]
assert b["e3_proper14_mask_decimal"]==20
assert b["P_W_materialized"] is False
assert b["P_W_materialized_columns"]==0
assert b["legacy_A2_to_proper14_mask20_source_binding_materialized"] is False
assert b["legacy_stage33_11_actual_gersten_representative_with_brauer_image_mask20_materialized"] is False
c=x["exact_conclusion"]
assert c["legacy_stage33_11_pipeline_is_currently_usable_as_e3_mask20_preimage"] is False
assert c["route_local_only"] is True
assert c["repository_wide_absence_claim"] is False
assert c["mathematical_nonexistence_claim"] is False
assert c["global_H2_mu2_nonexistence_claim"] is False
assert c["new_noncoordinate_cech_or_actual_gersten_construction_still_open"] is True
assert x["credit_firewall"]["stage33_progress"]=="6/11"
assert x["credit_firewall"]["stage33_12_closed_exact"] is False
assert x["credit_firewall"]["stage33_13_released"] is False
assert x["credit_firewall"]["merge_allowed"] is False

print(json.dumps({
 "success":True,
 "marker":"V87_LEGACY_GERSTEN_MASK20_SOURCE_BINDING_GAP_COMPLETE",
 "canonical_sha256":EXPECTED,
 "legacy_exact_connecting_columns":"0/26",
 "P_W_materialized_columns":"0/14",
 "e3_target_mask":20,
 "legacy_pipeline_currently_usable_for_e3_mask20":False,
 "global_H2_mu2_nonexistence_claim":False,
 "next_exact_leaf":x["next_exact_leaf"],
 "merge_allowed":False
},sort_keys=True))
