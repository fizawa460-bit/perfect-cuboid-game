#!/usr/bin/env python3
from itertools import product
from collections import Counter
from math import gcd

MODS=[2,2,2,4,4]
assert 2*2*2*4*4==128
RES3=[73,97,235]
SELECTED={73:0,97:1,235:2}
NORMS=[9,137,9]
AQ=[[4, 0, -2, -4, 2, -4, -3, 0], [0, 8, 4, -4, 4, 4, 0, -6], [-2, 4, 4, 0, 1, 4, 2, -4], [-4, -4, 0, 8, -4, 2, 4, 4], [2, 4, 1, -4, 4, 0, -2, -4], [-4, 4, 4, 2, 0, 8, 4, -4], [-3, 0, 2, 4, -2, 4, 4, 0], [0, -6, -4, 4, -4, -4, 0, 8]]
P=[[0, -2, -2, -1], [1, 2, 1, 0], [0, 0, 1, 0], [0, 1, 0, 0]]
PINV=[[0, 1, -1, -2], [0, 0, 0, 1], [0, 0, 1, 0], [-1, 0, -2, -2]]
SUM=[[0, 0, 0, 1, 0, 0, 0, -1, 0, -1], [0, 0, 0, 0, -1, 0, -1, 0, -1, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 0, -1, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, -1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0, 0, -1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0, 1]]
SUMINV2=[[0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, -1, 1, -1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, -1, 0, 0, 0], [0, 0, 0, 0, -1, 0, 0, 0, 1, 0], [-1, 0, 0, 0, 0, -1, 0, 1, 0, 1], [0, -1, -1, 1, 1, 0, 0, 0, -1, 0], [0, 0, 0, 0, 0, 1, 0, -1, 0, 0]]
IFIX=[[1, -2], [1, -1]]
PIVROWS=[0, 1, 2, 3, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 21, 23, 25, 26, 41, 43, 45, 46, 51, 52, 53, 55, 56, 57, 101]
OBS=[[2, -4, 12, 0, -6, -2, 4, 2, 0, 0, -1, -4, 0, 0, 0, -2, -2, 1, 0, 0, 1, 0, 0, 2, 2, 4, 2, 0, 0, 0], [0, -2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, -4, 6, 0, -3, 0, 4, 1, 0, 0, 0, -8, 0, 0, 0, -4, -6, 0, 0, 0, 0, 2, 0, 4, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, -4, 0, 1, -3, 0, -2, 0, 2, -2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1]]
JINVS=[[[0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, -1, 0, -1, 0, 0], [0, 0, 0, 0, 0, -1, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, -1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]], [[0, -1, 0, 1, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, -1, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, -1, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0, -1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, -1, 1, 0, 0, 0, 0, 0]], [[0, 1, 0, -1, 1, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 1, -1, 0, 1], [0, 0, 0, 0, 0, 0, -1, 0, 0, 0], [1, 0, 0, 0, 0, -1, -1, 0, 0, -1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, -1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, -1, 0, 1, 0, 0, 0, 0, 1, 0]], [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, -1, 1, 0, 0], [0, 0, 0, 0, 0, -1, 0, -1, 0, 0], [0, 0, 0, 0, 0, 0, 0, -1, 0, 0], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, -1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,v): return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]
def q(v): return sum(v[i]*AQ[i][j]*v[j] for i in range(8) for j in range(8))
def bits(r): return tuple((r>>i)&1 for i in range(8))
def gopts(n,typ):
    out=[]; lim=int(n**0.5)
    for a in range(-lim,lim+1):
      for b in range(-lim,lim+1):
        if a*a+b*b==n and ((typ=="id" and a%2 and b%2==0) or (typ=="i" and a%2==0 and b%2)):
            out.append((a,b))
    return out

