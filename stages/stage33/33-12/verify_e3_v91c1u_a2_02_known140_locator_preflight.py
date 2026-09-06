#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; S33=HERE.parent
OUT=HERE/'e3-v91c1u-a2-02-known140-locator-preflight.json'
T=HERE/'e3-v91c1t-a2-02-swap23-pic2-adapter-preflight.json'
C09=S33/'33-09'/'stage33-09-closure.json'
B09=S33/'33-09'/'marked-picard-basis-bridge-certified.json'
E11=S33/'33-11e'/'stage33-11e-prime-galois-transport-certificate.json'
NODES=S33/'33-07'/'exceptional-p1-tangent-coordinates.json'
SHA={OUT:'7480d0d77cc70762cb80e08081f49a5895bb21a46a99dfd699fe63980a977a34',T:'6c064cf02fb7a0908242317bf7ac1b20b0586751b78e07b26d6c7889060ffdfa',C09:'6c3ff8f7ca7d1bbd4084da0cc77ca6d43b31b32566a3bbb2c2103b7c2e9548b7',B09:'039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92',E11:'1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426',NODES:'beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636'}
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==SHA[p]==csha(b),p; return o
def main():
 out,t,c09,b09,e11,nodes=map(load,[OUT,T,C09,B09,E11,NODES])
 assert t['exact_consequence']['literal_swap23_full_codim1_difference_materialized'] is True
 assert t['exact_consequence']['literal_swap23_full_codim1_difference_nonzero'] is True
 assert t['exact_consequence']['source_bound_swap23_actual_divisor_to_retained_picard64_adapter_materialized'] is False
 assert c09['historical_q256_basis_marking_exact'] is True
 assert c09['source_locks']['marked_picard_bridge_certificate_sha256']==B09.name and False
if __name__=='__main__': main()
