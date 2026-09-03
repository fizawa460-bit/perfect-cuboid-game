#!/usr/bin/env python3
"""V42: prove that the current J2 V25 lift cannot be relabelled as the V41 e3 source.

This is an interface obstruction only. It does not assert that an e3 H2(mu2)
lift does not exist; it fixes the exact missing interface needed to construct it.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
V41 = HERE / "e3-independent-proper14-source-v41.json"
V25 = HERE / "j2-genuine-h2-mu2-kummer-adapter-v25.json"
CECH = HERE / "j2-corrected-explicit-cech-mu2-lift.json"
OUT = HERE / "e3-v25-transfer-obstruction-v42.json"
LOCKS = {
    V41: "04c6ead2226c87defff085fc641ee80867e1fdf4b07baa28c5e97d2c5e534ac6",
    V25: "d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c",
    CECH: "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b",
    OUT: "b51985a55899c693513959074fa08171b7537d1793fb1372b9dc54facf8f675e",
}

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def locked(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256")
    assert claimed == LOCKS[path] == csha(body), path
    return obj

v41 = locked(V41); v25 = locked(V25); cech = locked(CECH); out = locked(OUT)
e3 = v41["e3_source"]
j2 = v25["current_named_source"]
assert e3["retained10_standard_mask_decimal"] == 4
assert e3["proper14_mask_decimal"] == 20
assert j2["retained10_mask_decimal"] == 6
assert j2["proper14_mask_decimal"] == 25
assert e3["retained10_standard_mask_decimal"] != j2["retained10_mask_decimal"]
assert e3["proper14_mask_decimal"] != j2["proper14_mask_decimal"]
assert v25["genuine_h2_mu2_adapter"]["kc_lift_brauer_image"] == "corrected J2=(f2,1)"
assert "J2=(f2,1)" in cech["surface_mu2_lift"]["brauer_image"]
assert cech["surface_mu2_lift"]["genuine_surface_H2_mu2_lift_materialized"] is True
assert v41["construction_boundary"]["explicit_geometric_or_cech_representative_for_e3_materialized"] is False
assert out["construction_result"]["v25_adapter_relabelled_as_e3"] is False
assert out["construction_result"]["v25_adapter_proves_e3_h2_mu2_lift"] is False
assert out["construction_result"]["genuine_full_surface_h2_mu2_lift_for_e3_materialized"] is False
assert out["anti_inference"]["absence_of_current_interface_promoted_to_nonexistence"] is False
print(json.dumps({"success": True, "v41_e3": [4,20], "v25_j2": [6,25], "v25_relabel_blocked": True, "e3_h2_mu2_lift_materialized": False, "next_exact_leaf": out["next_exact_leaf"], "marker": "PROOF_REPLAY_COMPLETE"}, sort_keys=True))
