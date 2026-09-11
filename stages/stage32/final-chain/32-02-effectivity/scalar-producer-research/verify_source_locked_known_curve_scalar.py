#!/usr/bin/env python3
from source_locked_known_curve_scalar import produce_known_curve
r=produce_known_curve(1)
assert len(r["selected64_pairings"])==64 and len(r["picard64_coordinates"])==64
assert 16*r["negative_hperp_square_N"]==r["m"]*r["m"]*(r["d"]*r["d"]-16*r["C2"])
assert r["negative_hperp_square_N"]>=0
assert r["credit"]=={"regression_only":True,"main":False,"full178":False,"effectivity_final":False,"merge":False}
print("PASS_32_02_SOURCE_LOCKED_KNOWN_CURVE_SCALAR_REGRESSION",r["d"],r["C2"],r["negative_hperp_square_N"])
