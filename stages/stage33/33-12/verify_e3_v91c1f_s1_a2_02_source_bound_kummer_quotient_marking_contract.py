#!/usr/bin/env python3
"""V91C1F-S1: lock the V25 source-coordinate method witness and the exact A2_02 gap."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent
CERT=H/"e3-v91c1f-s1-a2-02-source-bound-kummer-quotient-marking-contract.json"
V1E=H/"e3-v91c1e-a2-02-marked-brauer-image-adapter-preflight.json"
V1D=H/"e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"
VC=H/"e3-v91c-type-safe-cech-adapter-interface.json"
V91=H/"e3-retained-at-marked-picard-dual-source-v91.json"
V25=H/"j2-genuine-h2-mu2-kummer-adapter-v25.json"
CECH=H/"j2-corrected-explicit-cech-mu2-lift.json"
LOCKS={CERT:"3f9bee9108bbf93b304c6d0fdae4235717c3fe919647c882fcc4ef5e822d3c93",V1E:"5dfbdf3dcd00f769d5550125cf7ca004ce4bf12aed5d3707cf9ddfc8dc292a4f",V1D:"fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14",VC:"da156e8fcbd59743073b5a3d8ba5359c533b0b045adddc41877310974cdc1754",V91:"729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9",V25:"d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c",CECH:"6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b"}
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p):
 o=json.loads(p.read_text(encoding="utf-8")); b=dict(o); q=b.pop("canonical_sha256"); assert q==LOCKS[p]==csha(b),p; return o
d=load(CERT); e=load(V1E); a=load(V1D); c=load(VC); v=load(V91); j=load(V25); z=load(CECH)
assert e["next_exact_leaf"]=="V91C1F_MATERIALIZE_SOURCE_BOUND_KUMMER_QUOTIENT_MARKING_FROM_LITERAL_A2_02_CECH_SEED_TO_MARKED_PROPER14"
assert a["exact_consequence"]["a2_02_full_surface_cech_cartier_seed_assembly_materialized"] is True
assert a["exact_consequence"]["a2_02_marked_brauer_image_computed"] is False
assert c["type_firewall"]["positional_or_dimension_identification_allowed"] is False
assert v["e3_source_binding"]["retained_at_mod2_quotient_support_one_based"]==[1,8,10]
assert j["current_named_source"]["source_coordinate_materialized"] is True
assert j["genuine_h2_mu2_adapter"]["named_source_and_cech_lift_identified_by_same_marked_brauer_coordinate"] is True
assert j["current_named_source"]["proper14_mask_decimal"]==25
assert z["explicit_cech_preimage"]["concrete_Cech_preimage_e_D_materialized"] is True
assert z["surface_mu2_lift"]["genuine_surface_H2_mu2_lift_materialized"] is True
assert d["entry_authority"]["hostile_audit_review"]==5123392163
assert d["entry_authority"]["merge_commit"]=="dbcff26c0267416caa4fdd0515293396d0f86887"
w=d["required_source_bound_marking_witness"]
assert w["materialized"] is False and w["positional_or_dimension_identification_allowed"] is False
assert w["picard_adjoint_substitution_allowed"] is False and w["j2_coordinate_relabel_allowed"] is False
x=d["exact_consequence"]
assert x["v25_success_condition_reduced_to_source_coordinate_identity_witness"] is True
assert x["a2_02_marked_brauer_image_computed"] is False and x["a2_02_marked_brauer_image_equal_mask20"] is False
assert x["repository_wide_absence_claim"] is False and x["mathematical_nonexistence_claim"] is False
assert d["credit_firewall"]["stage33_progress"]=="6/11" and d["credit_firewall"]["merge_allowed"] is False
print(json.dumps({"success":True,"marker":"V91C1F_S1_SOURCE_BOUND_MARKING_WITNESS_CONTRACT","certificate_sha256":LOCKS[CERT],"next_exact_leaf":d["next_exact_leaf"]},sort_keys=True))
