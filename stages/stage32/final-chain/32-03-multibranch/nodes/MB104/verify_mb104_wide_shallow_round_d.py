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
CERT=Path(__file__).with_name("MB104-WIDE-SHALLOW-ROUND-D-CERTIFICATE.json")
ARCHIVE_LOCKS={
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/A1-CONDUCTOR-BRANCH-DELTA-WALL.md":"a4de57f430aea249300c589aeeeaa3dbe67d5006",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-JOINT-PAIR-BIRATIONALITY-CERTIFICATE.json":"8fb4578029037c088c17b6cfb219955c9d0dc4d6",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BALANCED16-STATIC-LANDING-AVOIDANCE-WALL.md":"71f52716b9cbdd0218aa73a138837f3b3891f412",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ADAPTIVE-CANCELLATION-JET-BUDGET.md":"0cbe49c719362fcfc3eb0492833e02a551dcd1fe",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-SHEET-SELECTED-FIBER-ABEL-JACOBI.md":"76ef6c5638b9a601fd01ca28bb01531d7279c180",
}
def main():
 archive=archive_root_arg(); verify_archive_root(archive)
 for rel,sha in ARCHIVE_LOCKS.items():
  p=archive/rel; req(p.is_file(),"missing archive source "+rel); req(blob(p)==sha,"archive source drift "+rel)
 c=json.loads(CERT.read_text())
 req(c["schema"]=="STAGE32_MB104_WIDE_SHALLOW_ROUND_D_V1","schema")
 req(all(x.get("archive_head")==ARCHIVE_HEAD for x in c["historical_sources"]),"certificate archive heads")
 for l in range(1,20):
  disc=336*l*l-224*l-28
  req(disc>0,f"W16 discriminant l={l}")
 pairs=c["results"]["W17_SUPPORT_STABILIZER_DICHOTOMY"]["supported_node_pairs"]
 flat=[x for p in pairs for x in p]
 req(sorted(flat)==[0,1,2,3,8,9,10,11,24,25,26,32,33,34],"W17 support pairs")
 req(c["results"]["W17_SUPPORT_STABILIZER_DICHOTOMY"]["fixed_supported_nodes"]==[],"W17 no fixed support")
 for l in range(1,20):
  d=112*l; m=8*l
  req(7*d-14*6*m==112*l,f"W18 raw slack l={l}")
  req(112*l-49>0,f"W18 GL slack l={l}")
 for l in range(1,20):
  req(7*112*l==784*l,f"W19 weight l={l}")
  req(112*l<784*l,f"W19 optimistic slack l={l}")
 for l in range(1,20):
  req(112*l>=6,f"W20 RR room l={l}")
 rs=c["round_summary"]
 req(rs["drop"]==["W16","W17","W18","W19","W20"],"all drops")
 req(rs["pass_to_second_scan"]==[] and rs["deep_candidate"] is False,"no survivor")
 req(rs["archive_semantic_precheck_performed"] is True,"archive precheck")
 for k,v in c["credit_firewall"].items(): req(v is False,"credit "+k)
 print("PASS STAGE32_MB104_WIDE_SHALLOW_ROUND_D_V2")
 print("archive_head="+ARCHIVE_HEAD)
 print("W16=W17=W18=W19=W20=DROP")
 print("next=NEW_WIDE_ROUND_ONLY no_credit")
if __name__=="__main__": main()
