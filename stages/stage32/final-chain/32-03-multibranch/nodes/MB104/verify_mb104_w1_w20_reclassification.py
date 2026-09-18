#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6]
CERT=Path(__file__).with_name("MB104-W1-W20-RECLASSIFICATION-CERTIFICATE.json")
LOCKS={
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-WIDE-SHALLOW-ROUND-A-20260918.md":"6d2ec2dfaf9fc1da08b13d7d51df70dd9391e13c",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-WIDE-SHALLOW-ROUND-B-20260918.md":"151a1c42554ea2294df87b01704a18f5ab2a76de",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-WIDE-SHALLOW-ROUND-C-20260918.md":"8925b009c04563f10a5600bbac32a46eeadf4b66",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-WIDE-SHALLOW-ROUND-D-20260918.md":"9a1d23075b54482f753fcd503b8a5cdb3e20fce9",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-PRIMITIVE-RANK.md":"6b973691df9c835d14ac388082111d202a07d8c7",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-NULL-UNION-COHOMOLOGY-WALL.md":"260da960d17e9b756c2e27b056f33603e3b58d9d",
}
def blob(p):
 d=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(d)).encode()+b"\0"+d).hexdigest()
def req(x,m):
 if not x: raise SystemExit("FAIL: "+m)
def main():
 for rel,sha in LOCKS.items():
  p=ROOT/rel; req(p.is_file(),"missing "+rel); req(blob(p)==sha,"source drift "+rel)
 c=json.loads(CERT.read_text())
 req(c["schema"]=="STAGE32_MB104_WIDE_SCAN_W1_W20_RECLASSIFICATION_V1","schema")
 req(c["counts"]=={"HARD-DROP":5,"SOFT-PARK":15,"PROMOTE":0,"UNCLEAR":0},"counts")
 req(c["hard_drop"]==["W2","W8","W10","W14","W15"],"hard set")
 req(len(c["soft_park"])==15 and len(set(c["soft_park"]))==15,"soft set")
 req(set(c["hard_drop"]).isdisjoint(c["soft_park"]),"partition disjoint")
 req(set(c["hard_drop"]+c["soft_park"])=={f"W{i}" for i in range(1,21)},"W1-W20 coverage")
 req(c["promote"]==[] and c["unclear"]==[],"no promote/unclear")
 w15=c["w15_resolution"]
 req(w15["primitive_rank_retained"]=="h0(A)=124 and explicit F|Q0 !=0","W15 primitive")
 req("rank 1" in w15["consequence"],"W15 rank")
 for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
 print("PASS STAGE32_MB104_W1_W20_RECLASSIFICATION_V1")
 print("HARD=5 SOFT=15 PROMOTE=0 UNCLEAR=0")
 print("hard=W2,W8,W10,W14,W15")
if __name__=="__main__": main()
