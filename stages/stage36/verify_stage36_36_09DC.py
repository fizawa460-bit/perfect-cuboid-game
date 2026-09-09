#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DC/fixed-p2-rank3-brauer-two-place-evaluation-matrix-preflight.json'
DA=ROOT/'stages/stage36/36-09DA/fixed-p2-second-independent-brauer-evaluation-matrix-preflight.json'
DB=ROOT/'stages/stage36/36-09DB/fixed-p2-hyperelliptic-brauer-rank-third-class-preflight.json'
BASE='f2a89e613cdf91191a0aada9e90c9fc93373a6c6'
DB_HEAD='83d1f209f85ef747963f05a7b177c783b76142bd'
PROMO_HEAD='ded318a863f6e0515c2d9961dc6495a1af63d7bd'
LOCKS={
    CERT:'4865bd16973ddf0fd746bc4219ea68b8277817b3',
    DA:'8f286f71e828c18e19d65721ca5b3728650f680f',
    DB:'fbdf20fd4c4f4f338d31a55a2a1dd0786ca968c8',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def bit(s:str)->int:
    return 0 if s=='0' else 1

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',DB_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMO_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); da=json.loads(DA.read_text()); db=json.loads(DB.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
      'pr':1712,
      '36_09DB_exact_green_head':DB_HEAD,
      '36_09DB_exact_head_ci':'34202180603/101983301546',
      'promotion_replay_head':PROMO_HEAD,
      'promotion_replay_ci':'34202292960/101983647924'
    }
    assert da['joint_image']['equals_full_F2_squared'] is True
    assert db['third_independence_consequence']['A_B_D_independent_in_BrC_mod_BrQ'] is True

    q7=c['q7_control']; q11=c['q11_control']
    assert q7['A_B_evaluation_image']=='full F2^2'
    assert q7['D_invariant_on_all_four_witnesses']=='0'
    assert q11['A_invariant_on_both']=='0' and q11['B_invariant_on_both']=='0'
    assert q11['D_invariants']==['0','1/2']

    plane={tuple(bit(x) for x in row) for row in q7['available_triples']}
    line={tuple(bit(x) for x in row) for row in q11['available_triples']}
    assert plane=={(0,0,0),(1,1,0),(0,1,0),(1,0,0)}
    assert line=={(0,0,0),(0,0,1)}
    total={tuple(a[i]^b[i] for i in range(3)) for a in plane for b in line}
    assert len(total)==8 and total=={(a,b,d) for a in (0,1) for b in (0,1) for d in (0,1)}

    jc=c['two_place_joint_control']
    assert jc['image']=='full F2^3' and jc['image_cardinality']==8
    assert jc['rank3_joint_adelic_evaluation_matrix_complete'] is True
    ad=c['adelic_consequence']
    assert ad['rank3_constructed_subgroup_can_supply_Brauer_Manin_obstruction'] is False
    assert ad['does_not_prove_adelic_solubility'] is True
    assert ad['does_not_compute_full_Brauer_group'] is True
    assert ad['does_not_rule_out_fourth_or_other_independent_class'] is True

    cb=c['current_credit_boundary']
    assert cb['rank3_joint_adelic_evaluation_matrix_complete'] is True
    assert cb['rank3_constructed_subgroup_BM_obstruction_disproved_conditional_on_adelic_solubility'] is True
    for k in ['full_Brauer_group_computed','A_B_D_span_full_relevant_Brauer_group','Brauer_Manin_obstruction_from_full_Br_group_proved','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
        assert cb[k] is False,k
    assert c['route_result']['next_leaf']=='36-09DD_FIXED_P2_CREUTZ_VIRAY_SUBGROUP_COMPLETENESS_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09DC verified: Q7 controls A,B with D=0 and Q11 controls D with A=B=0, so the two-place evaluation image of G=<A,B,D> is all F2^3. Whenever an adelic point exists, a G-orthogonal adelic point exists. Full Brauer-group completeness remains open; no BM/fixed-p/receiver/endpoint credit.')

if __name__=='__main__': main()
