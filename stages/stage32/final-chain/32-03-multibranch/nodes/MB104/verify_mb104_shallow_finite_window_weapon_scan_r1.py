#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-SHALLOW-FINITE-WINDOW-WEAPON-SCAN-R1-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_SHALLOW_FINITE_WINDOW_WEAPON_SCAN_R1_V1"
assert d["frontier"]=="000707000f0f"
assert len(d["routes"])==3
assert all(r["result"].startswith("NO_") for r in d["routes"])
assert d["deep_route_selected"] is False
assert d["r2_candidates"]==[
 "SEVERI_EQUIGENERIC_CODIMENSION",
 "JET_AMPLENESS_AFTER_NULL_CONTRACTION",
 "DEFORMATION_CONDUCTOR_TJURINA_SUPERABUNDANCE"
]
assert d["scale_hint"]["linear_gap"]=="112*l"
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_SHALLOW_FINITE_WINDOW_WEAPON_SCAN_R1_V1")
print("R1 no deep winner; rotate to Severi/jet/deformation shallow scan R2")
