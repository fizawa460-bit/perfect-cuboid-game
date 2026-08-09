#!/usr/bin/env python3
from math import gcd


def factors(m,n):
    return [m,n,m-n,m+n,m*m+n*n]


def odd_part_gcd(a,b):
    g=gcd(abs(a),abs(b))
    while g%2==0 and g:
        g//=2
    return g


def audit(limit=300):
    checked=0
    for m in range(2,limit+1):
        for n in range(1,m):
            if gcd(m,n)!=1 or (m-n)%2==0:
                continue
            fs=factors(m,n)
            for i in range(5):
                for j in range(i+1,5):
                    assert odd_part_gcd(fs[i],fs[j])==1,(m,n,fs,i,j)
            checked+=1
    assert checked>0
    # Full-2-descent parity condition: nonzero even-weight vectors in F2^3.
    labels=[v for v in range(1,8) if ((v&1)+((v>>1)&1)+((v>>2)&1))%2==0]
    assert labels==[3,5,6]
    print(f"PASS primitive_pairs={checked} labels=12,13,23")

if __name__=='__main__':
    audit()
