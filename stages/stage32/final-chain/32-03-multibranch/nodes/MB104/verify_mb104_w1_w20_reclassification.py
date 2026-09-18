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
CERT=Path(__file__).with_name("MB104-W1-W20-RECLASSIFICATION-CERTIFICATE.json")
LOCAL_LOCKS={
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-WIDE-SHALLOW-ROUND-A-20260918.md":"6d2ec2dfaf9fc1da08b13d7d51df70dd9391e13c",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-WIDE-SHALLOW-ROUND-B-20260918.md":"151a1c42554ea2294df87b01704a18f5ab2a76de",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-WIDE-SHALLOW-ROUND-C-20260918.md":"8925b009c04563f10a5600bbac32a46eeadf4b66",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-WIDE-SHALLOW-ROUND-D-20260918.md":"9a1d23075b54482f753fcd503b8a5cdb3e20fce9",
}
ARCHIVE_LOCKS={
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-PRIMITIVE-RANK.md":"6b973691df9c835d14ac388082111d202a07d8c7",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-NULL-UNION-COHOMOLOGY-WALL.md":"6d5fde6404a99e4541c9447d4111c7d7d14df9ec",
}
def main():
 for rel,sha in LOCAL_LOCKS.items():
  p=ROOT/rel; req(p.is_file(),"missing local source "+rel); req(blob(p)==sha,"local source drift "+rel)
 archive=archive_root_arg(); verify_archive_root(archive)
 for rel,sha in ARCHIVE_LOCKS.items():
  p=archive/rel; req(p.is_file(),"missing archive source "+rel); req(blob(p)==sha,"archive source drift "+rel)
 c=json.loads(CERT.read_text())
 req(c["schema"]=="STAGE32_MB104_WIDE_SCAN_W1_W20_RECLASSIFICATION_V1","schema")
 archive_locks={x["path"]:x for x in c["source_locks"] if "archive_head" in x}
 req(all(x["archive_head"]==ARCHIVE_HEAD for x in archive_locks.values()),"certificate archive heads")
 req(archive_locks["stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-NULL-UNION-COHOMOLOGY-WALL.md"]["blob_sha1"]=="6d5fde6404a99e4541c9447d4111c7d7d14df9ec","null-union archive lock")
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
 print("PASS STAGE32_MB104_W1_W20_RECLASSIFICATION_V2")
 print("archive_head="+ARCHIVE_HEAD)
 print("HARD=5 SOFT=15 PROMOTE=0 UNCLEAR=0")
 print("hard=W2,W8,W10,W14,W15")
if __name__=="__main__": main()
