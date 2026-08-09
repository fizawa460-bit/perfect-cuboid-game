#!/usr/bin/env python3
from math import gcd


def primitive_pairs(B):
    out=[]
    m=2
    while m*m+1<=B:
        for n in range(1,m):
            H=m*m+n*n
            if H>B: continue
            if gcd(m,n)!=1 or ((m-n)&1)==0: continue
            S=m*m-n*n; X=2*m*n
            assert S*S+X*X==H*H
            assert 2*S*X*H == 4*m*n*(m-n)*(m+n)*(m*m+n*n)
            out.append((m,n,S,X,H))
        m+=1
    return out


def main():
    # Structural audit only: exact identities and primitive Euclid contract.
    for B in (100,1000,10000):
        rows=primitive_pairs(B)
        assert len({(S,X,H) for _,_,S,X,H in rows})==len(rows)
        print(B,len(rows))
    print('STAGE14_S5A=EUCLID_PARAMETER_DESCENT_SIEVE_TARGET_FORMULATED')
    print('LOCAL_SOLUBILITY_CHARACTER_MATRIX_DERIVED=false')
    print('FAMILY_LARGE_SIEVE_THEOREM_PROVED=false')
    print('SQRT_B_ASYMPTOTIC_PROVED=false')

if __name__=='__main__': main()
