"""Independent mod-3461 local Kummer evaluator, no Hensel factor lifting.
Only supports -1, fundamental units, pi2, GA, GB and rational-point images;
uses that GA generates the degree-1 ramified prime and GB=p/GA^2.
"""
from fractions import Fraction as F
import sympy as sp
import c3_selmer as S
p=3461
x=sp.Symbol('x')
P=sum(c*x**i for i,c in enumerate(S.P))
r=1119
Q=sp.Poly(P,x,modulus=p)
assert Q.eval(r)%p==0 and sp.Poly(sp.diff(P,x),x,modulus=p).eval(r)%p==0
q=sp.Poly((x-r)**2,x,modulus=p)
h=Q.exquo(q)
assert h.degree()==4 and sp.factor_list(h.as_expr(),modulus=p)[1]==[(h.as_expr(),1)]
hlow=[int(h.nth(i))%p for i in range(5)]

def rem(a,b):
    a=[v%p for v in a];b=[v%p for v in b]
    while a and a[-1]==0:a.pop()
    while len(a)>=len(b):
        mul=a[-1]*pow(b[-1],-1,p)%p
        deg=len(a)-len(b)
        for i,c in enumerate(b):a[deg+i]=(a[deg+i]-mul*c)%p
        while a and a[-1]==0:a.pop()
    return a

def times(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]=(c[i+j]+v*w)%p
    return rem(c,hlow)

def exp(a,k):
    v=[1]
    while k:
        if k&1:v=times(v,a)
        a=times(a,a);k>>=1
    return v

def chiFp(z):
    z%=p
    assert z
    q=pow(z,(p-1)//2,p)
    assert q in (1,p-1)
    return int(q!=1)

def chiF4(coeff):
    result=exp(coeff,(p**4-1)//2)
    assert result in ([1],[p-1]),(coeff,result)
    return int(result!=[1])

def pc(x):
    return [int((c.numerator * pow(c.denominator,-1,p))%p) for c in S.to_pow(x)]

def peval(a,z):
    t=0
    for c in a[::-1]:t=(t*z+c)%p
    return t

def der_eval(a,z):
    t=0
    for i in range(len(a)-1,0,-1): t=(t*z+i*a[i])%p
    return t

# P(r)/p p-adic (r is integral); quotient is integral mod p
val=int(P.subs(x,r))
assert val%p==0 and val%(p*p)!=0
h_r=peval(hlow,r)
rho= - (val//p)*pow(h_r,-1,p)%p
assert rho
print('FIELD_CERT p=',p,'r=',r,'h(r)=',h_r,'rho=',rho,'chi(rho)=',chiFp(rho))

GA=[F(v) for v in (10,-2,-11,-8,-10,2)]
GB=S.mul([F(p)]+[F(0)]*5,S.pw(GA,-2))
S.PI2=[F(v) for v in (-2,-1,1,2,1,0)]
GEN=[S.MINUS1,S.U1,S.U2,S.U3,S.PI2,GA,GB]

def class_unit(alpha,nn=None):
    aa=pc(alpha)
    z=peval(aa,r)
    assert z!=0,('ram nonunit',aa)
    hh=rem(aa,hlow)
    assert hh,('quartic nonunit',aa)
    N=S.norm(alpha) if nn is None else nn
    assert N.denominator%p
    N0=int(N.numerator*pow(N.denominator,-1,p)%p)
    assert N0
    return [0,chiFp(N0),0,chiFp(z),0,chiF4(hh)]

def class_GA():
    aa=pc(GA)
    assert peval(aa,r)==0
    der=der_eval(aa,r)
    assert der
    quart=rem(aa,hlow)
    return [1,0,1,chiFp(der),0,chiF4(quart)]

def class_GB():
    # GB = p/GA^2. On ramified quadratic, pi^2/p = rho;
    # GA/pi -> GA'(r), so GB residual is rho^-1 / GA'(r)^2.
    # On unramified quartic, GB/p -> GA^-2, a square.
    return [0,0,0,chiFp(rho),1,0]

from itertools import product
xs=[class_unit(z) for z in GEN[:5]]+[class_GA(),class_GB()]
print('GENERATOR_CLASSES_INDEPENDENT',xs)
if __name__=='__main__':
    DD=S.setup_3461()
    for nm,a,c in zip(['-1','u1','u2','u3','pi2','ga','gb'],GEN,xs):
        old=S.class_3461(S.norm(a),a,DD)
        print(nm,'new',c,'old',old,'match',c==old)
        assert c==old
    for v in (0,-99,-98):
        n,al=S.point_image(F(v))
        new=class_unit(al,n)
        old=S.class_3461(n,al,DD)
        print('point',v,'new',new,'old',old,'match',new==old)
        assert new==old
    print('INDEPENDENT_P3461_GENERATOR_AND_POINT_KUMMER_PASS')
