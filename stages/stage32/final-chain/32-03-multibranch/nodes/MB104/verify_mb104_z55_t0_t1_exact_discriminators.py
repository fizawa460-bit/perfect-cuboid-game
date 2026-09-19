#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-Z55-T0-T1-EXACT-DISCRIMINATORS-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z55_T0_T1_EXACT_DISCRIMINATORS_V1"
T0=d["normal_forms"]["T0"]; T1=d["normal_forms"]["T1"]
assert T0["rank4_quadric_exists"] is False
assert T0["pencil_determinant"]=="IDENTICALLY_ZERO"
assert T0["intersection_point_embedding_dimension"]==3
assert T1["rank4_quadric_exists"] is True
assert T1["pencil_determinant"]=="NONZERO_SCALAR_TIMES_b^4"
assert T1["intersection_point_embedding_dimension"]==2
assert d["cuboid_local_model"]["a1_b1_c_equation"]=="a1^2+b1^2-c^2=0"
assert d["cuboid_local_model"]["source_explicit"] is True
assert d["actual_tangent_type_selected"] is False
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_Z55_T0_T1_EXACT_DISCRIMINATORS_V1")
print("T0: det pencil zero / edim(P0)=3")
print("T1: rank4 exists / edim(P0)=2")
print("next=MB104-Z56-BOUNDED-MAXIMAL-IDEAL-GENERATOR-RECONSTRUCTION")
