#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
CERT=Path(__file__).with_name("MB104-SOFTPARK-SECOND-DEPTH-R4-CERTIFICATE.json")
def req(x,m):
 if not x: raise SystemExit("FAIL: "+m)
def main():
 c=json.loads(CERT.read_text())
 req(c["schema"]=="STAGE32_MB104_SOFTPARK_SECOND_DEPTH_R4_V1","schema")
 req(c["selection"]["advance_for_third_depth"]==[],"no advance")
 req(c["selection"]["park"]==["W1","W21","W22","W24","W27","W28"],"park set")
 for l in range(1,100):
  Delta=168*l*l+56*l
  full=(336*l*l-224*l+16)-4*Delta
  req(full==-336*l*l-448*l+16 and full<0,"W1 full discriminant")
  c2=336*l*l+112*l+80
  req(c2-Delta==168*l*l+56*l+80 and c2>Delta,"W21 rank2 capacity")
  req(112*l-7>0,"W27 residual obstruction")
  support_delta=112*l-14
  rem=Delta-support_delta
  req(rem==168*l*l-56*l+14 and rem>0,"W24 remainder")
 req(c["W22"]["cosection_localizes_virtual_class_not_actual_moduli"] is True,"W22 scope")
 req(c["W28"]["proper_canonical_subcluster_required"] is True,"W28/W16 absorption")
 for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
 print("PASS STAGE32_MB104_SOFTPARK_SECOND_DEPTH_R4_V1")
 print("advance=none park=W1,W21,W22,W24,W27,W28")
 print("cumulative_advance=W4,W16,W20; high_reserve=W5")
 print("next=W3,W7,W9,W12,W25")
 print("no_credit")
if __name__=="__main__": main()
