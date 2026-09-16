#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"LU-MIYAOKA-GENUS1-SINGULARITY-COUNT-CERTIFICATE.json"
LOCKS={
 "SOURCE_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/LU-MIYAOKA-GENUS1-SINGULARITY-COUNT-SOURCE-NOTE.md","82e247159d736f92aa1382a469fa1d46a81dbae0"),
 "STOLL_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/STOLL-CANONICAL-C0-SOURCE-NOTE.md","e344290d5241c3f7f165ea3027cfc778abec3360"),
 "FORMAL_PICARD":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-PICARD-REALIZABILITY.md","de83fc169814681109bcbc1576ad24f67d6159e0"),
}
def req(c,m):
    if not c: raise SystemExit("FAIL: "+m)
def root():
    p=HERE
    while p!=p.parent:
        if (p/"AGENTS.md").is_file() and (p/"stages").is_dir(): return p
        p=p.parent
    raise SystemExit("FAIL: repo root")
def blob(p):
    d=p.read_bytes(); return hashlib.sha1(f"blob {len(d)}\0".encode()+d).hexdigest()
def preflight(cert):
    declared={x["id"]:(x["path"],x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared==LOCKS,"source locks")
    rr=root()
    for k,(rel,sha) in LOCKS.items():
        p=rr/rel
        if not p.is_file(): raise SystemExit(f"SOURCE_LOCK_FAIL missing {k}")
        got=blob(p)
        if got!=sha: raise SystemExit(f"SOURCE_LOCK_FAIL {k}: expected {sha}, got {got}")
def main():
    cert=json.loads(CERT.read_text())
    req(cert["schema"]=="STAGE32_MB104_LU_MIYAOKA_GENUS1_SINGULARITY_COUNT_V1","schema")
    preflight(cert)
    K2=16; chi=8; c2=12*chi-K2
    req(c2==80,"c2")
    for l in range(1,9):
        d=112*l
        nmin=max(0,d-(3*c2-K2))
        req(nmin==max(0,112*l-224),f"nmin l={l}")
        delta=168*l*l+56*l
        req(delta>=nmin,f"delta budget l={l}")
    req(cert["adapter"]["c2_S"]==80,"cert c2")
    req(cert["adapter"]["lower_bound"]=="n(C)>=max(0,112*l-224)","bound string")
    req(cert["retained_consequence"]["closes_any_support_orbit"] is False,"firewall")
    print("PASS STAGE32_MB104_LU_MIYAOKA_GENUS1_SINGULARITY_COUNT_V1")
    print("c2(S)=80; genus1 uniform P5 requires n_ordinary_node_or_triple>=max(0,112l-224)")
    print("l>=3 excludes zero-ordinary-node/triple concentrated-cusp compatibility witnesses")
if __name__=="__main__": main()
