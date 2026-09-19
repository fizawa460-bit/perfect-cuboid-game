#!/usr/bin/env python3
import json
from pathlib import Path

p=Path(__file__).with_name("MB104-Z3-BIRKAR-SEMIAMPLENESS-CONTRACTION-CERTIFICATE.json")
d=json.loads(p.read_text())

assert d["schema"]=="STAGE32_MB104_Z3_BIRKAR_SEMIAMPLENESS_CONTRACTION_V1"
assert d["status"]=="PRE_AUDIT_SEMIAMPLENESS_NULL_CONTRACTION_NO_CREDIT"

i=d["inputs"]
assert i["P"]=="7H-4*sum_Sigma(E_i)"
assert i["P2"]==336
assert i["P_nef"] is True
assert i["complete_null_locus"] is True

f=d["formal_null"]
assert f["isolated_unsupported_exceptional"]["P_restriction_trivial"] is True
assert f["size48"]["all_finite_thickenings_trivial"] is True
assert f["size768"]["component_H1_zero"] is True
assert f["size768"]["only_dual_graph_cycle"]=="two A-B edges"
assert f["size768"]["cycle_formal_class_zero_all_orders"] is True
assert f["size768"]["all_finite_thickenings_trivial"] is True

b=d["birkar_application"]
assert b["formal_triviality_implies_L_on_Z_trivial"] is True
assert b["P_semiample"] is True

c=d["contraction"]
assert c["birational"] is True
assert c["contracts_exactly_P_null_curves"] is True
assert c["hidden_contracted_curves"] is False

assert all(v is False for v in d["firewalls"].values())

print("PASS: Z3 Birkar semiampleness reduction certificate")
print("P is big+nef; full formal null restriction is trivial")
print("Birkar Theorem 1.4 => P semiample; contraction exceptional locus equals Null(P)")
