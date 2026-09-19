#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

d=json.loads(Path(__file__).with_name(
 "MB104-Z41B-EXACT-LINE-BUNDLE-DESCENT-INDEX3-CERTIFICATE.json").read_text())

assert d["schema"]=="STAGE32_MB104_Z41B_EXACT_LINE_BUNDLE_DESCENT_INDEX3_V1"
f=d["formal_descent"]
assert f["phi_*O_S_equals_O_Y"] is True
assert f["completed_M_equals_completed_OY_at_contracted_points"] is True
assert f["faithful_flat_descent_to_local_freeness"] is True
assert f["A_line_bundle"] is True
assert f["pullback_A_equals_O_P"] is True
assert f["A_ample"] is True

c=d["canonical"]
assert c["A_equals_O_3KY"] is True
assert c["three_KY_Cartier"] is True and c["three_KY_ample"] is True
assert c["global_index"]==3
assert c["nonrational_local_index"]==3
assert c["isolated_A1_index"]==1
assert Fraction(c["K_Y2"])==Fraction(112,3)
assert c["e_Y_reg"]==16

assert d["next_leaf"]=="MB104-Z43-INDEX-THREE-CANONICAL-COVER-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())
print("PASS: Z41B exact line-bundle descent")
print("O_S(P)=phi^*O_Y(3K_Y), with 3K_Y ample Cartier")
print("nonrational contraction points have exact canonical index 3")
