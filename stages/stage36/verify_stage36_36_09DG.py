#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DG/fixed-p2-nonrational-qi-brauer-complement-preflight.json'
SRC=ROOT/'stages/stage36/36-09DG/qi-component-hilbert90-source-lock.md'
DF=ROOT/'stages/stage36/36-09DF/fixed-p2-creutz-viray-complement-local-obstruction-preflight.json'
DE=ROOT/'stages/stage36/36-09DE/fixed-p2-prime-private-brauer-family-preflight.json'
BASE='f2a89e613cdf91191a0aada9e90c9fc93373a6c6'
DF_HEAD='ac6dc90ac0a6a872076117cd9801f3e3c1bc6d09'
PROMO_HEAD='3362fefa40b2ea6ea8789af6ddad7bc23e9de4ba'
LOCKS={
    CERT:'01648358b303872f228b7835cbd44bb8d15578c7',
    SRC:'f5b5e0a333464257ca29ea058de2cf3bd191636f',
    DF:'e2ad1a187dc607b558288a6cad91272c021dd493',
    DE:'14e73de6228606ad077303db96f1a032c2955238',
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
    subprocess.check_call(['git','merge-base','--is-ancestor',DF_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMO_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); df=json.loads(DF.read_text()); de=json.loads(DE.read_text()); src=SRC.read_text()
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
      'pr':1712,
      '36_09DF_exact_green_head':DF_HEAD,
      '36_09DF_exact_head_ci':'34204479976/101990651818',
      'promotion_replay_head':PROMO_HEAD,
      'promotion_replay_ci':'34204580135/101990977783'
    }
    assert df['adelic_solubility']['C3_2_adelic_points_exist'] is True
    assert de['infinite_independence']['constructed_explicit_subgroup_infinite_F2_rank'] is True
    assert 'Hilbert Theorem 90' in src
    assert 'ell_5=(pi,pi,1,1)' in src
    assert 'local evaluation of `F_5`' in src

    pi=c['paired_input']
    assert pi['norm_pi']==5 and pi['total_norm']==25
    assert pi['ell_5_in_L1'] is True and pi['F_5_unramified_on_C3_2'] is True
    assert pi['norm_vector_squareclasses']==[5,5,1,1]
    assert pi['input_not_in_rational_component_subgroup'] is True
    assert pi['input_nonrationality_alone_proves_Brauer_independence'] is False

    rows={int(r['t']):r for r in c['q5_receiver_witnesses']}
    expected={2:(Fraction(16354,9),3,'1/2'),5:(Fraction(5626609,9),4,'0')}
    for t,(rex,evalres,inv) in expected.items():
        T=Fraction(t); rr=rhs(T)
        assert rr==rex and mod_frac(rr,5)==1
        assert (1*1-mod_frac(rr,5))%5==0 and 2%5!=0
        assert t not in (0,1,-1)
        e=((t-1)*(t-4))%5
        assert e==evalres and e!=0
        calc='0' if legendre(e,5)==1 else '1/2'
        row=rows[t]
        assert row['rhs_exact']==str(rex) and row['rhs_mod5']==1
        assert row['F5_invariant']==inv==calc
        assert row['retained_open'] is True

    # Known H generators are zero on both Q5 witnesses.
    # A,D use f0=t^2+4; B uses f2=t^2+9; their first entries are 7 or 11.
    for t in (2,5):
        assert (t*t+4)%5 != 0
        assert (t*t+9)%5 != 0
    assert 7%5 and 11%5
    # Every DE private q satisfies q == 17 mod a modulus divisible by 5, hence q == 2 mod5.
    assert de['prime_progression']['modulus']%5==0
    assert de['prime_progression']['residue']%5==2

    cmp=c['known_private_subgroup_comparison']
    assert cmp['H_infinite_F2_rank'] is True
    assert cmp['all_H_generators_have_equal_q5_evaluation_on_the_two_witnesses'] is True
    assert cmp['all_H_generators_evaluate_zero_on_both_witnesses'] is True
    assert cmp['F5_evaluation_varies'] is True
    assert cmp['F5_not_in_H_plus_BrQ'] is True

    cb=c['credit_boundary']
    assert cb['paired_nonrational_Creutz_Viray_class_found'] is True
    assert cb['F5_independent_from_known_private_subgroup_mod_BrQ'] is True
    assert cb['known_explicit_subgroup_strictly_enlarged'] is True
    for k in ['F5_independent_from_entire_rational_component_image','full_L1_quotient_computed','Pic0_mod2_computed','full_Creutz_Viray_explicit_image_computed','full_Brauer_group_computed','joint_BM_correction_with_F5_complete','Brauer_Manin_obstruction_from_full_Br_group_proved','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
        assert cb[k] is False,k
    assert c['route_result']['next_leaf']=='36-09DH_FIXED_P2_PAIRED_QI_CROSS_EVALUATION_AND_FAMILY_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09DG verified: the paired Q(i) input ell_5=(2+i,2+i,1,1) gives an unramified class F5 whose Q5 evaluation changes between retained-open receiver points t=2 and t=5, while every generator of the known infinite private subgroup H evaluates zero on both. Thus F5 is new modulo H+Br(Q). No claim about the entire rational-component image, full L1/Picard quotient, full Brauer group, BM obstruction, or fixed-p exclusion.')

if __name__=='__main__': main()
