#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DK/fixed-p2-f5-full-rational-component-span-preflight.json'
DJ=ROOT/'stages/stage36/36-09DJ/fixed-p2-f5-minus-r5-explicit-corestriction-preflight.json'
CW=ROOT/'stages/stage36/36-09CW/bt-literal-non-kummer-divisor-cech-construction-preflight.json'
SRC=ROOT/'stages/stage36/36-09DK/rational-component-reflection-source-lock.md'
BASE='1eea6800e479729c41ed8767a38298384a2dbc0f'
DJ_HEAD='b31c1017824be394785d1feaa2dd3b3717099e02'
PROMO='c46174566aff2abba5ea7fe83ffa336ed52a92d0'
LOCKS={
    CERT:'dd59fb2492e3bcb75409cc316c85ea6a130d10d1',
    DJ:'76b57c000b551846c24a0c7236c206d929faff20',
    CW:'a363c230cb44fec6d235eda0720d4fd624b1a87c',
    SRC:'ff93459f7c6c98f7ba57258bf5043a516b6d3e37',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def F(s:str)->Fraction:return Fraction(s)

def eval_poly(a:list[Fraction],t:Fraction)->Fraction:
    z=Fraction(0)
    for c in reversed(a):z=z*t+c
    return z

def vp(a:Fraction,p:int)->int:
    assert a
    n=abs(a.numerator);d=a.denominator;v=0
    while n%p==0:n//=p;v+=1
    while d%p==0:d//=p;v-=1
    return v

def unit_mod(a:Fraction,p:int)->int:
    v=vp(a,p);n=a.numerator;d=a.denominator
    if v>=0:n//=p**v
    else:d//=p**(-v)
    return (n%p)*pow(d%p,-1,p)%p

def leg(a:int,p:int)->int:
    a%=p;assert a
    q=pow(a,(p-1)//2,p);return 1 if q==1 else -1

def hilbert(a:Fraction,b:Fraction,p:int)->int:
    va,vb=vp(a,p),vp(b,p);ua,ub=unit_mod(a,p),unit_mod(b,p);e=0
    if (((p-1)//2)&1) and ((va*vb)&1):e^=1
    if (vb&1) and leg(ua,p)==-1:e^=1
    if (va&1) and leg(ub,p)==-1:e^=1
    return e

def square_q5(a:Fraction)->bool:
    return vp(a,5)%2==0 and leg(unit_mod(a,5),5)==1

def main()->None:
    for p,h in LOCKS.items():assert blob(p)==h,(p,blob(p),h)
    for h in [BASE,DJ_HEAD,PROMO]:subprocess.check_call(['git','merge-base','--is-ancestor',h,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text());dj=json.loads(DJ.read_text());cw=json.loads(CW.read_text());src=SRC.read_text()
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
      'pr':1712,
      '36_09DJ_exact_green_head':DJ_HEAD,
      '36_09DJ_exact_head_ci':'34211554107/102013504416',
      'promotion_replay_head':PROMO,
      'promotion_replay_ci':'34211686132/102013927335'
    }
    assert dj['credit_boundary']['F5_not_equal_R5_mod_BrQ_proved'] is True
    assert cw['explicit_family']['literal_unramified_Brauer_family_constructed'] is True
    assert 'full rational-component image is generated' in src
    assert 'ev_u - ev_-u' in src

    rc=c['full_rational_component_image']
    assert rc['Brauer_generators']=='(d,fj(t))_2 for arbitrary d in Q^*/Q^*2 and j in {0,1,2,3}'
    assert rc['every_generator_even_in_t'] is True
    assert rc['every_rational_component_class_even_evaluation_under_t_to_minus_t'] is True

    facs=[lambda t:t*t+4,lambda t:t*t+Fraction(1,4),lambda t:t*t+9,lambda t:t*t+Fraction(1,9)]
    tp,tm=Fraction(11),Fraction(-11)
    vals_p=[f(tp) for f in facs];vals_m=[f(tm) for f in facs]
    assert vals_p==vals_m
    rhs=Fraction(1)
    for z in vals_p:rhs*=z
    assert rhs==F(c['reflection_functional']['same_rhs'])==Fraction(2147640625,9)
    assert vp(rhs,5)==c['reflection_functional']['rhs_v5']==6
    assert unit_mod(rhs,5)==c['reflection_functional']['rhs_unit_mod5']==1
    assert square_q5(rhs)
    assert c['reflection_functional']['both_receiver_Q5_points_exist'] is True
    assert c['reflection_functional']['factor_values_identical_exactly'] is True
    assert c['reflection_functional']['annihilates_every_full_rational_component_class'] is True
    assert c['reflection_functional']['annihilates_constants'] is True

    chain=[[F(x) for x in row] for row in dj['euclidean_chain']['coefficients_low_to_high']]
    got=[]
    for t in [tp,tm]:
        vv=[eval_poly(r,t) for r in chain]
        assert all(x!=0 for x in vv)
        par=[hilbert(vv[i+1],vv[i],5) for i in range(8)]
        s=0
        for e in par:s^=e
        got.append((par,s))
    assert got[0][0]==c['F5_evaluation']['delta_Rosset_Tate_parities_at_t_11']
    assert got[1][0]==c['F5_evaluation']['delta_Rosset_Tate_parities_at_t_minus11']
    assert [got[0][1],got[1][1]]==c['F5_evaluation']['delta_variable_sum_parities']==[0,1]
    assert c['F5_evaluation']['R5_reflection_difference']==0
    assert c['F5_evaluation']['F5_reflection_invariant_difference']=='1/2'
    assert c['F5_evaluation']['F5_nonzero_under_rational_component_annihilator'] is True

    sc=c['separation_consequence'];cb=c['current_credit_boundary']
    assert sc['F5_outside_entire_rational_component_image_mod_BrQ'] is True
    assert sc['F5_genuine_nonrational_component_direction_in_Creutz_Viray_explicit_image'] is True
    assert cb['F5_outside_entire_rational_component_image'] is True
    assert cb['genuine_nonrational_Creutz_Viray_direction_found'] is True
    for k in ['rational_component_image_BM_set_nonempty','rational_plus_F5_BM_set_nonempty','full_Creutz_Viray_explicit_image_computed','full_L1_quotient_computed','Pic0_mod2_computed','full_Brauer_group_computed','Brauer_Manin_obstruction_from_full_Br_group_proved','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
        assert cb[k] is False,k
    assert c['route_result']['next_leaf']=='36-09DL_FIXED_P2_FULL_RATIONAL_COMPONENT_ADELIC_CONTROL_PREFLIGHT'
    for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
    print('36-09DK verified: reflected Q5 receiver points t=11,-11 have identical four branch-factor values, so every rational-component Brauer class and every constant has zero evaluation difference. The DJ corestriction gives F5 reflected difference 1/2. Hence F5 lies outside the entire rational-component image modulo Br(Q). Full explicit/full Brauer/BM/fixed-p credit remains open.')

if __name__=='__main__':main()
