#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DD/fixed-p2-creutz-viray-subgroup-completeness-preflight.json'
DC=ROOT/'stages/stage36/36-09DC/fixed-p2-rank3-brauer-two-place-evaluation-matrix-preflight.json'
CW=ROOT/'stages/stage36/36-09CW/bt-literal-non-kummer-divisor-cech-construction-preflight.json'
SRC=ROOT/'stages/stage36/36-09CW/creutz-viray-hyperelliptic-brauer-source-lock.md'
BASE='f2a89e613cdf91191a0aada9e90c9fc93373a6c6'
DC_HEAD='3b8e52fb6cd2629a4c7aef5f3a33a8b046faddfa'
PROMO_HEAD='04cff03159545c7c7638ea7ece9a962c0572153e'
LOCKS={
    CERT:'81c580ab09f2fc265f033c51e99f3a553d726f92',
    DC:'4865bd16973ddf0fd746bc4219ea68b8277817b3',
    CW:'a363c230cb44fec6d235eda0720d4fd624b1a87c',
    SRC:'4657040230644aef1dbef427a3a5ab6afe3998aa',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def rhs(t:Fraction)->Fraction:
    return (t*t+4)*(t*t+Fraction(1,4))*(t*t+9)*(t*t+Fraction(1,9))

def mod_frac(x:Fraction,p:int)->int:
    return (x.numerator%p)*pow(x.denominator%p,-1,p)%p

def legendre(a:int,p:int)->int:
    a%=p
    if a==0:return 0
    v=pow(a,(p-1)//2,p)
    return 1 if v==1 else -1

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',DC_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMO_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); dc=json.loads(DC.read_text()); cw=json.loads(CW.read_text()); src=SRC.read_text()
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
      'pr':1712,
      '36_09DC_exact_green_head':DC_HEAD,
      '36_09DC_exact_head_ci':'34202501921/101984315846',
      'promotion_replay_head':PROMO_HEAD,
      'promotion_replay_ci':'34202823332/101985326362'
    }
    assert dc['current_credit_boundary']['rank3_constructed_subgroup_BM_obstruction_disproved_conditional_on_adelic_solubility'] is True
    assert cw['explicit_family']['literal_unramified_Brauer_family_constructed'] is True
    assert 'A_d0=(d,t^2+p^2)_2' in cw['explicit_family']['literal_classes']
    assert 'does **not** prove that any `A_{d,j}` is nonconstant modulo `Br(Q)`' in src

    fc=c['fourth_candidate']
    assert fc['class']=='E=(17,t^2+4)_2' and fc['unramified_on_C3_2'] is True
    rows={int(r['t']):r for r in c['q17_independence_witnesses']}
    expected={
      3:(Fraction(19721),1,1,13,1,'0'),
      4:(Fraction(1178125,9),16,4,3,8,'1/2'),
    }
    for t,(rex,rmod,zmod,f0,f2,einv) in expected.items():
        T=Fraction(t); r=rhs(T)
        assert r==rex and mod_frac(r,17)==rmod
        assert (zmod*zmod-rmod)%17==0 and (2*zmod)%17!=0
        assert mod_frac(T*T+4,17)==f0
        assert mod_frac(T*T+9,17)==f2
        assert f0!=0 and f2!=0
        calc='0' if legendre(f0,17)==1 else '1/2'
        row=rows[t]
        assert row['rhs_exact']==str(rex)
        assert row['A_invariant']==row['B_invariant']==row['D_invariant']=='0'
        assert row['E_invariant']==einv==calc
        assert row['nonboundary'] is True

    ic=c['independence_consequence']
    assert ic['E_nonconstant_mod_BrQ'] is True
    assert ic['E_not_in_span_A_B_D_mod_BrQ'] is True
    assert ic['A_B_D_E_independent_in_BrC_mod_BrQ'] is True
    assert ic['BT_FOURTH_INDEPENDENT_BRAUER_CLASS_FOUND_FOR_FIXED_P2'] is True
    assert ic['constructed_Brauer_subgroup_rank_lower_bound']==4
    assert ic['rank3_completeness_disproved'] is True

    bd=c['creutz_viray_completeness_boundary']
    for k in ['rank3_explicit_subgroup_exhausts_CW_family','rank3_explicit_subgroup_exhausts_full_Brauer_group','full_Creutz_Viray_explicit_image_computed','full_Brauer_group_computed']:
        assert bd[k] is False,k
    cb=c['current_credit_boundary']
    assert cb['four_independent_CW_classes_found'] is True
    assert cb['constructed_Brauer_subgroup_rank_at_least_4'] is True
    for k in ['constructed_Brauer_subgroup_rank_exactly_4','full_Creutz_Viray_explicit_image_computed','full_Brauer_group_computed','rank4_joint_adelic_evaluation_matrix_complete','Brauer_Manin_obstruction_from_full_Br_group_proved','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
        assert cb[k] is False,k
    assert c['route_result']['next_leaf']=='36-09DE_FIXED_P2_PRIME_PRIVATE_BRAUER_FAMILY_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09DD verified: E=(17,t^2+4)_2 is a fourth unramified class independent of A,B,D; Q17 receiver witnesses keep A,B,D zero while E varies. Constructed rank >=4 and rank3 completeness is disproved. Full Creutz-Viray image/full Brauer group remain open; no BM/fixed-p/receiver/endpoint credit.')

if __name__=='__main__': main()
