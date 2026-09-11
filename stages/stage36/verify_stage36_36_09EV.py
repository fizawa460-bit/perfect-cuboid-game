#!/usr/bin/env python3
import json,math,subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EH='stages/stage36/36-09EH/rho-fixed-p-rankzero-torsion-criterion-preflight.json'
EK='stages/stage36/36-09EK/rho-sel2-literal-orbit-closure-preflight.json'
EO='stages/stage36/36-09EO/rho-point-search-free-sel2-evaluator-preflight.json'
ET='stages/stage36/36-09ET/rho-template-realization-nearmiss-expansion-preflight.json'
EU='stages/stage36/36-09EU/rho-t6-profile-legendre-rigidity-preflight.json'
SOURCE='stages/stage36/36-09EV/rho-t6-profile-rank3-realization-source-lock.md'
CERT='stages/stage36/36-09EV/rho-t6-profile-rank3-realization-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={
 EH:'d95bf71f3cbed1d3fd12eaa0d235d2aa83539d37',
 EK:'f6af11a0f7fd8a303531b2a587b7446c382a84c5',
 EO:'bb76c05c7549ebb243a193376691138d8e01a7fb',
 ET:'6130e12a668c66fa181b1e9a6be17c9219257002',
 EU:'0507f5a19cc3baf44553e7b9bdd0e689bd5ec5d7',
 SOURCE:'ec0b0d51fbfa4fbcb6cb6cdc2d068801923cd69d',
 CERT:'c5067f43b6217d7faebc23c9921895d5f53e3dbf'}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)
eh=load(EH);ek=load(EK);eo=load(EO);et=load(ET);eu=load(EU);c=load(CERT)
assert c['entry_authority']['v276_exact_head']=='4aecaa024f2e46273d15f8dc5f9e27015bc05347'
assert c['entry_authority']['v276_promotion_ci']=='34400789925/102631882375'
assert c['entry_authority']['36_09EV_entry_allowed'] is True
assert eu['pfaffian_rank_theorem']['sel2_dimension_2_iff_B_rank_3'] is True
assert eh['fixed_p_sufficient_conditions']==[
 'dim_F2 Sel^2(E_rho,p/Q)=2',
 '8h is not a rational square and -8h is not a rational square',
 'E_rho,p(Q)[3]=0']
assert ek['literal_orbit_theorem']['positive_literal_orbit_complete'] is True
assert et['new_fixed_parameter_exclusions']['expanded_registry_count']==36

# Exact arithmetic realization.
a,b=4802,5531
assert math.gcd(a,b)==1 and 0<a<b
N=a*a-b*b;d=a*b;P=N+2*d;Q=N-2*d;D=P*P-Q*Q
assert (N,d,P,Q,D)==(-7532757,26559862,45586967,-60652481,-1600551891196272)
assert D==8*N*d
assert P==73*624479
assert Q==-17*3567793
assert D==-(2**4)*(3**6)*(7**4)*5531*10333

def pf(n):
 n=abs(n);out=[]
 if n%2==0:
  out.append(2)
  while n%2==0:n//=2
 q=3
 while q*q<=n:
  if n%q==0:
   out.append(q)
   while n%q==0:n//=q
  q+=2
 if n>1:out.append(n)
 return out
SP=[q for q in pf(P) if q!=2];SQ=[q for q in pf(Q) if q!=2]
SD=[q for q in pf(D) if q!=2 and P%q and Q%q]
assert SP==[73,624479] and SQ==[17,3567793] and SD==[3,7,5531,10333]
profile=sorted([('P',q%8) for q in SP]+[('Q',q%8) for q in SQ]+[('D',q%8) for q in SD])
assert profile==sorted([('D',3),('D',3),('D',5),('D',7),('P',1),('P',7),('Q',1),('Q',1)])
# gcd(P,Q)=1 and v2(D)=4 gives the shallow branch used by EU.
assert math.gcd(abs(P),abs(Q))==1
z=0;t=abs(D)
while t%2==0:z+=1;t//=2
assert z==4
assert c['primitive_realization']['dyadic_branch']=='shallow'
assert c['primitive_realization']['matches_EU_fixed_coarse_profile'] is True

