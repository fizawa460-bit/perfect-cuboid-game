#!/usr/bin/env python3
"""Verify V91C1D A2_02 purity/off-boundary and Cech-Cartier assembly."""
from __future__ import annotations
import hashlib, json, runpy
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"
V1B=HERE/"e3-v91c1b-a2-02-resolved-valuation-carrier-preflight.json"
V1C=HERE/"e3-v91c1c-a2-02-strict-transform-prime-refinement.json"
SCALAR=HERE/"boundary-function-scalar-descent-certificate.json"
SELECTOR=HERE/"diagnose_e3_v91c1d_a2_02_v4_transition_selector.py"
CERT_SHA="fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14"
LOCKS={
 V1B:"4398be760e937e1aba279af5fd099b029dc9998675503b5df7130e714ee81387",
 V1C:"ac46916c7e46d3f5b6ac67125b4622d4e4aaa028509879d45811f0e4ec8f28f6",
 SCALAR:"e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b",
}
NEXT="V91C1E_COMPUTE_TYPE_SAFE_MARKED_BRAUER_IMAGE_OF_A2_02_FULL_SURFACE_CECH_CARTIER_SEED_AND_TEST_MASK20_WITHOUT_POSITIONAL_IDENTIFICATION"

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(path,expected):
 o=json.loads(path.read_text(encoding="utf-8")); b=dict(o); h=b.pop("canonical_sha256"); assert h==expected==csha(b),path; return o

cert=load(CERT,CERT_SHA); b=load(V1B,LOCKS[V1B]); c=load(V1C,LOCKS[V1C]); scalar=load(SCALAR,LOCKS[SCALAR])
sel=runpy.run_path(str(SELECTOR))["out"]
assert sel["success"] is True and sel["marker"]=="V91C1D_A2_02_V4_TRANSITION_SELECTOR_PASS"
assert sel["valid_cc_involution_count"]==cert["transition_selector"]["valid_cc_involution_count"]==4
assert sel["valid_ct_involution_count"]==cert["transition_selector"]["valid_ct_involution_count"]==4
assert sel["commuting_v4_pair_count"]==cert["transition_selector"]["commuting_v4_pair_count"]==16
assert sel["canonical_cc_map"]==cert["transition_selector"]["canonical_cc_map"]
assert sel["canonical_ct_map"]==cert["transition_selector"]["canonical_ct_map"]
assert sel["all_selected_function_scalar_units_one"] is True
assert cert["transition_selector"]["all_selected_function_scalar_units_Qi"]==[1,1,0,1]
for g in ("cc","ct"):
 m=cert["transition_selector"][f"canonical_{g}_map"]
 assert all(m[m[x]]==x for x in m)
assert all(cert["transition_selector"]["canonical_cc_map"][cert["transition_selector"]["canonical_ct_map"][x]]==cert["transition_selector"]["canonical_ct_map"][cert["transition_selector"]["canonical_cc_map"][x]] for x in cert["a2_02_literal_seed"]["component_ids"])

pos=b["exact_positive_reuse"]
assert pos["all_48_blowup_centers_evaluated_exact_for_a2_02"] is True
assert pos["a2_02_exceptional_locus_galois_difference_before_purity_correction"]=="ZERO_EXACT"
assert c["exact_consequence"]["resolved_full_surface_height_one_attachment_for_a2_02_complete"] is True
assert c["exact_consequence"]["prime_level_cc_ct_transport_complete"] is True
assert sel["prime_level_package_difference_cc"]=="ZERO_EXACT_PRIME_LEVEL"
assert sel["prime_level_package_difference_ct"]=="ZERO_EXACT_PRIME_LEVEL"
srow=next(r for r in scalar["generator_records"] if r["source_direction"]=="A2_02")
assert srow["action_scalar_records_sha256"]==cert["source_locks"]["a2_02_action_scalar_records_sha256"]
assert srow["all_candidate_scalar_ratios_one"] is True and srow["action_scalar_record_count"]==16

p=cert["purity_cartier"]
assert p["prime_level_package_difference_cc"]==p["prime_level_package_difference_ct"]=="ZERO_EXACT_PRIME_LEVEL"
assert p["exceptional_locus_difference_cc_ct"]=="ZERO_EXACT"
assert p["offboundary_height_one_residue_discrepancy"]=="ZERO_EXACT"
assert p["purity_offboundary_correction"]=="ZERO_DIVISOR_FORCED_BY_EXACT_PRIME_LEVEL_DIFFERENCE"
assert p["cartier_transition_unit"]=="ONE" and p["cartier_correction"]=="ZERO"
assert p["zero_correction_is_assumed_equivariance"] is False

e=cert["exact_consequence"]
for k in ("a2_02_codimension_one_and_resolution_exceptional_residue_audit_complete","a2_02_purity_offboundary_correction_materialized","a2_02_prime_level_cech_transition_data_materialized","a2_02_cartier_transition_binding_materialized","a2_02_full_surface_cech_cartier_seed_assembly_materialized"):
 assert e[k] is True
for k in ("a2_02_marked_brauer_image_computed","a2_02_marked_brauer_image_equal_mask20","a2_02_claimed_e3_coefficient","genuine_full_surface_h2_mu2_lift_for_e3"):
 assert e[k] is False
assert cert["next_exact_leaf"]==NEXT
assert cert["entry_authority"]["v91c1c_hostile_audit_pass_claimed"] is False
assert cert["credit_firewall"]["stage33_progress"]=="6/11"
for k in ("stage33_12_closed_exact","stage33_13_released","e3_kummer_column_materialized","receiver_credit","theorem_credit","endpoint_credit","perfect_cuboid_credit","merge_allowed"):
 assert cert["credit_firewall"][k] is False
print(json.dumps({"success":True,"marker":"V91C1D_A2_02_PURITY_CECH_CARTIER_ASSEMBLY_EXACT","certificate_sha256":CERT_SHA,"canonical_cc_map":"IDENTITY_8","canonical_ct_map":"IDENTITY_8","commuting_v4_pair_count":16,"purity_correction":"ZERO_FORCED","full_surface_a2_02_cech_cartier_seed":True,"marked_brauer_image_computed":False,"next_exact_leaf":NEXT,"stage33_progress":"6/11"},sort_keys=True))
