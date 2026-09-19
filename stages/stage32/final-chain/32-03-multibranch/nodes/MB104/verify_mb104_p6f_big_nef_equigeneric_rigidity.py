#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ARCHIVE_HEAD="ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11"
BASE="stages/stage32/final-chain/32-03-multibranch/nodes/MB104"
ARCHIVE_LOCKS={
 f"{BASE}/LU-MIYAOKA-GENUS1-SINGULARITY-COUNT-SOURCE-NOTE.md":"82e247159d736f92aa1382a469fa1d46a81dbae0",
 f"{BASE}/MIYAOKA2008-ORBIBUNDLE-GENUS1-WALL.md":"f59898039325b8a919f195ed9b0a491885e8232d",
}
P6E=f"{BASE}/MB104-P6E-HOSTILE-SURVIVOR-NEF-CERTIFICATE.json"
P6E_BLOB="9579b0c2b909310b426cd4a1539b3d4c2ede0248"

def req(c: bool,m: str)->None:
 if not c: raise SystemExit('FAIL: '+m)

def blob(p: Path)->str:
 b=p.read_bytes()
 return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def main()->None:
 ap=argparse.ArgumentParser()
 ap.add_argument('--archive-root',required=True)
 a=ap.parse_args()
 ar=Path(a.archive_root)
 head=subprocess.check_output(['git','-C',str(ar),'rev-parse','HEAD'],text=True).strip()
 req(head==ARCHIVE_HEAD,'archive head')
 for rel,sha in ARCHIVE_LOCKS.items():
  p=ar/rel
  req(p.is_file(),'missing '+rel)
  req(blob(p)==sha,'blob '+rel)
 root=Path(__file__).resolve().parents[6]
 req(blob(root/P6E)==P6E_BLOB,'P6E certificate blob')
 c=json.loads(Path(__file__).with_name('MB104-P6F-BIG-NEF-EQUIGENERIC-RIGIDITY-CERTIFICATE.json').read_text())
 req(c['hypothetical_carrier']['normalization_genus']==1,'genus')
 req(c['hypothetical_carrier']['K_dot_C_l_coefficient']==112,'K.C coefficient')
 req(c['dedieu_sernesi']['normalization_line_bundle_degree_l_coefficient']==-112,'negative degree')
 req(c['dedieu_sernesi']['normalization_h0']==0,'h0')
 req(c['dedieu_sernesi']['equigeneric_reduced_tangent_cone_zero'] is True,'equigeneric tangent cone')
 req(c['dedieu_sernesi']['equisingular_tangent_space_dimension']==0,'equisingular tangent')
 req(c['surface']['K2'] < c['surface']['c2'],'Miyaoka uniform-degree hypothesis must fail')
 req(c['conclusion']=='HYPOTHETICAL_GENUS1_CARRIER_EQUIGENERICALLY_ISOLATED_NOT_EXCLUDED','conclusion')
 req(all(v is False for v in c['firewalls'].values()),'firewall')
 print('PASS: P6F genus-one equigeneric rigidity gate')
 print('deg(omega_E tensor phi^*omega_S^-1) = -112*l < 0')
 print('equigeneric reduced tangent cone = 0; equisingular tangent space = 0')
 print('existence remains OPEN')

if __name__=='__main__':
 main()
