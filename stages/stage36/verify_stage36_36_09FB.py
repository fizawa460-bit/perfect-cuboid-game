#!/usr/bin/env python3
import json,math,runpy,subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
FA='stages/stage36/36-09FA/rho-residual-core-partial-legendre-chart-preflight.json'
FAV='stages/stage36/verify_stage36_36_09FA.py'
SOURCE='stages/stage36/36-09FB/rho-one-bit-splitting-realization-source-lock.md'
CERT='stages/stage36/36-09FB/rho-one-bit-splitting-realization-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={
 FA:'499ac146f0d453a7a7abee565e4dcfb4aec982ed',
 FAV:'93fd904a44879dad721fce7122fb79486cb2ab5c',
 SOURCE:'2625033de8c08696e54120a48211afa3c4272c12',
 CERT:'a48aa0032a4cf7789702458df2c537f2d1cf2e16',
}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)
fa=load(FA);c=load(CERT)
assert c['entry_authority']['v288_exact_head']=='7c3cfca4eb2f84d71621099c16dd58c7e7212802'
assert c['entry_authority']['v288_exact_head_ci']=='34415780996/102680229625'
assert c['entry_authority']['36_09FB_entry_allowed'] is True
assert c['entry_authority']['fixed_parameter_exclusion_registry_count']==208

# Reuse the exact-green FA symbolic/numeric machinery after immutable hash locks.
ns=runpy.run_path(str(ROOT/FAV))
rank=ns['rank'];legbit=ns['legbit'];matrix_from_pattern=ns['matrix_from_pattern']
previous=set(ns['previous'])|set(ns['new']);assert len(previous)==208
prime_support=ns['prime_support'];assignment=ns['assignment'];eval_matrix=ns['eval_matrix']
peel=ns['peel'];leaf_equation_rref=ns['leaf_equation_rref'];expected_chart=ns['expected_chart']
CHART_A=ns['CHART_A'];chart_ok=ns['chart_ok'];numeric_object=ns['numeric_object']
psi3_coeffs=ns['psi3_coeffs'];has_root_mod=ns['has_root_mod'];PAIRS=ns['PAIRS']

# FB Chart C is an unrestricted partial-Legendre leaf certificate, like FA A/B.
CHART_C=[(0,4,1),(0,5,0),(1,5,1),(3,4,0),(3,5,0),(3,7,1)]
rowC=next(x for x in c['arithmetic_realizations'] if x['u']==1642495667)
pC,_=prime_support(rowC['u'],rowC['factorization'])
aC=assignment(pC);trC,HC,_,_=peel(eval_matrix(aC))
assert len(trC)==22 and HC==[[0,0],[0,0]]
assert leaf_equation_rref(trC)==expected_chart(CHART_C)
cc=c['chart_C'];assert cc['condition_count']==6 and cc['all_unlisted_reciprocity_bits_are_dont_care'] is True
assert cc['leaf_pivots']==22 and cc['residual_size']==2 and cc['residual_rank']==0 and cc['support_rank']==22 and cc['sel2_dimension']==2

