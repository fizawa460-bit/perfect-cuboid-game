#!/usr/bin/env python3
import sympy as sp

p=5
x,T=sp.symbols('x T')
Q=sp.expand((x+1)**4+(x+2)**4)
Cpoly=sp.expand(Q.subs(x,x**2))
assert Q == 2*x**4+12*x**3+30*x**2+36*x+17
assert Cpoly == 2*x**8+12*x**6+30*x**4+36*x**2+17
assert sp.gcd(sp.Poly(Q,x,modulus=5),sp.Poly(Q,x,modulus=5).diff()).degree()==0
assert sp.gcd(sp.Poly(Cpoly,x,modulus=5),sp.Poly(Cpoly,x,modulus=5).diff()).degree()==0

# F_5 quadratic character.
def leg(a):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

# F_25 = F_5[w]/(w^2-2); 2 is nonsquare mod 5.
class F25:
    __slots__=('a','b')
    def __init__(self,a,b=0): self.a=a%5; self.b=b%5
    def __add__(self,o):
        if isinstance(o,int): return F25(self.a+o,self.b)
        return F25(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return F25(-self.a,-self.b)
    def __sub__(self,o): return self+(-o if not isinstance(o,int) else -o)
    def __mul__(self,o):
        if isinstance(o,int): return F25(self.a*o,self.b*o)
        return F25(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __pow__(self,n):
        r=F25(1); z=self
        while n:
            if n&1: r=r*z
            z=z*z; n//=2
        return r
    def __eq__(self,o):
        if isinstance(o,int): return self.b==0 and self.a==o%5
        return self.a==o.a and self.b==o.b

def chi25(z):
    if z==0: return 0
    return 1 if z**12==1 else -1

def eval_int_poly(poly,z):
    P=sp.Poly(poly,x)
    out=0 if isinstance(z,int) else F25(0)
    for c in P.all_coeffs(): out=out*z+int(c)
    return out

def count_curve(poly,r):
    lc=int(sp.Poly(poly,x).LC())%5
    if r==1:
        s=sum(leg(eval_int_poly(poly,a)) for a in range(5))
        inf=2 if leg(lc)==1 else 0
        return 5+s+inf
    s=0
    for a in range(5):
        for b in range(5):
            s+=chi25(eval_int_poly(poly,F25(a,b)))
    # Every nonzero F_5 element is a square in F_25.
    inf=2 if lc else 0
    return 25+s+inf

NC1=count_curve(Cpoly,1)
NE1=count_curve(Q,1)
NC2=count_curve(Cpoly,2)
NE2=count_curve(Q,2)
assert (NC1,NE1,NC2,NE2)==(4,4,36,32)

S1C=6-NC1; S1E=6-NE1
S2C=26-NC2; S2E=26-NE2
S1P=S1C-S1E
S2P=S2C-S2E
assert (S1P,S2P)==(0,-4)
e2=(S1P*S1P-S2P)//2
LP=sp.expand(1-S1P*T+e2*T**2-5*S1P*T**3+25*T**4)
assert LP==1+2*T**2+25*T**4

# E0: y^2=x^3-4x over F_5 has trace 2.
N0=6+sum(leg(a**3-4*a) for a in range(5))
a0=6-N0
assert a0==2
LE0=1-a0*T+5*T**2
quo,rem=sp.div(LP,LE0,domain=sp.QQ)
assert sp.expand(rem)!=0
assert sp.expand(rem)==sp.Rational(4,5)-sp.Rational(8,5)*T

# The chosen tuple is outside the reciprocal loci.
A=B=C=1; D=2
assert A*D-B*C!=0
assert (A*B-C*D)*(A*B+C*D)*(A*D+B*C)!=0

print('R504_FULL_SPLIT_SPECIALIZATION=(1,1,1,2)')
print('R504_FULL_SPLIT_SPECIALIZATION_GOOD_REDUCTION_P5=PASS')
print('R504_PRYM_F5_LPOLY=1+2*T^2+25*T^4')
print('R504_E0_F5_LPOLY=1-2*T+5*T^2')
print('R504_PRYM_E0_FROBENIUS_FACTOR_P5=false')
print('R504_FULL_SPLIT_GENERIC_PRYM_E0_FACTOR=false')
print('R504_FULL_SPLIT_EXCEPTIONAL_PRYM_E0_ISOGENY_LOCUS=OPEN')
print('GLOBAL_STAGE25_LOWER_CHANGED=false')
