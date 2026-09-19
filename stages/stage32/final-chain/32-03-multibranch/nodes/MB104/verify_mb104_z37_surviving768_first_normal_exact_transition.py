#!/usr/bin/env python3
import json
from pathlib import Path

p=Path(__file__).with_name("MB104-Z37-SURVIVING-768-FIRST-NORMAL-EXACT-TRANSITION-CERTIFICATE.json")
d=json.loads(p.read_text())

assert d["schema"]=="STAGE32_MB104_Z37_SURVIVING768_FIRST_NORMAL_EXACT_TRANSITION_V1"
assert d["status"]=="PRE_AUDIT_EXACT_FIRST_NORMAL_VANISHING_NO_CREDIT"
assert d["support"]=="000707000f0f"

lc=d["local_coordinates"]
assert lc["x"]=="b1" and lc["y"]=="b2"
assert lc["A"]=="x=0" and lc["B"]=="y=0" and lc["U"]=="xy=0"

t=d["transition"]
assert t["g_at_each_intersection"]=="i"
assert t["normalized_G"]=="g/i"

dt=d["derivative_table"]
assert dt["LA_x"]==0 and dt["LA_y"]=="i" and dt["LA_xy"]==0
assert dt["LB_x"]==-1 and dt["LB_y"]==0 and dt["LB_xy"]==0
assert dt["log_a2_xy"]==0 and dt["log_a3_xy"]==0
assert dt["log_g_xy"]==0

fn=d["first_normal"]
assert fn["c_plus"]==0 and fn["c_minus"]==0
assert fn["cycle_vector"]==[0,0]
assert fn["obstruction"] is False

disp=d["disposition"]
assert disp["surviving_768_excluded"] is False
assert disp["higher_formal_obstruction_computed"] is False

assert all(v is False for v in d["credit_firewall"].values())

print("PASS: Z37 surviving-768 first-normal exact transition")
print("ordinary holonomy is 1 and conductor-normalized first-normal coefficients are (0,0)")
print("no first-normal Picard obstruction; any formal obstruction must begin at higher order")
