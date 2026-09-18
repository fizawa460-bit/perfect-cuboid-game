#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6]
CERT=Path(__file__).with_name("MB104-WIDE-SHALLOW-ROUND-C-CERTIFICATE.json")
LOCKS={
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-W14-000707-DEGREE7-RESTRICTION-PREFLIGHT-CERTIFICATE.json":"9aaa1b73638b7311d8a1d95c64813e52452f2ecc",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_w14_000707_degree7_restriction_preflight.py":"2663e199fc86faac8426bc6619000c8c8a889914",
}
def blob(p):
 d=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(d)).encode()+b"\0"+d).hexdigest()
def req(x,m):
 if not x: raise SystemExit("FAIL: "+m)
def main():
 for rel,sha in LOCKS.items():
  p=ROOT/rel; req(p.is_file(),"missing "+rel); req(blob(p)==sha,"source drift "+rel)
 c=json.loads(CERT.read_text())
 req(c["schema"]=="STAGE32_MB104_WIDE_SHALLOW_ROUND_C_V1","schema")
 # W7 exact positive slack replay for a bounded panel.
 for n in range(2,9):
  for l in range(1,9):
   num=224*n*n +112*n*(n-1)*l +336*(n-1)*(2*n+1)*l*l
   req(num>0,f"W7 n={n} l={l}")
 w14=c["results"]["W14_ZERO_QUARTIC_RESTRICTION"]
 req(w14["p1097"]=={"jet_rank":220,"q0":221,"q1":221,"both":221},"W14 ranks")
 req(w14["char0_jet_rank_options"]==[220,221],"W14 rank window")
 rs=c["round_summary"]
 req(rs["drop"]==["W7","W9","W12","W13"],"drops")
 req(rs["pass_to_second_scan"]==["W14"],"survivor")
 req(rs["deep_candidate"] is False,"no deep")
 for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
 print("PASS STAGE32_MB104_WIDE_SHALLOW_ROUND_C_V1")
 print("W7=W9=W12=W13=DROP W14=SECOND_SCAN")
 print("char0_jet_rank={220,221} no_credit")
if __name__=="__main__": main()
