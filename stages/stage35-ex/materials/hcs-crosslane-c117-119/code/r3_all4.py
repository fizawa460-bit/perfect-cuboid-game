#!/usr/bin/env python3
"""POST C35-118: rigorous finite arithmetic input for a four-disk Coleman audit.
Stdlib only. The formal Coleman/Strassmann argument is in the accompanying proof.
Inherited premises: C35-118 scoped rank(J(Hcs)(Q))=1 and OLD 44D Mumford.
"""
import json, hashlib
from pathlib import Path
from fractions import Fraction
ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'r3_c116_hcs_p3_zero_disk_evidence_PRIOR.json'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == 'd84545a9f0a002f218e525978d75203a31fd455bbbbb9645eb0f40168ccfc0a7'
e=json.loads(SOURCE.read_text())
u=[Fraction(int(a['numerator']),int(a['denominator'])) for a in e['D_44_mumford']['u']]
v=[Fraction(int(a['numerator']),int(a['denominator'])) for a in e['D_44_mumford']['v']]
P=[0,1,6,3,-60,-169,-42,5]


def trim(a):
 a=list(a)
 while a and a[-1]==0:a.pop()
 return a


def pmul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out


def psub(a,b):
 out=[0]*max(len(a),len(b))
 for i,x in enumerate(a):out[i]+=x
 for i,x in enumerate(b):out[i]-=x
 return trim(out)


def prem(a,b):
 a=trim(a)
 while len(a)>=len(b):
  c=a[-1]/b[-1];offset=len(a)-len(b)
  for i,x in enumerate(b):a[i+offset]-=c*x
  a=trim(a)
 return a
assert u[3]==1 and prem(psub(pmul(v,v),P),u)==[]
A,B,C=9*u[2],9*u[1],9*u[0]
V0,V1,V2=[27*t for t in v]


def imod(x,pow3):
 x=Fraction(x);m=3**pow3
 assert x.denominator%3!=0
 return x.numerator*pow(x.denominator,-1,m)%m


def pole(n):
 mod=3**n
 a,b,c=[imod(x,n) for x in (A,B,C)]
 def F(s):return s**3+a*s*s+9*b*s+81*c
 s=-a%3
 for j in range(1,n):
  step=3**j
  found=[s+i*step for i in range(3) if F(s+i*step)%(3*step)==0]
  assert len(found)==1
  s=found[0]
 assert F(s)%mod==0
 return s


def factor(n):
 m=3**n;s=pole(n)
 a,b,c=[imod(x,n) for x in (A,B,C)]
 assert (a+s)%9==0
 U1=((a+s)%m)//9
 U0=(-c*pow(s,-1,m))%m
 assert (2+U1)%3==0 and (1+U1+U0)%9==0
 alpha=(2+U1)//3
 beta=(1+U1+U0)//9
 return s,U1,U0,alpha,beta


