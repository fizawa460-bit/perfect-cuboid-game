#!/usr/bin/env python3
"""Independent exact/modular certificate for Stage35EX-C p=3 log-difference.
Reads prior R3 rational Cantor 44D evidence, not prior verification code.
Uses only Python stdlib. Does not claim rank(J(Q))=1 independently.
"""
from fractions import Fraction
from pathlib import Path
import json, hashlib


ROOT=Path(__file__).resolve().parent
source=ROOT/'p3prev/r3_c116_hcs_p3_zero_disk_evidence.json'
data=json.loads(source.read_text())
def coeffs(n):
 return [Fraction(int(e['numerator']),int(e['denominator'])) for e in data['D_44_mumford'][n]]
u=coeffs('u'); v=coeffs('v')
P=[0,1,6,3,-60,-169,-42,5]


def trim(a):
 a=list(a)
 while a and a[-1]==0: a.pop()
 return a


def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b): c[i+j]+=x*y
 return c


def sub(a,b):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]-=x
 return trim(c)


def rem(a,b):
 x=trim(a)
 while len(x)>=len(b):
  t=x[-1]/b[-1]; shift=len(x)-len(b)
  for j in range(len(b)):x[shift+j]-=t*b[j]
  x=trim(x)
 return x


assert len(u)==4 and u[-1]==1 and len(v)==3
assert rem(sub(mul(v,v),P),u)==[]


def vp(x,p=3):
 if not x:return 100000
 x=Fraction(x);num=abs(x.numerator);den=x.denominator;k=0
 while num%p==0:num//=p;k+=1
 while den%p==0:den//=p;k-=1
 return k


def zmod(x,n):
 x=Fraction(x);m=3**n
 assert x.denominator%3!=0, ('non-integral',x)
 return (x.numerator*pow(x.denominator,-1,m))%m


# normalized integral coefficients: 9 u_j, 27 v_j
A,B,C=9*u[2],9*u[1],9*u[0]
V0,V1,V2=[27*x for x in v]
assert all(vp(t)>=0 for t in (A,B,C,V0,V1,V2))
assert [zmod(t,1) for t in (A,B,C,V0,V1,V2)] == [1,1,1,1,1,1]


def pole_s_root(n):
 mod=3**n; am,bm,cm=[zmod(t,n) for t in (A,B,C)]
 def polynomial(s):return s**3+am*s*s+9*bm*s+81*cm
 s=(-am)%3
 assert polynomial(s)%3==0
 for j in range(1,n):
  base=3**j
  roots=[s+k*base for k in range(3) if polynomial(s+k*base)%(base*3)==0]
  assert len(roots)==1, ('hensel failure',j,roots)
  s=roots[0]
 assert polynomial(s)%mod==0
 return s


N=15
s=pole_s_root(N)
# Local factor x_infty=s/9; u=(x-s/9)*(x^2+U1 x+U0)
# U1=(A+s)/9, U0= -C/s.
M=3**N
Am,Bm,Cm=[zmod(t,N) for t in (A,B,C)]
assert (Am+s)%9==0
U1=((Am+s)%M)//9
U0=(-Cm*pow(s,-1,M))%M
assert (U1%3,U0%3)==(1,1)
# q_finite=1+3w; quadratic for w from finite quadratic
assert (2+U1)%3==0
assert (1+U1+U0)%9==0
alpha=((2+U1)//3)%3
beta=((1+U1+U0)//9)%3
assert (alpha,beta)==(2,2)
assert all((k*k+alpha*k+beta)%3!=0 for k in (0,1,2))


# infinity local parameter t=y/x^4. y=v(x), x=s/9;
# t/3=(V2*s^2+9V1*s+81V0)/s^4 (exact local identity).
tdiv3=(zmod(V2,N)*s*s+9*zmod(V1,N)*s+81*zmod(V0,N))*pow(s,-4,M)%M
assert tdiv3%3==1
# Independent model identity at infinity: t^2 = P(q)/q^8 = 5/q + O(q^-2), q=s/9.
# Therefore (t/3)^2 = 5/s mod 3; this verifies nonzero t without the Mumford v sign.
assert (tdiv3*tdiv3)%3 == (5*pow(s,-1,3))%3 == 1
# for omega_i=q^i dq/(2y), omega2-omega1 = -1/5 + O(t^2) at infinity.
# finite points q=1+3w, omega2-omega1 has a zero at q=1,
# so both tiny integrals are divisible by 3^2.
# hence (L2-L1)/3 mod3 is the infinity tiny integral -t/(15) mod3.
log_diff_over3=(-tdiv3*pow(5,-1,3))%3
assert log_diff_over3==1
assert s%3==2
# independent precision levels and derivative (unit) checks
precisions=[]
for j in (5,8,11,14):
 sj=pole_s_root(j)
 mj=3**j
 derivative=(3*sj*sj+2*zmod(A,j)*sj+9*zmod(B,j))%3
 assert derivative==1
 tj=(zmod(V2,j)*sj*sj+9*zmod(V1,j)*sj+81*zmod(V0,j))*pow(sj,-4,mj)%mj
 assert tj%3==1
 precisions.append({'power':j,'pole_s_mod3':sj%3,'pole_s_mod27':sj%27,'t_over3_mod3':tj%3,'hensel_derivative_mod3':derivative})


out={
 'schema':'stage35ex-c-postC116-hcs-p3-log-difference-v1',
 'research_base':'C35-116',
 'prior_44D_rational_evidence_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'cantor_mumford_u_divides_v2_minus_P':'PASS',
 'u_coefficient_v3':[vp(x) for x in u],
 'v_coefficient_v3':[vp(x) for x in v],
 'normalized_9u2_9u1_9u0_mod3':[zmod(t,1) for t in (A,B,C)],
 'pole_s_mod81':s%81,
 'pole_q_valuation':-2,
 'finite_factor_q_polynomial_mod3':[1,1,1],
 'finite_factor_w_polynomial_mod3':[beta,alpha,1],
 'finite_factor_w_irreducible_F3':True,
 'finite_q_congruent_1_mod3':True,
 'finite_points_residue_field':'F9; q=1,y=+/-16 sqrt(-1)',
 'infinity_t_valuation':1,
 'infinity_t_over3_mod3':tdiv3%3,
 'infinity_model_t_over3_squared_mod3':(5*pow(s,-1,3))%3,
 'tiny_integral_finite_omega2_minus_omega1_divisible_by9':True,
 'log_omega2_minus_omega1_over3_mod3':log_diff_over3,
 'log_difference_v3_exactly':1,
 'full_three_component_log_computed':False,
 'primitive_log_direction_v1_v2_nonzero_mod3':True,
 'rank1_independent_audit':False,
 'conditional_X_Q_four_boundary_points':True,
 'unconditional_X_Q_four_boundary_points':False,
 'branch_b_closed':False,
 'precision_controls':precisions
}
print(json.dumps(out,sort_keys=True,indent=2,ensure_ascii=False))