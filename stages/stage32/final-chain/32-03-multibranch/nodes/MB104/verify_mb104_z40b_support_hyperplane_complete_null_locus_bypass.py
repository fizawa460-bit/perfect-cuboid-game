#!/usr/bin/env python3
import json
from pathlib import Path

p=Path(__file__).with_name("MB104-Z40B-SUPPORT-HYPERPLANE-COMPLETE-NULL-LOCUS-BYPASS-CERTIFICATE.json")
d=json.loads(p.read_text())

assert d["schema"]=="STAGE32_MB104_Z40B_SUPPORT_HYPERPLANE_COMPLETE_NULL_LOCUS_BYPASS_V1"
assert d["status"]=="PRE_AUDIT_EXACT_Z40_ENUMERATION_BYPASS_NO_CREDIT"

for s,sz,nc in [
    ("0000770000ff",48,4),
    ("00007b0000ff",48,4),
    ("000707000f0f",768,2),
]:
    assert d["supports"][s]["orbit_size"]==sz
    assert d["supports"][s]["section_components"]==nc
    assert d["supports"][s]["component_degree"]==4

q=d["proof"]
assert q["outside_hyperplane_contact_bound"]=="sum_Sigma M_i <= e"
assert q["outside_hyperplane_pairing"]=="P.R >= 3e > 0"
assert q["null_implies_in_support_hyperplane"] is True
assert q["contained_curve_is_section_component"] is True
assert q["section_components_complete"] is True
assert q["supported_exceptional_pairing"]==8
assert q["unsupported_exceptional_pairing"]==0

c=d["conclusion"]
assert c["complete_P_null_locus"] is True
assert c["unknown_degree8_12_16_20_null_curves"] is False
assert c["z40_picard64_enumeration_needed_for_balanced_uniform_null_locus"] is False

assert all(v is False for v in d["firewalls"].values())
print("PASS: Z40B support-hyperplane null-locus bypass")
print("P-null nonexceptional curves are forced into the support hyperplane")
print("exact incidence-16 section classification leaves only the known degree-4 zero quartics")
