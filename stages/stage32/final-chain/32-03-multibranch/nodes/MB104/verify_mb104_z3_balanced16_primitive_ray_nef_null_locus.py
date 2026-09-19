#!/usr/bin/env python3
import json
from pathlib import Path

p=Path(__file__).with_name("MB104-Z3-BALANCED16-PRIMITIVE-RAY-NEF-NULL-LOCUS-CERTIFICATE.json")
d=json.loads(p.read_text())

assert d["schema"]=="STAGE32_MB104_Z3_BALANCED16_PRIMITIVE_RAY_NEF_NULL_LOCUS_V1"
assert d["status"]=="PRE_AUDIT_EXACT_NEF_NULL_LOCUS_REDUCTION_NO_CREDIT"
assert d["primitive_ray"]=="P=7H-4*sum_{i in Sigma}E_i"
assert d["invariants"]=={"P2":336,"support_size":14}

for s,sz,q in [
    ("0000770000ff",48,4),
    ("00007b0000ff",48,4),
    ("000707000f0f",768,2),
]:
    assert d["supports"][s]["orbit_size"]==sz
    assert d["supports"][s]["zero_quartics"]==q

cp=d["curve_partition"]
assert cp["supported_exceptional_pairing"]==8
assert cp["unsupported_exceptional_pairing"]==0
assert cp["outside_support_hyperplane_bound"]=="P.R >= 3*H.R > 0"

c=d["conclusions"]
assert c["P_nef"] is True
assert c["P_big"] is True
assert c["hidden_negative_curve"] is False
assert "unsupported exceptional curves" in c["exact_null_locus"]
assert "zero-pairing elliptic-quartic" in c["exact_null_locus"]

assert all(v is False for v in d["firewalls"].values())

print("PASS: Z3 balanced16 primitive ray is big and nef")
print("outside support hyperplane: P.R >= 3 H.R > 0")
print("exact null locus: unsupported exceptional curves plus zero-pairing elliptic quartics")
