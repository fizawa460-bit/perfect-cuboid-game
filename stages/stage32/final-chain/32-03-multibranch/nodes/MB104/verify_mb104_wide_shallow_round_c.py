#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6]
CERT=Path(__file__).with_name("MB104-WIDE-SHALLOW-ROUND-C-CERTIFICATE.json")
LOCKS={
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-W14-000707-DEGREE7-RESTRICTION-PREFLIGHT-CERTIFICATE.json":"b2f3192462d745e98eabe20aec94c69cd273e12d",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-PRIMITIVE-RANK.md":"6b973691df9c835d14ac388082111d202a07d8c7",
}
def blob(p):
 d=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(d)).encode()+b"\0"+d).hexdigest()
def req(x,m):
 if not x: raise SystemExit("FAIL: "+m)
def main():
 for rel,sha in LOCKS.items():
  p=ROOT/rel; req(p.is_file(),"missing "+rel); req(blob(p)==sha,"source drift "+rel)
 c=json.loads(CERT.read_text())
 req(c["status"]=="ROUND_C_COMPLETE_ALL_DROPPED_NO_CREDIT","status")
 w=c["results"]["W14_ZERO_QUARTIC_RESTRICTION"]
 req(w["disposition"]=="DROP_ALREADY_RETAINED","W14 disposition")
 req(w["retained_result"]["h0_A"]==124 and w["retained_result"]["char0_jet_rank"]==220,"retained exact rank")
 req(w["retained_result"]["q0_q1_nonfixed_all_l"] is True,"nonfixed all l")
 rs=c["round_summary"]
 req(rs["drop"]==["W7","W9","W12","W13","W14"],"all drops")
 req(rs["pass_to_second_scan"]==[] and rs["deep_candidate"] is False,"no survivor")
 for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
 print("PASS STAGE32_MB104_WIDE_SHALLOW_ROUND_C_CORRECTED_V1")
 print("W7=W9=W12=W13=W14=DROP no_second_scan no_credit")
if __name__=="__main__": main()
