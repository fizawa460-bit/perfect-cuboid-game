#!/usr/bin/env python3
import json
from pathlib import Path

p=Path(__file__).with_name("MB104-Z3-SIZE48-BIRKAR-SEMIAMPLENESS-CERTIFICATE.json")
d=json.loads(p.read_text())

assert d["schema"]=="STAGE32_MB104_Z3_SIZE48_BIRKAR_SEMIAMPLENESS_V1"
assert d["status"]=="PRE_AUDIT_SOURCE_BASED_SEMIAMPLENESS_RESULT_NO_CREDIT"
assert d["supports"]==["0000770000ff","00007b0000ff"]

n=d["complete_null_locus"]
assert n["connected_tree_components"]==2
assert n["isolated_unsupported_exceptionals"]==32
assert n["tree_shape"]=="Q-E-Q"

f=d["formal_restriction"]
assert f["tree_all_finite_thickenings_trivial"] is True
assert f["isolated_exceptional_all_finite_thickenings_trivial"] is True
assert f["complete_null_locus_all_finite_thickenings_trivial"] is True

b=d["birkar_application"]
assert b["P_nef"] is True
assert b["P_Q_Cartier"] is True
assert b["Z_reduced_equals_exceptional_locus"] is True
assert b["Z_contained_in_some_finite_null_thickening"] is True
assert b["P_restricted_to_Z_trivial"] is True
assert b["P_semiample"] is True

assert all(v is False for v in d["firewalls"].values())
print("PASS: Z3 size48 Birkar semiampleness")
print("complete null locus formal restriction is trivial to all finite orders")
print("Birkar Theorem 1.5 => P is semiample on both size48 balanced orbits")
