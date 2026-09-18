#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
CERT=Path(__file__).with_name("MB104-W31-LAZARSFELD-MUKAI-PREFLIGHT-CERTIFICATE.json")
def req(x,m):
 if not x: raise SystemExit("FAIL: "+m)
def main():
 c=json.loads(CERT.read_text())
 req(c["schema"]=="STAGE32_MB104_W31_LAZARSFELD_MUKAI_PREFLIGHT_V1","schema")
 req(c["construction"]["rank"]==7,"rank")
 for l in range(1,100):
  c2=112*l
  c1sq=336*l*l
  disc=14*c2-6*c1sq
  req(disc==-224*l*(9*l-7),f"disc identity l={l}")
  req(disc<0,f"disc negative l={l}")
  req(112*l//7==16*l,f"slope l={l}")
 req(c["discriminant"]["negative_for_all_l_ge_1"] is True,"uniform negativity")
 req(c["second_scan_only"]["no_full_HN_enumeration_yet"] is True,"no deep")
 for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
 print("PASS STAGE32_MB104_W31_LAZARSFELD_MUKAI_PREFLIGHT_V1")
 print("rank=7 c1=D_l c2=112l Delta=-224l(9l-7)<0")
 print("W31=PROMOTE_TO_SECOND_SCAN no_credit")
if __name__=="__main__": main()
