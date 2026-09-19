#!/usr/bin/env python3
import json
from pathlib import Path

d=json.loads(Path(__file__).with_name("MB104-Z52-SIZE48-QUADRATIC-CI-MILNOR31-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z52_SIZE48_QUADRATIC_CI_MILNOR31_V1"
c=d["local_ci"]
assert c["dimension"]==2 and c["embedding_dimension"]==4 and c["codimension"]==2
assert c["multiplicity"]==4
assert c["defining_initial_orders"]==[2,2]
assert c["projectivized_tangent_cone_degree"]==4
assert c["projectivized_tangent_cone_arithmetic_genus"]==1

s=d["smoothing"]
assert s["exceptional_euler"]==4
assert s["canonical_square"]==-8
assert s["geometric_genus"]==3
mu_plus_one=s["exceptional_euler"]+s["canonical_square"]+12*s["geometric_genus"]
assert mu_plus_one==32
assert s["milnor_number"]==31
assert d["result"]["explicit_tangent_quadratic_pencil"] is False
assert d["result"]["deck_action_on_vanishing_cohomology_known"] is False
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_Z52_SIZE48_QUADRATIC_CI_MILNOR31_V1")
print("orders=(2,2) tangent_cone=2quadrics mu=31")
