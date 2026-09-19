#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-Z54-QUADRATIC-TANGENT-TWO-NORMAL-FORMS-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z54_QUADRATIC_TANGENT_TWO_NORMAL_FORMS_V1"
assert d["support"]["distinct_intersecting_lines"] is True
assert d["support"]["reduced_ideal"]==["x","y*z"]
forms={x["id"]:x for x in d["normal_forms"]}
assert set(forms)=={"T0","T1"}
assert forms["T0"]["equations"]==["x^2","y*z"]
assert forms["T0"]["second_quadric_rank"]==2
assert forms["T1"]["equations"]==["x^2","y*z+x*w"]
assert forms["T1"]["second_quadric_rank"]==4
assert d["classification"]["count"]==2
assert d["classification"]["continuous_parameter_survives_at_quadratic_level"] is False
assert d["classification"]["actual_type_selected"] is False
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_Z54_QUADRATIC_TANGENT_TWO_NORMAL_FORMS_V1")
print("normal_forms=T0:(x^2,yz), T1:(x^2,yz+xw)")
print("next=MB104-Z55-T0-VS-T1-CUBOID-TANGENT-BIT")
