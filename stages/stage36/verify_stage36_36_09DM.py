#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DM/fixed-p2-full-cv-explicit-image-boundary-adelic-control-preflight.json'
SRC=ROOT/'stages/stage36/36-09DM/boundary-squareclass-explicit-image-adelic-source-lock.md'
DL=ROOT/'stages/stage36/36-09DL/fixed-p2-full-rational-component-adelic-control-preflight.json'
CW=ROOT/'stages/stage36/36-09CW/creutz-viray-hyperelliptic-brauer-source-lock.md'
DD=ROOT/'stages/stage36/36-09DD/creutz-viray-explicit-image-completeness-source-lock.md'
LIT=ROOT/'docs/arsenal/lit-wf02-global-h1-localization-reciprocity-contract.json'
BASE='1eea6800e479729c41ed8767a38298384a2dbc0f'
DL_HEAD='fd628494e24daa6a6d9f300f0b61b90a1c26432e'
PROMO='d3799d2c9ec3aa02fca88e738d41a51c366bdc13'
LOCKS={
    CERT:'95956c74aca1aca1601a1f4c77b66bfb226a5198',
    SRC:'75257e9aca83b198809a6a3ed2c5aa44f29c7fb8',
    DL:'f3c8cba00d00b81fed2b316a62af96fc106cdaa7',
    CW:'4657040230644aef1dbef427a3a5ab6afe3998aa',
    DD:'632e908d3fcd4d1f3511be99b3993469537e3c07',
    LIT:'6fc62623ee59b4aaf1fc053ad42df2dcbba0855b',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def vp(x:Fraction,p:int)->int:
    assert x
    n=abs(x.numerator); d=x.denominator; v=0
    while n%p==0: n//=p; v+=1
    while d%p==0: d//=p; v-=1
    return v

def unit_mod(x:Fraction,p:int,m:int|None=None)->int:
    v=vp(x,p); n=x.numerator; d=x.denominator
    if v>=0: n//=p**v
    else: d//=p**(-v)
    mod=m or p
    return (n%mod)*pow(d%mod,-1,mod)%mod

def legendre(a:int,p:int)->int:
    a%=p; assert a
    z=pow(a,(p-1)//2,p)
    return 1 if z==1 else -1

def square_q2(x:Fraction)->bool:
    return vp(x,2)%2==0 and unit_mod(x,2,8)==1

def square_odd(x:Fraction,p:int)->bool:
    return vp(x,p)%2==0 and legendre(unit_mod(x,p),p)==1

def factors(t:Fraction)->list[Fraction]:
    return [t*t+4,t*t+Fraction(1,4),t*t+9,t*t+Fraction(1,9)]

def primes_upto(n:int)->list[int]:
    out=[]
    for x in range(2,n+1):
        if all(x%d for d in range(2,int(x**0.5)+1)): out.append(x)
    return out

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    for h in [BASE,DL_HEAD,PROMO]:
        subprocess.check_call(['git','merge-base','--is-ancestor',h,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); dl=json.loads(DL.read_text()); src=SRC.read_text(); cw=CW.read_text(); dd=DD.read_text(); lit=json.loads(LIT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
      'pr':1712,
      '36_09DL_exact_green_head':DL_HEAD,
      '36_09DL_exact_head_ci':'34213028270/102018234558',
      'promotion_replay_head':PROMO,
      'promotion_replay_ci':'34213196474/102018756323'
    }
    assert dl['current_credit_boundary']['p2_adelic_point_orthogonal_to_full_rational_component_image_constructed'] is True
    assert "gamma'(ell)=Cor" in cw
    assert 'does **not** identify that image with all' in dd
    assert lit['literature'][0]['theorem_identifier']=='Chapter III Theorems 2-4'
    assert 'Global Brauer/Hilbert reciprocity' in src

    fc=c['fixed_curve_and_branch_algebra']
    aa=[Fraction(2),Fraction(1,2),Fraction(3),Fraction(1,3)]
    assert fc['a_j']==['2','1/2','3','1/3']
    assert fc['alpha_j']==['2i','i/2','3i','i/3']

    # P0=(0,1): product of constant factors is exactly one and z is nonzero.
    assert factors(Fraction(0))==[Fraction(4),Fraction(1,4),Fraction(9),Fraction(1,9)]
    prod=Fraction(1)
    for x in factors(Fraction(0)): prod*=x
    assert prod==1
    p0=c['global_reference_point']
    assert p0['t']==0 and p0['z']==1 and p0['on_curve'] is True and p0['smooth'] is True and p0['rational'] is True
    assert p0['retained_open'] is False

    ar=c['adelic_recipe']; bl=c['branch_linear_squareclass_control']
    # E_2 valuation normalized by v(1+i)=1, hence v_E(2)=2.
    t2=Fraction(32)
    rational_v2=[vp(t2/a,2) for a in aa]
    e2_v=[2*v for v in rational_v2]
    assert rational_v2==[4,6,5,5]
    assert e2_v==ar['Q2']['v_t_over_a_j']==[8,12,10,10]
    assert ar['Q2']['normalized_v_1_plus_i']==1 and ar['Q2']['v_2']==2
    assert ar['Q2']['hensel_threshold_2v2']==4
    assert all(v>4 for v in e2_v) and ar['Q2']['all_strictly_above_threshold'] is True
    # Norm-side independent check: all four factors at t=32 are Q2 squares.
    assert all(square_q2(x) for x in factors(t2))

    # At Q3, E/Q3 is unramified and 2 is a unit; every ratio is 1 mod the maximal ideal.
    t3=Fraction(9)
    v3=[vp(t3/a,3) for a in aa]
    assert v3==ar['Q3']['v3_t_over_a_j']==[2,2,1,3]
    assert all(v>0 for v in v3) and ar['Q3']['all_positive'] is True
    assert all(square_odd(x,3) for x in factors(t3))

    # For every odd p>3 the symbolic condition is t/a_j in p O. Check over a bounded prime sample,
    # and independently check the norm factors are local squares as in DL.
    for p in [q for q in primes_upto(199) if q>3]:
        for a in aa: assert vp(Fraction(p)/a,p)==1
        assert all(square_odd(x,p) for x in factors(Fraction(p)))

    # Real component is retained and all norm factors are positive.
    assert all(x>0 for x in factors(Fraction(2)))
    assert ar['real']['t']==2 and ar['real']['linear_squareclass_preserved'] is True
    assert ar['all_t_coordinates_retained_open'] is True
    assert ar['receiver_local_point_every_place'] is True and ar['adelic_point_exists'] is True
    assert ar['integral_all_but_finitely_many_places'] is True

    assert bl['ratio_formula']=='(t_v-alpha_j)/(-alpha_j)=1+i*(t_v/a_j)'
    for k in ['Q2_all_ratios_squares','Q3_all_ratios_squares','odd_p_gt_3_all_ratios_squares','real_all_ratios_squares','same_branch_linear_squareclasses_as_P0']:
        assert bl[k] is True,k
    assert bl['all_places_all_components']=='[t_v-alpha_j]=[-alpha_j]'

    ev=c['explicit_image_evaluation']
    assert ev['Creutz_Viray_formula']=="gamma'(ell)=Cor((ell,t-alpha)_2)"
    for k in ['for_every_ell_in_L1_local_evaluation_equals_P0','P0_evaluation_is_localization_of_global_BrQ_class','global_reciprocity_total_invariant_zero','constant_BrQ_classes_total_invariant_zero','adelic_point_orthogonal_to_entire_Creutz_Viray_explicit_image','full_Creutz_Viray_explicit_image_BM_set_nonempty','full_Creutz_Viray_explicit_image_BM_obstruction_disproved','rational_plus_F5_BM_set_nonempty']:
        assert ev[k] is True,k

    cb=c['current_credit_boundary']
    for k in ['p2_retained_open_adelic_point_orthogonal_to_entire_Creutz_Viray_explicit_image','full_Creutz_Viray_explicit_image_BM_set_nonempty','full_Creutz_Viray_explicit_image_BM_obstruction_disproved','rational_plus_F5_BM_set_nonempty']:
        assert cb[k] is True,k
    for k in ['full_Creutz_Viray_explicit_image_computed','full_L1_quotient_computed','Pic0_mod2_computed','Creutz_Viray_explicit_image_equals_full_Br2','full_Brauer_group_computed','Brauer_Manin_obstruction_from_full_Br_group_proved','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
        assert cb[k] is False,k
    assert c['route_result']['next_leaf']=='36-09DN_FIXED_P2_FULL_BRAUER_OUTSIDE_CREUTZ_VIRAY_FORMAL_DISK_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09DM verified: a retained-open adelic point preserves every branch-linear squareclass relative to global P0=(0,1). Therefore every Creutz-Viray explicit class has the same local evaluations as at P0 and global reciprocity makes the entire explicit-image Brauer set nonempty. Full Brauer/full-BM/fixed-p/receiver/endpoint credit remains open.')

if __name__=='__main__': main()
