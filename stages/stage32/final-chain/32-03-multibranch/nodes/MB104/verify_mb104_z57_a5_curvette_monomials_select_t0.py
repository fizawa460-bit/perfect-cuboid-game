#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-Z57-A5-CURVETTE-MONOMIALS-SELECT-T0-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z57_A5_CURVETTE_MONOMIALS_SELECT_T0_V1"
F=d["graph"]["F"]
assert F==[1,2,2,2,2,2,1]
s=d["a5"]["val_s"]; u=d["a5"]["val_u"]; v=d["a5"]["val_v"]
assert [u[i]+v[i] for i in range(7)]==[6*x for x in s]
g=d["generators"]
assert g["val_y"]==[u[i]+s[i] for i in range(7)]
assert g["val_z"]==[v[i]+s[i] for i in range(7)]
assert g["val_w"]==[2*x for x in s]
assert g["val_x"]==[3*x for x in s]
twoF=[2*x for x in F]; threeF=[3*x for x in F]
for key in ["val_y","val_z","val_w","val_x"]:
    val=g[key]
    assert all(val[i]>=F[i] for i in range(7))
    assert not all(val[i]>=twoF[i] for i in range(7))
val_s6=[6*x for x in s]; val_s8=[8*x for x in s]
assert all(val_s6[i]>=threeF[i] for i in range(7))
assert all(val_s8[i]>=threeF[i] for i in range(7))
c=d["conclusion"]
assert c["tangent_type"]=="T0"
assert c["quadratic_initial_ideal"]==["x^2","y*z"]
assert c["mixed_coefficient_c"]==0
assert c["determinant_identically_zero"] is True
assert c["rank4_quadric_exists"] is False
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_Z57_A5_CURVETTE_MONOMIALS_SELECT_T0_V1")
print("T0 selected: initial ideal (x^2,yz), c=0")
