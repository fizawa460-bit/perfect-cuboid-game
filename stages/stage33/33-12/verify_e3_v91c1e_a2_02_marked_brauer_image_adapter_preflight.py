#!/usr/bin/env python3
"""Verify the bounded V91C1E type-safe marked-Brauer image adapter preflight."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
D=Path(__file__).resolve().parent; S33=D.parent; S07=S33/"33-07"
CERT=D/"e3-v91c1e-a2-02-marked-brauer-image-adapter-preflight.json"
V1D=D/"e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"; IFACE=D/"e3-v91c-type-safe-cech-adapter-interface.json"; KUM=D/"full-surface-pic2-kummer-target.json"; ADJ=D/"j2-picard-adjoint-proper-br2.json"; PROPER=S07/"proper-brauer2-from-discriminant.json"; V91=D/"e3-retained-at-marked-picard-dual-source-v91.json"
LOCKS={CERT:"5dfbdf3dcd00f769d5550125cf7ca004ce4bf12aed5d3707cf9ddfc8dc292a4f",V1D:"fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14",IFACE:"da156e8fcbd59743073b5a3d8ba5359c533b0b045adddc41877310974cdc1754",KUM:"384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890",ADJ:"066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8",PROPER:"c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",V91:"729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9"}
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p):
 o=json.loads(p.read_text(encoding="utf-8")); b=dict(o); h=b.pop("canonical_sha256"); assert h==LOCKS[p]==csha(b),p; return o
c,d,i,k,a,p,v=map(load,(CERT,V1D,IFACE,KUM,ADJ,PROPER,V91))
assert d["exact_consequence"]["a2_02_full_surface_cech_cartier_seed_assembly_materialized"] is True and d["exact_consequence"]["a2_02_marked_brauer_image_computed"] is False
assert k["exact_information_boundary"]["kummer_extension_class_missing"] is True and k["exact_information_boundary"]["picard_action_missing"] is False and k["exact_information_boundary"]["proper_invariant_basis_missing"] is False
assert k["kummer_defect_map_contract"]["columns_materialized"]==0
assert len(a["degree2_picard_adjoint"]["decoded_target_basis_columns"])==14
assert c["exact_positive_inventory"]["e3_target_proper14_mask_decimal"]==20 and c["exact_positive_inventory"]["e3_target_proper14_support_one_based"]==[3,5]
t=c["type_safe_adapter_audit"]; assert t["full_surface_kummer_extension_class_missing"] is True and t["full_surface_kummer_defect_columns_materialized"]==0 and t["literal_h2_seed_to_marked_proper14_quotient_map_materialized_by_locked_assets"] is False and t["source_bound_marking_of_this_literal_a2_02_seed_into_marked_proper14_materialized"] is False and t["picard_adjoint_may_substitute_for_missing_literal_h2_to_br_marking"] is False and t["positional_a2_to_proper14_identification_allowed"] is False and t["retired_14x14_p_w_used"] is False
x=c["exact_consequence"]; assert x["a2_02_marked_brauer_image_computed"] is False and x["a2_02_marked_brauer_image_equal_mask20"] is False and x["genuine_full_surface_h2_mu2_lift_for_e3"] is False and x["repository_wide_absence_claim"] is False and x["mathematical_nonexistence_claim"] is False
assert c["credit_firewall"]["stage33_progress"]=="6/11" and c["credit_firewall"]["merge_allowed"] is False
print(json.dumps({"success":True,"marker":"V91C1E_A2_02_MARKED_BRAUER_IMAGE_ADAPTER_PREFLIGHT_EXACT","certificate_sha256":LOCKS[CERT],"marked_brauer_image_computed":False,"next_exact_leaf":c["next_exact_leaf"]},sort_keys=True))
