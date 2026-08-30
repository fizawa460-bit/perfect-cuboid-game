#!/usr/bin/env python3
from fractions import Fraction


def poly_add(a,b):
    n=max(len(a),len(b)); out=[Fraction(0) for _ in range(n)]
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def poly_sub(a,b): return poly_add(a,[-x for x in b])
def poly_mul(a,b):
    out=[Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def poly_deriv(a): return [Fraction(i)*a[i] for i in range(1,len(a))] or [Fraction(0)]
def poly_eval(a,x):
    s=Fraction(0)
    for c in reversed(a): s=s*x+c
    return s

def poly_divmod(a,b):
    a=a[:]
    while len(a)>1 and a[-1]==0: a.pop()
    while len(b)>1 and b[-1]==0: b.pop()
    q=[Fraction(0) for _ in range(max(1,len(a)-len(b)+1))]
    while len(a)>=len(b) and not (len(a)==1 and a[0]==0):
        k=len(a)-len(b); c=a[-1]/b[-1]; q[k]=c
        for j in range(len(b)): a[k+j]-=c*b[j]
        while len(a)>1 and a[-1]==0: a.pop()
    return q,a

def poly_gcd(a,b):
    while not (len(b)==1 and b[0]==0):
        _,r=poly_divmod(a,b); a,b=b,r
    lc=a[-1]
    return [x/lc for x in a]

# ascending coefficients in t
one=[Fraction(1)]
t=[Fraction(0),Fraction(1)]
t2=poly_mul(t,t)
a=poly_sub(t2,one)                    # t^2-1
r=poly_mul(a,a)                        # (t^2-1)^2
q=[Fraction(1),0,Fraction(-6),0,Fraction(1)]
four_t2=[Fraction(0),0,Fraction(4)]
assert poly_sub(r,q)==four_t2
assert poly_eval(q,Fraction(0))==1
assert poly_eval(q,Fraction(1))==-4
assert poly_eval(q,Fraction(-1))==-4
assert poly_gcd(q,poly_deriv(q))==[Fraction(1)]

Dplus=[Fraction(-1),Fraction(-2),Fraction(1)]
Dminus=[Fraction(-1),Fraction(2),Fraction(1)]
assert poly_mul(Dplus,Dminus)==q

# Infinity chart u=1/t after dividing section coordinates by t^4.
# r/t^4=(1-u^2)^2 and q/t^4=1-6u^2+u^4, so difference is 4u^2.
u2=[Fraction(0),0,Fraction(1)]
r_inf=poly_mul(poly_sub(one,u2),poly_sub(one,u2))
q_inf=[Fraction(1),0,Fraction(-6),0,Fraction(1)]
assert poly_sub(r_inf,q_inf)==four_t2

# Direct substitutions verify the normalized line-factor formulas.
# C0: -r V^2-q W^2 = -[(aV)^2+(zW)^2], z^2=q.
# Cr: r U^2+(r-q)W^2 = (aU)^2+(2tW)^2.
# Cq: q U^2+(q-r)V^2 = (zU)^2-(2tV)^2.
assert r==poly_mul(a,a)
assert poly_sub(r,q)==four_t2
assert poly_sub(q,r)==[-x for x in four_t2]

print('PASS_EXACT_CONTACT_COMBINATORICS_REDUCTION')
