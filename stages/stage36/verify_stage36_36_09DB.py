#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DB/fixed-p2-hyperelliptic-brauer-rank-third-class-preflight.json'
DA=ROOT/'stages/stage36/36-09DA/fixed-p2-second-independent-brauer-evaluation-matrix-preflight.json'
CW=ROOT/'stages/stage36/36-09CW/bt-literal-non-kummer-divisor-cech-construction-preflight.json'
BASE='f2a89e613cdf91191a0aada9e90c9fc93373a6c6'
DA_HEAD='114d44b1e5014c6756a40edcd717da385fb2b383'
PROMO_HEAD='bee1328e5c12c7bead83818afe6327124a0ffc1c'
LOCKS={
    CERT:'fbdf20fd4c4f4f338d31a55a2a1dd0786ca968c8',
    DA:'8f286f71e828c18e19d65721ca5b3728650f680f',
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

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',DA_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMO_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); da=json.loads(DA.read_text()); cw=json.loads(CW.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
      'pr':1712,
      '36_09DA_exact_green_head':DA_HEAD,
      '36_09DA_exact_head_ci':'34201477356/101981018057',
      'promotion_replay_head':PROMO_HEAD,
      'promotion_replay_ci':'34201650283/101981578856'
    }
    assert da['independence_consequence']['A_B_independent_in_BrC_mod_BrQ'] is True
    assert cw['explicit_family']['literal_unramified_Brauer_family_constructed'] is True
    assert 'A_d0=(d,t^2+p^2)_2' in cw['explicit_family']['literal_classes']

    fc=c['fixed_curve_and_classes']
    assert fc['D']=='(11,t^2+4)_2' and fc['D_unramified'] is True
    rows={int(r['t']):r for r in c['q11_independence_witnesses']}
    expected={
      4:(Fraction(1178125,9),4,2,9,3,'0','0','0'),
      3:(Fraction(19721),9,3,2,7,'0','0','1/2'),
    }
    for t,(rex,rmod,zmod,f0,f2,ai,bi,di) in expected.items():
        T=Fraction(t); r=rhs(T)
        assert r==rex and mod_frac(r,11)==rmod
        assert (zmod*zmod-rmod)%11==0 and (2*zmod)%11!=0
        assert mod_frac(T*T+4,11)==f0
        assert mod_frac(T*T+9,11)==f2
        # A and B have first entry 7, an 11-adic unit, and the second entries are units.
        # D has first entry 11, so its unit-second-entry Hilbert symbol is the Legendre symbol.
        assert f0!=0 and f2!=0
        dcalc='0' if legendre(f0,11)==1 else '1/2'
        row=rows[t]
        assert row['rhs_exact']==str(rex) and row['A_invariant']==ai and row['B_invariant']==bi
        assert row['D_invariant']==di==dcalc and row['nonboundary'] is True

    tc=c['third_independence_consequence']
    assert tc['D_nonconstant_mod_BrQ'] is True
    assert tc['D_not_in_span_A_B_mod_BrQ'] is True
    assert tc['A_B_D_independent_in_BrC_mod_BrQ'] is True
    assert tc['BT_THIRD_INDEPENDENT_BRAUER_CLASS_FOUND_FOR_FIXED_P2'] is True
    assert tc['relevant_constructed_subgroup_rank_lower_bound']==3

    cb=c['current_credit_boundary']
    assert cb['three_independent_CW_classes_found'] is True
    assert cb['constructed_Brauer_subgroup_rank_at_least_3'] is True
    for k in ['constructed_Brauer_subgroup_rank_exactly_3','full_Brauer_group_computed','A_B_D_span_full_relevant_Brauer_group','rank3_joint_adelic_evaluation_matrix_complete','Brauer_Manin_obstruction_from_full_Br_group_proved','fixed_p_2_branch_excluded','receiver_emptiness_proved']:
        assert cb[k] is False,k
    assert c['route_result']['next_leaf']=='36-09DC_FIXED_P2_RANK3_BRAUER_TWO_PLACE_EVALUATION_MATRIX_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09DB verified: D=(11,t^2+4)_2 is an unramified third Brauer class independent of A,B, witnessed by Q_11 receiver points where A,B stay zero and D varies. Constructed rank is at least 3; full Brauer group remains open. No BM/fixed-p/receiver/endpoint credit.')

if __name__=='__main__': main()
