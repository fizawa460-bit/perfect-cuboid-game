#!/usr/bin/env python3
from itertools import product

K1 = (
    (0,-1,1,-1),
    (0,1,0,1),
    (-1,1,-1,1),
    (-1,-1,0,0),
)
R = (
    (1,0,-2,-2),
    (-1,-1,0,0),
    (1,1,1,0),
    (0,0,-1,-1),
)
I4 = tuple(tuple(int(i==j) for j in range(4)) for i in range(4))

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)) for i in range(4))

def mpow(A,n):
    out=I4
    for _ in range(n): out=mm(out,A)
    return out

def rank_mod2(A):
    m=[[x&1 for x in row] for row in A]
    r=0
    for c in range(4):
        p=next((i for i in range(r,4) if m[i][c]),None)
        if p is None: continue
        m[r],m[p]=m[p],m[r]
        for i in range(4):
            if i!=r and m[i][c]: m[i]=[x^y for x,y in zip(m[i],m[r])]
        r+=1
    return r

def fixed_nonzero(A):
    M=[[A[i][j] ^ int(i==j) for j in range(4)] for i in range(4)]
    out=[]
    for v in product((0,1),repeat=4):
        if v==(0,0,0,0): continue
        if all(sum(M[i][j]*v[j] for j in range(4))%2==0 for i in range(4)):
            out.append(v)
    return out

assert mpow(K1,8)==I4 and mpow(K1,4)!=I4
assert mpow(R,8)==I4 and mpow(R,4)!=I4
assert fixed_nonzero(K1)==[(1,1,0,0)]
assert fixed_nonzero(R)==[(0,0,0,1)]
assert rank_mod2(tuple(tuple((R[i][j]-I4[i][j])&1 for j in range(4)) for i in range(4)))==3
print('PASS_STAGE32_SCRATCH_ORDER8_FIXED_LINE_REENTRY')
print('KKK_mu1_fixed_J2_unique=true retained_STinv_fixed_line=L2 residue=97 conditional_only=true')
