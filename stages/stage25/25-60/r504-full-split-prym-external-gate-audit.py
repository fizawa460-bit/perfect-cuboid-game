#!/usr/bin/env python3
from itertools import product


def inv(a,p):
    return pow(a,p-2,p)


def nonsquare(p):
    for d in range(2,p):
        if pow(d,(p-1)//2,p)==p-1:
            return d
    raise RuntimeError('no nonsquare')


def add2(x,y,p):
    return ((x[0]+y[0])%p,(x[1]+y[1])%p)


def mul2(x,y,p,d):
    a,b=x; c,e=y
    return ((a*c+b*e*d)%p,(a*e+b*c)%p)


def pow2(x,n,p,d):
    out=(1,0); base=x
    while n:
        if n&1:
            out=mul2(out,base,p,d)
        n//=2
        if n:
            base=mul2(base,base,p,d)
    return out


def pgl2_reps(p):
    seen=set(); reps=[]
    for A,B,C,D in product(range(p), repeat=4):
        if (A*D-B*C)%p==0:
            continue
        tup=(A,B,C,D)
        for v in tup:
            if v%p:
                s=inv(v,p)
                norm=tuple((z*s)%p for z in tup)
                break
        if norm not in seen:
            seen.add(norm)
            reps.append(norm)
    assert len(reps)==p*(p*p-1)
    return reps


def count_curve(A,B,C,D,p,ext,genus3):
    if ext==1:
        elems=list(range(p))
        squares={y*y%p for y in elems}
        def qval(x):
            return (pow((A*x+B)%p,4,p)+pow((C*x+D)%p,4,p))%p
        vals=[qval((u*u)%p) for u in elems] if genus3 else [qval(x) for x in elems]
        lead=(pow(A,4,p)+pow(C,4,p))%p
        assert lead != 0
        aff=sum(1 if v==0 else (2 if v in squares else 0) for v in vals)
        return aff+(2 if lead in squares else 0)

    d=nonsquare(p)
    elems=[(a,b) for a in range(p) for b in range(p)]
    squares={mul2(y,y,p,d) for y in elems}
    def sc(c): return (c%p,0)
    def qval(x):
        axb=add2(mul2(sc(A),x,p,d),sc(B),p)
        cxd=add2(mul2(sc(C),x,p,d),sc(D),p)
        return add2(pow2(axb,4,p,d),pow2(cxd,4,p,d),p)
    vals=[qval(mul2(u,u,p,d)) for u in elems] if genus3 else [qval(x) for x in elems]
    lead=add2(pow2(sc(A),4,p,d),pow2(sc(C),4,p,d),p)
    assert lead != (0,0)
    aff=sum(1 if v==(0,0) else (2 if v in squares else 0) for v in vals)
    return aff+2


def e0_trace(p):
    squares={y*y%p for y in range(p)}
    n=1
    for x in range(p):
        v=(x*x*x-4*x)%p
        n += 1 if v==0 else (2 if v in squares else 0)
    return p+1-n


def prym_lpoly(A,B,C,D,p):
    c1=count_curve(A,B,C,D,p,1,True)
    e1=count_curve(A,B,C,D,p,1,False)
    c2=count_curve(A,B,C,D,p,2,True)
    e2=count_curve(A,B,C,D,p,2,False)
    s1c=p+1-c1
    s2c=p*p+1-c2
    ae=p+1-e1
    s2e=ae*ae-2*p
    s1=s1c-ae
    s2=s2c-s2e
    b2=(s1*s1-s2)//2
    return (1,-s1,b2,-p*s1,p*p)


def has_e0_factor(lp,p):
    a=e0_trace(p)
    b=-lp[1]-a
    return lp==(1,-(a+b),2*p+a*b,-p*(a+b),p*p)


def reciprocal_locus(r,p):
    A,B,C,D=r
    return ((A*B-C*D)%p==0 or
            (A*B+C*D)%p==0 or
            (A*D+B*C)%p==0)


for p,expected_hits in [(7,36),(11,80)]:
    reps=pgl2_reps(p)
    hits=[]
    for r in reps:
        A,B,C,D=r
        # For p=7,11 and invertible M these leading/constant terms do not vanish.
        assert (pow(A,4,p)+pow(C,4,p))%p != 0
        assert (pow(B,4,p)+pow(D,4,p))%p != 0
        lp=prym_lpoly(A,B,C,D,p)
        if has_e0_factor(lp,p):
            hits.append(r)
    assert len(hits)==expected_hits
    assert all(reciprocal_locus(r,p) for r in hits)
    assert e0_trace(p)==0

print('R504_PRYM_EXCEPTIONAL_PGL2_F7_CLASSES=336')
print('R504_PRYM_EXCEPTIONAL_PGL2_F7_E0_FACTOR_HITS=36')
print('R504_PRYM_EXCEPTIONAL_PGL2_F11_CLASSES=1320')
print('R504_PRYM_EXCEPTIONAL_PGL2_F11_E0_FACTOR_HITS=80')
print('R504_PRYM_EXCEPTIONAL_ALL_TESTED_E0_HITS_LIE_IN_RECIPROCAL_LOCUS=PASS')
print('R504_PRYM_EXCEPTIONAL_FINITE_FIELD_SIEVE_IS_EVIDENCE_ONLY=true')
print('R504_PRYM_EXCEPTIONAL_UNBOUNDED_ISOGENY_DEGREE_CLOSED=false')
