#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

FIBERS = {
    "20/21": (20,21,[107,131],[128,152]),
    "80/39": (80,39,[109,137],[112,120]),
    "24/7":  (24,7, [107,109],[120,104]),
    "84/13": (84,13,[107,109],[120,112]),
    "48/55": (48,55,[107,113],[120,128]),
    "20/99": (20,99,[107,109],[104,112]),
    "60/11": (60,11,[107,151],[96,136]),
}

def qcurve(q):
    A=(q**4+14*q*q+1)/3
    B=Fraction(2,27)*(q*q+1)*(q**4-34*q*q+1)
    return -A, -B  # y^2=x^3+a4*x+a6

def add(P,Q,a4,a6):
    if P is None: return Q
    if Q is None: return P
    x1,y1=P; x2,y2=Q
    if x1==x2 and y1==-y2: return None
    if P==Q:
        if y1==0: return None
        m=(3*x1*x1+a4)/(2*y1)
    else:
        m=(y2-y1)/(x2-x1)
    x3=m*m-x1-x2
    y3=-y1+m*(x1-x3)
    return (x3,y3)

def mul(P,n,a4,a6):
    if n<0:
        return mul((P[0],-P[1]),-n,a4,a6)
    R=None; Q=P
    while n:
        if n&1: R=add(R,Q,a4,a6)
        Q=add(Q,Q,a4,a6); n//=2
    return R

def on_curve(P,a4,a6):
    if P is None: return True
    x,y=P
    return y*y==x*x*x+a4*x+a6

def inv(a,p): return pow(a%p,-1,p)

def count_mod_p(a,b,p):
    assert p not in (2,3) and b%p
    q=a%p*inv(b,p)%p
    A=(q**4+14*q*q+1)*inv(3,p)%p
    B=2*inv(27,p)*(q*q+1)*(q**4-34*q*q+1)%p
    disc=(q*q*(q-1)**4*(q+1)**4)%p
    assert disc != 0
    n=1
    for x in range(p):
        rhs=(x**3-A*x-B)%p
        if rhs==0: n+=1
        elif pow(rhs,(p-1)//2,p)==1: n+=2
    return n

for name,(a,b,ps,expected_counts) in FIBERS.items():
    q=Fraction(a,b); a4,a6=qcurve(q)
    e1=Fraction(2,3)*(q*q+1)
    e2=Fraction(-1,3)*(q*q-6*q+1)
    e3=Fraction(-1,3)*(q*q+6*q+1)
    # Exact cubic roots / full rational 2-torsion.
    for e in (e1,e2,e3): assert on_curve((e,Fraction(0)),a4,a6)
    assert e1+e2+e3==0
    # A rational half of (e1,0), and an independent rational 2-torsion point.
    R4=(Fraction(5,3)-q*q/3, 2*(q*q-1))
    S2=(e2,Fraction(0))
    assert on_curve(R4,a4,a6) and on_curve(S2,a4,a6)
    assert mul(R4,2,a4,a6)==(e1,Fraction(0))
    assert mul(R4,4,a4,a6) is None and mul(R4,2,a4,a6) is not None
    assert mul(S2,2,a4,a6) is None and S2 is not None
    subgroup={add(mul(R4,r,a4,a6),mul(S2,s,a4,a6),a4,a6) for r in range(4) for s in range(2)}
    assert len(subgroup)==8
    got=[count_mod_p(a,b,p) for p in ps]
    assert got==expected_counts,(name,got,expected_counts)
    assert gcd(*got)==8
    print(f"PASS {name}: J(Q)_tors = Z/4 x Z/2; reduction counts {list(zip(ps,got))}")

print("PASS exact Stage34 D2 common-Jacobian torsion certification")
