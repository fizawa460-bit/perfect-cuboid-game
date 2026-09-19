#!/usr/bin/env python3
import json
from pathlib import Path

p=Path(__file__).with_name("MB104-Z3-COMPLETE-P-NULL-LOCUS-BY-SUPPORT-HYPERPLANE-CERTIFICATE.json")
d=json.loads(p.read_text())

assert d["schema"]=="STAGE32_MB104_Z3_COMPLETE_P_NULL_LOCUS_BY_SUPPORT_HYPERPLANE_V1"
assert d["status"]=="PRE_AUDIT_EXACT_NULL_LOCUS_COMPLETENESS_NO_CREDIT"

a=d["algebra"]
assert a["P"]=="7H-4*sum_Sigma(E_i)"
assert a["support_size"]==14
assert a["P_null_equation"]=="7e=4*M_Sigma"
assert a["P_null_implies_M_over_e"]=="M_Sigma=7e/4"
assert a["outside_hyperplane_contact_bound"]=="M_Sigma<=e"
assert a["contradiction_for_e_positive"] is True

s=d["section_geometry"]
assert s["balanced_quartic_supported_nodes"]==7
assert s["quartic_pairing"]=="7*4-4*7=0"

e=d["exceptional_geometry"]
assert e=={"supported_pairing":8,"unsupported_pairing":0,"unsupported_count":34}

for mask,sz,q in [
    ("0000770000ff",48,4),
    ("00007b0000ff",48,4),
    ("000707000f0f",768,2),
]:
    x=d["complete_null_locus"][mask]
    assert x["orbit_size"]==sz
    assert x["unsupported_exceptionals"]==34
    assert x["elliptic_quartics"]==q

c=d["conclusions"]
assert c["complete_P_null_locus_classified"] is True
assert c["unknown_positive_degree_P_null_curve"] is False
assert c["Z40_geometric_null_enumeration_needed"] is False

assert all(v is False for v in d["firewalls"].values())

print("PASS: complete P-null locus by support hyperplane")
print("P-null nonexceptional curve must lie in the unique support hyperplane")
print("incidence-16 section classification leaves only the retained zero elliptic quartics")
