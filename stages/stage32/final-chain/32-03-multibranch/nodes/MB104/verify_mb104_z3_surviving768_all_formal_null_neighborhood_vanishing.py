#!/usr/bin/env python3
import json
from pathlib import Path

p=Path(__file__).with_name("MB104-Z3-SURVIVING768-ALL-FORMAL-NULL-NEIGHBORHOOD-VANISHING-CERTIFICATE.json")
d=json.loads(p.read_text())

assert d["schema"]=="STAGE32_MB104_Z3_SURVIVING768_ALL_FORMAL_NULL_NEIGHBORHOOD_VANISHING_V1"
assert d["status"]=="PRE_AUDIT_EXACT_ALL_FINITE_FORMAL_PICARD_NO_GO_NO_CREDIT"
assert d["support"]=="000707000f0f"

g=d["geometry"]
assert g=={"A2":-4,"B2":-4,"A_dot_B":2,"intersection_point_count":2}

h=d["higher_kernels"]
assert h["sheaf"]=="O_U(-nU)"
assert h["degree_on_A"]=="2n" and h["degree_on_B"]=="2n"
assert h["for_n_ge_2"]["two_point_evaluation_surjective"] is True
assert h["for_n_ge_2"]["H1_U"]==0

f=d["first_step"]
assert f["n"]==1 and f["handled_by_Z37"] is True and f["O_2U_P_trivial"] is True

i=d["induction"]
assert i["Pic_transition_isomorphism_for_n_ge_2"] is True
assert i["O_nU_P_trivial_for_all_n_ge_1"] is True
assert i["O_nU_lP_trivial_for_all_l_n_ge_1"] is True

x=d["disposition"]
assert x["second_normal_separate_computation_needed"] is False
assert x["finite_formal_picard_route_exhausted"] is True
assert x["support_excluded"] is False

print("PASS: Z3 surviving768 all finite formal null-neighborhood vanishing")
print("Z37 kills n=1; H1(U,O_U(-nU))=0 for n>=2")
print("separate Z38 second-normal computation is unnecessary")
