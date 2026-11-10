from math import gcd,isqrt

# Exact multivariate integer coefficient arithmetic in r,s,z.
def add(*xs):
    d={}
    for x in xs:
        for k,v in x.items():d[k]=d.get(k,0)+v
    return {k:v for k,v in d.items() if v}
def sc(x,c):return {k:v*c for k,v in x.items() if v*c}
def mul(x,y):
    d={}
    for k,v in x.items():
        for l,w in y.items():
            q=tuple(a+b for a,b in zip(k,l));d[q]=d.get(q,0)+v*w
    return {k:v for k,v in d.items() if v}
def pw(x,n):
    d={(0,0,0):1}
    for _ in range(n):d=mul(d,x)
    return d
def ev(x,r,s,z=0):return sum(v*r**k[0]*s**k[1]*z**k[2] for k,v in x.items())
r={(1,0,0):1};s={(0,1,0):1};z={(0,0,1):1}
q0=add(pw(r,2),pw(s,2));q1=add(pw(r,2),sc(mul(r,s),-4),sc(pw(s,2),5))
n=add(pw(r,2),sc(mul(r,s),-2),sc(pw(s,2),-1))
k=add(pw(r,2),sc(mul(r,s),2),sc(pw(s,2),-1))
rs=add(r,sc(s,-1));u=sc(mul(mul(s,rs),n),-2)
v=add(pw(r,4),sc(mul(pw(r,3),s),-6),sc(mul(pw(r,2),pw(s,2)),12),sc(mul(r,pw(s,3)),-14),sc(pw(s,4),11))
d3=pw(q1,3)
d2=mul(n,add(pw(r,4),sc(mul(pw(r,3),s),4),sc(mul(pw(r,2),pw(s,2)),-50),sc(mul(r,pw(s,3)),100),sc(pw(s,4),-51)))
d1=sc(mul(mul(rs,s),add(sc(pw(r,4),3),sc(mul(pw(r,3),s),-17),sc(mul(pw(r,2),pw(s,2)),35),sc(mul(r,pw(s,3)),-41),sc(pw(s,4),32))),4)
d0=sc(mul(mul(pw(rs,2),pw(s,2)),n),4)
d=add(mul(d3,pw(z,3)),mul(d2,pw(z,2)),mul(d1,z),d0)
p=add(mul(add(pw(u,2),pw(v,2)),pw(z,4)),sc(mul(mul(u,v),pw(z,3)),-8),mul(add(sc(pw(u,2),11),sc(pw(v,2),-1)),pw(z,2)),sc(mul(mul(u,v),z),6),sc(pw(u,2),-1))
assert not add(p,sc(mul(add(mul(q0,z),sc(n,-1)),d),-1))
res=add(mul(d3,pw(n,3)),mul(mul(d2,pw(n,2)),q0),mul(mul(d1,n),pw(q0,2)),mul(d0,pw(q0,3)))
assert not add(res,sc(mul(mul(pw(q1,2),n),pw(k,3)),-2))
assert not add(add(pw(u,2),pw(v,2)),sc(mul(q0,pw(q1,3)),-1))
print('PASS: homogeneous exact coefficient factorization, linear/cubic resultant, norm identity')

def signed_sf(x):
    sg=-1 if x<0 else 1;x=abs(x);d=1;p=2
    while p*p<=x:
        e=0
        while x%p==0:e+=1;x//=p
        if e%2:d*=p
        p+=1
    return sg*d*x
tested=0;examples=[]
for rr in range(-12,13):
    for ss in range(1,13):
        if gcd(rr,ss)!=1:continue
        U,V,Q0,Q1,N,K=[ev(f,rr,ss) for f in (u,v,q0,q1,n,k)]
        if U==0 or V==0:continue
        cs=[ev(f,rr,ss) for f in (d0,d1,d2,d3)]
        for a in range(-12,13):
            for b in range(1,13):
                if gcd(a,b)!=1:continue
                L=Q0*a-N*b;D=sum(cs[j]*a**j*b**(3-j) for j in range(4))
                P=(U*U+V*V)*a**4-8*U*V*a**3*b+(11*U*U-V*V)*a*a*b*b+6*U*V*a*b**3-U*U*b**4
                assert L*D==P
                if L:
                    common=gcd(abs(L),abs(D))
                    bad=abs(2*Q0*Q1*N*K)
                    while common>1:
                        g=gcd(common,bad)
                        assert g>1
                        common//=g
                if P>=0:continue
                target=-P*Q0*Q1**3
                if isqrt(target)**2!=target:continue
                delta=signed_sf(L)
                assert (2*Q0*Q1*N*K)%abs(delta)==0
                assert signed_sf(L*Q0*b)==signed_sf(delta*Q0*b)
                tested+=1
                if len(examples)<4:examples.append((rr,ss,a,b,delta))
print('PASS: evaluated factorization/common-support checks; negative-square nonzero cases',tested,'examples',examples)
print('No-hit count has no existence, emptiness or counting credit; exact coefficient identities and valuation proof are authoritative.')