# EU decisive 4x3 Legendre matrix.
def legbit(x,q):return 0 if pow(x%q,(q-1)//2,q)==1 else 1
Ds=[3,5531,10333,7];cols=[73,17,3567793]
B=[[legbit(x,q) for x in cols] for q in Ds]
assert B==[[0,1,0],[1,1,0],[1,1,0],[1,1,1]]
def rank(A):
 A=[row[:] for row in A];rr=0
 for j in range(len(A[0])):
  k=next((i for i in range(rr,len(A)) if A[i][j]),None)
  if k is None:continue
  A[rr],A[k]=A[k],A[rr]
  for i in range(len(A)):
   if i!=rr and A[i][j]:A[i]=[x^y for x,y in zip(A[i],A[rr])]
  rr+=1
 return rr
assert rank(B)==3
ur=c['EU_rank3_replay'];assert ur['B']==B and ur['B_rank']==3 and ur['EU_implied_sel2_dimension']==2
assert ur['uses_parameter_specific_local_point_search'] is False
assert ur['uses_full_parameter_specific_selmer_recomputation'] is False

# Independent EH no-4 test.
def is_square(n):
 if n<0:return False
 r=math.isqrt(n);return r*r==n
eightNd=8*N*d
assert eightNd==-1600551891196272
assert not is_square(eightNd) and not is_square(-eightNd)
assert c['EH_checks']['plus_minus_eight_h_both_nonsquare'] is True

# Independent EH/36-09EI division-polynomial reduction at 5.
M=a*a+b*b
psi=[-64*N*N*d*d*(M**4+4*N*N*d*d),-192*N*N*d*d*M*M,-96*N*N*d*d,4*M*M,3]
mods=[x%5 for x in psi]
vals=[]
for x in range(5):
 y=0
 for zc in reversed(psi):y=(y*x+zc)%5
 vals.append(y)
assert mods==[4,0,4,0,3]
assert vals==[4,1,3,3,1] and all(vals)
assert c['EH_checks']['rational_3torsion_zero'] is True
assert c['EH_checks']['complete_EH_criterion'] is True

# Literal positive orbit, derived directly from EK transformation.
g=math.gcd(abs(a-b),a+b)
u=abs(a-b)//g;v=(a+b)//g
orbit={Fraction(a,b),Fraction(b,a),Fraction(u,v),Fraction(v,u)}
expected_orbit={Fraction(4802,5531),Fraction(5531,4802),Fraction(729,10333),Fraction(10333,729)}
assert orbit==expected_orbit and len(orbit)==4
stored={Fraction(x) for x in c['literal_orbit_consequence']['orbit']}
assert stored==orbit

# Exact disjointness from the previous 36-value authority: EO's 24 registry
# plus ET's 12 new values.
old={Fraction(x) for x in eo['criterion_consumption']['expanded_fixed_parameter_registry']}
assert len(old)==24
for orb in et['new_fixed_parameter_exclusions']['orbits']:
 old.update(Fraction(x) for x in orb)
assert len(old)==36 and orbit.isdisjoint(old)
impact=c['literal_orbit_consequence']
assert impact['disjoint_from_previous_registry'] is True
assert impact['previous_registry_count']==36 and impact['expanded_registry_count']==40
assert impact['all_four_fixed_parameter_receiver_sectors_empty'] is True

assert c['route_result']['next_leaf']=='36-09EW_RHO_T6_PROFILE_PARAMETRIC_REALIZATION_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
print('36-09EV verified: p=4802/5531 realizes the exact EU T6 coarse profile with rank(B)=3, passes independent EH no4/no3 checks, and its four-point literal orbit is disjoint from the previous 36-value registry. Provisional registry impact 36->40; no parent receiver/endpoint credit.')
