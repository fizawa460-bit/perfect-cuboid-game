#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"MB104-Z5P-EXACT-FACTOR-CUSP-PAIR-ADAPTER-CERTIFICATE.json"

def require(cond,msg):
    if not cond:
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
    require(len(out)==48 and len(set(out))==48,"canonical 48-node model")
    return out

VALUES={
    "0":(0,1),
    "inf":(1,0),
    "1":(1,1),
    "-1":(-1,1),
    "i":(1j,1),
    "-i":(-1j,1),
}

def classify(p,q):
    require(not (p==0 and q==0),"nonzero projective pair")
    hits=[]
    for lab,(a,b) in VALUES.items():
        if p*b==a*q:
            hits.append(lab)
    require(len(hits)==1,f"unique cusp label for [{p}:{q}]")
    return hits[0]

def tpair(z):
    a1,a2,a3,b1,b2,b3,c=z
    A=c+a3
    B=c-a3
    U=a1-1j*a2
    V=a1+1j*a2
    tz=classify(A,U) if not (A==0 and U==0) else classify(V,B)
    tw=classify(A,V) if not (A==0 and V==0) else classify(U,B)
    return tz,tw

d=json.loads(CERT.read_text())
V=nodes()
pairs=[tpair(z) for z in V]
cnt=Counter(pairs)
require(len(cnt)==12,"twelve factor cusp cells")
require(set(cnt.values())=={4},"each cell has four nodes")

by_type={"b1_zero":Counter(),"b2_zero":Counter(),"b3_zero":Counter()}
for z,p in zip(V,pairs):
    b1,b2,b3=z[3],z[4],z[5]
    zeros=[b1==0,b2==0,b3==0]
    require(sum(zeros)==1,"unique stabilizer zero")
    key=("b1_zero","b2_zero","b3_zero")[zeros.index(True)]
    by_type[key][p]+=1

expect_type={
 "b1_zero":{("1","1"),("1","-1"),("-1","1"),("-1","-1")},
 "b2_zero":{("i","i"),("i","-i"),("-i","i"),("-i","-i")},
 "b3_zero":{("0","0"),("0","inf"),("inf","0"),("inf","inf")},
}
for k,c in by_type.items():
    require(set(c)==expect_type[k],f"{k} four cells")
    require(set(c.values())=={4},f"{k} cell sizes")

host=set(d["hostile_support"])
require(len(host)==14 and min(host)>=0 and max(host)<48,"hostile support indices")

def matrix(rowlabs,collabs,which):
    m=[[0,0],[0,0]]
    for i in host:
        z=V[i]
        zero=(z[3]==0,z[4]==0,z[5]==0)
        key=("b1_zero","b2_zero","b3_zero")[zero.index(True)]
        if key!=which:
            continue
        r,c=tpair(z)
        m[rowlabs.index(r)][collabs.index(c)]+=1
    return m

m1=matrix(["1","-1"],["1","-1"],"b1_zero")
m2=matrix(["i","-i"],["i","-i"],"b2_zero")
m3=matrix(["0","inf"],["0","inf"],"b3_zero")
require(m1==d["hostile_matrices"]["b1_zero"],"hostile b1 matrix")
require(m2==d["hostile_matrices"]["b2_zero"],"hostile b2 matrix")
require(m3==d["hostile_matrices"]["b3_zero"],"hostile b3 matrix")
require([sum(map(sum,[m1])),sum(map(sum,[m2])),sum(map(sum,[m3]))]==[6,2,6],"hostile type totals")

# Node counts times 8l give exact unramified six-value passports.
f1_u=[8*sum(m1[0]),8*sum(m1[1]),8*sum(m2[0]),8*sum(m2[1]),8*sum(m3[0]),8*sum(m3[1])]
f2_u=[8*sum(row[0] for row in m1),8*sum(row[1] for row in m1),
      8*sum(row[0] for row in m2),8*sum(row[1] for row in m2),
      8*sum(row[0] for row in m3),8*sum(row[1] for row in m3)]
require(f1_u==[24,24,8,8,16,32],"factor1 unramified coefficients")
require(f2_u==[40,8,8,8,16,32],"factor2 unramified coefficients")
f1_r=[(56-x)//2 for x in f1_u]
f2_r=[(56-x)//2 for x in f2_u]
require(f1_r==[16,16,24,24,20,12],"factor1 ramification coefficients")
require(f2_r==[8,24,24,24,20,12],"factor2 ramification coefficients")
require(sum(f1_r)==112 and sum(f2_r)==112,"Riemann-Hurwitz totals")

print("PASS: Z5' exact factor X(4)-cusp pair adapter")
print("12 branch-value cells x 4 nodes; hostile matrices =",m1,m2,m3)
print("factor1 u coefficients =",f1_u)
print("factor2 u coefficients =",f2_u)
