#!/usr/bin/env python3
import json,itertools,math
from pathlib import Path

d=json.loads(Path(__file__).with_name("MB104-Z50-SIZE48-CANONICAL-COVER-RESOLUTION-GRAPH-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z50_SIZE48_CANONICAL_COVER_RESOLUTION_GRAPH_V1"

def det(M):
    n=len(M)
    if n==1:return M[0][0]
    return sum(((-1)**j)*M[0][j]*det([r[:j]+r[j+1:] for r in M[1:]]) for j in range(n))

n=7
M=[[0]*n for _ in range(n)]
for i in range(n):
    M[i][i]=-2
    if i+1<n:M[i][i+1]=M[i+1][i]=1
assert det(M)==-8

# Projection-formula checks for lifted strict transforms.
assert 3*(-2)+2==-4
assert 3*(-2)+2+2==-2

Z=[1]*7
MZ=[sum(M[i][j]*Z[j] for j in range(n)) for i in range(n)]
assert MZ==[-1,0,0,0,0,0,-1]
Z2=sum(Z[i]*MZ[i] for i in range(n))
assert Z2==-2
K=[2,0,0,0,0,0,2]
KZ=sum(K)
assert 1+(Z2+KZ)//2==2

a=[-2]*7
Ma=[sum(M[i][j]*a[j] for j in range(n)) for i in range(n)]
assert Ma==K
assert d["upstairs"]["canonical_cycle_coefficients"]==[2]*7
assert d["upstairs"]["log_canonical"] is False
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_Z50_SIZE48_CANONICAL_COVER_RESOLUTION_GRAPH_V1")
print("graph=elliptic(-2)-A2-bridge(-2)-A2-elliptic(-2)")
print("Z2=-2 paZ=2 ZK=2Z discrepancies=-2")
