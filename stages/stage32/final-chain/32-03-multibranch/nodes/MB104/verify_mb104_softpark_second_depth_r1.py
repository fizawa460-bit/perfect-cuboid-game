#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
CERT=Path(__file__).with_name("MB104-SOFTPARK-SECOND-DEPTH-R1-CERTIFICATE.json")
def req(x,m):
 if not x: raise SystemExit("FAIL: "+m)
def main():
 c=json.loads(CERT.read_text())
 req(c["schema"]=="STAGE32_MB104_SOFTPARK_SECOND_DEPTH_R1_V1","schema")
 req(c["selection"]["advance_for_third_depth"]==["W4","W16"],"advance set")
 req(c["selection"]["reserve"]==["W13"],"reserve")
 req(c["selection"]["park"]==["W26","W31"],"park")
 # W4 retained numerical inputs
 sq=c["W4"]["pushdown_square_coefficients"]
 req([sq[k] for k in ["a1","a2","a3","b1","b2","b3","c"]]==[1344,1344,1376,1152,1152,736,1312],"W4 squares")
 req(all(v>0 and v%2==0 for v in sq.values()),"W4 square positivity/parity")
 req(c["W4"]["degree_coefficient"]==112,"W4 degree")
 # W16 conditional cutoff arithmetic
 for l in range(1,50):
  d=(336*l*l-224*l+16)-4*(112*l)
  req(d==336*l*l-672*l+16,f"W16 formula l={l}")
  if l>=2: req(d>0,f"W16 positivity l={l}")
 req((336-672+16)<0,"W16 l1 remains finite backend")
 # W26 coefficient no-go
 for n in range(1,100):
  a=n/100
  gap=336*a-168*(1+a)**2
  req(gap<0,f"W26 coefficient wall alpha={a}")
 req(c["W31"]["current_all_carrier_nonextendable_coherent_system"] is False,"W31 no intrinsic system")
 for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
 print("PASS STAGE32_MB104_SOFTPARK_SECOND_DEPTH_R1_V1")
 print("advance=W4,W16 reserve=W13 park=W26,W31")
 print("W16_conditional_cutoff=l>=2; finite_backend=l=1")
 print("no_credit")
if __name__=="__main__": main()
