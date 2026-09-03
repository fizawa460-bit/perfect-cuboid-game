#!/usr/bin/env python3
"""Network-free hostile replay for Stage33 V45 A1.0 basis-definition lock."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
STAGE33=HERE.parent
CERT=HERE/"e3-proper14-boundary-basis-definitions-v45.json"
PROPER=STAGE33/"33-07"/"proper-brauer2-from-discriminant.json"
BOUNDARY=HERE/"boundary-function-generator-source-lock.json"
V41=HERE/"e3-independent-proper14-source-v41.json"
V44=HERE/"e3-proper14-boundary-basis-bridge-gap-v44.json"

EXPECTED_CERT="a1dafa0be79c80d7275cd2629278bf6a56d6e592f90738316e71ca2689f9feb5"
EXPECTED_PROPER="c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
EXPECTED_BOUNDARY="aaacc000f2e5fbbe733789f5f2a19d6c2cb14b5d3a26d0b8e508eea1f3bc8c96"
EXPECTED_V41="04c6ead2226c87defff085fc641ee80867e1fdf4b07baa28c5e97d2c5e534ac6"
EXPECTED_V44="81368384bfa77ebe37a27e7eb2f16b7244810fe998e1c47db00f31751f2f5445"
BOUNDARY_ORDER=["A2_02","A2_03","A2_24","A2_25","A2_26","A2_04","A2_01","A2_07","A2_05","A2_10","A2_08","A2_09","A2_16","A2_15"]

def csha(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def checked(path, expected):
    obj=json.loads(path.read_text(encoding="utf-8"))
    body=dict(obj)
    claimed=body.pop("canonical_sha256")
    assert claimed==expected==csha(body), (path,claimed,csha(body))
    return obj

cert=checked(CERT,EXPECTED_CERT)
proper=checked(PROPER,EXPECTED_PROPER)
boundary=checked(BOUNDARY,EXPECTED_BOUNDARY)
v41=checked(V41,EXPECTED_V41)
v44=checked(V44,EXPECTED_V44)

assert cert["schema"]=="STAGE33_12_E3_PROPER14_BOUNDARY_BASIS_DEFINITIONS_V45"
assert cert["micro_goal"]=="A1.0_LOCK_BOTH_14D_BASIS_DEFINITIONS"
assert cert["status"]=="PASS_EXACT_A1_0_BASIS_DEFINITIONS_LOCKED_WITHOUT_IDENTIFICATION"

pb=cert["proper14_basis"]
assert pb["dimension_f2"]==14
assert proper["proper_geometric_Br2_dimension_f2"]==14
for key in ("proper_Br2_cc_action_f2","proper_Br2_ct_action_f2"):
    M=proper[key]
    assert len(M)==14 and all(len(row)==14 for row in M)
axes=pb["ordered_axes"]
assert len(axes)==14
for i,rec in enumerate(axes):
    expect=[0]*14
    expect[i]=1
    assert rec["axis_index_one_based"]==i+1
    assert rec["label"]==f"proper14_axis_{i+1:02d}"
    assert rec["coordinate_f2"]==expect

bb=cert["boundary_function_basis"]
assert bb["dimension_f2"]==14
assert bb["ordered_source_directions"]==BOUNDARY_ORDER
assert boundary["stage33_11_working_generators"]==BOUNDARY_ORDER
assert [r["source_direction"] for r in boundary["generator_records"]]==BOUNDARY_ORDER

e3=cert["e3_context"]
assert e3["proper14_mask_decimal"]==20
assert e3["proper14_support_one_based"]==[3,5]
assert e3["boundary_source_coordinate_materialized"] is False
assert v41["e3_source"]["proper14_mask_decimal"]==20
assert v41["e3_source"]["proper14_coordinate_f2"]==[0,0,1,0,1,0,0,0,0,0,0,0,0,0]

lock=cert["non_identification_lock"]
assert all(lock[k] is False for k in (
    "proper14_order_identified_with_boundary_order",
    "positional_identification_allowed",
    "proper14_to_boundary_change_of_basis_materialized",
    "proper14_axis_3_assumed_to_be_boundary_coordinate_3",
    "proper14_axis_5_assumed_to_be_boundary_coordinate_5",
))
assert v44["missing_exact_bridge"]["materialized_in_reviewed_authority"] is False
assert cert["next_exact_leaf"]=="A1.1_CONSTRUCT_OR_CERTIFY_EXACT_14X14_F2_PROPER14_TO_A2_BOUNDARY_CHANGE_OF_BASIS_BRIDGE"

fire=cert["promotion_firewall"]
assert fire["e3_boundary_function_representative_materialized"] is False
assert fire["e3_cech_h2_mu2_lift_materialized"] is False
assert fire["e3_kummer_column_materialized"] is False
assert fire["stage33_12_closed_exact"] is False
assert fire["stage33_13_released"] is False
assert fire["merge_allowed"] is False
assert fire["theorem_credit"] is False
assert fire["endpoint_credit"] is False

print("PROOF_REPLAY_COMPLETE")
