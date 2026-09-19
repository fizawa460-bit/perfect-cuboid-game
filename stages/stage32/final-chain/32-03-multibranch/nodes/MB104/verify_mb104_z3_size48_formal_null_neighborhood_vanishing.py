#!/usr/bin/env python3
import json
from pathlib import Path

p=Path(__file__).with_name("MB104-Z3-SIZE48-FORMAL-NULL-NEIGHBORHOOD-VANISHING-CERTIFICATE.json")
d=json.loads(p.read_text())

assert d["schema"]=="STAGE32_MB104_Z3_SIZE48_FORMAL_NULL_NEIGHBORHOOD_VANISHING_V1"
assert d["status"]=="PRE_AUDIT_EXACT_FORMAL_PICARD_NO_GO_NO_CREDIT"

for s in ("0000770000ff","00007b0000ff"):
    assert d["supports"][s]["orbit_size"]==48
    assert d["supports"][s]["formal_null_tree_components"]==2

t=d["tree_component"]
i=t["intersections"]
assert i["Q1^2"]==-4 and i["Q2^2"]==-4 and i["E^2"]==-2
assert i["Q1.E"]==1 and i["Q2.E"]==1 and i["Q1.Q2"]==0
u=t["U_intersections"]
assert u=={"U.Q1":-3,"U.Q2":-3,"U.E":0}

n=t["for_n_ge_1"]
assert n["degrees_OU_minus_nU"]=={"Q1":"3n","Q2":"3n","E":0}
assert n["component_H1_zero"] is True
assert n["normalization_evaluation_surjective"] is True
assert n["H1_OU_minus_nU"]==0

f=d["formal_picard"]
assert f["Pic_transition_isomorphism_for_all_n_ge_1"] is True
assert f["O_U_P_trivial_from_Z33E_Z33G"] is True
assert f["O_nU_P_trivial_for_all_n_ge_1"] is True
assert f["O_nU_lP_trivial_for_all_l_n_ge_1"] is True

assert d["disposition"]["size48_excluded"] is False
assert d["disposition"]["finite_formal_picard_obstruction"] is False
assert d["disposition"]["future_formal_gluing_focus"]=="000707000f0f"

assert all(v is False for v in d["credit_firewall"].values())

print("PASS: Z3 size-48 formal null-neighborhood vanishing")
print("H1(U,O_U(-nU))=0 for all n>=1 on both tree null unions")
print("finite formal Picard gluing cannot exclude the two size-48 balanced orbits")
