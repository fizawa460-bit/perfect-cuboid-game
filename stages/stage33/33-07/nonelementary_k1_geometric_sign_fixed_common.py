#!/usr/bin/env python3
"""Exact helpers for k=1 pure-geometric seven-sign fixed-filtration census.

The source subgroup has type Z/4 + (Z/2)^7 and order 2^9 inside
A0=(Z/8)^10+(Z/16)^4.  The seven involutions are literal coordinate-K3
block signs.  No arithmetic cc/ct action is used.
"""
import math

NVAR=14
MODS0=[8]*10+[16]*4
QDIAG=[2]*10+[1]*4
TARGET_MODS=[2]*4+[4]*6+[8]*4
PIECE_COORDS=((0,1),(2,3),(4,5),(6,10),(7,11),(8,12),(9,13))
ALL14=(1<<14)-1
A0_LOG2=46
H_LOG2=9


def canon(rows):
    piv={}
    for raw in rows:
        x=int(raw)
        for p in sorted(piv,reverse=True):
            if (x>>p)&1:x^=piv[p]
        if not x:continue
        p=x.bit_length()-1
        for old in list(piv):
            if (piv[old]>>p)&1:piv[old]^=x
        piv[p]=x
    return tuple(piv[p] for p in sorted(piv,reverse=True))


def rank(rows):return len(canon(rows))


def contains(basis,x):
    y=int(x)
    for b in canon(basis):
        p=b.bit_length()-1
        if (y>>p)&1:y^=b
    return y==0


def complement(base,whole):
    cur=list(canon(base));out=[]
    for v in canon(whole):
        if rank(cur+[v])>len(canon(cur)):
            cur.append(v);out.append(v)
    return tuple(out)


FULL14=canon(1<<j for j in range(14))


def actual_order4_row(low,high):
    row=[]
    for j in range(14):
        normalized=((int(low)>>j)&1)+2*((int(high)>>j)&1)
        scale=2 if j<10 else 4
        row.append((scale*normalized)%MODS0[j])
    return tuple(row)


def actual_order2_row(bits):
    return tuple((4 if j<10 else 8) if (int(bits)>>j)&1 else 0 for j in range(14))


def reconstruct_H(record,solution):
    P=tuple(map(int,record['P_basis_bits']))
    W=tuple(map(int,record['W_basis_bits']))
    if len(P)!=1 or len(W)!=8:raise SystemExit('k1 structural shape regression')
    qb=complement(W,FULL14)
    if len(qb)!=6:raise SystemExit('k1 lift quotient dimension regression')
    c=0
    for bit,v in enumerate(qb):
        if (int(solution)>>bit)&1:c^=int(v)
    rows=[actual_order4_row(P[0],c)]
    wc=complement(P,W)
    if len(wc)!=7:raise SystemExit('W/P complement regression')
    rows.extend(actual_order2_row(v) for v in wc)
    if len(rows)!=8:raise SystemExit('k1 H generator count regression')
    return tuple(rows)


def q32(a):return sum(c*int(x)*int(x) for c,x in zip(QDIAG,a))%32

def b16(a,b):return sum(c*int(x)*int(y) for c,x,y in zip(QDIAG,a,b))%16


def verify_isotropic_H(rows):
    if len(rows)!=8:raise SystemExit('k1 H row count regression')
    for i,r in enumerate(rows):
        if q32(r):raise SystemExit('nonisotropic H generator')
        for j in range(i):
            if b16(r,rows[j]):raise SystemExit('nonorthogonal H generators')


def all_sections_stable_under_signs(record):
    """Section-independent descent criterion for all seven coordinate signs."""
    P=tuple(map(int,record['P_basis_bits']))
    W=tuple(map(int,record['W_basis_bits']))
    for coords in PIECE_COORDS:
        pos=sum(1<<j for j in coords);neg=ALL14^pos
        if any(not contains(W,p&neg) for p in P):return False
    return True


