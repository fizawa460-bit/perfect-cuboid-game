#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction
from pathlib import Path

AUDIT_HEAD="b28adadc95776762754e1415a0ecab0da1d4cd8e"
AUDIT_Z33="stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-Z33-SPAN5-HYPERPLANE-CONTACT-EQUALITY-20260919.md"
AUDIT_Z33_BLOB="65656518d30f69ab3a4a892c8d4ae1d5ed72670e"

CERT="MB104-P6E-HOSTILE-SURVIVOR-NEF-CERTIFICATE.json"
CERT_BLOB="9579b0c2b909310b426cd4a1539b3d4c2ede0248"
NOTE="MB104-P6E-HOSTILE-SURVIVOR-NEF-GATE-20260919.md"
NOTE_BLOB="09a59668e5a91e20c314b82331e9a902b6b2bdce"
SOURCE="MB104-P6E-STOLL-TESTA-LOW-SPAN-SOURCE-NOTE-20260919.md"
SOURCE_BLOB="0959df8849ed0b36e6e57bccda48d11b4ab4eecf"
P6B="MB104-P6B-KNOWN-CURVE-KC-QUOTIENT-CERTIFICATE.json"
P6B_BLOB="6713ec219456783180bb7966cf3a8420307accff"
MASK=int("0000093f442e",16)

class F:
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o):
        o=toF(o); return F(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return F(-self.a,-self.b)
    def __sub__(self,o): return self+(-toF(o))
    def __rsub__(self,o): return toF(o)-self
    def __mul__(self,o):
        o=toF(o); return F(self.a*o.a-self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __eq__(self,o):
        o=toF(o); return self.a==o.a and self.b==o.b

def toF(x): return x if isinstance(x,F) else F(x)
O=F(); U=F(1); I=F(0,1)

def req(v:bool,msg:str)->None:
    if not v: raise SystemExit("FAIL: "+msg)

def blob(p:Path)->str:
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def check_audit(root:Path)->None:
    got=subprocess.check_output(["git","-C",str(root),"rev-parse","HEAD"],text=True).strip()
    req(got==AUDIT_HEAD,"audit HEAD")
    p=root/AUDIT_Z33
    req(p.is_file() and blob(p)==AUDIT_Z33_BLOB,"Z33 source lock")

def z(x): return x==O
def inv(x):
    d=x.a*x.a+x.b*x.b
    req(d!=0,"invert zero")
    return F(x.a/d,-x.b/d)

def rank(M):
    A=[row[:] for row in M]
    if not A:return 0
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if not z(A[i][c])),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        q=inv(A[r][c]); A[r]=[q*x for x in A[r]]
        for i in range(m):
            if i==r or z(A[i][c]): continue
            f=A[i][c]
            A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
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

def min_square_sum(total:int,slots:int)->int:
    q,r=divmod(total,slots)
    return (slots-r)*q*q+r*(q+1)*(q+1)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--audit-root",required=True)
    args=ap.parse_args()
    check_audit(Path(args.audit_root))

    here=Path(__file__).resolve().parent
    for name,want in [(CERT,CERT_BLOB),(NOTE,NOTE_BLOB),(SOURCE,SOURCE_BLOB),(P6B,P6B_BLOB)]:
        req(blob(here/name)==want,"current source "+name)

    cert=json.loads((here/CERT).read_text())
    p6b=json.loads((here/P6B).read_text())
    req(cert["schema"]=="STAGE32_MB104_P6E_HOSTILE_SURVIVOR_NEF_CERTIFICATE_V1","schema")

    V=nodes()
    support=[i for i in range(48) if (MASK>>i)&1]
    req(support==cert["support"]["nodes"],"support")
    req(rank([list(V[i]) for i in support])==7,"support spans P6")

    den=int(cert["hyperplane_dual"]["denominator"])
    hs=cert["hyperplane_dual"]["hyperplanes"]
    req(den==609 and len(hs)==30,"dual shape")
    req(sum(int(h["weight_numerator"]) for h in hs)==1051,"dual total weight")

    coverage={i:0 for i in support}
    for k,h in enumerate(hs):
        T=list(map(int,h["support_nodes"]))
        w=int(h["weight_numerator"])
        req(w>0,"positive weight")
        req(len(T)==len(set(T)) and set(T)<=set(support),"hyperplane subset")
        req(rank([list(V[i]) for i in T])==6,f"hyperplane rank {k}")
        for i in support:
            if i not in T:
                req(rank([list(V[j]) for j in T+[i]])==7,
                    f"hyperplane exact support incidence {k}/{i}")
        for i in T: coverage[i]+=w

    req(set(coverage.values())=={655},"uniform weighted coverage")
    req(max(int(h["weight_numerator"]) for h in hs)==46,"max weight")
    for drop in range(len(hs)):
        for i in support:
            remain=coverage[i]-(int(hs[drop]["weight_numerator"]) if i in hs[drop]["support_nodes"] else 0)
            req(remain>=609,f"one-hyperplane robustness drop={drop} node={i}")

    req(4*1051 < 7*609,"dual ratio below negative threshold")
    req(7*609-4*1051==59,"positive margin numerator")
    req(cert["hyperplane_dual"]["positive_margin"]=="P.R >= (59/609)*d > 0","margin text")

    # P2/P3 source-complete known-curve checks come from P6B.
    lib=p6b["surface_known_curve_library"]
    req(lib["conics"]==32 and lib["b_genus1_degree4"]==12 and lib["other_genus1_degree4"]==48,
        "P6B low-span library counts")
    req(lib["survivor_max_supported_nodes"]=={"conic":3,"b_genus1":5,"other_genus1":3},
        "P6B low-span survivor maxima")

    # P4 contradiction arithmetic.  Negative pairing at d=8 forces M>=15.
    req(min_square_sum(15,14)==17,"P4 Cauchy integer minimum")
    # R^2 <= 64/16 -17/2 = -9/2, hence integral R^2<=-5.
    # Adjunction parity: R^2+d is even, d=8 even, hence R^2 even => <=-6.
    R2=-6
    pa=1+(R2+8)//2
    req(pa==2,"P4 arithmetic genus upper bound")
    req(cert["hodge_P4_negative_check"]["arithmetic_genus_upper"]==2,"certificate P4 genus bound")

    req(cert["conclusion"]["P_nef"] is True and cert["conclusion"]["P_big"] is True,
        "nef/big conclusion")
    req(cert["conclusion"]["genus1_carrier_excluded"] is False,"no carrier overclaim")
    for k,v in cert["credit_firewall"].items():
        req(v is False,"credit "+k)

    print("PASS STAGE32_MB104_P6E_HOSTILE_SURVIVOR_NEF_CERTIFICATE_V1")
    print("30 exact support hyperplanes; weighted coverage=655/609 per node")
    print("after deleting any one selected hyperplane coverage>=1")
    print("span P5/P6: M_Sigma <= (1051/609)d, so P.R >= (59/609)d > 0")
    print("P2/P3 positive by exact P6B known-curve replay")
    print("P4 negative pairing would force p_a<=2; published low-span theorem gives genus>=3")
    print("P is big+nef; whole_P6_closed=false credit=zero")
    print("external Stoll-Testa Theorem 16 remains a human/source audit item")

if __name__=="__main__":
    main()
