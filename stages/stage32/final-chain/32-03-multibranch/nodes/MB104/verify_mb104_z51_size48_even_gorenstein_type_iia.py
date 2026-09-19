#!/usr/bin/env python3
import json
from pathlib import Path

d=json.loads(Path(__file__).with_name("MB104-Z51-SIZE48-EVEN-GORENSTEIN-TYPE-IIA-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z51_SIZE48_EVEN_GORENSTEIN_TYPE_IIA_V1"
assert d["input"]["fundamental_genus"]==2
assert d["input"]["fundamental_cycle_square"]==-2
assert d["input"]["canonical_cycle_coefficients"]==[2]*7
assert d["konno"]["arithmetic_genus"]==2
assert d["konno"]["geometric_genus"]==3
assert d["konno"]["type"]=="ii.a"
assert d["konno"]["fixed_rdp_chain"]=="A5"

# F=Z+Gamma on the -2 seven-chain.
F=[1,2,2,2,2,2,1]
F2=-2*sum(x*x for x in F)+2*sum(F[i]*F[i+1] for i in range(6))
assert F2==-4
assert d["konno"]["multiplicity"]==4
assert d["konno"]["embedding_dimension"]==4
assert d["consequence"]["embedding_codimension"]==2
assert d["consequence"]["local_complete_intersection"] is True
assert d["consequence"]["explicit_equations_known"] is False
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_Z51_SIZE48_EVEN_GORENSTEIN_TYPE_IIA_V1")
print("pf=pa=2 pg=3 type=ii.a mult=4 embdim=4 CI=codim2")
