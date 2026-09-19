#!/usr/bin/env python3
import json
from pathlib import Path

d=json.loads(Path(__file__).with_name("MB104-Z47-POST-CONTRACTION-GLOBAL-RESCORE-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z47_POST_CONTRACTION_GLOBAL_RESCORE_V1"
assert d["authority"]["mb_cross_lane_open_demand"] is False
v=d["new_view"]
assert v["line_identity"]=="O_E(Cond_C) ~= A^(3l+1), A=K_Y|_E"
# degree checksum: deg A=112l, exponent=3l+1
for l in range(1,20):
    deg=112*l*(3*l+1)
    delta=168*l*l+56*l
    assert deg==2*delta
assert v["obstruction"] is False
assert d["cycle"]["live_candidates"]==0
assert d["cycle"]["exhaustive_view_audit"] is True
assert d["cycle"]["blind_rediscovery"] is True
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_Z47_POST_CONTRACTION_GLOBAL_RESCORE_V1")
print("new_view=adjunction_conductor_root exact_but_nonrestrictive")
print("class3_boundary=true live_candidates=0")
