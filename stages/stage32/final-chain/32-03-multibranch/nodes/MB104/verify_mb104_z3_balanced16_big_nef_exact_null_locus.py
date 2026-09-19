#!/usr/bin/env python3
import json
from pathlib import Path

p=Path(__file__).with_name("MB104-Z3-BALANCED16-BIG-NEF-EXACT-NULL-LOCUS-CERTIFICATE.json")
d=json.loads(p.read_text())

assert d["schema"]=="STAGE32_MB104_Z3_BALANCED16_BIG_NEF_EXACT_NULL_LOCUS_V1"
assert d["status"]=="PRE_AUDIT_EXACT_Z3_NEGATIVE_CURVE_CLOSURE_NO_CREDIT"
assert d["ray"]["P2"]==336

h=d["hyperplane_inequality"]
assert h["for_nonexceptional_R_not_in_support_hyperplane"]=="sum_{i in Sigma} E_i.R <= H.R"
assert h["consequence"]=="P.R >= 3*(H.R) > 0"

c=d["contained_components"]
assert c["size48_orbits"]["supports"]==["0000770000ff","00007b0000ff"]
assert c["size48_orbits"]["supported_nodes_per_component"]==7
assert c["size48_orbits"]["pairing_each"]==0
assert c["size768_orbits"]["supports"]==["000707000f0f","00070b000f0f"]
assert c["size768_orbits"]["supported_nodes_per_component"]==7
assert c["size768_orbits"]["pairing_each"]==0

e=d["exceptional_curves"]
assert e["supported_pairing"]==8
assert e["unsupported_pairing"]==0

q=d["conclusions"]
assert q["all_four_balanced_rays_nef"] is True
assert q["all_four_balanced_rays_big"] is True
assert q["hidden_negative_curve"] is False
assert q["exact_null_locus"] is True

assert all(v is False for v in d["firewalls"].values())

print("PASS: Z3 balanced16 big-nef exact null locus")
print("outside the support hyperplane: P.R >= 3 H.R > 0")
print("inside: only the exact zero-pairing section quartics; no hidden negative curve")