# Exact arithmetic identities behind the reduction from six chart bits to one.
K=729
assert K==27**2
# Progression u=17627 mod34440 fixes all residues used in the reciprocity proof.
u0=17627
assert (u0%3,u0%8,u0%7,u0%41,u0%5)==(2,3,1,38,2)
f0=2*u0+K;e0=4*u0+K
assert (f0%8,f0%7,f0%41)==(7,3,26)
assert (e0%8,e0%7)==(5,5)
# Euler-criterion helper for the small constant residue locks.
def lsg(a,p):
 z=pow(a%p,(p-1)//2,p)
 assert z in (1,p-1)
 return 1 if z==1 else -1
assert lsg(38,41)==-1
assert lsg(26,41)==-1
assert lsg(5,7)==-1 and lsg(3,7)==-1
# Polynomial divisibility identities used in the source proof.
# P=8d^2-K^2; e=4d+K; f=2d+K.
for d in (1,2,17,101):
 P=8*d*d-K*K;e=4*d+K;f=2*d+K
 assert 2*d*e-K*f==P
 assert 2*P+K*K==e*(4*d-K)
 assert P-K*K==2*(2*d-K)*f
# Mod-3 labeling: P/7 =2 mod3 on the progression.
P0=8*u0*u0-K*K
assert P0%7==0 and (P0//7)%3==2

# Propositional exhaustion of the remaining A sign when B=-1.
# bit 0 means Legendre +1; bit 1 means -1.
# Forced: p1/d=p2/d=A; 41/d=-1; p1/e=p2/e=B;
# 41/f=-1; p1/f=p2/f=A*B.  Mod-3 bits are (1,0).
def forced_bits(A,B):
 assert A in (1,-1) and B in (1,-1)
 bit=lambda z:0 if z==1 else 1
 return {
  (0,4):1,(0,5):0,
  (1,4):bit(A),(1,5):bit(A),(1,7):1,
  (2,5):bit(B),
  (3,4):bit(A*B),(3,5):bit(A*B),(3,6):0,(3,7):1,
 }
def chart_holds_forced(chart,A,B):
 f=forced_bits(A,B)
 return all(f.get((i,j))==rhs for i,j,rhs in chart)
assert chart_holds_forced(CHART_A,1,-1)
assert chart_holds_forced(CHART_C,-1,-1)
assert all(chart_holds_forced(CHART_A if A==1 else CHART_C,A,-1) for A in (1,-1))
ot=c['one_bit_theorem']
assert ot['sufficient_condition']=='B=-1'
assert ot['covers_both_A_signs'] is True
assert ot['B_minus_implies_rank_2n_minus_2'] is True and ot['B_minus_implies_sel2_dimension_2'] is True
assert ot['global_over_all_realizations_of_factor_shape'] is True
assert ot['B_minus_claimed_necessary'] is False and ot['factor_shape_realizations_claimed_infinite'] is False

# Exact new arithmetic realizations and registry separation.
new=set()
for row in c['arithmetic_realizations']:
 u=row['u'];j=row['j'];assert u==17627+34440*j
 primes,vals=prime_support(u,row['factorization'])
 # canonical order: 3,d,e,f,p1,p2,7,41,q1,q2
 d,e,f,p1,p2=primes[1],primes[2],primes[3],primes[4],primes[5]
 assert d==u and e==4*u+K and f==2*u+K
 assert p1%3==2 and p2%3==1
 A=-1 if legbit(p1,d) else 1;B=-1 if legbit(p1,e) else 1
 assert A==row['A'] and B==row['B']==-1
 assert (-1 if legbit(p2,d) else 1)==A
 assert (-1 if legbit(p2,e) else 1)==B
 assert (-1 if legbit(41,d) else 1)==-1
 assert (-1 if legbit(7,f) else 1)==1
 assert (-1 if legbit(41,f) else 1)==-1
 assert (-1 if legbit(p1,f) else 1)==A*B
 assert (-1 if legbit(p2,f) else 1)==A*B
 chosen=CHART_A if A==1 else CHART_C
 assert chart_ok(primes,chosen)
 M,n=matrix_from_pattern(numeric_object(primes));r=rank(M)
 tr,H,_,_=peel(M);rh=rank(H)
 assert (n,r,len(tr),len(H),rh,len(H)-rh)==(12,22,22,2,0,2)
 a=2*u;b=2*u+K;q=4*u+K
 assert math.gcd(u,b)==math.gcd(u,q)==math.gcd(b,q)==1
 assert math.isqrt(u)**2!=u and math.isqrt(u*b*q)**2!=u*b*q
 assert [z%5 for z in psi3_coeffs(a,b)]==[4,0,4,0,3]
 assert not has_root_mod(psi3_coeffs(a,b),5)
 orbit={Fraction(a,b),Fraction(b,a),Fraction(K,q),Fraction(q,K)}
 assert orbit=={Fraction(x) for x in row['literal_orbit']}
 assert not(orbit&previous) and not(orbit&new);new.update(orbit)
assert len(new)==16 and len(previous|new)==224
ri=c['registry_impact']
assert ri['previous_count']==208 and ri['new_orbits']==4 and ri['new_parameters']==16 and ri['disjoint'] is True and ri['provisional_count']==224
assert ri['exact_sufficient_template_count_unchanged']==17

# Diagnostic is retained as finite evidence only; no necessity/global opposite-sign credit.
di=c['diagnostic_200k']
assert di['exact_factor_shape_hits']==43 and di['B_minus_hits']==di['B_minus_rank22_hits']==25
assert di['B_plus_hits']==di['B_plus_rank20_hits']==18
assert di['B_plus_global_rank20_claimed'] is False and di['diagnostic_exhaustiveness_outside_domain_claimed'] is False
assert c['route_result']['next_leaf']=='36-09FC_RHO_ONE_BIT_SPLITTING_FORCE_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for key,val in c['scope_firewalls'].items():assert val is False,(key,val)
print('36-09FB verified: arithmetic factor identities plus FA Chart A and new Chart C prove the single splitting condition (p1/e)=-1 sufficient for rank 22/Sel2_dim=2 on the exact factor shape; four new EH-clean literal orbits give provisional registry 208->224. No necessity/infinitude/parent receiver/endpoint credit.')
