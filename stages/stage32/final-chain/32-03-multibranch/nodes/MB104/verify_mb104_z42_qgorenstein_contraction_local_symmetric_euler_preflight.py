#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path
d=json.loads(Path(__file__).with_name(
 "MB104-Z42-QGORENSTEIN-CONTRACTION-LOCAL-SYMMETRIC-EULER-PREFLIGHT-CERTIFICATE.json"
).read_text())
assert d["schema"]=="STAGE32_MB104_Z42_QGORENSTEIN_LOCAL_SYMMETRIC_EULER_PREFLIGHT_V1"
z=d["z41_input"]
assert z["K_Y_ample"] is True
assert Fraction(z["K_Y2"])==Fraction(112,3)
assert z["e_Y_reg"]==16
assert z["q_gorenstein_index_divides"]==3
s48=d["singularities"]["size48"]; s768=d["singularities"]["size768"]
assert s48["fundamental_genus"]==2 and s768["fundamental_genus"]==3
assert s48["quotient_A_n"] is False and s768["quotient_A_n"] is False
assert s48["log_canonical"] is False and s768["log_canonical"] is False
lit=d["literature"]
assert lit["exact_formula_for_current_nonlc_graphs_found"] is False
assert lit["graph_data_alone_source_proven_sufficient"] is False
c=d["conclusion"]
assert c["local_symmetric_euler_coefficient_computed"] is False
assert c["btva_N14_sign_repaired"] is False
assert c["quotient_formula_transfer_authorized"] is False
assert d["disposition"]=="PARK_Z42_AT_NONLC_LOCAL_SYMMETRIC_EULER_INTERFACE"
assert d["next_leaf"]=="MB104-Z43-INDEX-ONE-CANONICAL-COVER-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())
print("PASS: Z42 Q-Gorenstein local symmetric-Euler interface wall")
print("explicit A_n/quotient formulas do not source-completely cover the actual non-lc graph singularities")
print("next: Z43 index-one canonical cover preflight")
