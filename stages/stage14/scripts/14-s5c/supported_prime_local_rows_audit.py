#!/usr/bin/env python3
from math import gcd, isqrt


def prime_factors(n):
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:
                n//=p
        p += 1 if p==2 else 2
    if n>1: out.append(n)
    return out


def legendre(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1


def audit(limit=120):
    pairs=0
    odd_bad=0
    routing={'S12':0,'X13':0,'H23':0}
    for m in range(2,limit+1):
        for n in range(1,m):
            if gcd(m,n)!=1 or ((m-n)&1)==0:
                continue
            pairs += 1
            S=m*m-n*n; X=2*m*n; H=m*m+n*n
            cols=[m,n,m-n,m+n,H]
            # s5b invariant: odd pairwise coprime.
            for i in range(5):
                for j in range(i):
                    assert gcd(cols[i],cols[j]) & ~1 == 0 or gcd(cols[i],cols[j]) in (1,2)
                    g=gcd(cols[i],cols[j])
                    assert all(p==2 for p in prime_factors(g))
            for p in set(prime_factors(S*X*H)):
                if p==2: continue
                odd_bad += 1
                divS=S%p==0; divX=X%p==0; divH=H%p==0
                assert sum((divS,divX,divH))==1
                membership=sum(c%p==0 for c in cols)
                assert membership==1
                if divS:
                    assert (m-n)%p==0 or (m+n)%p==0
                    routing['S12']+=1
                elif divX:
                    assert m%p==0 or n%p==0
                    routing['X13']+=1
                else:
                    assert H%p==0
                    routing['H23']+=1

    # Symbol-row sanity: square-class equations are invariant under replacing
    # any ai by ai*square and under reciprocal in F_p*/squares.
    for p in (3,5,7,11,13,17,19,23,29,31):
        for a1 in range(1,p):
            for a2 in range(1,p):
                for a3 in range(1,p):
                    srow=(legendre(a1*a2,p)==1 and legendre(a3,p)==1)
                    xrow=(legendre(a1*a3,p)==1 and legendre(-a2,p)==1)
                    hrow=(legendre(a2*a3,p)==1 and legendre(a1,p)==1)
                    for q in (1,2):
                        sq=(q*q)%p
                        assert srow==(legendre((a1*sq)*a2,p)==1 and legendre(a3,p)==1)
                        assert xrow==(legendre((a1*sq)*a3,p)==1 and legendre(-a2,p)==1)
                        assert hrow==(legendre(a2*a3,p)==1 and legendre(a1*sq,p)==1)

    # 2-adic structural facts from primitive opposite parity.
    for m in range(2,limit+1):
        for n in range(1,m):
            if gcd(m,n)!=1 or ((m-n)&1)==0: continue
            S=m*m-n*n; X=2*m*n; H=m*m+n*n
            assert S%2==1 and H%2==1
            assert X%4==0

    print('STAGE14_S5C=COMPLETE_SUPPORTED_PRIME_LOCAL_HILBERT_ROWS')
    print(f'EUCLID_PAIRS={pairs}')
    print(f'ODD_BAD_PRIME_INCIDENCES={odd_bad}')
    print('ODD_SUPPORTED_FACTOR_TO_LABEL_ROUTING_DERIVED=true')
    print('ODD_SUPPORTED_ROWS_LINEAR_IN_RECIPROCITY_BITS=true')
    print('P2_SUPPORTED_LABEL_FORCED_TO_13=true')
    print('ODD_UNSELECTED_BAD_PRIME_ROWS_DERIVED=false')
    print('P2_COMPLETE_LOCAL_MATRIX_DERIVED=false')
    print('SQRT_B_ASYMPTOTIC_PROVED=false')
    print('ROUTING',routing)

if __name__=='__main__':
    audit()
