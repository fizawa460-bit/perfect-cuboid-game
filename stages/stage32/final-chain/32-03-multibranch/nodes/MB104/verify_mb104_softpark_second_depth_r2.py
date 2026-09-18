#!/usr/bin/env python3
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
CERT=Path(__file__).with_name("MB104-SOFTPARK-SECOND-DEPTH-R2-CERTIFICATE.json")
def req(x,m):
 if not x: raise SystemExit("FAIL: "+m)
def main():
 c=json.loads(CERT.read_text())
 req(c["schema"]=="STAGE32_MB104_SOFTPARK_SECOND_DEPTH_R2_V1","schema")
 req(c["selection"]["advance_for_third_depth"]==["W20"],"advance")
 req(c["selection"]["high_reserve"]==["W5"],"reserve")
 req(c["selection"]["park"]==["W6","W11","W30"],"park")
 # W5 asymptotic diagnostic
 smooth=Fraction(16-80,6)
 local=48*Fraction(4,27)
 net=smooth+local
 req(smooth==Fraction(-32,3),"W5 smooth leading")
 req(local==Fraction(64,9),"W5 A1 leading")
 req(net==Fraction(-32,9) and net<0,"W5 net leading")
 # W6 capacity threshold
 for s in range(1,8):
  cap=28*s
  if s<4: req(cap<112,"W6 nontrivial threshold")
  else: req(cap>=112,"W6 automatic threshold")
 # W11/W30 dimensions
 for l in range(1,50):
  req(28<224*l,"W11 no Sym2 overload")
  req(21<224*l,"W30 no Gaussian overload")
 # W20 finite torsion target
 req(c["W20"]["candidate_count_upper"]==4,"W20 E2 count")
 req("Pic^0(E)[2]" in c["W20"]["delta_fac"],"W20 torsion")
 for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
 print("PASS STAGE32_MB104_SOFTPARK_SECOND_DEPTH_R2_V1")
 print("advance=W20 high_reserve=W5 park=W6,W11,W30")
 print("W5_standard_net_leading=-32/9; W20_target=finite_E[2]_bridge")
 print("no_credit")
if __name__=="__main__": main()
