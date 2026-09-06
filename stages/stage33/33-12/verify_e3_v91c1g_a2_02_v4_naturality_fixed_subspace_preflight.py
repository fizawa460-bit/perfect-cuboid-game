#!/usr/bin/env python3
"""Verify V91C1G A2_02 V4-naturality fixed-subspace preflight."""
from __future__ import annotations
import hashlib,json
from pathlib import Path

D=Path(__file__).resolve().parent
S33=D.parent
CAND=D/"e3-v91c1g-a2-02-v4-naturality-fixed-subspace-preflight.json"
V1D=D/"e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"
V1F=D/"e3-v91c1f-a2-02-source-bound-kummer-quotient-marking-obstruction.json"
BR=S33/"33-07"/"proper-brauer2-from-discriminant.json"
CAND_SHA="2a176993614fac6f4b1555855794642702f3eeb055d710b8f04ac5097e9fb370"
V1D_SHA="fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14"
V1F_SHA="4f6d18c35ce9cf8bb6efd2493ce66667bebf97870d731f06f17f76200932d273"
BR_SHA="c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"

def csha(o):
    return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p,h):
    o=json.loads(p.read_text(encoding="utf-8")); b=dict(o); q=b.pop("canonical_sha256")
    assert q==h==csha(b), p
    return o
def row_action(v,m):
    return [sum(v[i]*m[i][j] for i in range(len(v)))%2 for j in range(len(v))]

c=load(CAND,CAND_SHA); d=load(V1D,V1D_SHA); f=load(V1F,V1F_SHA); br=load(BR,BR_SHA)
p=d["purity_cartier"]; t=d["transition_selector"]
assert d["exact_consequence"]["a2_02_full_surface_cech_cartier_seed_assembly_materialized"] is True
assert d["a2_02_literal_seed"]["prime_level_cc_ct_transport_complete"] is True
ids=d["a2_02_literal_seed"]["component_ids"]
assert t["canonical_cc_map"]=={x:x for x in ids}
assert t["canonical_ct_map"]=={x:x for x in ids}
assert p["cartier_transition_unit"]=="ONE"
assert p["prime_level_package_difference_cc"]=="ZERO_EXACT_PRIME_LEVEL"
assert p["prime_level_package_difference_ct"]=="ZERO_EXACT_PRIME_LEVEL"
assert f["construction_result"]["a2_02_marked_brauer_image_computed"] is False
assert br["proper_geometric_Br2_dimension_f2"]==14
assert br["proper_Br2_joint_v4_fixed_dimension_f2"]==10
assert br["proper_Br2_fixed_dimensions"]["joint_v4"]==10
v=[0]*14
for i in (3,5): v[i-1]=1
assert row_action(v,br["proper_Br2_cc_action_f2"])==v
assert row_action(v,br["proper_Br2_ct_action_f2"])==v
q=c["proper14_fixed_subspace_test"]
assert q["joint_v4_fixed_dimension_f2"]==10 and q["joint_v4_fixed_cardinality"]==2**10
assert q["e3_target_mask_decimal"]==20 and q["e3_target_support_one_based"]==[3,5]
assert q["mask20_joint_v4_fixed"] is True
assert q["v4_naturality_uniquely_identifies_mask20"] is False
r=c["construction_result"]
assert r["v4_naturality_constraint_materialized"] is True
for k in ("source_specific_marked_brauer_coordinate_materialized","a2_02_marked_brauer_image_computed","a2_02_marked_brauer_image_equal_mask20","a2_02_claimed_e3_coefficient","source_bound_kummer_quotient_marking_materialized","e3_genuine_full_surface_h2_mu2_lift_materialized","e3_kummer_column_materialized","repository_wide_absence_claim","mathematical_nonexistence_claim"):
    assert r[k] is False
assert c["entry_authority"]["pr"]==1646
assert c["entry_authority"]["hostile_audit_review"]==5123592182
assert c["entry_authority"]["exact_audited_head"]=="5471181a4decdc319cf3f00080d85da6d6e9fbb0"
assert c["entry_authority"]["merge_commit"]=="749e06f82a3ffa1e9cb4e831760244e9237f34a4"
assert c["credit_firewall"]["stage33_progress"]=="6/11"
assert c["credit_firewall"]["merge_allowed"] is False
print(json.dumps({"success":True,"marker":"V91C1G_A2_02_V4_NATURALITY_FIXED_SUBSPACE_PREFLIGHT","candidate_sha256":CAND_SHA,"joint_fixed_dimension":10,"mask20_joint_fixed":True,"marked_image_computed":False},sort_keys=True))
