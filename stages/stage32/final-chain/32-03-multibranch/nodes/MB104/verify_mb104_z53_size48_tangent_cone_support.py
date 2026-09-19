#!/usr/bin/env python3
import json
from pathlib import Path

d=json.loads(Path(__file__).with_name("MB104-Z53-SIZE48-TANGENT-CONE-SUPPORT-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z53_SIZE48_TANGENT_CONE_SUPPORT_V1"

F=d["maximal_ideal_cycle"]["coefficients"]
n=7
M=[[0]*n for _ in range(n)]
for i in range(n):
    M[i][i]=-2
    if i+1<n:
        M[i][i+1]=M[i+1][i]=1
MF=[sum(M[i][j]*F[j] for j in range(n)) for i in range(n)]
assert MF==d["maximal_ideal_cycle"]["intersection_vector"]
assert [-x for x in MF]==d["maximal_ideal_cycle"]["minusF_degrees"]
assert d["tangent_cone"]["only_positive_degree_components"]==["C1","C5"]
assert d["tangent_cone"]["reduced_support_component_upper_bound"]==2
assert d["tangent_cone"]["lines_distinct_known"] is False
assert d["first_normal"]["dimension"]==1
assert d["first_normal"]["adapter_to_quadratic_initial_forms_known"] is False
assert d["equivariant_milnor"]["total_milnor_number"]==31
assert d["equivariant_milnor"]["character_decomposition_known"] is False
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_Z53_SIZE48_TANGENT_CONE_SUPPORT_V1")
print("-F degrees = 0,1,0,0,0,1,0")
print("next=MB104-Z54-FIRST-NORMAL-TO-QUADRATIC-INITIAL-FORM-ADAPTER")
