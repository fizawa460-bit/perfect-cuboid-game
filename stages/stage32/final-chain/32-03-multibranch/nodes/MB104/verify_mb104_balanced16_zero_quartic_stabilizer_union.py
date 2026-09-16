#!/usr/bin/env python3
import hashlib, json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-STABILIZER-UNION-CERTIFICATE.json"
LOCKS = {
    "AUT_SOURCE": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/AUTS-NODE-ACTION-SOURCE-NOTE.md", "cbe21fdbacb975a726d0c2c8a1ab8fd3b21d0693"),
    "BALANCED_QUOTIENT_CERT": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-KNOWN-CONIC-BALANCED-QUOTIENT-CERTIFICATE.json", "f63d08b9005762a02935a727f35e6581ae52aaab"),
    "RESTRICTION_COHOM_CERT": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-RESTRICTION-COHOMOLOGY-CERTIFICATE.json", "f1e7e483e115b04cbf63c08a3be37627214a7122"),
    "HUMAN_NOTE": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-STABILIZER-UNION.md", "19b59a13f3c4cb2d4e7d0c46798c046ee6303d52"),
}

def require(c,m):
    if not c: raise SystemExit(f"FAIL: {m}")

def root():
    p=HERE
    while p!=p.parent:
        if (p/"AGENTS.md").is_file() and (p/"stages").is_dir(): return p
        p=p.parent
    raise SystemExit("FAIL: repo root not found")

def blob_sha1(p):
    d=p.read_bytes(); return hashlib.sha1(f"blob {len(d)}\0".encode()+d).hexdigest()

def preflight(cert):
    declared={x["id"]:(x["path"],x["blob_sha1"]) for x in cert["source_locks"]}
    require(declared==LOCKS,"source-lock table")
    rr=root()
    for k,(rel,sha) in LOCKS.items():
        p=rr/rel
        if not p.is_file(): raise SystemExit(f"SOURCE_LOCK_FAIL missing {k}")
        got=blob_sha1(p)
        if got!=sha: raise SystemExit(f"SOURCE_LOCK_FAIL {k}: expected {sha}, got {got}")

def nodes():
    out=[]
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
                    z=[0j]*7; z[a],z[b],z[3+a],z[3+b]=1,1j*sr,1j*ep,-eq*sr; out.append(tuple(z))
    require(len(out)==48 and len(set(out))==48,"48 nodes"); return out
V=nodes()

def peq(a,b):
    k=next((j for j,x in enumerate(a) if x!=0),None)
    return k is not None and b[k]!=0 and all(a[j]*b[k]==b[j]*a[k] for j in range(7))
def apply(x,src,cf): return tuple(cf[j]*x[src[j]] for j in range(7))
def generators():
    specs=[([1,0,2,4,3,5,6],[1]*7),([2,1,0,5,4,3,6],[1]*7)]
    c=[1]*7; c[0],c[4],c[5],c[6]=1j,1j,-1j,-1j; specs.append(([6,1,2,3,5,4,0],c))
    for qq in range(6):
        c=[1]*7; c[qq]=-1; specs.append((list(range(7)),c))
    out=[]
    for src,cf in specs:
        p=[]
        for x in V:
            hits=[r for r,z in enumerate(V) if peq(apply(x,src,cf),z)]
            require(len(hits)==1,"generator node image"); p.append(hits[0])
        out.append(tuple(p))
    return out
def compose(a,b): return tuple(a[b[i]] for i in range(48))
def group():
    ident=tuple(range(48)); seen={ident}; todo=[ident]
    for x in todo:
        for g in generators():
            h=compose(g,x)
            if h not in seen: seen.add(h); todo.append(h)
    require(len(todo)==1536,"Aut order"); return todo
def actset(s,p): return frozenset(p[i] for i in s)
def support(pred): return frozenset(r for r,z in enumerate(V) if pred(z))
def from_mask(h):
    m=int(h,16); return frozenset(r for r in range(48) if (m>>r)&1)
def q(z,k):
    a1,a2,a3,b1,b2,b3,c=z
    return (a1*a1+a2*a2-b3*b3,a2*a2+a3*a3-b1*b1,a1*a1+a3*a3-b2*b2,a1*a1+a2*a2+a3*a3-c*c)[k-1]
def elliptics(G):
    e0=support(lambda z: z[3]==0 and z[1]==1j*z[2] and z[6]==z[0] and q(z,1)==0 and q(z,3)==0)
    O={actset(e0,p) for p in G}; require(len(O)==12 and all(len(e)==8 for e in O),"12 elliptics"); return O

def main():
    cert=json.loads(CERT.read_text()); require(cert["schema"]=="STAGE32_MB104_BALANCED16_ZERO_QUARTIC_STABILIZER_UNION_V1","schema"); preflight(cert)
    G=group(); Es=elliptics(G)
    expected={
      "0000770000ff":(48,32,4,{27,31},Counter({4:4,0:2})),
      "00007b0000ff":(48,32,4,{26,31},Counter({4:4,0:2})),
      "000707000f0f":(768,2,2,{27,35},Counter({0:1})),
      "00070b000f0f":(768,2,2,{26,35},Counter({0:1})),
    }
    for h,(osz,ssz,nz,omits,overlaps) in expected.items():
        S=from_mask(h); require(len(S)==14,f"{h} N14")
        orbit={actset(S,p) for p in G}; require(len(orbit)==osz,f"{h} support orbit")
        stab=[p for p in G if actset(S,p)==S]; require(len(stab)==ssz,f"{h} stabilizer")
        zeros=[e for e in Es if len(S&e)==7]; require(len(zeros)==nz,f"{h} zero count")
        zorb={actset(zeros[0],p) for p in stab}; require(zorb==set(zeros),f"{h} zero transitivity")
        omitted={next(iter(e-S)) for e in zeros}; require(omitted==omits,f"{h} omitted nodes")
        norb={p[next(iter(omitted))] for p in stab}; require(norb==omitted,f"{h} omitted transitivity")
        ov=Counter(len(zeros[i]&zeros[j]) for i in range(len(zeros)) for j in range(i+1,len(zeros)))
        require(ov==overlaps,f"{h} node-overlap profile")
    rc=cert["retained_consequence"]
    require(rc["zero_quartic_fixedness_all_or_none_per_support_orbit"] is True,"all-or-none consequence")
    require(rc["restriction_rank_decided"] is False,"rank firewall")
    require(cert["credit_firewall"]["balanced16_closed"] is False,"balanced16 firewall")
    print("PASS STAGE32_MB104_BALANCED16_ZERO_QUARTIC_STABILIZER_UNION_V1")
    print("support_stabilizers=32,32,2,2 zero_orbits=4,4,2,2 transitive")
    print("restriction_fixedness=all_or_none_per_support_orbit; rank_not_decided")

if __name__=="__main__": main()
