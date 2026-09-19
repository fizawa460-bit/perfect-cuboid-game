#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-SHALLOW-FRESH-WEAPON-PORTFOLIO-R3-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_SHALLOW_FRESH_WEAPON_PORTFOLIO_R3_V1"
assert d["routeA"]["sym2_dimension"]==28
assert d["routeA"]["h0_L2"]=="224*l"
assert d["routeA"]["finite_l_obstruction_found"] is False
assert d["routeB"]["smooth_resolution_second_segre"]==-64
assert d["routeB"]["Y_non_lc_index3"] is True
assert d["routeB"]["source_valid_adapter"] is False
assert d["routeC"]["bounded_receiver_independent_of_l_found"] is False
assert d["deep_winner"] is False
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_SHALLOW_FRESH_WEAPON_PORTFOLIO_R3_V1")
print("R3 no deep winner; rotate again")
