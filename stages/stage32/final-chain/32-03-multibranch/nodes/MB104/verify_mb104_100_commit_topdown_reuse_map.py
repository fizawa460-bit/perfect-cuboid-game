#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-100-COMMIT-TOPDOWN-REUSE-MAP-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_100_COMMIT_TOPDOWN_REUSE_MAP_V1"
assert d["reviewed_commit_window"]==100
assert d["frontier"]["support"]=="000707000f0f"
assert d["frontier"]["orbit_size"]==768
assert d["exact_assets"]["six_fibration_P_intersections"]==[40,40,56,44,44,56]
assert d["exact_assets"]["common_ramification_bound"]=="80*l"
assert "degree10_residual_enumeration" in d["no_duplicate_32_01"]
assert d["priorities"][0]["id"]=="SIX_POLAR_CONDUCTOR_FITTING_GLOBALIZATION"
assert d["priorities"][1]["id"]=="SIX_ORDER_BRANCH_SEMIGROUP_JET_INEQUALITY"
assert "SIZE48_LOCAL_ANALYTIC_CHAIN" in d["parked"]
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_100_COMMIT_TOPDOWN_REUSE_MAP_V1")
print("frontier=000707; use 32-01 fibrations as measurement layer, not duplicate search")
print("priority=six-polar conductor globalization | six-order semigroup/jet")
