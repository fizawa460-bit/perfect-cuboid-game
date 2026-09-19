#!/usr/bin/env python3
import json
from pathlib import Path
import sympy as sp

p=Path(__file__).with_name("MB104-Z5P-000707-E4-INVARIANT-HALF-FIBER-RATIO-DESCENT-NOGO-CERTIFICATE.json")
d=json.loads(p.read_text())

assert d["schema"]=="STAGE32_MB104_Z5P_000707_E4_INVARIANT_HALF_FIBER_RATIO_DESCENT_NOGO_V1"
assert d["status"]=="PRE_AUDIT_EXACT_DESCENT_NOGO_NO_CREDIT"
assert d["support"]["mask"]=="000707000f0f"

i=sp.I
dz,ez,dw,ew=sp.symbols("dz ez dw ew")
A=dz*dw; B=ez*ew; U=ez*dw; V=dz*ew
C=A+B
W1=U+V
W2=i*(U-V)
W3=A-B
h=sp.expand(C-W1-W2-i*W3)
rhs=sp.expand((1-i)*(dz-i*ez)*(dw-ew))
assert sp.simplify(h-rhs)==0

chars=d["G_characters"]
assert chars["T"]==[1,1]
assert chars["Tprime"]==[1,1]
assert chars["R"]==[-1,-1]
for ch in chars.values():
    assert ch[0]==ch[1]

r=d["ratio"]
assert r["diagonal_G_invariant"] is True
assert r["descends_to_box_function_field"] is True
assert r["distinguished_conductor_obstruction"] is False

assert all(v is False for v in d["firewalls"].values())

print("PASS: Z5' invariant half-fiber ratio descent no-go")
print("h=(1-i)(d_z-i e_z)(d_w-e_w)")
print("both half-fiber factors have the same G-character, so their ratio descends")
