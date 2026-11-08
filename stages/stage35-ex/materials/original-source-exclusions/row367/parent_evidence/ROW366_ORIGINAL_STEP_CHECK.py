#!/usr/bin/env python3
"""Row366: exact formal-branch checks and GF(2) halving-coset combinatorics.
This is not a Kummer evaluation of beta and is not an n_(4,Gamma) certificate.
"""
import json,zipfile
from pathlib import Path
root=Path('/mnt/data')
zp=root/'STAGE35EX_R3_07_DYADIC_TORSION_TRANSVERSE_20261105_EVIDENCE.zip'
with zipfile.ZipFile(zp) as z:
    base='STAGE35EX_R3_07_DYADIC_TORSION_TRANSVERSE_20261105/math/'
    d=json.loads(z.read(base+'parents/rank6.json'))
    c=json.loads(z.read(base+'dyadic_transversality_certificate.json'))
A=d['A_coefficients_ascending'];B=d['B_coefficients_ascending'];h=d['h2_coefficients_ascending']
def ev(cs,x):
    r=0
    for a in cs[::-1]:r=r*x+a
    return r
assert len(h)==37 and len(A)==19 and len(B)==18
for x in (0,16,48,80,16*9,16*25,32,64):
    a,b=ev(A,x),ev(B,x)
    assert a*a-x*b*b==ev(h,x)
    # Z^2+A Z = -X*(B/2)^2; solve unique branch modulo 2^128
    assert a%2==1 and b%4==0
    N=128;Z=0
    for k in range(N):
        f=(Z*Z+a*Z+x*(b//2)**2)%(1<<(k+1))
        if f:Z+=1<<k
    assert (Z*Z+a*Z+x*(b//2)**2)%(1<<N)==0
    assert ((a+2*Z)**2-ev(h,x))%(1<<N)==0
    if x:
        v=0;t=Z
        while t and t%2==0:v+=1;t//=2
        print(f'X={x:5d} mod32={x%32:2d} Z mod2^16={Z%65536:5d} v2(Z)={v} Y mod2^16={(a+2*Z)%65536:5d}')
# For every depth-4 x, x mod32=16; formal continuity gives common beta.
# abstract local 19-dimensional quotient: 7 known vectors, 2 residual Selmer vectors, 2 transverse torsion vectors.
N=19
W={i for i in range(1<<7)} # 128 known translations including genuine D_inf in one generator
T={0, 1<<9, 1<<10, (1<<9)|(1<<10)}
H={i for i in range(1<<9)}
WT={a^b for a in W for b in T}
HT={a^b for a in H for b in T}
assert len(W)==128 and len(T)==4 and len(H)==512
assert len(WT)==512 and len(HT)==2048
assert (WT&H)==W
assert len(WT)+len(HT-WT)+((1<<N)-len(HT))==(1<<N)
for name,beta in [('tail-possible',1<<9),('bad',1<<7),('good',1<<11)]:
    # q contributions for halving exponent 0,1,2 exactly.
    q0=W
    q1=WT
    q2={beta^a for a in WT}
    print(name,'q0',len(q0),'q1',len(q1),'q2',len(q2),'q2_inter_H',len(q2&H),'q2_bad',len((q2&H)-W),'n_ge_3_possible',beta in WT)
print('beta categories: tail-possible',len(WT),'bad-depth4',len(HT-WT),'good-depth4',((1<<N)-len(HT)))
print('CHECK_PASS: branch equation for 7 nonzero X + GF(2) exhaustive beta categorization. Actual beta NOT computed.')
