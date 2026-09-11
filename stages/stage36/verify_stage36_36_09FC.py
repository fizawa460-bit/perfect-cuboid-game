#!/usr/bin/env python3
import json,runpy,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
FB='stages/stage36/36-09FB/rho-one-bit-splitting-realization-preflight.json'
FBS='stages/stage36/36-09FB/rho-one-bit-splitting-realization-source-lock.md'
FBV='stages/stage36/verify_stage36_36_09FB.py'
SOURCE='stages/stage36/36-09FC/rho-fixed-quartic-splitting-force-source-lock.md'
CERT='stages/stage36/36-09FC/rho-fixed-quartic-splitting-force-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={
 FB:'a48aa0032a4cf7789702458df2c537f2d1cf2e16',
 FBS:'2625033de8c08696e54120a48211afa3c4272c12',
 FBV:'149373f95a5e654d8985d358a40028ec45704bbd',
 SOURCE:'6a2ab63a4dac743e0e2126219ef929629cb225d1',
 CERT:'cceb1c3246ff6ebd4f6b4f239c56a95580a58214',
}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)

# Re-run the exact FB authority before consuming its one-bit theorem.
runpy.run_path(str(ROOT/FBV))
fb=load(FB);c=load(CERT)
assert fb['one_bit_theorem']['sufficient_condition']=='B=-1'
assert fb['one_bit_theorem']['B_minus_implies_rank_2n_minus_2'] is True
assert fb['one_bit_theorem']['B_minus_implies_sel2_dimension_2'] is True
assert c['entry_authority']['v290_receipt_head']=='8eeb0d00448320beb0c1d39708919e76bbb01319'
assert c['entry_authority']['v290_receipt_ci']=='34416716286/102683105148'
assert c['entry_authority']['36_09FC_entry_allowed'] is True
assert c['fixed_polynomial']['coefficients_ascending']==[-1,0,-2,0,1]
assert c['fixed_polynomial']['independent_of_u'] is True
assert c['fixed_polynomial']['independent_of_e'] is True

# Euler/Legendre character for the prime moduli already certified by FB.
def chi(a,p):
 a%=p
 if a==0:return 0
 z=pow(a,(p-1)//2,p)
 assert z in (1,p-1)
 return 1 if z==1 else -1

def quartic_value(y,p):return (pow(y,4,p)-2*pow(y,2,p)-1)%p

# Formal coefficient identity in F_p[r]/(r^2-2):
# (Y^2-(1+r))(Y^2-(1-r)) = Y^4-2Y^2+(1-r^2) = Y^4-2Y^2-1.
# The only possible derivative-zero roots would have y=0 or y^2=1,
# where F is respectively -1 or -2, so F is separable for odd p.
red=c['exact_reduction'];sp=c['splitting_type_theorem']
assert red['r_square']=='r^2=2 mod p'
assert red['character_pair_product']=='(1+r)(1-r)=-1'
assert red['character_pair_equal'] is True
assert red['B_plus_iff_F_has_root'] is True
assert red['B_minus_iff_F_has_no_root'] is True
assert red['root_choice_independent'] is True
assert sp['B_plus_factorization_degrees']==[1,1,1,1]
assert sp['B_minus_factorization_degrees']==[2,2]
assert sp['fixed_type_2_2_implies_support_rank_22'] is True
assert sp['fixed_type_2_2_implies_sel2_dimension_2'] is True

fbrows={row['u']:row for row in fb['arithmetic_realizations']}
for row in c['exact_replay']:
 d=row['u'];K=729;e=4*d+K;P=8*d*d-K*K
 assert d in fbrows
 fr=fbrows[d]
 sf=sorted(int(p) for p in fr['factorization']['s'])
 ps=sorted(row['p_factors'])
 assert ps==sf and P==7*ps[0]*ps[1]
 signs=[]
 for p in ps:
  assert p%8==1 and p%2==1
  invK=pow(K,-1,p)
  r=(4*d*invK)%p
  assert r*r%p==2%p
  assert e*invK%p==(1+r)%p
  # e=1 mod 4 and p=1 mod 4: reciprocity has no sign.
  B=chi(p,e)
  assert B==chi(e,p)==chi(1+r,p)
  cm=chi(1-r,p)
  assert chi(-1,p)==1
  assert ((1+r)*(1-r))%p==(-1)%p
  assert cm==B
  assert B==row['B']==-1
  # Both quadratic factors Y^2-(1+-r) are irreducible, hence type (2,2).
  assert chi(1+r,p)==chi(1-r,p)==-1
  assert row['expected_factorization_degrees']==[2,2]
  # Spot the polynomial identity at several field elements without root-search dependence.
  for y in (0,1,2,3,5,8,13):
   lhs=((y*y-(1+r))*(y*y-(1-r)))%p
   assert lhs==quartic_value(y,p)
  signs.append(B)
 assert signs==[-1,-1]

ri=c['registry_impact']
assert ri['previous_count']==ri['provisional_count']==224
assert ri['new_orbits']==ri['new_parameters']==0
assert ri['fixed_quartic_splitting_criterion_count_provisional']==1
assert c['route_result']['next_leaf']=='36-09FD_RHO_FIXED_QUARTIC_FROBENIUS_REALIZATION_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
print('36-09FC verified: on the exact FB factor shape, B=-1 is exactly the fixed quartic F(Y)=Y^4-2Y^2-1 factorization type (2,2) modulo either P1 factor. Registry remains 224; no infinitude/necessity/parent receiver/endpoint credit.')
