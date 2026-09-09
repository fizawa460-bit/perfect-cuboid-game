#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DI/fixed-p2-f5-rational-component-relation-preflight.json'
DH=ROOT/'stages/stage36/36-09DH/fixed-p2-paired-qi-cross-evaluation-family-preflight.json'
SRC=ROOT/'stages/stage36/36-09DG/qi-component-hilbert90-source-lock.md'
CW=ROOT/'stages/stage36/36-09CW/bt-literal-non-kummer-divisor-cech-construction-preflight.json'
COMP=ROOT/'stages/stage36/36-09DD/creutz-viray-explicit-image-completeness-source-lock.md'
BASE='f2a89e613cdf91191a0aada9e90c9fc93373a6c6'
DH_HEAD='49f4051ebabb7e0939713082cd28e5143ca5dc77'
PROMO_HEAD='4ae5f513c98669610ebb0871512dedad18b24b1d'
LOCKS={
    CERT:'52e860e51905f3b3ecc0e22b23791a0e8a33e0fc',
    DH:'03df0d6518259ed31d934161c33532e084c01936',
    SRC:'f5b5e0a333464257ca29ea058de2cf3bd191636f',
    CW:'a363c230cb44fec6d235eda0720d4fd624b1a87c',
    COMP:'632e908d3fcd4d1f3511be99b3993469537e3c07',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def legendre5(a:int)->str:
    a%=5
    assert a
    return '0' if a in (1,4) else '1/2'

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',DH_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMO_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); dh=json.loads(DH.read_text()); cw=json.loads(CW.read_text()); src=SRC.read_text(); comp=COMP.read_text()
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
      'pr':1712,
      '36_09DH_exact_green_head':DH_HEAD,
      '36_09DH_exact_head_ci':'34207729292/102001120783',
      'promotion_replay_head':PROMO_HEAD,
      'promotion_replay_ci':'34207968704/102001896485'
    }
    assert dh['adelic_consequence']['C3_2_adelic_points_orthogonal_to_G_exist'] is True
    assert 'local evaluation of `F_5`' in src
    assert 'A_d0=(d,t^2+p^2)_2' in cw['explicit_family']['literal_classes']
    assert 'Pic^0(C)/2 Pic^0(C)' in comp

    cc=c['classes_compared']
    assert cc['paired_class']=='F5=gamma(2+i,2+i,1,1)'
    assert cc['rational_component_class']=='R5=(5,t^2+4)_2'
    assert cc['both_unramified_on_C3_2'] is True
    assert cc['input_representatives_distinct_before_Picard_quotient'] is True
    assert cc['equality_or_difference_mod_BrQ_after_Picard_quotient_known'] is False

    qi=c['Q5_evaluation_identity']
    for t in range(5):
        assert (t*t+4-(t-1)*(t-4))%5==0
    assert qi['therefore_Q5_evaluation_functions_identical_on_common_unit_domain'] is True
    assert qi['DG_witness_t_values']==[2,5]
    fvals=[]; rvals=[]
    for t in [2,5]:
        f=((t-1)*(t-4))%5
        r=(t*t+4)%5
        assert f==r and f!=0
        fvals.append(legendre5(f)); rvals.append(legendre5(r))
    assert fvals==rvals==qi['F5_invariants']==qi['R5_invariants']==['1/2','0']
    assert qi['DG_Q5_witness_separates_F5_from_R5'] is False

    qb=c['quotient_boundary']
    for k in ['Pic0_C3_2_mod2_computed','x_alpha_Picard_image_computed','full_L1_quotient_computed','F5_minus_R5_in_x_alpha_Picard_image_decided','repo_search_found_existing_exact_C3_2_Picard_relation_adapter']:
        assert qb[k] is False,k

    cb=c['credit_boundary']
    assert cb['Q5_indistinguishability_with_R5_proved'] is True
    for k in ['F5_outside_entire_rational_component_image','F5_inside_rational_component_image','F5_equals_R5_mod_BrQ','Pic0_mod2_computed','full_L1_quotient_computed','full_Creutz_Viray_explicit_image_computed','full_Brauer_group_computed','Brauer_Manin_obstruction_from_full_Br_group_proved','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
        assert cb[k] is False,k
    assert c['route_result']['next_leaf']=='36-09DJ_FIXED_P2_F5_MINUS_R5_EXPLICIT_CORESTRICTION_OR_PICARD_RELATION_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09DI verified: on the common Q5 unit domain, F5 and the rational-component class R5=(5,t^2+4)_2 have identical evaluation functions because t^2+4=(t-1)(t-4) mod5. The DG witness therefore cannot prove F5 lies outside the full rational-component image. The missing obligation is the x-alpha Picard relation / explicit corestriction difference. No full L1/Brauer/BM/fixed-p/receiver credit.')

if __name__=='__main__': main()
