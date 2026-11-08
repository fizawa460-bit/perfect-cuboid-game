#!/usr/bin/env python3
"""Stage35EX-A: all-odd-index GOOD Ward / 2-isogeny same-Gaussian gate.
Independent stdlib finite-field elliptic law and quadratic-character controls.
Does not construct physical packets or test S243/S270. Prints exact JSON.
"""
import json
from math import gcd, isqrt


def leg(x,p):
    z=pow(x%p,(p-1)//2,p)
    return 0 if z==0 else (1 if z==1 else -1)


def prime(p):
    return p>1 and all(p%d for d in range(2,isqrt(p)+1))


def add(P,Q,p,a,b):
    if P is None:return Q
    if Q is None:return P
    x,y=P; X,Y=Q
    if x==X and (y+Y)%p==0:return None
    if x==X:
        if y==0:return None
        slope=(3*x*x+2*a*x+b)*pow(2*y,-1,p)%p
    else:slope=(Y-y)*pow(X-x,-1,p)%p
    z=(slope*slope-a-x-X)%p
    return z,(slope*(x-z)-y)%p


def mul(P,n,p,a,b):
    if n<0:return mul((P[0],(-P[1])%p),-n,p,a,b)
    Q=None
    while n:
        if n&1:Q=add(Q,P,p,a,b)
        P=add(P,P,p,a,b);n//=2
    return Q


def ord2P(P,p,a,b):
    T=add(P,P,p,a,b)
    if T is None:return 1
    Q=T
    cap=p+1+2*isqrt(p)+3
    for r in range(1,cap):
        if Q is None:return r
        Q=add(Q,T,p,a,b)
    raise AssertionError(('order not found',p,cap))


def check():
    out={'u_max':38,'p_max':199,'oriented_bases':0,'good_base_prime_pairs':0,
         'odd_order_2P_cases':0,'odd_order_good_W_rows':0,
         'bad_isogeny_character_rows':0,'good_isogeny_character_rows':0,
         'bad_character_nontrivial_other2torsion':0,
         'signed_index_group_checks':0,'physical_original_character_clashes':0,
         'control_good_character_cases':0,'moving_family_checks':0,'errors':0,
         'example':{},'samples_bad':[]}
    primes=[p for p in range(7,200) if prime(p)]
    for u in range(2,39):
      for v in range(1,u):
       if gcd(u,v)!=1 or (u-v)%2==0:continue
       A,B,C=2*u*v,u*u-v*v,u*u+v*v
       assert A*A+B*B==C*C and gcd(A,B)==1 and C%2
       out['oriented_bases']+=1
       D=A*C;H=A*A+C*C;Q=C*(A+C)
       for p in primes:
        if (2*A*B*C*H)%p==0:continue
        out['good_base_prime_pairs']+=1
        a=B*B%p;b=-D*D%p;P=(D%p,B*D%p)
        assert (P[1]**2-P[0]*(P[0]-A*A)*(P[0]+C*C))%p==0
        r=ord2P(P,p,a,b)
        if r%2==0:continue
        out['odd_order_2P_cases']+=1
        T_A=(A*A%p,0);T_C=((-C*C)%p,0);T_0=(0,0)
        X=mul(P,r,p,a,b)
        assert X in (None,T_0,T_A,T_C)
        # Legendre(C(A+C)) is the third 2-isogeny alpha-character.
        k=leg(Q,p);h=leg(H,p)
        assert k in (-1,1) and h in (-1,1)
        # Isogeny character at O/T0 is +1, at TA/TC is (H/p).
        expect=(1 if X in (None,T_0) else h)
        assert k==expect,(u,v,p,r,k,h,X)
        out['odd_order_good_W_rows']+=1
        if k==1:out['good_isogeny_character_rows']+=1
        else:
         out['bad_isogeny_character_rows']+=1
         assert h==-1 and X in (T_A,T_C)
         out['bad_character_nontrivial_other2torsion']+=1
         for n in (r,3*r,5*r,-r,-3*r,-5*r):
          Y=mul(P,n,p,a,b)
          assert Y==X
          x=Y[0]
          # C35-87 original canonical odd b character.
          d=(x*x+D*D)*pow(2*D*D,-1,p)%p
          assert d!=0 and leg(d,p)==leg(2*H,p)==-leg(2,p)
          out['physical_original_character_clashes']+=1
          out['signed_index_group_checks']+=1
         if len(out['samples_bad'])<10:
          out['samples_bad'].append({'A':A,'B':B,'C':C,'p':p,'ord2P':r,'kappa_mod_p':Q%p,'H_mod_p':H%p})
        if k==1:out['control_good_character_cases']+=1
    # Structural fixture: B-odd, rank 11 (prime not 3,5,7), dyadic surviving n=1111.
    A,B,C=40,9,41;p=47;D=A*C;H=A*A+C*C;Q=C*(A+C)
    a=B*B%p;b=-D*D%p;P=(D%p,B*D%p)
    assert ord2P(P,p,a,b)==11 and leg(Q,p)==-1 and leg(H,p)==-1
    assert mul(P,11,p,a,b)==(A*A%p,0)
    n=1111
    assert n%11==0 and n%3!=0 and n%5!=0 and n%7!=0
    z=n*n-1;k=0
    while z%2==0:z//=2;k+=1
    assert k==4 and z%8==1
    assert mul(P,n,p,a,b)==(A*A%p,0)
    out['example']={'A':A,'B':B,'C':C,'p':p,'order_2P':11,'n':n,
       'chi_C_AplusC':-1,'chi_H':-1,'S238_odd_Bodd_2adic_v':k,'S238_odd_Bodd_2adic_unit8':z%8,
       'scope':'NOT a complete physical packet, not a proof all old screens pass'}
    # Uniform Euclid residue family u=5+94j,v=4, fixed p=47.
    for j in range(100):
      u=5+94*j;v=4;A=2*u*v;B=u*u-v*v;C=u*u+v*v
      assert gcd(u,v)==1 and B>0 and B%2==1
      D=A*C;H=A*A+C*C;Q=C*(A+C)
      a=B*B%p;b=-D*D%p;P=(D%p,B*D%p)
      assert (2*A*B*C*H)%p!=0 and leg(Q,p)==-1 and leg(H,p)==-1
      assert ord2P(P,p,a,b)==11
      out['moving_family_checks']+=1
    return out


if __name__=='__main__':
    print(json.dumps(check(),indent=2,sort_keys=True))
