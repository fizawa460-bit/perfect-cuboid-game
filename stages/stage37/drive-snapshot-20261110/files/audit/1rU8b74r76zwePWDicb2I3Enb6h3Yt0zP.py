from math import gcd, isqrt
from collections import defaultdict
import json
from pathlib import Path

def euclid(B):
    out=set()
    for m in range(2,isqrt(B)+1):
        for n in range(1,m):
            p=m*m+n*n
            if p>B: break
            if gcd(m,n)!=1 or (m-n)%2==0: continue
            c,x=sorted((m*m-n*n,2*m*n))
            out.add((c,x,p))
    return out

def circles(B):
    out=set()
    for c in range(1,B):
        for x in range(c+1,isqrt(B*B-c*c)+1):
            if gcd(c,x)!=1: continue
            p=isqrt(c*c+x*x)
            if p*p==c*c+x*x: out.add((c,x,p))
    return out

def omega(n):
    count=0;p=2
    while p*p<=n:
        if n%p==0:
            count+=1
            while n%p==0:n//=p
        p+=1
    return count+(n>1)

def seeds(d):
    # alpha in (d, (3+2sqrt(2))*d]; reduction is exact integers.
    out=set()
    for p in range(1,3*d+1):
        z=2*p*p-d*d
        if z<=0:continue
        u=isqrt(z)
        if u*u!=z or u%2!=1 or gcd(u,d)!=1:continue
        if 3*u-4*p<=0:out.add((u,p))
    return out

def orbit_directions(B,D):
    out=set()
    for d in range(1,D+1,2):
        for u,p in seeds(d):
            while p<=B:
                if u>d:
                    c,x=(u-d)//2,(u+d)//2
                    assert c*c+x*x==p*p and gcd(c,x)==1
                    out.add((c,x,p))
                u,p=3*u+4*p,2*u+3*p
    return out

def reduce_seed(c,x,p):
    u=c+x;d=x-c;k=0
    assert u*u-2*p*p==-d*d and gcd(u,d)==1
    while 3*u-4*p>0:
        u,p=3*u-4*p,3*p-2*u;k+=1
    return d,u,p,k

def run():
    small=euclid(1500);second=circles(1500)
    assert small==second
    large=euclid(50000)
    norm_checks=0;by_d=defaultdict(set)
    for c,x,p in large:
        d,u,q,k=reduce_seed(c,x,p)
        assert (u,q) in seeds(d) if d<=300 else True
        assert u*u-2*q*q==-d*d and gcd(u,d)==1
        U,Q=u,q
        for _ in range(k):U,Q=3*U+4*Q,2*U+3*Q
        assert (U-d)//2==c and (U+d)//2==x and Q==p
        by_d[d].add((u,q));norm_checks+=1
    # All seeds, not merely those observed under the Euclid height ceiling.
    seed_checks=0
    for d in range(1,301,2):
        ss=seeds(d)
        assert len(ss)<=2**omega(d),(d,len(ss),omega(d))
        seed_checks+=len(ss)
    comparisons=[]
    for B,D in [(1500,25),(5000,50),(50000,100),(50000,300)]:
        a={z for z in euclid(B) if z[1]-z[0]<=D}
        b=orbit_directions(B,D)
        assert a==b
        comparisons.append({'B':B,'D':D,'unordered_directions':len(a),'match':True})
    content_checks=0
    for c,x,p in sorted(small):
        for g in (1,2,7,30):
            assert abs(g*c-g*x)//gcd(g*c,g*x)==x-c
            assert isqrt((g*c)**2+(g*x)**2)//gcd(g*c,g*x)==p
            content_checks+=1
    result={'status':'PASS','dual_circle_Euclid_directions_B1500':len(small),
      'Euclid_directions_B50000':len(large),'norm_and_reduction_checks':norm_checks,
      'primitive_seed_checks_d_le300':seed_checks,'orbit_comparisons':comparisons,
      'content_checks':content_checks,'physical_endpoints_enumerated':0,
      'asymptotic_proof_by_finite_data':False,'audit_mode':'WITHIN_SESSION_NOT_INDEPENDENT'}
    Path('research162/verification162.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':run()
