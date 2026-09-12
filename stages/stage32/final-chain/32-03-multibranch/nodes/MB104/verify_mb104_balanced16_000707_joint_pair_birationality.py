#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"GENUS1-SPAN5-BALANCED16-000707-JOINT-PAIR-BIRATIONALITY-CERTIFICATE.json"
LOCKS={
 "HUMAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-JOINT-PAIR-BIRATIONALITY.md","53608cb51aa49ccde1603b1cb1d136ea497b2324"),
 "HURWITZ_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-HURWITZ-CAPACITY-CERTIFICATE.json","76b458d2f21af7113764447e1a8064e957b025e7"),
 "SUPPORT_STABILIZER_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-STABILIZER-UNION-CERTIFICATE.json","31695c6908cff73d04baab2ed11dfd04608a2464"),
 "AUT_SOURCE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/AUTS-NODE-ACTION-SOURCE-NOTE.md","cbe21fdbacb975a726d0c2c8a1ab8fd3b21d0693"),
}
MASK="000707000f0f"

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
    req(dec==LOCKS,"source-lock table")
    rr=root()
    for k,(rel,sha) in LOCKS.items():
        p=rr/rel
        if not p.is_file(): raise SystemExit(f"SOURCE_LOCK_FAIL missing {k}")
        got=blob(p)
        if got!=sha: raise SystemExit(f"SOURCE_LOCK_FAIL {k}: expected {sha}, got {got}")
def load(k): return json.loads((root()/LOCKS[k][0]).read_text())

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
    req(len(out)==48 and len(set(out))==48,"48-node model")
    return out
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
            req(len(hits)==1,"generator node image")
            p.append(hits[0])
        out.append(tuple(p))
    return out
GEN=generators()
def compose(a,b): return tuple(a[b[i]] for i in range(48))
def group():
    ident=tuple(range(48)); seen={ident}; todo=[ident]
    for x in todo:
        for g in GEN:
            h=compose(g,x)
            if h not in seen: seen.add(h); todo.append(h)
    req(len(todo)==1536,"Aut(S) node-action order 1536")
    return todo
G=group()
def from_mask(h):
    m=int(h,16); return frozenset(i for i in range(48) if (m>>i)&1)
def actset(S,p): return frozenset(p[i] for i in S)
def ntype(z):
    zeros=[j for j in range(3) if z[3+j]==0]
    req(len(zeros)==1,"unique b-zero node type")
    return zeros[0]

def main():
    cert=json.loads(CERT.read_text())
    req(cert["schema"]=="STAGE32_MB104_BALANCED16_000707_JOINT_PAIR_BIRATIONALITY_V1","schema")
    preflight(cert)
    hz=load("HURWITZ_CERT")
    ss=load("SUPPORT_STABILIZER_CERT")
    req(hz["support"]["mask"]==MASK,"Hurwitz mask")
    req(hz["support"]["node_type_counts"]==[7,7,0],"Hurwitz node types")
    req(hz["scope_firewall"]["e2_closed"] is False and hz["scope_firewall"]["e4_closed"] is False,"upstream open cases")
    req(ss["support_stabilizers"][MASK]["stabilizer_order"]==2,"upstream stabilizer order")

    S=from_mask(MASK); req(len(S)==14,"N=14")
    types=[ntype(V[i]) for i in S]
    req([types.count(j) for j in range(3)]==[7,7,0],"exact support type counts")
    stab=[p for p in G if actset(S,p)==S]
    req(len(stab)==2,"exact support stabilizer order2")
    ident=tuple(range(48)); g0=GEN[0]
    req(g0 in stab and g0!=ident,"first generator is unique nonidentity stabilizer")
    req(set(stab)=={ident,g0},"stabilizer exactly identity plus first generator")
    for i in S:
        t=ntype(V[i]); tp=ntype(V[g0[i]])
        req((t,tp) in {(0,1),(1,0)},"nonidentity stabilizer swaps used types")
    type_preserving=[p for p in stab if all(ntype(V[p[i]])==ntype(V[i]) for i in S)]
    req(type_preserving==[ident] or set(type_preserving)=={ident},"type-preserving support stabilizer trivial")

    jq=cert["joint_quotient"]
    req(jq["H_order"]==4,"H order4")
    req(jq["e2_projection_degree"]=="28*l" and jq["e4_projection_degree"]=="56*l","projection degrees")
    rc=cert["relative_symmetry_consequence"]
    req(rc["relative_deck_symmetry_preserves_each_node_stabilizer_type"] is True,"relative type preservation")
    req(rc["nontrivial_relative_symmetry_possible"] is False,"relative symmetry excluded")
    req(rc["relative_symmetry_group_order"]==1 and rc["joint_pair_generic_degree"]==1,"generic degree one")
    req(rc["joint_pair_birational"] is True,"birational conclusion")
    req(cert["image"]["e2_bidegree"]==["28*l","28*l"],"e2 bidegree")
    req(cert["image"]["e4_bidegree"]==["56*l","56*l"],"e4 bidegree")
    fw=cert["credit_firewall"]
    req(fw["e2_closed"] is False and fw["e4_closed"] is False and fw["MB104_complete"] is False,"closure firewall")
    req(fw["merge_authorized"] is False,"merge firewall")
    print("PASS STAGE32_MB104_BALANCED16_000707_JOINT_PAIR_BIRATIONALITY_V1")
    print("Aut(S)=1536; support stabilizer={1, swap(a1,a2;b1,b2)}; nonidentity swaps the two used node types")
    print("relative deck symmetry is type-preserving => trivial; joint pair generic degree=1 for e=2,4")
    print("image bidegrees=(28l,28l) or (56l,56l); no closure claimed")
if __name__=="__main__": main()
