"""TI-004: parameter-uniform Legendre character rank bound, not rank values."""
from math import gcd
import json

def primes(n):
    out=[];q=2
    while q*q<=n:
        if n%q==0:
            out.append(q)
            while n%q==0:n//=q
        q+=1
    if n>1:out.append(n)
    return out

def bit(a,q):
    assert q%2 and a%q
    s=pow(a%q,(q-1)//2,q)
    assert s in (1,q-1)
    return int(s!=1)

def rank2(rows,width):
    vals=[sum(v<<i for i,v in enumerate(row)) for row in rows]
    basis={}
    for val in vals:
        while val:
            i=val.bit_length()-1
            if i in basis:val^=basis[i]
            else:basis[i]=val;break
    return len(basis)

def matrices(m,n):
    assert m>n>0 and gcd(m,n)==1 and (m-n)%2
    u,v,w=m*m-n*n,2*m*n,m*m+n*n
    pu,pvw=primes(u),primes(2*v*w)
    erows=[];etags=[]
    for i,q in enumerate(pu):
        if q%4==3:
            erows.append([int(i==j) for j in range(len(pu))]);etags.append(['inert_U',q])
    for q in pvw:
        if q==2:continue
        erows.append([bit(p,q) for p in pu]);etags.append(['VW_character',q])
    prows=[];ptags=[]
    for q in pu:
        if q%4==1:
            prows.append([bit(p,q) for p in pvw]);ptags.append(['split_U_character',q])
    re,rp=rank2(erows,len(pu)),rank2(prows,len(pvw))
    defect_e,defect_p=len(pu)-re,len(pvw)-1-rp
    assert defect_e>=0 and defect_p>=0
    return dict(m=m,n=n,U=u,V=v,W=w,E_columns=pu,E_rows=erows,E_tags=etags,
                Eprime_columns=pvw,Eprime_rows=prows,Eprime_tags=ptags,
                E_rank=re,Eprime_rank=rp,defect_E=defect_e,defect_Eprime=defect_p,
                rank_upper_bound=defect_e+defect_p,
                TI_closed_by_matrix=(defect_e+defect_p==0 and any(u*v*w%q for q in (7,11,13,17))))

if __name__=='__main__':
    examples=[matrices(4,1),matrices(9,4)]
    for row in examples:print(json.dumps(row))
    with open('ti004_examples.json','w') as f:json.dump(examples,f,indent=2)
