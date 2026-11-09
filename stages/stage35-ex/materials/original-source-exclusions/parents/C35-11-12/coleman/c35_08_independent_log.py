"""Stage35EX C35-08. Independent p=3 log(E26) from quadratic algebra trace,
no c3_chab4/c3_chabauty helpers, no Q9 sqrt or sigma choice.
May rely on exact Mumford polynomials E_26.pkl, then verifies their identity.
"""
from fractions import Fraction as F
from math import comb
import pickle,os
P=3; N=int(os.environ.get("PADIC_PREC","19")); M=P**N; K=int(os.environ.get("SERIES_K","32"))
FT=[0,-1,5,-8,5,-8,5,1] # coefficient x^i of xP(-x)
def vpint(a):
    if a==0:return 10**9
    s=0
    while a%3==0:a//=3;s+=1
    return s
def vpq(a):return vpint(a.numerator)-vpint(a.denominator)
def qm(a,mod=M):
    a=F(a); n,d=a.numerator,a.denominator
    if d%3==0:
        v=vpint(d);assert n%3**v==0,(a,v)
        n//=3**v;d//=3**v
    return n*pow(d,-1,mod)%mod
def fpoly(cs,x):
    z=0
    for c in cs[::-1]:z=(z*x+qm(c))%M
    return z
