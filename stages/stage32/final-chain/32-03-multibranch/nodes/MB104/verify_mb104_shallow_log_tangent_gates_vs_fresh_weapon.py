#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-SHALLOW-LOG-TANGENT-GATES-VS-FRESH-WEAPON-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_SHALLOW_LOG_TANGENT_GATES_VS_FRESH_WEAPON_V1"
L=d["log_tangent"]; Y=d["fresh_contraction"]
assert L["branch_excess_linear_bound_known"] is False
assert L["six_fibration_branch_multiplicity_bound_controls_B"] is False
assert L["semistability_source_valid"] is False
assert L["route_parked"] is True
assert Y["KY2"]=="112/3"
assert Y["e_Y_reg"]==16
assert Y["formal_difference"]=="64/3"
assert Y["smooth_resolution_s2"]==-64
assert Y["Y_non_lc_index3"] is True
assert Y["smooth_bogomolov_directly_applicable"] is False
assert d["next_portfolio"]==[
 "ELLIPTIC_LINEAR_SERIES_SYZYGY_RECEIVER",
 "SINGULAR_PLURICANONICAL_LOW_GENUS_THEOREM",
 "FINITE_RECEIVER_ELIMINATION_GEOMETRY"
]
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_SHALLOW_LOG_TANGENT_GATES_VS_FRESH_WEAPON_V1")
print("log tangent parked; rotate to fresh three-way portfolio")
