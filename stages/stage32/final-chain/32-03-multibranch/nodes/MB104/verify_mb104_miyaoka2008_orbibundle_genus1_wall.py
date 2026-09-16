#!/usr/bin/env python3
from fractions import Fraction
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"MIYAOKA2008-ORBIBUNDLE-GENUS1-WALL-CERTIFICATE.json"
LOCKS={
 "HUMAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MIYAOKA2008-ORBIBUNDLE-GENUS1-WALL.md","f59898039325b8a919f195ed9b0a491885e8232d"),
 "STOLL_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/STOLL-CANONICAL-C0-SOURCE-NOTE.md","e344290d5241c3f7f165ea3027cfc778abec3360"),
 "FORMAL_PICARD":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-PICARD-REALIZABILITY.md","de83fc169814681109bcbc1576ad24f67d6159e0"),
 "LU_MIYAOKA_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/LU-MIYAOKA-GENUS1-SINGULARITY-COUNT-SOURCE-NOTE.md","82e247159d736f92aa1382a469fa1d46a81dbae0"),
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
    dec={x["id"]:(x["path"],x["blob_sha1"]) for x in cert["source_locks"]}
    req(dec==LOCKS,"source locks")
    rr=root()
    for k,(rel,sha) in LOCKS.items():
        p=rr/rel
        if not p.is_file(): raise SystemExit(f"SOURCE_LOCK_FAIL missing {k}")
        got=blob(p)
        if got!=sha: raise SystemExit(f"SOURCE_LOCK_FAIL {k}: expected {sha}, got {got}")

def f(l,a):
    return 168*l*(l+1)*a*a-224*l*a+224

def main():
    cert=json.loads(CERT.read_text())
    req(cert["schema"]=="STAGE32_MB104_MIYAOKA2008_ORBIBUNDLE_GENUS1_WALL_V1","schema")
    preflight(cert)
    K2=16; chi=8; c2=12*chi-K2
    req(c2==80 and 3*c2-K2==224,"surface invariants")
    for l in range(1,101):
        a=Fraction(2,3*(l+1))
        req(0<a<1,"alpha range")
        expected=Fraction(224*(2*l+3),3*(l+1))
        req(f(l,a)==expected,"quadratic minimum value")
        req(expected>0,"strict positivity")
        # derivative vanishes at the displayed alpha
        req(336*l*(l+1)*a-224*l==0,"stationary point")
    cc=cert["adapter"]
    req(cc["K2"]==16 and cc["c2"]==80,"cert invariants")
    req(cc["quadratic"]=="168*l*(l+1)*alpha^2-224*l*alpha+224","cert quadratic")
    req(cc["minimum"]=="224*(2*l+3)/(3*(l+1))","cert minimum")
    rc=cert["retained_consequence"]
    req(rc["bounds_l"] is False,"no l bound")
    req(rc["closes_any_support_orbit"] is False,"no closure")
    print("PASS STAGE32_MB104_MIYAOKA2008_ORBIBUNDLE_GENUS1_WALL_V1")
    print("f_l(alpha)=168*l*(l+1)*alpha^2-224*l*alpha+224")
    print("min at alpha=2/(3(l+1)); minimum=224*(2l+3)/(3(l+1))>0")
    print("standard single-curve orbibundle BMY gives no l-bound on the uniform P5 ray")
if __name__=="__main__": main()
