from math import gcd
from pathlib import Path

base=Path('stages/stage15')
df=(base/'15-6df/result.md').read_text()
dg=(base/'15-6dg/result.md').read_text()
dh=(base/'15-6dh/result.md').read_text()

assert 'K_G_SQUARED_DIVIDES_DELTA=true' in df
assert 'MOVING_COMMON_SUPPORT_EXACTLY_G=true' in df
assert 'DOUBLE_ELIMINANTS_CRAMER_EQUIVALENT=true' in dg
assert 'SECOND_DETERMINISTIC_RECONSTRUCTION=false' in dg
assert 'DISPERSION_PROMOTED=true' in dh
assert 'CONDITIONAL_BETA=-1' in dh
assert 'MERGE_ALLOWED=false' in dh

# Exact g>1 survivor diagnostic.
m,n,r,s=13,9,28,3
assert gcd(m,n)==gcd(r,s)==1
a,b,c,d=gcd(m,r),gcd(m,s),gcd(n,r),gcd(n,s)
M=m//(a*b); N=n//(c*d); U=r//(a*c); V=s//(b*d)
assert (a,b,c,d,M,N,U,V)==(1,1,1,3,13,3,28,1)

# Primitive reduced norms: k=1, P=365, Q=85, g=5.
k,P,Q=1,365,85
g=gcd(P,Q)
assert g==5
A0=a**4*M*M*U*U+d**4*N*N*V*V
B0=b**4*M*M*V*V+c**4*N*N*U*U
assert A0==k*P*P and B0==k*Q*Q

Delta=(a*b*M)**4-(c*d*N)**4
Rm=b*b*M*P-d*d*N*Q
Rp=b*b*M*P+d*d*N*Q
Sm=a*a*M*Q-c*c*N*P
Sp=a*a*M*Q+c*c*N*P
assert gcd(Rm,Rp)==2*g
assert gcd(Sm,Sp)==2*g
assert Delta%(k*g*g)==0
assert Delta*U*U==k*Rm*Rp
assert Delta*V*V==k*Sm*Sp

p=P//g; q=Q//g; D=Delta//(k*g*g)
r_m=b*b*M*p-d*d*N*q
r_p=b*b*M*p+d*d*N*q
s_m=a*a*M*q-c*c*N*p
s_p=a*a*M*q+c*c*N*p
assert gcd(r_m,r_p) in (1,2)
assert gcd(s_m,s_p) in (1,2)
assert D*U*U==r_m*r_p
assert D*V*V==s_m*s_p

print('Stage15-6 main-batch df-dh: PASS')