def TA(t):
    a11,b11,a12,b12,a21,b21,a22,b22=t
    R=[[a11,a12,-2*b11,-2*b12],[a21,a22,-2*b21,-2*b22],
       [b11,b12,a11,a12],[b21,b22,a21,a22]]
    R[2]=[2*x for x in R[2]]; R[3]=[2*x for x in R[3]]
    assert all(R[i][j]%2==0 for i in range(4) for j in (2,3))
    for i in range(4): R[i][2]//=2; R[i][3]//=2
    return mm(mm(P,R),PINV)

def build(t,gp,assert_integral=True):
    M=[[0]*10 for _ in range(10)]; A=TA(t)
    for i in range(4):
      for j in range(4): M[i][j]=A[i][j]
    off=4
    for a,b in gp:
      G=[[a*(i==j)+b*IFIX[i][j] for j in range(2)] for i in range(2)]
      for i in range(2):
        for j in range(2): M[off+i][off+j]=G[i][j]
      off+=2
    N=mm(mm(SUM,M),SUMINV2)
    integral=all(x%2==0 for row in N for x in row)
    if assert_integral: assert integral
    return ([[x//2 for x in row] for row in N] if integral else None),integral

def obstruction(F,JI):
    B=mm(F,JI); k=[0]*102; k[0]=81; k[101]=105; z=1
    for i in range(10):
      for j in range(10): k[z]=B[i][j]; z+=1
    y=mv(OBS,[k[i] for i in PIVROWS])
    ob=tuple(y[i]%MODS[i] for i in range(5))
    order=1
    for v,d in zip(ob,MODS):
      if v:
        o=d//gcd(v,d); order=order*o//gcd(order,o)
    return ob,order

lifts={}
for r in RES3:
  b=bits(r); L=[]
  for s in product((0,1),repeat=8):
    t=tuple(b[i]+2*s[i] for i in range(8))
    if q(t)%8==2: L.append(t)
  assert len(L)==128
  lifts[r]=L

def one_choice(sel):
  return tuple(gopts(n,"i" if j==sel else "id")[0] for j,n in enumerate(NORMS))

for r in RES3:
  for s in range(3):
    _,ok=build(lifts[r][0],one_choice(s),False)
    assert ok==(s==SELECTED[r])

counts=[Counter() for _ in range(4)]
orders=[Counter() for _ in range(4)]
byres=[Counter() for _ in range(4)]
total=0
for r in RES3:
  opts=[gopts(n,"i" if j==SELECTED[r] else "id") for j,n in enumerate(NORMS)]
  assert [len(x) for x in opts]==[2,4,2]
  gs=list(product(*opts)); assert len(gs)==16
  for t in lifts[r]:
    for gp in gs:
      F,ok=build(t,gp); assert ok; total+=1
      for j,JI in enumerate(JINVS):
        ob,o=obstruction(F,JI); counts[j][ob]+=1; orders[j][o]+=1; byres[j][(r,ob,o)]+=1
assert total==6144
EXP={(1,1,1,2,0):3072,(1,1,1,0,2):3072}
for j in range(4):
  assert dict(counts[j])==EXP
  assert dict(orders[j])=={2:6144}
  for r in RES3:
    assert byres[j][(r,(1,1,1,2,0),2)]==1024
    assert byres[j][(r,(1,1,1,0,2),2)]==1024

t0=lifts[73][0]; gp=one_choice(SELECTED[73]); F0,_=build(t0,gp)
for i in range(8):
  t=list(t0); t[i]+=4; F1,_=build(tuple(t),gp)
  for JI in JINVS: assert obstruction(F0,JI)==obstruction(F1,JI)

for C in counts:
  for ob in C:
    assert any(ob) and all((2*ob[i])%MODS[i]==0 for i in range(5))

QST=list(range(210,267,2)); assert len(QST)==29
print("PASS_EX1_05AF_ALL_6144_ASSEMBLIES_HAVE_ORDER2_NS_DESCENT_OBSTRUCTION")
print("pullback_cokernel","(Z/2)^3 x (Z/4)^2","index",128)
print("assemblies",total,"primitive_descent_success",0)
print("obstruction_distribution",dict(counts[0]))
print("residues",RES3,"Q_states",len(QST),"h4_states_excluded_candidate",29)
