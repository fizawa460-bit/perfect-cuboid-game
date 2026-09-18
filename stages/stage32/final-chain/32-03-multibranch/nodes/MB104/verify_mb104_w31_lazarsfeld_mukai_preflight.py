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
 req(c["status"]=="ARCHITECTURE_HARD_DROP_TAUTOLOGICAL_DESTABILIZER_NO_CREDIT","status")
 for l in range(1,100):
  disc=14*(112*l)-6*(336*l*l)
  req(disc==-224*l*(9*l-7) and disc<0,f"disc l={l}")
  req(112*l-16 > 16*l,f"explicit destabilizer slope l={l}")
 r=c["structural_resolution"]
 req(r["dual_extension"]=="0 -> O_S(D_l-H) -> E -> M_H^vee -> 0","dual extension")
 d=r["decision"]
 req(d["tested_architecture_status"]=="HARD-DROP","hard")
 req(d["broader_direction_status"]=="SOFT-PARK","soft")
 req(d["promote_to_deep"] is False,"no deep")
 for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
 print("PASS STAGE32_MB104_W31_LM_TAUTOLOGICAL_DESTABILIZER_V1")
 print("explicit_subline=O(D_l-H) slope=112l-16 > 16l")
 print("W31 architecture=HARD broader=SOFT no_credit")
if __name__=="__main__": main()
