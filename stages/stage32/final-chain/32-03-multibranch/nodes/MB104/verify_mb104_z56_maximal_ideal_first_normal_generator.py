#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-Z56-MAXIMAL-IDEAL-FIRST-NORMAL-GENERATOR-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z56_MAXIMAL_IDEAL_FIRST_NORMAL_GENERATOR_V1"
assert d["cycles"]["F_plus_D"]==[2,3,3,3,3,3,2]
assert d["cycles"]["two_F"]==[2,4,4,4,4,4,2]
r=d["restriction"]
assert r["degrees"]==[0,1,0,0,0,1,0]
assert sum(r["component_h0"])-r["node_count"]==3
assert r["h0"]==3 and r["h1"]==0
t=d["tangent"]
assert t["embedding_dimension"]==4
assert t["exceptional_visible_dimension"]==3
assert t["first_normal_generator_dimension"]==1
assert t["x_restricts_zero_on_D"] is True
q=d["quadratic_receiver"]
assert q["q1"]=="x^2"
assert q["q2"]=="y*z + c*x*w"
assert q["actual_case_known"] is False
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_Z56_MAXIMAL_IDEAL_FIRST_NORMAL_GENERATOR_V1")
print("m/m2 = 3 exceptional-visible + 1 first-normal generator")
print("quadratic bit: yz + c*xw, c=0 vs c!=0")
