#!/usr/bin/env python3
"""Verify V91C1T A2_02 swap23 Pic/2 adapter preflight."""
from __future__ import annotations
import hashlib, json, runpy
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"e3-v91c1t-a2-02-swap23-pic2-adapter-preflight.json"
V1S=HERE/"diagnose_e3_v91c1s_swap23_prime_attached_cech_difference.py"
V1D=HERE/"e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"
V1L=HERE/"e3-v91c1l-a2-02-cech-to-marked-discriminant-dual-evaluation-contract.json"
J2=HERE/"audit_j2_current_v4_pic2_cocycle_v32.py"
V91=HERE/"e3-retained-at-marked-picard-dual-source-v91.json"
PROPER=HERE.parent/"33-07"/"proper-brauer2-from-discriminant.json"

CERT_SHA="6c064cf02fb7a0908242317bf7ac1b20b0586751b78e07b26d6c7889060ffdfa"
LOCKS={
 V1D:"fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14",
 V1L:"6ae7e0464c2acd012c1c486e6a12fdb806d65049359c0c6c2440168be138e3dc",
 V91:"729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9",
 PROPER:"c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
}

def csha(o):
 return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def load(path, expected):
 o=json.loads(path.read_text(encoding="utf-8")); b=dict(o); h=b.pop("canonical_sha256")
 assert h==expected==csha(b), path
 return o

cert=load(CERT,CERT_SHA)
d=load(V1D,LOCKS[V1D]); l=load(V1L,LOCKS[V1L]); v91=load(V91,LOCKS[V91]); proper=load(PROPER,LOCKS[PROPER])
s=runpy.run_path(str(V1S))["result"]
assert s["success"] is True
assert s["full_codim1_package_difference_zero"] is False
assert s["components_with_zero_full_attached_divisor_difference"]==0
assert s["component_count"]==8
assert s["strict_package_difference_nonzero_coefficients"]==8
assert s["strict_package_difference_sha256"]=="e3a0426055c2c4722b32159e7d589a662f6fcec3b04b1944149c0d31f96f30a1"
assert s["exceptional_package_difference_nonzero_coefficients"]==28
assert s["exceptional_package_difference_sha256"]=="a272ec956ffcef457c9b2503c9e864d7cfa15472f96956fe5fde814b38d6bf02"
assert s["retained_carrier_images_missing_count"]==12
assert s["acted_actual_primes_outside_retained_inventory_count"]==10
assert s["swap23_actual_prime_transport_materialized"] is True
assert s["exceptional_node_inventory_closed_under_swap23"] is True
assert s["pic2_cech_difference_class_computed"] is False
assert s["a2_02_swap23_seed_fixed_mod_pic2"] is False
assert s["a2_02_marked_brauer_image_excluded_from_mask20"] is False

assert d["exact_consequence"]["a2_02_full_surface_cech_cartier_seed_assembly_materialized"] is True
assert l["acceptance"]["source_evaluation_vector_materialized"] is False
assert l["exact_consequence"]["source_bound_marked_brauer_functional_materialized"] is False

# Type firewall: historical J2 Pic/2 machinery is explicitly J2-specific and is
# not silently relabelled as an A2_02 source adapter.
j2_text=J2.read_text(encoding="utf-8")
assert "J2" in j2_text
assert "A2_02" not in j2_text

# The retained target-side JSON assets do not contain a materialized named
# actual-divisor -> Picard64 adapter interface.
for obj in (v91, proper):
 text=json.dumps(obj,sort_keys=True)
 assert "actual_divisor_to_picard64" not in text
 assert "swap23_actual_divisor" not in text

e=cert["exact_consequence"]
assert e["literal_swap23_full_codim1_difference_materialized"] is True
assert e["literal_swap23_full_codim1_difference_nonzero"] is True
for k in ("pic2_cech_difference_class_computed","a2_02_swap23_seed_fixed_mod_pic2",
          "a2_02_marked_brauer_image_excluded_from_mask20","a2_02_marked_brauer_image_computed"):
 assert e[k] is False
assert cert["evaluated_adapter_inventory"]["scope"]=="LOCKED_CURRENT_WORKING_SET_ONLY_NOT_REPOSITORY_WIDE"
assert cert["anti_inference"]["repository_wide_absence_claim"] is False
assert cert["anti_inference"]["mathematical_nonexistence_claim"] is False
assert cert["credit_firewall"]["stage33_progress"]=="6/11"
assert cert["credit_firewall"]["merge_allowed"] is False
print(json.dumps({
 "success":True,
 "marker":"V91C1T_A2_02_SWAP23_PIC2_ADAPTER_PREFLIGHT",
 "certificate_sha256":CERT_SHA,
 "literal_full_codim1_difference_zero":False,
 "pic2_cech_difference_class_computed":False,
 "next_exact_leaf":cert["next_exact_leaf"],
 "stage33_progress":"6/11"
},sort_keys=True))
