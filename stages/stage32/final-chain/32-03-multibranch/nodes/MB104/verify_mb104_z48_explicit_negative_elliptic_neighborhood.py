#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

d=json.loads(Path(__file__).with_name("MB104-Z48-EXPLICIT-NEGATIVE-ELLIPTIC-NEIGHBORHOOD-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z48_EXPLICIT_NEGATIVE_ELLIPTIC_NEIGHBORHOOD_V1"
# Legendre j(lambda)=256(1-lambda+lambda^2)^3/(lambda^2(1-lambda)^2)
lam=Fraction(-1,1)
j=Fraction(256,1)*(1-lam+lam*lam)**3/(lam*lam*(1-lam)**2)
assert j==1728
assert d["representative"]["j"]==1728
assert d["normal_bundle"]["self_intersection"]==-4
assert d["normal_bundle"]["exact_class"]=="O_Q(-4p)"
assert d["result"]["z43_generic_graph_wall_strictly_refined"] is True
assert d["size48"]["complete_connected_germ_classified"] is False
assert d["size768"]["complete_connected_germ_classified"] is False
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_Z48_EXPLICIT_NEGATIVE_ELLIPTIC_NEIGHBORHOOD_V1")
print("j=1728 normal_bundle=O(-4p)")
print("next=MB104-Z49-EXPLICIT-PLUMBING-CANONICAL-COVER-PREFLIGHT")
