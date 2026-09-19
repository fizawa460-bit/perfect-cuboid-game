#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-Z33H-SURVIVING-768-FIRST-NORMAL-GLUING-PREFLIGHT-CERTIFICATE.json").read_text())
g=d["geometry"]; c=d["conormal"]; r=d["retained_interface"]
assert d["support"]=="000707000f0f"
assert g=={"A2":-4,"B2":-4,"A_dot_B":2,"ordinary_holonomy":"1"}
assert c["sheaf"]=="O_U(-U)"
assert c["degree_on_A"]==2 and c["degree_on_B"]==2
assert c["H1_component_A"]==0 and c["H1_component_B"]==0
assert r["ordinary_transition_values_exact"] is True
assert r["normal_direction_transition_coefficients_source_locked"] is False
assert r["normalized_first_neighborhood_class_computed"] is False
assert d["disposition"]=="PARK_Z33H_AT_FIRST_NORMAL_NEIGHBORHOOD_INTERFACE"
assert d["next_leaf"]=="MB104-Z34-Z12-BTVA-GENERAL-M-SUPPORT-HILBERT-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())
print("PASS: Z33H first-normal-neighborhood preflight wall")
print("ordinary holonomy is trivial; only a cycle-coupled normal-direction class can remain")
print("no retained normalized first-neighborhood adapter; route parked")
