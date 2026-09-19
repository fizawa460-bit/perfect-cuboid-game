#!/usr/bin/env python3
import json
from pathlib import Path

d=json.loads(Path(__file__).with_name(
 "MB104-Z40-P-NULL-PICARD64-FINITE-ENUMERATION-PREFLIGHT-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z40_P_NULL_PICARD64_FINITE_ENUMERATION_PREFLIGHT_V1"
assert d["degrees"]==[4,8,12,16,20]
assert len(d["shells"])==17

expected=[]
for e in [4,8,12,16,20]:
    for pa in range(20):
        r2=2*pa-2-e
        if 64*r2 <= -3*e*e:
            expected.append({
              "degree":e,
              "arithmetic_genus":pa,
              "R2":r2,
              "close_vector_norm":16*e*e-256*r2
            })
assert d["shells"]==expected

c=d["close_vector"]
assert c["base"]=="b_e=16*B_e-e*H"
assert c["lattice"]=="16*Hperp"
assert c["reconstruction"]=="R=B_e-x/16"
assert c["norm_formula"]=="N=16*e^2-256*R^2"

a=d["node_adapter"]
assert a["compact_nodes"]==a["stoll_nodes"]==48
assert a["require_exact_projective_coordinate_bijection"] is True
assert a["assume_index_order_equal"] is False

z=d["conclusion"]
assert z["shell_count"]==17
assert z["exact_finite_enumeration_interface_available"] is True
assert z["enumeration_executed"] is False
assert z["complete_null_locus_classified"] is False
assert d["active_leaf"]=="MB104-Z40-P-NULL-PICARD64-FINITE-ENUMERATION"
assert all(v is False for v in d["credit_firewall"].values())

print("PASS: Z40 Picard64 finite-enumeration preflight")
print("17 exact close-vector shells across degrees 4,8,12,16,20")
print("support exceptional indices must be matched by exact projective coordinates, never assumed")
print("enumeration remains the active leaf")