def divint(a,b):
    if not b:raise ZeroDivisionError()
    v=vpint(b); assert v<1e8 and a%3**v==0,('not divisible',v)
    return (a//3**v)*pow(b//3**v,-1,M)%M

def mulpoly(a,b,n):
    z=[F(0)]*(n+1)
    for i,x in enumerate(a[:n+1]):
        for j,y in enumerate(b[:n+1-i]):z[i+j]+=x*y
    return z
def powerser(a,n):
    cur=[F(1)]+[F(0)]*n
    for k in range(n):cur=mulpoly(cur,a,n)
    return cur
def sqrtser(g,n):
    assert g[0]==1
    out=[F(1)]
    for j in range(1,n+1):
        out.append((g[j] if j<len(g) else F(0))/2-sum((out[i]*out[j-i] for i in range(1,j)),F(0))/2)
    return out
def invser(a,n):
    assert a[0]==1
    out=[F(1)]
    for j in range(1,n+1):out.append(-sum(a[i]*out[j-i] for i in range(1,min(j,len(a)-1)+1)))
    return out
class Q2:
    def __init__(self,d,a=0,b=0):self.d=d;self.a=a%M;self.b=b%M
    def __add__(self,z):return Q2(self.d,self.a+z.a,self.b+z.b)
    def __sub__(self,z):return Q2(self.d,self.a-z.a,self.b-z.b)
    def __mul__(self,z):return Q2(self.d,self.a*z.a+self.d*self.b*z.b,self.a*z.b+self.b*z.a)
    def scale(self,c):
        c=F(c);v=vpq(c)
        if v>=0:return Q2(self.d,self.a*qm(c),self.b*qm(c))
        k=-v;assert self.a%3**k==0 and self.b%3**k==0,('not integral',k,self.a%3**k,self.b%3**k)
        t=qm(c*3**k)
        return Q2(self.d,(self.a//3**k)*t,(self.b//3**k)*t)
    def inv(self):
        det=(self.a*self.a-self.d*self.b*self.b)%M
        assert det%3,('nonunit determinant',vpint(det))
        z=pow(det,-1,M)
        return Q2(self.d,z*self.a,-z*self.b)
    def __repr__(self):return f'({self.a},{self.b})'
    def __pow__(self,e):
        assert e>=0
        z=Q2(self.d,1,0);a=self
        while e:
            if e&1:z=z*a
            a=a*a;e//=2
        return z

def qeval(coeff,x):
    z=Q2(x.d)
    for c in coeff[::-1]:z=z*x+Q2(x.d,qm(c),0)
    return z

def evalseries(c,x):
    z=Q2(x.d)
    for v in c[::-1]:z=z*x+Q2(x.d,qm(v),0)
    return z

def integrate_poly_at(coeff,x):
    s=Q2(x.d);z=x
    for n,h in enumerate(coeff):
        if h:s=s+z.scale(h/F(n+1))
        z=z*x
    return s

def raw_mumford_check(u,v):
    # division over Q to check exact U | V^2 - FT
    h=[F(0)]*max(8,2*len(v)-1)
    for i,c in enumerate(FT):h[i]+=c
    for i,a in enumerate(v):
        for j,b in enumerate(v):h[i+j]-=a*b
    h=h[:]
    for i in range(len(h)-1,len(u)-2,-1):
        c=h[i]
        for j,a in enumerate(u):h[i-len(u)+1+j]-=c*a
    assert not any(h[:len(u)-1]),('bad Mumford',h[:len(u)-1])

u,v=pickle.load(open(os.path.join(os.path.dirname(__file__),'E_26.pkl'),'rb'))
raw_mumford_check(u,v)
# reciprocal cubic for w=1/u: 1/u0 + u2/u0*w + u1/u0*w^2 + w^3
Ut=[1/u[0],u[2]/u[0],u[1]/u[0],F(1)]
assert [vpq(x) for x in Ut[:3]]==[2,0,0]
ww=0
for j in range(1,N):
    k=3**j;f0=fpoly(Ut,ww)
    assert f0%k==0
    t=(-f0//k*pow(qm(Ut[1]),-1,3))%3
    ww=(ww+t*k)%M
assert fpoly(Ut,ww)==0
assert vpint(ww)==2
A=(qm(Ut[2])+ww)%M
B=(qm(Ut[1])+A*ww)%M
D=((A*A*pow(4,-1,M)-B)%M)
assert D%9==0 and vpint(D)==2
zD=(D//9)%M
assert zD%3==2
# quadratic algebra Q3[rho], rho^2=zD. Roots w2,w3 = -A/2 +/- 3 rho
w=Q2(zD,-A*pow(2,-1,M),3)
assert (w*w +w.scale(A)+Q2(zD,B,0)).a==0
assert (w*w +w.scale(A)+Q2(zD,B,0)).b==0
x=w.inv(); tau=x+Q2(zD,-1)
assert tau.a%3==0 and tau.b%3==0
scale=27
Vscaled=[F(27)*cc for cc in v]
assert all(vpq(c)>=0 for c in Vscaled)
y2s=qeval(Vscaled,x)
assert y2s.a%27==0 and y2s.b%27==0,(y2s.a%27,y2s.b%27)
y2=y2s.scale(F(1,27))
assert (y2*y2-qeval([F(z) for z in FT],x)).a%(3**8)==0
assert (y2*y2-qeval([F(z) for z in FT],x)).b%(3**8)==0
# expansion at x=1: g(t)=ft(1+t)/ft(1)=-ft(1+t)
assert sum(FT)==-1
g=[F(-sum(FT[j]*comb(j,k) for j in range(k,8))) for k in range(8)]
sg=sqrtser(g,K); gi=invser(sg,K)
# ybase = y2 / sqrt(g(tau)) ; 1/ybase = sqrt(g(tau))/y2
ib=y2.inv()*evalseries(sg,tau)
assert ((ib.inv()*ib.inv())+Q2(zD,1)).a%(3**9)==0,('base branch square failed',ib)
# paired integrals to base pair sum = 0; trace of each integral from x=1 to P_i
pair=[]
for i in range(3):
    coeff=[F(0)]*(K+1)
    for n,c in enumerate(gi):
        for j in range(i+1):
            if n+j<=K:coeff[n+j]+=comb(i,j)*c
    val=integrate_poly_at(coeff,tau)*ib.scale(F(1,2))
    pair.append(2*val.a%M)
# infinity root w1 and uniformizer s via formal power series R(w)=sqrt(ft(u)/u^7)
cR=[F(FT[7-j]) for j in range(1,8)]
SR=sqrtser([F(1)]+cR,K);IR=invser(SR,K)
R_w=sum(qm(s)*pow(ww,j,M) for j,s in enumerate(SR))%M
Vtw=sum(qm(F(27)*v[i])*pow(ww,2-i,M) for i in range(3))%M
# s = (27*R(w))/(w*(27*(v2+v1*w+v0*w^2)))
s=divint(27*R_w%M, ww*Vtw%M)
assert vpint(s)==1
inf=[]
for i in range(3):
    out=0
    for j,h in enumerate(IR):
        e=5-2*i+2*j
        if e>=K:break
        a=pow(s,e,M)
        # integral coefficient = -h/e
        t=Q2(zD,a).scale(-h/F(e)).a
        out=(out+t)%M
    inf.append(out)
le=[(a+b)%M for a,b in zip(inf,pair)]
print('STATUS independent quadratic trace C35-08')
print('w1 valuation',vpint(ww),'s valuation',vpint(s),'quadratic D v3',vpint(D),'d mod 3',zD%3)
print('E=26D2 log/3 mod 729',[(q//3)%729 for q in le])
print('logs v3', [vpint(q) for q in le])
print('rho trace pair/3 mod729',[(q//3)%729 for q in pair])
print('infinity/3 mod729',[(q//3)%729 for q in inf])
print('expected log(D2)/3 mod729', [56,164,310])
print('INDEPENDENT LOG/3',[((q//3)*pow(26,-1,729))%729 for q in le])
assert [(q//3*pow(26,-1,729))%729 for q in le]==[56,164,310]
print('PASS_INDEPENDENT_Q9_TRACE_LOGE26')


