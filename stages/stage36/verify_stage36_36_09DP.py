#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DP/fixed-p2-global-2primary-brauer-q2-localization-image-preflight.json'
SRC=ROOT/'stages/stage36/36-09DP/global-q2-2primary-weil-chatelet-localization-source-lock.md'
DO=ROOT/'stages/stage36/36-09DO/fixed-p2-2primary-full-brauer-relevance-boundary-preflight.json'
DOSRC=ROOT/'stages/stage36/36-09DO/full-2primary-q2-formal-neighborhood-boundary-source-lock.md'
DNSRC=ROOT/'stages/stage36/36-09DN/full-br2-local-common-neighborhood-source-lock.md'
BASE='538913633330a8414c87931d3c52f93e4aaf5d0f'
DO_GREEN='a1a88d5171045547da44279bb1c144f536233e55'
DO_REPLAY='055df2a859d4af5a76d09ecbad371bd39add412f'
LOCKS={
 CERT:'ca4e238820ee5c1f5850ac99e5995e71c7d68eba',
 SRC:'d9e081ac00c1b0267c970ba1ab2c0932d0a51425',
 DO:'db5368da5162014e8fae767c778d6ddb0c2180e0',
 DOSRC:'4529177bbe39401ed93c0395cce66176bf451dc8',
 DNSRC:'60984a1f42b999e770219398690e833b54c8eb0f',
}

def git(*args:str)->str:
 return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
def blob(path:Path)->str:
 return git('hash-object',str(path.relative_to(ROOT)))

def main()->None:
 for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
 for h in [BASE,DO_GREEN,DO_REPLAY]:
  subprocess.check_call(['git','merge-base','--is-ancestor',h,'HEAD'],cwd=ROOT)
 c=json.loads(CERT.read_text()); do=json.loads(DO.read_text())
 assert c['base_main_sha']==BASE
 assert c['batch_parent']['36_09DO_exact_green_head']==DO_GREEN
 assert c['batch_parent']['36_09DO_exact_head_ci']=='34228677867/102069016868'
 assert c['batch_parent']['36_09DO_promotion_replay_head']==DO_REPLAY
 assert c['batch_parent']['36_09DO_promotion_replay_ci']=='34228969368/102069989754'
 assert c['source_locks']['stage36_36_09DN_source']['blob_sha']==LOCKS[DNSRC]
 assert c['source_locks']['stage36_36_09DO']['blob_sha']==LOCKS[DO]
 assert c['source_locks']['stage36_36_09DO_source']['blob_sha']==LOCKS[DOSRC]
 assert c['source_locks']['global_2primary_localization_source']['blob_sha']==LOCKS[SRC]

 # Parent firewall remains local-only at DO.
 gl0=do['global_localization_firewall']
 assert gl0['global_2primary_Brauer_set_nonempty'] is False
 assert gl0['global_2primary_Brauer_set_empty'] is False
 assert gl0['first_missing_obligation']=='GLOBAL_2PRIMARY_BRAUER_Q2_LOCALIZATION_IMAGE_BOUNDEDNESS_OR_SEPARATION'

 # Exact Brauer/Weil-Chatelet and weak-approximation interface.
 bw=c['brauer_weil_chatelet_identification']
 assert bw['global_nonconstant_brauer_quotient']=='Br(C3_2)/Br(Q) ~= H^1(Q,J)'
 assert bw['local_nonconstant_brauer_quotient']=='Br(C3_2 x Q_2)/Br(Q_2) ~= H^1(Q_2,J)'
 assert bw['compatible_with_localization'] is True
 cw=c['creutz_weak_approximation']
 assert cw['author']=='Brendan Creutz'
 assert cw['doi']=='10.4064/aa154-4-2'
 assert cw['arxiv']=='1009.3546v3'
 assert cw['theorem']=='Theorem 1.3 (weak approximation)'
 assert cw['unconditional_on_Sha_finiteness'] is True
 assert cw['fixed_n_torsion_surjectivity_claimed'] is False

 # Primary-component deduction: full H1 weak approximation implies 2-primary-union surjectivity,
 # without claiming any fixed-level H1[2^n] surjectivity.
 pc=c['primary_component_argument']
 assert pc['global_weil_chatelet_group_is_torsion'] is True
 assert pc['localization_respects_primary_decomposition'] is True
 assert pc['take_S']=='{2}'
 assert pc['full_H1_localization_surjective'] is True
 assert pc['take_2primary_component_of_any_global_preimage'] is True
 assert pc['global_2primary_localization_surjective'] is True
 assert pc['fixed_level_H1_2n_surjectivity_required'] is False
 assert pc['fixed_level_H1_2n_surjectivity_claimed'] is False

 qi=c['q2_localization_image']
 assert qi['map']=='H^1(Q,J)(2) -> H^1(Q_2,J)(2)'
 assert qi['surjective'] is True
 assert qi['global_image_equals_full_local_2primary'] is True
 assert qi['bounded_exponent'] is False
 assert qi['finite_image'] is False
 assert qi['contains_characters_of_order_2n_for_all_n'] is True
 fn=c['formal_neighborhood_upgrade']
 assert fn['DO_local_separating_characters_globalize'] is True
 assert fn['punctured_P0_neighborhood_constant_for_all_global_2primary_classes_exists'] is False
 assert fn['bounded_global_image_DN_style_common_neighborhood_option_survives'] is False

 # Single-place surjectivity is not an adelic Brauer-Manin obstruction.
 af=c['adelic_firewall']
 assert af['single_place_surjectivity_implies_global_Brauer_Manin_obstruction'] is False
 assert af['global_2primary_Brauer_set_nonempty'] is False
 assert af['global_2primary_Brauer_set_empty'] is False
 assert af['fixed_p2_exclusion_obtained'] is False
 assert af['first_missing_obligation']=='GLOBAL_2PRIMARY_ADELIC_ANNIHILATOR_UNDER_SUM_LOCAL_TATE_PAIRINGS'
 assert c['route_result']['next_leaf']=='36-09DQ_FIXED_P2_GLOBAL_2PRIMARY_ADELIC_ANNIHILATOR_PREFLIGHT'
 cb=c['current_credit_boundary']
 assert cb['global_Q2_2primary_localization_image_computed'] is True
 assert cb['global_Q2_2primary_localization_image_is_full'] is True
 assert cb['global_Q2_2primary_localization_image_unbounded'] is True
 for k in ['full_2primary_Brauer_set_nonempty','full_2primary_Brauer_set_empty','full_Brauer_set_nonempty','full_Brauer_set_empty','Brauer_Manin_obstruction_obtained','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
  assert cb[k] is False,k
 for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
 print('36-09DP verified: Creutz weak approximation makes H^1(Q,J)(2) -> H^1(Q2,J)(2) surjective after taking the 2-primary component of a global preimage. Combined with the DO Mattuck/local-duality boundary, the global Q2 image has unbounded dyadic depth and global separating characters exist near P0. Fixed-level H1[2^n] surjectivity and adelic Brauer-Manin/fixed-p/receiver/endpoint credit remain closed.')

if __name__=='__main__': main()
