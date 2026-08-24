#!/usr/bin/env python3
"""Prepare the Stage33-03 hostile-audit handoff without releasing downstream."""
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
inv=json.loads((ROOT/"br0b-all-primary-inventory.json").read_text())
ext=json.loads((ROOT/"absolute-h2-extension-class.json").read_text())
required=["explicit_galois_action_certified","upic_gersten_maps_certified","kernels_cokernels_torsion_exact","unit_kernel_absolute_galois_inflation_character_terms_exact","no_unjustified_two_primary_restriction","qbar_to_q_descent_adapter_certified","open_algebraic_q_defined_class_inventory_complete","br0b_all_primary_classes_accounted","filtration_extension_class_exact"]
if any(not inv[k] for k in required): raise SystemExit("Stage33-03 non-audit closure gate failed")
if inv["filtration_extension_split_claimed"]: raise SystemExit("unexpected filtration split claim")
if not ext["full_extension_class_exact"] or not ext["primary_orders_exact_parametrically"]: raise SystemExit("extension certificate incomplete")
if inv["source_locks"]["absolute_h2_extension_class_sha256"]!=ext["canonical_sha256"]: raise SystemExit("extension certificate source-lock mismatch")
if inv["br0b"]!="DISCHARGED" or inv["unresolved_unknown_in_scope"]!=0: raise SystemExit("BR0B closure regression")
h={"schema":"STAGE33_03_PREAUDIT_HANDOFF_V2_EXTENSION_EXACT","stage33_unit":"33-03","unit_name":"BR0B_ABSOLUTE_GALOIS_UPIC_GERSTEN","unit_status":"AUDIT_REQUIRED","unit_closed":False,"downstream_released":False,"prerequisite_units":["33-02"],"prerequisites_all_closed":True,"closure_criteria_total":11,"closure_criteria_satisfied":10,"hostile_audit":"PENDING","unresolved_unknown_in_scope":0,"receivers_discharged_provisional":["R29-BR0B"],"new_kernel_id":"NONE","br0b":"DISCHARGED","br0b_all_primary_classes_accounted":True,"open_algebraic_q_defined_class_inventory_complete":True,"kernels_cokernels_torsion_exact":True,"filtration_extension_split_claimed":False,"filtration_extension_class_exact":True,"extension_certificate_sha256":ext["canonical_sha256"],"inventory_certificate_sha256":inv["canonical_sha256"],"theorem_credit":inv["theorem_credit"],"endpoint_credit":False,"perfect_cuboid_nonexistence_claim":False,"next_expected_command":"Stage33-audit"}
raw=json.dumps(h,sort_keys=True,separators=(",",":")).encode(); h["canonical_sha256"]=hashlib.sha256(raw).hexdigest(); (ROOT/"handoff-preaudit.json").write_text(json.dumps(h,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"UNIT_STATUS":"AUDIT_REQUIRED","closure_criteria_satisfied":"10/11","BR0B":"DISCHARGED","FILTRATION_EXTENSION_CLASS_EXACT":True,"FILTRATION_EXTENSION_SPLIT_CLAIMED":False,"next_expected_command":"Stage33-audit","certificate_sha256":h["canonical_sha256"]},indent=2,sort_keys=True))
