#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name(
 "MB104-Z43-INDEX3-CANONICAL-COVER-PREFLIGHT-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z43_INDEX3_CANONICAL_COVER_PREFLIGHT_V1"
assert d["input"]["nonrational_local_index"]==3
assert d["input"]["three_KY_Cartier"] is True
c=d["canonical_cover"]
assert c["degree"]==3
assert c["algebra"]=="O + O(-K) + O(-2K)"
assert c["quasi_etale_off_singular_point"] is True
assert c["K_upstairs_Cartier"] is True
assert c["Gorenstein"] is True
assert d["conclusion"]["analytic_type_classified"] is False
assert d["conclusion"]["local_symmetric_euler_coefficient_computed"] is False
assert d["disposition"]=="PARK_Z43_AT_CANONICAL_COVER_ANALYTIC_TYPE_INTERFACE"
assert d["next_leaf"]=="MB104-Z44-CANONICAL-ALGEBRA-FROM-CUBOID-HYPERPLANE-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())
print("PASS: Z43 exact index-three canonical cover preflight")
print("degree-three Gorenstein canonical cover exists")
print("analytic type is not source-determined by the retained graph/discrepancy data")
