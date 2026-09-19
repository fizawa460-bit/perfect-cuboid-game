#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name(
 "MB104-Z36-Z4P-FORCED-ORDINARY-SINGULARITY-LOCALIZATION-PREFLIGHT-CERTIFICATE.json").read_text())
x=d["exact_input"]; m=d["missing_interface"]; a=d["asymptotic"]
assert x["ordinary_count_lower_bound"]=="max(0,112*l-224)"
assert x["for_l_ge_3"]=="112*(l-2)"
assert x["total_delta"]=="168*l^2+56*l"
assert x["equigeneric_reduced_tangent_cone_dimension"]==0
assert all(v is False for v in m.values())
assert a["controlled_ordinary_count_growth"]=="O(l)"
assert a["positivity_scale"]=="(lP-K)^2=336*l^2-224*l+16"
assert a["ordinary_subpackage_alone_overdetermines"] is False
assert d["disposition"]=="PARK_Z36_AT_SINGULARITY_LOCALIZATION_AND_POSTULATION_INTERFACE"
assert d["next_leaf"]=="MB104-Z37-SURVIVING-768-FIRST-NORMAL-EXACT-TRANSITION-REOPEN-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())
print("PASS: Z36 forced ordinary-singularity localization preflight")
print("Lu-Miyaoka supplies only an O(l) count; full O(l^2) singularity package/positions are not source-locked")
print("T-smoothness/postulation cannot be applied from the retained packet")
