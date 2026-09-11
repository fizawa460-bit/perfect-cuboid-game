#!/usr/bin/env python3
from picard_pairing_scalar_producer import produce
I=[[1 if i==j else 0 for j in range(64)] for i in range(64)]
G=[[-1 if i==j else 0 for j in range(64)] for i in range(64)]
y=[0]*64
r=produce("synthetic-d32",32,"unit-regression",y,I,G,{"synthetic":True})
assert r["C2"]==0 and r["negative_hperp_square_N"]==64 and r["m"]==1
try:
    P=[row[:] for row in I]; P[0][0]=2
    produce("bad",32,"nonintegral", [1]+[0]*63,P,G,{})
except ValueError: pass
else: raise SystemExit("FAIL: nonintegral witness accepted")
print("PASS_32_02_SELECTED64_TO_HPERP_SCALAR_PRODUCER")