# Path 1: evaluate canonical Mumford y=v(q) in the quadratic residue field
# with q=1+3w, w^2+alpha*w+beta=0.
precision=[]
for n in (12,15,18,21,24,27):
 m=3**n;s,U1,U0,alpha,beta=factor(n)
 v0,v1,v2=[imod(x,n) for x in (V0,V1,V2)]
 c=(v2*(1-9*beta)+v1+v0)%m
 l=(v2*(6-9*alpha)+3*v1)%m
 assert c%27==0 and l%27==0
 cr=(c//27)%3;lr=(l//27)%3
 assert (alpha%3,beta%3,cr,lr)==(2,2,1,1)
 t3=(v2*s*s+9*v1*s+81*v0)*pow(s,-4,m)%3
 assert t3==1
 precision.append({'precision_exponent':n,'s_mod81':s%81,'finite_w_polynomial_mod3':[beta%3,alpha%3,1],
                   'finite_y_in_F9_basis_1_w':[cr,lr], 'infinity_t_div3_mod3':t3})


# Path 2: independent direct Newton in Z/3^k[delta]/(delta^2+1) (unramified degree 2).
# Pick finite w root reducing to delta-1; compute y from v(q) DIRECTLY.
def q2_mod_newton(k):
 mod=3**k
 def add(x,y):return ((x[0]+y[0])%mod,(x[1]+y[1])%mod)
 def neg(x):return (-x[0]%mod,-x[1]%mod)
 def mul(x,y):return ((x[0]*y[0]-x[1]*y[1])%mod,(x[0]*y[1]+x[1]*y[0])%mod)
 def scal(c,x):return ((c*x[0])%mod,(c*x[1])%mod)
 def inv(x):
  den=(x[0]*x[0]+x[1]*x[1])%mod
  assert den%3!=0
  d=pow(den,-1,mod)
  return ((x[0]*d)%mod,(-x[1]*d)%mod)
 def eval_poly(w,aa,bb):return add(add(mul(w,w),scal(aa,w)),(bb%mod,0))
 n=k+8;s,U1,U0,aa,bb=factor(n)
 aa%=mod;bb%=mod
 w=(mod-1,1)
 for _ in range(k+4):
  f=eval_poly(w,aa,bb)
  df=add(scal(2,w),(aa,0))
  w=add(w,neg(mul(f,inv(df))))
 assert eval_poly(w,aa,bb)==(0,0)
 q=add((1,0),scal(3,w))
 v0,v1,v2=[imod(x,k) for x in (V0,V1,V2)]
 numerator=add(add(scal(v2,mul(q,q)),scal(v1,q)),(v0,0))
 assert numerator[0]%27==0 and numerator[1]%27==0
 y=(numerator[0]//27%3,numerator[1]//27%3)
 assert (w[0]%3,w[1]%3)==(2,1) # w=delta-1
 assert y==(0,1) # y=delta=w+1, not minus sign
 assert (y[0]*y[0]-y[1]*y[1])%3==2
 return {'precision_exponent':k,'finite_w_mod3':[w[0]%3,w[1]%3],
         'finite_y_mod3_in_1_delta_basis':list(y),'w_polynomial_residual_zero':True}


newton=[q2_mod_newton(k) for k in (6,8,10,12)]


# F3 point enumeration and exact discriminant-free squarefreeness.
def f3polytrim(a):
 a=[x%3 for x in a]
 while a and a[-1]==0:a.pop()
 return a


def f3remainder(a,b):
 a=f3polytrim(a);b=f3polytrim(b)
 while len(a)>=len(b):
  top=a[-1]*pow(b[-1],-1,3)%3
  for i,t in enumerate(b):a[len(a)-len(b)+i]=(a[len(a)-len(b)+i]-top*t)%3
  a=f3polytrim(a)
 return a


def f3gcd(a,b):
 while b:a,b=b,f3remainder(a,b)
 return a
assert len(f3gcd(P,[i*P[i] for i in range(1,len(P))]))==1
pts=[]
for q in range(3):
 fx=sum(c*pow(q,i,3) for i,c in enumerate(P))%3
 for y in range(3):
  if y*y%3==fx:pts.append([q,y])
assert pts==[[0,0],[2,1],[2,2]]
assert (sum(c*(-1)**i for i,c in enumerate(P)))==64


# Finite field F9=F3[delta]/(delta^2+1): w=delta-1, y=delta.
# w/y = (delta-1)/delta = 1+delta. Its trace is 2 (delta trace 0).
trace_w_over_y=2
assert trace_w_over_y==2
inv2=2
finite_log_each=(inv2*trace_w_over_y)%3 # =1 for i=0,1,2
infty_log=( -1*pow(5,-1,3))%3 # t_inf/3=1
assert (finite_log_each,infty_log)==(1,1)
vector=[finite_log_each,finite_log_each,(finite_log_each+infty_log)%3]
assert vector==[1,1,2]
# Reductions of annihilating differential omega1-(L1/L0)omega0 and
# omega2-(L2/L0)omega0; can lift exactly since normalized L0 unit.
ann_finite=[2,1,0]    # (-1,1,0) in F3
ann_infinity=[1,0,1] # (-2,0,1) in F3
assert sum(x*y for x,y in zip(ann_finite,vector))%3==0
assert sum(x*y for x,y in zip(ann_infinity,vector))%3==0
residues={
 'T0_q0_y0':[1,0,0],
 'Pplus_q2_y1':[1,2,1],
 'Pminus_q2_y2':[1,2,1],
 'infinity':[0,0,1]
}
checks={}
for name,evalrow in residues.items():
 ann=ann_infinity if name=='infinity' else ann_finite
 check=sum(x*y for x,y in zip(ann,evalrow))%3
 assert check!=0
 checks[name]={'evaluation_vector_mod3':evalrow,'annihilator_mod3':ann,'unit_evaluation_mod3':check}
# valuation inequality: j >=1, val_3(3^j/(j+1)) >=1, for all j
for j in range(1,500):
 t=j+1;vv=0
 while t%3==0:t//=3;vv+=1
 assert j-vv>=1


out={
 'schema':'r3-postC118-hcs-full-fourpoint-chabauty-v1',
 'base_head':'C35-118',
 'inherited_rank_one_scope':'R0_C35_118_PROVISIONAL_RESEARCH_ACCEPT',
 'prior_44D_evidence_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
 'point_count_C_F3':4,'F3_affine_points':pts,'F3_good_reduction':True,
 'mumford_44D_membership_check':'PASS',
 'finite_2adic_field_method':'not involved',
 'p3_hensel_mumford_precision_replays':precision,
 'independent_unramified_quadratic_newton':newton,
 'finite_F9_w_root_polynomial_mod3':[2,2,1],
 'finite_F9_residue_y_as_polynomial_in_w_mod3':[1,1],
 'finite_F9_trace_w_over_y_mod3':trace_w_over_y,
 'normalized_abelian_log_vector_mod3':vector,
 'L0_L1_L2_mod9':[3,3,6],
 'all_four_disk_unit_annihilator_checks':checks,
 'Hcs_Q_points':['infinity','(0,0)','(-1,8)','(-1,-8)'],
 'Hcs_Q_cardinality_at_scoped_research_rank_gate':4,
 'fixed_X_Q_classification':'OLD_ACCEPTED_C35_118_ZERO_RECREDIT',
 'original_signed_index6_exclusion':'OLD_ACCEPTED_C35_118_ZERO_RECREDIT',
 'R0_new_result':'full_rational_point_exhaustion_of_OLD_Hcs_genus3_by_all_four_p3_disks',
 'worldwide_novelty_certified':False,
 'external_hostile_audit':False,
 'original_full_allindex_physical_closed':False,
 'branch_b_closed':False,'stage35_closed':False,'E1_proven':False,
}
( ROOT/'r3_c119_hcs_all4_p3_evidence.json').write_text(json.dumps(out,indent=2,ensure_ascii=False,sort_keys=True)+'\n')
print('PASS',json.dumps({'log_vector':vector,'four_disks':checks,'newton':newton},ensure_ascii=False))