#!/usr/bin/env python3
"""Exact helpers for k=2 geometric seven-sign fixed-filtration census.

The seven source involutions are literal integral block-scalar actions on
L0=<8>^10 + <16>^4: +1 on one coordinate-K3 rank-2 block and -1 on the
other six blocks.  No arithmetic cc/ct action appears here.
"""
import math

NVAR=14
MODS0=[8]*10+[16]*4
QDIAG=[2]*10+[1]*4
TARGET_MODS=[2]*4+[4]*6+[8]*4
PIECE_COORDS=((0,1),(2,3),(4,5),(6,10),(7,11),(8,12),(9,13))
ALL14=(1<<14)-1
H_COEFF_LOG2=9
A0_LOG2=46


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


def free_variables(rref):
    piv=set()
    for z in rref:
        c=int(z)&((1<<NVAR)-1)
        if not c:raise SystemExit('zero affine row')
        piv.add(c.bit_length()-1)
    return tuple(i for i in range(NVAR) if i not in piv)


def solution_from_free(rref,free,mask):
    sol=0
    for j,v in enumerate(free):
        if (int(mask)>>j)&1:sol|=1<<v
    for z in reversed(rref):
        c=int(z)&((1<<NVAR)-1);p=c.bit_length()-1
        rhs=((int(z)>>NVAR)&1)^((c&sol).bit_count()&1)
        if rhs:sol|=1<<p
    return sol


def order4_corrections(p_basis,qbasis,solution):
    q=len(qbasis);out=[]
    for g in range(len(p_basis)):
        c=0
        for b,v in enumerate(qbasis):
            if (int(solution)>>(q*g+b))&1:c^=int(v)
        out.append(c)
    return tuple(out)


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
    p=tuple(map(int,record['P_basis_bits']))
    w=tuple(map(int,record['W_basis_bits']))
    qb=tuple(map(int,record['quotient_basis_bits']))
    if len(p)!=2 or len(w)!=7 or len(qb)!=7:raise SystemExit('k2 structural shape regression')
    corr=order4_corrections(p,qb,solution)
    rows=[actual_order4_row(a,b) for a,b in zip(p,corr)]
    wc=complement(p,w)
    if len(wc)!=5:raise SystemExit('W/P complement regression')
    rows.extend(actual_order2_row(x) for x in wc)
    if len(rows)!=7:raise SystemExit('H generator count regression')
    return tuple(rows)


def q32(a):return sum(c*int(x)*int(x) for c,x in zip(QDIAG,a))%32

def b16(a,b):return sum(c*int(x)*int(y) for c,x,y in zip(QDIAG,a,b))%16

def verify_isotropic_H(rows):
    for i,r in enumerate(rows):
        if q32(r):raise SystemExit('nonisotropic H generator')
        for j in range(i):
            if b16(r,rows[j]):raise SystemExit('nonorthogonal H generators')


def all_sections_stable_under_signs(record):
    """Section-independent exact criterion.

    For h=p+2c in normalized order-4 coordinates, a block sign changes h-h'
    by 2*(p restricted to the negated coordinates); c cancels.  The order-two
    part of H is exactly W.  Hence stability for every affine lift is the
    F2 membership condition below.  Order-two generators are sign-fixed
    because -x=x on elements of order two.
    """
    P=tuple(map(int,record['P_basis_bits']));W=tuple(map(int,record['W_basis_bits']))
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
    """Exact log2 order of a generated subgroup of a finite 2-group.

    Recursively reduce modulo 2.  If S<=C, then
      |S| = |image(S -> C/2C)| * |S cap 2C|,
    and division by 2 identifies S cap 2C with a subgroup of the halved
    ambient 2-group.  Dependencies of generator parity rows plus doubles of
    generators generate that kernel exactly.
    """
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
    """Count Fix((Hperp/H)[power]) directly in A0, without a quotient basis.

    A class x+H lies in Q[power] and is fixed by sign s exactly when
      x in Hperp, power*x in H, (s-1)x in H.
    The two H-membership witnesses are unique because the seven H generators
    give H ~= (Z/4)^2 + (Z/2)^5.  Thus an exact kernel count of this finite
    homomorphism, divided by |H|=2^9, is the desired fixed subgroup order.
    """
    if power not in (2,4):raise ValueError(power)
    codmods=(16,)*7+tuple(MODS0)+tuple(MODS0)
    gens=[];positive=set(PIECE_COORDS[int(piece_index)])
    for j,m in enumerate(MODS0):
        row=[0]*35
        for i,h in enumerate(Hrows):row[i]=(QDIAG[j]*int(h[j]))%16
        row[7+j]=int(power)%m
        row[21+j]=(0 if j in positive else -2)%m
        gens.append(tuple(row))
    for h in Hrows:
        row=[0]*35
        for j,m in enumerate(MODS0):row[7+j]=(-int(h[j]))%m
        gens.append(tuple(row))
    for h in Hrows:
        row=[0]*35
        for j,m in enumerate(MODS0):row[21+j]=(-int(h[j]))%m
        gens.append(tuple(row))
    domain_log=A0_LOG2+2*H_COEFF_LOG2
    kernel_log=domain_log-subgroup_log2(gens,codmods)
    fixed_log=kernel_log-H_COEFF_LOG2
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
