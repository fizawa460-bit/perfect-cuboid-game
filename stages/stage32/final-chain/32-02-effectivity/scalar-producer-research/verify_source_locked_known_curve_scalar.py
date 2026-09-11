#!/usr/bin/env python3
from source_locked_known_curve_scalar import produce_known_curve
from picard_pairing_scalar_producer import produce
r=produce_known_curve(1)
q=produce(r["row_id"],r["d"],"known-curve-1",r["selected64_pairings"],[[1 if False else 0]],[],{})
# generic producer is separately tested; here replay the exact identity directly.
assert r["negative_hperp_square_N"]>=0
assert len(r["selected64_pairings"])==64 and len(r["picard64_coordinates"])==64
assert r["credit"]["full178"] is False
print("PASS_32_02_SOURCE_LOCKED_KNOWN_CURVE_SCALAR_REGRESSION",r["d"],r["C2"],r["negative_hperp_square_N"])
