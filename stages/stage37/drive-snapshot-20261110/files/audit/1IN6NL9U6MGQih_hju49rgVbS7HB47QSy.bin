"""TI-005: TI-004 character matrices plus a proved 2-adic row.
No rank-positive inference from a nonzero upper bound; no density claim.
"""
from math import gcd
import json

def factors(n):
    ps=[];q=2
    while q*q<=n:
        if n%q==0:
            ps.append(q)
            while n%q==0:n//=q
        q+=1
    if n>1:ps.append(n)
    return ps

def sf(n):
    out=1
    for p in factors(n):
        e=0
        while n%p==0:n//=p;e+=1
        if e%2:out*=p
    return out

def v2(n):
    e=0
    while n%2==0:e+=1;n//=2
    return e

def charbit(p,q):
    value=pow(p%q,(q-1)//2,q);assert value in (1,q-1)
    return int(value==q-1)

def rank(rows):
    basis={}
    for row in rows:
        x=sum(bit<<i for i,bit in enumerate(row))
        while x:
            i=x.bit_length()-1
            if i in basis:x^=basis[i]
            else:basis[i]=x;break
    return len(basis)

def matrix(m,n):
    assert m>n>0 and gcd(m,n)==1 and (m-n)%2
    u,v,w=m*m-n*n,2*m*n,m*m+n*n
    pc,dc=factors(u),factors(2*v*w)
    A=[[int(i==j) for j in range(len(pc))] for i,p in enumerate(pc) if p%4==3]
    A += [[charbit(p,q) for p in pc] for q in factors(v*w) if q!=2]
    B=[[charbit(p,q) for p in dc] for q in pc if q%4==1]
    C=B+([[int(p==2) for p in dc]] if v2(v)==2 else [])
    old=len(pc)-rank(A)+len(dc)-1-rank(B)
    new=len(pc)-rank(A)+len(dc)-1-rank(C)
    assert 0<=new<=old
    gtor=any(u*v*w%q!=0 for q in [7,11,13,17])
    return dict(m=m,n=n,U=u,V=v,W=w,v2V=v2(v),A_columns=pc,A=A,
                B_columns=dc,B=B,B_enhanced=C,delta_old=old,delta_new=new,
                forced_sfmn=sf(m*n),forced_sf2W=sf(2*w),G_tor=gtor,TI_CLOSED=(new==0 and gtor))

if __name__=='__main__':
    fixtures=[matrix(m,n) for m,n in [(2,1),(6,1),(11,2),(8,5),(18,7),(4,1),(9,4)]]
    open('ti005_examples.json','w').write(json.dumps(fixtures,indent=2))
    print(json.dumps([(r['m'],r['n'],r['delta_old'],r['delta_new'],r['TI_CLOSED']) for r in fixtures]))
