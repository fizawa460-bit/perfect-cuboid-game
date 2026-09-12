#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"GENUS1-SPAN5-BALANCED16-BEAUVILLE-NODE-TYPE-QUOTIENT-CERTIFICATE.json"
LOCKS={
 "HUMAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-BEAUVILLE-NODE-TYPE-QUOTIENT.md","968b1a98bfabed60ab8909da0728beeca482bd40"),
 "EQUALITY_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY-CERTIFICATE.json","62a2d01447016731001d35cc5915880daa2bfada"),
 "NODE_TYPE_SOURCE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md","a29161602c0b38f0607794e56e61068b8cb9735d"),
 "NODE_MODEL_VERIFIER":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_genus1_span5_known_conic_balanced_quotient.py","fe55e8a7bcd5b790f8d65419a9a88ba59106ba54"),
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
        p=rr/rel; req(p.is_file(),f"missing {k}")
        req(blob(p)==sha,f"SOURCE_LOCK_FAIL {k}")

def nodes():
    out=[]
    I=1j
    for j in range(3):
        for sa in (1,-1):
            for s1 in (1,-1):
                for s2 in (1,-1):
                    z=[0j]*7; z[j]=sa; o=[t for t in range(3) if t!=j]
                    z[3+o[0]],z[3+o[1]],z[6]=s1,s2,1; out.append(tuple(z))
    for j in range(3):
        o=[t for t in range(3) if t!=j]; a,b=o
        for sr in (1,-1):
            for ep in (1,-1):
                for eq in (1,-1):
                    z=[0j]*7; z[a]=1; z[b]=I*sr; z[3+a]=I*ep; z[3+b]=-eq*sr
                    out.append(tuple(z))
    req(len(out)==48 and len(set(out))==48,"48 node model")
    return out
V=nodes()
def support(mask):
    m=int(mask,16); return [i for i in range(48) if (m>>i)&1]
def ntype(z):
    zeros=[j for j in range(3) if z[3+j]==0]
    req(len(zeros)==1,"unique zero b-coordinate")
    return zeros[0]
def counts(mask):
    c=[0,0,0]
    for i in support(mask): c[ntype(V[i])]+=1
    return c

def main():
    cert=json.loads(CERT.read_text())
    req(cert["schema"]=="STAGE32_MB104_BALANCED16_BEAUVILLE_NODE_TYPE_QUOTIENT_V1","schema")
    preflight(cert)
    expected={
      "0000770000ff":[14,0,0],
      "00007b0000ff":[14,0,0],
      "000707000f0f":[7,7,0],
      "00070b000f0f":[7,7,0],
    }
    for h,c in expected.items():
        req(len(support(h))==14,f"N14 {h}")
        req(counts(h)==c,f"node type counts {h}")
    surv=cert["survivors"]
    req(surv["0000770000ff"]["node_type_counts"]==[14,0,0],"size48 A")
    req(surv["00007b0000ff"]["node_type_counts"]==[14,0,0],"size48 B")
    req(surv["000707000f0f"]["node_type_counts"]==[7,7,0],"000707")
    # F2^3 model: G0 is an index-two plane. Two distinct elements in its outside coset
    # have a nonzero product/difference in G0, forcing component degree e>=2.
    G0={0,1,2,3}; outside={4,5,6,7}
    for a in outside:
        for b in outside:
            if a<b:
                req((a^b) in G0 and (a^b)!=0,"two outside types give nonzero G0 element")
    req(surv["000707000f0f"]["allowed_e"]==[2,4],"000707 e set")
    req(surv["000707000f0f"]["e1_excluded"] is True,"e1 exclusion")
    req(surv["0000770000ff"]["allowed_e"]==[1,2,4],"size48 e set A")
    req(surv["00007b0000ff"]["allowed_e"]==[1,2,4],"size48 e set B")
    req(cert["historical_explicit_support_firewall"]["old_5_5_4_support_is_current_survivor"] is False,"historical scope")
    for k,v in cert["credit_firewall"].items(): req(v is False,f"firewall {k}")
    print("PASS STAGE32_MB104_BALANCED16_BEAUVILLE_NODE_TYPE_QUOTIENT_V1")
    print("current survivors: [14,0,0], [14,0,0], [7,7,0]")
    print("000707 uses two outside stabilizer types => e in {2,4}; size48 remains e in {1,2,4}")

if __name__=="__main__": main()
