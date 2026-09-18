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
 req(c["status"]=="SECOND_SCAN_COMPLETE_HIGH_VALUE_SOFT_PARK_NO_CREDIT","status")
 for l in range(1,100):
  disc=14*(112*l)-6*(336*l*l)
  req(disc==-224*l*(9*l-7) and disc<0,f"BG l={l}")
  req(-8 > -16*l,f"B=H rank2 slope witness l={l}")
  req(16 < 32*l,f"det cone witness l={l}")
 s=c["second_scan_result"]
 req(s["status"]=="NUMERICAL_DETERMINANT_CONE_NONEMPTY","second status")
 req(s["exact_witness_family"]["B"]=="H" and s["exact_witness_family"]["rank_r"]==2,"witness")
 d=s["decision"]
 req(d["tested_second_architecture_status"]=="HARD-DROP","second hard")
 req(d["broader_direction_status"]=="SOFT-PARK_HIGH_VALUE","broader soft")
 req(d["promote_to_deep"] is False,"no deep")
 for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
 print("PASS STAGE32_MB104_W31_LAZARSFELD_MUKAI_SECOND_SCAN_V1")
 print("uniform_BG_instability=true determinant_cone_witness=(B=H,r=2)")
 print("W31=HIGH_VALUE_SOFT_PARK no_deep no_credit")
if __name__=="__main__": main()
