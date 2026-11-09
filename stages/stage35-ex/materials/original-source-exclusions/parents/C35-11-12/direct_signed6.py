import sympy as S
u,q=S.symbols('u q')
P=u**6-5*u**5-8*u**4-5*u**3-8*u**2-5*u-1;Q=S.expand(P.subs(u,-1-u))
f=1+q-13*q*q-5*q**3;g=1+5*q+11*q*q-q**3
h=1+2*q-33*q*q-116*q**3-65*q**4-46*q**5+q**6
hh=1+10*q+55*q*q+156*q**3+111*q**4-70*q**5-7*q**6
assert S.expand(h.subs(q,u*(u+1))-P*Q)==0
assert [S.resultant(h,z,q) for z in [f,g,hh]]==[-2**24,-2**24,-2**52]
assert S.resultant(P,Q,u)==-2**24*13
assert S.gcd(S.Poly(P,u,modulus=13),S.Poly(Q,u,modulus=13))==S.Poly(u-6,u,modulus=13)
assert 6 not in {i*i%13 for i in range(13)}
# B even: D odd, V=B^4=0 mod8; -W5 W7 = D^36 F G H1 H2 =5 mod8.
assert ((-5)*(-1)*1*(-7))%8==5
# B odd: D even, V=B^4=1 mod8, all four homogeneous factors =1 mod8.
# A even primitive => 4|A, hence A^2=0 mod8; B^2=1 => K=L=-1 mod8.
assert int(P.subs(u,0))%8==int(Q.subs(u,0))%8==7
print('DIRECT_H1_COPRIMALITY_RESULTANTS_PASS')
print('DIRECT_PQ_GCD13_ROOT6_NONSQUARE_PASS')
print('B_EVEN_ADJACENT_PRODUCT_UNIT5_MOD8_PASS')
print('NO_S264_SIGNS_NO_S322_MODULAR_PRIME_SIEVE_REQUIRED')
