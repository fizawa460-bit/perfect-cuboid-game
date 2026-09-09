#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DL/fixed-p2-full-rational-component-adelic-control-preflight.json'
DK=ROOT/'stages/stage36/36-09DK/fixed-p2-f5-full-rational-component-span-preflight.json'
SRC=ROOT/'stages/stage36/36-09DL/full-rational-component-factorwise-square-source-lock.md'
BASE='1eea6800e479729c41ed8767a38298384a2dbc0f'
DK_HEAD='b673f8d711873ca83d36ce849a28c207bb0675b7'
PROMO='11b28d18fea9befc8cb7b5cbc0735d37fc92fbe8'
LOCKS={CERT:'f3c8cba00d00b81fed2b316a62af96fc106cdaa7',DK:'dd59fb2492e3bcb75409cc316c85ea6a130d10d1',SRC:'02fdb27a59d252bfd73571173d6c246767239b6a'}

def git(*a:str)->str:return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p:Path)->str:return git('hash-object',str(p.relative_to(ROOT)))
def vp(a:Fraction,p:int)->int:
    assert a
    n=abs(a.numerator);d=a.denominator;v=0
    while n%p==0:n//=p;v+=1
    while d%p==0:d//=p;v-=1
    return v
def unit_mod(a:Fraction,p:int,m:int|None=None)->int:
    v=vp(a,p);n=a.numerator;d=a.denominator
    if v>=0:n//=p**v
    else:d//=p**(-v)
    mod=m or p
    return (n%mod)*pow(d%mod,-1,mod)%mod
def leg(a:int,p:int)->int:
    a%=p;assert a
    q=pow(a,(p-1)//2,p);return 1 if q==1 else -1
def square_odd(a:Fraction,p:int)->bool:return vp(a,p)%2==0 and leg(unit_mod(a,p),p)==1
def square_2(a:Fraction)->bool:return vp(a,2)%2==0 and unit_mod(a,2,8)==1
def factors(t:Fraction)->list[Fraction]:return [t*t+4,t*t+Fraction(1,4),t*t+9,t*t+Fraction(1,9)]

def primes_upto(n:int):
    out=[]
    for x in range(2,n+1):
        if all(x%d for d in range(2,int(x**0.5)+1)):out.append(x)
    return out

def main()->None:
    for p,h in LOCKS.items():assert blob(p)==h,(p,blob(p),h)
    for h in [BASE,DK_HEAD,PROMO]:subprocess.check_call(['git','merge-base','--is-ancestor',h,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text());dk=json.loads(DK.read_text());src=SRC.read_text()
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1712,'36_09DK_exact_green_head':DK_HEAD,'36_09DK_exact_head_ci':'34212206197/102015582572','promotion_replay_head':PROMO,'promotion_replay_ci':'34212313701/102015925546'}
    assert dk['current_credit_boundary']['F5_outside_entire_rational_component_image'] is True
    assert 'every generator `(d,fj(t_v))_2` is pointwise trivial' in src

    # Real place.
    assert all(x>0 for x in factors(Fraction(2)))
    # Q2 recipe.
    q2=factors(Fraction(8)); assert q2==[Fraction(68),Fraction(257,4),Fraction(73),Fraction(577,9)]
    assert all(square_2(x) for x in q2)
    assert [vp(x,2)%2 for x in q2]==c['adelic_recipe']['Q2']['valuation_parities']==[0,0,0,0]
    assert [unit_mod(x,2,8) for x in q2]==c['adelic_recipe']['Q2']['odd_units_mod8']==[1,1,1,1]
    # Q3 recipe.
    q3=factors(Fraction(9)); assert q3==[Fraction(85),Fraction(325,4),Fraction(90),Fraction(730,9)]
    assert all(square_odd(x,3) for x in q3)
    assert [vp(x,3)%2 for x in q3]==c['adelic_recipe']['Q3']['valuation_parities']==[0,0,0,0]
    assert [unit_mod(x,3) for x in q3]==c['adelic_recipe']['Q3']['units_mod3']==[1,1,1,1]
    # Uniform l>3 identity checked over a bounded prime sample; source records the symbolic Hensel argument.
    aa=[Fraction(2),Fraction(1,2),Fraction(3),Fraction(1,3)]
    for ell in [p for p in primes_upto(199) if p>3]:
        vv=factors(Fraction(ell))
        for x,a in zip(vv,aa):
            assert x==a*a*(1+(Fraction(ell)/a)**2)
            assert vp(x,ell)==0 and leg(unit_mod(x,ell),ell)==1
    ar=c['adelic_recipe'];ro=c['rational_component_orthogonality'];cb=c['current_credit_boundary']
    assert ar['all_parameters_retained_open'] is True and ar['receiver_local_point_every_place'] is True and ar['adelic_point_exists'] is True
    assert ro['each_generator_pointwise_invariant_zero_at_every_place'] is True
    assert ro['orthogonal_to_full_rational_component_image'] is True
    assert ro['full_rational_component_Brauer_set_nonempty'] is True
    assert ro['not_a_finite_generator_truncation'] is True
    assert cb['p2_adelic_point_orthogonal_to_full_rational_component_image_constructed'] is True
    assert cb['full_rational_component_image_BM_obstruction_disproved'] is True
    for k in ['rational_plus_F5_BM_set_nonempty','full_nonrational_component_control','full_Creutz_Viray_explicit_image_computed','full_L1_quotient_computed','Pic0_mod2_computed','full_Brauer_group_computed','Brauer_Manin_obstruction_from_full_Br_group_proved','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
        assert cb[k] is False,k
    assert c['route_result']['next_leaf']=='36-09DM_FIXED_P2_FULL_RATIONAL_COMPONENT_PLUS_F5_ADELIC_CONTROL_PREFLIGHT'
    for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
    print('36-09DL verified: an explicit retained-open adelic point makes all four branch factors local squares at every place. Hence every rational-component generator (d,f_j) evaluates pointwise to zero and the full rational-component Brauer set is nonempty. F5/full nonrational/full Brauer/BM/fixed-p credit remains open.')
if __name__=='__main__':main()