def parity_bits(g):
    out=0
    for j,x in enumerate(g):
        if int(x)&1:out|=1<<j
    return out


def dependency_basis(vecs):
    piv={};deps=[]
    for i,v0 in enumerate(vecs):
        v=int(v0);coef=1<<i
        while v:
            p=v.bit_length()-1
            if p in piv:
                old,c=piv[p];v^=old;coef^=c
            else:
                piv[p]=(v,coef);break
        if not v:deps.append(coef)
    return len(piv),tuple(deps)


def subgroup_log2(generators,moduli):
    gens=[tuple(int(x)%int(m) for x,m in zip(g,moduli)) for g in generators]
    gens=[g for g in dict.fromkeys(gens) if any(g)]
    if not gens:return 0
    r,deps=dependency_basis([parity_bits(g) for g in gens])
    keep=[j for j,m in enumerate(moduli) if int(m)>2]
    if not keep:return r
    mods2=tuple(int(moduli[j])//2 for j in keep)
    nxt=[]
    for g in gens:
        h=tuple(int(g[j])%mods2[k] for k,j in enumerate(keep))
        if any(h):nxt.append(h)
    for cm in deps:
        sums=[0]*len(moduli)
        for i,g in enumerate(gens):
            if (int(cm)>>i)&1:
                for j,m in enumerate(moduli):sums[j]=(sums[j]+int(g[j]))%int(m)
        if any(x&1 for x in sums):raise SystemExit('parity dependency lift regression')
        h=tuple((sums[j]//2)%mods2[k] for k,j in enumerate(keep))
        if any(h):nxt.append(h)
    return r+subgroup_log2(nxt,mods2)


def fixed_Qpower_log2_direct(Hrows,piece_index,power):
    """Exact log2 |Fix_s((Hperp/H)[power])| directly in A0."""
    if power not in (2,4):raise ValueError(power)
    n=len(Hrows)
    if n!=8:raise SystemExit('k1 fixed-filtration H row regression')
    codmods=(16,)*n+tuple(MODS0)+tuple(MODS0)
    width=n+28;gens=[];positive=set(PIECE_COORDS[int(piece_index)])
    for j,m in enumerate(MODS0):
        row=[0]*width
        for i,h in enumerate(Hrows):row[i]=(QDIAG[j]*int(h[j]))%16
        row[n+j]=int(power)%m
        row[n+14+j]=(0 if j in positive else -2)%m
        gens.append(tuple(row))
    for h in Hrows:
        row=[0]*width
        for j,m in enumerate(MODS0):row[n+j]=(-int(h[j]))%m
        gens.append(tuple(row))
    for h in Hrows:
        row=[0]*width
        for j,m in enumerate(MODS0):row[n+14+j]=(-int(h[j]))%m
        gens.append(tuple(row))
    kernel_log=A0_LOG2+2*H_LOG2-subgroup_log2(gens,codmods)
    fixed_log=kernel_log-H_LOG2
    if not (0<=fixed_log<=28):raise SystemExit('fixed subgroup log regression')
    return fixed_log


def restrict_action_to_power(A,mods,power):
    gm=[math.gcd(int(m),int(power)) for m in mods]
    step=[int(m)//g for m,g in zip(mods,gm)]
    B=[]
    for i in range(len(mods)):
        row=[]
        for j in range(len(mods)):
            val=(step[i]*int(A[i][j]))%int(mods[j])
            if val%step[j]:raise SystemExit('restricted action expression regression')
            row.append((val//step[j])%gm[j])
        B.append(tuple(row))
    return tuple(B),tuple(gm)


def fixed_log2_from_action(A,mods,power):
    B,gm=restrict_action_to_power(A,mods,power)
    image=[]
    for i,row in enumerate(B):
        image.append(tuple((int(row[j])-(1 if i==j else 0))%gm[j] for j in range(len(gm))))
    return sum(int(m).bit_length()-1 for m in gm)-subgroup_log2(image,gm)
