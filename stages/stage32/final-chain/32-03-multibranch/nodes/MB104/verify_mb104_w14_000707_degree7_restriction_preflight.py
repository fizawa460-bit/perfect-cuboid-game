#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6]
CERT=Path(__file__).with_name("MB104-W14-000707-DEGREE7-RESTRICTION-PREFLIGHT-CERTIFICATE.json")
LOCKS={
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-PRIMITIVE-RANK.md":"6b973691df9c835d14ac388082111d202a07d8c7",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_000707_primitive_rank.py":"51e3ab3df3dbdf30305085f07fdbb7deca0d27cf",
}
def blob(p):
 d=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(d)).encode()+b"\0"+d).hexdigest()
def req(x,m):
 if not x: raise SystemExit("FAIL: "+m)
def main():
 for rel,sha in LOCKS.items():
  p=ROOT/rel; req(p.is_file(),"missing "+rel); req(blob(p)==sha,"source drift "+rel)
 c=json.loads(CERT.read_text())
 req(c["status"]=="SUPERSEDED_BY_RETAINED_PRIMITIVE_RANK_DROP_NO_CREDIT","status")
 r=c["retained_archive_resolution"]["exact_result"]
 req(r["h0_A"]==124 and r["h1_A"]==4 and r["char0_jet_rank"]==220,"exact primitive rank")
 req(r["q0_restriction_nonzero"] is True and r["q0_q1_nonfixed_all_l"] is True,"nonfixedness")
 req(c["decision"]["disposition"]=="DROP_ALREADY_RETAINED","drop")
 req(c["decision"]["deep_candidate"] is False and c["decision"]["second_scan_required"] is False,"routing")
 for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
 print("PASS STAGE32_MB104_W14_RETAINED_PRIMITIVE_RANK_CORRECTION_V1")
 print("h0(A)=124 jet_rank=220 Q0,Q1_nonfixed_all_l W14=DROP no_credit")
if __name__=="__main__": main()
