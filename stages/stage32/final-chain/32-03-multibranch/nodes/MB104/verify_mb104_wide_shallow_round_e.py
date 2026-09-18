#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
CERT=Path(__file__).with_name("MB104-WIDE-SHALLOW-ROUND-E-CERTIFICATE.json")
def req(x,m):
 if not x: raise SystemExit("FAIL: "+m)
def main():
 c=json.loads(CERT.read_text())
 req(c["schema"]=="STAGE32_MB104_WIDE_SHALLOW_ROUND_E_V1","schema")
 for l in range(1,50):
  c2j=80+224*l+1008*l*l
  delta=168*l*l+56*l
  req(c2j>delta,f"W21 l={l}")
  req(-112*l<0,f"W22 l={l}")
  req(1 <= (28*l-1)**2 and 1 <= (56*l-1)**2,f"W23 l={l}")
  req(336*l*l+112*l == 2*delta,f"W24 l={l}")
  ncrit=1008*l*l+224*l+80
  req(ncrit>delta,f"W25 l={l}")
 rs=c["round_summary"]
 req(rs["tested_architecture_hard_drop"]==["W21","W22","W23","W24","W25"],"hard set")
 req(rs["broader_direction_soft_park"]==["W21","W22","W23","W24","W25"],"soft set")
 req(rs["promote"]==[] and rs["unclear"]==[],"no promote")
 for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
 print("PASS STAGE32_MB104_WIDE_SHALLOW_ROUND_E_V1")
 print("W21-W25 architecture=HARD direction=SOFT PROMOTE=none")
if __name__=="__main__": main()
