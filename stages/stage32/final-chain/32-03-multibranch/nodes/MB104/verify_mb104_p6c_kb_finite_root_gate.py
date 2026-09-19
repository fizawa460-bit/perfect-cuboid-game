#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from fractions import Fraction
from pathlib import Path

MASK=int("0000093f442e",16)
CERT="MB104-P6C-KB-FINITE-ROOT-CERTIFICATE.json"
CERT_BLOB="fbbf357fddb9a482385e30098649bdaf0d64a3eb"
NOTE="MB104-P6C-KB-FINITE-ROOT-GATE-20260919.md"
NOTE_BLOB="a85122b2199881a0547494e79a85eeeb6347ece7"
P6B_CERT="MB104-P6B-KNOWN-CURVE-KC-QUOTIENT-CERTIFICATE.json"
P6B_BLOB="6713ec219456783180bb7966cf3a8420307accff"

def req(c,m):
    if not c: raise SystemExit("FAIL: "+m)

def blob(p):
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

# Gaussian rationals.
def G(a=0,b=0): return (Fraction(a),Fraction(b))
O=G(); U=G(1)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def zero(x): return x==O
def inv(x):
    d=x[0]*x[0]+x[1]*x[1]
    req(d!=0,"invert zero")
    return (x[0]/d,-x[1]/d)

def rank(M):
    A=[row[:] for row in M]
    if not A:return 0
    m=len(A);n=len(A[0]);r=0
    for c in range(n):
        p=next((i for i in range(r,m) if not zero(A[i][c])),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        q=inv(A[r][c]); A[r]=[mul(q,x) for x in A[r]]
        for i in range(m):
            if i==r or zero(A[i][c]): continue
            f=A[i][c]
            A[i]=[sub(A[i][j],mul(f,A[r][j])) for j in range(n)]
        r+=1
        if r==m: break
    return r

def nodes():
    v=[]
    for j in range(3):
      for sa in (1,-1):
       for s1 in (1,-1):
        for s2 in (1,-1):
         x=[O for _ in range(7)]
         x[j]=G(sa)
         q=[t for t in range(3) if t!=j]
         x[3+q[0]]=G(s1);x[3+q[1]]=G(s2);x[6]=U
         v.append(tuple(x))
    for j in range(3):
      q=[t for t in range(3) if t!=j];a,b=q
      for sr in (1,-1):
       for ep in (1,-1):
        for eq in (1,-1):
         x=[O for _ in range(7)]
         x[a]=U;x[b]=G(0,sr);x[3+a]=G(0,ep);x[3+b]=G(-eq*sr)
         v.append(tuple(x))
    req(len(v)==48,"48 nodes")
    return v

def peq(a,b):
    k=next(i for i,x in enumerate(a) if not zero(x))
    return all(mul(a[j],b[k])==mul(b[j],a[k]) for j in range(7))

def sign_perm(q,V):
    p=[]
    for x in V:
        y=tuple(neg(x[j]) if j==q else x[j] for j in range(7))
        hit=[i for i,w in enumerate(V) if peq(y,w)]
        req(len(hit)==1,"sign action")
        p.append(hit[0])
    return p

def quotient_data(S,q,V):
    p=sign_perm(q,V); seen=set(); out=[]
    S=set(S)
    for i in range(48):
        if i in seen: continue
        orb={i,p[i]};seen|=orb
        w=len(S&orb)
        if not w or zero(V[i][q]): continue
        pr=[V[i][j] for j in range(7) if j!=q]
        out.append((w,pr))
    return out

def min_rank_at_weight(data,thr):
    best=99
    n=len(data)
    for m in range(1,1<<n):
        W=sum(data[j][0] for j in range(n) if (m>>j)&1)
        if W<thr: continue
        R=rank([data[j][1] for j in range(n) if (m>>j)&1])
        best=min(best,R)
    return best

def main():
    here=Path(__file__).resolve().parent
    req(blob(here/CERT)==CERT_BLOB,"certificate blob")
    req(blob(here/NOTE)==NOTE_BLOB,"note blob")
    req(blob(here/P6B_CERT)==P6B_BLOB,"P6B certificate blob")
    cert=json.loads((here/CERT).read_text())

    V=nodes()
    S=[i for i in range(48) if (MASK>>i)&1]
    req(S==[1,2,3,5,10,14,16,17,18,19,20,21,24,27],"support")

    results={}
    for q,name in [(3,"b1"),(4,"b2"),(5,"b3")]:
        data=quotient_data(S,q,V)
        weights=sorted([w for w,_ in data],reverse=True)
        r8=min_rank_at_weight(data,8)
        results[name]={"weights":weights,"r8":r8}
        if name=="b2":
            results[name]["r11"]=min_rank_at_weight(data,11)

    req(results["b1"]=={"weights":[2,2,1,1,1,1],"r8":5},"b1 finite span")
    req(results["b2"]=={"weights":[2,2,2,2,1,1,1,1],"r8":4,"r11":6},"b2 finite span")
    req(results["b3"]=={"weights":[2,1,1,1,1,1,1],"r8":6},"b3 finite span")

    for name in ("b1","b2","b3"):
        c=cert["kb_data"][name]
        req(c["quotient_node_weights"]==results[name]["weights"],"cert weights "+name)
        req(c["min_vector_rank_weight_ge_8"]==results[name]["r8"],"cert conic rank "+name)
    req(cert["kb_data"]["b2"]["min_vector_rank_weight_ge_11"]==results["b2"]["r11"],"cert cubic rank")

    # Projective span criteria.
    req(results["b1"]["r8"]>3 and results["b2"]["r8"]>3 and results["b3"]["r8"]>3,
        "no weight>=8 subset can lie on a plane conic")
    req(results["b2"]["r11"]>4,
        "no weight>=11 subset can lie on a P3 twisted cubic")

    req(cert["consequence"]["all_seven_coordinate_quotient_W4_root_walls_closed_negative_on_survivor"] is True,
        "W4 coordinate quotient disposition")
    for k,v in cert["credit_firewall"].items():
        req(v is False,"credit "+k)

    print("PASS STAGE32_MB104_P6C_KB_FINITE_ROOT_GATE_V1")
    print("b1 conic min vector rank at W>=8 = 5")
    print("b2 conic/cubic min ranks = 4 / 6")
    print("b3 conic min vector rank at W>=8 = 6")
    print("all seven coordinate-sign quotient negative-root walls closed on survivor")
    print("whole_P6_closed=false credit=zero")

if __name__=="__main__":
    main()
