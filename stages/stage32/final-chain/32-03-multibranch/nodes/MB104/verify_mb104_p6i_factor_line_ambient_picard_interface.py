#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ARCHIVE_HEAD="ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11"
BASE="stages/stage32/final-chain/32-03-multibranch/nodes/MB104"
LOCKS={
 f"{BASE}/BEAUVILLE-PRODUCT-COVER-SOURCE-NOTE.md":"974c6cfecb6e4141615583841a0c90146ad2b4a6",
 f"{BASE}/GENUS1-SPAN5-BALANCED16-000707-E2-EXTERNAL-PRODUCT-PICARD-REDUCTION.md":"dc2def9e4d0148aa3146a034a2ce0ef331206a29",
 f"{BASE}/GENUS1-SPAN5-BALANCED16-000707-E2-HALF-HYPERPLANE-FACTORIZATION.md":"ba7ea7a7e21f0e4ca5d8b96c3dac1dbafbbddff6",
 f"{BASE}/GENUS1-SPAN5-BALANCED16-000707-ONE-FACTOR-HALF-BRANCH-CLASS.md":"e22de5a6f4be163268e699cde03d37e1e564d43b",
 f"{BASE}/STOLL-TESTA-G2-ISOTRIVIAL-FIBRATION-SOURCE-NOTE.md":"b71225ac859eef5afefeebd019a97c403ed27655",
}
P6H=f"{BASE}/MB104-P6H-FULL-G-TWO-FACTOR-CHARACTER-LINE-CERTIFICATE.json"
P6H_BLOB="5c9b3eafed5e55d0a360870722cea7ea81758745"

def req(c:bool,m:str)->None:
 if not c: raise SystemExit('FAIL: '+m)

def blob(p:Path)->str:
 b=p.read_bytes()
 return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def main()->None:
 ap=argparse.ArgumentParser()
 ap.add_argument('--archive-root',required=True)
 a=ap.parse_args()
 ar=Path(a.archive_root)
 head=subprocess.check_output(['git','-C',str(ar),'rev-parse','HEAD'],text=True).strip()
 req(head==ARCHIVE_HEAD,'archive head')
 for rel,sha in LOCKS.items():
  p=ar/rel
  req(p.is_file(),'missing '+rel)
  req(blob(p)==sha,'blob '+rel)
 root=Path(__file__).resolve().parents[6]
 req(blob(root/P6H)==P6H_BLOB,'P6H certificate blob')
 c=json.loads(Path(__file__).with_name('MB104-P6I-FACTOR-LINE-AMBIENT-PICARD-INTERFACE-CERTIFICATE.json').read_text())
 f=c['findings']
 req(f['exact_ambient_factor_class_adapter_found'] is False,'must not invent factor class adapter')
 req(f['repository_wide_absence_claimed'] is False,'bounded search only')
 req(c['disposition']=='PARK_P6I_AT_MISSING_AMBIENT_FACTOR_PENCIL_ADAPTER','disposition')
 req(c['next_leaf']=='MB104-P6J-FULL-G-PRODUCT-CORRESPONDENCE-CENTRALIZER','next leaf')
 req(all(v is False for v in c['firewalls'].values()),'credit firewall')
 print('PASS: P6I ambient Picard interface wall')
 print('P6H common factor line retained; no ambient F_i adapter guessed')
 print('next: P6J full-G product correspondence centralizer')

if __name__=='__main__':
 main()
