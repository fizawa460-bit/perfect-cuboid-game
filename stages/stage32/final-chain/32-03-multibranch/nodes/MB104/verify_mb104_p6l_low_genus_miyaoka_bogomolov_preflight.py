#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-P6L-LOW-GENUS-MIYAOKA-BOGOMOLOV-PREFLIGHT-CERTIFICATE.json").read_text())
assert d["surface"]=={"K2":16,"c2":80,"three_c2_minus_K2":224}
assert d["hostile_ray"]["C2_coefficient"]==336
assert d["hostile_ray"]["KC_coefficient"]==112
for l in (1,2,3,10,100):
 lhs=2*(112*l)**2-224*(336*l*l+3*112*l)
 assert lhs==-50176*l*l-75264*l
 assert lhs<0
assert d["smooth_corollary"]["applicable"] is False
assert d["singular_curve_inequality"]["finite_window"] is False
assert d["next_leaf"]=="MB104-P6M-SINGULARITY-TYPE-LOG-BMY-CORRECTION-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())
print("PASS: P6L singular-curve Miyaoka inequality is compatible with all l>=1")
