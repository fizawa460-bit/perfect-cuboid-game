#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DE/fixed-p2-prime-private-brauer-family-preflight.json'
SRC=ROOT/'stages/stage36/36-09DE/prime-private-brauer-family-source-lock.md'
DD=ROOT/'stages/stage36/36-09DD/fixed-p2-creutz-viray-subgroup-completeness-preflight.json'
DC=ROOT/'stages/stage36/36-09DC/fixed-p2-rank3-brauer-two-place-evaluation-matrix-preflight.json'
CW=ROOT/'stages/stage36/36-09CW/bt-literal-non-kummer-divisor-cech-construction-preflight.json'
BASE='f2a89e613cdf91191a0aada9e90c9fc93373a6c6'
DD_HEAD='d1e1e48745b4ea2bdebb7ea69f2beb500f4974df'
PROMO_HEAD='ccc2341a39ec0c3eac61f2e0897acbbf4af13e53'
LOCKS={
    CERT:'14e73de6228606ad077303db96f1a032c2955238',
    SRC:'6314560c7d55b34ef4ce060cb3a85bd79e0181f6',
    DD:'81c580ab09f2fc265f033c51e99f3a553d726f92',
    DC:'4865bd16973ddf0fd746bc4219ea68b8277817b3',
    CW:'a363c230cb44fec6d235eda0720d4fd624b1a87c',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def legendre(a:int,p:int)->int:
    a%=p
    assert a
    v=pow(a,(p-1)//2,p)
    assert v in (1,p-1)
    return 1 if v==1 else -1

def is_prime(n:int)->bool:
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def rhs(t:Fraction)->Fraction:
    return (t*t+4)*(t*t+Fraction(1,4))*(t*t+9)*(t*t+Fraction(1,9))

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',DD_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMO_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); dd=json.loads(DD.read_text()); dc=json.loads(DC.read_text()); cw=json.loads(CW.read_text()); src=SRC.read_text()
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
      'pr':1712,
      '36_09DD_exact_green_head':DD_HEAD,
      '36_09DD_exact_head_ci':'34203063483/101986101989',
      'promotion_replay_head':PROMO_HEAD,
      'promotion_replay_ci':'34203319763/101986947639'
    }
    assert dd['independence_consequence']['constructed_Brauer_subgroup_rank_lower_bound']==4
    assert dc['two_place_joint_control']['image']=='full F2^3'
    assert cw['explicit_family']['literal_unramified_Brauer_family_constructed'] is True
    assert 'Dirichlet' in src and 'infinitely many primes' in src and 'Quadratic reciprocity' in src

    pp=c['prime_progression']
    M=5*13*29*37*41
    assert M==2859545==pp['modulus']
    assert math.gcd(17,M)==1==pp['gcd_residue_modulus']
    assert pp['Dirichlet_infinitely_many_primes'] is True

    # The progression fixes the relevant quadratic characters because every
    # modulus prime is 1 mod 4, so reciprocity reduces (r/q) to (q/r).
    expected={5:-1,13:1,29:-1,37:-1,41:-1}
    for r,s in expected.items():
        assert r%4==1
        assert legendre(17,r)==s
    fd=c['fixed_character_data']
    assert [fd[f'Legendre_{r}'] for r in [5,13,29,37,41]]==[expected[r] for r in [5,13,29,37,41]]

    r3=rhs(Fraction(3)); r4=rhs(Fraction(4))
    assert r3==19721==13*37*41
    assert r4==Fraction(1178125,9)==Fraction((5**5)*13*29,3**2)
    assert expected[13]*expected[37]*expected[41]==1
    assert expected[5]*expected[13]*expected[29]==1
    assert expected[13]==1 and expected[5]==-1

    # Concrete progression sanity beyond q=17; the proof of infinitude is the
    # source-locked Dirichlet theorem, not this finite check.
    q=11438197
    assert q%M==17 and is_prime(q)
    for r,s in expected.items(): assert legendre(r,q)==s
    for T in [Fraction(3),Fraction(4)]:
        rr=rhs(T)
        assert legendre(rr.numerator,q)*legendre(rr.denominator,q)==1
    assert legendre(13,q)==1 and legendre(20,q)==-1

    pf=c['private_family']; ii=c['infinite_independence']; bd=c['block_diagonal_adelic_control']
    assert pf['each_class_unramified_by_CW'] is True
    assert pf['q_local_t_values']==[3,4]
    assert pf['q_local_receiver_points_exist_by_Hensel'] is True
    assert pf['E_q_invariants_at_t3_t4']==['0','1/2']
    assert pf['all_prior_distinct_prime_first_entry_classes_evaluate_zero_on_q_witnesses'] is True
    assert ii['private_classes_pairwise_independent_mod_BrQ'] is True
    assert ii['private_classes_independent_from_A_B_D_mod_BrQ'] is True
    assert ii['Creutz_Viray_explicit_image_contains_infinite_F2_independent_set'] is True
    assert ii['constructed_explicit_subgroup_infinite_F2_rank'] is True
    assert ii['full_Creutz_Viray_explicit_image_computed'] is False
    assert ii['full_Brauer_group_computed'] is False
    assert bd['every_finite_generated_subgroup_has_full_coordinate_correction_image'] is True
    assert bd['infinite_private_subgroup_can_supply_Brauer_Manin_obstruction_conditional_on_adelic_solubility'] is False

    cb=c['current_credit_boundary']
    assert cb['infinite_rank_Creutz_Viray_explicit_subgroup_constructed'] is True
    assert cb['infinite_private_subgroup_BM_obstruction_disproved_conditional_on_adelic_solubility'] is True
    for k in ['full_Creutz_Viray_explicit_image_computed','private_subgroup_equals_full_explicit_image','full_Brauer_group_computed','Brauer_Manin_obstruction_from_full_Br_group_proved','C3_2_adelic_points_exist','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
        assert cb[k] is False,k
    assert c['route_result']['next_leaf']=='36-09DF_FIXED_P2_CREUTZ_VIRAY_COMPLEMENT_AND_LOCAL_OBSTRUCTION_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09DE verified: Dirichlet + quadratic reciprocity produce infinitely many private primes q congruent 17 mod 2859545. The classes E_q=(q,t^2+4)_2 form an infinite F2-independent Creutz-Viray explicit subgroup, with block-diagonal local correction against A,B,D and each E_q. This subgroup cannot BM-obstruct conditional on adelic solubility. Full explicit image/full Brauer group remain open.')

if __name__=='__main__': main()
