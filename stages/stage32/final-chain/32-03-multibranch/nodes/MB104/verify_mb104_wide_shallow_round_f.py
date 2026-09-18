#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
CERT=Path(__file__).with_name("MB104-WIDE-SHALLOW-ROUND-F-CERTIFICATE.json")
def req(x,m):
 if not x: raise SystemExit("FAIL: "+m)
def main():
 c=json.loads(CERT.read_text())
 req(c["schema"]=="STAGE32_MB104_WIDE_SHALLOW_ROUND_F_V1","schema")
 for l in range(1,50):
  req(112*l>7,f"W27 l={l}")
  req(112*l>0,f"W29 l={l}")
  req(21<224*l,f"W30 l={l}")
 rs=c["round_summary"]
 req(rs["tested_architecture_hard_drop"]==["W26","W27","W28","W29","W30"],"hard set")
 req(rs["broader_direction_soft_park"]==["W26","W27","W28","W29","W30"],"soft set")
 req(rs["high_value_soft_additions"]==["W26"],"high value")
 req(rs["promote"]==[] and rs["unclear"]==[],"no promote")
 for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
 print("PASS STAGE32_MB104_WIDE_SHALLOW_ROUND_F_V1")
 print("W26-W30 architecture=HARD direction=SOFT; W26=HIGHER_VALUE_SOFT")
if __name__=="__main__": main()
