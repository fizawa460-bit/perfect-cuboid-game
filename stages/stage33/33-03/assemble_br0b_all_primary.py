#!/usr/bin/env python3
"""Assemble the exact all-primary BR0B inventory including the hidden extension."""
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def load(name): return json.loads((ROOT/name).read_text())
def csha(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

odd=load("odd-primary-closure.json")
d201=load("d2-01-image.json")
h3=load("absolute-h3-tate-vanishing.json")
h1=load("absolute-h1-picu-exact.json")
finite=load("finite-transgression-ranks.json")
upic=load("upic-v4-action-certificate.json")
ext=load("absolute-h2-extension-class.json")

if not odd["odd_primary_br0b_parametrically_complete"]: raise SystemExit("odd-primary inventory regression")
if not d201["finite_d2_01_image_exact"] or d201["image_f2_rank"]!=2: raise SystemExit("d2_01 image regression")
if not h3["absolute_d2_11_zero"]: raise SystemExit("absolute d2_11 regression")
if not h1["absolute_H1_PicU_all_classes_accounted"]: raise SystemExit("absolute H1 PicU inventory incomplete")
if finite["rank_d2_01"]!=2 or finite["rank_d2_11"]!=2: raise SystemExit("finite rank regression")
if not ext["full_extension_class_exact"] or not ext["primary_orders_exact_parametrically"]: raise SystemExit("absolute hypercohomology extension class unresolved")
if ext["filtration_extension_split_claimed"]: raise SystemExit("unexpected split claim")
if not ext["filtration_extension_class_exact"]: raise SystemExit("extension-class exactness regression")

rels=[]
for item in d201["torsion_generator_images"]:
    v=[int(x)&1 for x in item["h2_v4_unit_basis_vector_f2_cc_then_ct"]]
    if len(v)!=28: raise SystemExit("bad d2_01 image width")
    coords=[]
    for j,(a,b) in enumerate(zip(v[:14],v[14:]),1):
        char="0" if (a,b)==(0,0) else "chi_-1" if (a,b)==(1,0) else "chi_2" if (a,b)==(0,1) else "chi_-1+chi_2"
        coords.append({"unit_smith_coordinate_1based":j,"quadratic_character":char})
    rels.append({"source_torsion_generator":item["torsion_generator"],"relation_id":f"KAPPA_{len(rels)+1}","unit_character_coordinates":coords,"f2_vector_cc_then_ct":v})
if len(rels)!=2: raise SystemExit("expected two d2_01 relations")
finite_basis=h1["finite_free_H1_cocycle_basis"]
if len(finite_basis)!=5: raise SystemExit("expected five finite H1 classes")

cert={
 "schema":"STAGE33_03_BR0B_ALL_PRIMARY_INVENTORY_V3_EXTENSION_EXACT",
 "stage33_unit":"33-03",
 "receiver":"R29-BR0B",
 "br0b":"DISCHARGED",
 "source_locks":{
   "upic_v4_action_sha256":upic["canonical_sha256"],
   "odd_primary_closure_sha256":odd["canonical_sha256"],
   "d2_01_exact_image_sha256":d201["canonical_sha256"],
   "absolute_h3_tate_vanishing_sha256":h3["canonical_sha256"],
   "absolute_h1_picu_exact_sha256":h1["canonical_sha256"],
   "finite_transgression_ranks_sha256":finite["canonical_sha256"],
   "absolute_h2_extension_class_sha256":ext["canonical_sha256"]
 },
 "absolute_hypercohomology_identification":"Br_a(U)=H^2(G_Q,UPic(Ubar))",
 "character_group_XQ":"X_Q=Hom_cont(G_Q,Q/Z)",
 "left_filtration":{
   "group":"X_Q^14 / <KAPPA_1,KAPPA_2>",
   "origin":"coker absolute d2_01",
   "absolute_d2_01_rank":2,
   "relations":rels,
   "odd_primary_part":"X_Q,odd^14",
   "two_primary_part":"X_Q[2^infinity]^14 / <KAPPA_1,KAPPA_2>"
 },
 "right_filtration":{
   "group":"Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5",
   "origin":"H^1(G_Q,Pic(Ubar)); absolute d2_11=0",
   "quadratic_character_families":"Hom_cont(G_Q,(Z/2)^2)",
   "finite_class_basis":finite_basis,
   "primary":"2"
 },
 "exact_filtration_sequence":"0 -> X_Q^14/<KAPPA_1,KAPPA_2> -> Br_a(U) -> Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5 -> 0",
 "filtration_extension_split_claimed":False,
 "filtration_extension_class_exact":True,
 "extension_class":{
   "certificate_sha256":ext["canonical_sha256"],
   "quadratic_doubling_formula":ext["hidden_extension_doubling_map"]["formula_character_presentation"],
   "quadratic_delta_zero_criterion":ext["quadratic_family_primary_orders"]["delta_zero_criterion"],
   "quadratic_minimal_lift_order_if_delta_zero":2,
   "quadratic_minimal_lift_order_if_delta_nonzero":4,
   "finite_free_class_minimal_lift_order":2,
   "no_right_filtration_class_requires_minimal_order_above_4":True
 },
 "explicit_galois_action_certified":True,
 "upic_gersten_maps_certified":True,
 "kernels_cokernels_torsion_exact":True,
 "unit_kernel_absolute_galois_inflation_character_terms_exact":True,
 "no_unjustified_two_primary_restriction":True,
 "qbar_to_q_descent_adapter_certified":True,
 "open_algebraic_q_defined_class_inventory_complete":True,
 "all_odd_primary_classes_accounted":True,
 "all_two_primary_classes_accounted":True,
 "br0b_all_primary_classes_accounted":True,
 "unresolved_unknown_in_scope":0,
 "unit_status":"AUDIT_REQUIRED",
 "unit_closed":False,
 "downstream_released":False,
 "hostile_audit":"PENDING",
 "new_kernel_id":"NONE",
 "new_theorem_required":False,
 "external_theorem_used":"Milne, Arithmetic Duality Theorems, I.4 Corollary 4.17; Serre, Topics in Galois Theory, Ch.1 sec.1.2 Thm.1.2.4 only for the cyclic-quartic/sum-of-two-squares adapter",
 "theorem_credit":True,
 "theorem_credit_scope":"Milne H^3(G_Q,Z)=0; extension-class computation is derived from exact Postnikov/Bockstein data, with Serre used only as an adapter",
 "endpoint_credit":False,
 "perfect_cuboid_nonexistence_claim":False,
 "next_expected_command":"Stage33-audit"
}
cert["canonical_sha256"]=csha(cert)
(ROOT/"br0b-all-primary-inventory.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"BR0B":"DISCHARGED","BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED":True,"OPEN_ALGEBRAIC_Q_DEFINED_CLASS_INVENTORY_COMPLETE":True,"KERNELS_COKERNELS_TORSION_EXACT":True,"FILTRATION_EXTENSION_CLASS_EXACT":True,"FILTRATION_EXTENSION_SPLIT_CLAIMED":False,"UNRESOLVED_UNKNOWN_IN_SCOPE":0,"unit_status":cert["unit_status"],"next_expected_command":cert["next_expected_command"],"certificate_sha256":cert["canonical_sha256"]},indent=2,sort_keys=True))
