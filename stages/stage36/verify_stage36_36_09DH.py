#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DH/fixed-p2-paired-qi-cross-evaluation-family-preflight.json'
DG=ROOT/'stages/stage36/36-09DG/fixed-p2-nonrational-qi-brauer-complement-preflight.json'
SRC=ROOT/'stages/stage36/36-09DG/qi-component-hilbert90-source-lock.md'
DE=ROOT/'stages/stage36/36-09DE/fixed-p2-prime-private-brauer-family-preflight.json'
DC=ROOT/'stages/stage36/36-09DC/fixed-p2-rank3-brauer-two-place-evaluation-matrix-preflight.json'
DF=ROOT/'stages/stage36/36-09DF/fixed-p2-creutz-viray-complement-local-obstruction-preflight.json'
BASE='f2a89e613cdf91191a0aada9e90c9fc93373a6c6'
DG_HEAD='d9c8b2714f249971c2353681fb90d706f7d69514'
PROMO_HEAD='e026ec1a5760ada2e555074b562c725def3dfbd5'
LOCKS={
    CERT:'03df0d6518259ed31d934161c33532e084c01936',
    DG:'01648358b303872f228b7835cbd44bb8d15578c7',
    SRC:'f5b5e0a333464257ca29ea058de2cf3bd191636f',
    DE:'14e73de6228606ad077303db96f1a032c2955238',
    DC:'4865bd16973ddf0fd746bc4219ea68b8277817b3',
    DF:'e2ad1a187dc607b558288a6cad91272c021dd493',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',DG_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMO_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); dg=json.loads(DG.read_text()); de=json.loads(DE.read_text()); dc=json.loads(DC.read_text()); df=json.loads(DF.read_text()); src=SRC.read_text()
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
      'pr':1712,
      '36_09DG_exact_green_head':DG_HEAD,
      '36_09DG_exact_head_ci':'34207109875/101999074076',
      'promotion_replay_head':PROMO_HEAD,
      'promotion_replay_ci':'34207290275/101999672833'
    }
    assert dg['known_private_subgroup_comparison']['F5_not_in_H_plus_BrQ'] is True
    assert de['block_diagonal_adelic_control']['infinite_private_subgroup_can_supply_Brauer_Manin_obstruction_conditional_on_adelic_solubility'] is False
    assert dc['two_place_joint_control']['image']=='full F2^3'
    assert df['adelic_solubility']['C3_2_adelic_points_exist'] is True
    assert 'At 5, `Q(i) tensor Q_5` splits' in src

    fx=c['F5_cross_evaluation']
    # Q7: f0=t^2+4 and f1=t^2+1/4 are units on every A/B correction witness.
    q7=[7,8,2,3]; inv4_7=pow(4,-1,7)
    assert [((t*t+4)%7) for t in q7]==fx['Q7_f0_residues']==[4,5,1,6]
    assert [((t*t+inv4_7)%7) for t in q7]==fx['Q7_f1_residues']==[2,3,6,4]
    assert all(x for x in fx['Q7_f0_residues']+fx['Q7_f1_residues'])
    assert fx['F5_zero_on_all_Q7_H_witnesses'] is True

    # Q11: same unit check on the D-control witnesses.
    q11=[4,3]; inv4_11=pow(4,-1,11)
    assert [((t*t+4)%11) for t in q11]==fx['Q11_f0_residues']==[9,2]
    assert [((t*t+inv4_11)%11) for t in q11]==fx['Q11_f1_residues']==[8,1]
    assert all(x for x in fx['Q11_f0_residues']+fx['Q11_f1_residues'])
    assert fx['F5_zero_on_all_Q11_H_witnesses'] is True

    # DE private q witnesses t=3,4: f0 values 13,20 and f1 values 37/4,65/4.
    M=de['prime_progression']['modulus']; a=de['prime_progression']['residue']
    assert M==2859545 and a==17
    for r in [5,13,37]:
        assert M%r==0 and a%r!=0
    assert fx['private_q_f0_values']==['13','20']
    assert fx['private_q_f1_values']==['37/4','65/4']
    assert fx['private_progression_excludes_prime_divisors_of_these_values'] is True
    assert fx['F5_zero_on_all_private_q_H_witnesses'] is True

    # At Q5, the F5-control pair leaves every H coordinate zero.
    hc=c['H_cross_evaluation_at_Q5']
    assert hc['F5_control_t_values']==[2,5]
    assert hc['F5_invariants']==['1/2','0']
    for t in [2,5]:
        assert (t*t+4)%5!=0 and (t*t+9)%5!=0
    assert 7%5 and 11%5 and a%5==2
    assert hc['A_B_D_zero_on_both'] is True
    assert hc['all_private_Eq_zero_on_both'] is True
    assert hc['all_H_generators_zero_on_both'] is True

    bd=c['block_diagonal_control']; ad=c['adelic_consequence']
    assert bd['all_selected_cross_evaluations_zero'] is True
    assert bd['every_finite_generated_subgroup_of_G_has_full_coordinate_correction_image'] is True
    assert bd['infinite_coordinate_correction_extends_DE'] is True
    assert ad['C3_2_adelic_points_exist'] is True
    assert ad['C3_2_adelic_points_orthogonal_to_G_exist'] is True
    assert ad['G_can_supply_Brauer_Manin_obstruction'] is False
    assert ad['does_not_control_classes_outside_G'] is True

    cb=c['credit_boundary']
    assert cb['F5_cross_evaluation_matrix_complete_on_known_correction_witnesses'] is True
    assert cb['known_private_plus_F5_subgroup_BM_set_nonempty'] is True
    for k in ['paired_QI_family_infinite_or_systematic','F5_outside_entire_rational_component_image','full_L1_quotient_computed','Pic0_mod2_computed','full_Creutz_Viray_explicit_image_computed','full_Brauer_group_computed','Brauer_Manin_obstruction_from_full_Br_group_proved','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
        assert cb[k] is False,k
    assert c['route_result']['next_leaf']=='36-09DI_FIXED_P2_F5_RATIONAL_COMPONENT_RELATION_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09DH verified: F5 is zero on the Q7/Q11/private-q H-correction witnesses, while H is zero on the Q5 F5-control pair. Thus the DE block-diagonal correction extends to G=H+<F5>; with DF adelic solubility, C3_2(A_Q)^G is nonempty. No claim that F5 lies outside the entire rational-component image, no full L1/Picard/Brauer control, and no BM/fixed-p/receiver credit.')

if __name__=='__main__': main()
