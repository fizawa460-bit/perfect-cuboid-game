#!/usr/bin/env python3
from collections import Counter

VALUES={
    "0":(0,1),"inf":(1,0),"1":(1,1),"-1":(-1,1),
    "i":(1j,1),"-i":(-1j,1),
}

def require(c,msg):
    if not c:
        raise SystemExit("FAIL: "+msg)

def nodes():
    out=[]
    for j in range(3):
        for sa in (1,-1):
            for s1 in (1,-1):
                for s2 in (1,-1):
                    z=[0j]*7
                    z[j]=sa
                    o=[t for t in range(3) if t!=j]
                    z[3+o[0]],z[3+o[1]],z[6]=s1,s2,1
                    out.append(tuple(z))
    for j in range(3):
        o=[t for t in range(3) if t!=j]
        a,b=o
        for sr in (1,-1):
            for ep in (1,-1):
                for eq in (1,-1):
                    z=[0j]*7
                    z[a],z[b],z[3+a],z[3+b]=1,1j*sr,1j*ep,-eq*sr
                    out.append(tuple(z))
    require(len(out)==48 and len(set(out))==48,"48-node model")
    return out

def classify(p,q):
    hits=[]
    for lab,(a,b) in VALUES.items():
        if p*b==a*q:
            hits.append(lab)
    require(len(hits)==1,f"unique projective label {p}:{q}")
    return hits[0]

def tpair(z):
    a1,a2,a3,b1,b2,b3,c=z
    A=c+a3; B=c-a3; U=a1-1j*a2; V=a1+1j*a2
    tz=classify(A,U) if not (A==0 and U==0) else classify(V,B)
    tw=classify(A,V) if not (A==0 and V==0) else classify(U,B)
    return tz,tw

V=nodes()
mask=int("000707000f0f",16)
S=[i for i in range(48) if (mask>>i)&1]
require(S==[0,1,2,3,8,9,10,11,24,25,26,32,33,34],"support indices")

pairs={i:tpair(V[i]) for i in S}
expect={}
for i in [0,1,2,3]: expect[i]=("1","1")
for i in [8,9,10,11]: expect[i]=("i","-i")
for i in [24,25,26]: expect[i]=("-1","1")
for i in [32,33,34]: expect[i]=("i","i")
require(pairs==expect,"exact four occupied cells")

c=Counter(pairs.values())
require(c==Counter({("1","1"):4,("i","-i"):4,("-1","1"):3,("i","i"):3}),"cell counts")

f1=Counter(a for a,b in pairs.values())
f2=Counter(b for a,b in pairs.values())
require(f1==Counter({"i":7,"1":4,"-1":3}),"factor1 node counts")
require(f2==Counter({"1":7,"-i":4,"i":3}),"factor2 node counts")

# Each node carries 8l unramified branches in the dangerous equality packet.
u1={q:8*f1[q] for q in VALUES}
u2={q:8*f2[q] for q in VALUES}
require([u1[q] for q in ("1","-1","i","-i","0","inf")]==[32,24,56,0,0,0],"factor1 u/l")
require([u2[q] for q in ("1","-1","i","-i","0","inf")]==[56,0,24,32,0,0],"factor2 u/l")
r1={q:(56-u1[q])//2 for q in VALUES}
r2={q:(56-u2[q])//2 for q in VALUES}
require([r1[q] for q in ("1","-1","i","-i","0","inf")]==[12,16,0,28,28,28],"factor1 r/l")
require([r2[q] for q in ("1","-1","i","-i","0","inf")]==[0,28,16,12,28,28],"factor2 r/l")

Q0={0,1,2,3,24,25,26,27}
Q1={8,9,10,11,32,33,34,35}
require(set(S)&Q0=={0,1,2,3,24,25,26},"Q0 seven-node packet")
require(set(S)&Q1=={8,9,10,11,32,33,34},"Q1 seven-node packet")
require({i for i in S if pairs[i][1]=="1"}==set(S)&Q0,"Q0 = factor2 +1 saturated fiber nodes")
require({i for i in S if pairs[i][0]=="i"}==set(S)&Q1,"Q1 = factor1 +i saturated fiber nodes")

print("PASS: Z5' 000707 e=4 exact X(4) grid")
print("cells:",dict(c))
print("factor1 +i and factor2 +1 each contain exactly seven supported nodes")
print("=> each carries 56l distinct unramified points, saturating a degree-56l fiber")
