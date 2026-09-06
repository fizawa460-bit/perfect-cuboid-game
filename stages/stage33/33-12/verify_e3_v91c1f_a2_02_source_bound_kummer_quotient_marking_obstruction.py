#!/usr/bin/env python3
"""Verify V91C1F exact type/provenance obstruction for the A2_02 source-bound Kummer quotient marking."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent
OUT=H/"e3-v91c1f-a2-02-source-bound-kummer-quotient-marking-obstruction.json"
LOCKS={
 "v91c1d":(H/"e3-v91c1d-a2-02-purity-cech-cartier-assembly.json","fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14"),
 "v91c1e":(H/"e3-v91c1e-a2-02-marked-brauer-image-adapter-preflight.json","5dfbdf3dcd00f769d5550125cf7ca004ce4bf12aed5d3707cf9ddfc8dc292a4f"),
 "v91c":(H/"e3-v91c-type-safe-cech-adapter-interface.json","da156e8fcbd59743073b5a3d8ba5359c533b0b045adddc41877310974cdc1754"),
 "v41":(H/"e3-independent-proper14-source-v41.json","04c6ead2226c87defff085fc641ee80867e1fdf4b07baa28c5e97d2c5e534ac6"),
 "v25":(H/"j2-genuine-h2-mu2-kummer-adapter-v25.json","d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"),
 "j2cech":(H/"j2-corrected-explicit-cech-mu2-lift.json","6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b"),
 "j2contract":(H/"j2-full-surface-mu2-zero-defect-contract.json","55cd01cc8570cb759e7029ddef3b9dac764625a7cdd313c76fd694e37fd478ce"),
}
OUT_SHA="4f6d18c35ce9cf8bb6efd2493ce66667bebf97870d731f06f17f76200932d273"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def locked(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop("canonical_sha256"); assert q==h==csha(b),p; return o
d={k:locked(*v) for k,v in LOCKS.items()}
c=locked(OUT,OUT_SHA)
v1d=d["v91c1d"]; v1e=d["v91c1e"]; v91c=d["v91c"]; v41=d["v41"]; v25=d["v25"]; j2=d["j2cech"]; jc=d["j2contract"]
assert v1d["exact_consequence"]["a2_02_full_surface_cech_cartier_seed_assembly_materialized"] is True
assert v1d["exact_consequence"]["a2_02_marked_brauer_image_computed"] is False
assert v1e["type_safe_adapter_audit"]["literal_h2_seed_to_marked_proper14_quotient_map_materialized_by_locked_assets"] is False
assert v1e["type_safe_adapter_audit"]["full_surface_kummer_extension_class_missing"] is True
assert v91c["type_firewall"]["direct_boundary_source_to_K_basis_identification_allowed"] is False
assert v91c["adapter_definition"]["proper14_mask_decimal"]==20 and v91c["adapter_definition"]["materialized"] is False
assert v41["e3_source"]["proper14_mask_decimal"]==20 and v41["e3_source"]["source_coordinate_materialized"] is True
assert v25["current_named_source"]["proper14_mask_decimal"]==25 and v25["current_named_source"]["marked_brauer_coordinate_f2"]==[1,0]
assert v25["genuine_h2_mu2_adapter"]["named_source_and_cech_lift_identified_by_same_marked_brauer_coordinate"] is True
assert v25["genuine_h2_mu2_adapter"]["full_surface_lift"]=="pull back lambda_D along the exact V21 projection forget c"
assert "J2=(f2,1)" in j2["surface_mu2_lift"]["brauer_image"] and j2["explicit_cech_preimage"]["maps_to_corrected_branch_class"] is True
assert jc["exact_input"]["marked_brauer_coordinate"]==[1,0] and "J2=(f2,1)" in jc["exact_input"]["class"]
assert jc["kummer_exact_sequence"]["sequence"]=="Pic(Kc_bar)/2 -> H^2_et(Kc_bar,mu_2) -> Br(Kc_bar)[2] -> 0"
assert c["v25_method_decomposition"]["v25_is_source_independent_coordinate_map"] is False
assert c["v25_method_decomposition"]["v25_is_named_j2_source_composition_adapter"] is True
assert c["a2_02_source_inventory"]["source_specific_marked_brauer_coordinate_materialized"] is False
assert c["type_provenance_obstruction"]["abstract_quotient_arrow_is_not_a_marked_coordinate_computation"] is True
assert c["type_provenance_obstruction"]["target_side_picard_adjoint_supplies_missing_datum"] is False
r=c["construction_result"]
assert r["generic_v25_method_applicable_as_checklist"] is True and r["v25_direct_adapter_reuse_for_a2_02"] is False
assert r["source_bound_kummer_quotient_marking_materialized"] is False and r["a2_02_marked_brauer_image_computed"] is False
assert r["a2_02_marked_brauer_image_equal_mask20"] is False and r["a2_02_claimed_e3_coefficient"] is False and r["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
assert r["repository_wide_absence_claim"] is False and r["mathematical_nonexistence_claim"] is False and r["exact_obstruction_materialized"] is True
assert c["next_exact_leaf"]=="V91C1G_CONSTRUCT_SOURCE_SPECIFIC_A2_02_BRAUER_IMAGE_WITNESS_OR_GEOMETRIC_QUOTIENT_ADAPTER_THEN_TEST_MASK20" and c["credit_firewall"]["stage33_progress"]=="6/11" and c["credit_firewall"]["merge_allowed"] is False
print(json.dumps({"success":True,"marker":"V91C1F_EXACT_TYPE_PROVENANCE_OBSTRUCTION","canonical_sha256":OUT_SHA,"v25_direct_reuse":False,"source_bound_marking_materialized":False,"next_exact_leaf":c["next_exact_leaf"]},sort_keys=True))
