#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction
from math import gcd
from pathlib import Path

AUDIT_HEAD="b28adadc95776762754e1415a0ecab0da1d4cd8e"
AUDIT_LOCKS={
 "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-WIDE-W4-K3-QUOTIENT-SOURCE-NOTE-20260918.md":
   "ff61ae6c06549af194b4f1af611c7d4ea46d0dff",
 "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-W4-THIRD-DEPTH-ROOT-WALL-20260918.md":
   "b28fbeb260250ec2cb97ee45aaaf1933a886909a",
}
SOURCE_NOTE="MB104-P6B-STOLL-TESTA-KNOWN-CURVE-KC-SOURCE-NOTE-20260919.md"
SOURCE_BLOB="dc58a0a7d57dff5286e7b6739d4ac02f9266fa87"
CERT="MB104-P6B-KNOWN-CURVE-KC-QUOTIENT-CERTIFICATE.json"
CERT_BLOB="6713ec219456783180bb7966cf3a8420307accff"
MASK=int("0000093f442e",16)

class F:
    __slots__=("a","b","c","d")
    def __init__(self,a=0,b=0,c=0,d=0):
        self.a,self.b,self.c,self.d=map(Fraction,(a,b,c,d))
    def __add__(self,o):
        o=toF(o); return F(self.a+o.a,self.b+o.b,self.c+o.c,self.d+o.d)
    __radd__=__add__
    def __neg__(self): return F(-self.a,-self.b,-self.c,-self.d)
    def __sub__(self,o): return self+(-toF(o))
    def __rsub__(self,o): return toF(o)-self
    def __mul__(self,o):
        o=toF(o)
        def cm(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
        A=(self.a,self.b); C=(self.c,self.d); B=(o.a,o.b); D=(o.c,o.d)
        AB=cm(A,B); CD=cm(C,D); AD=cm(A,D); CB=cm(C,B)
        return F(AB[0]+2*CD[0],AB[1]+2*CD[1],AD[0]+CB[0],AD[1]+CB[1])
    __rmul__=__mul__
    def __eq__(self,o):
        o=toF(o); return (self.a,self.b,self.c,self.d)==(o.a,o.b,o.c,o.d)

def toF(x): return x if isinstance(x,F) else F(x)
O=F(); U=F(1); I=F(0,1); S=F(0,0,1)
def z(x): return x==O

def req(c,m):
    if not c: raise SystemExit("FAIL: "+m)

def blob(p:Path):
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def check_audit(root:Path):
    got=subprocess.check_output(["git","-C",str(root),"rev-parse","HEAD"],text=True).strip()
    req(got==AUDIT_HEAD,"audit HEAD")
    for rel,want in AUDIT_LOCKS.items():
        p=root/rel
        req(p.is_file() and blob(p)==want,"audit source "+rel)

def nodes():
    v=[]
    for j in range(3):
        for sa in (1,-1):
            for s1 in (1,-1):
                for s2 in (1,-1):
                    x=[O for _ in range(7)]
                    x[j]=F(sa)
                    q=[t for t in range(3) if t!=j]
                    x[3+q[0]]=F(s1); x[3+q[1]]=F(s2); x[6]=U
                    v.append(tuple(x))
    for j in range(3):
        q=[t for t in range(3) if t!=j]; a,b=q
        for sr in (1,-1):
            for ep in (1,-1):
                for eq in (1,-1):
                    x=[O for _ in range(7)]
                    x[a]=U; x[b]=F(0,sr); x[3+a]=F(0,ep); x[3+b]=F(-eq*sr)
                    v.append(tuple(x))
    req(len(v)==48,"48 nodes")
    return v

def peq(a,b):
    k=next(i for i,x in enumerate(a) if not z(x))
    return all(a[j]*b[k]==b[j]*a[k] for j in range(7))

def perm_for(fn,V):
    p=[]
    for x in V:
        y=fn(x)
        hit=[j for j,w in enumerate(V) if peq(y,w)]
        req(len(hit)==1,"node action")
        p.append(hit[0])
    return p

def compose(a,b): return [a[b[i]] for i in range(48)]

def sign_perm(q,V):
    return perm_for(lambda x: tuple((-x[j] if j==q else x[j]) for j in range(7)),V)

def aut_perms(V):
    def g0(x):
        a1,a2,a3,b1,b2,b3,c=x; return (a2,a1,a3,b2,b1,b3,c)
    def g1(x):
        a1,a2,a3,b1,b2,b3,c=x; return (a3,a2,a1,b3,b2,b1,c)
    def g2(x):
        a1,a2,a3,b1,b2,b3,c=x
        return (I*c,a2,a3,b1,I*b3,-I*b2,-I*a1)
    return [perm_for(f,V) for f in (g0,g1,g2)]

def known_surface_curves():
    out=[]
    meta=[]
    # C1: 32 conics.
    for fam in range(4):
      for e1 in (1,-1):
       for e2 in (1,-1):
        for e3 in (1,-1):
          if fam==0:
            fn=lambda x,e1=e1,e2=e2,e3=e3: z(x[0]) and z(x[1]+e1*x[5]) and z(x[2]+e2*x[4]) and z(x[3]+e3*x[6])
          elif fam==1:
            fn=lambda x,e1=e1,e2=e2,e3=e3: z(x[1]) and z(x[2]+e1*x[3]) and z(x[0]+e2*x[5]) and z(x[4]+e3*x[6])
          elif fam==2:
            fn=lambda x,e1=e1,e2=e2,e3=e3: z(x[2]) and z(x[0]+e1*x[4]) and z(x[1]+e2*x[3]) and z(x[5]+e3*x[6])
          else:
            fn=lambda x,e1=e1,e2=e2,e3=e3: z(x[6]) and z(I*x[0]+e1*x[3]) and z(I*x[1]+e2*x[4]) and z(I*x[2]+e3*x[5])
          out.append(fn); meta.append(("C1",2))
    # C2: 12 elliptic quartics.
    for fam in range(3):
      for e1 in (1,-1):
       for e2 in (1,-1):
        if fam==0:
            fn=lambda x,e1=e1,e2=e2: z(x[3]) and z(I*x[1]+e1*x[2]) and z(x[0]+e2*x[6])
        elif fam==1:
            fn=lambda x,e1=e1,e2=e2: z(x[4]) and z(I*x[2]+e1*x[0]) and z(x[1]+e2*x[6])
        else:
            fn=lambda x,e1=e1,e2=e2: z(x[5]) and z(I*x[0]+e1*x[1]) and z(x[2]+e2*x[6])
        out.append(fn); meta.append(("C2",4))
    # C3: 48 further elliptic quartics.
    for fam in range(6):
      for e1 in (1,-1):
       for e2 in (1,-1):
        for e3 in (1,-1):
          if fam==0:
            fn=lambda x,e1=e1,e2=e2,e3=e3: z(x[0]+e1*x[1]) and z(S*x[0]+e2*x[5]) and z(x[3]+e3*x[4])
          elif fam==1:
            fn=lambda x,e1=e1,e2=e2,e3=e3: z(x[1]+e1*x[2]) and z(S*x[1]+e2*x[3]) and z(x[4]+e3*x[5])
          elif fam==2:
            fn=lambda x,e1=e1,e2=e2,e3=e3: z(x[2]+e1*x[0]) and z(S*x[2]+e2*x[4]) and z(x[5]+e3*x[3])
          elif fam==3:
            fn=lambda x,e1=e1,e2=e2,e3=e3: z(I*x[0]+e1*x[6]) and z(I*x[4]+e2*x[5]) and z(I*S*x[0]+e3*x[3])
          elif fam==4:
            fn=lambda x,e1=e1,e2=e2,e3=e3: z(I*x[1]+e1*x[6]) and z(I*x[5]+e2*x[3]) and z(I*S*x[1]+e3*x[4])
          else:
            fn=lambda x,e1=e1,e2=e2,e3=e3: z(I*x[2]+e1*x[6]) and z(I*x[3]+e2*x[4]) and z(I*S*x[2]+e3*x[5])
          out.append(fn); meta.append(("C3",4))
    req(len(out)==92,"92 known curves")
    return out,meta

def kc_conics():
    out=[]
    # C1sK first 12.
    for fam in range(3):
      for e1 in (1,-1):
       for e2 in (1,-1):
        if fam==0:
            fn=lambda x,e1=e1,e2=e2: z(x[0]) and z(x[1]+e1*x[5]) and z(x[2]+e2*x[4])
        elif fam==1:
            fn=lambda x,e1=e1,e2=e2: z(x[1]) and z(x[2]+e1*x[3]) and z(x[0]+e2*x[5])
        else:
            fn=lambda x,e1=e1,e2=e2: z(x[2]) and z(x[0]+e1*x[4]) and z(x[1]+e2*x[3])
        out.append(fn)
    # 8 branch conics.
    for e1 in (1,-1):
     for e2 in (1,-1):
      for e3 in (1,-1):
       out.append(lambda x,e1=e1,e2=e2,e3=e3:
                  z(I*x[0]+e1*x[3]) and z(I*x[1]+e2*x[4]) and z(I*x[2]+e3*x[5]))
    # C3sK first 24.
    for fam in range(3):
      for e1 in (1,-1):
       for e2 in (1,-1):
        for e3 in (1,-1):
          if fam==0:
            fn=lambda x,e1=e1,e2=e2,e3=e3: z(x[0]+e1*x[1]) and z(S*x[0]+e2*x[5]) and z(x[3]+e3*x[4])
          elif fam==1:
            fn=lambda x,e1=e1,e2=e2,e3=e3: z(x[1]+e1*x[2]) and z(S*x[1]+e2*x[3]) and z(x[4]+e3*x[5])
          else:
            fn=lambda x,e1=e1,e2=e2,e3=e3: z(x[2]+e1*x[0]) and z(S*x[2]+e2*x[4]) and z(x[5]+e3*x[3])
          out.append(fn)
    req(len(out)==44,"44 Kc conics")
    return out

def reduce_frac(n,d):
    g0=gcd(n,d); return (n//g0,d//g0)

def quotient_weights(S,p,V,q):
    S=set(S); seen=set(); ans=[]
    for i in range(48):
        if i in seen: continue
        orb={i,p[i]}; seen|=orb
        w=len(S&orb)
        if not w: continue
        # quotient singular points are images of nodes with forgotten coordinate nonzero.
        if z(V[i][q]): continue
        ans.append((orb,w))
    return ans

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--audit-root",required=True)
    args=ap.parse_args()
    check_audit(Path(args.audit_root))

    here=Path(__file__).resolve().parent
    req(blob(here/SOURCE_NOTE)==SOURCE_BLOB,"current source note")
    req(blob(here/CERT)==CERT_BLOB,"certificate blob")
    cert=json.loads((here/CERT).read_text())

    V=nodes()
    supp=[i for i in range(48) if (MASK>>i)&1]
    req(supp==cert["support"]["nodes"],"support")

    # All 92 surface known curves.
    funcs,meta=known_surface_curves()
    mx={"C1":0,"C2":0,"C3":0}
    counts={"C1":0,"C2":0,"C3":0}
    nodecount={"C1":set(),"C2":set(),"C3":set()}
    Sset=set(supp)
    for fn,(typ,deg) in zip(funcs,meta):
        pts=[i for i,x in enumerate(V) if fn(x)]
        counts[typ]+=1; nodecount[typ].add(len(pts))
        mx[typ]=max(mx[typ],len(Sset&set(pts)))
    req(counts=={"C1":32,"C2":12,"C3":48},"known curve counts")
    req(nodecount=={"C1":{6},"C2":{8},"C3":{4}},"known curve node counts")
    req(mx=={"C1":3,"C2":5,"C3":3},"survivor known curve maxima")

    # Coordinate sign pushdown P^2.
    sp=[sign_perm(q,V) for q in range(7)]
    p2={}
    for q,name in enumerate(("a1","a2","a3","b1","b2","b3","c")):
        ws=quotient_weights(supp,sp[q],V,q)
        ss=sum(w*w for _,w in ws)
        p2[name]=1568-32*ss
    req(p2=={"a1":1376,"a2":1376,"a3":1184,"b1":1184,"b2":928,"b3":1248,"c":992},"pushdown squares")

    # Move a1/a2/a3 quotient to c-type by exact Aut(S) generators.
    g0,g1,g2=aut_perms(V)
    trans={
      "a1":g2,
      "a2":compose(g2,g0),
      "a3":compose(g2,g1),
      "c":list(range(48)),
    }
    signc=sp[6]
    Kcons=kc_conics()
    maxW={}
    for name,p in trans.items():
        St=[p[i] for i in supp]
        qdata=quotient_weights(St,signc,V,6)
        data=[]
        for orb,w in qdata:
            i=min(orb)
            pr=V[i][:6]
            data.append((w,pr))
        m=0
        for fn in Kcons:
            W=sum(w for w,pr in data if fn(pr))
            m=max(m,W)
        maxW[name]=m
    req(maxW=={"a1":3,"a2":3,"a3":5,"c":6},"Kc conic weighted maxima")

    bounds={}
    for name,P2 in p2.items():
        bounds[name]=reduce_frac(16*(1568-P2),P2)
    req(bounds=={
      "a1":(96,43),"a2":(96,43),"a3":(192,37),
      "b1":(192,37),"b2":(320,29),"b3":(160,39),"c":(288,31)
    },"root degree bounds")

    # Certificate checks.
    for name in ("a1","a2","a3","c"):
        c=cert["kc_quotient_gate"]["coordinate_data"][name]
        req(c["P2"]==p2[name],"cert P2 "+name)
        req(c["max_weighted_incidence_on_44_conics"]==maxW[name],"cert W "+name)
    req(cert["kb_remaining"]["b1"]["possible_positive_root_degrees"]==[2],"Kb b1")
    req(cert["kb_remaining"]["b2"]["possible_positive_root_degrees"]==[2,3],"Kb b2")
    req(cert["kb_remaining"]["b3"]["possible_positive_root_degrees"]==[2],"Kb b3")
    for k,v in cert["credit_firewall"].items():
        req(v is False,"credit "+k)

    print("PASS STAGE32_MB104_P6B_KNOWN_CURVE_KC_QUOTIENT_GATE_V1")
    print("surface92 max supported nodes C1/C2/C3 = 3/5/3; all pairings positive")
    print("Kc weighted conic maxima a1/a2/a3/c = 3/3/5/6; threshold=8")
    print("Kb residual: b1 d=2; b2 d=2,3; b3 d=2")
    print("whole_P6_closed=false credit=zero")

if __name__=="__main__":
    main()
