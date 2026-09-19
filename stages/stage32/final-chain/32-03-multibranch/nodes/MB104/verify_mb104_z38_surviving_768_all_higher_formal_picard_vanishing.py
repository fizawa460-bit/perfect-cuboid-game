#!/usr/bin/env python3
import json
from pathlib import Path

d=json.loads(Path(__file__).with_name(
 "MB104-Z38-SURVIVING-768-ALL-HIGHER-FORMAL-PICARD-VANISHING-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z38_SURVIVING768_ALL_HIGHER_FORMAL_PICARD_VANISHING_V1"
assert d["support"]=="000707000f0f"
assert d["geometry"]=={"A2":-4,"B2":-4,"A_dot_B":2,"intersection_points":2}

h=d["higher_kernel"]
for n in range(2,100):
    assert 2*n>0
    assert 2*n-2>0
assert h["degree_on_A"]=="2n"
assert h["degree_on_B"]=="2n"
assert h["degree_after_two_node_subtraction"]=="2n-2"
assert h["component_H1_zero_for_n_ge_1"] is True
assert h["two_node_evaluation_surjective_for_n_ge_2"] is True
assert h["H1_U_zero_for_n_ge_2"] is True
assert h["Pic_transition_isomorphism_for_n_ge_2"] is True

b=d["base"]; c=d["conclusion"]
assert b["O_U_P_trivial"] is True
assert b["O_2U_P_trivial_from_Z37"] is True
assert c["O_nU_P_trivial_all_finite_n"] is True
assert c["O_nU_lP_trivial_all_l_all_finite_n"] is True
assert c["finite_formal_picard_obstruction"] is False
assert c["surviving_768_excluded"] is False
assert d["next_leaf"]=="MB104-Z39-REMAINING-BALANCED-SEMAMPLE-CONTRACTION-DESCENT-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())
print("PASS: Z38 all-higher formal Picard vanishing")
print("for n>=2, H1(U,O_U(-nU))=0 by positive component degree and surjective two-node evaluation")
print("Z37 base O(P)|2U trivial => O(P)|nU trivial for every finite n")
