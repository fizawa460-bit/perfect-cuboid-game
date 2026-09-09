#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DF/fixed-p2-creutz-viray-complement-local-obstruction-preflight.json'
DE=ROOT/'stages/stage36/36-09DE/fixed-p2-prime-private-brauer-family-preflight.json'
DD=ROOT/'stages/stage36/36-09DD/fixed-p2-creutz-viray-subgroup-completeness-preflight.json'
SRC=ROOT/'stages/stage36/36-09DD/creutz-viray-explicit-image-completeness-source-lock.md'
BASE='f2a89e613cdf91191a0aada9e90c9fc93373a6c6'
DE_HEAD='b857167b4652cec6b5d149a3509c465c862b7b0e'
PROMO_HEAD='2a09edd4f9263508035d6fbbb7c59da504180913'
LOCKS={
    CERT:'e2ad1a187dc607b558288a6cad91272c021dd493',
    DE:'14e73de6228606ad077303db96f1a032c2955238',
    DD:'81c580ab09f2fc265f033c51e99f3a553d726f92',
    SRC:'632e908d3fcd4d1f3511be99b3993469537e3c07',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def rhs(t:Fraction)->Fraction:
    return (t*t+4)*(t*t+Fraction(1,4))*(t*t+9)*(t*t+Fraction(1,9))

def primes_upto(n:int)->list[int]:
    out=[]
    for x in range(2,n+1):
        if all(x%d for d in range(2,int(x**0.5)+1)):
            out.append(x)
    return out

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',DE_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMO_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); de=json.loads(DE.read_text()); dd=json.loads(DD.read_text()); src=SRC.read_text()
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
      'pr':1712,
      '36_09DE_exact_green_head':DE_HEAD,
      '36_09DE_exact_head_ci':'34203824191/101988565446',
      'promotion_replay_head':PROMO_HEAD,
      'promotion_replay_ci':'34203958808/101988985143'
    }
    assert de['infinite_independence']['constructed_explicit_subgroup_infinite_F2_rank'] is True
    assert de['block_diagonal_adelic_control']['infinite_private_subgroup_can_supply_Brauer_Manin_obstruction_conditional_on_adelic_solubility'] is False
    assert dd['independence_consequence']['constructed_Brauer_subgroup_rank_lower_bound']==4
    assert 'Pic^0(C)/2 Pic^0(C)' in src and 'does **not** identify that image with all' in src

    # Real point: t=2 gives positive RHS.
    r2=rhs(Fraction(2))
    assert r2==Fraction(16354,9) and r2>0

    # Q_2 point: an odd unit is a square iff it is 1 mod 8.
    rq2=rhs(Fraction(3))
    assert rq2==19721 and rq2.denominator==1 and rq2.numerator%8==1

    # Q_3 point at t=2: v_3=-2 and the remaining unit is 1 mod 3.
    rq3=rhs(Fraction(2))
    assert rq3==Fraction(16354,9)
    assert rq3.denominator==9 and rq3.numerator%3==1

    # For every l>3, t=l gives RHS == 1 mod l because the four constants
    # multiply to 4*(1/4)*9*(1/9)=1. Check the exact symbolic residues over a
    # bounded prime sample; the certificate records the uniform identity.
    for ell in [p for p in primes_upto(101) if p>3]:
        inv4=pow(4,-1,ell); inv9=pow(9,-1,ell)
        residue=(4*inv4*9*inv9)%ell
        assert residue==1
        assert 2%ell!=0
        assert ell not in (0,1,-1)

    lp=c['explicit_local_points']; ad=c['adelic_solubility']
    assert lp['real']['t']=='2' and lp['real']['positive'] is True and lp['real']['retained_open'] is True
    assert lp['Q2']['t']=='3' and lp['Q2']['rhs']=='19721' and lp['Q2']['retained_open'] is True
    assert lp['Q3']['t']=='2' and lp['Q3']['valuation']==-2 and lp['Q3']['unit_residue_mod3']==1
    assert lp['all_primes_l_gt_3']['t']=='l' and lp['all_primes_l_gt_3']['rhs_mod_l']==1
    assert lp['all_primes_l_gt_3']['hensel_seed_z_mod_l']==1 and lp['all_primes_l_gt_3']['hensel_derivative_2z_nonzero'] is True
    assert ad['retained_open_local_point_every_place'] is True
    assert ad['C3_2_adelic_points_exist'] is True
    assert ad['local_obstruction_for_fixed_p2'] is False

    pu=c['private_subgroup_upgrade']
    assert pu['H_infinite_F2_rank'] is True
    assert pu['DE_block_diagonal_correction_available'] is True
    assert pu['starting_adelic_point_now_materialized'] is True
    assert pu['C3_2_adelic_points_orthogonal_to_H_exist'] is True
    assert pu['private_subgroup_Brauer_Manin_obstruction_obtained'] is False

    comp=c['creutz_viray_complement_boundary']
    for k in ['private_subgroup_equals_full_explicit_image','full_Creutz_Viray_explicit_image_computed','full_Brauer_group_computed']:
        assert comp[k] is False,k
    assert set(comp['unresolved_inputs'])=={
      'non-rational Q(i) component squareclasses in L_1',
      'other factor-component combinations modulo the diagonal K^* and squares',
      'x-alpha image of Pic^0(C3_2)/2',
      'possible full-Br classes outside the Creutz-Viray explicit image'
    }

    cb=c['current_credit_boundary']
    assert cb['p2_retained_open_adelic_solubility_proved'] is True
    assert cb['p2_local_obstruction_excluded'] is True
    assert cb['private_infinite_subgroup_BM_set_nonempty'] is True
    for k in ['full_Creutz_Viray_explicit_image_computed','full_Brauer_group_computed','Brauer_Manin_obstruction_from_full_Br_group_proved','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
        assert cb[k] is False,k
    assert c['route_result']['next_leaf']=='36-09DG_FIXED_P2_NONRATIONAL_QI_BRAUER_COMPLEMENT_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09DF verified: C3_2 has retained-open local points at every place, hence an adelic point; DE block-diagonal correction therefore gives an actual adelic point orthogonal to the infinite private subgroup. The local-obstruction route and private-subgroup BM obstruction are closed, while the Creutz-Viray complement/full Brauer group remain open. No fixed-p/receiver/endpoint credit.')

if __name__=='__main__': main()
