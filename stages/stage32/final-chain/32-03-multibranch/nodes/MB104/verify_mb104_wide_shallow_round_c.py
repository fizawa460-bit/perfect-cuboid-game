#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6]
ARCHIVE_HEAD="ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11"
def blob(p):
 d=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(d)).encode()+b"\0"+d).hexdigest()
def req(x,m):
 if not x: raise SystemExit("FAIL: "+m)
def archive_root_arg():
 ap=argparse.ArgumentParser()
 ap.add_argument("--archive-root", type=Path, required=True)
 return ap.parse_args().archive_root.resolve()
def verify_archive_root(root):
 req(root.is_dir(),"archive root missing")
 try:
  head=subprocess.check_output(["git","-C",str(root),"rev-parse","HEAD"],text=True,stderr=subprocess.STDOUT).strip()
 except (subprocess.CalledProcessError,FileNotFoundError) as e:
  raise SystemExit("FAIL: archive root is not a readable git checkout") from e
 req(head==ARCHIVE_HEAD,"archive head mismatch")
CERT=Path(__file__).with_name("MB104-WIDE-SHALLOW-ROUND-C-CERTIFICATE.json")
LOCAL_LOCKS={
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-W14-000707-DEGREE7-RESTRICTION-PREFLIGHT-CERTIFICATE.json":"b2f3192462d745e98eabe20aec94c69cd273e12d",
}
ARCHIVE_LOCKS={
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-PRIMITIVE-RANK.md":"6b973691df9c835d14ac388082111d202a07d8c7",
}
def main():
 for rel,sha in LOCAL_LOCKS.items():
  p=ROOT/rel; req(p.is_file(),"missing local source "+rel); req(blob(p)==sha,"local source drift "+rel)
 archive=archive_root_arg(); verify_archive_root(archive)
 for rel,sha in ARCHIVE_LOCKS.items():
  p=archive/rel; req(p.is_file(),"missing archive source "+rel); req(blob(p)==sha,"archive source drift "+rel)
 c=json.loads(CERT.read_text())
 req(c["status"]=="ROUND_C_COMPLETE_ALL_DROPPED_NO_CREDIT","status")
 w=c["results"]["W14_ZERO_QUARTIC_RESTRICTION"]
 req(w["disposition"]=="DROP_ALREADY_RETAINED","W14 disposition")
 req(w["retained_result"]["archive_head"]==ARCHIVE_HEAD,"W14 archive head")
 req(w["retained_result"]["h0_A"]==124 and w["retained_result"]["char0_jet_rank"]==220,"retained exact rank")
 req(w["retained_result"]["q0_q1_nonfixed_all_l"] is True,"nonfixed all l")
 rs=c["round_summary"]
 req(rs["drop"]==["W7","W9","W12","W13","W14"],"all drops")
 req(rs["pass_to_second_scan"]==[] and rs["deep_candidate"] is False,"no survivor")
 for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
 print("PASS STAGE32_MB104_WIDE_SHALLOW_ROUND_C_CORRECTED_V2")
 print("archive_head="+ARCHIVE_HEAD)
 print("W7=W9=W12=W13=W14=DROP no_second_scan no_credit")
if __name__=="__main__": main()
