#!/usr/bin/env python3
import json,math,runpy,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
FC='stages/stage36/36-09FC/rho-fixed-quartic-splitting-force-preflight.json'
FCV='stages/stage36/verify_stage36_36_09FC.py'
FB='stages/stage36/36-09FB/rho-one-bit-splitting-realization-preflight.json'
SOURCE='stages/stage36/36-09FD/rho-fixed-quartic-frobenius-seed-crt-source-lock.md'
CERT='stages/stage36/36-09FD/rho-fixed-quartic-frobenius-seed-crt-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={
 FC:'cceb1c3246ff6ebd4f6b4f239c56a95580a58214',
 FCV:'43c12a5499e647ff633c280607555ef70527a21e',
 FB:'a48aa0032a4cf7789702458df2c537f2d1cf2e16',
 SOURCE:'18e2be3e2950289cb4768bb396eac595b70020c7',
 CERT:'0a397081cc689a85120328764d7a633da2542eff',
}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)

# Consume exact FC authority first.
runpy.run_path(str(ROOT/FCV))
fc=load(FC);fb=load(FB);c=load(CERT)
assert c['entry_authority']['v292_exact_head']=='da9d2de92e34e4e2879370f58968d3c8e95bfa5c'
assert c['entry_authority']['v292_exact_head_ci']=='34419317648/102691087835'
assert c['entry_authority']['36_09FD_entry_allowed'] is True
assert fc['splitting_type_theorem']['B_minus_factorization_degrees']==[2,2]
assert fc['splitting_type_theorem']['fixed_type_2_2_implies_support_rank_22'] is True

# FB carries rank/Sel2 credit globally in the one-bit theorem, not per arithmetic row.
fbth=fb['one_bit_theorem']
assert fbth['sufficient_condition']=='B=-1'
assert fbth['B_minus_implies_rank_2n_minus_2'] is True
assert fbth['B_minus_implies_sel2_dimension_2'] is True
assert fbth['global_over_all_realizations_of_factor_shape'] is True

U0=17627;M=34440;K=729
assert c['family']=={'U0':U0,'M':M,'K':K,'u':'U0+M*j','P':'8*u^2-K^2','M_factorization':'2^3*3*5*7*41'}

def isprime(n):
 if n<2:return False
 if n%2==0:return n==2
 q=3
 while q*q<=n:
  if n%q==0:return False
  q+=2
 return True

def chi(a,p):
 a%=p
 if a==0:return 0
 z=pow(a,(p-1)//2,p)
 assert z in (1,p-1)
 return 1 if z==1 else -1

def roots2(p):return [r for r in range(p) if r*r%p==2]
def proots(p):return [u for u in range(p) if (8*u*u-K*K)%p==0]
def jroots(p):
 invM=pow(M,-1,p)
 return sorted(((u-U0)*invM)%p for u in proots(p))

def good_seed(p):
 if not isprime(p) or p%8!=1 or math.gcd(p,M)!=1:return False
 rs=roots2(p)
 assert len(rs)==2
 return chi(1+rs[0],p)==-1 and chi(1-rs[0],p)==-1

th=c['general_crt_theorem']
assert th['P_zero_roots_formula']=='u=+-K/(2r) mod p0 where r^2=2'
assert th['P_zero_root_count']==2 and th['forced_subprogression_count_per_seed']==2
assert th['each_u_root_gives_unique_j_mod_p0'] is True
assert th['p0_divides_P_on_each_subprogression'] is True
assert th['FB_factor_shape_implies_p0_is_one_of_p1_p2'] is True
assert th['fixed_type_2_2_then_FC_applies'] is True
assert th['all_FB_factor_shape_realizations_on_forced_progressions_excluded'] is True
assert th['factor_shape_realizations_claimed_infinite'] is False

for p in c['illustrative_good_seeds']:
 assert good_seed(p),p
 rs=roots2(p);us=sorted(proots(p));assert len(us)==2
 predicted=set()
 for r in rs:
  predicted.add((K*pow(2*r,-1,p))%p)
  predicted.add((-K*pow(2*r,-1,p))%p)
 assert predicted==set(us),(p,predicted,us)
 js=jroots(p);assert len(js)==2 and js[0]!=js[1]
 for j in js:
  u=U0+M*j
  assert (8*u*u-K*K)%p==0
  for t in (0,1,2,7,19):
   uu=U0+M*(j+p*t)
   assert (8*uu*uu-K*K)%p==0

s=c['seed_17'];assert s['p0']==17 and good_seed(17)
r17=roots2(17)
u17=sorted(proots(17))
cu17=sorted(int(x) for x in s['u_roots_mod_p0'])
j17=jroots(17)
cj17=sorted(int(x) for x in s['j_roots_mod_p0'])
assert r17==[6,11],('sqrt2 roots',r17)
assert u17==[3,14],('computed P roots',u17)
assert cu17==[3,14],('certificate P roots',cu17)
assert u17==cu17,('P root replay mismatch',u17,cu17)
assert j17==[6,9],('computed j roots',j17)
assert cj17==[6,9],('certificate j roots',cj17)
assert j17==cj17,('j root replay mismatch',j17,cj17)
assert s['factorization_degrees']==[2,2]
res={pow(x,2,17) for x in range(1,17)}
assert sorted(res)==s['quadratic_residues_nonzero']
assert 7 not in res and 12 not in res
for y in range(17):
 assert (pow(y,4,17)-2*y*y-1)%17 == ((y*y-7)*(y*y-12))%17

ups=s['u_progressions'];assert ups==[{'residue':224267,'modulus':585480,'j_residue':6},{'residue':327587,'modulus':585480,'j_residue':9}]
for row in ups:
 assert row['modulus']==M*17
 assert row['residue']%M==U0%M
 assert row['residue']%17 in (3,14)
 assert (8*row['residue']**2-K*K)%17==0
 for t in (0,1,2,17,101):
  u=row['residue']+row['modulus']*t
  assert u%M==U0%M and (8*u*u-K*K)%17==0

fbrows={row['u']:row for row in fb['arithmetic_realizations']}
for w in s['retained_FB_witnesses']:
 assert w['u']==U0+M*w['j'] and w['j']%17==w['j_mod_17']==6
 row=fbrows[w['u']]
 sf=sorted(int(p) for p in row['factorization']['s'])
 assert w['fixed_P1_factor']==17 and 17 in sf
 assert row['B']==-1
 # Rank 22 / Sel2 dimension 2 follow from the global FB theorem replayed above.
 # Seed 17's fixed-quartic type (2,2) is independently replayed above as well.

ri=c['registry_impact']
assert ri['previous_count']==ri['provisional_count']==224
assert ri['new_orbits']==ri['new_parameters']==0
assert ri['frobenius_seed_crt_forcing_criterion_count_provisional']==1
assert ri['forced_crt_subprogression_count_for_seed_17']==2
assert c['route_result']['next_leaf']=='36-09FE_RHO_FORCED_CRT_FACTOR_SHAPE_REALIZATION_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
print('36-09FD verified: every good fixed-quartic seed prime yields two CRT subprogressions forcing that prime into P; p0=17 gives j=6,9 mod17 / u=224267,327587 mod585480. Any FB-factor-shape realization there has the required FC Frobenius type. Registry remains 224; no factor-shape infinitude/receiver/endpoint credit.')
