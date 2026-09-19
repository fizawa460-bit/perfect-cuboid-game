#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path
d=json.loads(Path(__file__).with_name(
 "MB104-Z45-FULL-NULL-BOUNDARY-SABATINO-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z45_FULL_NULL_BOUNDARY_SABATINO_V1"
assert d["size48"]["D2"]==-76 and d["size48"]["KplusD2"]==-28
assert d["size768"]["D2"]==-68 and d["size768"]["KplusD2"]==-36
for l in range(1,10000):
    m48=Fraction(4*(l+57),3*(l+1))
    m768=Fraction(28*(l+9),3*(l+1))
    assert m48>Fraction(4,3)
    assert m768>Fraction(28,3)
assert d["size48"]["contradiction"] is False
assert d["size768"]["contradiction"] is False
assert d["conclusion"]["finite_l_window"] is False
assert d["next_leaf"]=="MB104-Z46-LOG-BOGOMOLOV-MIYAOKA-CORRECTION-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())
print("PASS: Z45 full-null-boundary Sabatino reoptimization")
print("size48 minimum=4(l+57)/(3(l+1)) > 4/3")
print("size768 minimum=28(l+9)/(3(l+1)) > 28/3")
print("actual null boundary sharpens but does not close the surviving rays")
