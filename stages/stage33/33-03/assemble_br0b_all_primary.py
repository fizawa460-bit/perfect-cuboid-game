#!/usr/bin/env python3
"""Assemble the exact all-primary BR0B filtration and audit handoff."""
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
odd=json.loads((ROOT/"odd-primary-closure.json").read_text())
d201=json.loads((ROOT/"d2-01-image.json").read_text())
h3=json.loads((ROOT/"absolute-h3-tate-vanishing.json").read_text())
h1=json.loads((ROOT/"absolute-h1-picu-exact.json").read_text())
finite=json.loads((ROOT/"finite-transgression-ranks.json").read_text())

if not odd["odd_primary_br0b_parametrically_complete"]: raise SystemExit("odd-primary inventory regression")
if not d201["finite_d2_01_image_exact"] or d201["image_f2_rank"]!=2: raise SystemExit("d2_01 image regression")
if not h3["absolute_d2_11_zero"]: raise SystemExit("absolute d2_11 regression")
if not h1["absolute_H1_PicU_all_classes_accounted"]: raise SystemExit("absolute H1 PicU inventory incomplete")
if finite["rank_d2_01"]!=2 or finite["rank_d2_11"]!=2: raise SystemExit("finite rank regression")

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
 "schema":"STAGE33_03_BR0B_ALL_PRIMARY_INVENTORY_V1",
 "stage33_unit":"33-03","receiver":"R29-BR0B","br0b":"DISCHARGED",
 "source_locks":{"odd_primary_closure_sha256":odd["canonical_sha256"],"d2_01_exact_image_sha256":d201["canonical_sha256"],"absolute_h3_tate_vanishing_sha256":h3["canonical_sha256"],"absolute_h1_picu_exact_sha256":h1["canonical_sha256"],"finite_transgression_ranks_sha256":finite["canonical_sha256"]},
 "absolute_hypercohomology_identification":"Br_a(U)=H^2(G_Q,UPic(Ubar))",
 "character_group_XQ":"X_Q=Hom_cont(G_Q,Q/Z)",
 "left_filtration":{"group":"X_Q^14 / <KAPPA_1,KAPPA_2>","origin":"coker(d2_01:Pic(Ubar)^G_Q -> H^2(G_Q,U_D))","absolute_d2_01_rank":2,"relations":rels,"odd_primary_part":"X_Q,odd^14","two_primary_part":"X_Q[2^infinity]^14 / <KAPPA_1,KAPPA_2>"},
 "right_filtration":{"group":"Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5","origin":"H^1(G_Q,Pic(Ubar)); absolute d2_11=0","quadratic_character_families":"Hom_cont(G_Q,(Z/2)^2) ~= (Q^*/Q^{*2})^2","finite_class_basis":finite_basis,"primary":"2"},
 "exact_filtration_sequence":"0 -> X_Q^14/<KAPPA_1,KAPPA_2> -> Br_a(U) -> Hom_cont(G_Q,(Z/2)^2) direct-sum (Z/2)^5 -> 0",
 "filtration_extension_split_claimed":False,
 "all_odd_primary_classes_accounted":True,"all_two_primary_classes_accounted":True,"br0b_all_primary_classes_accounted":True,
 "complete_Q_defined_open_algebraic_inventory":True,"unresolved_unknown_in_scope":0,
 "unit_status":"READY_FOR_HOSTILE_AUDIT","unit_closed":False,"downstream_released":False,"hostile_audit_required":True,
 "new_kernel_id":"NONE","new_theorem_required":False,
 "theorem_credit":True,"theorem_credit_scope":"Milne ADT I.4 Cor.4.17 only: H^3(G_Q,Z)=0, hence absolute d2_11=0",
 "endpoint_credit":False,"perfect_cuboid_nonexistence_claim":False,"next_expected_command":"Stage33-audit"}
raw=json.dumps(cert,sort_keys=True,separators=(",",":")).encode(); cert["canonical_sha256"]=hashlib.sha256(raw).hexdigest(); (ROOT/"br0b-all-primary-inventory.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"BR0B":"DISCHARGED","BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED":True,"finite_right_class_count":5,"unit_status":cert["unit_status"],"next_expected_command":cert["next_expected_command"],"certificate_sha256":cert["canonical_sha256"]},indent=2,sort_keys=True))
