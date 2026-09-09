#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DQ/fixed-p2-global-2primary-adelic-annihilator-preflight.json'
SRC=ROOT/'stages/stage36/36-09DQ/global-2primary-adelic-annihilator-proselmer-source-lock.md'
DP=ROOT/'stages/stage36/36-09DP/fixed-p2-global-2primary-brauer-q2-localization-image-preflight.json'
DPSRC=ROOT/'stages/stage36/36-09DP/global-q2-2primary-weil-chatelet-localization-source-lock.md'
DNSRC=ROOT/'stages/stage36/36-09DN/full-br2-local-common-neighborhood-source-lock.md'
BASE='538913633330a8414c87931d3c52f93e4aaf5d0f'
DP_GREEN='ac5d65e7cd148db91e41706cc213c350f981e2f4'
DP_REPLAY='0c2fe56af961728ab658665fbbf1d4d71eac05f0'
LOCKS={
 CERT:'4c41228d23f9088bfbea8b68c94b2a26948f8691',
 SRC:'71829ec5e0af601605f1f93c5f3a3fec4cae2102',
 DP:'ca4e238820ee5c1f5850ac99e5995e71c7d68eba',
 DPSRC:'d9e081ac00c1b0267c970ba1ab2c0932d0a51425',
 DNSRC:'60984a1f42b999e770219398690e833b54c8eb0f',
}

def git(*args:str)->str:
 return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
def blob(path:Path)->str:
 return git('hash-object',str(path.relative_to(ROOT)))

def main()->None:
 for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
 for h in [BASE,DP_GREEN,DP_REPLAY]:
  subprocess.check_call(['git','merge-base','--is-ancestor',h,'HEAD'],cwd=ROOT)
 c=json.loads(CERT.read_text()); dp=json.loads(DP.read_text())
 assert c['base_main_sha']==BASE
 assert c['batch_parent']['36_09DP_exact_green_head']==DP_GREEN
 assert c['batch_parent']['36_09DP_exact_head_ci']=='34230132989/102073890507'
 assert c['batch_parent']['36_09DP_promotion_replay_head']==DP_REPLAY
 assert c['batch_parent']['36_09DP_promotion_replay_ci']=='34230446625/102074937357'
 assert c['source_locks']['stage36_36_09DN_source']['blob_sha']==LOCKS[DNSRC]
 assert c['source_locks']['stage36_36_09DP']['blob_sha']==LOCKS[DP]
 assert c['source_locks']['stage36_36_09DP_source']['blob_sha']==LOCKS[DPSRC]
 assert c['source_locks']['global_2primary_adelic_annihilator_source']['blob_sha']==LOCKS[SRC]

 # Parent DP is exact-green and still does not decide the adelic BM sum.
 assert dp['q2_localization_image']['surjective'] is True
 assert dp['q2_localization_image']['global_image_equals_full_local_2primary'] is True
 assert dp['adelic_firewall']['global_2primary_Brauer_set_nonempty'] is False
 assert dp['adelic_firewall']['global_2primary_Brauer_set_empty'] is False

 fc=c['fixed_curve']
 assert fc['genus']==3 and fc['jacobian_dimension']==3
 assert fc['principally_polarized'] is True
 assert fc['dual_identification']=='J^t ~= J'
 gt=c['generalized_cassels_tate']
 assert gt['doi']=='10.4310/MRL.2007.v14.n2.a11'
 assert gt['arxiv']=='math/0608587'
 assert gt['result']=='Main Theorem'
 assert gt['m']==2
 assert gt['sha_finiteness_required'] is False
 assert gt['exact_sequence']=='0 -> T_2 Sel(J) -> product_v J(Q_v)^hat_2 -> H^1(Q,J)(2)^D -> Sha(J)(2)^D -> 0'

 at=c['adelic_tate_map']
 assert at['domain']=='product_v J(Q_v)^hat_2'
 assert at['target']=='H^1(Q,J)(2)^D'
 assert at['kernel']=='image(T_2 Sel(J))'
 assert at['global_2primary_adelic_annihilator_computed'] is True
 assert at['annihilator_equals_Mordell_Weil_closure_unconditionally'] is False
 bm=c['brauer_manin_translation']
 assert bm['abel_jacobi_map']=='iota(P)=[P-P0]'
 assert bm['global_reference_sum_zero'] is True
 assert bm['completed_adelic_curve_image']=='iota_hat_2(U_ret(A_Q))'
 assert bm['orthogonality_equivalence']=='(P_v) is orthogonal to Br(C3_2)(2) iff iota_hat_2((P_v)) lies in image(T_2 Sel(J))'
 assert bm['intersection_problem']=='iota_hat_2(U_ret(A_Q)) intersect image(T_2 Sel(J))'

 mw=c['mordell_weil_firewall']
 assert mw['JQ_2adic_completion_contained_in_T2Sel'] is True
 assert mw['extra_part_measured_by_T2Sha'] is True
 assert mw['Sha_2primary_finiteness_proved'] is False
 assert mw['T2Sha_vanishes_proved'] is False
 assert mw['T2Sel_equals_JQ_2adic_completion_proved'] is False
 fr=c['finite_level_route']
 assert fr['tower'][:3]==['Sel_2(J)','Sel_4(J)','Sel_8(J)']
 assert fr['must_test_curve_image_mod_2n_against_localized_Selmer_image'] is True
 assert fr['inverse_compatibility_required'] is True
 assert fr['single_finite_level_hit_suffices_for_proSelmer_membership'] is False
 assert c['route_result']['next_leaf']=='36-09DR_FIXED_P2_PROSELMER_CURVE_INTERSECTION_PREFLIGHT'
 cb=c['current_credit_boundary']
 assert cb['global_2primary_adelic_annihilator_computed'] is True
 assert cb['global_2primary_adelic_annihilator']=='image(T_2 Sel(J))'
 for k in ['full_2primary_Brauer_set_nonempty','full_2primary_Brauer_set_empty','Brauer_Manin_obstruction_obtained','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
  assert cb[k] is False,k
 for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
 print('36-09DQ verified: unconditional generalized Cassels-Tate duality identifies the global 2-primary adelic annihilator with image(T_2 Sel(J)). The retained-open Br(2) problem is exactly the intersection of the completed adelic Abel-Jacobi curve image with that pro-Selmer image. No Sha-finiteness/Mordell-Weil-collapse, BM, fixed-p, receiver, or endpoint credit is granted.')

if __name__=='__main__': main()
