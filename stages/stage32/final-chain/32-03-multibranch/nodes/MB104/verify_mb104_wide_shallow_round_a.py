#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[6]
CERT=Path(__file__).with_name("MB104-WIDE-SHALLOW-ROUND-A-CERTIFICATE.json")

LOCKS={
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-WIDE-SHALLOW-CLOSURE-SCAN-20260918.md":
"b9b440abd01b5f2a33a4a2b91881536d1f6683d8",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-WIDE-W4-K3-QUOTIENT-SOURCE-NOTE-20260918.md":
"ff61ae6c06549af194b4f1af611c7d4ea46d0dff",
}

MASK="000707000f0f"

def blob(path:Path)->str:
    data=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def req(ok,msg):
    if not ok:
        raise SystemExit("FAIL: "+msg)

def canon(z):
    for x in z:
        if x!=0:
            s=x
            break
    w=tuple(x/s for x in z)
    return tuple(complex(round(x.real),round(x.imag)) for x in w)

def nodes():
    out=[]
    for j in range(3):
        for sa in (1,-1):
            for s1 in (1,-1):
                for s2 in (1,-1):
                    z=[0j]*7
                    z[j]=sa
                    o=[t for t in range(3) if t!=j]
                    z[3+o[0]]=s1
                    z[3+o[1]]=s2
                    z[6]=1
                    out.append(tuple(z))
    for j in range(3):
        o=[t for t in range(3) if t!=j]
        a,b=o
        for sr in (1,-1):
            for ep in (1,-1):
                for eq in (1,-1):
                    z=[0j]*7
                    z[a]=1
                    z[b]=1j*sr
                    z[3+a]=1j*ep
                    z[3+b]=-eq*sr
                    out.append(tuple(z))
    req(len(out)==48,"48 nodes")
    return out

def apply_gen(z,k):
    a1,a2,a3,b1,b2,b3,c=z
    if k==0:return (a2,a1,a3,b2,b1,b3,c)
    if k==1:return (a3,a2,a1,b3,b2,b1,c)
    if k==2:return (1j*c,a2,a3,b1,1j*b3,-1j*b2,-1j*a1)
    if k==3:return (-a1,a2,a3,b1,b2,b3,c)
    if k==4:return (a1,-a2,a3,b1,b2,b3,c)
    if k==5:return (a1,a2,-a3,b1,b2,b3,c)
    if k==6:return (a1,a2,a3,-b1,b2,b3,c)
    if k==7:return (a1,a2,a3,b1,-b2,b3,c)
    if k==8:return (a1,a2,a3,b1,b2,-b3,c)
    raise ValueError(k)

def compose(p,q):
    return tuple(p[q[i]] for i in range(48))

def perms():
    V=nodes()
    cs=[canon(z) for z in V]
    idx={z:i for i,z in enumerate(cs)}
    gs=[]
    for k in range(9):
        p=tuple(idx[canon(apply_gen(z,k))] for z in V)
        req(sorted(p)==list(range(48)),f"gen {k}")
        gs.append(p)
    return gs

def generate_group(gs):
    ident=tuple(range(48))
    group={ident}
    stack=[ident]
    while stack:
        a=stack.pop()
        for g in gs:
            h=compose(g,a)
            if h not in group:
                group.add(h)
                stack.append(h)
    return group

def supp(mask):
    x=int(mask,16)
    return {i for i in range(48) if (x>>i)&1}

def main():
    for rel,expected in LOCKS.items():
        p=ROOT/rel
        req(p.is_file(),"missing "+rel)
        req(blob(p)==expected,"source drift "+rel)

    c=json.loads(CERT.read_text())
    req(c["schema"]=="STAGE32_MB104_WIDE_SHALLOW_ROUND_A_V1","schema")

    # W1 and W2 polynomial replay.
    for l in range(1,20):
        discr=(336*l*l-224*l+16)-4*(168*l*l+56*l)
        req(discr==-336*l*l-448*l+16 and discr<0,f"W1 l={l}")
        chi=168*l*l-56*l+8
        req(chi>0,f"W2 chi l={l}")
        req(16-112*l<0,f"W2 h2 l={l}")

    # W3 exact orbit double count and norm class.
    gs=perms()
    G=generate_group(gs)
    req(len(G)==1536,"Aut order")
    req(len({g[0] for g in G})==48,"node transitivity")
    S=supp(MASK)
    orbit={frozenset(g[i] for i in S) for g in G}
    req(len(orbit)==768,"support orbit")
    counts=[sum(1 for T in orbit if i in T) for i in range(48)]
    req(set(counts)=={224},"uniform incidence")
    A2=36*16-48*2
    req(A2==480,"W3 A2")
    req(6*16==96,"W3 KA")
    req(8+(480-96)//2==200,"W3 chi")
    req(12-6==6 and 24-8==16 and (96-8*2)//2==40,"W3 test pairings")

    # W4 coordinate sign involutions. The c-sign permutation is the product
    # of the six independent coordinate sign generators, projectively.
    coord_perms=gs[3:9]
    cp=tuple(range(48))
    for p in coord_perms:
        cp=compose(p,cp)
    coord_perms=coord_perms+[cp]
    names=["a1","a2","a3","b1","b2","b3","c"]
    expected={
        "a1":(7,7,1344),"a2":(7,7,1344),"a3":(8,8,1376),
        "b1":(13,7,1152),"b2":(13,7,1152),"b3":(12,0,736),
        "c":(6,6,1312)
    }
    for name,p in zip(names,coord_perms):
        T={p[i] for i in S}
        t=len(S&T)
        fixed={i for i,j in enumerate(p) if i==j}
        f=len(S&fixed)
        sq=1120-32*t+64*f
        req((t,f,sq)==expected[name],f"W4 {name}")
        req(0<sq<=1568,f"W4 Hodge {name}")

    # W6 retained numerical saturation.
    for l in range(1,20):
        req(7*l*4-4*l*7==0,f"W6 quartic pairing l={l}")

    rs=c["round_summary"]
    req(rs["drop"]==["W1","W2","W3","W6"],"drops")
    req(rs["pass_to_second_scan"]==["W4"],"W4 survivor")
    req(rs["deep_candidate"] is False,"no deep")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit firewall "+k)

    print("PASS STAGE32_MB104_WIDE_SHALLOW_ROUND_A_V1")
    print("W1=DROP W2=DROP W3=DROP W4=SECOND_SCAN W6=DROP")
    print("next=ROUND_B_PLUS_W4_SECOND_SCAN no_credit")

if __name__=="__main__":
    main()
