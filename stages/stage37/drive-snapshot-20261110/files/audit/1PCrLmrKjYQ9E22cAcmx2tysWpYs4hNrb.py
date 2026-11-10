import json, math
from fractions import Fraction as Q
from pathlib import Path

def det(A):
    A=[r[:] for r in A]; old=1; sign=1
    for k in range(len(A)-1):
        if A[k][k]==0:
            j=next(j for j in range(k+1,len(A)) if A[j][k])
            A[k],A[j]=A[j],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,len(A)):
            for j in range(k+1,len(A)):
                v=A[i][j]*pivot-A[i][k]*A[k][j]
                assert v%old==0
                A[i][j]=v//old
            A[i][k]=0
        old=pivot
    return sign*A[-1][-1]
def trim(p):
    while len(p)>1 and p[-1]==0:p.pop()
    return p
def rem(p,d):
    p=p[:]
    while len(p)>=len(d) and any(p):
        c=p[-1]/d[-1];k=len(p)-len(d)
        for j,v in enumerate(d):p[k+j]-=c*v
        trim(p)
    return p
def ev(p,x):
    v=Q(0)
    for c in reversed(p):v=v*x+c
    return v
def sg(x):return 1 if x>0 else -1 if x<0 else 0
def sturm(p):
    s=[p,[i*p[i] for i in range(1,len(p))]]
    while len(s[-1])>1:s.append([-v for v in rem(s[-2],s[-1])])
    return s
def var(s,x):
    vs=[]
    for p in s:
        v=sg(p[-1])*(-1 if x=='-' and (len(p)-1)%2 else 1) if isinstance(x,str) else sg(ev(p,x))
        if v:vs.append(v)
    return sum(a!=b for a,b in zip(vs,vs[1:]))
def below(s,x):return var(s,'-')-var(s,x)
def vp(n,p):
    assert n
    n=abs(n);v=0
    while n%p==0:n//=p;v+=1
    return v
def square_Qp(q,p):
    v=vp(q.numerator,p)-vp(q.denominator,p)
    if v%2:return False
    num=q.numerator//p**vp(q.numerator,p);den=q.denominator//p**vp(q.denominator,p)
    m=8 if p==2 else p;u=num*pow(den,-1,m)%m
    return u==1 if p==2 else pow(u,(p-1)//2,p)==1
def mul(p,q,mod):
    v=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
      for j,b in enumerate(q):v[i+j]=(v[i+j]+a*b)%mod
    return v

# Independently exhaust all monic linear and quadratic factors over F3.
f3=[2,0,2,0,1]
for degree in [1,2]:
 import itertools
 for cs in itertools.product(range(3),repeat=degree):
    d=list(cs)+[1];p=f3[:]
    while len(p)>=len(d):
        c=p[-1]%3;k=len(p)-len(d)
        for j,v in enumerate(d):p[k+j]=(p[k+j]-c*v)%3
        trim(p)
    assert any(p)
cube11=[4,8,8,1]
assert all(ev(cube11,Q(x))%11 for x in range(11))
assert ev(cube11,Q(9))%11!=0
f11=mul([2,1],cube11,11)

rows=[]; local=0
primes=[2,3,5,7,11,13,17,19,23,29,769]
for k in range(26):
    r=8+66*k;a=2*r;b=r*r-1;c=r*r+1;N=a*a+b*b;D=2*b*b-25*a*a
    assert math.gcd(a,b)==1 and N==c*c and D>0
    p=[-a*a,6*a*b,11*a*a-b*b,-8*a*b,N]
    assert [v%3 for v in p]==f3 and [v%11 for v in p]==f11
    s=sturm(list(map(Q,p)))
    assert (below(s,'+'),below(s,Q(0)),below(s,Q(a,b)))==(4,1,2)
    assert -Q(p[0],N)==Q(a,c)**2
    G=[-a*a*N**3,6*a*b*N**2,N*(11*a*a-b*b),-8*a*b]
    A=[[0]*4 for _ in range(4)]
    for j in range(3):A[j+1][j]=1
    for i in range(4):A[i][3]=-G[i]
    c0=[[-v for v in row] for row in A]
    B=[[a*N*(i==j)-b*A[i][j] for j in range(4)] for i in range(4)]
    assert det(c0)==-a*a*N**3==-(a*c**3)**2
    assert det(B)==a*a*N**3*(a*a+2*b*b)**2
    assert Q(1,det(B))==Q(1,a*c**3*(a*a+2*b*b))**2
    locals_data=[]
    for prime in primes:
        depth=3+2*vp(a,prime);z=prime**depth
        ratio=Q(ev(p,Q(z)),p[0])
        assert vp((ratio-1).numerator,prime)-vp((ratio-1).denominator,prime)>=3
        assert square_Qp(ratio,prime)
        local+=1;locals_data.append(dict(p=prime,depth=depth,nonpole_residual_local_square=True))
    rows.append(dict(r=r,a=a,b=b,c=c,D0=D,S4_certificate='irreducible mod3 and1+3 mod11',
      norm_c0=str(det(c0)),xi_signature='--++',physical=False,local_checks=locals_data))
out=dict(status='PASS',packets=len(rows),certified_S4_packets=len(rows),four_real_packets=len(rows),
  local_nonpole_square_checks=local,global_residual_points='z=0,w=a/c',
  physical_endpoints=0,global_counting_credit=0,packets_detail=rows)
Path(__file__).with_name('M3-T11-129-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='packets_detail'}))
