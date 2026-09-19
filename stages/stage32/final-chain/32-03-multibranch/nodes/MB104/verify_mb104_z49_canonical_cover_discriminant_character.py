#!/usr/bin/env python3
import json, itertools, math
from fractions import Fraction
from pathlib import Path

d=json.loads(Path(__file__).with_name("MB104-Z49-CANONICAL-COVER-DISCRIMINANT-CHARACTER-CERTIFICATE.json").read_text())

def det(M):
    n=len(M)
    if n==1: return M[0][0]
    return sum(((-1)**j)*M[0][j]*det([row[:j]+row[j+1:] for row in M[1:]]) for j in range(n))

def minor_gcd(M,k):
    rows=list(itertools.combinations(range(len(M)),k))
    cols=list(itertools.combinations(range(len(M[0])),k))
    g=0
    for rr in rows:
        for cc in cols:
            A=[[M[i][j] for j in cc] for i in rr]
            g=math.gcd(g,abs(det(A)))
    return g

M48=d["size48"]["matrix"]
assert det(M48)==-24
assert minor_gcd(M48,1)==1
assert minor_gcd(M48,2)==1
assert d["size48"]["smith"]==[1,1,24]
a48=[Fraction(-4,3)]*3
k48=[sum(Fraction(M48[i][j])*a48[j] for j in range(3)) for i in range(3)]
assert k48==[4,0,4]
assert all((3*x).denominator==1 for x in a48) and any(x.denominator==3 for x in a48)

M=d["size768"]["matrix"]
assert det(M)==33
assert minor_gcd(M,1)==1
assert minor_gcd(M,2)==1
assert minor_gcd(M,3)==1
assert d["size768"]["smith"]==[1,1,1,33]
a=[Fraction(-8,3),Fraction(-8,3),Fraction(-4,3),Fraction(-4,3)]
k=[sum(Fraction(M[i][j])*a[j] for j in range(4)) for i in range(4)]
assert k==[4,4,0,0]
assert all((3*x).denominator==1 for x in a) and any(x.denominator==3 for x in a)
assert d["result"]["unique_order3_cover_direction_up_to_inversion"] is True
assert d["result"]["analytic_holomorphic_lift_unique"] is False
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_Z49_CANONICAL_COVER_DISCRIMINANT_CHARACTER_V1")
print("A48=Z/24 A768=Z/33 canonical_order=3")
print("next=MB104-Z49B-SIZE48-PLUMBING-INDEX3-HOLOMORPHIC-LIFT")
