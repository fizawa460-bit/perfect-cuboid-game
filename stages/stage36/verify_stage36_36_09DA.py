#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DA/fixed-p2-second-independent-brauer-evaluation-matrix-preflight.json'
CZ=ROOT/'stages/stage36/36-09CZ/fixed-p2-brauer-local-image-adelic-sum-preflight.json'
CW=ROOT/'stages/stage36/36-09CW/bt-literal-non-kummer-divisor-cech-construction-preflight.json'
BASE='f2a89e613cdf91191a0aada9e90c9fc93373a6c6'
CZ_HEAD='bc0df8c5604dd66d9225afd125c0db847a49493e'
PROMO_HEAD='5626183da7876d44a34c44521ad4398da8eb4207'
LOCKS={
    CERT:'8f286f71e828c18e19d65721ca5b3728650f680f',
    CZ:'dc0e80444707e57ce9ddb41fe76682a76e65f760',
    CW:'a363c230cb44fec6d235eda0720d4fd624b1a87c',
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

def invstr(s:int)->str:
    return '0' if s==1 else '1/2'

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CZ_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMO_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); cz=json.loads(CZ.read_text()); cw=json.loads(CW.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
        'pr':1712,
        '36_09CZ_exact_green_head':CZ_HEAD,
        '36_09CZ_exact_head_ci':'34200137461/101976800810',
        'promotion_replay_head':PROMO_HEAD,
        'promotion_replay_ci':'34200274467/101977231581'
    }
    assert cz['current_credit_boundary']['selected_class_A_Brauer_Manin_obstruction_disproved_conditional_on_adelic_solubility'] is True
    assert cw['explicit_family']['literal_unramified_Brauer_family_constructed'] is True
    assert 'A_d0=(d,t^2+p^2)_2' in cw['explicit_family']['literal_classes']
    assert 'A_d2=(d,t^2+c^2)_2' in cw['explicit_family']['literal_classes']

    fc=c['fixed_classes']
    assert fc['A']=='(7,t^2+4)_2' and fc['B']=='(7,t^2+9)_2'
    assert fc['A_unramified'] is True and fc['B_unramified'] is True

    expected={
      7:(Fraction(66916369,9),1,1,4,2,'0','0'),
      8:(Fraction(184026649,9),1,1,5,3,'1/2','1/2'),
      2:(Fraction(16354,9),1,1,1,6,'0','1/2'),
      3:(Fraction(19721),2,3,6,4,'1/2','0'),
    }
    seen=set()
    rows={int(r['t']):r for r in c['q7_joint_evaluation_witnesses']}
    assert set(rows)==set(expected)
    for t,(rex,rmod,zmod,amod,bmod,ainv,binv) in expected.items():
        T=Fraction(t); r=rhs(T)
        assert r==rex and mod_frac(r,7)==rmod
        assert (zmod*zmod-rmod)%7==0 and (2*zmod)%7!=0
        A=mod_frac(T*T+4,7); B=mod_frac(T*T+9,7)
        assert (A,B)==(amod,bmod)
        assert invstr(legendre(A,7))==ainv
        assert invstr(legendre(B,7))==binv
        row=rows[t]
        assert row['rhs_exact']==str(rex) and row['rhs_mod7']==rmod
        assert row['A_invariant']==ainv and row['B_invariant']==binv and row['nonboundary'] is True
        seen.add((ainv,binv))
    full={('0','0'),('0','1/2'),('1/2','0'),('1/2','1/2')}
    assert seen==full

    ji=c['joint_image']; ind=c['independence_consequence']; ad=c['pair_subgroup_adelic_consequence']
    assert ji['equals_full_F2_squared'] is True and ji['all_points_exist_by_Hensel_in_z'] is True
    assert ind['A_B_independent_in_BrC_mod_BrQ'] is True
    assert ind['BT_SECOND_INDEPENDENT_BRAUER_CLASS_FOUND_FOR_FIXED_P2'] is True
    assert ad['pair_subgroup_can_supply_Brauer_Manin_obstruction'] is False
    assert ad['does_not_compute_full_Brauer_group'] is True
    assert ad['does_not_rule_out_a_third_independent_class'] is True
    assert ad['does_not_prove_adelic_solubility'] is True

    cb=c['current_credit_boundary']
    assert cb['second_independent_Brauer_class_found'] is True
    assert cb['joint_evaluation_matrix_complete_at_q7'] is True
    assert cb['pair_subgroup_BM_obstruction_disproved_conditional_on_adelic_solubility'] is True
    for k in ['full_Brauer_group_computed','third_independent_class_excluded','Brauer_Manin_obstruction_from_full_Br_group_proved','fixed_p_2_branch_excluded','receiver_emptiness_proved']:
        assert cb[k] is False,k
    assert c['route_result']['next_leaf']=='36-09DB_FIXED_P2_HYPERELLIPTIC_BRAUER_RANK_THIRD_CLASS_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09DA verified: A=(7,t^2+4)_2 and B=(7,t^2+9)_2 are independent modulo Br(Q) because C3_2(Q_7) realizes the full F2^2 joint evaluation image. Consequently <A,B> cannot be a BM obstruction whenever an adelic point exists. Full Brauer rank/third class remains open; no fixed-p/receiver/endpoint credit.')

if __name__=='__main__': main()
