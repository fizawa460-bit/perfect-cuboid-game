#!/usr/bin/env python3
"""Exact rational arithmetic checks for a conditional uniform rank>=2 off-orbit theorem.
Universal assertions are proved in the research card, not by finite tests.
No packages, internet, or rank oracles.
"""
from fractions import Fraction as F
from math import isqrt,gcd,lcm
import json
from pathlib import Path


O=None


def neg(P):
    return None if P is None else (P[0],-P[1])


def add(P,Q,a):
    if P is None:return Q
    if Q is None:return P
    x1,y1=P; x2,y2=Q
    if x1==x2 and y1==-y2:return None
    if x1!=x2: s=(y2-y1)/(x2-x1)
    else:
        assert y1
        s=(3*x1*x1+2*a*x1-D*D)/(2*y1)
    x3=s*s-a-x1-x2
    y3=s*(x1-x3)-y1
    return (x3,y3)


def mul(k,P,a):
    if k<0:return mul(-k,neg(P),a)
    R=None; Q=P
    while k:
        if k&1:R=add(R,Q,a)
        Q=add(Q,Q,a);k//=2
    return R


def sqr(q):
    if q<0:return False
    return isqrt(q.numerator)**2==q.numerator and isqrt(q.denominator)**2==q.denominator


def sqrt_q(q):
    assert sqr(q)
    return F(isqrt(q.numerator),isqrt(q.denominator))


def ord_over_prime(P,p,A,B,C):
    # Project a rational point with denominator prime to p
    if P is None:return None
    if P[0].denominator%p==0 or P[1].denominator%p==0:return None
    return (P[0].numerator*pow(P[0].denominator,-1,p)%p,P[1].numerator*pow(P[1].denominator,-1,p)%p)


def addp(P,Q,a,b,p):
    if P is None:return Q
    if Q is None:return P
    x1,y1=P; x2,y2=Q
    if x1==x2 and (y1+y2)%p==0:return None
    if x1!=x2:s=(y2-y1)*pow((x2-x1)%p,-1,p)%p
    else:s=(3*x1*x1+2*a*x1+b)*pow((2*y1)%p,-1,p)%p
    x3=(s*s-a-x1-x2)%p
    y3=(s*(x1-x3)-y1)%p
    return (x3,y3)


def mulp(n,P,a,b,p):
    R=None
    while n:
        if n&1:R=addp(R,P,a,b,p)
        P=addp(P,P,a,b,p)
        n//=2
    return R


def countp(p,a,b):
    ans=1
    for x in range(p):
        z=(x*x*x+a*x*x+b*x)%p
        ans+=1 if z==0 else 2 if pow(z,(p-1)//2,p)==1 else 0
    return ans


A,B,C=8,15,17;D=A*C; coeff=B*B
P=(F(D),F(B*D)); U=(F(72),F(456)); T0=(F(0),F(0))
assert A*A+B*B==C*C and gcd(A,B)==1
assert P[1]*P[1]==P[0]*(P[0]-A*A)*(P[0]+C*C)
assert U[1]*U[1]==U[0]*(U[0]-A*A)*(U[0]+C*C)
rows=[]
for k in range(-6,7):
    V=add(U,mul(k,P,coeff),coeff)
    assert V is not None
    W=mul(2,V,coeff)
    Q=add(T0,W,coeff)
    assert Q is not None and Q[0]!=0
    x,y=Q
    assert y*y==x*(x-A*A)*(x+C*C)
    r2=-x; p2=A*A+r2; q2=C*C-r2; s2=B*B-r2
    assert sqr(r2) and sqr(p2) and sqr(q2)
    rr,pp,qq=map(sqrt_q,(r2,p2,q2))
    # negative y picks physical sign, but r,p,q are positive sqrt values.
    assert (y*y)==(rr*pp*qq)**2
    assert rr*rr+ s2 == B*B
    strict=bool(-B*B<x<0 and y<0)
    rows.append({"k":k,"strict_real":strict,"s_rational_square":sqr(s2),"x_num_digits":len(str(abs(x.numerator))),"x_den_digits":len(str(x.denominator))})


Q0=add(T0,mul(2,U,coeff),coeff)
assert Q0==(F(-938961,34225),F(-5128769712,6331625)),Q0
r2=-Q0[0]; p2=A*A+r2; q2=C*C-r2; s2=B*B-r2
assert sqrt_q(r2)==F(969,185)
assert sqrt_q(p2)==F(1769,185)
assert sqrt_q(q2)==F(2992,185)
assert s2==F(6761664,34225) and not sqr(s2)
assert Q0[1]==-sqrt_q(r2)*sqrt_q(p2)*sqrt_q(q2)
assert -B*B<Q0[0]<0 and Q0[1]<0


finite=[]
for p in (7,11):
    count=countp(p,coeff,-D*D)
    assert count in (12,16)
    assert count==(12 if p==7 else 16)
    Pp=ord_over_prime(P,p,A,B,C);Up=ord_over_prime(U,p,A,B,C)
    assert mulp(48,Pp,coeff,-D*D,p) is None
    assert mulp(48,Up,coeff,-D*D,p) is None
    assert B%p!=0
    finite.append({"p":p,"E_Fp":count,"48P_zero":True,"48U_zero":True,"near_T0_s2_unit_square":True})


out={"run_id":"R4-20261016-POSTC118-ORIGINAL-RANK2-OFFCYCLE-ANY-FINITELOCAL-V1", "head_snapshot":"C35-118", "scope":"conditional rank(original E)>=2, U independent modulo E[2]+ZP", "math_status":"PASS_EXACT_FINITE_REPLAY_PROOF_IN_CARD", "base": [A,B,C],"original_P":str(P),"independent_U":str(U), "sample_point":{"x":str(Q0[0]),"y":str(Q0[1]),"r":str(sqrt_q(r2)),"p":str(sqrt_q(p2)),"q":str(sqrt_q(q2)),"s2":str(s2),"s_square":False,"is_indexed":False,"is_indexed_reason":"S242 independence U mod E[2]+ZP; no D=T0+2nP"},"signed_samples":rows,"finite_good_reduction":finite,"finite_tests":len(rows),"global_fourth_square":"Faltings genus-2 finiteness (inherited S241) guarantees only finitely many k; finite tests not proof", "original_signed_index_membership":False,"full_physical_packet":False,"full_upstream_forward":False,"branch_b_closed":False,"e1_proved":False,"r0_accepted":False}
print(json.dumps(out,ensure_ascii=False,sort_keys=True))
